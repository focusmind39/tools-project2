/*
  Base64 Image Encoder Tool Logic
  Reads files locally in-browser using HTML5 FileReader.
*/

document.addEventListener("DOMContentLoaded", () => {
  const dropArea = document.getElementById("image-drop-zone");
  const fileInput = document.getElementById("image-file-input");
  
  const previewWrapper = document.getElementById("preview-wrapper");
  const previewImage = document.getElementById("image-preview");
  const imgMeta = document.getElementById("image-meta-info");

  const rawBox = document.getElementById("base64-raw");
  const htmlBox = document.getElementById("base64-html");
  const cssBox = document.getElementById("base64-css");

  const copyRaw = document.getElementById("btn-copy-raw");
  const copyHtml = document.getElementById("btn-copy-html");
  const copyCss = document.getElementById("btn-copy-css");
  
  const clearBtn = document.getElementById("btn-clear-encoder");

  // Drag and Drop Events
  if (dropArea && fileInput) {
    dropArea.addEventListener("click", () => fileInput.click());

    ["dragenter", "dragover"].forEach(eventName => {
      dropArea.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropArea.classList.add("dragover");
      }, false);
    });

    ["dragleave", "drop"].forEach(eventName => {
      dropArea.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropArea.classList.remove("dragover");
      }, false);
    });

    dropArea.addEventListener("drop", (e) => {
      const dt = e.dataTransfer;
      const files = dt.files;
      if (files.length > 0) {
        processFile(files[0]);
      }
    });

    fileInput.addEventListener("change", (e) => {
      if (e.target.files.length > 0) {
        processFile(e.target.files[0]);
      }
    });
  }

  // File Processing using FileReader
  const processFile = (file) => {
    if (!file.type.startsWith("image/")) {
      showToast("Please upload an image file.", "error");
      return;
    }

    const reader = new FileReader();
    
    reader.onload = (e) => {
      const dataUrl = e.target.result;
      
      // Update preview
      if (previewImage) previewImage.src = dataUrl;
      if (previewWrapper) previewWrapper.style.display = "flex";
      
      // Update meta info
      const sizeKB = (file.size / 1024).toFixed(2);
      if (imgMeta) {
        imgMeta.textContent = `${file.name} | Size: ${sizeKB} KB | Format: ${file.type}`;
      }

      // Generate Base64 Strings
      // Raw string is the part after the comma
      const commaIndex = dataUrl.indexOf(",");
      const rawBase64 = dataUrl.substring(commaIndex + 1);
      
      const htmlSnippet = `<img src="${dataUrl}" alt="${file.name}">`;
      const cssSnippet = `background-image: url("${dataUrl}");`;

      // Set outputs
      if (rawBox) rawBox.textContent = rawBase64;
      if (htmlBox) htmlBox.textContent = htmlSnippet;
      if (cssBox) cssBox.textContent = cssSnippet;

      showToast("Image encoded successfully!");
    };

    reader.onerror = () => {
      showToast("Error reading file.", "error");
    };

    reader.readAsDataURL(file);
  };

  // Copy Buttons
  const setupCopy = (btn, box, label) => {
    if (btn && box) {
      btn.addEventListener("click", () => {
        const val = box.textContent;
        if (val === "" || val === "-") {
          showToast(`Encode an image first.`, "error");
          return;
        }
        copyToClipboard(val, `${label} copied!`);
      });
    }
  };

  setupCopy(copyRaw, rawBox, "Raw string");
  setupCopy(copyHtml, htmlBox, "HTML code");
  setupCopy(copyCss, cssBox, "CSS code");

  // Clear
  if (clearBtn) {
    clearBtn.addEventListener("click", () => {
      if (fileInput) fileInput.value = "";
      if (previewWrapper) previewWrapper.style.display = "none";
      if (previewImage) previewImage.src = "";
      if (imgMeta) imgMeta.textContent = "";
      
      if (rawBox) rawBox.textContent = "-";
      if (htmlBox) htmlBox.textContent = "-";
      if (cssBox) cssBox.textContent = "-";
      
      showToast("Encoder fields reset!");
    });
  }
});

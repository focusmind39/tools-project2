/*
  URL Encoder & Decoder Tool Logic
*/

document.addEventListener("DOMContentLoaded", () => {
  const urlInput = document.getElementById("url-input-text");
  const urlOutput = document.getElementById("url-output-box");
  
  const encodeBtn = document.getElementById("btn-encode-url");
  const decodeBtn = document.getElementById("btn-decode-url");
  
  const copyBtn = document.getElementById("btn-copy-url");
  const clearBtn = document.getElementById("btn-clear-url");

  const processURL = (action) => {
    const text = urlInput.value;
    if (text === "") {
      showToast("Please enter some text to process.", "error");
      urlOutput.textContent = "";
      return;
    }

    try {
      if (action === "encode") {
        const encoded = encodeURIComponent(text);
        urlOutput.textContent = encoded;
        showToast("URL encoded successfully!");
      } else {
        const decoded = decodeURIComponent(text);
        urlOutput.textContent = decoded;
        showToast("URL decoded successfully!");
      }
    } catch (err) {
      urlOutput.textContent = "Malformed URI. Could not decode: " + err.message;
      showToast("Conversion error. Check query syntax.", "error");
    }
  };

  if (encodeBtn) {
    encodeBtn.addEventListener("click", () => processURL("encode"));
  }

  if (decodeBtn) {
    decodeBtn.addEventListener("click", () => processURL("decode"));
  }

  // Copy
  if (copyBtn && urlOutput) {
    copyBtn.addEventListener("click", () => {
      const result = urlOutput.textContent;
      if (result === "" || result.startsWith("Malformed URI")) {
        showToast("No valid URL result to copy.", "error");
        return;
      }
      copyToClipboard(result, "URL copied to clipboard!");
    });
  }

  // Clear
  if (clearBtn && urlInput) {
    clearBtn.addEventListener("click", () => {
      urlInput.value = "";
      urlOutput.textContent = "";
      showToast("Fields cleared!");
    });
  }
});

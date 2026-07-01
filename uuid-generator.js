/*
  UUID Generator Tool Logic
  Generates cryptographically secure version 4 UUIDs locally.
*/

document.addEventListener("DOMContentLoaded", () => {
  const uuidCount = document.getElementById("uuid-count");
  const uuidUppercase = document.getElementById("uuid-uppercase");
  const uuidBraces = document.getElementById("uuid-braces");
  const uuidNoHyphens = document.getElementById("uuid-no-hyphens");
  
  const uuidOutput = document.getElementById("uuid-output-box");
  const generateBtn = document.getElementById("btn-generate-uuid");
  const copyBtn = document.getElementById("btn-copy-uuid");
  const clearBtn = document.getElementById("btn-clear-uuid");

  // Secure UUID v4 Generation
  const generateUUIDv4 = () => {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      const r = window.crypto.getRandomValues(new Uint8Array(1))[0] % 16;
      const v = c === 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  };

  const processUUIDs = () => {
    const count = parseInt(uuidCount.value, 10) || 1;
    let list = [];

    for (let i = 0; i < count; i++) {
      let uuid = generateUUIDv4();
      
      // Formatting options
      if (uuidNoHyphens.checked) {
        uuid = uuid.replace(/-/g, "");
      }
      
      if (uuidUppercase.checked) {
        uuid = uuid.toUpperCase();
      }
      
      if (uuidBraces.checked) {
        uuid = "{" + uuid + "}";
      }
      
      list.push(uuid);
    }

    if (uuidOutput) {
      uuidOutput.textContent = list.join("\n");
      showToast(`Generated ${count} UUID(s) successfully!`);
    }
  };

  if (generateBtn) {
    generateBtn.addEventListener("click", processUUIDs);
  }

  // Copy
  if (copyBtn && uuidOutput) {
    copyBtn.addEventListener("click", () => {
      const val = uuidOutput.textContent;
      if (val === "" || val === "Click Generate...") {
        showToast("Generate UUIDs first.", "error");
        return;
      }
      copyToClipboard(val, "UUIDs copied to clipboard!");
    });
  }

  // Clear
  if (clearBtn && uuidOutput) {
    clearBtn.addEventListener("click", () => {
      uuidOutput.textContent = "";
      showToast("UUID box cleared!");
    });
  }

  // Initial trigger
  processUUIDs();
});

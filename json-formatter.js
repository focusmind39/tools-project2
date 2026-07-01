/*
  JSON Formatter & Validator Tool Logic
*/

document.addEventListener("DOMContentLoaded", () => {
  const jsonInput = document.getElementById("json-input");
  const jsonOutput = document.getElementById("json-output-box");
  const indentSelect = document.getElementById("json-indent");
  
  const formatBtn = document.getElementById("btn-format-json");
  const minifyBtn = document.getElementById("btn-minify-json");
  const validateBtn = document.getElementById("btn-validate-json");
  
  const copyBtn = document.getElementById("btn-copy-json");
  const clearBtn = document.getElementById("btn-clear-json");
  
  const statusDisplay = document.getElementById("json-status-msg");

  const getSpaceCount = () => {
    return parseInt(indentSelect.value, 10);
  };

  const setStatus = (msg, type = "success") => {
    if (!statusDisplay) return;
    statusDisplay.textContent = msg;
    statusDisplay.className = "";
    if (type === "success") {
      statusDisplay.style.color = "var(--success)";
      statusDisplay.style.fontWeight = "600";
    } else {
      statusDisplay.style.color = "var(--danger)";
      statusDisplay.style.fontWeight = "600";
    }
  };

  // Format JSON
  const formatJSON = () => {
    const raw = jsonInput.value.trim();
    if (raw === "") {
      setStatus("Input is empty.", "error");
      jsonOutput.textContent = "";
      return;
    }

    try {
      const parsed = JSON.parse(raw);
      const space = getSpaceCount();
      const formatted = JSON.stringify(parsed, null, space);
      jsonOutput.textContent = formatted;
      setStatus("Valid JSON. Formatted successfully!", "success");
    } catch (err) {
      jsonOutput.textContent = err.message;
      setStatus("Invalid JSON. " + err.message, "error");
    }
  };

  // Minify JSON
  const minifyJSON = () => {
    const raw = jsonInput.value.trim();
    if (raw === "") {
      setStatus("Input is empty.", "error");
      jsonOutput.textContent = "";
      return;
    }

    try {
      const parsed = JSON.parse(raw);
      const minified = JSON.stringify(parsed);
      jsonOutput.textContent = minified;
      setStatus("Valid JSON. Minified successfully!", "success");
    } catch (err) {
      jsonOutput.textContent = err.message;
      setStatus("Invalid JSON. " + err.message, "error");
    }
  };

  // Validate JSON
  const validateJSON = () => {
    const raw = jsonInput.value.trim();
    if (raw === "") {
      setStatus("Input is empty.", "error");
      return;
    }

    try {
      JSON.parse(raw);
      setStatus("Valid JSON! No syntax errors found.", "success");
    } catch (err) {
      setStatus("Invalid JSON. " + err.message, "error");
    }
  };

  // Triggers
  if (formatBtn) formatBtn.addEventListener("click", formatJSON);
  if (minifyBtn) minifyBtn.addEventListener("click", minifyJSON);
  if (validateBtn) validateBtn.addEventListener("click", validateJSON);

  // Copy
  if (copyBtn && jsonOutput) {
    copyBtn.addEventListener("click", () => {
      const content = jsonOutput.textContent;
      if (content === "" || content.startsWith("Unexpected") || content.startsWith("JSON")) {
        showToast("No valid formatted JSON to copy.", "error");
        return;
      }
      copyToClipboard(content, "JSON copied to clipboard!");
    });
  }

  // Clear
  if (clearBtn && jsonInput) {
    clearBtn.addEventListener("click", () => {
      jsonInput.value = "";
      jsonOutput.textContent = "";
      if (statusDisplay) statusDisplay.textContent = "";
      showToast("Fields cleared!");
    });
  }
});

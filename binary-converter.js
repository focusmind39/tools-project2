/*
  Binary Converter Tool Logic
*/

document.addEventListener("DOMContentLoaded", () => {
  // 1. Radix Base Translation
  const baseBin = document.getElementById("base-bin");
  const baseOct = document.getElementById("base-oct");
  const baseDec = document.getElementById("base-dec");
  const baseHex = document.getElementById("base-hex");
  const clearBases = document.getElementById("btn-clear-bases");

  const updateAllBases = (value, sourceRadix) => {
    if (isNaN(value)) {
      baseBin.value = "";
      baseOct.value = "";
      baseDec.value = "";
      baseHex.value = "";
      return;
    }

    if (sourceRadix !== 2) baseBin.value = value.toString(2);
    if (sourceRadix !== 8) baseOct.value = value.toString(8);
    if (sourceRadix !== 10) baseDec.value = value.toString(10);
    if (sourceRadix !== 16) baseHex.value = value.toString(16).toUpperCase();
  };

  const setupBaseListener = (element, radix) => {
    if (element) {
      element.addEventListener("input", (e) => {
        const raw = e.target.value.trim();
        if (raw === "") {
          updateAllBases(NaN);
          return;
        }

        const value = parseInt(raw, radix);
        updateAllBases(value, radix);
      });
    }
  };

  setupBaseListener(baseBin, 2);
  setupBaseListener(baseOct, 8);
  setupBaseListener(baseDec, 10);
  setupBaseListener(baseHex, 16);

  if (clearBases) {
    clearBases.addEventListener("click", () => {
      baseBin.value = "";
      baseOct.value = "";
      baseDec.value = "";
      baseHex.value = "";
      showToast("Numeric forms reset!");
    });
  }

  // 2. Text to/from Binary Translation
  const textInput = document.getElementById("txt-input");
  const binOutput = document.getElementById("bin-output");
  const btnTxtToBin = document.getElementById("btn-text-to-bin");
  const btnBinToTxt = document.getElementById("btn-bin-to-text");
  const clearTextBtn = document.getElementById("btn-clear-text-converter");

  if (btnTxtToBin) {
    btnTxtToBin.addEventListener("click", () => {
      const text = textInput.value;
      if (text === "") {
        showToast("Please enter some text.", "error");
        return;
      }

      // Convert characters to binary bits
      const binary = text.split("").map(char => {
        return char.charCodeAt(0).toString(2).padStart(8, '0');
      }).join(" ");

      binOutput.textContent = binary;
      showToast("Converted text to binary!");
    });
  }

  if (btnBinToTxt) {
    btnBinToTxt.addEventListener("click", () => {
      const rawBinary = textInput.value.trim();
      if (rawBinary === "") {
        showToast("Please enter binary bits.", "error");
        return;
      }

      try {
        // Strip spaces, split by 8-bits blocks
        const blocks = rawBinary.replace(/\s+/g, "").match(/.{1,8}/g) || [];
        const decoded = blocks.map(block => {
          const charCode = parseInt(block, 2);
          if (isNaN(charCode)) throw new Error("Invalid binary code.");
          return String.fromCharCode(charCode);
        }).join("");

        binOutput.textContent = decoded;
        showToast("Converted binary to text!");
      } catch (err) {
        binOutput.textContent = "Malformed binary input. Ensure you provide binary characters (0s and 1s).";
        showToast("Decoding error. Check syntax.", "error");
      }
    });
  }

  if (clearTextBtn) {
    clearTextBtn.addEventListener("click", () => {
      textInput.value = "";
      binOutput.textContent = "";
      showToast("Text forms reset!");
    });
  }

  // Copy Buttons
  const setupCopyBtn = (btnId, boxId, label) => {
    const btn = document.getElementById(btnId);
    const box = document.getElementById(boxId);
    if (btn && box) {
      btn.addEventListener("click", () => {
        const val = box.value || box.textContent;
        if (val === "" || val === "-") {
          showToast("Calculate first.", "error");
          return;
        }
        copyToClipboard(val, `${label} copied!`);
      });
    }
  };

  setupCopyBtn("btn-copy-bin", "base-bin", "Binary value");
  setupCopyBtn("btn-copy-oct", "base-oct", "Octal value");
  setupCopyBtn("btn-copy-dec", "base-dec", "Decimal value");
  setupCopyBtn("btn-copy-hex", "base-hex", "Hexadecimal value");
  setupCopyBtn("btn-copy-bin-txt", "bin-output", "Converter output");
});

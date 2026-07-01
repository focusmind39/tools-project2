/*
  Percentage Calculator Tool Logic
  Calculates percentages across three common equations.
*/

document.addEventListener("DOMContentLoaded", () => {
  // Equation 1: What is X% of Y?
  const eq1X = document.getElementById("eq1-x");
  const eq1Y = document.getElementById("eq1-y");
  const eq1Btn = document.getElementById("btn-calc-eq1");
  const eq1Out = document.getElementById("eq1-out");

  if (eq1Btn) {
    eq1Btn.addEventListener("click", () => {
      const x = parseFloat(eq1X.value);
      const y = parseFloat(eq1Y.value);

      if (isNaN(x) || isNaN(y)) {
        showToast("Please enter valid numbers.", "error");
        return;
      }

      const result = (x / 100) * y;
      // Round to 4 decimal places if fractional
      const displayVal = Number(result.toFixed(4)).toString();
      eq1Out.textContent = displayVal;
      showToast("Calculated!");
    });
  }

  // Equation 2: X is what percent of Y?
  const eq2X = document.getElementById("eq2-x");
  const eq2Y = document.getElementById("eq2-y");
  const eq2Btn = document.getElementById("btn-calc-eq2");
  const eq2Out = document.getElementById("eq2-out");

  if (eq2Btn) {
    eq2Btn.addEventListener("click", () => {
      const x = parseFloat(eq2X.value);
      const y = parseFloat(eq2Y.value);

      if (isNaN(x) || isNaN(y)) {
        showToast("Please enter valid numbers.", "error");
        return;
      }

      if (y === 0) {
        showToast("Cannot divide by zero.", "error");
        return;
      }

      const result = (x / y) * 100;
      const displayVal = Number(result.toFixed(4)).toString() + "%";
      eq2Out.textContent = displayVal;
      showToast("Calculated!");
    });
  }

  // Equation 3: Percentage increase/decrease from X to Y?
  const eq3X = document.getElementById("eq3-x");
  const eq3Y = document.getElementById("eq3-y");
  const eq3Btn = document.getElementById("btn-calc-eq3");
  const eq3Out = document.getElementById("eq3-out");

  if (eq3Btn) {
    eq3Btn.addEventListener("click", () => {
      const x = parseFloat(eq3X.value);
      const y = parseFloat(eq3Y.value);

      if (isNaN(x) || isNaN(y)) {
        showToast("Please enter valid numbers.", "error");
        return;
      }

      if (x === 0) {
        showToast("Initial value cannot be zero.", "error");
        return;
      }

      const diff = y - x;
      const percentChange = (diff / x) * 100;
      
      let direction = "increase";
      if (percentChange < 0) {
        direction = "decrease";
      }

      const displayVal = Math.abs(Number(percentChange.toFixed(4))).toString() + "% " + direction;
      eq3Out.textContent = displayVal;
      showToast("Calculated!");
    });
  }

  // Setup separate Copy badge listeners for outputs
  const setupCopyBtn = (btnId, boxId, label) => {
    const btn = document.getElementById(btnId);
    const box = document.getElementById(boxId);
    if (btn && box) {
      btn.addEventListener("click", () => {
        const val = box.textContent;
        if (val === "" || val === "-") {
          showToast("Calculate first.", "error");
          return;
        }
        copyToClipboard(val, `${label} result copied!`);
      });
    }
  };

  setupCopyBtn("btn-copy-eq1", "eq1-out", "Equation 1");
  setupCopyBtn("btn-copy-eq2", "eq2-out", "Equation 2");
  setupCopyBtn("btn-copy-eq3", "eq3-out", "Equation 3");

  // General Reset trigger
  const clearBtn = document.getElementById("btn-clear-percentages");
  if (clearBtn) {
    clearBtn.addEventListener("click", () => {
      if (eq1X) eq1X.value = "";
      if (eq1Y) eq1Y.value = "";
      if (eq1Out) eq1Out.textContent = "-";

      if (eq2X) eq2X.value = "";
      if (eq2Y) eq2Y.value = "";
      if (eq2Out) eq2Out.textContent = "-";

      if (eq3X) eq3X.value = "";
      if (eq3Y) eq3Y.value = "";
      if (eq3Out) eq3Out.textContent = "-";

      showToast("Percentage forms reset!");
    });
  }
});

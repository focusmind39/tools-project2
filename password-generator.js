/*
  Password Generator Tool Logic
*/

document.addEventListener("DOMContentLoaded", () => {
  const lengthSlider = document.getElementById("pw-length");
  const lengthVal = document.getElementById("pw-length-val");
  
  const includeUpper = document.getElementById("pw-upper");
  const includeLower = document.getElementById("pw-lower");
  const includeNumbers = document.getElementById("pw-numbers");
  const includeSymbols = document.getElementById("pw-symbols");
  const excludeSimilar = document.getElementById("pw-similar");

  const passwordOutput = document.getElementById("password-result-box");
  const generateBtn = document.getElementById("btn-generate-pw");
  const copyBtn = document.getElementById("btn-copy-pw");
  const strengthBar = document.getElementById("pw-strength-bar");
  const strengthText = document.getElementById("pw-strength-text");

  // Sync length value display
  if (lengthSlider && lengthVal) {
    lengthSlider.addEventListener("input", (e) => {
      lengthVal.textContent = e.target.value;
    });
  }

  // Cryptographically Secure Password Generator
  const generatePassword = () => {
    const uppercaseChars = "ABCDEFGHJKLMNPQRSTUVWXYZ"; // Similar chars removed by default: I, O
    const lowercaseChars = "abcdefghijkmnopqrstuvwxyz"; // similar chars removed by default: l, o
    const numberChars = "23456789"; // similar chars removed by default: 0, 1
    const symbolChars = "!@#$%^&*()_+-=[]{}|;:,.<>?";

    let charPool = "";
    let requiredTypes = [];

    // Base character pools (adding similarities if not excluded)
    let finalUpper = uppercaseChars;
    let finalLower = lowercaseChars;
    let finalNumbers = numberChars;
    
    if (!excludeSimilar.checked) {
      finalUpper += "IO";
      finalLower += "lo";
      finalNumbers += "01";
    }

    if (includeUpper.checked) {
      charPool += finalUpper;
      requiredTypes.push(finalUpper);
    }
    if (includeLower.checked) {
      charPool += finalLower;
      requiredTypes.push(finalLower);
    }
    if (includeNumbers.checked) {
      charPool += finalNumbers;
      requiredTypes.push(finalNumbers);
    }
    if (includeSymbols.checked) {
      charPool += symbolChars;
      requiredTypes.push(symbolChars);
    }

    if (charPool === "") {
      showToast("Please select at least one character set.", "error");
      return;
    }

    const length = parseInt(lengthSlider.value, 10);
    let password = "";
    
    // Ensure we get at least one of each required type first
    requiredTypes.forEach(typePool => {
      password += getRandomChar(typePool);
    });

    // Fill remaining password length from overall pool
    for (let i = password.length; i < length; i++) {
      password += getRandomChar(charPool);
    }

    // Shuffle final password
    password = shuffleString(password);
    
    if (passwordOutput) {
      passwordOutput.textContent = password;
      updateStrength(password, charPool.length);
    }
  };

  // Helper to pick secure random character
  const getRandomChar = (pool) => {
    const array = new Uint32Array(1);
    window.crypto.getRandomValues(array);
    const randomIndex = array[0] % pool.length;
    return pool.charAt(randomIndex);
  };

  // Helper to shuffle characters securely
  const shuffleString = (str) => {
    const arr = str.split("");
    for (let i = arr.length - 1; i > 0; i--) {
      const array = new Uint32Array(1);
      window.crypto.getRandomValues(array);
      const j = array[0] % (i + 1);
      const temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
    }
    return arr.join("");
  };

  // Update Strength Metric
  const updateStrength = (password, poolSize) => {
    if (!strengthBar || !strengthText) return;
    
    const length = password.length;
    if (length === 0) {
      strengthBar.style.width = "0%";
      strengthText.textContent = "-";
      return;
    }

    // Entropy calculation: L * log2(R)
    const entropy = length * Math.log2(poolSize);
    
    let percent = 0;
    let label = "";
    let color = "";

    if (entropy < 40) {
      percent = 25;
      label = `Weak (${Math.round(entropy)} bits entropy)`;
      color = "var(--danger)";
    } else if (entropy >= 40 && entropy < 60) {
      percent = 50;
      label = `Medium (${Math.round(entropy)} bits entropy)`;
      color = "var(--warning)";
    } else if (entropy >= 60 && entropy < 80) {
      percent = 75;
      label = `Strong (${Math.round(entropy)} bits entropy)`;
      color = "var(--color-violet)";
    } else {
      percent = 100;
      label = `Very Strong (${Math.round(entropy)} bits entropy)`;
      color = "var(--success)";
    }

    strengthBar.style.width = percent + "%";
    strengthBar.style.backgroundColor = color;
    strengthText.textContent = label;
    strengthText.style.color = color;
  };

  // Triggers
  if (generateBtn) {
    generateBtn.addEventListener("click", generatePassword);
  }

  if (copyBtn && passwordOutput) {
    copyBtn.addEventListener("click", () => {
      const password = passwordOutput.textContent;
      if (password === "" || password === "Click Generate...") {
        showToast("Generate a password first.", "error");
        return;
      }
      copyToClipboard(password, "Secure password copied!");
    });
  }

  // Generate initial password on load
  generatePassword();
});

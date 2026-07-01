/*
  Case Converter Tool Logic
*/

document.addEventListener("DOMContentLoaded", () => {
  const textArea = document.getElementById("case-converter-input");
  
  const upperBtn = document.getElementById("btn-uppercase");
  const lowerBtn = document.getElementById("btn-lowercase");
  const titleBtn = document.getElementById("btn-titlecase");
  const sentenceBtn = document.getElementById("btn-sentencecase");
  const capitalizedBtn = document.getElementById("btn-capitalizedcase");
  const alternatingBtn = document.getElementById("btn-alternatingcase");
  
  const copyBtn = document.getElementById("btn-copy-case");
  const clearBtn = document.getElementById("btn-clear-case");

  const checkEmpty = () => {
    if (!textArea || textArea.value.trim() === "") {
      showToast("Please enter some text first.", "error");
      return true;
    }
    return false;
  };

  // UPPERCASE
  if (upperBtn && textArea) {
    upperBtn.addEventListener("click", () => {
      if (checkEmpty()) return;
      textArea.value = textArea.value.toUpperCase();
      showToast("Converted to UPPERCASE!");
    });
  }

  // lowercase
  if (lowerBtn && textArea) {
    lowerBtn.addEventListener("click", () => {
      if (checkEmpty()) return;
      textArea.value = textArea.value.toLowerCase();
      showToast("Converted to lowercase!");
    });
  }

  // Title Case (caps first letter of each main word)
  if (titleBtn && textArea) {
    titleBtn.addEventListener("click", () => {
      if (checkEmpty()) return;
      const minorWords = ["a", "an", "the", "and", "but", "for", "or", "nor", "at", "by", "to", "from", "in", "on", "of", "with"];
      const words = textArea.value.toLowerCase().split(/\s+/);
      
      const titleCased = words.map((word, index) => {
        if (index > 0 && minorWords.includes(word)) {
          return word;
        }
        return word.charAt(0).toUpperCase() + word.slice(1);
      }).join(" ");
      
      textArea.value = titleCased;
      showToast("Converted to Title Case!");
    });
  }

  // Sentence Case (caps first letter of each sentence)
  if (sentenceBtn && textArea) {
    sentenceBtn.addEventListener("click", () => {
      if (checkEmpty()) return;
      const text = textArea.value.toLowerCase();
      // Split sentences, keep delimiters
      const sentences = text.split(/([.!?]\s*)/);
      
      const sentenceCased = sentences.map((piece, index) => {
        // If it's a delimiter/space, leave it
        if (index % 2 !== 0) return piece;
        // Find first alphabetical char and capitalize it
        const firstLetterMatch = piece.match(/[a-z]/);
        if (firstLetterMatch) {
          const indexFirst = piece.indexOf(firstLetterMatch[0]);
          return piece.slice(0, indexFirst) + firstLetterMatch[0].toUpperCase() + piece.slice(indexFirst + 1);
        }
        return piece;
      }).join("");

      textArea.value = sentenceCased;
      showToast("Converted to Sentence Case!");
    });
  }

  // Capitalized Case (caps first letter of EVERY word)
  if (capitalizedBtn && textArea) {
    capitalizedBtn.addEventListener("click", () => {
      if (checkEmpty()) return;
      const words = textArea.value.toLowerCase().split(/(\s+)/);
      const capitalized = words.map(word => {
        if (word.trim() === "") return word; // whitespace
        return word.charAt(0).toUpperCase() + word.slice(1);
      }).join("");
      
      textArea.value = capitalized;
      showToast("Converted to Capitalized Case!");
    });
  }

  // Alternating Case (aLtErNaTiNg)
  if (alternatingBtn && textArea) {
    alternatingBtn.addEventListener("click", () => {
      if (checkEmpty()) return;
      let chars = textArea.value.split("");
      let isUpper = false;
      
      const alternating = chars.map(char => {
        if (/[a-zA-Z]/.test(char)) {
          const converted = isUpper ? char.toUpperCase() : char.toLowerCase();
          isUpper = !isUpper;
          return converted;
        }
        return char;
      }).join("");
      
      textArea.value = alternating;
      showToast("Converted to Alternating Case!");
    });
  }

  // Copy
  if (copyBtn && textArea) {
    copyBtn.addEventListener("click", () => {
      if (textArea.value.trim() === "") {
        showToast("Please enter some text to copy.", "error");
        return;
      }
      copyToClipboard(textArea.value, "Converted text copied to clipboard!");
    });
  }

  // Clear
  if (clearBtn && textArea) {
    clearBtn.addEventListener("click", () => {
      textArea.value = "";
      showToast("Text cleared!");
    });
  }
});

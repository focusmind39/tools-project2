/*
  Word Counter Tool Logic
*/

document.addEventListener("DOMContentLoaded", () => {
  const textArea = document.getElementById("word-counter-input");
  const charCountVal = document.getElementById("stat-chars");
  const charNoSpaceVal = document.getElementById("stat-chars-nospace");
  const wordCountVal = document.getElementById("stat-words");
  const sentenceCountVal = document.getElementById("stat-sentences");
  const paragraphCountVal = document.getElementById("stat-paragraphs");
  const readingTimeVal = document.getElementById("stat-reading-time");
  
  const copyBtn = document.getElementById("btn-copy-text");
  const clearBtn = document.getElementById("btn-clear-text");

  if (textArea) {
    textArea.addEventListener("input", () => {
      const text = textArea.value;
      
      // Character counts
      const totalChars = text.length;
      const charsNoSpace = text.replace(/\s/g, "").length;
      
      // Word count
      const cleanText = text.trim();
      const words = cleanText === "" ? 0 : cleanText.split(/\s+/).length;
      
      // Sentence count
      // Splitting by standard ending punctuations: . ! ?
      const sentences = cleanText === "" ? 0 : cleanText.split(/[.!?]+/).filter(s => s.trim().length > 0).length;
      
      // Paragraph count
      // Splitting by double newline
      const paragraphs = cleanText === "" ? 0 : cleanText.split(/\n\s*\n/).filter(p => p.trim().length > 0).length;
      
      // Average Reading Time (approx 200 words per minute)
      const readingTime = Math.ceil(words / 200);
      
      // Update values
      if (charCountVal) charCountVal.textContent = totalChars;
      if (charNoSpaceVal) charNoSpaceVal.textContent = charsNoSpace;
      if (wordCountVal) wordCountVal.textContent = words;
      if (sentenceCountVal) sentenceCountVal.textContent = sentences;
      if (paragraphCountVal) paragraphCountVal.textContent = paragraphs;
      if (readingTimeVal) readingTimeVal.textContent = readingTime + " min";
    });
  }

  // Copy functionality
  if (copyBtn && textArea) {
    copyBtn.addEventListener("click", () => {
      if (textArea.value.trim() === "") {
        showToast("Please enter some text to copy.", "error");
        return;
      }
      copyToClipboard(textArea.value, "Text copied to clipboard!");
    });
  }

  // Clear functionality
  if (clearBtn && textArea) {
    clearBtn.addEventListener("click", () => {
      textArea.value = "";
      textArea.dispatchEvent(new Event("input"));
      showToast("Text cleared!");
    });
  }
});

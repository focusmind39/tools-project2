/*
  Morse Code Translator Tool Logic
  Translates text to/from Morse code and plays audio using the Web Audio API.
*/

const MORSE_MAP = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
  '8': '---..', '9': '----.', '0': '-----',
  '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
  '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
  '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
  ' ': '/'
};

const REVERSE_MAP = {};
for (let key in MORSE_MAP) {
  REVERSE_MAP[MORSE_MAP[key]] = key;
}

document.addEventListener("DOMContentLoaded", () => {
  const textInput = document.getElementById("morse-input-text");
  const outputBox = document.getElementById("morse-output-box");
  
  const translateToMorseBtn = document.getElementById("btn-translate-to-morse");
  const translateToTextBtn = document.getElementById("btn-translate-to-text");
  const playBtn = document.getElementById("btn-play-morse");
  const stopBtn = document.getElementById("btn-stop-morse");
  const clearBtn = document.getElementById("btn-clear-morse");
  
  const playIndicator = document.querySelector(".morse-play-indicator");

  // Translate text to Morse
  const textToMorse = () => {
    const text = textInput.value.toUpperCase().trim();
    if (text === "") {
      showToast("Please enter some text.", "error");
      return;
    }

    const morse = text.split("").map(char => {
      // Return mapped morse or blank if not found
      return MORSE_MAP[char] !== undefined ? MORSE_MAP[char] : "";
    }).filter(s => s.length > 0).join(" ");

    outputBox.textContent = morse;
    showToast("Translated to Morse code!");
  };

  // Translate Morse to text
  const morseToText = () => {
    const morse = textInput.value.trim();
    if (morse === "") {
      showToast("Please enter Morse code (dots and dashes).", "error");
      return;
    }

    // Split letters by space, words by slash '/'
    const words = morse.split(/\s*\/\s*/);
    const decoded = words.map(word => {
      const letters = word.split(/\s+/);
      return letters.map(letter => {
        return REVERSE_MAP[letter] !== undefined ? REVERSE_MAP[letter] : "";
      }).join("");
    }).join(" ");

    outputBox.textContent = decoded;
    showToast("Translated to text!");
  };

  // Audio Playback using Web Audio API
  let audioCtx = null;
  let oscillator = null;
  let gainNode = null;
  let timeouts = [];

  const stopAudio = () => {
    // Clear all scheduled timers
    timeouts.forEach(t => clearTimeout(t));
    timeouts = [];

    // Stop sound nodes
    if (oscillator) {
      try {
        oscillator.stop();
        oscillator.disconnect();
      } catch (e) {}
      oscillator = null;
    }
    if (audioCtx) {
      try {
        audioCtx.close();
      } catch (e) {}
      audioCtx = null;
    }

    if (playIndicator) {
      playIndicator.classList.remove("morse-playing");
    }
  };

  const playMorse = () => {
    const code = outputBox.textContent.trim();
    if (code === "" || code === "-" || code.startsWith("Please") || !/[.\-\/]/.test(code)) {
      showToast("Translate to Morse code first.", "error");
      return;
    }

    stopAudio(); // Reset any playing contexts

    // Create browser Audio Context
    const AudioContextClass = window.AudioContext || window.webkitAudioContext;
    if (!AudioContextClass) {
      showToast("Browser does not support Web Audio API.", "error");
      return;
    }

    try {
      audioCtx = new AudioContextClass();
      
      // Setup gain node (volume)
      gainNode = audioCtx.createGain();
      gainNode.gain.setValueAtTime(0, audioCtx.currentTime); // start silent
      
      // Setup oscillator node (beeps)
      oscillator = audioCtx.createOscillator();
      oscillator.type = "sine";
      oscillator.frequency.setValueAtTime(600, audioCtx.currentTime); // 600Hz frequency tone
      
      oscillator.connect(gainNode);
      gainNode.connect(audioCtx.destination);
      oscillator.start();
    } catch (e) {
      console.error("AudioContext initialization failed:", e);
      showToast("Audio playback failed. Please verify your system sound configuration.", "error");
      stopAudio();
      return;
    }

    if (playIndicator) {
      playIndicator.classList.add("morse-playing");
    }

    // Playback Timing Constants (in milliseconds)
    const dotDuration = 80;
    const dashDuration = dotDuration * 3;
    const intraSymbolGap = dotDuration;
    const interLetterGap = dotDuration * 3;
    const interWordGap = dotDuration * 7;

    let timeOffset = 50; // initial start delay

    const scheduleBeep = (duration) => {
      // Turn volume UP at start of beep
      const startTimer = setTimeout(() => {
        if (gainNode && audioCtx) {
          gainNode.gain.setValueAtTime(0.5, audioCtx.currentTime);
        }
      }, timeOffset);
      timeouts.push(startTimer);

      timeOffset += duration;

      // Turn volume DOWN at end of beep
      const endTimer = setTimeout(() => {
        if (gainNode && audioCtx) {
          gainNode.gain.setValueAtTime(0, audioCtx.currentTime);
        }
      }, timeOffset);
      timeouts.push(endTimer);
    };

    // Parse code characters
    // Space means end of letter, slash '/' means end of word
    for (let i = 0; i < code.length; i++) {
      const char = code.charAt(i);
      
      if (char === ".") {
        scheduleBeep(dotDuration);
        timeOffset += intraSymbolGap;
      } else if (char === "-") {
        scheduleBeep(dashDuration);
        timeOffset += intraSymbolGap;
      } else if (char === " ") {
        timeOffset += interLetterGap;
      } else if (char === "/") {
        timeOffset += interWordGap;
      }
    }

    // Schedule final stop callback
    const finalTimer = setTimeout(() => {
      stopAudio();
    }, timeOffset);
    timeouts.push(finalTimer);
  };

  if (translateToMorseBtn) translateToMorseBtn.addEventListener("click", textToMorse);
  if (translateToTextBtn) translateToTextBtn.addEventListener("click", morseToText);
  if (playBtn) playBtn.addEventListener("click", playMorse);
  if (stopBtn) stopBtn.addEventListener("click", stopAudio);

  // Copy Result
  const copyBtn = document.getElementById("btn-copy-morse");
  if (copyBtn && outputBox) {
    copyBtn.addEventListener("click", () => {
      const val = outputBox.textContent;
      if (val === "" || val === "-") {
        showToast("Translate some text first.", "error");
        return;
      }
      copyToClipboard(val, "Morse result copied!");
    });
  }

  // Clear fields
  if (clearBtn && textInput) {
    clearBtn.addEventListener("click", () => {
      textInput.value = "";
      outputBox.textContent = "-";
      stopAudio();
      showToast("Morse form cleared!");
    });
  }
});

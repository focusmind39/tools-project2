/*
  Color Picker & Converter Tool Logic
*/

document.addEventListener("DOMContentLoaded", () => {
  const colorInput = document.getElementById("color-picker-input");
  
  const hexOut = document.getElementById("color-hex");
  const rgbOut = document.getElementById("color-rgb");
  const hslOut = document.getElementById("color-hsl");
  const cmykOut = document.getElementById("color-cmyk");
  
  const paletteContainer = document.getElementById("color-palette");

  // Helper: Hex to RGB
  const hexToRgb = (hex) => {
    hex = hex.replace(/^#/, "");
    if (hex.length === 3) {
      hex = hex.split("").map(c => c + c).join("");
    }
    const num = parseInt(hex, 16);
    return {
      r: (num >> 16) & 255,
      g: (num >> 8) & 255,
      b: num & 255
    };
  };

  // Helper: RGB to HSL
  const rgbToHsl = (r, g, b) => {
    r /= 255; g /= 255; b /= 255;
    const max = Math.max(r, g, b), min = Math.min(r, g, b);
    let h, s, l = (max + min) / 2;

    if (max === min) {
      h = s = 0; // achromatic
    } else {
      const d = max - min;
      s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
      switch (max) {
        case r: h = (g - b) / d + (g < b ? 6 : 0); break;
        case g: h = (b - r) / d + 2; break;
        case b: h = (r - g) / d + 4; break;
      }
      h /= 6;
    }

    return {
      h: Math.round(h * 360),
      s: Math.round(s * 100),
      l: Math.round(l * 100)
    };
  };

  // Helper: RGB to CMYK
  const rgbToCmyk = (r, g, b) => {
    const rL = r / 255;
    const gL = g / 255;
    const bL = b / 255;
    
    const k = 1 - Math.max(rL, gL, bL);
    if (k === 1) {
      return { c: 0, m: 0, y: 0, k: 100 };
    }
    
    const c = Math.round(((1 - rL - k) / (1 - k)) * 100);
    const m = Math.round(((1 - gL - k) / (1 - k)) * 100);
    const y = Math.round(((1 - bL - k) / (1 - k)) * 100);
    
    return {
      c: c,
      m: m,
      y: y,
      k: Math.round(k * 100)
    };
  };

  // Helper: HSL to Hex
  const hslToHex = (h, s, l) => {
    l /= 100;
    const a = s * Math.min(l, 1 - l) / 100;
    const f = n => {
      const k = (n + h / 30) % 12;
      const color = l - a * Math.max(Math.min(k - 3, 9 - k, 1), -1);
      return Math.round(255 * color).toString(16).padStart(2, "0");
    };
    return `#${f(0)}${f(8)}${f(4)}`;
  };

  // Core update cycle
  const updateColors = (hexValue) => {
    colorInput.value = hexValue;
    
    const rgb = hexToRgb(hexValue);
    const hsl = rgbToHsl(rgb.r, rgb.g, rgb.b);
    const cmyk = rgbToCmyk(rgb.r, rgb.g, rgb.b);

    // Update outputs
    hexOut.textContent = hexValue.toUpperCase();
    rgbOut.textContent = `rgb(${rgb.r}, ${rgb.g}, ${rgb.b})`;
    hslOut.textContent = `hsl(${hsl.h}, ${hsl.s}%, ${hsl.l}%)`;
    cmykOut.textContent = `cmyk(${cmyk.c}%, ${cmyk.m}%, ${cmyk.y}%, ${cmyk.k}%)`;

    // Generate shade/tint palette swatches
    generatePalette(hsl.h, hsl.s);
  };

  const generatePalette = (h, s) => {
    if (!paletteContainer) return;
    paletteContainer.innerHTML = "";
    
    // Lightness variations: 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%
    const lightnesses = [10, 20, 30, 40, 50, 60, 70, 80, 90];
    
    lightnesses.forEach(l => {
      const hex = hslToHex(h, s, l);
      const swatch = document.createElement("div");
      swatch.className = "color-swatch";
      swatch.style.backgroundColor = hex;
      swatch.textContent = `${l}%`;
      swatch.title = hex.toUpperCase();
      
      swatch.addEventListener("click", () => {
        updateColors(hex);
        showToast(`Selected shade ${hex.toUpperCase()}!`);
      });
      
      paletteContainer.appendChild(swatch);
    });
  };

  if (colorInput) {
    colorInput.addEventListener("input", (e) => {
      updateColors(e.target.value);
    });
  }

  // Setup copy badge listeners
  const setupCopy = (btnId, boxId, label) => {
    const btn = document.getElementById(btnId);
    const box = document.getElementById(boxId);
    if (btn && box) {
      btn.addEventListener("click", () => {
        const val = box.textContent;
        if (val === "" || val === "-") {
          showToast("Select a color first.", "error");
          return;
        }
        copyToClipboard(val, `${label} copied!`);
      });
    }
  };

  setupCopy("btn-copy-hex", "color-hex", "HEX color code");
  setupCopy("btn-copy-rgb", "color-rgb", "RGB color code");
  setupCopy("btn-copy-hsl", "color-hsl", "HSL color code");
  setupCopy("btn-copy-cmyk", "color-cmyk", "CMYK color code");

  // Set initial default color (Enginewheels Violet #7C3AED)
  updateColors("#7c3aed");
});

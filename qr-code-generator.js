/*
  QR Code Generator Tool Logic
  Utilizes the QRious canvas renderer to generate QR codes locally.
*/

document.addEventListener("DOMContentLoaded", () => {
  const qrInput = document.getElementById("qr-value");
  const qrSize = document.getElementById("qr-size");
  const qrSizeVal = document.getElementById("qr-size-val");
  
  const qrFgColor = document.getElementById("qr-fg");
  const qrBgColor = document.getElementById("qr-bg");
  const qrLevel = document.getElementById("qr-level");
  
  const canvasElement = document.getElementById("qrcode-canvas");
  const generateBtn = document.getElementById("btn-generate-qr");
  const downloadBtn = document.getElementById("btn-download-qr");

  // Sync size range value
  if (qrSize && qrSizeVal) {
    qrSize.addEventListener("input", (e) => {
      qrSizeVal.textContent = e.target.value + " x " + e.target.value + " px";
    });
  }

  let qrInstance = null;

  const generateQRCode = () => {
    const value = qrInput.value.trim();
    if (value === "") {
      showToast("Please enter some text or link.", "error");
      return;
    }

    const size = parseInt(qrSize.value, 10);
    const fg = qrFgColor.value;
    const bg = qrBgColor.value;
    const level = qrLevel.value;

    try {
      if (!qrInstance) {
        qrInstance = new QRious({
          element: canvasElement,
          value: value,
          size: size,
          foreground: fg,
          background: bg,
          level: level
        });
      } else {
        qrInstance.set({
          value: value,
          size: size,
          foreground: fg,
          background: bg,
          level: level
        });
      }
      showToast("QR Code generated successfully!");
    } catch (err) {
      showToast("Error generating QR Code.", "error");
    }
  };

  // Download functionality
  const downloadQRCode = () => {
    if (!canvasElement) return;
    
    // Check if canvas has content
    const dataURL = canvasElement.toDataURL("image/png");
    if (!dataURL || qrInput.value.trim() === "") {
      showToast("Generate a QR code first.", "error");
      return;
    }

    const link = document.createElement("a");
    link.download = "qrcode-enginewheels.png";
    link.href = dataURL;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    showToast("QR Code downloaded!");
  };

  if (generateBtn) {
    generateBtn.addEventListener("click", generateQRCode);
  }

  if (downloadBtn) {
    downloadBtn.addEventListener("click", downloadQRCode);
  }

  // Generate initial QR Code on load (wait slightly for QRious to load)
  setTimeout(() => {
    if (typeof QRious !== "undefined") {
      generateQRCode();
    }
  }, 300);
});

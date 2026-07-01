/*
  Epoch Time Converter Tool Logic
*/

document.addEventListener("DOMContentLoaded", () => {
  // 1. Live Ticking Epoch Time
  const liveTick = document.getElementById("epoch-live-tick");
  const copyLiveBtn = document.getElementById("btn-copy-live-epoch");

  const updateLiveEpoch = () => {
    if (liveTick) {
      liveTick.textContent = Math.floor(Date.now() / 1000);
    }
  };
  setInterval(updateLiveEpoch, 1000);
  updateLiveEpoch(); // initial run

  if (copyLiveBtn && liveTick) {
    copyLiveBtn.addEventListener("click", () => {
      copyToClipboard(liveTick.textContent, "Current Unix timestamp copied!");
    });
  }

  // 2. Convert Unix Timestamp to Date
  const tsInput = document.getElementById("ts-input-val");
  const convertTsBtn = document.getElementById("btn-convert-ts");
  const tsOutUtc = document.getElementById("ts-out-utc");
  const tsOutLocal = document.getElementById("ts-out-local");
  const tsOutRelative = document.getElementById("ts-out-relative");

  const convertTimestamp = () => {
    let raw = tsInput.value.trim();
    if (raw === "") {
      showToast("Please enter a timestamp.", "error");
      return;
    }

    let timestamp = parseInt(raw, 10);
    if (isNaN(timestamp)) {
      showToast("Invalid number format.", "error");
      return;
    }

    // Auto detect: If it's a 10-digit number, assume seconds. If 13-digit, assume milliseconds.
    let date;
    if (raw.length <= 10) {
      date = new Date(timestamp * 1000);
    } else {
      date = new Date(timestamp);
    }

    if (isNaN(date.getTime())) {
      showToast("Invalid timestamp range.", "error");
      return;
    }

    if (tsOutUtc) tsOutUtc.textContent = date.toUTCString();
    if (tsOutLocal) tsOutLocal.textContent = date.toString();
    if (tsOutRelative) tsOutRelative.textContent = getRelativeTime(date);
    showToast("Converted!");
  };

  // Helper for relative time (e.g., '3 years ago', 'in 2 hours')
  const getRelativeTime = (date) => {
    const now = new Date();
    const diffMs = date - now;
    const diffSec = Math.floor(diffMs / 1000);
    const diffMin = Math.floor(diffSec / 60);
    const diffHours = Math.floor(diffMin / 60);
    const diffDays = Math.floor(diffHours / 24);

    if (Math.abs(diffDays) > 0) {
      return diffDays > 0 ? `in ${diffDays} day(s)` : `${Math.abs(diffDays)} day(s) ago`;
    }
    if (Math.abs(diffHours) > 0) {
      return diffHours > 0 ? `in ${diffHours} hour(s)` : `${Math.abs(diffHours)} hour(s) ago`;
    }
    if (Math.abs(diffMin) > 0) {
      return diffMin > 0 ? `in ${diffMin} minute(s)` : `${Math.abs(diffMin)} minute(s) ago`;
    }
    return diffSec > 0 ? `in ${diffSec} seconds` : "just now";
  };

  if (convertTsBtn) {
    convertTsBtn.addEventListener("click", convertTimestamp);
  }

  // 3. Convert Human Date to Unix Timestamp
  const dateInput = document.getElementById("date-input-val");
  const convertDateBtn = document.getElementById("btn-convert-date");
  const dateOutSec = document.getElementById("date-out-sec");
  const dateOutMs = document.getElementById("date-out-ms");

  // Set default calendar date input to today
  if (dateInput) {
    const today = new Date();
    const yyyy = today.getFullYear();
    const mm = String(today.getMonth() + 1).padStart(2, '0');
    const dd = String(today.getDate()).padStart(2, '0');
    const hh = "12";
    const min = "00";
    dateInput.value = `${yyyy}-${mm}-${dd}T${hh}:${min}`;
  }

  const convertCalendarDate = () => {
    const rawVal = dateInput.value;
    if (!rawVal) {
      showToast("Please select a date and time.", "error");
      return;
    }

    const dateObj = new Date(rawVal);
    if (isNaN(dateObj.getTime())) {
      showToast("Invalid calendar date selection.", "error");
      return;
    }

    const ms = dateObj.getTime();
    const sec = Math.floor(ms / 1000);

    if (dateOutSec) dateOutSec.textContent = sec;
    if (dateOutMs) dateOutMs.textContent = ms;
    showToast("Converted!");
  };

  if (convertDateBtn) {
    convertDateBtn.addEventListener("click", convertCalendarDate);
  }

  // Setup separate copy badges
  const setupCopy = (btnId, boxId, label) => {
    const btn = document.getElementById(btnId);
    const box = document.getElementById(boxId);
    if (btn && box) {
      btn.addEventListener("click", () => {
        const val = box.textContent;
        if (val === "" || val === "-") {
          showToast("Convert first.", "error");
          return;
        }
        copyToClipboard(val, `${label} copied!`);
      });
    }
  };

  setupCopy("btn-copy-utc", "ts-out-utc", "UTC Date");
  setupCopy("btn-copy-local", "ts-out-local", "Local Date");
  setupCopy("btn-copy-sec", "date-out-sec", "Seconds timestamp");
  setupCopy("btn-copy-ms", "date-out-ms", "Milliseconds timestamp");
});

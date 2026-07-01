/*
  Age Calculator Tool Logic
  Calculates precise chronological age and breakdowns.
*/

document.addEventListener("DOMContentLoaded", () => {
  const birthdateInput = document.getElementById("age-birthdate");
  const targetDateInput = document.getElementById("age-target-date");
  
  const calculateBtn = document.getElementById("btn-calculate-age");
  const clearBtn = document.getElementById("btn-clear-age");
  
  const outputExact = document.getElementById("age-output-exact");
  const outputNextBirthday = document.getElementById("age-output-next");
  
  const breakdownMonths = document.getElementById("breakdown-months");
  const breakdownWeeks = document.getElementById("breakdown-weeks");
  const breakdownDays = document.getElementById("breakdown-days");
  const breakdownHours = document.getElementById("breakdown-hours");
  const breakdownMinutes = document.getElementById("breakdown-minutes");

  // Set default target date to today
  if (targetDateInput) {
    const today = new Date();
    const yyyy = today.getFullYear();
    const mm = String(today.getMonth() + 1).padStart(2, '0');
    const dd = String(today.getDate()).padStart(2, '0');
    targetDateInput.value = `${yyyy}-${mm}-${dd}`;
  }

  const calculateAge = () => {
    const bDateStr = birthdateInput.value;
    const tDateStr = targetDateInput.value;

    if (!bDateStr || !tDateStr) {
      showToast("Please enter both dates.", "error");
      return;
    }

    const birthDate = new Date(bDateStr);
    const targetDate = new Date(tDateStr);

    if (birthDate > targetDate) {
      showToast("Birthdate cannot be in the future of the target date.", "error");
      return;
    }

    // Precise calculation of years, months, days
    let bYear = birthDate.getFullYear();
    let bMonth = birthDate.getMonth();
    let bDay = birthDate.getDate();

    let tYear = targetDate.getFullYear();
    let tMonth = targetDate.getMonth();
    let tDay = targetDate.getDate();

    let years = tYear - bYear;
    let months = tMonth - bMonth;
    let days = tDay - bDay;

    if (days < 0) {
      // Borrow days from the previous month
      months--;
      // Find days in previous month
      const prevMonth = new Date(tYear, tMonth, 0); // 0th day gets last day of prev month
      days += prevMonth.getDate();
    }

    if (months < 0) {
      // Borrow months from years
      years--;
      months += 12;
    }

    // Display Exact Age
    if (outputExact) {
      outputExact.innerHTML = `
        <span style="font-size: 1.5rem; font-weight:700; color:var(--color-violet)">${years}</span> years, 
        <span style="font-size: 1.5rem; font-weight:700; color:var(--color-violet)">${months}</span> months, 
        <span style="font-size: 1.5rem; font-weight:700; color:var(--color-violet)">${days}</span> days
      `;
    }

    // Total breakdowns
    const diffTime = Math.abs(targetDate - birthDate);
    const totalDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    const totalMonths = (tYear - bYear) * 12 + (tMonth - bMonth) + (tDay < bDay ? -1 : 0);
    const totalWeeks = Math.floor(totalDays / 7);
    const remainingDays = totalDays % 7;
    
    const totalHours = totalDays * 24;
    const totalMinutes = totalHours * 60;

    if (breakdownMonths) breakdownMonths.textContent = totalMonths.toLocaleString();
    if (breakdownWeeks) breakdownWeeks.textContent = `${totalWeeks.toLocaleString()} weeks, ${remainingDays} days`;
    if (breakdownDays) breakdownDays.textContent = totalDays.toLocaleString();
    if (breakdownHours) breakdownHours.textContent = totalHours.toLocaleString();
    if (breakdownMinutes) breakdownMinutes.textContent = totalMinutes.toLocaleString();

    // Next Birthday Countdown
    let nextBdate = new Date(tYear, bMonth, bDay);
    if (nextBdate < targetDate) {
      nextBdate.setFullYear(tYear + 1);
    }
    
    const nextDiffTime = Math.abs(nextBdate - targetDate);
    const daysToNext = Math.ceil(nextDiffTime / (1000 * 60 * 60 * 24));
    
    if (outputNextBirthday) {
      if (daysToNext === 365 || daysToNext === 366 || (bMonth === tMonth && bDay === tDay)) {
        outputNextBirthday.textContent = "Happy Birthday! Today is the day! 🎉";
        outputNextBirthday.style.color = "var(--success)";
      } else {
        outputNextBirthday.textContent = `${daysToNext} days remaining.`;
        outputNextBirthday.style.color = "var(--text-main)";
      }
    }
    
    showToast("Age calculated successfully!");
  };

  if (calculateBtn) {
    calculateBtn.addEventListener("click", calculateAge);
  }

  if (clearBtn) {
    clearBtn.addEventListener("click", () => {
      birthdateInput.value = "";
      if (outputExact) outputExact.innerHTML = "-";
      if (outputNextBirthday) outputNextBirthday.textContent = "-";
      
      if (breakdownMonths) breakdownMonths.textContent = "-";
      if (breakdownWeeks) breakdownWeeks.textContent = "-";
      if (breakdownDays) breakdownDays.textContent = "-";
      if (breakdownHours) breakdownHours.textContent = "-";
      if (breakdownMinutes) breakdownMinutes.textContent = "-";
      
      showToast("Dates reset!");
    });
  }
});

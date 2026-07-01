# -*- coding: utf-8 -*-
"""
Date and Age Calculators Data
"""

DATE_AGES_TOOLS = [
    {
        "name": "Date Difference Calculator",
        "slug": "date-difference-calculator",
        "category": "Date Calculators",
        "icon": "📅",
        "desc": "Calculate the exact duration between two dates in years, months, weeks, and days.",
        "formula": "Diff = Date2 - Date1",
        "formula_desc": "Finds the absolute difference in days and resolves into precise Gregorian calendar metrics (years, months, days).",
        "inputs": [
            {"id": "dd-d1", "label": "Start Date:", "type": "date"},
            {"id": "dd-d2", "label": "End Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Detailed Difference", "type": "textarea"}
        ],
        "calc_js": """
            const d1Val = document.getElementById('dd-d1').value;
            const d2Val = document.getElementById('dd-d2').value;
            if (!d1Val || !d2Val) {
                showToast("Please select both start and end dates.", "error");
                return;
            }
            const d1 = new Date(d1Val);
            const d2 = new Date(d2Val);
            
            let start = d1 < d2 ? d1 : d2;
            let end = d1 < d2 ? d2 : d1;
            
            let years = end.getFullYear() - start.getFullYear();
            let months = end.getMonth() - start.getMonth();
            let days = end.getDate() - start.getDate();
            
            if (days < 0) {
                months--;
                // Get days in previous month
                const prevMonth = new Date(end.getFullYear(), end.getMonth(), 0);
                days += prevMonth.getDate();
            }
            if (months < 0) {
                years--;
                months += 12;
            }
            
            const diffTime = Math.abs(d2 - d1);
            const totalDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
            const weeks = Math.floor(totalDays / 7);
            const remainingDays = totalDays % 7;
            
            const output = `Difference Details:\\n` +
                           `==============================\\n` +
                           `- Years  : ${years}\\n` +
                           `- Months : ${months}\\n` +
                           `- Days   : ${days}\\n\\n` +
                           `Alternatively:\\n` +
                           `- Total Days  : ${totalDays.toLocaleString()}\\n` +
                           `- Total Weeks : ${weeks} weeks, ${remainingDays} days`;
            
            document.getElementById('text-output').value = output;
            updateBreakdown(`<p>Calculated difference: ${years} years, ${months} months, ${days} days.</p>`);
        """
    },
    {
        "name": "Days Between Dates Calculator",
        "slug": "days-between-dates-calculator",
        "category": "Date Calculators",
        "icon": "📆",
        "desc": "Determine the total number of calendar days between two dates, with option to include the start/end date.",
        "formula": "Days = |Date2 - Date1| (+1 if Inclusive)",
        "formula_desc": "Computes absolute millisecond differences and scales to complete solar day cycles.",
        "inputs": [
            {"id": "dbd-d1", "label": "Start Date:", "type": "date"},
            {"id": "dbd-d2", "label": "End Date:", "type": "date"},
            {"id": "dbd-inc", "label": "Include End Date?", "type": "select", "options": [("no", "No (Exclusive)"), ("yes", "Yes (Inclusive)")]}
        ],
        "outputs": [
            {"id": "out-dbd-days", "label": "Total Days", "prefix": "", "suffix": " Days"}
        ],
        "calc_js": """
            const d1Val = document.getElementById('dbd-d1').value;
            const d2Val = document.getElementById('dbd-d2').value;
            if (!d1Val || !d2Val) {
                showToast("Please choose both dates.", "error");
                return;
            }
            const d1 = new Date(d1Val);
            const d2 = new Date(d2Val);
            const inc = document.getElementById('dbd-inc').value;
            
            const diffTime = Math.abs(d2 - d1);
            let diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
            if (inc === 'yes') {
                diffDays += 1;
            }
            
            document.getElementById('out-dbd-days').textContent = diffDays.toLocaleString();
            updateBreakdown(`<p>Total days interval calculated. Inclusion setting: ${inc}.</p>`);
        """
    },
    {
        "name": "Weeks Between Dates Calculator",
        "slug": "weeks-between-dates-calculator",
        "category": "Date Calculators",
        "icon": "⏳",
        "desc": "Calculate the number of weeks and remaining days between two calendar dates.",
        "formula": "Weeks = Days / 7",
        "formula_desc": "Calculates total day delta and performs Euclidean division by 7 to yield weeks and remaining days.",
        "inputs": [
            {"id": "wbd-d1", "label": "Start Date:", "type": "date"},
            {"id": "wbd-d2", "label": "End Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "out-wbd-weeks", "label": "Weeks", "prefix": "", "suffix": " Weeks"},
            {"id": "out-wbd-days", "label": "Remaining Days", "prefix": "", "suffix": " Days"}
        ],
        "calc_js": """
            const d1Val = document.getElementById('wbd-d1').value;
            const d2Val = document.getElementById('wbd-d2').value;
            if (!d1Val || !d2Val) {
                showToast("Please select start and end dates.", "error");
                return;
            }
            const d1 = new Date(d1Val);
            const d2 = new Date(d2Val);
            
            const diffDays = Math.floor(Math.abs(d2 - d1) / (1000 * 60 * 60 * 24));
            const weeks = Math.floor(diffDays / 7);
            const days = diffDays % 7;
            
            document.getElementById('out-wbd-weeks').textContent = weeks.toLocaleString();
            document.getElementById('out-wbd-days').textContent = days;
            updateBreakdown(`<p>${diffDays} total days translates to ${weeks} weeks and ${days} days.</p>`);
        """
    },
    {
        "name": "Months Between Dates Calculator",
        "slug": "months-between-dates-calculator",
        "category": "Date Calculators",
        "icon": "🗓️",
        "desc": "Find the elapsed calendar months and remaining days between two dates.",
        "formula": "Months = YearDelta*12 + MonthDelta",
        "formula_desc": "Calculates month boundaries, adjusts for date displacements and counts leftover days.",
        "inputs": [
            {"id": "mbd-d1", "label": "Start Date:", "type": "date"},
            {"id": "mbd-d2", "label": "End Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "out-mbd-months", "label": "Months", "prefix": "", "suffix": " Months"},
            {"id": "out-mbd-days", "label": "Remaining Days", "prefix": "", "suffix": " Days"}
        ],
        "calc_js": """
            const d1Val = document.getElementById('mbd-d1').value;
            const d2Val = document.getElementById('mbd-d2').value;
            if (!d1Val || !d2Val) {
                showToast("Select both dates.", "error");
                return;
            }
            const d1 = new Date(d1Val);
            const d2 = new Date(d2Val);
            
            let start = d1 < d2 ? d1 : d2;
            let end = d1 < d2 ? d2 : d1;
            
            let months = (end.getFullYear() - start.getFullYear()) * 12 + (end.getMonth() - start.getMonth());
            let tempDate = new Date(start.getFullYear(), start.getMonth() + months, start.getDate());
            
            if (tempDate > end) {
                months--;
                tempDate = new Date(start.getFullYear(), start.getMonth() + months, start.getDate());
            }
            
            const diffTime = Math.abs(end - tempDate);
            const days = Math.floor(diffTime / (1000 * 60 * 60 * 24));
            
            document.getElementById('out-mbd-months').textContent = months.toLocaleString();
            document.getElementById('out-mbd-days').textContent = days;
            updateBreakdown(`<p>Parsed month displacement: ${months} months and ${days} leftover days.</p>`);
        """
    },
    {
        "name": "Years Between Dates Calculator",
        "slug": "years-between-dates-calculator",
        "category": "Date Calculators",
        "icon": "🏹",
        "desc": "Calculate the exact number of years elapsed between two historical or future calendar dates.",
        "formula": "Years = YearDelta (Adjusted)",
        "formula_desc": "Measures calendar year difference and subtracts one if the anniversary day has not been crossed.",
        "inputs": [
            {"id": "ybd-d1", "label": "Start Date:", "type": "date"},
            {"id": "ybd-d2", "label": "End Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "out-ybd-years", "label": "Years", "prefix": "", "suffix": " Years"}
        ],
        "calc_js": """
            const d1Val = document.getElementById('ybd-d1').value;
            const d2Val = document.getElementById('ybd-d2').value;
            if (!d1Val || !d2Val) {
                showToast("Enter both dates.", "error");
                return;
            }
            const d1 = new Date(d1Val);
            const d2 = new Date(d2Val);
            
            let start = d1 < d2 ? d1 : d2;
            let end = d1 < d2 ? d2 : d1;
            
            let years = end.getFullYear() - start.getFullYear();
            const temp = new Date(start.getFullYear() + years, start.getMonth(), start.getDate());
            if (temp > end) {
                years--;
            }
            
            document.getElementById('out-ybd-years').textContent = years.toLocaleString();
            updateBreakdown(`<p>Total elapsed years: ${years} full calendar cycles.</p>`);
        """
    },
    {
        "name": "Business Days Calculator",
        "slug": "business-days-calculator",
        "category": "Date Calculators",
        "icon": "💼",
        "desc": "Calculate the count of working business days (Monday to Friday) between two dates, excluding weekends.",
        "formula": "BizDays = TotalDays - Weekends",
        "formula_desc": "Loops through dates in range and filters out Saturdays (6) and Sundays (0).",
        "inputs": [
            {"id": "bdc-d1", "label": "Start Date:", "type": "date"},
            {"id": "bdc-d2", "label": "End Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "out-bdc-working", "label": "Working Days", "prefix": "", "suffix": " Working Days"},
            {"id": "out-bdc-weekend", "label": "Weekend Days Excluded", "prefix": "", "suffix": " Weekend Days"}
        ],
        "calc_js": """
            const d1Val = document.getElementById('bdc-d1').value;
            const d2Val = document.getElementById('bdc-d2').value;
            if (!d1Val || !d2Val) {
                showToast("Please choose start and end dates.", "error");
                return;
            }
            let d1 = new Date(d1Val);
            let d2 = new Date(d2Val);
            
            let start = d1 < d2 ? new Date(d1) : new Date(d2);
            let end = d1 < d2 ? new Date(d2) : new Date(d1);
            
            let biz = 0;
            let wends = 0;
            
            while (start <= end) {
                const day = start.getDay();
                if (day === 0 || day === 6) {
                    wends++;
                } else {
                    biz++;
                }
                start.setDate(start.getDate() + 1);
            }
            
            document.getElementById('out-bdc-working').textContent = biz.toLocaleString();
            document.getElementById('out-bdc-weekend').textContent = wends.toLocaleString();
            updateBreakdown(`<p>Completed weekend filter checklist: ${biz} working days and ${wends} weekend days found.</p>`);
        """
    },
    {
        "name": "Working Days Calculator",
        "slug": "working-days-calculator",
        "category": "Date Calculators",
        "icon": "🏭",
        "desc": "Calculate active working days using custom weekend formats (e.g. Sunday-only rest days).",
        "formula": "WorkingDays = Range - CustomRestDays",
        "formula_desc": "Evaluates calendar span and omits days matching the user selected weekend pattern.",
        "inputs": [
            {"id": "wdc-d1", "label": "Start Date:", "type": "date"},
            {"id": "wdc-d2", "label": "End Date:", "type": "date"},
            {"id": "wdc-weekend", "label": "Weekend Pattern:", "type": "select", "options": [
                ("sat-sun", "Saturday & Sunday"),
                ("sun-only", "Sunday Only"),
                ("fri-sat", "Friday & Saturday")
            ]}
        ],
        "outputs": [
            {"id": "out-wdc-working", "label": "Work Days", "prefix": "", "suffix": " Days"}
        ],
        "calc_js": """
            const d1Val = document.getElementById('wdc-d1').value;
            const d2Val = document.getElementById('wdc-d2').value;
            if (!d1Val || !d2Val) {
                showToast("Select dates.", "error");
                return;
            }
            let d1 = new Date(d1Val);
            let d2 = new Date(d2Val);
            const style = document.getElementById('wdc-weekend').value;
            
            let start = d1 < d2 ? new Date(d1) : new Date(d2);
            let end = d1 < d2 ? new Date(d2) : new Date(d1);
            
            let work = 0;
            while (start <= end) {
                const day = start.getDay();
                let isWeekend = false;
                if (style === 'sat-sun') {
                    isWeekend = (day === 0 || day === 6);
                } else if (style === 'sun-only') {
                    isWeekend = (day === 0);
                } else if (style === 'fri-sat') {
                    isWeekend = (day === 5 || day === 6);
                }
                
                if (!isWeekend) work++;
                start.setDate(start.getDate() + 1);
            }
            
            document.getElementById('out-wdc-working').textContent = work.toLocaleString();
            updateBreakdown(`<p>Calculated using pattern '${style}': ${work} custom working days.</p>`);
        """
    },
    {
        "name": "School Days Calculator",
        "slug": "school-days-calculator",
        "category": "Date Calculators",
        "icon": "🎒",
        "desc": "Calculate school attendance days between two dates, adjusting for weekends and institutional holidays.",
        "formula": "SchoolDays = BusinessDays - CustomHolidays",
        "formula_desc": "Calculates business days (Monday-Friday) and deducts custom vacation or holiday values.",
        "inputs": [
            {"id": "sdc-d1", "label": "Start Term:", "type": "date"},
            {"id": "sdc-d2", "label": "End Term:", "type": "date"},
            {"id": "sdc-hols", "label": "Vacation / Holiday Days:", "type": "number", "default": "0", "min": "0", "max": "365"}
        ],
        "outputs": [
            {"id": "out-sdc-school", "label": "School Days", "prefix": "", "suffix": " Days"}
        ],
        "calc_js": """
            const d1Val = document.getElementById('sdc-d1').value;
            const d2Val = document.getElementById('sdc-d2').value;
            const hols = parseInt(document.getElementById('sdc-hols').value) || 0;
            
            if (!d1Val || !d2Val) {
                showToast("Set term dates.", "error");
                return;
            }
            let d1 = new Date(d1Val);
            let d2 = new Date(d2Val);
            
            let start = d1 < d2 ? new Date(d1) : new Date(d2);
            let end = d1 < d2 ? new Date(d2) : new Date(d1);
            
            let biz = 0;
            while (start <= end) {
                const day = start.getDay();
                if (day !== 0 && day !== 6) biz++;
                start.setDate(start.getDate() + 1);
            }
            
            let schoolDays = biz - hols;
            if (schoolDays < 0) schoolDays = 0;
            
            document.getElementById('out-sdc-school').textContent = schoolDays.toLocaleString();
            updateBreakdown(`<p>Business days: ${biz}. Deducted holidays: ${hols}. Net school days: ${schoolDays}.</p>`);
        """
    },
    {
        "name": "Holiday Calculator",
        "slug": "holiday-calculator",
        "category": "Date Calculators",
        "icon": "🎉",
        "desc": "Calculate calendar days and week positions of major national and international holidays for any given year.",
        "formula": "HolidayDates = Math.Rule(Year)",
        "formula_desc": "Solves day matching rules (e.g. Thanksgiving on the 4th Thursday in November) for any year parameter.",
        "inputs": [
            {"id": "hc-year", "label": "Calendar Year:", "type": "number", "default": "2026", "min": "1900", "max": "2100"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Calculated Holiday List", "type": "textarea"}
        ],
        "calc_js": """
            const yr = parseInt(document.getElementById('hc-year').value);
            if (isNaN(yr) || yr < 1900 || yr > 2100) {
                showToast("Please enter a valid year between 1900 and 2100.", "error");
                return;
            }
            
            // Helper to get Nth weekday of a month
            function getNthWeekday(year, month, weekday, nth) {
                let count = 0;
                let date = new Date(year, month, 1);
                while (date.getMonth() === month) {
                    if (date.getDay() === weekday) {
                        count++;
                        if (count === nth) return new Date(date);
                    }
                    date.setDate(date.getDate() + 1);
                }
                return null;
            }
            
            const holidays = [
                { name: "New Year's Day", date: new Date(yr, 0, 1) },
                { name: "MLK Jr. Day (US)", date: getNthWeekday(yr, 0, 1, 3) }, // 3rd Monday in Jan (1 = Mon)
                { name: "Valentine's Day", date: new Date(yr, 1, 14) },
                { name: "Memorial Day (US)", date: (() => {
                    // Last Monday in May
                    let d = new Date(yr, 4, 31);
                    while (d.getDay() !== 1) d.setDate(d.getDate() - 1);
                    return d;
                })() },
                { name: "Independence Day (US)", date: new Date(yr, 6, 4) },
                { name: "Labor Day (US)", date: getNthWeekday(yr, 8, 1, 1) }, // 1st Monday in Sep
                { name: "Halloween", date: new Date(yr, 9, 31) },
                { name: "Thanksgiving (US)", date: getNthWeekday(yr, 10, 4, 4) }, // 4th Thursday in Nov
                { name: "Christmas Day", date: new Date(yr, 11, 25) }
            ];
            
            let output = `Federal & Major Holidays for ${yr}:\\n`;
            output += `=========================================\\n`;
            holidays.forEach(h => {
                const opt = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
                output += `${h.name.padEnd(25)} : ${h.date.toLocaleDateString('en-US', opt)}\\n`;
            });
            
            document.getElementById('text-output').value = output;
            updateBreakdown(`<p>Successfully resolved holiday rules for calendar year ${yr}.</p>`);
        """
    },
    {
        "name": "Leap Year Calculator",
        "slug": "leap-year-calculator",
        "category": "Date Calculators",
        "icon": "🐸",
        "desc": "Check if a specific year is a leap year (containing 366 days instead of 365).",
        "formula": "Leap = (Y % 4 == 0) && (Y % 100 != 0 || Y % 400 == 0)",
        "formula_desc": "Evaluates calendar year matching divisibility constraints based on the Gregorian reform guidelines.",
        "inputs": [
            {"id": "ly-year", "label": "Year to Check:", "type": "number", "default": "2026", "min": "1", "max": "99999"}
        ],
        "outputs": [
            {"id": "out-ly-status", "label": "Leap Year Status", "prefix": "This year is ", "suffix": ""}
        ],
        "calc_js": """
            const yr = parseInt(document.getElementById('ly-year').value);
            if (isNaN(yr) || yr < 1) {
                showToast("Please enter a positive year.", "error");
                return;
            }
            
            const isLeap = (yr % 4 === 0 && yr % 100 !== 0) || (yr % 400 === 0);
            const status = isLeap ? "a LEAP YEAR (366 Days)" : "a STANDARD YEAR (365 Days)";
            
            document.getElementById('out-ly-status').textContent = status;
            
            let nextLeap = yr;
            while (true) {
                nextLeap++;
                if ((nextLeap % 4 === 0 && nextLeap % 100 !== 0) || (nextLeap % 400 === 0)) {
                    break;
                }
            }
            updateBreakdown(`<p>Year ${yr} checked. The next leap year after this is ${nextLeap}.</p>`);
        """
    },
    {
        "name": "Age Calculator",
        "slug": "age-calculator",
        "category": "Age Calculators",
        "icon": "🎂",
        "desc": "Calculate your exact age in years, months, and days based on your birthdate.",
        "formula": "Age = TargetDate - DateOfBirth",
        "formula_desc": "Extracts years, months, and days differences, matching days of month to avoid fractional shift errors.",
        "inputs": [
            {"id": "ac-birth", "label": "Date of Birth:", "type": "date"},
            {"id": "ac-target", "label": "Age at Date of:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Calculated Age Result", "type": "textarea"}
        ],
        "calc_js": """
            const birthVal = document.getElementById('ac-birth').value;
            let targetVal = document.getElementById('ac-target').value;
            
            if (!birthVal) {
                showToast("Please enter a birth date.", "error");
                return;
            }
            if (!targetVal) {
                // Default to today
                const today = new Date();
                targetVal = today.toISOString().split('T')[0];
                document.getElementById('ac-target').value = targetVal;
            }
            
            const dob = new Date(birthVal);
            const target = new Date(targetVal);
            
            if (dob > target) {
                showToast("Birthdate cannot be after target age date.", "error");
                return;
            }
            
            let years = target.getFullYear() - dob.getFullYear();
            let months = target.getMonth() - dob.getMonth();
            let days = target.getDate() - dob.getDate();
            
            if (days < 0) {
                months--;
                const prevMonth = new Date(target.getFullYear(), target.getMonth(), 0);
                days += prevMonth.getDate();
            }
            if (months < 0) {
                years--;
                months += 12;
            }
            
            const diffTime = Math.abs(target - dob);
            const totalDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
            
            const output = `Your Calculated Age:\\n` +
                           `==============================\\n` +
                           `- Years  : ${years}\\n` +
                           `- Months : ${months}\\n` +
                           `- Days   : ${days}\\n\\n` +
                           `Equivalents:\\n` +
                           `- In Days   : ${totalDays.toLocaleString()} days\\n` +
                           `- In Weeks  : ${Math.floor(totalDays/7).toLocaleString()} weeks`;
            
            document.getElementById('text-output').value = output;
            updateBreakdown(`<p>Computed precise age: ${years} years, ${months} months, and ${days} days.</p>`);
        """
    },
    {
        "name": "Age In Days Calculator",
        "slug": "age-in-days-calculator",
        "category": "Age Calculators",
        "icon": "👶",
        "desc": "Calculate your total age in days, hours, and minutes since your birthdate.",
        "formula": "AgeDays = TotalElapsedTime / (24 * 3600 * 1000)",
        "formula_desc": "Finds millisecond variance from birth epoch to now, dividing by ms-per-day.",
        "inputs": [
            {"id": "aid-birth", "label": "Date of Birth:", "type": "date"}
        ],
        "outputs": [
            {"id": "out-aid-days", "label": "Age in Days", "prefix": "", "suffix": " Days"}
        ],
        "calc_js": """
            const birthVal = document.getElementById('aid-birth').value;
            if (!birthVal) {
                showToast("Please pick your birthdate.", "error");
                return;
            }
            const dob = new Date(birthVal);
            const now = new Date();
            if (dob > now) {
                showToast("Date of birth cannot be in the future.", "error");
                return;
            }
            const days = Math.floor((now - dob) / (1000 * 60 * 60 * 24));
            document.getElementById('out-aid-days').textContent = days.toLocaleString();
            updateBreakdown(`<p>Calculated total days: ${days.toLocaleString()} days. Equivalent to ${(days * 24).toLocaleString()} hours.</p>`);
        """
    },
    {
        "name": "Age In Months Calculator",
        "slug": "age-in-months-calculator",
        "category": "Age Calculators",
        "icon": "🍼",
        "desc": "Compute your age in months, showing total months elapsed since birth.",
        "formula": "AgeMonths = Years * 12 + Months",
        "formula_desc": "Finds total full month cycles from birth to the current date.",
        "inputs": [
            {"id": "aim-birth", "label": "Date of Birth:", "type": "date"}
        ],
        "outputs": [
            {"id": "out-aim-months", "label": "Age in Months", "prefix": "", "suffix": " Months"}
        ],
        "calc_js": """
            const birthVal = document.getElementById('aim-birth').value;
            if (!birthVal) {
                showToast("Please enter birthdate.", "error");
                return;
            }
            const dob = new Date(birthVal);
            const now = new Date();
            if (dob > now) {
                showToast("Date of birth cannot be in the future.", "error");
                return;
            }
            
            let months = (now.getFullYear() - dob.getFullYear()) * 12 + (now.getMonth() - dob.getMonth());
            if (now.getDate() < dob.getDate()) {
                months--;
            }
            document.getElementById('out-aim-months').textContent = months.toLocaleString();
            updateBreakdown(`<p>Total full month cycles: ${months.toLocaleString()} months.</p>`);
        """
    },
    {
        "name": "Exact Age Calculator",
        "slug": "exact-age-calculator",
        "category": "Age Calculators",
        "icon": "⏳",
        "desc": "Track your exact age in real-time down to the millisecond with a live ticking display.",
        "formula": "ExactAge = Now() - BirthTime (10Hz Interval)",
        "formula_desc": "Initiates a rapid 100ms timer loop showing years, months, days, hours, minutes, seconds, and milliseconds.",
        "auto_calc": True,
        "inputs": [
            {"id": "eac-birth", "label": "Date of Birth:", "type": "date"},
            {"id": "eac-time", "label": "Time of Birth (24h format):", "type": "text", "default": "12:00"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Live Exact Age Dashboard", "type": "textarea"}
        ],
        "calc_js": """
            if (window.exactAgeInterval) clearInterval(window.exactAgeInterval);
            
            const birthVal = document.getElementById('eac-birth').value;
            const timeVal = document.getElementById('eac-time').value || "12:00";
            
            if (!birthVal) {
                showToast("Select date of birth first.", "error");
                return;
            }
            
            const parts = timeVal.split(':');
            const hrs = parseInt(parts[0]) || 0;
            const mins = parseInt(parts[1]) || 0;
            
            const dob = new Date(birthVal);
            dob.setHours(hrs, mins, 0, 0);
            
            function tick() {
                const now = new Date();
                const diff = now - dob;
                if (diff < 0) {
                    document.getElementById('text-output').value = "Birth time cannot be in the future!";
                    return;
                }
                
                let years = now.getFullYear() - dob.getFullYear();
                let months = now.getMonth() - dob.getMonth();
                let days = now.getDate() - dob.getDate();
                
                if (days < 0) {
                    months--;
                    const prevMonth = new Date(now.getFullYear(), now.getMonth(), 0);
                    days += prevMonth.getDate();
                }
                if (months < 0) {
                    years--;
                    months += 12;
                }
                
                // Hours, minutes, seconds, milliseconds
                let ms = diff % 1000;
                let secs = Math.floor(diff / 1000) % 60;
                let mns = Math.floor(diff / (1000 * 60)) % 60;
                let hours = Math.floor(diff / (1000 * 60 * 60)) % 24;
                
                const dash = `======================================\\n` +
                             `          LIVE EXACT AGE TIMER        \\n` +
                             `======================================\\n` +
                             ` Age: ${years} Years, ${months} Months, ${days} Days\\n` +
                             ` Time: ${hours}h : ${mns}m : ${secs}s : ${ms}ms\\n` +
                             `======================================\\n` +
                             `Total Elapsed Milliseconds: ${diff.toLocaleString()}`;
                             
                document.getElementById('text-output').value = dash;
            }
            
            tick();
            window.exactAgeInterval = setInterval(tick, 100);
            updateBreakdown(`<p>Ticking exact age stopwatch running. Uses 100ms interval ticks.</p>`);
        """
    },
    {
        "name": "Birthday Countdown Calculator",
        "slug": "birthday-countdown-calculator",
        "category": "Age Calculators",
        "icon": "🎁",
        "desc": "Check how many months, days, hours, and minutes remain until your next annual birthday celebration.",
        "formula": "Countdown = NextBirthday - Now()",
        "formula_desc": "Finds date of next birthday, runs interval counter loops to display ticking updates.",
        "auto_calc": True,
        "inputs": [
            {"id": "bcc-birth", "label": "Date of Birth:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Birthday Countdown Timer", "type": "textarea"}
        ],
        "calc_js": """
            if (window.bdayCountdownInterval) clearInterval(window.bdayCountdownInterval);
            
            const birthVal = document.getElementById('bcc-birth').value;
            if (!birthVal) {
                showToast("Please set birthdate.", "error");
                return;
            }
            
            const dob = new Date(birthVal);
            
            function tick() {
                const now = new Date();
                let nextBday = new Date(now.getFullYear(), dob.getMonth(), dob.getDate());
                if (nextBday < now) {
                    nextBday.setFullYear(now.getFullYear() + 1);
                }
                
                const diff = nextBday - now;
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                const secs = Math.floor(diff / 1000) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `        BIRTHDAY COUNTDOWN TIMER        \\n` +
                    `========================================\\n` +
                    `  Time Left: ${days} Days, ${hrs} Hours, ${mins} Mins, ${secs} Secs\\n` +
                    `========================================\\n` +
                    `Target Date: ${nextBday.toLocaleDateString()}`;
            }
            
            tick();
            window.bdayCountdownInterval = setInterval(tick, 1000);
            updateBreakdown(`<p>Birthday countdown ticking live. Next birthday resolved based on calendar month.</p>`);
        """
    },
    {
        "name": "Next Birthday Calculator",
        "slug": "next-birthday-calculator",
        "category": "Age Calculators",
        "icon": "🎂",
        "desc": "Calculate days left for your next birthday and discover what day of the week it will fall on.",
        "formula": "NextBirthdayInfo = NextBdayWeekday & DaysLeft",
        "formula_desc": "Determines days count to next birthday anniversary and maps to week weekday string index.",
        "inputs": [
            {"id": "nbc-birth", "label": "Date of Birth:", "type": "date"}
        ],
        "outputs": [
            {"id": "out-nbc-days", "label": "Days Remaining", "prefix": "", "suffix": " Days"},
            {"id": "out-nbc-day", "label": "Day of the Week", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const birthVal = document.getElementById('nbc-birth').value;
            if (!birthVal) {
                showToast("Please enter birthdate.", "error");
                return;
            }
            
            const dob = new Date(birthVal);
            const now = new Date();
            let nextBday = new Date(now.getFullYear(), dob.getMonth(), dob.getDate());
            if (nextBday < now) {
                nextBday.setFullYear(now.getFullYear() + 1);
            }
            
            const diff = nextBday - now;
            const daysLeft = Math.ceil(diff / (1000 * 60 * 60 * 24));
            
            const weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
            const targetDayName = weekdays[nextBday.getDay()];
            
            document.getElementById('out-nbc-days').textContent = daysLeft.toLocaleString();
            document.getElementById('out-nbc-day').textContent = targetDayName;
            
            updateBreakdown(`<p>Next birthday lands on a ${targetDayName}. Total full days left: ${daysLeft}.</p>`);
        """
    },
    {
        "name": "Pet Age Calculator",
        "slug": "pet-age-calculator",
        "category": "Age Calculators",
        "icon": "🐶",
        "desc": "Translate human years of dogs and cats into their biological pet age equivalent.",
        "formula": "PetAge = 1stYr(15) + 2ndYr(9) + standard(4/5 per human yr)",
        "formula_desc": "Applies standard veterinary ratios mapping pet development phases to human equivalents.",
        "inputs": [
            {"id": "pac-type", "label": "Pet Type:", "type": "select", "options": [("dog", "Dog"), ("cat", "Cat")]},
            {"id": "pac-age", "label": "Human Years:", "type": "number", "default": "1", "min": "1", "max": "30"}
        ],
        "outputs": [
            {"id": "out-pac-age", "label": "Pet Age", "prefix": "", "suffix": " Pet Years"}
        ],
        "calc_js": """
            const type = document.getElementById('pac-type').value;
            const humanYears = parseFloat(document.getElementById('pac-age').value);
            if (isNaN(humanYears) || humanYears <= 0) {
                showToast("Please enter a valid human age.", "error");
                return;
            }
            
            let petYears = 0;
            if (type === 'dog') {
                if (humanYears <= 1) {
                    petYears = humanYears * 15;
                } else if (humanYears <= 2) {
                    petYears = 15 + (humanYears - 1) * 9;
                } else {
                    petYears = 24 + (humanYears - 2) * 5; // standard medium dog rule
                }
            } else if (type === 'cat') {
                if (humanYears <= 1) {
                    petYears = humanYears * 15;
                } else if (humanYears <= 2) {
                    petYears = 15 + (humanYears - 1) * 9;
                } else {
                    petYears = 24 + (humanYears - 2) * 4;
                }
            }
            
            document.getElementById('out-pac-age').textContent = petYears.toFixed(1);
            updateBreakdown(`<p>Calculated equivalent biological age of a ${type} is ${petYears} years.</p>`);
        """
    },
    {
        "name": "Retirement Age Calculator",
        "slug": "retirement-age-calculator",
        "category": "Age Calculators",
        "icon": "🏖️",
        "desc": "Calculate how many years are left until your target retirement and find out the calendar year you will retire.",
        "formula": "YearsLeft = RetireAge - CurrentAge",
        "formula_desc": "Subtracts current age from retirement age, adding that difference to current year to find target year.",
        "inputs": [
            {"id": "rac-age", "label": "Current Age:", "type": "number", "default": "30", "min": "1", "max": "99"},
            {"id": "rac-retire", "label": "Target Retirement Age:", "type": "number", "default": "65", "min": "2", "max": "100"}
        ],
        "outputs": [
            {"id": "out-rac-years", "label": "Years Left", "prefix": "", "suffix": " Years"},
            {"id": "out-rac-year", "label": "Retirement Year", "prefix": "Year ", "suffix": ""}
        ],
        "calc_js": """
            const curAge = parseFloat(document.getElementById('rac-age').value);
            const retAge = parseFloat(document.getElementById('rac-retire').value);
            
            if (isNaN(curAge) || isNaN(retAge)) {
                showToast("Please enter numbers for age.", "error");
                return;
            }
            if (curAge >= retAge) {
                showToast("Retirement age must be greater than current age.", "error");
                return;
            }
            
            const yearsLeft = retAge - curAge;
            const currentYear = new Date().getFullYear();
            const targetYear = currentYear + Math.ceil(yearsLeft);
            
            document.getElementById('out-rac-years').textContent = yearsLeft.toFixed(0);
            document.getElementById('out-rac-year').textContent = targetYear;
            updateBreakdown(`<p>You will retire in ${yearsLeft} years, in the year ${targetYear}.</p>`);
        """
    },
    {
        "name": "Zodiac Age Calculator",
        "slug": "zodiac-age-calculator",
        "category": "Age Calculators",
        "icon": "🔮",
        "desc": "Discover your Western Zodiac and Chinese Zodiac symbols based on your birthdate.",
        "formula": "Zodiac = Sign(Birthdate)",
        "formula_desc": "Maps birthdate month/day boundaries to astrological constellations and resolves year modulo 12 for Chinese elements.",
        "inputs": [
            {"id": "zac-birth", "label": "Date of Birth:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Zodiac Profile Details", "type": "textarea"}
        ],
        "calc_js": """
            const birthVal = document.getElementById('zac-birth').value;
            if (!birthVal) {
                showToast("Please enter birthdate.", "error");
                return;
            }
            const dob = new Date(birthVal);
            const m = dob.getMonth() + 1;
            const d = dob.getDate();
            const y = dob.getFullYear();
            
            let sign = "";
            let element = "";
            
            if ((m === 3 && d >= 21) || (m === 4 && d <= 19)) { sign = "Aries"; element = "Fire"; }
            else if ((m === 4 && d >= 20) || (m === 5 && d <= 20)) { sign = "Taurus"; element = "Earth"; }
            else if ((m === 5 && d >= 21) || (m === 6 && d <= 20)) { sign = "Gemini"; element = "Air"; }
            else if ((m === 6 && d >= 21) || (m === 7 && d <= 22)) { sign = "Cancer"; element = "Water"; }
            else if ((m === 7 && d >= 23) || (m === 8 && d <= 22)) { sign = "Leo"; element = "Fire"; }
            else if ((m === 8 && d >= 23) || (m === 9 && d <= 22)) { sign = "Virgo"; element = "Earth"; }
            else if ((m === 9 && d >= 23) || (m === 10 && d <= 22)) { sign = "Libra"; element = "Air"; }
            else if ((m === 10 && d >= 23) || (m === 11 && d <= 21)) { sign = "Scorpio"; element = "Water"; }
            else if ((m === 11 && d >= 22) || (m === 12 && d <= 21)) { sign = "Sagittarius"; element = "Fire"; }
            else if ((m === 12 && d >= 22) || (m === 1 && d <= 19)) { sign = "Capricorn"; element = "Earth"; }
            else if ((m === 1 && d >= 20) || (m === 2 && d <= 18)) { sign = "Aquarius"; element = "Air"; }
            else { sign = "Pisces"; element = "Water"; }
            
            const animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"];
            const chineseIndex = (y - 4) % 12;
            const chineseAnimal = animals[chineseIndex >= 0 ? chineseIndex : chineseIndex + 12];
            
            const profile = `Astrological Zodiac Profile:\\n` +
                            `===============================\\n` +
                            ` Western Zodiac Sign : ${sign}\\n` +
                            ` Astrological Element: ${element}\\n` +
                            ` Chinese Zodiac Animal: ${chineseAnimal}\\n` +
                            `===============================\\n` +
                            `Computed from birthdate: ${dob.toLocaleDateString()}`;
            
            document.getElementById('text-output').value = profile;
            updateBreakdown(`<p>Zodiac profile completed. Elemental association: ${element}.</p>`);
        """
    },
    {
        "name": "Life Expectancy Calculator",
        "slug": "life-expectancy-calculator",
        "category": "Age Calculators",
        "icon": "🧬",
        "desc": "Check your estimated remaining lifespan and statistical average life expectancy based on demographic and lifestyle choices.",
        "formula": "LifeExpectancy = Baseline(Gender) +/- LifestyleAdjustments",
        "formula_desc": "Applies actuarial database baselines (approx. 81 for female, 76 for male) adjusting for habits.",
        "inputs": [
            {"id": "lec-gender", "label": "Gender:", "type": "select", "options": [("female", "Female"), ("male", "Male")]},
            {"id": "lec-birth", "label": "Birth Year:", "type": "number", "default": "1990", "min": "1900", "max": "2026"},
            {"id": "lec-smoke", "label": "Smoking Status:", "type": "select", "options": [("no", "Non-Smoker"), ("yes", "Active Smoker")]}
        ],
        "outputs": [
            {"id": "out-lec-expectancy", "label": "Lifespan Expectancy", "prefix": "", "suffix": " Years"},
            {"id": "out-lec-remaining", "label": "Remaining Life", "prefix": "", "suffix": " Years"}
        ],
        "calc_js": """
            const gender = document.getElementById('lec-gender').value;
            const birthYear = parseInt(document.getElementById('lec-birth').value);
            const smoke = document.getElementById('lec-smoke').value;
            
            if (isNaN(birthYear) || birthYear < 1900 || birthYear > 2026) {
                showToast("Please enter a valid birth year.", "error");
                return;
            }
            
            let baseline = gender === 'female' ? 81.1 : 76.2;
            if (smoke === 'yes') {
                baseline -= 10.0; // Statistical reduction of about 10 years
            }
            
            const currentYear = new Date().getFullYear();
            const age = currentYear - birthYear;
            let remaining = baseline - age;
            if (remaining < 1) remaining = 1; // safety minimum
            
            document.getElementById('out-lec-expectancy').textContent = baseline.toFixed(1);
            document.getElementById('out-lec-remaining').textContent = remaining.toFixed(1);
            updateBreakdown(`<p>Based on habits, average expectancy is ${baseline} years. Calculated remaining life is ${remaining.toFixed(1)} years.</p>`);
        """
    }
]

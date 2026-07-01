# -*- coding: utf-8 -*-
"""
Conversion and Business Time Tools Data
"""

CONVERSIONS_BUSINESS_TOOLS = [
    {
        "name": "Time Zone Converter",
        "slug": "time-zone-converter",
        "category": "Conversion Tools",
        "icon": "🌐",
        "desc": "Convert standard times between multiple international time zones instantly.",
        "formula": "ConvertedTime = Time + OffsetDifference",
        "formula_desc": "Translates calendar date elements relative to selected standard international offsets.",
        "inputs": [
            {"id": "tz-time", "label": "Time to Convert (HH:MM):", "type": "text", "default": "12:00"},
            {"id": "tz-from", "label": "From Time Zone:", "type": "select", "options": [
                ("UTC", "UTC (Coordinated Universal Time)"),
                ("America/New_York", "New York (EST/EDT)"),
                ("Europe/London", "London (GMT/BST)"),
                ("Asia/Kolkata", "India (IST)"),
                ("Asia/Tokyo", "Tokyo (JST)"),
                ("Australia/Sydney", "Sydney (AEST/AEDT)")
            ]},
            {"id": "tz-to", "label": "To Time Zone:", "type": "select", "options": [
                ("Asia/Kolkata", "India (IST)"),
                ("UTC", "UTC (Coordinated Universal Time)"),
                ("America/New_York", "New York (EST/EDT)"),
                ("Europe/London", "London (GMT/BST)"),
                ("Asia/Tokyo", "Tokyo (JST)"),
                ("Australia/Sydney", "Sydney (AEST/AEDT)")
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Converted Time Results", "type": "textarea"}
        ],
        "calc_js": """
            const timeStr = document.getElementById('tz-time').value || "12:00";
            const fromTz = document.getElementById('tz-from').value;
            const toTz = document.getElementById('tz-to').value;
            
            const parts = timeStr.split(':');
            const h = parseInt(parts[0]) || 0;
            const m = parseInt(parts[1]) || 0;
            
            const now = new Date();
            // Create target in fromTz
            try {
                // To do timezone conversion properly in client JS:
                // Create a formatter for the source timezone to parse the date representation
                const srcDate = new Date(now.getFullYear(), now.getMonth(), now.getDate(), h, m, 0, 0);
                
                // Format in source timezone, check offsets or use standard translation
                const optTo = { timeZone: toTz, hour: '2-digit', minute: '2-digit', hour12: true, second: '2-digit' };
                const converted = srcDate.toLocaleTimeString('en-US', optTo);
                
                document.getElementById('text-output').value = 
                    `TIME ZONE CONVERSION RESULT:\\n` +
                    `========================================\\n` +
                    ` Input Time    : ${timeStr} (${fromTz})\\n` +
                    ` Converted Time: ${converted} (${toTz})\\n` +
                    `========================================`;
            } catch(e) {
                document.getElementById('text-output').value = "Error parsing timezone details: " + e.message;
            }
            updateBreakdown("<p>Resolved timezone translation metrics.</p>");
        """
    },
    {
        "name": "Unix Timestamp Converter",
        "slug": "unix-timestamp-converter",
        "category": "Conversion Tools",
        "icon": "💻",
        "desc": "Translate 10-digit Unix timestamps into readable local and UTC dates.",
        "formula": "Date = UnixTimestamp * 1000",
        "formula_desc": "Multiplies Unix seconds index by 1000 to construct standard browser Date objects.",
        "inputs": [
            {"id": "utc-ts", "label": "Unix Timestamp (seconds):", "type": "text", "default": "1774212000"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Converted Date Dashboard", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('utc-ts').value.trim();
            if (!val) {
                showToast("Please enter a timestamp.", "error");
                return;
            }
            const ts = parseInt(val);
            if (isNaN(ts)) {
                showToast("Invalid numeric format.", "error");
                return;
            }
            
            // Handle seconds vs milliseconds detection
            const isMs = val.length > 11;
            const date = new Date(isMs ? ts : ts * 1000);
            
            const localStr = date.toString();
            const utcStr = date.toUTCString();
            const isoStr = date.toISOString();
            
            document.getElementById('text-output').value = 
                `UNIX TIMESTAMP TRANSLATION:\\n` +
                `========================================\\n` +
                ` Unix Epoch : ${ts}\\n` +
                ` UTC Time   : ${utcStr}\\n` +
                ` Local Time : ${localStr}\\n` +
                ` ISO-8601   : ${isoStr}\\n` +
                `========================================`;
            updateBreakdown("<p>Timestamp conversion processed successfully.</p>");
        """
    },
    {
        "name": "Epoch Converter",
        "slug": "epoch-converter",
        "category": "Conversion Tools",
        "icon": "📆",
        "desc": "Convert standard calendar dates to seconds and milliseconds Unix Epoch timestamps.",
        "formula": "Epoch = Date.getTime() / 1000",
        "formula_desc": "Finds milliseconds from 1970-01-01 and divides by 1000 to determine Unix seconds index.",
        "inputs": [
            {"id": "ec-date", "label": "Select Date:", "type": "date"},
            {"id": "ec-time", "label": "Time (24h format):", "type": "text", "default": "12:00"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Epoch Output Details", "type": "textarea"}
        ],
        "calc_js": """
            const dVal = document.getElementById('ec-date').value;
            const tVal = document.getElementById('ec-time').value || "00:00";
            if (!dVal) {
                showToast("Please choose a date.", "error");
                return;
            }
            
            const date = new Date(dVal);
            const parts = tVal.split(':');
            date.setHours(parseInt(parts[0])||0, parseInt(parts[1])||0, 0, 0);
            
            const ms = date.getTime();
            const secs = Math.floor(ms / 1000);
            
            document.getElementById('text-output').value = 
                `CALENDAR DATE TO EPOCH DETAILS:\\n` +
                `========================================\\n` +
                ` Date Selected : ${date.toLocaleString()}\\n` +
                ` Unix Seconds  : ${secs}\\n` +
                ` Unix Millis   : ${ms}\\n` +
                `========================================`;
            updateBreakdown("<p>Converted calendar timestamp into epoch seconds and milliseconds.</p>");
        """
    },
    {
        "name": "12 Hour To 24 Hour Converter",
        "slug": "12-hour-to-24-hour-converter",
        "category": "Conversion Tools",
        "icon": "🎖️",
        "desc": "Translate standard 12-hour (AM/PM) clock time into 24-hour military values.",
        "formula": "24H = HH + 12 (if PM and HH != 12) / 00 (if AM and HH == 12)",
        "formula_desc": "Applies standard military time translation logic to map AM/PM markers to 24-hour limits.",
        "inputs": [
            {"id": "c12-time", "label": "Standard Time (HH:MM):", "type": "text", "default": "02:30"},
            {"id": "c12-ampm", "label": "Period Indicator:", "type": "select", "options": [("pm", "PM"), ("am", "AM")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "24-Hour Military Format", "type": "textarea"}
        ],
        "calc_js": """
            const timeStr = document.getElementById('c12-time').value.trim();
            const ampm = document.getElementById('c12-ampm').value;
            
            const parts = timeStr.split(':');
            if (parts.length < 2) {
                showToast("Please enter time in HH:MM format.", "error");
                return;
            }
            
            let hr = parseInt(parts[0]);
            let min = parseInt(parts[1]) || 0;
            
            if (isNaN(hr) || hr < 1 || hr > 12 || min < 0 || min > 59) {
                showToast("Invalid 12-hour time bounds.", "error");
                return;
            }
            
            let militaryHr = hr;
            if (ampm === 'pm' && hr !== 12) militaryHr += 12;
            if (ampm === 'am' && hr === 12) militaryHr = 0;
            
            const milStr = `${militaryHr.toString().padStart(2, '0')}:${min.toString().padStart(2, '0')}`;
            
            document.getElementById('text-output').value = 
                `12-HOUR TO 24-HOUR RESULT:\\n` +
                `========================================\\n` +
                ` 12-Hour Input : ${timeStr} ${ampm.toUpperCase()}\\n` +
                ` 24-Hour Output: ${milStr}\\n` +
                `========================================`;
            updateBreakdown("<p>12-hour AM/PM structure parsed to 24-hour index.</p>");
        """
    },
    {
        "name": "24 Hour To 12 Hour Converter",
        "slug": "24-hour-to-12-hour-converter",
        "category": "Conversion Tools",
        "icon": "🕰️",
        "desc": "Convert 24-hour military clock values into standard 12-hour (AM/PM) format.",
        "formula": "12H = (H % 12 || 12) + (H >= 12 ? PM : AM)",
        "formula_desc": "Evaluates hour index modulo 12 and assigns AM or PM period markers accordingly.",
        "inputs": [
            {"id": "c24-time", "label": "24-Hour Military Time (HH:MM):", "type": "text", "default": "14:30"}
        ],
        "outputs": [
            {"id": "text-output", "label": "12-Hour Output Format", "type": "textarea"}
        ],
        "calc_js": """
            const timeStr = document.getElementById('c24-time').value.trim();
            const parts = timeStr.split(':');
            if (parts.length < 2) {
                showToast("Please enter military time in HH:MM format.", "error");
                return;
            }
            let hr = parseInt(parts[0]);
            let min = parseInt(parts[1]) || 0;
            
            if (isNaN(hr) || hr < 0 || hr > 23 || min < 0 || min > 59) {
                showToast("Invalid 24-hour clock limits.", "error");
                return;
            }
            
            const ampm = hr >= 12 ? "PM" : "AM";
            let displayHr = hr % 12;
            if (displayHr === 0) displayHr = 12;
            
            const outStr = `${displayHr.toString().padStart(2, '0')}:${min.toString().padStart(2, '0')} ${ampm}`;
            
            document.getElementById('text-output').value = 
                `24-HOUR TO 12-HOUR RESULT:\\n` +
                `========================================\\n` +
                ` 24-Hour Input : ${timeStr}\\n` +
                ` 12-Hour Output: ${outStr}\\n` +
                `========================================`;
            updateBreakdown("<p>Parsed 24-hour military index to 12-hour AM/PM schedule.</p>");
        """
    },
    {
        "name": "Seconds Converter",
        "slug": "seconds-converter",
        "category": "Conversion Tools",
        "icon": "⚡",
        "desc": "Convert seconds into minutes, hours, days, and fractional weeks.",
        "formula": "Minutes = Secs / 60, Hours = Secs / 3600",
        "formula_desc": "Applies standard fractional division indexes to resolve seconds into bulk time categories.",
        "inputs": [
            {"id": "sc-secs", "label": "Enter Seconds:", "type": "number", "default": "86400", "min": "0"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Time Category Breakdown", "type": "textarea"}
        ],
        "calc_js": """
            const secs = parseFloat(document.getElementById('sc-secs').value);
            if (isNaN(secs) || secs < 0) {
                showToast("Please enter a non-negative number.", "error");
                return;
            }
            
            const ms = secs * 1000;
            const mins = secs / 60;
            const hrs = secs / 3600;
            const days = secs / 86400;
            const weeks = secs / (86400 * 7);
            
            document.getElementById('text-output').value = 
                `SECONDS CONVERSION BREAKDOWN:\\n` +
                `========================================\\n` +
                `- Milliseconds : ${ms.toLocaleString()} ms\\n` +
                `- Minutes      : ${mins.toFixed(4)} min\\n` +
                `- Hours        : ${hrs.toFixed(4)} hrs\\n` +
                `- Days         : ${days.toFixed(4)} days\\n` +
                `- Weeks        : ${weeks.toFixed(4)} weeks\\n` +
                `========================================`;
            updateBreakdown("<p>Unit scaling completed.</p>");
        """
    },
    {
        "name": "Minutes Converter",
        "slug": "minutes-converter",
        "category": "Conversion Tools",
        "icon": "⏰",
        "desc": "Convert minute values into seconds, hours, and calendar day counts.",
        "formula": "Seconds = Mins * 60, Hours = Mins / 60",
        "formula_desc": "Multiplies or divides inputs based on standard hourly cycles (60 minutes per hour).",
        "inputs": [
            {"id": "mc-mins", "label": "Enter Minutes:", "type": "number", "default": "1440", "min": "0"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Time Category Breakdown", "type": "textarea"}
        ],
        "calc_js": """
            const mins = parseFloat(document.getElementById('mc-mins').value);
            if (isNaN(mins) || mins < 0) {
                showToast("Please enter minutes.", "error");
                return;
            }
            const secs = mins * 60;
            const hrs = mins / 60;
            const days = mins / 1440;
            
            document.getElementById('text-output').value = 
                `MINUTES CONVERSION DETAILS:\\n` +
                `========================================\\n` +
                `- Seconds : ${secs.toLocaleString()} s\\n` +
                `- Hours   : ${hrs.toFixed(4)} hours\\n` +
                `- Days    : ${days.toFixed(4)} days\\n` +
                `========================================`;
            updateBreakdown("<p>Minute metric scaling completed.</p>");
        """
    },
    {
        "name": "Hours Converter",
        "slug": "hours-converter",
        "category": "Conversion Tools",
        "icon": "⏳",
        "desc": "Translate hours into equivalent seconds, minutes, days, and calendar weeks.",
        "formula": "Minutes = Hours * 60, Days = Hours / 24",
        "formula_desc": "Scales hours using chronological multiples matching solar days and weeks.",
        "inputs": [
            {"id": "hc-hours", "label": "Enter Hours:", "type": "number", "default": "48", "min": "0"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Time Category Breakdown", "type": "textarea"}
        ],
        "calc_js": """
            const hrs = parseFloat(document.getElementById('hc-hours').value);
            if (isNaN(hrs) || hrs < 0) {
                showToast("Please input positive hours.", "error");
                return;
            }
            const mins = hrs * 60;
            const secs = mins * 60;
            const days = hrs / 24;
            const weeks = days / 7;
            
            document.getElementById('text-output').value = 
                `HOURS CONVERSION DETAILS:\\n` +
                `========================================\\n` +
                `- Seconds : ${secs.toLocaleString()} s\\n` +
                `- Minutes : ${mins.toLocaleString()} min\\n` +
                `- Days    : ${days.toFixed(3)} days\\n` +
                `- Weeks   : ${weeks.toFixed(3)} weeks\\n` +
                `========================================`;
            updateBreakdown("<p>Hour conversions solved.</p>");
        """
    },
    {
        "name": "Days Converter",
        "slug": "days-converter",
        "category": "Conversion Tools",
        "icon": "📅",
        "desc": "Convert calendar day counts into equivalent weeks, months, and hours.",
        "formula": "Weeks = Days / 7, Hours = Days * 24",
        "formula_desc": "Applies solar day divisions to evaluate week portions and hourly totals.",
        "inputs": [
            {"id": "dc-days", "label": "Enter Days:", "type": "number", "default": "30", "min": "0"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Time Category Breakdown", "type": "textarea"}
        ],
        "calc_js": """
            const days = parseFloat(document.getElementById('dc-days').value);
            if (isNaN(days) || days < 0) {
                showToast("Invalid day count.", "error");
                return;
            }
            const hrs = days * 24;
            const mins = hrs * 60;
            const weeks = days / 7;
            const months = days / 30.4375; // average Gregorian month
            
            document.getElementById('text-output').value = 
                `DAYS CONVERSION DETAILS:\\n` +
                `========================================\\n` +
                `- Hours   : ${hrs.toLocaleString()} hrs\\n` +
                `- Minutes : ${mins.toLocaleString()} min\\n` +
                `- Weeks   : ${weeks.toFixed(2)} weeks\\n` +
                `- Months  : ${months.toFixed(2)} months\\n` +
                `========================================`;
            updateBreakdown("<p>Day metric conversions computed.</p>");
        """
    },
    {
        "name": "Date Format Converter",
        "slug": "date-format-converter",
        "category": "Conversion Tools",
        "icon": "🗄️",
        "desc": "Translate standard calendar dates into multiple string styles (ISO-8601, RFC-2822, UNIX, DD/MM/YYYY, etc.).",
        "formula": "Formats = Map(Date, StyleString)",
        "formula_desc": "Parses date inputs and extracts locale components matching standard technical formatting patterns.",
        "inputs": [
            {"id": "df-date", "label": "Select Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted Date Formats", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('df-date').value;
            if (!val) {
                showToast("Please choose a date.", "error");
                return;
            }
            const date = new Date(val);
            
            const iso = date.toISOString().split('T')[0];
            const us = `${date.getMonth()+1}/${date.getDate()}/${date.getFullYear()}`;
            const eu = `${date.getDate().toString().padStart(2,'0')}/${(date.getMonth()+1).toString().padStart(2,'0')}/${date.getFullYear()}`;
            const textStr = date.toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
            
            document.getElementById('text-output').value = 
                `DATE STRUCTURE STYLES:\\n` +
                `========================================\\n` +
                `- ISO Format : ${iso}\\n` +
                `- US Format  : ${us} (MM/DD/YYYY)\\n` +
                `- EU Format  : ${eu} (DD/MM/YYYY)\\n` +
                `- Full Text  : ${textStr}\\n` +
                `========================================`;
            updateBreakdown("<p>Alternative date strings constructed.</p>");
        """
    },
    {
        "name": "Payroll Hours Calculator",
        "slug": "payroll-hours-calculator",
        "category": "Business Time Tools",
        "icon": "💵",
        "desc": "Calculate gross payroll earnings by combining working hours and overtime rates.",
        "formula": "GrossPay = (RegularHours * Rate) + (OvertimeHours * Rate * OvertimeMultiplier)",
        "formula_desc": "Multiplies regular hours by standard hourly rate and adds scaled overtime increments.",
        "inputs": [
            {"id": "ph-hours", "label": "Regular Hours Worked:", "type": "number", "default": "40", "min": "0", "max": "168"},
            {"id": "ph-rate", "label": "Hourly Pay Rate ($):", "type": "number", "default": "25", "min": "0"},
            {"id": "ph-othours", "label": "Overtime Hours:", "type": "number", "default": "5", "min": "0", "max": "100"},
            {"id": "ph-otmult", "label": "Overtime Multiplier:", "type": "select", "options": [("1.5", "1.5x (Time & a Half)"), ("2.0", "2.0x (Double Time)"), ("1.0", "1.0x (Regular)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Payroll Earnings Statement", "type": "textarea"}
        ],
        "calc_js": """
            const regHours = parseFloat(document.getElementById('ph-hours').value) || 0;
            const payRate = parseFloat(document.getElementById('ph-rate').value) || 0;
            const otHours = parseFloat(document.getElementById('ph-othours').value) || 0;
            const otMult = parseFloat(document.getElementById('ph-otmult').value) || 1.5;
            
            const regPay = regHours * payRate;
            const otPay = otHours * payRate * otMult;
            const grossPay = regPay + otPay;
            
            document.getElementById('text-output').value = 
                `GROSS PAYROLL EARNINGS STATEMENT:\\n` +
                `========================================\\n` +
                ` Regular Hours : ${regHours} hrs @ $${payRate.toFixed(2)}/hr\\n` +
                ` Regular Pay   : $${regPay.toFixed(2)}\\n` +
                ` Overtime Hours: ${otHours} hrs @ $${(payRate * otMult).toFixed(2)}/hr\\n` +
                ` Overtime Pay  : $${otPay.toFixed(2)}\\n` +
                `----------------------------------------\\n` +
                ` Gross Pay     : $${grossPay.toFixed(2)}\\n` +
                `========================================`;
            updateBreakdown("<p>Gross earnings calculated.</p>");
        """
    },
    {
        "name": "Employee Time Tracker",
        "slug": "employee-time-tracker",
        "category": "Business Time Tools",
        "icon": "🕒",
        "desc": "Track employee shifts by logging custom clock-in and clock-out hours.",
        "formula": "ShiftDuration = ClockOut - ClockIn - LunchBreak",
        "formula_desc": "Solves elapsed decimal hours from clock-in and clock-out timestamps, excluding break minutes.",
        "inputs": [
            {"id": "ett-in", "label": "Clock In Time (HH:MM):", "type": "text", "default": "09:00"},
            {"id": "ett-out", "label": "Clock Out Time (HH:MM):", "type": "text", "default": "17:00"},
            {"id": "ett-break", "label": "Lunch Break (minutes):", "type": "number", "default": "30", "min": "0", "max": "180"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Shift Time Summary", "type": "textarea"}
        ],
        "calc_js": """
            const clockIn = document.getElementById('ett-in').value || "09:00";
            const clockOut = document.getElementById('ett-out').value || "17:00";
            const lunchMins = parseFloat(document.getElementById('ett-break').value) || 0;
            
            const inParts = clockIn.split(':');
            const outParts = clockOut.split(':');
            
            let inMin = (parseInt(inParts[0]) || 0) * 60 + (parseInt(inParts[1]) || 0);
            let outMin = (parseInt(outParts[0]) || 0) * 60 + (parseInt(outParts[1]) || 0);
            
            // Handle overnight shifts
            if (outMin < inMin) {
                outMin += 24 * 60;
            }
            
            let workMin = outMin - inMin - lunchMins;
            if (workMin < 0) workMin = 0;
            
            const hours = workMin / 60;
            
            document.getElementById('text-output').value = 
                `SHIFT TRACKER SUMMARY:\\n` +
                `========================================\\n` +
                ` Clock-In    : ${clockIn}\\n` +
                ` Clock-Out   : ${clockOut}\\n` +
                ` Lunch Break : ${lunchMins} minutes\\n` +
                `----------------------------------------\\n` +
                ` Total Worked: ${hours.toFixed(2)} hours\\n` +
                `========================================`;
            updateBreakdown("<p>Shift decimal hours computed successfully.</p>");
        """
    },
    {
        "name": "Timesheet Calculator",
        "slug": "timesheet-calculator",
        "category": "Business Time Tools",
        "icon": "📆",
        "desc": "Calculate total weekly working hours by inputting daily working shifts.",
        "formula": "WeeklyHours = Sum(DailyHours)",
        "formula_desc": "Sums shifts recorded across 5 days (Monday to Friday) to compute the weekly total.",
        "inputs": [
            {"id": "tc-mon", "label": "Monday Shift Hours (e.g. 8.0):", "type": "number", "default": "8.0", "min": "0", "max": "24", "step": "0.1"},
            {"id": "tc-tue", "label": "Tuesday Shift Hours:", "type": "number", "default": "8.0", "min": "0", "max": "24", "step": "0.1"},
            {"id": "tc-wed", "label": "Wednesday Shift Hours:", "type": "number", "default": "8.0", "min": "0", "max": "24", "step": "0.1"},
            {"id": "tc-thu", "label": "Thursday Shift Hours:", "type": "number", "default": "8.0", "min": "0", "max": "24", "step": "0.1"},
            {"id": "tc-fri", "label": "Friday Shift Hours:", "type": "number", "default": "8.0", "min": "0", "max": "24", "step": "0.1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Timesheet Overview", "type": "textarea"}
        ],
        "calc_js": """
            const mon = parseFloat(document.getElementById('tc-mon').value) || 0;
            const tue = parseFloat(document.getElementById('tc-tue').value) || 0;
            const wed = parseFloat(document.getElementById('tc-wed').value) || 0;
            const thu = parseFloat(document.getElementById('tc-thu').value) || 0;
            const fri = parseFloat(document.getElementById('tc-fri').value) || 0;
            
            const total = mon + tue + wed + thu + fri;
            
            document.getElementById('text-output').value = 
                `WEEKLY TIMESHEET SUMMARY:\\n` +
                `========================================\\n` +
                ` Mon: ${mon.toFixed(1)} hrs | Tue: ${tue.toFixed(1)} hrs\\n` +
                ` Wed: ${wed.toFixed(1)} hrs | Thu: ${thu.toFixed(1)} hrs\\n` +
                ` Fri: ${fri.toFixed(1)} hrs\\n` +
                `----------------------------------------\\n` +
                ` Total Weekly Hours: ${total.toFixed(1)} hours\\n` +
                `========================================`;
            updateBreakdown("<p>Weekly timesheet log summation completed.</p>");
        """
    },
    {
        "name": "Attendance Calculator",
        "slug": "attendance-calculator",
        "category": "Business Time Tools",
        "icon": "📋",
        "desc": "Calculate attendance rates and see the minimum classes needed to meet target percentage rules.",
        "formula": "AttendanceRate = (Attended / Total) * 100",
        "formula_desc": "Finds percentage of attended slots relative to total scheduled shifts or classroom courses.",
        "inputs": [
            {"id": "ac-attended", "label": "Classes / Shifts Attended:", "type": "number", "default": "38", "min": "0"},
            {"id": "ac-total", "label": "Total Classes / Shifts:", "type": "number", "default": "45", "min": "1"},
            {"id": "ac-target", "label": "Target Percentage (%):", "type": "number", "default": "75", "min": "10", "max": "100"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Attendance Report Details", "type": "textarea"}
        ],
        "calc_js": """
            const att = parseFloat(document.getElementById('ac-attended').value) || 0;
            const tot = parseFloat(document.getElementById('ac-total').value) || 0;
            const tgt = parseFloat(document.getElementById('ac-target').value) || 75;
            
            if (att > tot) {
                showToast("Attended classes cannot exceed total classes.", "error");
                return;
            }
            
            const rate = (att / tot) * 100;
            let status = "";
            let recommendation = "";
            
            if (rate >= tgt) {
                status = "COMPLIANT";
                // How many can they miss
                let safeMiss = 0;
                while (((att) / (tot + safeMiss + 1)) * 100 >= tgt) {
                    safeMiss++;
                }
                recommendation = `You can safely miss the next ${safeMiss} classes/shifts and stay above ${tgt}%.`;
            } else {
                status = "NON-COMPLIANT";
                let needed = 0;
                while (((att + needed) / (tot + needed)) * 100 < tgt) {
                    needed++;
                }
                recommendation = `You must attend the next ${needed} consecutive classes/shifts to reach ${tgt}%.`;
            }
            
            document.getElementById('text-output').value = 
                `ATTENDANCE COMPLIANCE REPORT:\\n` +
                `========================================\\n` +
                ` Current Rate: ${rate.toFixed(2)}%\\n` +
                ` Target Rate : ${tgt}%\\n` +
                ` Status      : ${status}\\n` +
                `----------------------------------------\\n` +
                ` Recommendation:\\n` +
                ` ${recommendation}\\n` +
                `========================================`;
            updateBreakdown("<p>Attendance rates and thresholds evaluated.</p>");
        """
    },
    {
        "name": "Work Hours Calculator",
        "slug": "work-hours-calculator",
        "category": "Business Time Tools",
        "icon": "⏳",
        "desc": "Calculate shift duration excluding custom break limits.",
        "formula": "WorkHours = ShiftDuration - BreakDuration",
        "formula_desc": "Translates shift start and end times, subtracting custom rest gaps to determine total working hours.",
        "inputs": [
            {"id": "wh-start", "label": "Shift Start (HH:MM):", "type": "text", "default": "08:30"},
            {"id": "wh-end", "label": "Shift End (HH:MM):", "type": "text", "default": "17:00"},
            {"id": "wh-break", "label": "Break Time (minutes):", "type": "number", "default": "45", "min": "0", "max": "180"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Shift Output", "type": "textarea"}
        ],
        "calc_js": """
            const startVal = document.getElementById('wh-start').value || "08:30";
            const endVal = document.getElementById('wh-end').value || "17:00";
            const breakMins = parseFloat(document.getElementById('wh-break').value) || 0;
            
            const startParts = startVal.split(':');
            const endParts = endVal.split(':');
            
            let startMin = (parseInt(startParts[0]) || 0) * 60 + (parseInt(startParts[1]) || 0);
            let endMin = (parseInt(endParts[0]) || 0) * 60 + (parseInt(endParts[1]) || 0);
            
            if (endMin < startMin) {
                endMin += 24 * 60;
            }
            
            let totalWorkedMins = endMin - startMin - breakMins;
            if (totalWorkedMins < 0) totalWorkedMins = 0;
            
            const hours = totalWorkedMins / 60;
            
            document.getElementById('text-output').value = 
                `WORK HOURS COMPUTATION:\\n` +
                `========================================\\n` +
                ` Shift Start : ${startVal}\\n` +
                ` Shift End   : ${endVal}\\n` +
                ` Break Time  : ${breakMins} minutes\\n` +
                `----------------------------------------\\n` +
                ` Active Hours: ${hours.toFixed(2)} hours\\n` +
                `========================================`;
            updateBreakdown("<p>Shift parameters parsed.</p>");
        """
    },
    {
        "name": "Shift Duration Calculator",
        "slug": "shift-duration-calculator",
        "category": "Business Time Tools",
        "icon": "🏭",
        "desc": "Calculate total duration for regular or overnight shifts.",
        "formula": "ShiftHours = OutTime - InTime",
        "formula_desc": "Tracks elapsed hours, adjusting for overnight shifts crossing midnight boundaries.",
        "inputs": [
            {"id": "sdc-in", "label": "Shift In (HH:MM):", "type": "text", "default": "22:00"},
            {"id": "sdc-out", "label": "Shift Out (HH:MM):", "type": "text", "default": "06:00"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Shift Time Summary", "type": "textarea"}
        ],
        "calc_js": """
            const clockIn = document.getElementById('sdc-in').value || "22:00";
            const clockOut = document.getElementById('sdc-out').value || "06:00";
            
            const inParts = clockIn.split(':');
            const outParts = clockOut.split(':');
            
            let inMin = (parseInt(inParts[0]) || 0) * 60 + (parseInt(inParts[1]) || 0);
            let outMin = (parseInt(outParts[0]) || 0) * 60 + (parseInt(outParts[1]) || 0);
            
            let flag = "";
            if (outMin < inMin) {
                outMin += 24 * 60;
                flag = " (Overnight Shift)";
            }
            
            const diffMin = outMin - inMin;
            const hours = diffMin / 60;
            
            document.getElementById('text-output').value = 
                `SHIFT DURATION SUMMARY:\\n` +
                `========================================\\n` +
                ` Clock-In : ${clockIn}\\n` +
                ` Clock-Out: ${clockOut}${flag}\\n` +
                `----------------------------------------\\n` +
                ` Total    : ${hours.toFixed(2)} hours (${diffMin} minutes)\\n` +
                `========================================`;
            updateBreakdown("<p>Hourly shift parameters calculated.</p>");
        """
    },
    {
        "name": "Billable Hours Calculator",
        "slug": "billable-hours-calculator",
        "category": "Business Time Tools",
        "icon": "💵",
        "desc": "Find total invoice values by inputting client rates and billable hour metrics.",
        "formula": "InvoiceTotal = BillableHours * HourlyRate",
        "formula_desc": "Multiplies billable working hours by flat client rates to yield the gross invoice total.",
        "inputs": [
            {"id": "bh-hours", "label": "Billable Hours:", "type": "number", "default": "25.5", "min": "0", "step": "0.1"},
            {"id": "bh-rate", "label": "Hourly Rate ($):", "type": "number", "default": "75", "min": "0"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Invoice Projection Details", "type": "textarea"}
        ],
        "calc_js": """
            const hrs = parseFloat(document.getElementById('bh-hours').value) || 0;
            const rate = parseFloat(document.getElementById('bh-rate').value) || 0;
            
            const invoice = hrs * rate;
            
            document.getElementById('text-output').value = 
                `BILLABLE HOURS INVOICE SUMMARY:\\n` +
                `========================================\\n` +
                ` Billable Hours: ${hrs} hours\\n` +
                ` Hourly Rate   : $${rate.toFixed(2)} / hr\\n` +
                `----------------------------------------\\n` +
                ` Invoice Total : $${invoice.toFixed(2)}\\n` +
                `========================================`;
            updateBreakdown("<p>Freelance invoice billing totals resolved.</p>");
        """
    },
    {
        "name": "Freelancer Time Tracker",
        "slug": "freelancer-time-tracker",
        "category": "Business Time Tools",
        "icon": "💻",
        "desc": "A tracking timer for freelancers to log active client tasks and estimate invoice earnings.",
        "formula": "Earnings = ElapsedHours * BillingRate",
        "formula_desc": "Integrates ticking timing loops with billing variables to display earnings in real-time.",
        "inputs": [
            {"id": "ftt-rate", "label": "Client Billing Rate ($/hr):", "type": "number", "default": "50", "min": "0"},
            {"id": "ftt-act", "label": "Tracker Action:", "type": "select", "options": [
                ("start", "Start Tracking"),
                ("stop", "Stop & Log Task")
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Freelancer Earnings Ledger", "type": "textarea"}
        ],
        "calc_js": """
            if (!window.fttState) {
                window.fttState = { running: false, elapsed: 0, start: 0, interval: null };
            }
            const act = document.getElementById('ftt-act').value;
            const rate = parseFloat(document.getElementById('ftt-rate').value) || 50;
            
            if (act === 'start') {
                if (window.fttState.running) return;
                window.fttState.running = true;
                window.fttState.start = Date.now() - window.fttState.elapsed;
                window.fttState.interval = setInterval(() => {
                    window.fttState.elapsed = Date.now() - window.fttState.start;
                    const sec = Math.floor(window.fttState.elapsed / 1000);
                    const hours = sec / 3600;
                    const earnings = hours * rate;
                    document.getElementById('text-output').value = `TRACKING TASK...\\nTime: ${sec}s\\nEst. Earnings: $${earnings.toFixed(4)}`;
                }, 1000);
                showToast("Freelance tracking active!");
            } else {
                if (!window.fttState.running) return;
                window.fttState.running = false;
                clearInterval(window.fttState.interval);
                const finalSecs = window.fttState.elapsed / 1000;
                const hours = finalSecs / 3600;
                const earnings = hours * rate;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `          FREELANCE TASK REPORT          \\n` +
                    `========================================\\n` +
                    ` Billable Hours: ${hours.toFixed(5)} hours\\n` +
                    ` Rate          : $${rate.toFixed(2)}/hr\\n` +
                    ` Total Earned  : $${earnings.toFixed(2)}\\n` +
                    `========================================`;
                showToast("Task tracking paused.");
            }
            updateBreakdown("<p>Freelance tracker adjustments applied.</p>");
        """
    },
    {
        "name": "Project Time Calculator",
        "slug": "project-time-calculator",
        "category": "Business Time Tools",
        "icon": "📊",
        "desc": "Aggregate multiple employee and task sprint times into a master project total.",
        "formula": "ProjectTotal = Sum(SprintIntervals)",
        "formula_desc": "Combines list of hours and minutes inputs to represent the total cumulative project investment.",
        "inputs": [
            {"id": "ptc-logs", "label": "Sprint Logs (Hours:Minutes per line):", "type": "textarea", "default": "4:30\\n12:15\\n8:45\\n2:00"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Aggregated Project Total", "type": "textarea"}
        ],
        "calc_js": """
            const logs = document.getElementById('ptc-logs').value;
            let totalMins = 0;
            
            const lines = logs.split('\\n');
            lines.forEach(l => {
                if (!l.includes(':')) return;
                const parts = l.split(':');
                const hrs = parseInt(parts[0]) || 0;
                const mins = parseInt(parts[1]) || 0;
                totalMins += hrs * 60 + mins;
            });
            
            const totalHours = Math.floor(totalMins / 60);
            const remainingMins = totalMins % 60;
            
            document.getElementById('text-output').value = 
                `PROJECT TIME AGGREGATION REPORT:\\n` +
                `========================================\\n` +
                ` Total Mins : ${totalMins.toLocaleString()} minutes\\n` +
                `----------------------------------------\\n` +
                ` Net Total  : ${totalHours} hours, ${remainingMins} minutes\\n` +
                ` Decimal Hrs: ${(totalMins / 60).toFixed(2)} hours\\n` +
                `========================================`;
            updateBreakdown("<p>Sprint values summed.</p>");
        """
    },
    {
        "name": "Productivity Hours Calculator",
        "slug": "productivity-hours-calculator",
        "category": "Business Time Tools",
        "icon": "📈",
        "desc": "Measure the ratio of productive working hours relative to total clocked shift times.",
        "formula": "ProductivityRatio = (ProductiveHours / TotalHours) * 100",
        "formula_desc": "Compares active working hours against the gross shift budget to calculate work efficiency.",
        "inputs": [
            {"id": "prc-total", "label": "Total Clocked Shift (hours):", "type": "number", "default": "8.0", "min": "1", "max": "24", "step": "0.1"},
            {"id": "prc-productive", "label": "Active Productive Hours:", "type": "number", "default": "5.5", "min": "0", "max": "24", "step": "0.1"}
        ],
        "outputs": [
            {"id": "out-prc-score", "label": "Productivity Score", "prefix": "", "suffix": "%"}
        ],
        "calc_js": """
            const total = parseFloat(document.getElementById('prc-total').value) || 8;
            const productive = parseFloat(document.getElementById('prc-productive').value) || 0;
            
            if (productive > total) {
                showToast("Productive hours cannot exceed shift hours.", "error");
                return;
            }
            
            const ratio = (productive / total) * 100;
            document.getElementById('out-prc-score').textContent = ratio.toFixed(1);
            updateBreakdown(`<p>Shift productivity ratio evaluated. Productive portion: ${ratio.toFixed(1)}%.</p>`);
        """
    }
]

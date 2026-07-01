# -*- coding: utf-8 -*-
"""
Database of 10 Date & Time Tools for Enginewheels
"""

DATE_TIME_TOOLS = [
    {
        "category": "Date & Time Tools",
        "name": "Unix Timestamp Converter",
        "slug": "unix-timestamp-converter",
        "desc": "Convert Unix epoch timestamps to human-readable dates and vice-versa.",
        "formula": "new Date(timestamp * 1000) <=> timestamp / 1000",
        "formula_desc": "Converts Unix epoch seconds to JavaScript Date objects and outputs ISO date strings.",
        "icon": "🕒",
        "inputs": [
            {"id": "ts-input", "label": "Enter Unix Timestamp (seconds):", "type": "text", "default": "1782121200"}
        ],
        "outputs": [
            {"id": "out-date", "label": "Human Readable Date (Local):", "type": "text"},
            {"id": "out-iso", "label": "ISO 8601 String (UTC):", "type": "text"}
        ],
        "calc_js": """
            const val = document.getElementById('ts-input').value.trim();
            if (!val) {
                showToast("Please enter a timestamp.", "error");
                return;
            }
            const ts = parseInt(val);
            if (isNaN(ts)) {
                showToast("Invalid timestamp integer.", "error");
                return;
            }
            try {
                // Determine if ms or seconds
                const date = new Date(ts > 99999999999 ? ts : ts * 1000);
                document.getElementById('out-date').textContent = date.toString();
                document.getElementById('out-iso').textContent = date.toISOString();
                updateBreakdown(`<p class='text-success'>Resolved successfully. Local time offset: ${date.getTimezoneOffset()} minutes.</p>`);
            } catch(e) {
                showToast("Conversion failed!", "error");
            }
        """
    },
    {
        "category": "Date & Time Tools",
        "name": "Epoch Converter",
        "slug": "epoch-converter-dev",
        "desc": "Bi-directional epoch time converter featuring a live ticking Unix clock.",
        "formula": "Date.now() / 1000",
        "formula_desc": "Evaluates client system time continuously to render ticking Unix seconds.",
        "icon": "🕒",
        "inputs": [
            {"id": "epoch-val", "label": "Enter Epoch Timestamp:", "type": "text", "default": "1782121200"}
        ],
        "outputs": [
            {"id": "out-local", "label": "Local Time String:", "type": "text"},
            {"id": "out-utc", "label": "UTC Time:", "type": "text"}
        ],
        "calc_js": """
            const val = document.getElementById('epoch-val').value.trim();
            if (!val) {
                showToast("Please enter a timestamp.", "error");
                return;
            }
            const ts = parseInt(val);
            if (isNaN(ts)) {
                showToast("Invalid integer.", "error");
                return;
            }
            const date = new Date(ts * 1000);
            document.getElementById('out-local').textContent = date.toLocaleString();
            document.getElementById('out-utc').textContent = date.toUTCString();
            updateBreakdown("<p class='text-success'>Epoch converted successfully.</p>");
        """
    },
    {
        "category": "Date & Time Tools",
        "name": "Date Formatter",
        "slug": "date-formatter",
        "desc": "Format date elements into multiple calendar standard formats.",
        "formula": "Date Formatting Parser",
        "formula_desc": "Extracts years, months, and days properties from calendar inputs to assemble specific localized layouts.",
        "icon": "📅",
        "inputs": [
            {"id": "date-val", "label": "Choose Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "out-d1", "label": "Format YYYY-MM-DD:", "type": "text"},
            {"id": "out-d2", "label": "Format DD/MM/YYYY:", "type": "text"},
            {"id": "out-d3", "label": "Format Month DD, YYYY:", "type": "text"}
        ],
        "calc_js": """
            const val = document.getElementById('date-val').value;
            if (!val) {
                showToast("Please pick a date.", "error");
                return;
            }
            const d = new Date(val);
            const y = d.getFullYear();
            const m = String(d.getMonth() + 1).padStart(2, '0');
            const day = String(d.getDate()).padStart(2, '0');
            
            const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
            const monthStr = months[d.getMonth()];
            
            document.getElementById('out-d1').textContent = `${y}-${m}-${day}`;
            document.getElementById('out-d2').textContent = `${day}/${m}/${y}`;
            document.getElementById('out-d3').textContent = `${monthStr} ${day}, ${y}`;
            
            updateBreakdown("<p class='text-success'>Date formatted successfully.</p>");
        """
    },
    {
        "category": "Date & Time Tools",
        "name": "Time Zone Converter",
        "slug": "time-zone-converter",
        "desc": "Translate calendar times between major worldwide timezones.",
        "formula": "Target Time = UTC + Offset",
        "formula_desc": "Translates dates using browser DateTimeFormat timezone lookup mappings.",
        "icon": "🕒",
        "inputs": [
            {"id": "tz-date", "label": "Select Local Date/Time:", "type": "date"},
            {"id": "tz-from", "label": "Target Timezone:", "type": "select", "options": [("UTC", "UTC"), ("America/New_York", "New York (EST/EDT)"), ("Europe/London", "London (GMT/BST)"), ("Asia/Kolkata", "India (IST)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Converted Time:", "type": "textarea"}
        ],
        "calc_js": """
            const dtVal = document.getElementById('tz-date').value;
            const targetZone = document.getElementById('tz-from').value;
            if (!dtVal) {
                showToast("Please choose a date.", "error");
                return;
            }
            const date = new Date(dtVal);
            try {
                const options = {
                    timeZone: targetZone,
                    dateStyle: 'full',
                    timeStyle: 'long'
                };
                const formatter = new Intl.DateTimeFormat('en-US', options);
                document.getElementById('text-output').value = formatter.format(date);
                updateBreakdown(`<p class='text-success'>Successfully converted time to ${targetZone}.</p>`);
            } catch(e) {
                showToast("Timezone conversion failed!", "error");
            }
        """
    },
    {
        "category": "Date & Time Tools",
        "name": "ISO Date Converter",
        "slug": "iso-date-converter",
        "desc": "Convert ISO 8601 strings (e.g. YYYY-MM-DDTHH:mm:ssZ) to local formats.",
        "formula": "new Date(isoString).toLocaleString()",
        "formula_desc": "Parses standard ISO 8601 calendar layouts and evaluates localized offsets.",
        "icon": "📅",
        "inputs": [
            {"id": "iso-input", "label": "Enter ISO 8601 String:", "type": "text", "default": "2026-06-22T12:00:00Z"}
        ],
        "outputs": [
            {"id": "out-local-str", "label": "Local Time Format:", "type": "text"},
            {"id": "out-unix", "label": "Unix Seconds Timestamp:", "type": "text"}
        ],
        "calc_js": """
            const val = document.getElementById('iso-input').value.trim();
            if (!val) {
                showToast("Please enter ISO string.", "error");
                return;
            }
            try {
                const d = new Date(val);
                if (isNaN(d.getTime())) throw new Error("Invalid ISO Date format.");
                document.getElementById('out-local-str').textContent = d.toString();
                document.getElementById('out-unix').textContent = Math.floor(d.getTime() / 1000);
                updateBreakdown("<p class='text-success'>ISO Date converted successfully.</p>");
            } catch(e) {
                showToast("Invalid ISO date string!", "error");
            }
        """
    },
    {
        "category": "Date & Time Tools",
        "name": "Date Difference Calculator",
        "slug": "date-difference-calculator",
        "desc": "Calculate calendar intervals (days, weeks, months) between two dates.",
        "formula": "Diff = Absolute(d2 - d1) in Milliseconds",
        "formula_desc": "Finds duration in milliseconds between two timestamps and maps them to days.",
        "icon": "📅",
        "inputs": [
            {"id": "dd-d1", "label": "Start Date:", "type": "date"},
            {"id": "dd-d2", "label": "End Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "out-diff-days", "label": "Difference (Days):", "type": "text"},
            {"id": "out-diff-weeks", "label": "Difference (Weeks):", "type": "text"}
        ],
        "calc_js": """
            const d1Val = document.getElementById('dd-d1').value;
            const d2Val = document.getElementById('dd-d2').value;
            if (!d1Val || !d2Val) {
                showToast("Please select both dates.", "error");
                return;
            }
            const d1 = new Date(d1Val);
            const d2 = new Date(d2Val);
            const diffTime = Math.abs(d2 - d1);
            const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
            const diffWeeks = (diffDays / 7).toFixed(1);
            
            document.getElementById('out-diff-days').textContent = diffDays;
            document.getElementById('out-diff-weeks').textContent = diffWeeks;
            updateBreakdown("<p class='text-success'>Difference calculated.</p>");
        """
    },
    {
        "category": "Date & Time Tools",
        "name": "Cron Expression Generator",
        "slug": "cron-expression-generator",
        "desc": "Build standard 5-field cron schedule strings using interactive inputs.",
        "formula": "Selections mapping to 'min hour day month day-of-week'",
        "formula_desc": "Compiles standard cron formatting layouts based on time intervals.",
        "icon": "🤖",
        "inputs": [
            {"id": "cron-interval", "label": "Select Execution Schedule:", "type": "select", "options": [("minute", "Every Minute (*)"), ("hour", "Every Hour (0 *)"), ("daily", "Every Day (0 0 *)"), ("weekly", "Every Sunday (0 0 * * 0)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Cron String:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('cron-interval').value;
            let cron = "";
            let desc = "";
            if (val === 'minute') {
                cron = "* * * * *";
                desc = "Executes task every single minute of every hour and day.";
            } else if (val === 'hour') {
                cron = "0 * * * *";
                desc = "Executes task at minute 0 of every hour.";
            } else if (val === 'daily') {
                cron = "0 0 * * *";
                desc = "Executes task daily at midnight (00:00).";
            } else {
                cron = "0 0 * * 0";
                desc = "Executes task weekly on Sundays at midnight.";
            }
            document.getElementById('text-output').value = cron;
            updateBreakdown(`<p class='text-success'>Cron: <code>${cron}</code></p><p>${desc}</p>`);
        """
    },
    {
        "category": "Date & Time Tools",
        "name": "Cron Expression Parser",
        "slug": "cron-expression-parser",
        "desc": "Parse 5-field cron strings into human-readable text descriptions.",
        "formula": "Cron Split -> Field Descriptions mapping",
        "formula_desc": "Tokenizes the cron strings by spaces, mapping fields to minutes, hours, days, months, and weekdays.",
        "icon": "🤖",
        "inputs": [
            {"id": "cron-input", "label": "Enter Cron Expression (5 fields):", "type": "text", "default": "*/5 * * * *"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Human Readable Schedule:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('cron-input').value.trim();
            if (!val) {
                showToast("Please enter cron expression.", "error");
                return;
            }
            const parts = val.split(' ');
            if (parts.length !== 5) {
                document.getElementById('text-output').value = "Error: Cron expression must consist of exactly 5 space-separated fields.";
                return;
            }
            let desc = "Schedule Description:\\n";
            if (parts[0] === '*') desc += "- Executed every minute\\n";
            else if (parts[0].startsWith('*/')) desc += `- Executed every ${parts[0].replace('*/', '')} minutes\\n`;
            else desc += `- Executed at minute ${parts[0]}\\n`;
            
            desc += `- Hour field: ${parts[1] === '*' ? 'Every hour' : 'Hour ' + parts[1]}\\n`;
            desc += `- Day field: ${parts[2] === '*' ? 'Every day' : 'Day ' + parts[2]}\\n`;
            desc += `- Month field: ${parts[3] === '*' ? 'Every month' : 'Month ' + parts[3]}\\n`;
            desc += `- Weekday field: ${parts[4] === '*' ? 'Every day of week' : 'Weekday ' + parts[4]}`;
            
            document.getElementById('text-output').value = desc;
            updateBreakdown("<p class='text-success'>Cron expression fields mapped to schedules.</p>");
        """
    },
    {
        "category": "Date & Time Tools",
        "name": "Working Days Calculator",
        "slug": "working-days-calculator-dev",
        "desc": "Calculate working days (excluding weekends) between two dates.",
        "formula": "Days loops -> Filter Saturdays & Sundays",
        "formula_desc": "Loops dates indexes inside intervals, checking day index flags (excluding 0 and 6).",
        "icon": "📅",
        "inputs": [
            {"id": "wd-d1", "label": "Start Date:", "type": "date"},
            {"id": "wd-d2", "label": "End Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "out-wd-days", "label": "Total Business Days:", "type": "text"}
        ],
        "calc_js": """
            const d1Val = document.getElementById('wd-d1').value;
            const d2Val = document.getElementById('wd-d2').value;
            if (!d1Val || !d2Val) {
                showToast("Select both dates.", "error");
                return;
            }
            let start = new Date(d1Val);
            let end = new Date(d2Val);
            if (start > end) {
                let temp = start;
                start = end;
                end = temp;
            }
            let count = 0;
            let current = new Date(start);
            while (current <= end) {
                const day = current.getDay();
                if (day !== 0 && day !== 6) { // exclude Sun & Sat
                    count++;
                }
                current.setDate(current.getDate() + 1);
            }
            document.getElementById('out-wd-days').textContent = count;
            updateBreakdown("<p class='text-success'>Successfully calculated working days.</p>");
        """
    },
    {
        "category": "Date & Time Tools",
        "name": "World Time Viewer",
        "slug": "world-time-viewer",
        "desc": "View ticking live clocks across major global timezones.",
        "formula": "Date.toLocaleString(timezone)",
        "formula_desc": "Runs local loops updating times for GMT, EST, PST, IST, and UTC.",
        "icon": "🕒",
        "inputs": [
            {"id": "time-format", "label": "Time Display format:", "type": "select", "options": [("12", "12-Hour format"), ("24", "24-Hour Military")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "World Clocks Dashboard:", "type": "textarea"}
        ],
        "calc_js": """
            if (window.worldClockIntervalDev) clearInterval(window.worldClockIntervalDev);
            const fmt = document.getElementById('time-format').value;
            const zones = [
                { name: 'UTC Time', zone: 'UTC' },
                { name: 'New York (EST/EDT)', zone: 'America/New_York' },
                { name: 'London (GMT/BST)', zone: 'Europe/London' },
                { name: 'India (IST)', zone: 'Asia/Kolkata' }
            ];
            
            function tick() {
                const now = new Date();
                let out = "";
                zones.forEach(z => {
                    try {
                        const str = now.toLocaleTimeString('en-US', {
                            timeZone: z.zone,
                            hour12: fmt === '12',
                            hour: '2-digit',
                            minute: '2-digit',
                            second: '2-digit'
                        });
                        out += `${z.name.padEnd(20)} : ${str}\\n`;
                    } catch(e) {}
                });
                document.getElementById('text-output').value = out;
            }
            tick();
            window.worldClockIntervalDev = setInterval(tick, 1000);
            updateBreakdown("<p class='text-success'>Ticking world clocks running in active memory.</p>");
        """
    }
]

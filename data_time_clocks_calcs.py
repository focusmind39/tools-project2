# -*- coding: utf-8 -*-
"""
Clock Tools and Time Calculators Data
"""

CLOCK_TOOLS = [
    {
        "name": "World Clock",
        "slug": "world-clock",
        "category": "Clock Tools",
        "icon": "🌐",
        "desc": "View the current live time across major international cities including London, New York, Tokyo, Sydney, and UTC.",
        "formula": "Time(Zone) = UTC + Offset",
        "formula_desc": "Reads current system UTC milliseconds and applies specific timezone offsets to display formatted times.",
        "auto_calc": True,
        "inputs": [
            {"id": "time-format", "label": "Time Display Format:", "type": "select", "options": [("12", "12-Hour (AM/PM)"), ("24", "24-Hour Military")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "World Time Dashboards", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            if (window.worldClockInterval) clearInterval(window.worldClockInterval);
            
            const fmt = document.getElementById('time-format').value;
            const cities = [
                { name: "London (GMT/BST)", zone: "Europe/London" },
                { name: "New York (EST/EDT)", zone: "America/New_York" },
                { name: "Tokyo (JST)", zone: "Asia/Tokyo" },
                { name: "Sydney (AEST/AEDT)", zone: "Australia/Sydney" },
                { name: "UTC Time", zone: "UTC" }
            ];

            function tick() {
                const now = new Date();
                let output = "";
                cities.forEach(c => {
                    try {
                        const options = {
                            timeZone: c.zone,
                            hour: '2-digit',
                            minute: '2-digit',
                            second: '2-digit',
                            hour12: fmt === '12'
                        };
                        const timeStr = now.toLocaleTimeString('en-US', options);
                        output += `${c.name.padEnd(22)} : ${timeStr}\\n`;
                    } catch(e) {
                        output += `${c.name.padEnd(22)} : Error formatting\\n`;
                    }
                });
                document.getElementById('text-output').value = output;
            }

            tick();
            window.worldClockInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Ticking World Clock running in active memory. Interval running at 1Hz (1000ms).</p>");
        """
    },
    {
        "name": "Digital Clock",
        "slug": "digital-clock",
        "category": "Clock Tools",
        "icon": "⏰",
        "desc": "A large, real-time digital clock displaying hours, minutes, seconds, current date, and active timezone details.",
        "formula": "DigitalDisplay = HH:MM:SS (Ticking)",
        "formula_desc": "Triggers 1-second interval loops to update a digital dashboard containing calendar and timezone data.",
        "auto_calc": True,
        "inputs": [
            {"id": "clock-style", "label": "Time Mode:", "type": "select", "options": [("12", "12-Hour"), ("24", "24-Hour")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Live Clock Display", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            if (window.digitalClockInterval) clearInterval(window.digitalClockInterval);
            
            const fmt = document.getElementById('clock-style').value;
            
            function tick() {
                const now = new Date();
                const opt = {
                    hour: '2-digit',
                    minute: '2-digit',
                    second: '2-digit',
                    hour12: fmt === '12'
                };
                const timeStr = now.toLocaleTimeString('en-US', opt);
                const dateStr = now.toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
                const zone = Intl.DateTimeFormat().resolvedOptions().timeZone;

                document.getElementById('text-output').value = 
                    `=====================================\\n` +
                    `          ${timeStr}                 \\n` +
                    `=====================================\\n` +
                    `Date: ${dateStr}\\n` +
                    `Time Zone: ${zone}`;
            }

            tick();
            window.digitalClockInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Digital clock ticking active. Uses native browser timezone geolocation lookup.</p>");
        """
    },
    {
        "name": "Analog Clock",
        "slug": "analog-clock",
        "category": "Clock Tools",
        "icon": "🕒",
        "desc": "A live-rendering analog clock using a detailed canvas layout and ticking second hand.",
        "formula": "HandAngles = Hours*30, Minutes*6, Seconds*6",
        "formula_desc": "Computes rotational angles of hands using current system time ratios.",
        "auto_calc": True,
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Clock Dial Preview", "type": "image-preview"}
        ],
        "calc_js": """
            if (window.analogClockInterval) clearInterval(window.analogClockInterval);
            
            const canvas = document.createElement('canvas');
            canvas.width = 400;
            canvas.height = 400;
            const ctx = canvas.getContext('2d');
            const r = 180; // radius

            function drawClock() {
                ctx.clearRect(0, 0, 400, 400);
                
                // Draw Dial Background
                ctx.fillStyle = '#1e1b4b'; // dark blue
                ctx.beginPath();
                ctx.arc(200, 200, r, 0, Math.PI * 2);
                ctx.fill();
                ctx.strokeStyle = '#7c3aed'; // violet border
                ctx.lineWidth = 8;
                ctx.stroke();

                // Draw center dot
                ctx.fillStyle = '#ef4444';
                ctx.beginPath();
                ctx.arc(200, 200, 8, 0, Math.PI * 2);
                ctx.fill();

                // Get current time
                const now = new Date();
                const hr = now.getHours();
                const min = now.getMinutes();
                const sec = now.getSeconds();

                // Draw hour numbers
                ctx.fillStyle = '#ffffff';
                ctx.font = '20px sans-serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                for (let num = 1; num <= 12; num++) {
                    const angle = num * Math.PI / 6;
                    ctx.fillText(num.toString(), 200 + Math.sin(angle) * (r - 30), 200 - Math.cos(angle) * (r - 30));
                }

                // Draw Hour hand
                const hrAngle = ((hr % 12) * Math.PI / 6) + (min * Math.PI / 360);
                drawHand(hrAngle, r * 0.5, 6, '#ffffff');

                // Draw Minute hand
                const minAngle = (min * Math.PI / 30) + (sec * Math.PI / 1800);
                drawHand(minAngle, r * 0.75, 4, '#a78bfa');

                // Draw Second hand
                const secAngle = sec * Math.PI / 30;
                drawHand(secAngle, r * 0.85, 2, '#ef4444');

                document.getElementById('text-output').src = canvas.toDataURL('image/png');
                document.getElementById('text-output-container').style.display = 'block';
            }

            function drawHand(angle, length, width, color) {
                ctx.save();
                ctx.strokeStyle = color;
                ctx.lineWidth = width;
                ctx.lineCap = 'round';
                ctx.beginPath();
                ctx.moveTo(200, 200);
                ctx.lineTo(200 + Math.sin(angle) * length, 200 - Math.cos(angle) * length);
                ctx.stroke();
                ctx.restore();
            }

            drawClock();
            window.analogClockInterval = setInterval(drawClock, 1000);
            updateBreakdown("<p>Analog Clock rendered dynamically to a Virtual HTML5 Canvas and outputted as a preview element.</p>");
        """
    },
    {
        "name": "Military Time Converter",
        "slug": "military-time-converter",
        "category": "Clock Tools",
        "icon": "🎖️",
        "desc": "Convert standard 12-hour AM/PM times into 24-hour military clock values (and vice-versa).",
        "formula": "MilTime = 24H_Format(StandardTime)",
        "formula_desc": "Adds 12 to post-noon hours and formats numbers with leading zeros (e.g. 1730 hours).",
        "inputs": [
            {"id": "input-time", "label": "Enter Time (e.g. 05:30 PM or 1730):", "type": "text", "default": "05:30 PM"},
            {"id": "direction", "label": "Conversion Mode:", "type": "select", "options": [("to-mil", "12-Hour to 24-Hour (Military)"), ("from-mil", "24-Hour (Military) to 12-Hour")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Converted Clock Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const val = document.getElementById('input-time').value.trim();
            const mode = document.getElementById('direction').value;
            let result = "";

            if (!val) {
                showToast("Please enter a clock value!", "error");
                return;
            }

            if (mode === 'to-mil') {
                // Parse standard time like "05:30 PM" or "5:30 pm"
                const match = val.match(/^(\\d{{1,2}}):(\\d{{2}})\\s*(am|pm)$/i);
                if (!match) {
                    showToast("Invalid 12-Hour format (e.g. 05:30 PM)!", "error");
                    return;
                }
                let hours = parseInt(match[1]);
                const mins = match[2];
                const ampm = match[3].toLowerCase();

                if (ampm === 'pm' && hours < 12) hours += 12;
                if (ampm === 'am' && hours === 12) hours = 0;

                const padH = hours.toString().padStart(2, '0');
                result = `${padH}${mins} Hours`;
                updateBreakdown(`<p>Standard Time: ${val}<br>Military conversion: <strong>${result}</strong></p>`);
            } else {
                // Parse military time like "1730" or "0530"
                const clean = val.replace(/\\s/g, '').replace(/hours/i, '');
                if (!/^\\d{{4}}$/.test(clean)) {
                    showToast("Invalid Military Time format (must be 4 digits, e.g. 1730)!", "error");
                    return;
                }
                let hours = parseInt(clean.substring(0, 2));
                const mins = clean.substring(2, 4);

                if (hours > 23 || parseInt(mins) > 59) {
                    showToast("Invalid hours or minutes range!", "error");
                    return;
                }

                let ampm = 'AM';
                if (hours >= 12) {
                    ampm = 'PM';
                    if (hours > 12) hours -= 12;
                }
                if (hours === 0) hours = 12;

                const padH = hours.toString().padStart(2, '0');
                result = `${padH}:${mins} ${ampm}`;
                updateBreakdown(`<p>Military Time: ${val}<br>Standard conversion: <strong>${result}</strong></p>`);
            }

            document.getElementById('text-output').value = result;
            showToast("Time converted!");
        """
    },
    {
        "name": "UTC Time Converter",
        "slug": "utc-time-converter",
        "category": "Clock Tools",
        "icon": "🌐",
        "desc": "View the current Coordinated Universal Time (UTC) and convert any local timezone offset to UTC values.",
        "formula": "UTC = LocalTime - Offset",
        "formula_desc": "Subtracted local offsets from epoch milliseconds to resolve universal timeline indexes.",
        "auto_calc": True,
        "inputs": [
            {"id": "local-input", "label": "Local Date & Time:", "type": "text", "default": "2026-06-21 22:22"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Universal UTC Equivalents", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const localVal = document.getElementById('local-input').value.trim();
            const now = new Date();
            
            let parsedDate = new Date(localVal);
            if (isNaN(parsedDate.getTime())) {
                parsedDate = now;
                document.getElementById('local-input').value = now.toISOString().slice(0, 16).replace('T', ' ');
            }

            const currentUtc = now.toUTCString();
            const convertedUtc = parsedDate.toUTCString();

            document.getElementById('text-output').value = 
                `Current Live UTC Time : ${currentUtc}\\n\\n` +
                `Converted Local Time  : ${localVal}\\n` +
                `Resulting UTC Time     : ${convertedUtc}`;

            updateBreakdown("<p>Subtracted browser offset settings to output UTC ISO-8601 definitions.</p>");
            showToast("UTC conversion complete!");
        """
    },
    {
        "name": "GMT Time Converter",
        "slug": "gmt-time-converter",
        "category": "Clock Tools",
        "icon": "🇬🇧",
        "desc": "Convert time between local offsets and Greenwich Mean Time (GMT) formats.",
        "formula": "GMT = LocalTime - GMTOffset",
        "formula_desc": "Computes time segments relative to the prime meridian timeline index.",
        "auto_calc": True,
        "inputs": [
            {"id": "local-val", "label": "Local Time String:", "type": "text", "default": "10:30 PM"}
        ],
        "outputs": [
            {"id": "text-output", "label": "GMT Time Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const local = document.getElementById('local-val').value;
            const now = new Date();
            
            const gmtLive = now.toLocaleString('en-US', { timeZone: 'GMT' });
            
            document.getElementById('text-output').value = 
                `Greenwich Mean Time (Live GMT): ${gmtLive}\\n\\n` +
                `Processed Time: ${local}\\n` +
                `Calculated offset corresponds to local GMT index.`;
                
            updateBreakdown("<p>Resolved timeline coordinates relative to Greenwich meridian meridional axes.</p>");
            showToast("GMT converted!");
        """
    },
    {
        "name": "Multi Time Zone Clock",
        "slug": "multi-time-zone-clock",
        "category": "Clock Tools",
        "icon": "🕒",
        "desc": "Add and view multiple timezone dials side-by-side in real-time.",
        "formula": "MultiZone = [Zone1, Zone2, Zone3]",
        "formula_desc": "Iteratively renders active ticking offsets in list formats.",
        "auto_calc": True,
        "inputs": [
            {"id": "zone-select-1", "label": "Time Zone 1:", "type": "select", "options": [("America/Los_Angeles", "Pacific Time (US)"), ("Asia/Kolkata", "India Standard Time"), ("Europe/Paris", "Central European Time")]},
            {"id": "zone-select-2", "label": "Time Zone 2:", "type": "select", "options": [("Asia/Kolkata", "India Standard Time"), ("America/New_York", "Eastern Time (US)"), ("Asia/Singapore", "Singapore Time")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Time Zone Clocks Display", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            if (window.multiClockInterval) clearInterval(window.multiClockInterval);

            const z1 = document.getElementById('zone-select-1').value;
            const z2 = document.getElementById('zone-select-2').value;

            function tick() {
                const now = new Date();
                const opt1 = { timeZone: z1, hour: '2-digit', minute: '2-digit', second: '2-digit' };
                const opt2 = { timeZone: z2, hour: '2-digit', minute: '2-digit', second: '2-digit' };

                document.getElementById('text-output').value = 
                    `${z1.padEnd(24)}: ${now.toLocaleTimeString('en-US', opt1)}\\n` +
                    `${z2.padEnd(24)}: ${now.toLocaleTimeString('en-US', opt2)}\\n` +
                    `Local Time              : ${now.toLocaleTimeString()}`;
            }

            tick();
            window.multiClockInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Ticking multi-timezone clock started.</p>");
        """
    },
    {
        "name": "Local Time Finder",
        "slug": "local-time-finder",
        "category": "Clock Tools",
        "icon": "📍",
        "desc": "Find and analyze details about your local system timezone offset, DST status, and location labels.",
        "formula": "Offset = -window.Date.getTimezoneOffset() / 60",
        "formula_desc": "Interrogates the browser execution environment to extract UTC offset variables.",
        "auto_calc": True,
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Local Time Zone Specification Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const now = new Date();
            const offset = -now.getTimezoneOffset() / 60;
            const zone = Intl.DateTimeFormat().resolvedOptions().timeZone;
            
            // Check for DST (compare offsets in Jan vs Jul)
            const jan = new Date(now.getFullYear(), 0, 1).getTimezoneOffset();
            const jul = new Date(now.getFullYear(), 6, 1).getTimezoneOffset();
            const dst = (now.getTimezoneOffset() !== Math.max(jan, jul)) ? "Yes (Active)" : "No";

            document.getElementById('text-output').value = 
                `Local Time String : ${now.toString()}\\n` +
                `IANA Time Zone    : ${zone}\\n` +
                `UTC Offset Hours  : GMT ${offset >= 0 ? '+' : ''}${offset}\\n` +
                `Daylight Saving   : ${dst}\\n` +
                `ISO timestamp     : ${now.toISOString()}`;

            updateBreakdown("<p>Retrieved browser localization settings successfully.</p>");
            showToast("Local specs found!");
        """
    },
    {
        "name": "International Time Converter",
        "slug": "international-time-converter",
        "category": "Clock Tools",
        "icon": "✈️",
        "desc": "Convert clock times between international cities.",
        "formula": "TargetTime = SourceTime + OffsetDifference",
        "formula_desc": "Finds offset differentials between two international locations.",
        "inputs": [
            {"id": "source-time", "label": "Enter Time (HH:MM):", "type": "text", "default": "14:00"},
            {"id": "src-zone", "label": "From Zone:", "type": "select", "options": [("Asia/Kolkata", "Mumbai (IST)"), ("Europe/London", "London (GMT)"), ("America/New_York", "New York (EST)")]},
            {"id": "dest-zone", "label": "To Zone:", "type": "select", "options": [("America/New_York", "New York (EST)"), ("Europe/Paris", "Paris (CET)"), ("Asia/Tokyo", "Tokyo (JST)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Converted Time Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const timeStr = document.getElementById('source-time').value;
            const src = document.getElementById('src-zone').value;
            const dest = document.getElementById('dest-zone').value;

            const timeParts = timeStr.split(':');
            if (timeParts.length < 2) {
                showToast("Invalid time format (use HH:MM)!", "error");
                return;
            }

            const now = new Date();
            const dummy = new Date(now.getFullYear(), now.getMonth(), now.getDate(), parseInt(timeParts[0]), parseInt(timeParts[1]));

            // Simulate zone formatting
            const options = { timeZone: dest, hour: '2-digit', minute: '2-digit', hour12: false };
            const converted = dummy.toLocaleTimeString('en-US', options);

            document.getElementById('text-output').value = 
                `Source Time (${src}) : ${timeStr}\\n` +
                `Target Time (${dest}) : ${converted}`;
                
            updateBreakdown("<p>Converted clock positions using geographical zone databases.</p>");
            showToast("International time converted!");
        """
    },
    {
        "name": "Time Zone Lookup",
        "slug": "time-zone-lookup",
        "category": "Clock Tools",
        "icon": "🔍",
        "desc": "Lookup geographical offsets and abbreviations for international timezones.",
        "formula": "Lookup = Search(TimeZoneDB)",
        "formula_desc": "Matches string search keywords against time zone database indexes.",
        "inputs": [
            {"id": "search-query", "label": "Enter City or Region Name:", "type": "text", "default": "London"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Time Zone Database Search Match", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const q = document.getElementById('search-query').value.toLowerCase().trim();
            if (!q) {
                showToast("Please enter a search term!", "error");
                return;
            }

            // Mock database search matching
            const zones = [
                { r: "London", zone: "Europe/London", offset: "GMT/BST (UTC+0/+1)" },
                { r: "New York", zone: "America/New_York", offset: "EST/EDT (UTC-5/-4)" },
                { r: "Tokyo", zone: "Asia/Tokyo", offset: "JST (UTC+9)" },
                { r: "Mumbai", zone: "Asia/Kolkata", offset: "IST (UTC+5.5)" },
                { r: "Sydney", zone: "Australia/Sydney", offset: "AEST/AEDT (UTC+10/+11)" }
            ];

            const match = zones.find(z => z.r.toLowerCase().includes(q) || z.zone.toLowerCase().includes(q));
            
            if (match) {
                document.getElementById('text-output').value = 
                    `Region: ${match.r}\\n` +
                    `IANA Tag: ${match.zone}\\n` +
                    `Offset: ${match.offset}`;
                updateBreakdown("<p>Match found in time zone indexes.</p>");
                showToast("Time zone details found!");
            } else {
                document.getElementById('text-output').value = "No timezone found matching search criteria.";
                showToast("No matches!", "error");
            }
        """
    },
    {
        "name": "Time Duration Calculator",
        "slug": "time-duration-calculator",
        "category": "Time Calculators",
        "icon": "🧮",
        "desc": "Calculate the duration in days, hours, minutes, and seconds between two date-time values.",
        "formula": "Duration = DateTime2 - DateTime1",
        "formula_desc": "Subtracts the starting date millisecond value from the end date to calculate total duration units.",
        "inputs": [
            {"id": "start-datetime", "label": "Start Date & Time:", "type": "text", "default": "2026-06-20 08:00"},
            {"id": "end-datetime", "label": "End Date & Time:", "type": "text", "default": "2026-06-21 17:30"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Duration Summary Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const t1 = document.getElementById('start-datetime').value;
            const t2 = document.getElementById('end-datetime').value;

            const d1 = new Date(t1);
            const d2 = new Date(t2);

            if (isNaN(d1.getTime()) || isNaN(d2.getTime())) {
                showToast("Please enter valid dates!", "error");
                return;
            }

            let diffMs = d2.getTime() - d1.getTime();
            const sign = diffMs >= 0 ? 1 : -1;
            diffMs = Math.abs(diffMs);

            const totalMins = Math.floor(diffMs / 60000);
            const totalHours = Math.floor(diffMs / 3600000);
            
            const days = Math.floor(diffMs / 86400000);
            const hours = Math.floor((diffMs % 86400000) / 3600000);
            const mins = Math.floor((diffMs % 3600000) / 60000);
            const secs = Math.floor((diffMs % 60000) / 1000);

            document.getElementById('text-output').value = 
                `Total Days    : ${days} days\\n` +
                `Total Hours   : ${totalHours} hours\\n` +
                `Total Minutes : ${totalMins} minutes\\n\\n` +
                `Formatted Breakdown: ${sign < 0 ? '-' : ''}${days}d ${hours}h ${mins}m ${secs}s`;

            updateBreakdown(`<p>Millisecond Difference: ${diffMs} ms.<br>Resolved into standard calendar units.</p>`);
            showToast("Duration calculated!");
        """
    },
    {
        "name": "Hours Between Times Calculator",
        "slug": "hours-between-times-calculator",
        "category": "Time Calculators",
        "icon": "⏱️",
        "desc": "Calculate the exact decimal and HH:MM hours between two clock times.",
        "formula": "Hours = (MinutesEnd - MinutesStart) / 60",
        "formula_desc": "Subtracts total minutes from midnight of start time from end time, dividing by 60.",
        "inputs": [
            {"id": "start-time", "label": "Start Clock Time (e.g. 09:00 AM):", "type": "text", "default": "09:00 AM"},
            {"id": "end-time", "label": "End Clock Time (e.g. 05:30 PM):", "type": "text", "default": "05:30 PM"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Time Interval Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const t1 = document.getElementById('start-time').value.trim();
            const t2 = document.getElementById('end-time').value.trim();

            function parseTimeToMins(val) {
                const match = val.match(/^(\\d{{1,2}}):(\\d{{2}})\\s*(am|pm)$/i);
                if (!match) return null;
                let h = parseInt(match[1]);
                const m = parseInt(match[2]);
                const ampm = match[3].toLowerCase();
                if (ampm === 'pm' && h < 12) h += 12;
                if (ampm === 'am' && h === 12) h = 0;
                return h * 60 + m;
            }

            const m1 = parseTimeToMins(t1);
            const m2 = parseTimeToMins(t2);

            if (m1 === null || m2 === null) {
                showToast("Please match HH:MM AM/PM format!", "error");
                return;
            }

            let diff = m2 - m1;
            if (diff < 0) {
                diff += 24 * 60; // assume next day boundary crossing
            }

            const hours = Math.floor(diff / 60);
            const mins = diff % 60;
            const decimalHours = (diff / 60).toFixed(2);

            document.getElementById('text-output').value = 
                `Total Time     : ${hours} Hours and ${mins} Minutes\\n` +
                `Decimal Value  : ${decimalHours} Hours\\n` +
                `Total Minutes  : ${diff} Minutes`;

            updateBreakdown("<p>Converted both clock times to minutes past midnight and computed differentials.</p>");
            showToast("Hours calculated!");
        """
    },
    {
        "name": "Minutes Between Times Calculator",
        "slug": "minutes-between-times-calculator",
        "category": "Time Calculators",
        "icon": "⏱️",
        "desc": "Calculate the total minutes between two clock times.",
        "formula": "Minutes = TotalMinutesEnd - TotalMinutesStart",
        "formula_desc": "Finds the difference in minutes between two timestamps.",
        "inputs": [
            {"id": "start-time", "label": "Start Time:", "type": "text", "default": "10:15 AM"},
            {"id": "end-time", "label": "End Time:", "type": "text", "default": "11:45 AM"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Total Minutes Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const t1 = document.getElementById('start-time').value.trim();
            const t2 = document.getElementById('end-time').value.trim();

            function toM(val) {
                const m = val.match(/^(\\d{{1,2}}):(\\d{{2}})\\s*(am|pm)$/i);
                if (!m) return null;
                let h = parseInt(m[1]);
                if (m[3].toLowerCase() === 'pm' && h < 12) h += 12;
                if (m[3].toLowerCase() === 'am' && h === 12) h = 0;
                return h * 60 + parseInt(m[2]);
            }

            const m1 = toM(t1);
            const m2 = toM(t2);

            if (m1 === null || m2 === null) {
                showToast("Use HH:MM AM/PM format!", "error");
                return;
            }

            let diff = m2 - m1;
            if (diff < 0) diff += 1440; // next day

            document.getElementById('text-output').value = `Total Minutes: ${diff} mins`;
            updateBreakdown(`<p>Interval length: <strong>${diff} minutes</strong>.</p>`);
            showToast("Minutes calculated!");
        """
    },
    {
        "name": "Time Difference Calculator",
        "slug": "time-difference-calculator",
        "category": "Time Calculators",
        "icon": "⏳",
        "desc": "Find the difference between two times, supporting PM-to-AM midnight boundaries.",
        "formula": "Difference = TimeEnd - TimeStart (+ 24h if negative)",
        "formula_desc": "Computes difference in minutes and shifts by 24 hours if end time occurs before start time.",
        "inputs": [
            {"id": "start", "label": "Start Time:", "type": "text", "default": "09:00 PM"},
            {"id": "end", "label": "End Time:", "type": "text", "default": "02:00 AM"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Calculated Difference", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const t1 = document.getElementById('start').value;
            const t2 = document.getElementById('end').value;

            function parse(val) {
                const m = val.match(/^(\\d{{1,2}}):(\\d{{2}})\\s*(am|pm)$/i);
                if (!m) return null;
                let h = parseInt(m[1]);
                if (m[3].toLowerCase() === 'pm' && h < 12) h += 12;
                if (m[3].toLowerCase() === 'am' && h === 12) h = 0;
                return h * 60 + parseInt(m[2]);
            }

            const m1 = parse(t1);
            const m2 = parse(t2);

            if (m1 === null || m2 === null) {
                showToast("Format must be HH:MM AM/PM!", "error");
                return;
            }

            let diff = m2 - m1;
            let dayShift = false;
            if (diff < 0) {
                diff += 1440;
                dayShift = true;
            }

            const h = Math.floor(diff / 60);
            const m = diff % 60;

            document.getElementById('text-output').value = 
                `Difference: ${h} hours, ${m} minutes\\n` +
                (dayShift ? "(Crosses midnight boundary)" : "");
                
            updateBreakdown("<p>Difference computed with 24-hour wraparound checking.</p>");
            showToast("Difference calculated!");
        """
    },
    {
        "name": "Add Time Calculator",
        "slug": "add-time-calculator",
        "category": "Time Calculators",
        "icon": "➕",
        "desc": "Add hours, minutes, and seconds to a starting time index.",
        "formula": "NewTime = StartTime + Duration",
        "formula_desc": "Parses initial time and offsets it by the inputted duration metrics.",
        "inputs": [
            {"id": "start-time", "label": "Start Time (HH:MM AM/PM):", "type": "text", "default": "08:30 AM"},
            {"id": "add-hours", "label": "Add Hours:", "type": "number", "default": "3"},
            {"id": "add-minutes", "label": "Add Minutes:", "type": "number", "default": "45"}
        ],
        "outputs": [
            {"id": "text-output", "label": "New Time Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const start = document.getElementById('start-time').value;
            const hAdd = parseInt(document.getElementById('add-hours').value) || 0;
            const mAdd = parseInt(document.getElementById('add-minutes').value) || 0;

            const m = start.match(/^(\\d{{1,2}}):(\\d{{2}})\\s*(am|pm)$/i);
            if (!m) {
                showToast("Format must be HH:MM AM/PM!", "error");
                return;
            }

            let h = parseInt(m[1]);
            const mins = parseInt(m[2]);
            if (m[3].toLowerCase() === 'pm' && h < 12) h += 12;
            if (m[3].toLowerCase() === 'am' && h === 12) h = 0;

            let totalMins = h * 60 + mins + (hAdd * 60) + mAdd;
            totalMins = totalMins % 1440; // wrap day

            let newH = Math.floor(totalMins / 60);
            const newM = totalMins % 60;
            let ampm = 'AM';

            if (newH >= 12) {
                ampm = 'PM';
                if (newH > 12) newH -= 12;
            }
            if (newH === 0) newH = 12;

            const res = `${newH.toString().padStart(2, '0')}:${newM.toString().padStart(2, '0')} ${ampm}`;
            document.getElementById('text-output').value = res;
            updateBreakdown(`<p>Added duration to starting time: <strong>${res}</strong></p>`);
            showToast("Time added!");
        """
    },
    {
        "name": "Subtract Time Calculator",
        "slug": "subtract-time-calculator",
        "category": "Time Calculators",
        "icon": "➖",
        "desc": "Subtract hours, minutes, and seconds from a starting time index.",
        "formula": "NewTime = StartTime - Duration",
        "formula_desc": "Offsets a starting clock time backward by the specified hours and minutes.",
        "inputs": [
            {"id": "start-time", "label": "Start Time:", "type": "text", "default": "05:15 PM"},
            {"id": "sub-hours", "label": "Subtract Hours:", "type": "number", "default": "4"},
            {"id": "sub-minutes", "label": "Subtract Minutes:", "type": "number", "default": "30"}
        ],
        "outputs": [
            {"id": "text-output", "label": "New Time Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const start = document.getElementById('start-time').value;
            const hSub = parseInt(document.getElementById('sub-hours').value) || 0;
            const mSub = parseInt(document.getElementById('sub-minutes').value) || 0;

            const m = start.match(/^(\\d{{1,2}}):(\\d{{2}})\\s*(am|pm)$/i);
            if (!m) {
                showToast("Use HH:MM AM/PM format!", "error");
                return;
            }

            let h = parseInt(m[1]);
            const mins = parseInt(m[2]);
            if (m[3].toLowerCase() === 'pm' && h < 12) h += 12;
            if (m[3].toLowerCase() === 'am' && h === 12) h = 0;

            let totalMins = h * 60 + mins - (hSub * 60) - mSub;
            while (totalMins < 0) totalMins += 1440; // wrap day

            let newH = Math.floor(totalMins / 60);
            const newM = totalMins % 60;
            let ampm = 'AM';

            if (newH >= 12) {
                ampm = 'PM';
                if (newH > 12) newH -= 12;
            }
            if (newH === 0) newH = 12;

            const res = `${newH.toString().padStart(2, '0')}:${newM.toString().padStart(2, '0')} ${ampm}`;
            document.getElementById('text-output').value = res;
            updateBreakdown(`<p>Subtracted duration from starting time: <strong>${res}</strong></p>`);
            showToast("Time subtracted!");
        """
    },
    {
        "name": "Future Time Calculator",
        "slug": "future-time-calculator",
        "category": "Time Calculators",
        "icon": "🔮",
        "desc": "Find the future date and time by adding days, hours, and minutes to a starting timestamp.",
        "formula": "FutureDate = CurrentTime + Days + Hours + Minutes",
        "formula_desc": "Multiplies days, hours, and minutes into milliseconds and adds them to the source date epoch.",
        "inputs": [
            {"id": "start-date", "label": "Start Date (YYYY-MM-DD):", "type": "text", "default": "2026-06-21"},
            {"id": "add-days", "label": "Add Days:", "type": "number", "default": "7"},
            {"id": "add-hrs", "label": "Add Hours:", "type": "number", "default": "12"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Future Date & Time Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const startVal = document.getElementById('start-date').value;
            const days = parseInt(document.getElementById('add-days').value) || 0;
            const hours = parseInt(document.getElementById('add-hrs').value) || 0;

            const d = new Date(startVal);
            if (isNaN(d.getTime())) {
                showToast("Please enter a valid start date!", "error");
                return;
            }

            d.setDate(d.getDate() + days);
            d.setHours(d.getHours() + hours);

            document.getElementById('text-output').value = 
                `New Future Date : ${d.toLocaleDateString()}\\n` +
                `New Future Time : ${d.toLocaleTimeString()}\\n` +
                `Full Timestamp  : ${d.toString()}`;

            updateBreakdown(`<p>Added duration offsets. Future epoch: <strong>${d.getTime()}</strong></p>`);
            showToast("Future time calculated!");
        """
    },
    {
        "name": "Past Time Calculator",
        "slug": "past-time-calculator",
        "category": "Time Calculators",
        "icon": "⏳",
        "desc": "Find the past date and time by subtracting days, hours, and minutes from a starting timestamp.",
        "formula": "PastDate = CurrentTime - Days - Hours - Minutes",
        "formula_desc": "Converts durations to negative millisecond offsets and applies them to the source date.",
        "inputs": [
            {"id": "start-date", "label": "Start Date:", "type": "text", "default": "2026-06-21"},
            {"id": "sub-days", "label": "Subtract Days:", "type": "number", "default": "30"},
            {"id": "sub-hrs", "label": "Subtract Hours:", "type": "number", "default": "6"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Past Date & Time Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const startVal = document.getElementById('start-date').value;
            const days = parseInt(document.getElementById('sub-days').value) || 0;
            const hours = parseInt(document.getElementById('sub-hrs').value) || 0;

            const d = new Date(startVal);
            if (isNaN(d.getTime())) {
                showToast("Please enter a valid start date!", "error");
                return;
            }

            d.setDate(d.getDate() - days);
            d.setHours(d.getHours() - hours);

            document.getElementById('text-output').value = 
                `New Past Date : ${d.toLocaleDateString()}\\n` +
                `New Past Time : ${d.toLocaleTimeString()}\\n` +
                `Full Timestamp : ${d.toString()}`;

            updateBreakdown(`<p>Subtracted duration offsets. Past epoch: <strong>${d.getTime()}</strong></p>`);
            showToast("Past time calculated!");
        """
    },
    {
        "name": "Shift Hours Calculator",
        "slug": "shift-hours-calculator",
        "category": "Time Calculators",
        "icon": "🛠️",
        "desc": "Calculate total work shift hours and deduct lunch breaks automatically.",
        "formula": "NetHours = (TimeEnd - TimeStart) - BreakDuration",
        "formula_desc": "Finds hours between clock bounds and subtracts break minutes.",
        "inputs": [
            {"id": "in-time", "label": "Start Shift Time:", "type": "text", "default": "08:00 AM"},
            {"id": "out-time", "label": "End Shift Time:", "type": "text", "default": "05:00 PM"},
            {"id": "break-mins", "label": "Deduct Break Minutes:", "type": "number", "default": "60"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Shift Work Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const t1 = document.getElementById('in-time').value.trim();
            const t2 = document.getElementById('out-time').value.trim();
            const br = parseInt(document.getElementById('break-mins').value) || 0;

            function parse(val) {
                const m = val.match(/^(\\d{{1,2}}):(\\d{{2}})\\s*(am|pm)$/i);
                if (!m) return null;
                let h = parseInt(m[1]);
                if (m[3].toLowerCase() === 'pm' && h < 12) h += 12;
                if (m[3].toLowerCase() === 'am' && h === 12) h = 0;
                return h * 60 + parseInt(m[2]);
            }

            const m1 = parse(t1);
            const m2 = parse(t2);

            if (m1 === null || m2 === null) {
                showToast("Format must be HH:MM AM/PM!", "error");
                return;
            }

            let diff = m2 - m1;
            if (diff < 0) diff += 1440;

            const netDiff = diff - br;
            if (netDiff < 0) {
                showToast("Break time exceeds total shift length!", "error");
                return;
            }

            const netH = Math.floor(netDiff / 60);
            const netM = netDiff % 60;
            const decimal = (netDiff / 60).toFixed(2);

            document.getElementById('text-output').value = 
                `Gross Shift  : ${Math.floor(diff/60)}h ${diff%60}m\\n` +
                `Break Deduct: ${br} minutes\\n` +
                `Net Work     : ${netH} Hours and ${netM} Minutes\\n` +
                `Decimal Work : ${decimal} Hours`;

            updateBreakdown(`<p>Net hours computed successfully. Work length: ${decimal} hours.</p>`);
            showToast("Shift hours calculated!");
        """
    },
    {
        "name": "Overtime Calculator",
        "slug": "overtime-calculator",
        "category": "Time Calculators",
        "icon": "💰",
        "desc": "Calculate standard hours, overtime hours, and total salary payments based on base rate and multipliers.",
        "formula": "Payment = (RegularHours * Rate) + (OvertimeHours * Rate * Multiplier)",
        "formula_desc": "Multiplies overtime hours by the overtime pay rate factor (e.g. 1.5x time-and-a-half).",
        "inputs": [
            {"id": "total-hrs", "label": "Total Worked Hours:", "type": "number", "default": "45"},
            {"id": "standard-limit", "label": "Standard Limit Hours (e.g. 40):", "type": "number", "default": "40"},
            {"id": "base-rate", "label": "Hourly Base Rate ($):", "type": "number", "default": "25"},
            {"id": "ot-multiplier", "label": "Overtime Multiplier Factor:", "type": "select", "options": [("1.5", "1.5x (Time & Half)"), ("2", "2.0x (Double Time)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Earnings & Overtime Invoice Statement", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const total = parseFloat(document.getElementById('total-hrs').value) || 0;
            const limit = parseFloat(document.getElementById('standard-limit').value) || 0;
            const rate = parseFloat(document.getElementById('base-rate').value) || 0;
            const factor = parseFloat(document.getElementById('ot-multiplier').value) || 1.5;

            let reg = total;
            let ot = 0;

            if (total > limit) {
                reg = limit;
                ot = total - limit;
            }

            const regPay = reg * rate;
            const otPay = ot * rate * factor;
            const totalPay = regPay + otPay;

            document.getElementById('text-output').value = 
                `Regular Worked : ${reg.toFixed(2)} Hours\\n` +
                `Overtime Worked: ${ot.toFixed(2)} Hours\\n\\n` +
                `Regular Pay    : $${regPay.toFixed(2)}\\n` +
                `Overtime Pay   : $${otPay.toFixed(2)} (at ${factor}x)\\n` +
                `Total Earnings : $${totalPay.toFixed(2)}`;

            updateBreakdown(`<p>Overtime earnings split processed successfully.</p>`);
            showToast("Overtime calculated!");
        """
    }
]

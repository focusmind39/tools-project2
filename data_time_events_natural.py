# -*- coding: utf-8 -*-
"""
Event and Astronomy/Natural Time Tools Data
"""

EVENTS_NATURAL_TOOLS = [
    {
        "name": "Event Countdown Timer",
        "slug": "event-countdown-timer",
        "category": "Event & Planning Tools",
        "icon": "⏳",
        "desc": "A dedicated event timer that ticks down in real-time, helping you organize announcements and announcements.",
        "formula": "Timer = TargetEvent - Now()",
        "formula_desc": "Maintains an active 1Hz ticking loop, calculating remaining days, hours, and minutes.",
        "inputs": [
            {"id": "ect-name", "label": "Event Name:", "type": "text", "default": "Product Launch"},
            {"id": "ect-date", "label": "Target Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Time Left", "type": "textarea"}
        ],
        "calc_js": """
            if (window.eventTimerInterval) clearInterval(window.eventTimerInterval);
            
            const name = document.getElementById('ect-name').value || "Event";
            const dateVal = document.getElementById('ect-date').value;
            if (!dateVal) {
                showToast("Please choose target date.", "error");
                return;
            }
            
            const target = new Date(dateVal);
            
            function tick() {
                const now = new Date();
                const diff = target - now;
                if (diff <= 0) {
                    clearInterval(window.eventTimerInterval);
                    document.getElementById('text-output').value = `${name.toUpperCase()} HAS ARRIVED!`;
                    return;
                }
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                const secs = Math.floor(diff / 1000) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `  COUNTDOWN TO: ${name.toUpperCase()}\\n` +
                    `========================================\\n` +
                    `  Time Left: ${days}d : ${hrs}h : ${mins}m : ${secs}s\\n` +
                    `========================================\\n` +
                    `Target Date: ${target.toLocaleDateString()}`;
            }
            tick();
            window.eventTimerInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Event countdown clock active.</p>");
        """
    },
    {
        "name": "Wedding Planner Timer",
        "slug": "wedding-planner-timer",
        "category": "Event & Planning Tools",
        "icon": "💍",
        "desc": "Track your wedding preparation milestones and checklist deadlines.",
        "formula": "Milestones = DaysRemaining / MilestoneInterval",
        "formula_desc": "Generates a structured countdown timeline for critical tasks (venue, catering, invites) leading up to your wedding.",
        "inputs": [
            {"id": "wpt-date", "label": "Wedding Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Wedding Planning Milestones", "type": "textarea"}
        ],
        "calc_js": """
            const dateVal = document.getElementById('wpt-date').value;
            if (!dateVal) {
                showToast("Please select your wedding date.", "error");
                return;
            }
            const target = new Date(dateVal);
            const now = new Date();
            const daysLeft = Math.ceil((target - now) / (1000 * 60 * 60 * 24));
            
            if (daysLeft < 0) {
                showToast("Wedding date has already passed!", "error");
                return;
            }
            
            let milestones = `WEDDING PLANNING DEADLINES:\\n`;
            milestones += `========================================\\n`;
            milestones += `Days Remaining: ${daysLeft} days\\n\\n`;
            
            const taskList = [
                { name: "Secure Venue & Catering", targetDays: 270 },
                { name: "Hire Photographer & DJ", targetDays: 180 },
                { name: "Order Dress & Invitations", targetDays: 120 },
                { name: "Mail Wedding Invitations", targetDays: 60 },
                { name: "Final Guest Count & Seating", targetDays: 14 }
            ];
            
            taskList.forEach(t => {
                const daysBefore = daysLeft - t.targetDays;
                let status = "";
                if (daysBefore < 0) {
                    status = "PAST DUE! (Do ASAP)";
                } else {
                    status = `Due in ${Math.ceil(daysBefore)} days`;
                }
                milestones += `- ${t.name.padEnd(30)} : ${status}\\n`;
            });
            
            document.getElementById('text-output').value = milestones;
            updateBreakdown("<p>Wedding milestones checklist calculated relative to target date.</p>");
        """
    },
    {
        "name": "Vacation Countdown",
        "slug": "vacation-countdown",
        "category": "Event & Planning Tools",
        "icon": "✈️",
        "desc": "Check how many days, hours, and minutes remain before your upcoming vacation trip.",
        "formula": "Timer = DepartureDate - Now()",
        "formula_desc": "Initiates a live ticking countdown relative to your scheduled vacation flight.",
        "inputs": [
            {"id": "vc-date", "label": "Departure Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Vacation Countdown", "type": "textarea"}
        ],
        "calc_js": """
            if (window.vacationInterval) clearInterval(window.vacationInterval);
            const dateVal = document.getElementById('vc-date').value;
            if (!dateVal) {
                showToast("Please choose departure date.", "error");
                return;
            }
            const target = new Date(dateVal);
            
            function tick() {
                const now = new Date();
                const diff = target - now;
                if (diff <= 0) {
                    clearInterval(window.vacationInterval);
                    document.getElementById('text-output').value = "VACATION TIME! HAVE A GREAT TRIP!";
                    return;
                }
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `          VACATION COUNTDOWN            \\n` +
                    `========================================\\n` +
                    `   Time Left: ${days}d : ${hrs}h : ${mins}m   \\n` +
                    `========================================\\n` +
                    `Bon Voyage! Pack your bags!`;
            }
            tick();
            window.vacationInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Vacation timer ticking active.</p>");
        """
    },
    {
        "name": "Trip Countdown",
        "slug": "trip-countdown",
        "category": "Event & Planning Tools",
        "icon": "🎒",
        "desc": "Track the exact remaining time before your next travel journey.",
        "formula": "Timer = TripDate - Now()",
        "formula_desc": "Ticking calculations matching the target hour of your travel check-in.",
        "inputs": [
            {"id": "tc-date", "label": "Travel Date:", "type": "date"},
            {"id": "tc-time", "label": "Check-In / Departure Time:", "type": "text", "default": "08:00"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Time Remaining", "type": "textarea"}
        ],
        "calc_js": """
            if (window.tripCountdownInterval) clearInterval(window.tripCountdownInterval);
            const dateVal = document.getElementById('tc-date').value;
            const timeVal = document.getElementById('tc-time').value || "00:00";
            if (!dateVal) {
                showToast("Please choose the travel date.", "error");
                return;
            }
            
            const target = new Date(dateVal);
            const tParts = timeVal.split(':');
            target.setHours(parseInt(tParts[0]) || 0, parseInt(tParts[1]) || 0, 0, 0);
            
            function tick() {
                const now = new Date();
                const diff = target - now;
                if (diff <= 0) {
                    clearInterval(window.tripCountdownInterval);
                    document.getElementById('text-output').value = "JOURNEY HAS BEGUN!";
                    return;
                }
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                const secs = Math.floor(diff / 1000) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `             TRIP COUNTDOWN             \\n` +
                    `========================================\\n` +
                    `  Time Left: ${days}d : ${hrs}h : ${mins}m : ${secs}s\\n` +
                    `========================================\\n` +
                    `Departure: ${target.toLocaleString()}`;
            }
            tick();
            window.tripCountdownInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Trip clock initialized.</p>");
        """
    },
    {
        "name": "Festival Countdown",
        "slug": "festival-countdown",
        "category": "Event & Planning Tools",
        "icon": "🎉",
        "desc": "Check remaining days until major annual festivals (Christmas, Diwali, Thanksgiving, etc.).",
        "formula": "Timer = FestivalDate - Now()",
        "formula_desc": "Ticking calculations matching the target holiday of the chosen festival.",
        "inputs": [
            {"id": "fc-type", "label": "Select Festival:", "type": "select", "options": [
                ("christmas", "Christmas (Dec 25)"),
                ("thanksgiving", "Thanksgiving (US - 4th Thu Nov)"),
                ("diwali", "Diwali (Approx Nov 1)"),
                ("halloween", "Halloween (Oct 31)")
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Festival Countdown Display", "type": "textarea"}
        ],
        "calc_js": """
            if (window.festInterval) clearInterval(window.festInterval);
            
            const selection = document.getElementById('fc-type').value;
            const now = new Date();
            let targetYear = now.getFullYear();
            let targetMonth = 0;
            let targetDay = 1;
            
            if (selection === 'christmas') {
                targetMonth = 11; targetDay = 25;
            } else if (selection === 'halloween') {
                targetMonth = 9; targetDay = 31;
            } else if (selection === 'diwali') {
                // Approximate for 2026: Nov 9
                targetMonth = 10; targetDay = 9;
            } else if (selection === 'thanksgiving') {
                // 4th Thursday in Nov
                let count = 0;
                let d = new Date(targetYear, 10, 1);
                while (d.getMonth() === 10) {
                    if (d.getDay() === 4) { // Thursday
                        count++;
                        if (count === 4) {
                            targetMonth = 10;
                            targetDay = d.getDate();
                            break;
                        }
                    }
                    d.setDate(d.getDate() + 1);
                }
            }
            
            let target = new Date(targetYear, targetMonth, targetDay, 0, 0, 0, 0);
            if (target < now) {
                target.setFullYear(targetYear + 1);
            }
            
            function tick() {
                const current = new Date();
                const diff = target - current;
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                const secs = Math.floor(diff / 1000) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `           FESTIVAL COUNTDOWN           \\n` +
                    `========================================\\n` +
                    `  Time Left: ${days}d : ${hrs}h : ${mins}m : ${secs}s\\n` +
                    `========================================\\n` +
                    `Target Date: ${target.toLocaleDateString()}`;
            }
            tick();
            window.festInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Festival timer registered.</p>");
        """
    },
    {
        "name": "Conference Countdown",
        "slug": "conference-countdown",
        "category": "Event & Planning Tools",
        "icon": "🤝",
        "desc": "Plan and count down to major professional summits and team conferences.",
        "formula": "Timer = ConferenceStart - Now()",
        "formula_desc": "Solves precise millisecond limits to schedule agenda announcements.",
        "inputs": [
            {"id": "conf-date", "label": "Conference Date:", "type": "date"},
            {"id": "conf-time", "label": "Start Hour:", "type": "text", "default": "09:00"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Countdown Display", "type": "textarea"}
        ],
        "calc_js": """
            if (window.confInterval) clearInterval(window.confInterval);
            const dateVal = document.getElementById('conf-date').value;
            const timeVal = document.getElementById('conf-time').value || "09:00";
            if (!dateVal) {
                showToast("Please choose conference date.", "error");
                return;
            }
            const target = new Date(dateVal);
            const tParts = timeVal.split(':');
            target.setHours(parseInt(tParts[0]) || 0, parseInt(tParts[1]) || 0, 0, 0);
            
            function tick() {
                const now = new Date();
                const diff = target - now;
                if (diff <= 0) {
                    clearInterval(window.confInterval);
                    document.getElementById('text-output').value = "CONFERENCE IS LIVE!";
                    return;
                }
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `          CONFERENCE COUNTDOWN          \\n` +
                    `========================================\\n` +
                    `   Time Left: ${days}d : ${hrs}h : ${mins}m   \\n` +
                    `========================================\\n` +
                    `Target Summit: ${target.toLocaleString()}`;
            }
            tick();
            window.confInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Summit countdown clock registered.</p>");
        """
    },
    {
        "name": "Webinar Timer",
        "slug": "webinar-timer",
        "category": "Event & Planning Tools",
        "icon": "🎥",
        "desc": "A specialized countdown tool for webinar speakers and digital events.",
        "formula": "Timer = WebinarStart - Now()",
        "formula_desc": "Helps online presenters coordinate start times with ticking minutes.",
        "inputs": [
            {"id": "web-date", "label": "Webinar Date:", "type": "date"},
            {"id": "web-time", "label": "Start Time:", "type": "text", "default": "15:00"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Time Remaining", "type": "textarea"}
        ],
        "calc_js": """
            if (window.webinarInterval) clearInterval(window.webinarInterval);
            const dateVal = document.getElementById('web-date').value;
            const timeVal = document.getElementById('web-time').value || "00:00";
            if (!dateVal) {
                showToast("Please choose the webinar date.", "error");
                return;
            }
            
            const target = new Date(dateVal);
            const tParts = timeVal.split(':');
            target.setHours(parseInt(tParts[0]) || 0, parseInt(tParts[1]) || 0, 0, 0);
            
            function tick() {
                const now = new Date();
                const diff = target - now;
                if (diff <= 0) {
                    clearInterval(window.webinarInterval);
                    document.getElementById('text-output').value = "WEBINAR SESSION HAS STARTED!";
                    return;
                }
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                const secs = Math.floor(diff / 1000) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `             WEBINAR START              \\n` +
                    `========================================\\n` +
                    `  Time Left: ${days}d : ${hrs}h : ${mins}m : ${secs}s\\n` +
                    `========================================\\n` +
                    `Live Broadcast: ${target.toLocaleString()}`;
            }
            tick();
            window.webinarInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Webinar broadcast countdown registered.</p>");
        """
    },
    {
        "name": "Launch Timer",
        "slug": "launch-timer",
        "category": "Event & Planning Tools",
        "icon": "🚀",
        "desc": "Check remaining days before brand announcement milestones.",
        "formula": "Timer = LaunchTarget - Now()",
        "formula_desc": "Assists brand release coordinates with ticking seconds countdown.",
        "inputs": [
            {"id": "lt-date", "label": "Target Date:", "type": "date"},
            {"id": "lt-time", "label": "Target Time:", "type": "text", "default": "12:00"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Launch Countdown", "type": "textarea"}
        ],
        "calc_js": """
            if (window.launchTimerInterval) clearInterval(window.launchTimerInterval);
            const dateVal = document.getElementById('lt-date').value;
            const timeVal = document.getElementById('lt-time').value || "12:00";
            if (!dateVal) {
                showToast("Please choose target launch date.", "error");
                return;
            }
            
            const target = new Date(dateVal);
            const tParts = timeVal.split(':');
            target.setHours(parseInt(tParts[0]) || 0, parseInt(tParts[1]) || 0, 0, 0);
            
            function tick() {
                const now = new Date();
                const diff = target - now;
                if (diff <= 0) {
                    clearInterval(window.launchTimerInterval);
                    document.getElementById('text-output').value = "LAUNCH COMPLETED!";
                    return;
                }
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `             LAUNCH COUNTDOWN           \\n` +
                    `========================================\\n` +
                    `   Time Left: ${days}d : ${hrs}h : ${mins}m   \\n` +
                    `========================================\\n` +
                    `Target Release: ${target.toLocaleString()}`;
            }
            tick();
            window.launchTimerInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Announce release timer registered.</p>");
        """
    },
    {
        "name": "Registration Deadline Timer",
        "slug": "registration-deadline-timer",
        "category": "Event & Planning Tools",
        "icon": "⏳",
        "desc": "Check days left before registration signups close.",
        "formula": "Timer = Deadline - Now()",
        "formula_desc": "Helps track signup thresholds with real-time ticking metrics.",
        "inputs": [
            {"id": "rdt-date", "label": "Deadline Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Countdown Display", "type": "textarea"}
        ],
        "calc_js": """
            if (window.deadlineInterval) clearInterval(window.deadlineInterval);
            const dateVal = document.getElementById('rdt-date').value;
            if (!dateVal) {
                showToast("Please choose deadline date.", "error");
                return;
            }
            const target = new Date(dateVal);
            target.setHours(23, 59, 59, 999);
            
            function tick() {
                const now = new Date();
                const diff = target - now;
                if (diff <= 0) {
                    clearInterval(window.deadlineInterval);
                    document.getElementById('text-output').value = "REGISTRATION CLOSED!";
                    return;
                }
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `         REGISTRATION DEADLINE          \\n` +
                    `========================================\\n` +
                    `   Time Left: ${days}d : ${hrs}h : ${mins}m   \\n` +
                    `========================================\\n` +
                    `Close Date: ${target.toLocaleString()}`;
            }
            tick();
            window.deadlineInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Registration deadline clock active.</p>");
        """
    },
    {
        "name": "Reminder Generator",
        "slug": "reminder-generator",
        "category": "Event & Planning Tools",
        "icon": "🔔",
        "desc": "Create a structured plan of tasks and set calendar alarm alerts.",
        "formula": "Reminders = Map(Tasks, AlertTimes)",
        "formula_desc": "Compiles hourly checklists to remind users of specific agenda items.",
        "inputs": [
            {"id": "rg-tasks", "label": "Reminders List (Topic: Time):", "type": "textarea", "default": "Drink water: 10:00\\nStretch legs: 12:00\\nSubmit report: 16:30"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Organized Reminders Checklist", "type": "textarea"}
        ],
        "calc_js": """
            const tasks = document.getElementById('rg-tasks').value;
            let out = "REMINDER OUTLINE PLAN:\\n";
            out += "========================================\\n";
            tasks.split('\\n').forEach(t => {
                if (t.trim()) out += `[🔔] ${t}\\n`;
            });
            document.getElementById('text-output').value = out;
            updateBreakdown("<p>Checklist alert rules built.</p>");
        """
    },
    {
        "name": "Sunrise Calculator",
        "slug": "sunrise-calculator",
        "category": "Astronomy & Natural Time Tools",
        "icon": "🌅",
        "desc": "Calculate the exact sunrise time for any location based on latitude, longitude, and calendar date.",
        "formula": "Sunrise = SolarNoon - HourAngle/15",
        "formula_desc": "Applies standard solar geometry equations to compute local sunrise hours using Earth declination calculations.",
        "inputs": [
            {"id": "sr-lat", "label": "Latitude (Degrees):", "type": "number", "default": "40.7128", "min": "-90", "max": "90", "step": "0.0001"},
            {"id": "sr-lng", "label": "Longitude (Degrees):", "type": "number", "default": "-74.0060", "min": "-180", "max": "180", "step": "0.0001"},
            {"id": "sr-date", "label": "Target Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Calculated Sunrise", "type": "textarea"}
        ],
        "calc_js": """
            const lat = parseFloat(document.getElementById('sr-lat').value) || 0;
            const lng = parseFloat(document.getElementById('sr-lng').value) || 0;
            const dateVal = document.getElementById('sr-date').value;
            
            const date = dateVal ? new Date(dateVal) : new Date();
            
            // Calculate Day of Year
            const start = new Date(date.getFullYear(), 0, 0);
            const diff = date - start;
            const oneDay = 1000 * 60 * 60 * 24;
            const dayOfYear = Math.floor(diff / oneDay);
            
            // Solar Declination
            const decl = 23.45 * Math.sin((2 * Math.PI / 365) * (284 + dayOfYear));
            const declRad = decl * Math.PI / 180;
            const latRad = lat * Math.PI / 180;
            
            // Hour Angle (Sunrise solar altitude is -0.833 degrees)
            const sinAlt = Math.sin(-0.833 * Math.PI / 180);
            const cosHourAngle = (sinAlt - Math.sin(latRad) * Math.sin(declRad)) / (Math.cos(latRad) * Math.cos(declRad));
            
            if (cosHourAngle > 1) {
                document.getElementById('text-output').value = "Polar Night: Sun does not rise at this latitude on this date.";
                return;
            }
            if (cosHourAngle < -1) {
                document.getElementById('text-output').value = "Midnight Sun: Sun does not set (always above horizon).";
                return;
            }
            
            const hourAngle = Math.acos(cosHourAngle) * 180 / Math.PI;
            // Solar Noon in local time (simplified approximation)
            const solarNoon = 12.0 - (lng / 15.0); // timezone adjustment neglected in basic calc
            const riseTimeDec = solarNoon - (hourAngle / 15.0);
            
            let hr = Math.floor(riseTimeDec);
            let mn = Math.floor((riseTimeDec - hr) * 60);
            if (hr < 0) hr += 24;
            hr = hr % 24;
            
            const outTime = `${hr.toString().padStart(2,'0')}:${mn.toString().padStart(2,'0')}`;
            
            document.getElementById('text-output').value = 
                `SUNRISE CALCULATION RESULTS:\\n` +
                `========================================\\n` +
                ` Latitude  : ${lat.toFixed(4)}\\n` +
                ` Longitude : ${lng.toFixed(4)}\\n` +
                ` Date      : ${date.toLocaleDateString()}\\n` +
                ` Sunrise   : ${outTime} (Approx Local Solar)\\n` +
                `========================================\\n` +
                `Note: Does not account for daylight savings.`;
            updateBreakdown("<p>Resolved solar geometry variables.</p>");
        """
    },
    {
        "name": "Sunset Calculator",
        "slug": "sunset-calculator",
        "category": "Astronomy & Natural Time Tools",
        "icon": "🌇",
        "desc": "Find the precise local sunset hour for any global latitude and date coordinates.",
        "formula": "Sunset = SolarNoon + HourAngle/15",
        "formula_desc": "Solves celestial angles to determine when the sun falls below horizon boundaries.",
        "inputs": [
            {"id": "ss-lat", "label": "Latitude (Degrees):", "type": "number", "default": "40.7128", "min": "-90", "max": "90", "step": "0.0001"},
            {"id": "ss-lng", "label": "Longitude (Degrees):", "type": "number", "default": "-74.0060", "min": "-180", "max": "180", "step": "0.0001"},
            {"id": "ss-date", "label": "Target Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Calculated Sunset", "type": "textarea"}
        ],
        "calc_js": """
            const lat = parseFloat(document.getElementById('ss-lat').value) || 0;
            const lng = parseFloat(document.getElementById('ss-lng').value) || 0;
            const dateVal = document.getElementById('ss-date').value;
            
            const date = dateVal ? new Date(dateVal) : new Date();
            const start = new Date(date.getFullYear(), 0, 0);
            const diff = date - start;
            const dayOfYear = Math.floor(diff / (1000 * 60 * 60 * 24));
            
            const decl = 23.45 * Math.sin((2 * Math.PI / 365) * (284 + dayOfYear));
            const declRad = decl * Math.PI / 180;
            const latRad = lat * Math.PI / 180;
            
            const sinAlt = Math.sin(-0.833 * Math.PI / 180);
            const cosHourAngle = (sinAlt - Math.sin(latRad) * Math.sin(declRad)) / (Math.cos(latRad) * Math.cos(declRad));
            
            if (cosHourAngle > 1) {
                document.getElementById('text-output').value = "Polar Night: Sun does not rise.";
                return;
            }
            if (cosHourAngle < -1) {
                document.getElementById('text-output').value = "Midnight Sun: Sun does not set.";
                return;
            }
            
            const hourAngle = Math.acos(cosHourAngle) * 180 / Math.PI;
            const solarNoon = 12.0 - (lng / 15.0);
            const setTimeDec = solarNoon + (hourAngle / 15.0);
            
            let hr = Math.floor(setTimeDec);
            let mn = Math.floor((setTimeDec - hr) * 60);
            if (hr < 0) hr += 24;
            hr = hr % 24;
            
            const outTime = `${hr.toString().padStart(2,'0')}:${mn.toString().padStart(2,'0')}`;
            
            document.getElementById('text-output').value = 
                `SUNSET CALCULATION RESULTS:\\n` +
                `========================================\\n` +
                ` Latitude  : ${lat.toFixed(4)}\\n` +
                ` Longitude : ${lng.toFixed(4)}\\n` +
                ` Date      : ${date.toLocaleDateString()}\\n` +
                ` Sunset    : ${outTime} (Approx Local Solar)\\n` +
                `========================================`;
            updateBreakdown("<p>Sunset solar declination calculated.</p>");
        """
    },
    {
        "name": "Golden Hour Calculator",
        "slug": "golden-hour-calculator",
        "category": "Astronomy & Natural Time Tools",
        "icon": "📷",
        "desc": "Identify the optimal morning and evening golden hours for photography based on solar elevations.",
        "formula": "GoldenHour = SolarNoon +/- HourAngle(6 degrees)",
        "formula_desc": "Determines the timing windows when the sun sits between 6 degrees above and 4 degrees below the horizon.",
        "inputs": [
            {"id": "gh-lat", "label": "Latitude:", "type": "number", "default": "40.7128", "min": "-90", "max": "90", "step": "0.01"},
            {"id": "gh-lng", "label": "Longitude:", "type": "number", "default": "-74.0060", "min": "-180", "max": "180", "step": "0.01"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Golden Hour Intervals", "type": "textarea"}
        ],
        "calc_js": """
            const lat = parseFloat(document.getElementById('gh-lat').value) || 0;
            const lng = parseFloat(document.getElementById('gh-lng').value) || 0;
            const date = new Date();
            
            const start = new Date(date.getFullYear(), 0, 0);
            const diff = date - start;
            const dayOfYear = Math.floor(diff / (1000 * 60 * 60 * 24));
            
            const decl = 23.45 * Math.sin((2 * Math.PI / 365) * (284 + dayOfYear));
            const declRad = decl * Math.PI / 180;
            const latRad = lat * Math.PI / 180;
            
            // Golden hour ends/starts when sun is 6 degrees above horizon
            const cosHourAngle = (Math.sin(6 * Math.PI / 180) - Math.sin(latRad) * Math.sin(declRad)) / (Math.cos(latRad) * Math.cos(declRad));
            
            if (cosHourAngle > 1 || cosHourAngle < -1) {
                document.getElementById('text-output').value = "Golden hour does not occur at this latitude today.";
                return;
            }
            
            const hourAngle = Math.acos(cosHourAngle) * 180 / Math.PI;
            const solarNoon = 12.0 - (lng / 15.0);
            
            const amEndDec = solarNoon - (hourAngle / 15.0);
            const pmStartDec = solarNoon + (hourAngle / 15.0);
            
            function formatDec(val) {
                let h = Math.floor(val);
                let m = Math.floor((val - h) * 60);
                if (h < 0) h += 24;
                return `${h.toString().padStart(2,'0')}:${m.toString().padStart(2,'0')}`;
            }
            
            document.getElementById('text-output').value = 
                `GOLDEN HOUR FORECAST:\\n` +
                `========================================\\n` +
                ` Morning ends around: ${formatDec(amEndDec)} Local Solar\\n` +
                ` Evening begins around: ${formatDec(pmStartDec)} Local Solar\\n` +
                `========================================\\n` +
                `Ideal timing for outdoor photography sessions.`;
            updateBreakdown("<p>Photographic golden hour brackets calculated.</p>");
        """
    },
    {
        "name": "Moon Phase Calculator",
        "slug": "moon-phase-calculator",
        "category": "Astronomy & Natural Time Tools",
        "icon": "🌙",
        "desc": "Calculate the current phase of the moon and its illumination percentage.",
        "formula": "LunarPhase = (Date - KnownNewMoonDate) % 29.53059",
        "formula_desc": "Determines lunar age cycles since the baseline new moon epoch to identify phase segments.",
        "inputs": [
            {"id": "mp-date", "label": "Select Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Lunisolar Results", "type": "textarea"}
        ],
        "calc_js": """
            const dateVal = document.getElementById('mp-date').value;
            const date = dateVal ? new Date(dateVal) : new Date();
            
            // Jan 6, 2000 was a New Moon
            const knownNewMoon = new Date(2000, 0, 6, 18, 14, 0);
            const cycle = 29.530588853 * 24 * 60 * 60 * 1000;
            const diff = date - knownNewMoon;
            
            let phase = (diff % cycle) / cycle;
            if (phase < 0) phase += 1;
            
            const age = phase * 29.53;
            let name = "";
            let illumination = 0;
            
            if (phase < 0.03 || phase > 0.97) { name = "New Moon"; illumination = 0; }
            else if (phase < 0.22) { name = "Waxing Crescent"; illumination = phase * 200; }
            else if (phase < 0.28) { name = "First Quarter"; illumination = 50; }
            else if (phase < 0.47) { name = "Waxing Gibbous"; illumination = (phase - 0.25) * 200 + 50; }
            else if (phase < 0.53) { name = "Full Moon"; illumination = 100; }
            else if (phase < 0.72) { name = "Waning Gibbous"; illumination = 100 - (phase - 0.5) * 200; }
            else if (phase < 0.78) { name = "Third Quarter"; illumination = 50; }
            else { name = "Waning Crescent"; illumination = 50 - (phase - 0.75) * 200; }
            
            document.getElementById('text-output').value = 
                `LUNAR PHASE CLASSIFICATION:\\n` +
                `========================================\\n` +
                ` Date        : ${date.toLocaleDateString()}\\n` +
                ` Phase Name  : ${name}\\n` +
                ` Moon Age    : ${age.toFixed(1)} days\\n` +
                ` Illumination: ${Math.min(100, Math.max(0, illumination)).toFixed(0)}%\\n` +
                `========================================`;
            updateBreakdown("<p>Lunar orbit period modules resolved.</p>");
        """
    },
    {
        "name": "Day Length Calculator",
        "slug": "day-length-calculator",
        "category": "Astronomy & Natural Time Tools",
        "icon": "☀️",
        "desc": "Calculate total daylight photoperiod hours based on latitudinal tilt.",
        "formula": "DayLength = (2 / 15) * acos(-tan(lat) * tan(declination))",
        "formula_desc": "Solves standard astronomical sunrise-to-sunset hour angle offsets.",
        "inputs": [
            {"id": "dl-lat", "label": "Latitude:", "type": "number", "default": "40.7128", "min": "-90", "max": "90", "step": "0.01"},
            {"id": "dl-date", "label": "Target Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Day Length Details", "type": "textarea"}
        ],
        "calc_js": """
            const lat = parseFloat(document.getElementById('dl-lat').value) || 0;
            const dateVal = document.getElementById('dl-date').value;
            const date = dateVal ? new Date(dateVal) : new Date();
            
            const start = new Date(date.getFullYear(), 0, 0);
            const diff = date - start;
            const dayOfYear = Math.floor(diff / (1000 * 60 * 60 * 24));
            
            const decl = 23.45 * Math.sin((2 * Math.PI / 365) * (284 + dayOfYear));
            const declRad = decl * Math.PI / 180;
            const latRad = lat * Math.PI / 180;
            
            const cosH = -Math.tan(latRad) * Math.tan(declRad);
            
            let dayLength = 0;
            if (cosH > 1) {
                dayLength = 0; // Polar Night
            } else if (cosH < -1) {
                dayLength = 24; // Polar Day
            } else {
                const hourAngle = Math.acos(cosH) * 180 / Math.PI;
                dayLength = (2 / 15) * hourAngle;
            }
            
            const hr = Math.floor(dayLength);
            const mn = Math.floor((dayLength - hr) * 60);
            
            document.getElementById('text-output').value = 
                `DAYLIGHT DURATION BREAKDOWN:\\n` +
                `========================================\\n` +
                ` Latitude    : ${lat.toFixed(4)}\\n` +
                ` Date        : ${date.toLocaleDateString()}\\n` +
                `----------------------------------------\\n` +
                ` Day Length  : ${hr} hours, ${mn} minutes\\n` +
                ` Decimal Hrs : ${dayLength.toFixed(3)} hrs\\n` +
                `========================================`;
            updateBreakdown("<p>Latitude-based day length solved.</p>");
        """
    },
    {
        "name": "Night Length Calculator",
        "slug": "night-length-calculator",
        "category": "Astronomy & Natural Time Tools",
        "icon": "🌃",
        "desc": "Calculate total night photoperiod hours based on latitudinal tilt.",
        "formula": "NightLength = 24 - DayLength",
        "formula_desc": "Subtracts the computed daylight hours from a complete 24-hour cycle to yield night duration.",
        "inputs": [
            {"id": "nl-lat", "label": "Latitude:", "type": "number", "default": "40.7128", "min": "-90", "max": "90", "step": "0.01"},
            {"id": "nl-date", "label": "Target Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Night Length Details", "type": "textarea"}
        ],
        "calc_js": """
            const lat = parseFloat(document.getElementById('nl-lat').value) || 0;
            const dateVal = document.getElementById('nl-date').value;
            const date = dateVal ? new Date(dateVal) : new Date();
            
            const start = new Date(date.getFullYear(), 0, 0);
            const diff = date - start;
            const dayOfYear = Math.floor(diff / (1000 * 60 * 60 * 24));
            
            const decl = 23.45 * Math.sin((2 * Math.PI / 365) * (284 + dayOfYear));
            const declRad = decl * Math.PI / 180;
            const latRad = lat * Math.PI / 180;
            
            const cosH = -Math.tan(latRad) * Math.tan(declRad);
            
            let dayLength = 0;
            if (cosH > 1) {
                dayLength = 0;
            } else if (cosH < -1) {
                dayLength = 24;
            } else {
                const hourAngle = Math.acos(cosH) * 180 / Math.PI;
                dayLength = (2 / 15) * hourAngle;
            }
            
            const nightLength = 24 - dayLength;
            const hr = Math.floor(nightLength);
            const mn = Math.floor((nightLength - hr) * 60);
            
            document.getElementById('text-output').value = 
                `NIGHT DURATION BREAKDOWN:\\n` +
                `========================================\\n` +
                ` Latitude    : ${lat.toFixed(4)}\\n` +
                ` Date        : ${date.toLocaleDateString()}\\n` +
                `----------------------------------------\\n` +
                ` Night Length: ${hr} hours, ${mn} minutes\\n` +
                ` Decimal Hrs : ${nightLength.toFixed(3)} hrs\\n` +
                `========================================`;
            updateBreakdown("<p>Latitude-based night length solved.</p>");
        """
    },
    {
        "name": "Solar Time Calculator",
        "slug": "solar-time-calculator",
        "category": "Astronomy & Natural Time Tools",
        "icon": "⏳",
        "desc": "Calculate True Solar Time (sundial time) based on Equation of Time variations.",
        "formula": "SolarTime = LocalTime + 4*(Lng - StandardMeridian) + EoT",
        "formula_desc": "Adjusts local clock time based on longitudinal displacement and Earth orbital eccentricity variables.",
        "inputs": [
            {"id": "slt-lng", "label": "Longitude (Degrees):", "type": "number", "default": "-74.0060", "min": "-180", "max": "180", "step": "0.01"},
            {"id": "slt-std", "label": "Standard Meridian (Degrees):", "type": "number", "default": "-75", "min": "-180", "max": "180", "step": "15"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Solar Time Details", "type": "textarea"}
        ],
        "calc_js": """
            const lng = parseFloat(document.getElementById('slt-lng').value) || 0;
            const std = parseFloat(document.getElementById('slt-std').value) || 0;
            
            const date = new Date();
            const start = new Date(date.getFullYear(), 0, 0);
            const diff = date - start;
            const dayOfYear = Math.floor(diff / (1000 * 60 * 60 * 24));
            
            // Equation of Time (EoT) approximation in minutes
            const b = (2 * Math.PI / 364) * (dayOfYear - 81);
            const eot = 9.87 * Math.sin(2 * b) - 7.53 * Math.cos(b) - 1.5 * Math.sin(b);
            
            const localMin = date.getHours() * 60 + date.getMinutes();
            // Solar time adjustment: 4 minutes per degree longitude variance + EoT minutes
            const solarMin = localMin + 4 * (lng - std) + eot;
            
            let solarHr = Math.floor(solarMin / 60);
            let solarMn = Math.floor(solarMin % 60);
            if (solarHr < 0) solarHr += 24;
            solarHr = solarHr % 24;
            
            const outStr = `${solarHr.toString().padStart(2,'0')}:${solarMn.toString().padStart(2,'0')}`;
            
            document.getElementById('text-output').value = 
                `TRUE SOLAR TIME RESULTS:\\n` +
                `========================================\\n` +
                ` Local Clock Time  : ${date.toLocaleTimeString()}\\n` +
                ` Longitude         : ${lng} degrees\\n` +
                ` Equation of Time  : ${eot.toFixed(2)} minutes\\n` +
                `----------------------------------------\\n` +
                ` True Solar Time   : ${outStr}\\n` +
                `========================================`;
            updateBreakdown("<p>Sundial true solar time coordinates calculated.</p>");
        """
    },
    {
        "name": "Seasonal Calculator",
        "slug": "seasonal-calculator",
        "category": "Astronomy & Natural Time Tools",
        "icon": "🍁",
        "desc": "Check dates of Spring Equinox, Summer Solstice, Autumn Equinox, and Winter Solstice for any given year.",
        "formula": "SolsticeDates = SolsticeOrbit(Year)",
        "formula_desc": "Tracks orbital positions of Earth relative to Solstice declination targets.",
        "inputs": [
            {"id": "sc-year", "label": "Target Year:", "type": "number", "default": "2026", "min": "2000", "max": "2050"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Seasonal Calendar Dates", "type": "textarea"}
        ],
        "calc_js": """
            const yr = parseInt(document.getElementById('sc-year').value) || 2026;
            
            // Standard approximations for equinoxes and solstices
            const spring = new Date(yr, 2, 20); // Mar 20
            const summer = new Date(yr, 5, 21); // Jun 21
            const autumn = new Date(yr, 8, 22); // Sep 22
            const winter = new Date(yr, 11, 21); // Dec 21
            
            document.getElementById('text-output').value = 
                `SEASONAL SOLSTICE & EQUINOX FOR ${yr}:\\n` +
                `========================================\\n` +
                ` Spring Equinox : ${spring.toLocaleDateString()}\\n` +
                ` Summer Solstice: ${summer.toLocaleDateString()}\\n` +
                ` Autumn Equinox : ${autumn.toLocaleDateString()}\\n` +
                ` Winter Solstice: ${winter.toLocaleDateString()}\\n` +
                `========================================`;
            updateBreakdown("<p>Orbital declination estimates loaded.</p>");
        """
    },
    {
        "name": "Equinox Calculator",
        "slug": "equinox-calculator",
        "category": "Astronomy & Natural Time Tools",
        "icon": "🌓",
        "desc": "Check dates of Vernal (Spring) and Autumnal equinoxes.",
        "formula": "EquinoxDate = AstronomyFormula(Year)",
        "formula_desc": "Estimates exact planetary crossing dates for Spring and Fall celestial equator transits.",
        "inputs": [
            {"id": "eq-year", "label": "Target Year:", "type": "number", "default": "2026", "min": "1970", "max": "2099"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Equinox Dates Details", "type": "textarea"}
        ],
        "calc_js": """
            const yr = parseInt(document.getElementById('eq-year').value) || 2026;
            
            const vernal = new Date(yr, 2, 20);
            const autumnal = new Date(yr, 8, 22);
            
            document.getElementById('text-output').value = 
                `PLANETARY EQUINOX TRANSITS FOR ${yr}:\\n` +
                `========================================\\n` +
                ` Vernal Equinox (Spring) : ${vernal.toLocaleDateString()}\\n` +
                ` Autumnal Equinox (Fall) : ${autumnal.toLocaleDateString()}\\n` +
                `========================================`;
            updateBreakdown("<p>Equator solar transit times resolved.</p>");
        """
    },
    {
        "name": "Solstice Calculator",
        "slug": "solstice-calculator",
        "category": "Astronomy & Natural Time Tools",
        "icon": "☀️",
        "desc": "Calculate dates of Summer and Winter solstices.",
        "formula": "SolsticeDate = AstronomyFormula(Year)",
        "formula_desc": "Estimates exact planetary crossing dates for Summer and Winter solar declination points.",
        "inputs": [
            {"id": "sol-year", "label": "Target Year:", "type": "number", "default": "2026", "min": "1970", "max": "2099"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Solstice Dates Details", "type": "textarea"}
        ],
        "calc_js": """
            const yr = parseInt(document.getElementById('sol-year').value) || 2026;
            
            const summer = new Date(yr, 5, 21);
            const winter = new Date(yr, 11, 21);
            
            document.getElementById('text-output').value = 
                `PLANETARY SOLSTICE DECLINATIONS FOR ${yr}:\\n` +
                `========================================\\n` +
                ` Summer Solstice (Jun) : ${summer.toLocaleDateString()}\\n` +
                ` Winter Solstice (Dec) : ${winter.toLocaleDateString()}\\n` +
                `========================================`;
            updateBreakdown("<p>Solstice orbital crossings resolved.</p>");
        """
    }
]

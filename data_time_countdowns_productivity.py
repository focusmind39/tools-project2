# -*- coding: utf-8 -*-
"""
Countdown and Productivity Tools Data
"""

COUNTDOWN_PRODUCTIVITY_TOOLS = [
    {
        "name": "Countdown Timer",
        "slug": "countdown-timer",
        "category": "Countdown Tools",
        "icon": "⏳",
        "desc": "Set a custom duration in hours, minutes, and seconds, and receive an audio alert when the countdown reaches zero.",
        "formula": "Timer = Duration - ElapsedTime",
        "formula_desc": "Maintains an active millisecond count down timer, updating the layout at 1Hz frequency and playing a synthesized audio alert at completion.",
        "inputs": [
            {"id": "ct-hrs", "label": "Hours:", "type": "number", "default": "0", "min": "0", "max": "99"},
            {"id": "ct-mins", "label": "Minutes:", "type": "number", "default": "5", "min": "0", "max": "59"},
            {"id": "ct-secs", "label": "Seconds:", "type": "number", "default": "0", "min": "0", "max": "59"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Countdown Display", "type": "textarea"}
        ],
        "calc_js": """
            if (window.countdownTimerInterval) clearInterval(window.countdownTimerInterval);
            
            const hrs = parseInt(document.getElementById('ct-hrs').value) || 0;
            const mins = parseInt(document.getElementById('ct-mins').value) || 0;
            const secs = parseInt(document.getElementById('ct-secs').value) || 0;
            
            let totalSecs = hrs * 3600 + mins * 60 + secs;
            if (totalSecs <= 0) {
                showToast("Please enter a duration greater than zero.", "error");
                return;
            }
            
            function playAlarm() {
                try {
                    const ctx = new (window.AudioContext || window.webkitAudioContext)();
                    const osc = ctx.createOscillator();
                    const gain = ctx.createGain();
                    osc.connect(gain);
                    gain.connect(ctx.destination);
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(880, ctx.currentTime); // A5 note
                    gain.gain.setValueAtTime(0.5, ctx.currentTime);
                    osc.start();
                    osc.stop(ctx.currentTime + 1.2);
                } catch(e) {
                    console.error("Audio blocked or not supported", e);
                }
            }
            
            function tick() {
                if (totalSecs <= 0) {
                    clearInterval(window.countdownTimerInterval);
                    document.getElementById('text-output').value = "00:00:00\\nTIME IS UP!";
                    playAlarm();
                    showToast("Time is up!", "success");
                    return;
                }
                
                totalSecs--;
                const h = Math.floor(totalSecs / 3600).toString().padStart(2, '0');
                const m = Math.floor((totalSecs % 3600) / 60).toString().padStart(2, '0');
                const s = (totalSecs % 60).toString().padStart(2, '0');
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `            COUNTDOWN ACTIVE            \\n` +
                    `========================================\\n` +
                    `               ${h}:${m}:${s}           \\n` +
                    `========================================\\n` +
                    `Remaining seconds: ${totalSecs}`;
            }
            
            tick();
            window.countdownTimerInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Timer initialized. Active 1Hz ticking loop registered.</p>");
        """
    },
    {
        "name": "Event Countdown",
        "slug": "event-countdown",
        "category": "Countdown Tools",
        "icon": "📆",
        "desc": "Count down to any specific calendar date and time event.",
        "formula": "Timer = TargetDate - Now()",
        "formula_desc": "Retrieves the user designated event epoch, ticking down at 1Hz interval until target is reached.",
        "inputs": [
            {"id": "ec-date", "label": "Event Date:", "type": "date"},
            {"id": "ec-time", "label": "Event Time:", "type": "text", "default": "18:00"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Time Remaining", "type": "textarea"}
        ],
        "calc_js": """
            if (window.eventCountdownInterval) clearInterval(window.eventCountdownInterval);
            
            const dateVal = document.getElementById('ec-date').value;
            const timeVal = document.getElementById('ec-time').value || "00:00";
            
            if (!dateVal) {
                showToast("Please choose an event date.", "error");
                return;
            }
            
            const tParts = timeVal.split(':');
            const target = new Date(dateVal);
            target.setHours(parseInt(tParts[0]) || 0, parseInt(tParts[1]) || 0, 0, 0);
            
            function tick() {
                const now = new Date();
                const diff = target - now;
                
                if (diff <= 0) {
                    clearInterval(window.eventCountdownInterval);
                    document.getElementById('text-output').value = "EVENT HAS ARRIVED!";
                    showToast("Event reached!", "success");
                    return;
                }
                
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                const secs = Math.floor(diff / 1000) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `            EVENT COUNTDOWN             \\n` +
                    `========================================\\n` +
                    `  Time Left: ${days}d : ${hrs}h : ${mins}m : ${secs}s \\n` +
                    `========================================\\n` +
                    `Target Event: ${target.toLocaleString()}`;
            }
            
            tick();
            window.eventCountdownInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Ticking event timer registered locally.</p>");
        """
    },
    {
        "name": "Birthday Countdown",
        "slug": "birthday-countdown",
        "category": "Countdown Tools",
        "icon": "🎂",
        "desc": "Check the precise remaining time until your next annual birthday anniversary.",
        "formula": "Countdown = NextBirthdayDate - Now()",
        "formula_desc": "Solves next birthday date boundary and counts down.",
        "auto_calc": True,
        "inputs": [
            {"id": "bc-birth", "label": "Select Birth Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Countdown Display", "type": "textarea"}
        ],
        "calc_js": """
            if (window.bdayCountdownInterval) clearInterval(window.bdayCountdownInterval);
            
            const birthVal = document.getElementById('bc-birth').value;
            if (!birthVal) {
                showToast("Please pick your birthdate.", "error");
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
                    `         MY BIRTHDAY COUNTDOWN          \\n` +
                    `========================================\\n` +
                    `  Time Left: ${days} Days, ${hrs} Hours, ${mins} Mins, ${secs} Secs\\n` +
                    `========================================\\n` +
                    `Target Date: ${nextBday.toLocaleDateString()}`;
            }
            
            tick();
            window.bdayCountdownInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Ticking next anniversary tracker registered.</p>");
        """
    },
    {
        "name": "Wedding Countdown",
        "slug": "wedding-countdown",
        "category": "Countdown Tools",
        "icon": "💍",
        "desc": "Track the months, days, hours, and seconds remaining until your wedding day.",
        "formula": "Timer = WeddingDate - Now()",
        "formula_desc": "Ticking calculations matching your designated wedding day timestamp.",
        "inputs": [
            {"id": "wc-date", "label": "Wedding Date:", "type": "date"},
            {"id": "wc-time", "label": "Wedding Ceremony Time:", "type": "text", "default": "14:00"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Countdown Display", "type": "textarea"}
        ],
        "calc_js": """
            if (window.weddingCountdownInterval) clearInterval(window.weddingCountdownInterval);
            
            const dateVal = document.getElementById('wc-date').value;
            const timeVal = document.getElementById('wc-time').value || "00:00";
            if (!dateVal) {
                showToast("Please choose your wedding date.", "error");
                return;
            }
            
            const target = new Date(dateVal);
            const tParts = timeVal.split(':');
            target.setHours(parseInt(tParts[0]) || 0, parseInt(tParts[1]) || 0, 0, 0);
            
            function tick() {
                const now = new Date();
                const diff = target - now;
                if (diff <= 0) {
                    clearInterval(window.weddingCountdownInterval);
                    document.getElementById('text-output').value = "CONGRATULATIONS! THE BIG DAY IS HERE!";
                    return;
                }
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                const secs = Math.floor(diff / 1000) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `          WEDDING COUNTDOWN             \\n` +
                    `========================================\\n` +
                    `  Time Left: ${days}d : ${hrs}h : ${mins}m : ${secs}s\\n` +
                    `========================================\\n` +
                    `Target Date: ${target.toLocaleString()}`;
            }
            tick();
            window.weddingCountdownInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Active wedding countdown timer ticking.</p>");
        """
    },
    {
        "name": "Exam Countdown",
        "slug": "exam-countdown",
        "category": "Countdown Tools",
        "icon": "📝",
        "desc": "Check how much study time you have left before your target exam date.",
        "formula": "Timer = ExamDate - Now()",
        "formula_desc": "Solves precise time interval boundaries to manage study preparation schedules.",
        "inputs": [
            {"id": "exc-date", "label": "Exam Date:", "type": "date"},
            {"id": "exc-time", "label": "Exam Start Time:", "type": "text", "default": "09:00"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Countdown Display", "type": "textarea"}
        ],
        "calc_js": """
            if (window.examCountdownInterval) clearInterval(window.examCountdownInterval);
            
            const dateVal = document.getElementById('exc-date').value;
            const timeVal = document.getElementById('exc-time').value || "00:00";
            if (!dateVal) {
                showToast("Please choose the exam date.", "error");
                return;
            }
            
            const target = new Date(dateVal);
            const tParts = timeVal.split(':');
            target.setHours(parseInt(tParts[0]) || 0, parseInt(tParts[1]) || 0, 0, 0);
            
            function tick() {
                const now = new Date();
                const diff = target - now;
                if (diff <= 0) {
                    clearInterval(window.examCountdownInterval);
                    document.getElementById('text-output').value = "EXAM SESSION IS UNDERWAY!";
                    return;
                }
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                const secs = Math.floor(diff / 1000) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `            EXAM COUNTDOWN              \\n` +
                    `========================================\\n` +
                    `  Time Left: ${days}d : ${hrs}h : ${mins}m : ${secs}s\\n` +
                    `========================================\\n` +
                    `Exam target: ${target.toLocaleString()}`;
            }
            tick();
            window.examCountdownInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Study prep countdown interval established.</p>");
        """
    },
    {
        "name": "New Year Countdown",
        "slug": "new-year-countdown",
        "category": "Countdown Tools",
        "icon": "🎆",
        "desc": "Track the exact time remaining until the stroke of midnight on January 1st.",
        "formula": "Timer = Jan_01_NextYear - Now()",
        "formula_desc": "Locates next year boundary, displaying live ticking seconds to midnight.",
        "auto_calc": True,
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "New Year Countdown Display", "type": "textarea"}
        ],
        "calc_js": """
            if (window.newYearInterval) clearInterval(window.newYearInterval);
            
            function tick() {
                const now = new Date();
                const nextYear = now.getFullYear() + 1;
                const target = new Date(nextYear, 0, 1, 0, 0, 0, 0);
                
                const diff = target - now;
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                const secs = Math.floor(diff / 1000) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `       NEW YEAR COUNTDOWN TO ${nextYear}        \\n` +
                    `========================================\\n` +
                    `  Time Left: ${days} Days, ${hrs} Hours, ${mins} Mins, ${secs} Secs\\n` +
                    `========================================\\n` +
                    `Target Midnight: 01/01/${nextYear} 00:00:00`;
            }
            tick();
            window.newYearInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Auto-loaded New Year midnight countdown running.</p>");
        """
    },
    {
        "name": "Holiday Countdown",
        "slug": "holiday-countdown",
        "category": "Countdown Tools",
        "icon": "⛱️",
        "desc": "Count down to major upcoming seasonal holidays and public vacation breaks.",
        "formula": "Timer = HolidayDate - Now()",
        "formula_desc": "Solves annual date of the selected holiday and counts down.",
        "inputs": [
            {"id": "hc-selection", "label": "Select Holiday:", "type": "select", "options": [
                ("christmas", "Christmas Day (Dec 25)"),
                ("halloween", "Halloween (Oct 31)"),
                ("july4", "US Independence Day (July 4)"),
                ("valentines", "Valentine's Day (Feb 14)")
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Countdown Display", "type": "textarea"}
        ],
        "calc_js": """
            if (window.holidayCountdownInterval) clearInterval(window.holidayCountdownInterval);
            
            const selection = document.getElementById('hc-selection').value;
            const now = new Date();
            let targetYear = now.getFullYear();
            let targetMonth = 0;
            let targetDay = 1;
            
            if (selection === 'christmas') {
                targetMonth = 11; targetDay = 25;
            } else if (selection === 'halloween') {
                targetMonth = 9; targetDay = 31;
            } else if (selection === 'july4') {
                targetMonth = 6; targetDay = 4;
            } else if (selection === 'valentines') {
                targetMonth = 1; targetDay = 14;
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
                    `          HOLIDAY COUNTDOWN             \\n` +
                    `========================================\\n` +
                    `  Time Left: ${days}d : ${hrs}h : ${mins}m : ${secs}s\\n` +
                    `========================================\\n` +
                    `Target Date: ${target.toLocaleDateString()}`;
            }
            tick();
            window.holidayCountdownInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Ticking holiday countdown started.</p>");
        """
    },
    {
        "name": "Product Launch Countdown",
        "slug": "product-launch-countdown",
        "category": "Countdown Tools",
        "icon": "🚀",
        "desc": "Create a live countdown for launch announcements and product release goals.",
        "formula": "Timer = ReleaseDate - Now()",
        "formula_desc": "Uses local date definitions to coordinate synchronized product rollouts.",
        "inputs": [
            {"id": "plc-date", "label": "Release Date:", "type": "date"},
            {"id": "plc-time", "label": "Release Time:", "type": "text", "default": "10:00"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Countdown Display", "type": "textarea"}
        ],
        "calc_js": """
            if (window.launchCountdownInterval) clearInterval(window.launchCountdownInterval);
            
            const dateVal = document.getElementById('plc-date').value;
            const timeVal = document.getElementById('plc-time').value || "00:00";
            if (!dateVal) {
                showToast("Please choose the launch date.", "error");
                return;
            }
            
            const target = new Date(dateVal);
            const tParts = timeVal.split(':');
            target.setHours(parseInt(tParts[0]) || 0, parseInt(tParts[1]) || 0, 0, 0);
            
            function tick() {
                const now = new Date();
                const diff = target - now;
                if (diff <= 0) {
                    clearInterval(window.launchCountdownInterval);
                    document.getElementById('text-output').value = "PRODUCT IS LIVE!";
                    return;
                }
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                const secs = Math.floor(diff / 1000) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `          PRODUCT LAUNCH TIMER          \\n` +
                    `========================================\\n` +
                    `  Time Left: ${days}d : ${hrs}h : ${mins}m : ${secs}s\\n` +
                    `========================================\\n` +
                    `Release Target: ${target.toLocaleString()}`;
            }
            tick();
            window.launchCountdownInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Product launch release clock initialized.</p>");
        """
    },
    {
        "name": "Anniversary Countdown",
        "slug": "anniversary-countdown",
        "category": "Countdown Tools",
        "icon": "🎁",
        "desc": "Check remaining days until your corporate, wedding, or custom milestone anniversary.",
        "formula": "Timer = AnniversaryDate - Now()",
        "formula_desc": "Maintains ticking updates relative to annual milestone dates.",
        "inputs": [
            {"id": "ac-date", "label": "Milestone Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Countdown Display", "type": "textarea"}
        ],
        "calc_js": """
            if (window.anniversaryCountdownInterval) clearInterval(window.anniversaryCountdownInterval);
            
            const dateVal = document.getElementById('ac-date').value;
            if (!dateVal) {
                showToast("Please choose the milestone date.", "error");
                return;
            }
            
            const dob = new Date(dateVal);
            
            function tick() {
                const now = new Date();
                let nextAnniv = new Date(now.getFullYear(), dob.getMonth(), dob.getDate());
                if (nextAnniv < now) {
                    nextAnniv.setFullYear(now.getFullYear() + 1);
                }
                
                const diff = nextAnniv - now;
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                const secs = Math.floor(diff / 1000) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `        ANNIVERSARY COUNTDOWN           \\n` +
                    `========================================\\n` +
                    `  Time Left: ${days}d : ${hrs}h : ${mins}m : ${secs}s\\n` +
                    `========================================\\n` +
                    `Target Anniversary: ${nextAnniv.toLocaleDateString()}`;
            }
            tick();
            window.anniversaryCountdownInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Anniversary tracking interval established.</p>");
        """
    },
    {
        "name": "Goal Countdown",
        "slug": "goal-countdown",
        "category": "Countdown Tools",
        "icon": "🎯",
        "desc": "Stay motivated by counting down to your target deadline for specific achievements.",
        "formula": "Timer = GoalDeadline - Now()",
        "formula_desc": "Encourages focus by highlighting ticking seconds left to complete milestones.",
        "inputs": [
            {"id": "gc-date", "label": "Goal Deadline:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Countdown Display", "type": "textarea"}
        ],
        "calc_js": """
            if (window.goalCountdownInterval) clearInterval(window.goalCountdownInterval);
            
            const dateVal = document.getElementById('gc-date').value;
            if (!dateVal) {
                showToast("Please choose your goal deadline date.", "error");
                return;
            }
            
            const target = new Date(dateVal);
            target.setHours(23, 59, 59, 999); // End of target day
            
            function tick() {
                const now = new Date();
                const diff = target - now;
                if (diff <= 0) {
                    clearInterval(window.goalCountdownInterval);
                    document.getElementById('text-output').value = "DEADLINE COMPLETED!";
                    return;
                }
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hrs = Math.floor(diff / (1000 * 60 * 60)) % 24;
                const mins = Math.floor(diff / (1000 * 60)) % 60;
                const secs = Math.floor(diff / 1000) % 60;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `             GOAL DEADLINE              \\n` +
                    `========================================\\n` +
                    `  Time Left: ${days}d : ${hrs}h : ${mins}m : ${secs}s\\n` +
                    `========================================\\n` +
                    `Deadline Target: ${target.toLocaleString()}`;
            }
            tick();
            window.goalCountdownInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Ticking goal timeline active.</p>");
        """
    },
    {
        "name": "Pomodoro Timer",
        "slug": "pomodoro-timer",
        "category": "Productivity Tools",
        "icon": "🍅",
        "desc": "A productivity timer implementing the standard Pomodoro method: 25 minutes of focus followed by a 5-minute break.",
        "formula": "Timer = PomodoroCycle(25m Focus / 5m Break / 15m LongBreak)",
        "formula_desc": "Uses AudioContext alarm triggers and counts session completion counts.",
        "auto_calc": True,
        "inputs": [
            {"id": "pt-mode", "label": "Session Type:", "type": "select", "options": [
                ("focus", "Focus (25 min)"),
                ("short", "Short Break (5 min)"),
                ("long", "Long Break (15 min)")
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Timer Console", "type": "textarea"}
        ],
        "calc_js": """
            if (window.pomodoroInterval) clearInterval(window.pomodoroInterval);
            
            const mode = document.getElementById('pt-mode').value;
            let timeRemaining = 0;
            if (mode === 'focus') timeRemaining = 25 * 60;
            else if (mode === 'short') timeRemaining = 5 * 60;
            else if (mode === 'long') timeRemaining = 15 * 60;
            
            function playAlarm() {
                try {
                    const ctx = new (window.AudioContext || window.webkitAudioContext)();
                    const osc = ctx.createOscillator();
                    const gain = ctx.createGain();
                    osc.connect(gain);
                    gain.connect(ctx.destination);
                    osc.type = 'triangle';
                    osc.frequency.setValueAtTime(660, ctx.currentTime);
                    gain.gain.setValueAtTime(0.4, ctx.currentTime);
                    osc.start();
                    osc.stop(ctx.currentTime + 1.0);
                } catch(e) {}
            }
            
            function tick() {
                if (timeRemaining <= 0) {
                    clearInterval(window.pomodoroInterval);
                    document.getElementById('text-output').value = "SESSION COMPLETED! TAKE A BREAK OR START WORK.";
                    playAlarm();
                    showToast("Pomodoro session completed!", "success");
                    return;
                }
                
                timeRemaining--;
                const m = Math.floor(timeRemaining / 60).toString().padStart(2, '0');
                const s = (timeRemaining % 60).toString().padStart(2, '0');
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `           POMODORO: ${mode.toUpperCase()}          \\n` +
                    `========================================\\n` +
                    `                ${m}:${s}                \\n` +
                    `========================================\\n` +
                    `Click 'Process Text' again to restart or change modes.`;
            }
            
            tick();
            window.pomodoroInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Pomodoro cycle running. 25-minute default focus interval setup.</p>");
        """
    },
    {
        "name": "Focus Timer",
        "slug": "focus-timer",
        "category": "Productivity Tools",
        "icon": "🧠",
        "desc": "A simple customizable focus timer that tracks and logs completed focus blocks.",
        "formula": "Timer = FocusLimit - ElapsedTime",
        "formula_desc": "Initiates active focused intervals and records sessions locally in browser.",
        "inputs": [
            {"id": "ft-dur", "label": "Duration (minutes):", "type": "number", "default": "45", "min": "1", "max": "180"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Focus Console", "type": "textarea"}
        ],
        "calc_js": """
            if (window.focusTimerInterval) clearInterval(window.focusTimerInterval);
            
            const dur = parseInt(document.getElementById('ft-dur').value) || 45;
            let secsLeft = dur * 60;
            
            function tick() {
                if (secsLeft <= 0) {
                    clearInterval(window.focusTimerInterval);
                    document.getElementById('text-output').value = "FOCUS CYCLE COMPLETE! REST FOR A MOMENT.";
                    showToast("Focus duration completed!", "success");
                    return;
                }
                secsLeft--;
                const m = Math.floor(secsLeft / 60).toString().padStart(2, '0');
                const s = (secsLeft % 60).toString().padStart(2, '0');
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `            FOCUS BLOCK ACTIVE          \\n` +
                    `========================================\\n` +
                    `                ${m}:${s}                \\n` +
                    `========================================\\n` +
                    `Focused block duration: ${dur} minutes.`;
            }
            tick();
            window.focusTimerInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Ticking focus tracker established.</p>");
        """
    },
    {
        "name": "Study Timer",
        "slug": "study-timer",
        "category": "Productivity Tools",
        "icon": "📖",
        "desc": "A timer optimized for structured study blocks (e.g. 50 minutes study, 10 minutes rest).",
        "formula": "Timer = StudyCycle(50m Study / 10m Rest)",
        "formula_desc": "Sets up academic session divisions to maximize information retention.",
        "inputs": [
            {"id": "st-mode", "label": "Session:", "type": "select", "options": [
                ("study", "Study Mode (50 Min)"),
                ("rest", "Rest Mode (10 Min)")
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Study Console", "type": "textarea"}
        ],
        "calc_js": """
            if (window.studyTimerInterval) clearInterval(window.studyTimerInterval);
            const mode = document.getElementById('st-mode').value;
            let secs = mode === 'study' ? 50 * 60 : 10 * 60;
            
            function tick() {
                if (secs <= 0) {
                    clearInterval(window.studyTimerInterval);
                    document.getElementById('text-output').value = "ACADEMIC CYCLE COMPLETED!";
                    showToast("Study alarm!", "success");
                    return;
                }
                secs--;
                const m = Math.floor(secs / 60).toString().padStart(2, '0');
                const s = (secs % 60).toString().padStart(2, '0');
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `           STUDY MODE: ${mode.toUpperCase()}         \\n` +
                    `========================================\\n` +
                    `                ${m}:${s}                \\n` +
                    `========================================\\n` +
                    `Maintain optimal academic focus periods.`;
            }
            tick();
            window.studyTimerInterval = setInterval(tick, 1000);
            updateBreakdown("<p> Ticking study session registered.</p>");
        """
    },
    {
        "name": "Work Timer",
        "slug": "work-timer",
        "category": "Productivity Tools",
        "icon": "💻",
        "desc": "Track active task sprints with custom limits and rest interval notifications.",
        "formula": "Timer = WorkSprintDuration",
        "formula_desc": "Encourages time-blocked working sprint segments to avoid exhaustion.",
        "inputs": [
            {"id": "wt-dur", "label": "Sprint Limit (minutes):", "type": "number", "default": "60", "min": "1", "max": "240"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Sprint Console", "type": "textarea"}
        ],
        "calc_js": """
            if (window.workTimerInterval) clearInterval(window.workTimerInterval);
            const mins = parseInt(document.getElementById('wt-dur').value) || 60;
            let secs = mins * 60;
            
            function tick() {
                if (secs <= 0) {
                    clearInterval(window.workTimerInterval);
                    document.getElementById('text-output').value = "SPRINT COMPLETED! STAND UP AND STRETCH.";
                    showToast("Sprint finished!", "success");
                    return;
                }
                secs--;
                const m = Math.floor(secs / 60).toString().padStart(2, '0');
                const s = (secs % 60).toString().padStart(2, '0');
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `             WORK SPRINT ACTIVE         \\n` +
                    `========================================\\n` +
                    `                ${m}:${s}                \\n` +
                    `========================================\\n` +
                    `Total sprint block target: ${mins}m`;
            }
            tick();
            window.workTimerInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Work sprint timer ticking active.</p>");
        """
    },
    {
        "name": "Break Timer",
        "slug": "break-timer",
        "category": "Productivity Tools",
        "icon": "☕",
        "desc": "An adjustable timer for micro-breaks, lunch breaks, and stretching sessions.",
        "formula": "Timer = BreakDuration",
        "formula_desc": "Generates audio notification alerts when micro rest sessions are complete.",
        "inputs": [
            {"id": "bt-dur", "label": "Break Time (minutes):", "type": "number", "default": "10", "min": "1", "max": "60"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Break Console", "type": "textarea"}
        ],
        "calc_js": """
            if (window.breakTimerInterval) clearInterval(window.breakTimerInterval);
            const mins = parseInt(document.getElementById('bt-dur').value) || 10;
            let secs = mins * 60;
            
            function tick() {
                if (secs <= 0) {
                    clearInterval(window.breakTimerInterval);
                    document.getElementById('text-output').value = "BREAK OVER! TIME TO RESUME WORK.";
                    showToast("Break has ended!", "success");
                    return;
                }
                secs--;
                const m = Math.floor(secs / 60).toString().padStart(2, '0');
                const s = (secs % 60).toString().padStart(2, '0');
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `              RESTING BLOCK             \\n` +
                    `========================================\\n` +
                    `                ${m}:${s}                \\n` +
                    `========================================\\n` +
                    `Relax and step away from your monitors.`;
            }
            tick();
            window.breakTimerInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Break timer ticking.</p>");
        """
    },
    {
        "name": "Deep Work Timer",
        "slug": "deep-work-timer",
        "category": "Productivity Tools",
        "icon": "🌊",
        "desc": "Optimize cognitive focus with dedicated 90-minute deep work blocks.",
        "formula": "Timer = DeepWorkCycle(90 minutes)",
        "formula_desc": "Tracks progress through highly demanding cognitive sprint sessions.",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Deep Work Console", "type": "textarea"}
        ],
        "calc_js": """
            if (window.deepWorkInterval) clearInterval(window.deepWorkInterval);
            let secs = 90 * 60;
            
            function tick() {
                if (secs <= 0) {
                    clearInterval(window.deepWorkInterval);
                    document.getElementById('text-output').value = "DEEP WORK BLOCK FINISHED! TAKE A PROLONGED BREAK.";
                    showToast("Deep work session complete!", "success");
                    return;
                }
                secs--;
                const h = Math.floor(secs / 3600).toString().padStart(2, '0');
                const m = Math.floor((secs % 3600) / 60).toString().padStart(2, '0');
                const s = (secs % 60).toString().padStart(2, '0');
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `            DEEP WORK SPAN ACTIVE       \\n` +
                    `========================================\\n` +
                    `              ${h}:${m}:${s}            \\n` +
                    `========================================\\n` +
                    `Maintain absolute focus, close social feeds.`;
            }
            tick();
            window.deepWorkInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Deep Work block registered: 90 minutes focus cycle.</p>");
        """
    },
    {
        "name": "Meeting Timer",
        "slug": "meeting-timer",
        "category": "Productivity Tools",
        "icon": "🤝",
        "desc": "Track and budget meeting discussions to prevent time overflow.",
        "formula": "Timer = MeetingDurationBudget",
        "formula_desc": "A ticking stopwatch layout that tracks elapsed agenda time and remaining minutes.",
        "inputs": [
            {"id": "mt-dur", "label": "Agenda Limit (minutes):", "type": "number", "default": "30", "min": "1", "max": "120"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Meeting Console", "type": "textarea"}
        ],
        "calc_js": """
            if (window.meetingInterval) clearInterval(window.meetingInterval);
            const budget = parseInt(document.getElementById('mt-dur').value) || 30;
            let elapsed = 0;
            
            function tick() {
                elapsed++;
                const remaining = budget * 60 - elapsed;
                const remStr = remaining >= 0 
                    ? `${Math.floor(remaining/60)}m ${remaining%60}s remaining`
                    : `${Math.floor(Math.abs(remaining)/60)}m ${Math.abs(remaining)%60}s OVER BUDGET!`;
                
                const min = Math.floor(elapsed / 60).toString().padStart(2, '0');
                const sec = (elapsed % 60).toString().padStart(2, '0');
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `             MEETING TRACKER            \\n` +
                    `========================================\\n` +
                    `          Elapsed: ${min}:${sec}        \\n` +
                    `========================================\\n` +
                    `Status: ${remStr}`;
            }
            tick();
            window.meetingInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Meeting agenda tracker active.</p>");
        """
    },
    {
        "name": "Presentation Timer",
        "slug": "presentation-timer",
        "category": "Productivity Tools",
        "icon": "📊",
        "desc": "Track your speech time with visual and audio alerts when nearing deadline limits.",
        "formula": "Timer = SpeechDurationLimit",
        "formula_desc": "Helps presenters stay within allocated speaking slot boundaries.",
        "inputs": [
            {"id": "pr-limit", "label": "Time Limit (minutes):", "type": "number", "default": "15", "min": "1", "max": "90"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Speech Console", "type": "textarea"}
        ],
        "calc_js": """
            if (window.presentationInterval) clearInterval(window.presentationInterval);
            const limitMins = parseInt(document.getElementById('pr-limit').value) || 15;
            let elapsedSecs = 0;
            
            function tick() {
                elapsedSecs++;
                const limitSecs = limitMins * 60;
                const left = limitSecs - elapsedSecs;
                
                let warn = "Time status: Normal";
                if (left <= 60 && left > 0) {
                    warn = "WARNING: 1 MINUTE LEFT!";
                } else if (left <= 0) {
                    warn = "TIME EXCEEDED!";
                }
                
                const m = Math.floor(elapsedSecs / 60).toString().padStart(2, '0');
                const s = (elapsedSecs % 60).toString().padStart(2, '0');
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `           PRESENTATION SPEAKER         \\n` +
                    `========================================\\n` +
                    `          Speaking time: ${m}:${s}       \\n` +
                    `========================================\\n` +
                    `Target: ${limitMins}m | ${warn}`;
            }
            tick();
            window.presentationInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Presentation timer tracking speaker slot.</p>");
        """
    },
    {
        "name": "Classroom Timer",
        "slug": "classroom-timer",
        "category": "Productivity Tools",
        "icon": "🏫",
        "desc": "A teacher's utility to budget student tests, quizzes, and classroom team activities.",
        "formula": "Timer = QuizDuration",
        "formula_desc": "Maintains ticking updates for tests or group tasks in the classroom.",
        "inputs": [
            {"id": "crt-dur", "label": "Duration (minutes):", "type": "number", "default": "20", "min": "1", "max": "180"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Classroom Display", "type": "textarea"}
        ],
        "calc_js": """
            if (window.classroomInterval) clearInterval(window.classroomInterval);
            const mins = parseInt(document.getElementById('crt-dur').value) || 20;
            let secs = mins * 60;
            
            function tick() {
                if (secs <= 0) {
                    clearInterval(window.classroomInterval);
                    document.getElementById('text-output').value = "CLASS ACTIVITY COMPLETED! RESUME LESSON.";
                    showToast("Activity complete!", "success");
                    return;
                }
                secs--;
                const m = Math.floor(secs / 60).toString().padStart(2, '0');
                const s = (secs % 60).toString().padStart(2, '0');
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `          CLASSROOM ACTIVITY TIMER       \\n` +
                    `========================================\\n` +
                    `                ${m}:${s}                \\n` +
                    `========================================\\n` +
                    `Budgeted limit: ${mins} minutes.`;
            }
            tick();
            window.classroomInterval = setInterval(tick, 1000);
            updateBreakdown("<p>Classroom activity timer registered.</p>");
        """
    },
    {
        "name": "Productivity Tracker",
        "slug": "productivity-tracker",
        "category": "Productivity Tools",
        "icon": "📈",
        "desc": "Track focused hours, log completed tasks, and calculate your daily productivity score.",
        "formula": "ProdScore = (FocusTimeMinutes / 480) * 100",
        "formula_desc": "Aggregates focused minutes against standard 8-hour target block (480 minutes) to score daily performance percentage.",
        "inputs": [
            {"id": "pt-hours", "label": "Focus Time (Hours):", "type": "number", "default": "4", "min": "0", "max": "24"},
            {"id": "pt-tasks", "label": "Tasks Completed:", "type": "number", "default": "3", "min": "0", "max": "50"},
            {"id": "pt-dist", "label": "Distraction Rating (1-10):", "type": "number", "default": "3", "min": "1", "max": "10"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Productivity Metrics Dashboard", "type": "textarea"}
        ],
        "calc_js": """
            const hours = parseFloat(document.getElementById('pt-hours').value) || 0;
            const tasks = parseInt(document.getElementById('pt-tasks').value) || 0;
            const dist = parseInt(document.getElementById('pt-dist').value) || 1;
            
            const targetMins = 8 * 60; // 8 hour goal
            const focusMins = hours * 60;
            
            // Score = focus % weighted with tasks and distraction penalty
            let score = (focusMins / targetMins) * 70 + (tasks * 6) - (dist * 2);
            if (score > 100) score = 100;
            if (score < 0) score = 0;
            
            let grade = "Excellent";
            if (score < 40) grade = "Low Focus";
            else if (score < 70) grade = "Moderate Focus";
            
            const dashboard = 
                `DAILY PRODUCTIVITY SCORE CARD:\\n` +
                `===============================\\n` +
                ` Score        : ${score.toFixed(1)}%\\n` +
                ` Category     : ${grade}\\n` +
                ` Focus hours  : ${hours} hours\\n` +
                ` Tasks done   : ${tasks}\\n` +
                ` Distractions : ${dist} / 10\\n` +
                `===============================\\n` +
                `Daily target hours: 8.0 hrs`;
            
            document.getElementById('text-output').value = dashboard;
            updateBreakdown(`<p>Score calculated using weighted distraction and task multipliers.</p>`);
        """
    }
]

# -*- coding: utf-8 -*-
"""
Stopwatch and Scheduling Tools Data
"""

STOPWATCH_SCHEDULING_TOOLS = [
    {
        "name": "Online Stopwatch",
        "slug": "online-stopwatch",
        "category": "Stopwatch Tools",
        "icon": "⏱️",
        "desc": "A precise online stopwatch with start, split/lap, pause, and reset features.",
        "formula": "ElapsedTime = CurrentTime - StartTime",
        "formula_desc": "Uses a high-performance 10ms timer loop to track elapsed milliseconds since clicking start.",
        "inputs": [
            {"id": "sw-action", "label": "Control State:", "type": "select", "options": [
                ("start", "Start / Resume"),
                ("pause", "Pause Timer")
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Stopwatch Console", "type": "textarea"}
        ],
        "calc_js": """
            if (!window.swState) {
                window.swState = {
                    running: false,
                    elapsed: 0,
                    start: 0,
                    interval: null
                };
            }
            
            const action = document.getElementById('sw-action').value;
            
            if (action === 'start') {
                if (window.swState.running) return;
                window.swState.running = true;
                window.swState.start = Date.now() - window.swState.elapsed;
                
                window.swState.interval = setInterval(() => {
                    window.swState.elapsed = Date.now() - window.swState.start;
                    const diff = window.swState.elapsed;
                    const ms = Math.floor((diff % 1000) / 10).toString().padStart(2, '0');
                    const sec = Math.floor((diff / 1000) % 60).toString().padStart(2, '0');
                    const min = Math.floor((diff / (1000 * 60)) % 60).toString().padStart(2, '0');
                    const hr = Math.floor(diff / (1000 * 60 * 60)).toString().padStart(2, '0');
                    
                    document.getElementById('text-output').value = 
                        `========================================\\n` +
                        `             STOPWATCH RUNNING          \\n` +
                        `========================================\\n` +
                        `             ${hr}:${min}:${sec}.${ms}          \\n` +
                        `========================================\\n` +
                        `Set action to 'Pause Timer' and click Process to pause.`;
                }, 10);
                showToast("Stopwatch started!");
            } else {
                if (!window.swState.running) return;
                window.swState.running = false;
                clearInterval(window.swState.interval);
                showToast("Stopwatch paused.");
            }
            
            updateBreakdown("<p>Stopwatch toggle registered. Click Reset to clear elapsed time.</p>");
        """
    },
    {
        "name": "Lap Stopwatch",
        "slug": "lap-stopwatch",
        "category": "Stopwatch Tools",
        "icon": "🔄",
        "desc": "A stopwatch optimized for recording and exporting multiple lap splits.",
        "formula": "LapDuration = LapTime - PreviousLapTime",
        "formula_desc": "Captures elapsed delta times upon split clicks and logs them to active dashboard views.",
        "inputs": [
            {"id": "lap-action", "label": "Action Selection:", "type": "select", "options": [
                ("start", "Start / Resume"),
                ("lap", "Record Lap Split"),
                ("pause", "Pause Timer")
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Laps Board", "type": "textarea"}
        ],
        "calc_js": """
            if (!window.lapState) {
                window.lapState = {
                    running: false,
                    elapsed: 0,
                    start: 0,
                    interval: null,
                    laps: []
                };
            }
            
            const act = document.getElementById('lap-action').value;
            
            function formatTime(diff) {
                const ms = Math.floor((diff % 1000) / 10).toString().padStart(2, '0');
                const sec = Math.floor((diff / 1000) % 60).toString().padStart(2, '0');
                const min = Math.floor((diff / (1000 * 60)) % 60).toString().padStart(2, '0');
                return `${min}:${sec}.${ms}`;
            }
            
            function updateDisplay() {
                let out = `Time: ${formatTime(window.lapState.elapsed)}\\n\\n`;
                out += `LAP HISTORY:\\n`;
                out += `===============================\\n`;
                window.lapState.laps.forEach((l, idx) => {
                    out += `Lap ${idx+1.toString().padStart(2)}: ${formatTime(l.lap)} | Cumulative: ${formatTime(l.cum)}\\n`;
                });
                document.getElementById('text-output').value = out;
            }
            
            if (act === 'start') {
                if (window.lapState.running) return;
                window.lapState.running = true;
                window.lapState.start = Date.now() - window.lapState.elapsed;
                window.lapState.interval = setInterval(() => {
                    window.lapState.elapsed = Date.now() - window.lapState.start;
                    updateDisplay();
                }, 50);
                showToast("Timer running!");
            } else if (act === 'lap') {
                if (!window.lapState.running) {
                    showToast("Start the stopwatch first!", "error");
                    return;
                }
                const total = window.lapState.elapsed;
                let prev = 0;
                if (window.lapState.laps.length > 0) {
                    prev = window.lapState.laps[window.lapState.laps.length - 1].cum;
                }
                const lapTime = total - prev;
                window.lapState.laps.push({ lap: lapTime, cum: total });
                showToast("Lap recorded!");
            } else {
                if (!window.lapState.running) return;
                window.lapState.running = false;
                clearInterval(window.lapState.interval);
                showToast("Stopwatch paused.");
            }
            
            updateBreakdown("<p>Lap stopwatch state changes applied successfully.</p>");
        """
    },
    {
        "name": "Sports Stopwatch",
        "slug": "sports-stopwatch",
        "category": "Stopwatch Tools",
        "icon": "⚽",
        "desc": "A sports-oriented coaching timer designed for outdoor training schedules.",
        "formula": "SessionDuration = TimeElapsed",
        "formula_desc": "Keeps sports timing records cleanly in local browser memory.",
        "inputs": [
            {"id": "sp-mode", "label": "Coaching Phase:", "type": "select", "options": [
                ("start", "Start Sprint Timer"),
                ("pause", "Pause Coach Timer")
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Session Log", "type": "textarea"}
        ],
        "calc_js": """
            if (!window.spState) {
                window.spState = { running: false, elapsed: 0, start: 0, interval: null };
            }
            const mode = document.getElementById('sp-mode').value;
            if (mode === 'start') {
                if (window.spState.running) return;
                window.spState.running = true;
                window.spState.start = Date.now() - window.spState.elapsed;
                window.spState.interval = setInterval(() => {
                    window.spState.elapsed = Date.now() - window.spState.start;
                    const diff = window.spState.elapsed;
                    const ms = Math.floor((diff % 1000) / 10).toString().padStart(2, '0');
                    const sec = Math.floor((diff / 1000) % 60).toString().padStart(2, '0');
                    const min = Math.floor((diff / (1000 * 60)) % 60).toString().padStart(2, '0');
                    document.getElementById('text-output').value = `SPORTS SPRINT TIME:\\n${min}:${sec}.${ms}\\n\\nStatus: Active Session`;
                }, 30);
            } else {
                if (!window.spState.running) return;
                window.spState.running = false;
                clearInterval(window.spState.interval);
                showToast("Sprint timing paused.");
            }
            updateBreakdown("<p>Coaching stopwatch event registered.</p>");
        """
    },
    {
        "name": "Race Timer",
        "slug": "race-timer",
        "category": "Stopwatch Tools",
        "icon": "🏎️",
        "desc": "A race-day lap timer designed to track speeds and interval displacements.",
        "formula": "Velocity = Distance / ElapsedTime",
        "formula_desc": "Solves average speeds based on custom elapsed running times.",
        "inputs": [
            {"id": "rt-dist", "label": "Lap Distance (meters):", "type": "number", "default": "100", "min": "1", "max": "10000"},
            {"id": "rt-act", "label": "Race Action:", "type": "select", "options": [
                ("start", "Start Clock"),
                ("finish", "Finish Lap / Stop")
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Race Log", "type": "textarea"}
        ],
        "calc_js": """
            if (!window.rtState) {
                window.rtState = { running: false, elapsed: 0, start: 0, interval: null };
            }
            const act = document.getElementById('rt-act').value;
            const dist = parseFloat(document.getElementById('rt-dist').value) || 100;
            
            if (act === 'start') {
                if (window.rtState.running) return;
                window.rtState.running = true;
                window.rtState.start = Date.now();
                window.rtState.interval = setInterval(() => {
                    const diff = Date.now() - window.rtState.start;
                    const sec = (diff / 1000).toFixed(2);
                    document.getElementById('text-output').value = `RACING TIMER:\\nRunning: ${sec} seconds`;
                }, 50);
                showToast("Race clock started!");
            } else {
                if (!window.rtState.running) return;
                window.rtState.running = false;
                clearInterval(window.rtState.interval);
                const finalTime = (Date.now() - window.rtState.start) / 1000;
                const speed = dist / finalTime;
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `              RACE COMPLETED            \\n` +
                    `========================================\\n` +
                    ` Final Time  : ${finalTime.toFixed(3)} seconds\\n` +
                    ` Distance    : ${dist} meters\\n` +
                    ` Avg Speed   : ${speed.toFixed(2)} m/s (${(speed * 3.6).toFixed(2)} km/h)\\n` +
                    `========================================`;
                showToast("Racer finished!");
            }
            updateBreakdown("<p>Race time statistics completed.</p>");
        """
    },
    {
        "name": "Training Timer",
        "slug": "training-timer",
        "category": "Stopwatch Tools",
        "icon": "🏋️",
        "desc": "A workout timer designed for tracking split training sessions and exercise durations.",
        "formula": "TrainingTime = Sum(SetDurations)",
        "formula_desc": "Keeps athletic training tracking logs in browser storage.",
        "inputs": [
            {"id": "tt-act", "label": "Action Mode:", "type": "select", "options": [
                ("start", "Start Set Tracker"),
                ("pause", "Pause Set")
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Workout Console", "type": "textarea"}
        ],
        "calc_js": """
            if (!window.ttState) {
                window.ttState = { running: false, elapsed: 0, start: 0, interval: null };
            }
            const act = document.getElementById('tt-act').value;
            if (act === 'start') {
                if (window.ttState.running) return;
                window.ttState.running = true;
                window.ttState.start = Date.now() - window.ttState.elapsed;
                window.ttState.interval = setInterval(() => {
                    window.ttState.elapsed = Date.now() - window.ttState.start;
                    const sec = Math.floor(window.ttState.elapsed / 1000);
                    document.getElementById('text-output').value = `TRAINING ACTIVE:\\nTime: ${sec}s`;
                }, 200);
            } else {
                if (!window.ttState.running) return;
                window.ttState.running = false;
                clearInterval(window.ttState.interval);
                showToast("Set paused.");
            }
            updateBreakdown("<p>Set log session updated.</p>");
        """
    },
    {
        "name": "Fitness Stopwatch",
        "slug": "fitness-stopwatch",
        "category": "Stopwatch Tools",
        "icon": "💪",
        "desc": "A stopwatch that tracks workout durations and estimates standard metabolic calorie burn metrics.",
        "formula": "CalorieBurn = MET * 3.5 * Weight / 200 * Time(Minutes)",
        "formula_desc": "Calculates exercise calorie burn indicators based on standard MET activity levels.",
        "inputs": [
            {"id": "fs-weight", "label": "Body Weight (kg):", "type": "number", "default": "70", "min": "30", "max": "200"},
            {"id": "fs-met", "label": "Workout Type (MET):", "type": "select", "options": [
                ("6", "Moderate Jogging (MET 6.0)"),
                ("8", "Vigorous Running (MET 8.0)"),
                ("4", "Calisthenics/Yoga (MET 4.0)")
            ]},
            {"id": "fs-act", "label": "Timer State:", "type": "select", "options": [
                ("start", "Start Workout"),
                ("stop", "Stop / Log calories")
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Fitness Dashboard", "type": "textarea"}
        ],
        "calc_js": """
            if (!window.fsState) {
                window.fsState = { running: false, elapsed: 0, start: 0, interval: null };
            }
            const act = document.getElementById('fs-act').value;
            const w = parseFloat(document.getElementById('fs-weight').value) || 70;
            const met = parseFloat(document.getElementById('fs-met').value) || 6;
            
            if (act === 'start') {
                if (window.fsState.running) return;
                window.fsState.running = true;
                window.fsState.start = Date.now() - window.fsState.elapsed;
                window.fsState.interval = setInterval(() => {
                    window.fsState.elapsed = Date.now() - window.fsState.start;
                    const sec = Math.floor(window.fsState.elapsed / 1000);
                    const mins = sec / 60;
                    const burn = met * 3.5 * w / 200 * mins;
                    document.getElementById('text-output').value = `WORKOUT CLOCK:\\nTime: ${sec}s\\nEst. Calorie Burn: ${burn.toFixed(2)} kcal`;
                }, 1000);
                showToast("Workout started!");
            } else {
                if (!window.fsState.running) return;
                window.fsState.running = false;
                clearInterval(window.fsState.interval);
                const finalSecs = window.fsState.elapsed / 1000;
                const burn = met * 3.5 * w / 200 * (finalSecs / 60);
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `            WORKOUT REVIEW              \\n` +
                    `========================================\\n` +
                    ` Duration   : ${(finalSecs/60).toFixed(2)} minutes\\n` +
                    ` Total Burn : ${burn.toFixed(1)} Calories (kcal)\\n` +
                    ` MET Rating : ${met.toFixed(1)}\\n` +
                    `========================================`;
                showToast("Workout ended!");
            }
            updateBreakdown("<p>Calorie estimation logs processed successfully.</p>");
        """
    },
    {
        "name": "Running Stopwatch",
        "slug": "running-stopwatch",
        "category": "Stopwatch Tools",
        "icon": "🏃",
        "desc": "A stopwatch with integrated pace estimation algorithms for running workouts.",
        "formula": "Pace = Time / Distance",
        "formula_desc": "Solves minutes-per-kilometer pace calculations relative to run time intervals.",
        "inputs": [
            {"id": "rs-dist", "label": "Target Distance (km):", "type": "number", "default": "5", "min": "1", "max": "100"},
            {"id": "rs-act", "label": "Runner Control:", "type": "select", "options": [
                ("start", "Start Running"),
                ("stop", "Finish Run")
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Pace Console", "type": "textarea"}
        ],
        "calc_js": """
            if (!window.rsState) {
                window.rsState = { running: false, elapsed: 0, start: 0, interval: null };
            }
            const act = document.getElementById('rs-act').value;
            const dist = parseFloat(document.getElementById('rs-dist').value) || 5;
            
            if (act === 'start') {
                if (window.rsState.running) return;
                window.rsState.running = true;
                window.rsState.start = Date.now() - window.rsState.elapsed;
                window.rsState.interval = setInterval(() => {
                    window.rsState.elapsed = Date.now() - window.rsState.start;
                    const sec = Math.floor(window.rsState.elapsed / 1000);
                    document.getElementById('text-output').value = `RUN ACTIVE:\\nTime: ${sec}s`;
                }, 1000);
                showToast("Running tracker active!");
            } else {
                if (!window.rsState.running) return;
                window.rsState.running = false;
                clearInterval(window.rsState.interval);
                const elapsedSecs = window.rsState.elapsed / 1000;
                
                const avgSecsPerKm = elapsedSecs / dist;
                const paceMin = Math.floor(avgSecsPerKm / 60);
                const paceSec = Math.floor(avgSecsPerKm % 60);
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `             RUN STATISTICS             \\n` +
                    `========================================\\n` +
                    ` Distance   : ${dist} km\\n` +
                    ` Total Time : ${Math.floor(elapsedSecs/60)}m ${Math.floor(elapsedSecs%60)}s\\n` +
                    ` Avg Pace   : ${paceMin}:${paceSec.toString().padStart(2, '0')} /km\\n` +
                    `========================================`;
                showToast("Run logged!");
            }
            updateBreakdown("<p>Pace tracker stopwatch logs finalized.</p>");
        """
    },
    {
        "name": "Swimming Stopwatch",
        "slug": "swimming-stopwatch",
        "category": "Stopwatch Tools",
        "icon": "🏊",
        "desc": "A swimmer's stopwatch optimized for recording pool lap splits and stroke pace intervals.",
        "formula": "Pace = TimeElapsed / PoolLaps",
        "formula_desc": "Analyzes average split durations per length of pool structured in workspace memory.",
        "inputs": [
            {"id": "swm-pool", "label": "Pool Length (meters):", "type": "number", "default": "25", "min": "10", "max": "100"},
            {"id": "swm-act", "label": "Swimmer Action:", "type": "select", "options": [
                ("start", "Start Swim Clock"),
                ("lap", "Touch Wall / Lap Split"),
                ("stop", "End Swim session")
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Swimmer Console", "type": "textarea"}
        ],
        "calc_js": """
            if (!window.swmState) {
                window.swmState = { running: false, elapsed: 0, start: 0, interval: null, laps: [] };
            }
            const act = document.getElementById('swm-act').value;
            const len = parseFloat(document.getElementById('swm-pool').value) || 25;
            
            function showSwm() {
                const totalSec = window.swmState.elapsed / 1000;
                let out = `Total Swim Time: ${totalSec.toFixed(1)}s\\n`;
                out += `Laps Swum: ${window.swmState.laps.length}\\n\\n`;
                out += `WALL SPLIT LOGS:\\n`;
                out += `===============================\\n`;
                window.swmState.laps.forEach((l, i) => {
                    out += `Lap ${i+1}: ${l.toFixed(1)}s (${(len/l).toFixed(2)} m/s)\\n`;
                });
                document.getElementById('text-output').value = out;
            }
            
            if (act === 'start') {
                if (window.swmState.running) return;
                window.swmState.running = true;
                window.swmState.start = Date.now() - window.swmState.elapsed;
                window.swmState.interval = setInterval(() => {
                    window.swmState.elapsed = Date.now() - window.swmState.start;
                    showSwm();
                }, 200);
            } else if (act === 'lap') {
                if (!window.swmState.running) return;
                const current = window.swmState.elapsed;
                let prev = 0;
                if (window.swmState.laps.length > 0) {
                    prev = window.swmState.laps.reduce((a,b)=>a+b, 0) * 1000;
                }
                const lapSecs = (current - prev) / 1000;
                window.swmState.laps.push(lapSecs);
                showToast("Lap captured!");
            } else {
                if (!window.swmState.running) return;
                window.swmState.running = false;
                clearInterval(window.swmState.interval);
                showToast("Swimmer clock paused.");
            }
            updateBreakdown("<p>Pool splits logged.</p>");
        """
    },
    {
        "name": "Interval Stopwatch",
        "slug": "interval-stopwatch",
        "category": "Stopwatch Tools",
        "icon": "⚡",
        "desc": "A custom training timer for configuring and tracking high-intensity interval training (HIIT) workout loops.",
        "formula": "Timer = Loop(WorkPeriod + RestPeriod)",
        "formula_desc": "Automates repeating series of active workout sprints and short rest periods.",
        "inputs": [
            {"id": "is-work", "label": "Work Interval (seconds):", "type": "number", "default": "40", "min": "5", "max": "300"},
            {"id": "is-rest", "label": "Rest Interval (seconds):", "type": "number", "default": "20", "min": "5", "max": "300"},
            {"id": "is-rounds", "label": "Rounds Count:", "type": "number", "default": "8", "min": "1", "max": "50"}
        ],
        "outputs": [
            {"id": "text-output", "label": "HIIT Console", "type": "textarea"}
        ],
        "calc_js": """
            if (window.hiitInterval) clearInterval(window.hiitInterval);
            
            const work = parseInt(document.getElementById('is-work').value) || 40;
            const rest = parseInt(document.getElementById('is-rest').value) || 20;
            const totalRounds = parseInt(document.getElementById('is-rounds').value) || 8;
            
            let round = 1;
            let isWorkPhase = true;
            let timeRemaining = work;
            
            function tick() {
                if (round > totalRounds) {
                    clearInterval(window.hiitInterval);
                    document.getElementById('text-output').value = "HIIT WORKOUT COMPLETED! GOOD JOB.";
                    showToast("HIIT session finished!", "success");
                    return;
                }
                
                if (timeRemaining <= 0) {
                    if (isWorkPhase) {
                        isWorkPhase = false;
                        timeRemaining = rest;
                        showToast("Switch to REST!", "success");
                    } else {
                        isWorkPhase = true;
                        timeRemaining = work;
                        round++;
                        showToast(`Round ${round} WORK!`, "success");
                    }
                }
                
                timeRemaining--;
                const phaseText = isWorkPhase ? "WORK HARD" : "RESTING";
                
                document.getElementById('text-output').value = 
                    `========================================\\n` +
                    `             HIIT INTERVALS             \\n` +
                    `========================================\\n` +
                    ` Round: ${round} / ${totalRounds} | Phase: ${phaseText}\\n` +
                    ` Remaining Seconds: ${timeRemaining}s\\n` +
                    `========================================\\n` +
                    `Configured: ${work}s work / ${rest}s rest`;
            }
            
            tick();
            window.hiitInterval = setInterval(tick, 1000);
            updateBreakdown("<p>HIIT interval loop started.</p>");
        """
    },
    {
        "name": "Precision Stopwatch",
        "slug": "precision-stopwatch",
        "category": "Stopwatch Tools",
        "icon": "⏳",
        "desc": "A millisecond-precise stopwatch display featuring microsecond accuracy clocks.",
        "formula": "PreciseTime = Date.now() - Start",
        "formula_desc": "Synchronizes DOM render operations to the highest available browser animation frame speed.",
        "inputs": [
            {"id": "ps-act", "label": "Action:", "type": "select", "options": [
                ("start", "Start High Precision"),
                ("stop", "Stop / Display Split")
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "High-Res display", "type": "textarea"}
        ],
        "calc_js": """
            if (!window.psState) {
                window.psState = { running: false, elapsed: 0, start: 0, interval: null };
            }
            const act = document.getElementById('ps-act').value;
            if (act === 'start') {
                if (window.psState.running) return;
                window.psState.running = true;
                window.psState.start = performance.now() - window.psState.elapsed;
                
                window.psState.interval = setInterval(() => {
                    window.psState.elapsed = performance.now() - window.psState.start;
                    const diff = window.psState.elapsed;
                    const ms = (diff % 1000).toFixed(1).padStart(5, '0');
                    const sec = Math.floor((diff / 1000) % 60).toString().padStart(2, '0');
                    const min = Math.floor((diff / (1000 * 60)) % 60).toString().padStart(2, '0');
                    
                    document.getElementById('text-output').value = `PRECISION STOPWATCH:\\n${min}:${sec}:${ms} ms\\n\\nUses performance.now() epoch index.`;
                }, 16); // ~60fps
                showToast("Precision clock started!");
            } else {
                if (!window.psState.running) return;
                window.psState.running = false;
                clearInterval(window.psState.interval);
                showToast("Clock paused.");
            }
            updateBreakdown("<p>Performance clock delta computed.</p>");
        """
    },
    {
        "name": "Meeting Planner",
        "slug": "meeting-planner",
        "category": "Scheduling Tools",
        "icon": "📅",
        "desc": "Plan and structure agenda slots for business meetings or workshop sessions.",
        "formula": "Schedule = StartTime + CumulativeSlotDurations",
        "formula_desc": "Sequentially schedules items based on their duration relative to the starting hour.",
        "inputs": [
            {"id": "mp-start", "label": "Start Hour (HH:MM):", "type": "text", "default": "09:00"},
            {"id": "mp-items", "label": "Agenda Topics & Durations:", "type": "textarea", "default": "Introduction: 10\\nProject Update: 20\\nBrainstorming: 30\\nQ&A: 15"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted Meeting Agenda", "type": "textarea"}
        ],
        "calc_js": """
            const startStr = document.getElementById('mp-start').value || "09:00";
            const itemsStr = document.getElementById('mp-items').value;
            
            const parts = startStr.split(':');
            let hour = parseInt(parts[0]) || 9;
            let min = parseInt(parts[1]) || 0;
            
            if (!itemsStr.trim()) {
                showToast("Please enter agenda items.", "error");
                return;
            }
            
            let agenda = `MEETING AGENDA PLANNER:\\n`;
            agenda += `===============================\\n`;
            
            const lines = itemsStr.split('\\n');
            lines.forEach(l => {
                if (!l.includes(':')) return;
                const lParts = l.split(':');
                const title = lParts[0].trim();
                const dur = parseInt(lParts[1]) || 0;
                
                const timeStr = `${hour.toString().padStart(2, '0')}:${min.toString().padStart(2, '0')}`;
                agenda += `${timeStr} - ${title} (${dur} mins)\\n`;
                
                min += dur;
                hour += Math.floor(min / 60);
                min = min % 60;
                hour = hour % 24;
            });
            
            document.getElementById('text-output').value = agenda;
            updateBreakdown("<p>Chronological agenda layout built.</p>");
        """
    },
    {
        "name": "Meeting Time Finder",
        "slug": "meeting-time-finder",
        "category": "Scheduling Tools",
        "icon": "🔍",
        "desc": "Find the best common meeting slot based on team member availabilities.",
        "formula": "Overlap = SetIntersection(Availabilities)",
        "formula_desc": "Intersects hour ranges across multiple staff lists to locate mutually open business hours.",
        "inputs": [
            {"id": "mtf-member1", "label": "User A Available Hours:", "type": "text", "default": "09:00-12:00, 14:00-17:00"},
            {"id": "mtf-member2", "label": "User B Available Hours:", "type": "text", "default": "10:00-13:00, 15:00-18:00"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Matching Open Slots", "type": "textarea"}
        ],
        "calc_js": """
            const m1 = document.getElementById('mtf-member1').value;
            const m2 = document.getElementById('mtf-member2').value;
            
            function getHourSet(str) {
                const hrs = new Set();
                const slots = str.split(',');
                slots.forEach(s => {
                    const range = s.split('-');
                    if (range.length !== 2) return;
                    const start = parseInt(range[0].split(':')[0]) || 0;
                    const end = parseInt(range[1].split(':')[0]) || 0;
                    for (let h = start; h < end; h++) {
                        hrs.add(h);
                    }
                });
                return hrs;
            }
            
            const set1 = getHourSet(m1);
            const set2 = getHourSet(m2);
            const overlap = [];
            
            for (let h = 0; h < 24; h++) {
                if (set1.has(h) && set2.has(h)) {
                    overlap.push(`${h.toString().padStart(2, '0')}:00 - ${(h+1).toString().padStart(2, '0')}:00`);
                }
            }
            
            let out = "MUTUALLY AVAILABLE SLOTS:\\n";
            out += "===============================\\n";
            if (overlap.length === 0) {
                out += "No overlapping slot found!";
            } else {
                overlap.forEach(slot => {
                    out += `- ${slot}\\n`;
                });
            }
            document.getElementById('text-output').value = out;
            updateBreakdown("<p>Mutual availability matrices evaluated.</p>");
        """
    },
    {
        "name": "Time Zone Meeting Planner",
        "slug": "time-zone-meeting-planner",
        "category": "Scheduling Tools",
        "icon": "🌐",
        "desc": "Find overlapping meeting slots for remote team members located in different time zones.",
        "formula": "CommonSlot = LocalTime - TimeZoneOffsetDifference",
        "formula_desc": "Maps target hours across selected timezone offsets to display corresponding local times side-by-side.",
        "inputs": [
            {"id": "tzmp-time", "label": "Target Meeting Time (Host Local):", "type": "text", "default": "14:00"},
            {"id": "tzmp-host", "label": "Host Time Zone:", "type": "select", "options": [("America/New_York", "New York (EST/EDT)"), ("Europe/London", "London (GMT/BST)"), ("Asia/Kolkata", "India (IST)"), ("Asia/Tokyo", "Tokyo (JST)")]},
            {"id": "tzmp-guest", "label": "Guest Time Zone:", "type": "select", "options": [("Asia/Kolkata", "India (IST)"), ("America/New_York", "New York (EST/EDT)"), ("Europe/London", "London (GMT/BST)"), ("Asia/Tokyo", "Tokyo (JST)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Time Zone Comparisons", "type": "textarea"}
        ],
        "calc_js": """
            const timeStr = document.getElementById('tzmp-time').value || "14:00";
            const hostTz = document.getElementById('tzmp-host').value;
            const guestTz = document.getElementById('tzmp-guest').value;
            
            const parts = timeStr.split(':');
            const hrs = parseInt(parts[0]) || 0;
            const mins = parseInt(parts[1]) || 0;
            
            const now = new Date();
            // Host target date
            const hostDate = new Date(now.getFullYear(), now.getMonth(), now.getDate(), hrs, mins, 0, 0);
            
            try {
                // Formatting host and guest times
                const optHost = { timeZone: hostTz, hour: '2-digit', minute: '2-digit', hour12: true };
                const optGuest = { timeZone: guestTz, hour: '2-digit', minute: '2-digit', hour12: true };
                
                const hostStr = hostDate.toLocaleTimeString('en-US', optHost);
                const guestStr = hostDate.toLocaleTimeString('en-US', optGuest);
                
                document.getElementById('text-output').value = 
                    `TIME ZONE MEETING SCHEDULE:\\n` +
                    `========================================\\n` +
                    ` Host Zone (${hostTz}) : ${hostStr}\\n` +
                    ` Guest Zone (${guestTz}): ${guestStr}\\n` +
                    `========================================`;
            } catch(e) {
                document.getElementById('text-output').value = "Error comparing timezones: " + e.message;
            }
            updateBreakdown("<p>Computed relative timezone displacement for target meeting.</p>");
        """
    },
    {
        "name": "Appointment Scheduler",
        "slug": "appointment-scheduler",
        "category": "Scheduling Tools",
        "icon": "📆",
        "desc": "A scheduling assistant to help divide your day into clean, structured appointment slots.",
        "formula": "Slots = StartTime + index * SlotDuration",
        "formula_desc": "Generates list of individual appointment blocks based on opening hours and duration parameters.",
        "inputs": [
            {"id": "as-start", "label": "Start Hour:", "type": "text", "default": "09:00"},
            {"id": "as-end", "label": "Closing Hour:", "type": "text", "default": "17:00"},
            {"id": "as-slot", "label": "Slot Duration (minutes):", "type": "number", "default": "30", "min": "10", "max": "180"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Slots List", "type": "textarea"}
        ],
        "calc_js": """
            const startVal = document.getElementById('as-start').value || "09:00";
            const endVal = document.getElementById('as-end').value || "17:00";
            const dur = parseInt(document.getElementById('as-slot').value) || 30;
            
            const startParts = startVal.split(':');
            const endParts = endVal.split(':');
            
            let startMin = (parseInt(startParts[0]) || 0) * 60 + (parseInt(startParts[1]) || 0);
            let endMin = (parseInt(endParts[0]) || 0) * 60 + (parseInt(endParts[1]) || 0);
            
            if (startMin >= endMin) {
                showToast("Opening hour must be before closing hour.", "error");
                return;
            }
            
            let out = "APPOINTMENT SLOT OUTLINE:\\n";
            out += "===============================\\n";
            let idx = 1;
            
            for (let m = startMin; m + dur <= endMin; m += dur) {
                const sh = Math.floor(m / 60).toString().padStart(2, '0');
                const sm = (m % 60).toString().padStart(2, '0');
                const eh = Math.floor((m + dur) / 60).toString().padStart(2, '0');
                const em = ((m + dur) % 60).toString().padStart(2, '0');
                
                out += `Slot ${idx.toString().padStart(2)}: ${sh}:${sm} - ${eh}:${em}\\n`;
                idx++;
            }
            
            document.getElementById('text-output').value = out;
            updateBreakdown("<p>Structured appointment schedule established.</p>");
        """
    },
    {
        "name": "Shift Planner",
        "slug": "shift-planner",
        "category": "Scheduling Tools",
        "icon": "🛠️",
        "desc": "Plan and allocate daily employee work shifts based on hours and roles.",
        "formula": "Shift = Role + ShiftTimeRange",
        "formula_desc": "Organizes team members into custom shift blocks to simplify operations.",
        "inputs": [
            {"id": "sp-staff", "label": "Staff Names (comma-separated):", "type": "text", "default": "Alice, Bob, Charlie"},
            {"id": "sp-shifts", "label": "Available Shifts (comma-separated):", "type": "text", "default": "Day (08:00-16:00), Night (16:00-00:00)"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Assigned Shift Board", "type": "textarea"}
        ],
        "calc_js": """
            const staff = document.getElementById('sp-staff').value.split(',').map(s=>s.trim()).filter(s=>s);
            const shifts = document.getElementById('sp-shifts').value.split(',').map(s=>s.trim()).filter(s=>s);
            
            if (staff.length === 0 || shifts.length === 0) {
                showToast("Please enter staff and shift definitions.", "error");
                return;
            }
            
            let out = "STAFF SHIFT PLANNER:\\n";
            out += "========================================\\n";
            staff.forEach((s, idx) => {
                const shift = shifts[idx % shifts.length];
                out += `${s.padEnd(15)} : Assigned to ${shift}\\n`;
            });
            
            document.getElementById('text-output').value = out;
            updateBreakdown("<p>Shift schedules mapped to team rosters.</p>");
        """
    },
    {
        "name": "Work Schedule Generator",
        "slug": "work-schedule-generator",
        "category": "Scheduling Tools",
        "icon": "🏭",
        "desc": "Generate structured weekly work rosters for multiple team members.",
        "formula": "Roster = Map(DaysOfWeek, AssignedStaff)",
        "formula_desc": "Distributes work shift patterns across weekly calendar cycles.",
        "inputs": [
            {"id": "wsg-staff", "label": "Roster Staff List:", "type": "text", "default": "A. Smith, B. Jones, C. Davis"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Weekly Roster Output", "type": "textarea"}
        ],
        "calc_js": """
            const staff = document.getElementById('wsg-staff').value.split(',').map(s=>s.trim()).filter(s=>s);
            if (staff.length === 0) {
                showToast("Please input staff names.", "error");
                return;
            }
            
            const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
            let out = "WEEKLY WORK SCHEDULE ROSTER:\\n";
            out += "========================================\\n";
            days.forEach((day, dIdx) => {
                const morning = staff[dIdx % staff.length];
                const evening = staff[(dIdx + 1) % staff.length];
                out += `${day.padEnd(10)} : Morning Shift: ${morning} | Evening Shift: ${evening}\\n`;
            });
            
            document.getElementById('text-output').value = out;
            updateBreakdown("<p>Completed rolling weekly work schedule generation.</p>");
        """
    },
    {
        "name": "Weekly Planner",
        "slug": "weekly-planner",
        "category": "Scheduling Tools",
        "icon": "📅",
        "desc": "Organize tasks and distribute priorities across the days of the week.",
        "formula": "WeeklyGrid = Map(DaysOfWeek, TasksList)",
        "formula_desc": "Organizes weekly goals and notes into day-by-day blocks.",
        "inputs": [
            {"id": "wp-notes", "label": "Tasks List:", "type": "textarea", "default": "Mon: Workout, Buy groceries\\nTue: Study meeting\\nWed: Code project\\nThu: Client call\\nFri: Review reports"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Weekly Schedule Grid", "type": "textarea"}
        ],
        "calc_js": """
            const notes = document.getElementById('wp-notes').value;
            let out = "WEEKLY SCHEDULE PREVIEW:\\n";
            out += "========================================\\n";
            
            const lines = notes.split('\\n').filter(l=>l.trim());
            lines.forEach(l => {
                out += `[ ] ${l}\\n`;
            });
            document.getElementById('text-output').value = out;
            updateBreakdown("<p>Weekly planner formatted.</p>");
        """
    },
    {
        "name": "Monthly Planner",
        "slug": "monthly-planner",
        "category": "Scheduling Tools",
        "icon": "🗓️",
        "desc": "Organize key deadlines and milestones across a monthly calendar view.",
        "formula": "MonthlyPlanner = Calendar(Month, Year)",
        "formula_desc": "Generates list grids representing daily slots for scheduling monthly projects.",
        "inputs": [
            {"id": "mop-month", "label": "Month Select:", "type": "select", "options": [
                ("0", "January"), ("1", "February"), ("2", "March"), ("3", "April"),
                ("4", "May"), ("5", "June"), ("6", "July"), ("7", "August"),
                ("8", "September"), ("9", "October"), ("10", "November"), ("11", "December")
            ]},
            {"id": "mop-year", "label": "Year Select:", "type": "number", "default": "2026", "min": "2020", "max": "2030"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Month Grid", "type": "textarea"}
        ],
        "calc_js": """
            const month = parseInt(document.getElementById('mop-month').value);
            const year = parseInt(document.getElementById('mop-year').value);
            
            const daysInMonth = new Date(year, month + 1, 0).getDate();
            const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
            
            let grid = `MONTHLY OUTLINE FOR ${monthNames[month].toUpperCase()} ${year}:\\n`;
            grid += `========================================\\n`;
            
            for (let d = 1; d <= daysInMonth; d++) {
                const dateObj = new Date(year, month, d);
                const dayName = dateObj.toLocaleDateString('en-US', { weekday: 'short' });
                grid += `${d.toString().padStart(2)} (${dayName}): [ ] _________________________\\n`;
            }
            
            document.getElementById('text-output').value = grid;
            updateBreakdown("<p>Monthly calendar layout generated.</p>");
        """
    },
    {
        "name": "Daily Planner",
        "slug": "daily-planner",
        "category": "Scheduling Tools",
        "icon": "📋",
        "desc": "Structure your daily goals hour-by-hour to optimize personal productivity.",
        "formula": "DayPlan = HourByHourGrid(08:00 - 20:00)",
        "formula_desc": "Generates hourly timeline splits mapping tasks to calendar times.",
        "inputs": [
            {"id": "dp-goals", "label": "Main Daily Objectives:", "type": "textarea", "default": "Gym at 8am\\nCode review at 10am\\nSync meeting at 2pm"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Daily Hourly Schedule", "type": "textarea"}
        ],
        "calc_js": """
            const goals = document.getElementById('dp-goals').value;
            let out = "DAILY SCHEDULE FOR TODAY:\\n";
            out += "========================================\\n";
            
            const hrs = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"];
            hrs.forEach(h => {
                let match = "";
                goals.split('\\n').forEach(g => {
                    if (g.toLowerCase().includes(h.split(':')[0]) || g.toLowerCase().includes(h.replace(/^0/, ''))) {
                        match += ` - ${g}`;
                    }
                });
                out += `${h}: [ ]${match || " Free"}\\n`;
            });
            
            document.getElementById('text-output').value = out;
            updateBreakdown("<p>Hour-by-hour planning framework compiled.</p>");
        """
    },
    {
        "name": "Event Planner",
        "slug": "event-planner",
        "category": "Scheduling Tools",
        "icon": "🎉",
        "desc": "Schedule milestones and track agenda budgets for large social events.",
        "formula": "EventRoster = TimelineScheduling",
        "formula_desc": "Renders chronological checklists for coordinative team activities.",
        "inputs": [
            {"id": "ep-name", "label": "Event Title:", "type": "text", "default": "Annual Gala"},
            {"id": "ep-steps", "label": "Milestones & Times:", "type": "textarea", "default": "Setup: 09:00\\nWelcome Speech: 18:00\\nDinner Served: 19:30\\nAwards ceremony: 21:00"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Event Timeline Output", "type": "textarea"}
        ],
        "calc_js": """
            const name = document.getElementById('ep-name').value || "Event";
            const steps = document.getElementById('ep-steps').value;
            
            let out = `TIMELINE PLAN FOR: ${name.toUpperCase()}\\n`;
            out += `========================================\\n`;
            steps.split('\\n').forEach(s => {
                if (s.trim()) out += `[ ] ${s}\\n`;
            });
            
            document.getElementById('text-output').value = out;
            updateBreakdown("<p>Milestone planning checklist mapped.</p>");
        """
    }
]

# -*- coding: utf-8 -*-
"""
Database of 20 Developer and AI/Productivity Generator Tools for Enginewheels
"""

DEV_GENERATORS = [
    {
        "category": "Developer Generators",
        "name": "JSON Generator",
        "slug": "json-generator-dev",
        "desc": "Generate custom mock JSON objects with dynamic key-value pairs.",
        "formula": "Structured JSON string representation",
        "formula_desc": "Iterates through chosen mock variables and builds formatted, syntax-highlighted JSON strings.",
        "icon": "☕",
        "inputs": [
            {"id": "json-records", "label": "Number of Records:", "type": "number", "default": "3"}
        ],
        "outputs": [
            {"id": "text-output", "label": "JSON Output:", "type": "textarea"}
        ],
        "calc_js": """
            const qty = parseInt(document.getElementById('json-records').value) || 3;

            const names = ["Alice", "Bob", "Charlie", "David", "Emma"];
            const roles = ["Developer", "Designer", "Manager", "Analyst", "Admin"];

            let list = [];
            for (let i = 0; i < qty; i++) {
                list.push({
                    id: 1000 + i,
                    name: names[i % names.length],
                    role: roles[Math.floor(Math.random() * roles.length)],
                    isActive: Math.random() > 0.3,
                    createdAt: new Date().toISOString().split('T')[0]
                });
            }

            document.getElementById('text-output').value = JSON.stringify(list, null, 2);
            updateBreakdown("<p class='text-success'>Mock JSON array compiled.</p>");
        """
    },
    {
        "category": "Developer Generators",
        "name": "Mock Data Generator",
        "slug": "mock-data-generator-dev",
        "desc": "Generate lists of mock user names, emails, and phone numbers in CSV format.",
        "formula": "CSV row compounding",
        "formula_desc": "Combines header labels and randomized values into comma-separated value (CSV) strings.",
        "icon": "📊",
        "inputs": [
            {"id": "mock-rows", "label": "Rows to Generate:", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "text-output", "label": "CSV Data Output:", "type": "textarea"}
        ],
        "calc_js": """
            const qty = parseInt(document.getElementById('mock-rows').value) || 5;

            const firsts = ["James", "Mary", "John", "Patricia", "Robert"];
            const lasts = ["Smith", "Johnson", "Williams", "Brown", "Jones"];

            let csv = "id,name,email,phone\\n";
            for (let i = 1; i <= qty; i++) {
                let first = firsts[Math.floor(Math.random() * firsts.length)];
                let last = lasts[Math.floor(Math.random() * lasts.length)];
                let name = `${first} ${last}`;
                let email = `${first.toLowerCase()}.${last.toLowerCase()}@example.com`;
                let phone = `+1-555-01${String(Math.floor(Math.random()*90 + 10))}`;
                csv += `${i},"${name}",${email},${phone}\\n`;
            }

            document.getElementById('text-output').value = csv.trim();
            updateBreakdown("<p class='text-success'>Mock CSV data generated.</p>");
        """
    },
    {
        "category": "Developer Generators",
        "name": "SQL Query Generator",
        "slug": "sql-query-generator-dev",
        "desc": "Generate custom SQL INSERT statements for database seeding.",
        "formula": "SQL statement mapping template",
        "formula_desc": "Maps mock data elements to INSERT INTO query statements matching table structures.",
        "icon": "🗄️",
        "inputs": [
            {"id": "sql-table", "label": "Table Name:", "type": "text", "default": "users"},
            {"id": "sql-fields", "label": "Fields (Comma Separated):", "type": "text", "default": "username, email"}
        ],
        "outputs": [
            {"id": "text-output", "label": "SQL Query Output:", "type": "textarea"}
        ],
        "calc_js": """
            const table = document.getElementById('sql-table').value.trim() || "users";
            const fieldsRaw = document.getElementById('sql-fields').value.trim();

            if (!fieldsRaw) {
                showToast("Please enter fields.", "error");
                return;
            }

            const fields = fieldsRaw.split(',').map(f => f.trim()).filter(f => f);
            
            let query = `INSERT INTO ${table} (${fields.join(', ')}) VALUES\\n`;
            
            const records = [];
            for (let r = 0; r < 3; r++) {
                let vals = fields.map(f => {
                    if (f.toLowerCase().includes('id') || f.toLowerCase().includes('status')) {
                        return Math.floor(Math.random() * 100);
                    }
                    return `'value_${Math.floor(Math.random()*90 + 10)}'`;
                });
                records.push(`  (${vals.join(', ')})`);
            }

            query += records.join(',\\n') + ';';
            document.getElementById('text-output').value = query;
            updateBreakdown("<p class='text-success'>SQL insert query statement generated.</p>");
        """
    },
    {
        "category": "Developer Generators",
        "name": "API Response Generator",
        "slug": "api-response-generator-dev",
        "desc": "Generate mock API response payloads for frontend testing.",
        "formula": "Standard HTTP payload mapping",
        "formula_desc": "Outputs structured JSON blocks containing standard status codes and payload descriptions.",
        "icon": "📡",
        "inputs": [
            {"id": "api-status", "label": "HTTP Status Code:", "type": "select", "default": "200",
             "options": [
                 ("200", "200 OK"),
                 ("400", "400 Bad Request"),
                 ("500", "500 Internal Error")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "HTTP Response Payload:", "type": "textarea"}
        ],
        "calc_js": """
            const status = document.getElementById('api-status').value;
            
            let response = {};
            if (status === "200") {
                response = {
                    status: 200,
                    success: true,
                    message: "Data retrieved successfully.",
                    data: {
                        id: 101,
                        name: "Mock API Record",
                        timestamp: new Date().toISOString()
                    }
                };
            } else if (status === "400") {
                response = {
                    status: 400,
                    success: false,
                    error: "Bad Request",
                    message: "Required parameter 'api_key' is missing from headers."
                };
            } else {
                response = {
                    status: 500,
                    success: false,
                    error: "Internal Server Error",
                    message: "The database connection timed out after 5000ms."
                };
            }

            document.getElementById('text-output').value = JSON.stringify(response, null, 2);
            updateBreakdown("<p class='text-success'>Mock HTTP response payload generated.</p>");
        """
    },
    {
        "category": "Developer Generators",
        "name": "UUID Generator",
        "slug": "uuid-generator-dev",
        "desc": "Generate version 4 UUID values client-side.",
        "formula": "RFC4122 Version 4 bits compilation",
        "formula_desc": "Replaces placeholders in a UUID template, forcing specific version bits (4) and variant bits.",
        "icon": "🆔",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "UUID v4 Output:", "type": "textarea"}
        ],
        "calc_js": """
            function genUUID() {
                return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
                    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
                    return v.toString(16);
                });
            }
            document.getElementById('text-output').value = genUUID();
            updateBreakdown("<p class='text-success'>Standard UUID v4 generated.</p>");
        """
    },
    {
        "category": "Developer Generators",
        "name": "JSON Schema Generator",
        "slug": "json-schema-generator-dev",
        "desc": "Generate standard draft-07 JSON Schemas based on input JSON structures.",
        "formula": "JSON object property type mappings",
        "formula_desc": "Parses JSON structures and generates matching JSON Schema drafts mapping data types.",
        "icon": "📋",
        "inputs": [
            {"id": "json-input", "label": "Paste JSON Object:", "type": "textarea", "default": '{\\n  "id": 1,\\n  "name": "Example"\\n}'}
        ],
        "outputs": [
            {"id": "text-output", "label": "JSON Schema Output:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('json-input').value.trim();
            if (!raw) {
                showToast("Please enter a JSON object.", "error");
                return;
            }

            try {
                const obj = JSON.parse(raw);
                
                const schema = {
                    "$schema": "http://json-schema.org/draft-07/schema#",
                    "title": "GeneratedSchema",
                    "type": "object",
                    "properties": {},
                    "required": []
                };

                for (let key in obj) {
                    const val = obj[key];
                    let type = typeof val;
                    if (val === null) type = "null";
                    else if (Array.isArray(val)) type = "array";
                    
                    schema.properties[key] = { "type": type };
                    schema.required.push(key);
                }

                document.getElementById('text-output').value = JSON.stringify(schema, null, 2);
                updateBreakdown("<p class='text-success'>JSON schema drafted successfully.</p>");
            } catch (e) {
                showToast("Invalid JSON syntax: " + e.message, "error");
            }
        """
    },
    {
        "category": "Developer Generators",
        "name": "HTML Boilerplate Generator",
        "slug": "html-boilerplate-generator-dev",
        "desc": "Generate modern HTML5 index.html boilerplate codes.",
        "formula": "HTML5 layout templates",
        "formula_desc": "Builds complete, mobile-responsive HTML5 index pages containing metadata, CSS, and JS links.",
        "icon": "🌐",
        "inputs": [
            {"id": "html-title", "label": "Page Title:", "type": "text", "default": "My Web Application"}
        ],
        "outputs": [
            {"id": "text-output", "label": "HTML5 Boilerplate:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('html-title').value.trim() || "Web App";
            
            const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Welcome to ${title}</h1>
    <p>This page was generated with the Enginewheels HTML Boilerplate Generator.</p>

    <script src="script.js"></script>
</body>
</html>`;

            document.getElementById('text-output').value = html;
            updateBreakdown("<p class='text-success'>HTML5 boilerplate generated.</p>");
        """
    },
    {
        "category": "Developer Generators",
        "name": "CSS Boilerplate Generator",
        "slug": "css-boilerplate-generator-dev",
        "desc": "Generate clean CSS resets and custom variables boilerplates.",
        "formula": "Standard CSS resets mapping",
        "formula_desc": "Outputs CSS layout variables and responsive formatting properties.",
        "icon": "🎨",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "CSS Boilerplate Output:", "type": "textarea"}
        ],
        "calc_js": """
            const css = `/* CSS reset and variable boilerplate */
:root {
    --primary: #7C3AED;
    --secondary: #EF4444;
    --background: #111827;
    --text: #f3f4f6;
}

*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: system-ui, -apple-system, sans-serif;
    background-color: var(--background);
    color: var(--text);
    line-height: 1.5;
}`;

            document.getElementById('text-output').value = css;
            updateBreakdown("<p class='text-success'>CSS boilerplate generated.</p>");
        """
    },
    {
        "category": "Developer Generators",
        "name": "Regex Generator",
        "slug": "regex-generator-dev",
        "desc": "Generate regular expressions for emails, URLs, dates, or numeric values.",
        "formula": "Regex matching patterns",
        "formula_desc": "Formats regular expression characters depending on chosen fields.",
        "icon": "🔍",
        "inputs": [
            {"id": "reg-target", "label": "Regex Goal:", "type": "select", "default": "email",
             "options": [
                 ("email", "Email Validation"),
                 ("url", "URL Validation"),
                 ("digits", "Digits Only")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Regular Expression:", "type": "textarea"}
        ],
        "calc_js": """
            const target = document.getElementById('reg-target').value;
            
            let regex = "";
            let desc = "";
            if (target === "email") {
                regex = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\\\.[a-zA-Z]{2,}$";
                desc = "Matches typical email structures (e.g. user@domain.com).";
            } else if (target === "url") {
                regex = "^https?://(www\\\\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\\\\.[a-zA-Z0-9()]{1,6}\\\\b([-a-zA-Z0-9()@:%_+.~#?&//=]*)$";
                desc = "Matches standard secure and non-secure HTTP web URLs.";
            } else {
                regex = "^[0-9]+$";
                desc = "Matches strings containing digits only.";
            }

            document.getElementById('text-output').value = regex;
            updateBreakdown(`<p class='text-success'>Compiled regex: ${desc}</p>`);
        """
    },
    {
        "category": "Developer Generators",
        "name": "Cron Expression Generator",
        "slug": "cron-expression-generator-dev",
        "desc": "Generate crontab expression scripts for scheduling tasks.",
        "formula": "Cron schedule compilation",
        "formula_desc": "Formats minutes, hours, days, and months selectors into crontab scripts.",
        "icon": "⏰",
        "inputs": [
            {"id": "cron-min", "label": "Minute Interval:", "type": "select", "default": "0",
             "options": [
                 ("0", "Every hour (at minute 0)"),
                 ("*/15", "Every 15 minutes"),
                 ("*", "Every minute")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Cron Expression:", "type": "textarea"}
        ],
        "calc_js": """
            const min = document.getElementById('cron-min').value;
            
            const cron = `${min} * * * *`;
            document.getElementById('text-output').value = cron;
            updateBreakdown(`<p class='text-success'>Cron expression: Runs ${min === "0" ? "hourly at minute 0" : (min === "*/15" ? "every 15 minutes" : "every minute")}.</p>`);
        """
    },
    {
        "category": "AI & Productivity Generators",
        "name": "To-Do List Generator",
        "slug": "todo-list-generator",
        "desc": "Generate custom, structured checklists for projects or daily tasks.",
        "formula": "Todo items array parsing",
        "formula_desc": "Combines action variables to compile structured daily task lists.",
        "icon": "✅",
        "inputs": [
            {"id": "todo-project", "label": "Project/Goal:", "type": "text", "default": "Launch website"}
        ],
        "outputs": [
            {"id": "text-output", "label": "To-Do Checklist:", "type": "textarea"}
        ],
        "calc_js": """
            const goal = document.getElementById('todo-project').value.trim();
            if (!goal) {
                showToast("Please enter a project goal.", "error");
                return;
            }

            const items = [
                `[ ] Define requirements and scope for "${goal}"`,
                `[ ] Research tools and design interfaces`,
                `[ ] Implement core functionality and write logic`,
                `[ ] Run verification audits and check health`,
                `[ ] Publish and announce to audience`
            ];

            document.getElementById('text-output').value = items.join("\\n");
            updateBreakdown("<p class='text-success'>Checklist compiled.</p>");
        """
    },
    {
        "category": "AI & Productivity Generators",
        "name": "Study Plan Generator",
        "slug": "study-plan-generator",
        "desc": "Generate study plans and calendars for learning goals.",
        "formula": "Study timetable structure",
        "formula_desc": "Packs subjects, focus hours, and review slots into daily templates.",
        "icon": "📚",
        "inputs": [
            {"id": "study-subj", "label": "Subject to Study:", "type": "text", "default": "Data Structures"},
            {"id": "study-hours", "label": "Hours per day:", "type": "number", "default": "2"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Suggested Study Plan:", "type": "textarea"}
        ],
        "calc_js": """
            const subj = document.getElementById('study-subj').value.trim();
            const hours = document.getElementById('study-hours').value || 2;

            if (!subj) {
                showToast("Please enter a subject.", "error");
                return;
            }

            const plan = `Daily Study Plan: ${subj} (${hours} Hours/Day)
--------------------------------------------------
Block 1 (40% time): Focus on core concepts and read documentation.
Block 2 (40% time): Active recall and coding practice.
Block 3 (20% time): Review notes and document mistakes.
Tip: Take a 5-minute break every 25 minutes (Pomodoro technique).`;

            document.getElementById('text-output').value = plan;
            updateBreakdown("<p class='text-success'>Study timetable compiled.</p>");
        """
    },
    {
        "category": "AI & Productivity Generators",
        "name": "Workout Plan Generator",
        "slug": "workout-plan-generator",
        "desc": "Generate simple 3-day split workout routines.",
        "formula": "Exercise routine matrix mapping",
        "formula_desc": "Compiles structured physical training timetables based on chosen targets (strength, fitness).",
        "icon": "💪",
        "inputs": [
            {"id": "work-goal", "label": "Workout Focus:", "type": "select", "default": "strength",
             "options": [
                 ("strength", "Strength / Muscle Building"),
                 ("cardio", "Cardio & Weight Loss")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "3-Day Workout Split:", "type": "textarea"}
        ],
        "calc_js": """
            const goal = document.getElementById('work-goal').value;

            let plan = "";
            if (goal === "strength") {
                plan = `Day 1: Push (Chest, Shoulders, Triceps)
- Bench Press: 3 sets x 8 reps
- Overhead Press: 3 sets x 10 reps

Day 2: Pull (Back, Biceps)
- Pull-Ups: 3 sets x max reps
- Barbell Rows: 3 sets x 8 reps

Day 3: Legs (Squats, Calves)
- Barbell Squats: 3 sets x 10 reps
- Romanian Deadlifts: 3 sets x 12 reps`;
            } else {
                plan = `Day 1: Interval Running
- 5 min warm-up jog
- 8 intervals (30s sprint, 90s walk)
- 5 min cool-down

Day 2: Bodyweight Circuit
- 3 rounds of: 15 Squats, 10 Push-ups, 20 Jumping Jacks

Day 3: Steady-State Cardio
- 30-45 minutes of steady cycling or jogging`;
            }

            document.getElementById('text-output').value = plan;
            updateBreakdown("<p class='text-success'>3-day workout routine generated.</p>");
        """
    },
    {
        "category": "AI & Productivity Generators",
        "name": "Daily Routine Generator",
        "slug": "daily-routine-generator",
        "desc": "Generate custom, productive daily routine timetables.",
        "formula": "Time block schedule",
        "formula_desc": "Formats standard time windows (morning, afternoon, evening) with focus blocks.",
        "icon": "⏰",
        "inputs": [
            {"id": "routine-wake", "label": "Wake Up Time:", "type": "text", "default": "7:00 AM"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Productive Routine:", "type": "textarea"}
        ],
        "calc_js": """
            const wake = document.getElementById('routine-wake').value.trim() || "7:00 AM";
            
            const routine = `${wake} - Wake Up & Hydrate
${wake.replace('7:00', '8:00').replace('7', '8')} - Deep Work Focus Block (No distractions)
12:00 PM - Lunch & Quick Walk
1:00 PM - Secondary Focus Block (Meetings, emails)
5:00 PM - Exercise & Dinner
10:00 PM - Wind down and sleep`;

            document.getElementById('text-output').value = routine;
            updateBreakdown("<p class='text-success'>Daily routine generated.</p>");
        """
    },
    {
        "category": "AI & Productivity Generators",
        "name": "Project Idea Generator",
        "slug": "project-idea-generator",
        "desc": "Generate creative ideas for coding side-projects.",
        "formula": "Tech stack + tool combination matrices",
        "formula_desc": "Combines typical tech stacks (React, Python) with tool categories to spawn side project ideas.",
        "icon": "💻",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Suggested Project Ideas:", "type": "textarea"}
        ],
        "calc_js": """
            const projects = [
                "1. Build a client-side Markdown editor with PDF download support using vanilla JavaScript.",
                "2. Create a weather dashboard displaying detailed temperature charts utilizing public API requests.",
                "3. Develop an offline-first password generator dashboard utilizing the Web Crypto API.",
                "4. Build a responsive kanban board using local storage to persist user data."
            ];

            document.getElementById('text-output').value = projects.join("\\n\\n");
            updateBreakdown("<p class='text-success'>Project ideas generated.</p>");
        """
    },
    {
        "category": "AI & Productivity Generators",
        "name": "Startup Idea Generator",
        "slug": "startup-idea-generator",
        "desc": "Generate innovative tech startup ideas by crossing industries.",
        "formula": "Startup concept combination matrix",
        "formula_desc": "Pairs modern tech capabilities with industries to suggest startup business models.",
        "icon": "🚀",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Generated Startup Concept:", "type": "textarea"}
        ],
        "calc_js": """
            const concepts = [
                "An AI-powered tool that automatically converts meeting transcripts into structured blog posts.",
                "A marketplace matching remote developers with local green energy projects.",
                "A micro-SaaS providing zero-knowledge secure cookie storage API wrappers for developers.",
                "An on-demand mobile repair service for e-bikes in metropolitan areas."
            ];

            document.getElementById('text-output').value = concepts[Math.floor(Math.random() * concepts.length)];
            updateBreakdown("<p class='text-success'>Startup concept generated successfully.</p>");
        """
    },
    {
        "category": "AI & Productivity Generators",
        "name": "Side Hustle Idea Generator",
        "slug": "side-hustle-generator",
        "desc": "Generate low-investment side hustle ideas.",
        "formula": "Skill monetizing combinations",
        "formula_desc": "Combines digital skills with monetization platforms to suggest quick income projects.",
        "icon": "🪙",
        "inputs": [
            {"id": "hustle-skill", "label": "Your Core Skill:", "type": "text", "default": "Writing"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Side Hustle Ideas:", "type": "textarea"}
        ],
        "calc_js": """
            const skill = document.getElementById('hustle-skill').value.trim();
            if (!skill) {
                showToast("Please enter a skill.", "error");
                return;
            }

            const ideas = [
                `1. Offer freelance ${skill} services on platforms like Upwork or Fiverr.`,
                `2. Sell digital templates or guides about ${skill} on Gumroad or Etsy.`,
                `3. Start a niche newsletter or blog sharing your experiences with ${skill}.`
            ];

            document.getElementById('text-output').value = ideas.join("\\n\\n");
            updateBreakdown("<p class='text-success'>Side hustle ideas compiled.</p>");
        """
    },
    {
        "category": "AI & Productivity Generators",
        "name": "Marketing Plan Generator",
        "slug": "marketing-plan-generator",
        "desc": "Generate simple 4-step marketing plans for new product launches.",
        "formula": "4-stage launch timelines",
        "formula_desc": "Fills out a standard 4-stage marketing roadmap (Organic SEO, Social media, Email, Referral).",
        "icon": "📈",
        "inputs": [
            {"id": "mkt-product", "label": "Product Name:", "type": "text", "default": "Enginewheels"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Marketing Plan Output:", "type": "textarea"}
        ],
        "calc_js": """
            const prod = document.getElementById('mkt-product').value.trim();
            if (!prod) {
                showToast("Please enter product name.", "error");
                return;
            }

            const plan = `Marketing Plan for ${prod}
--------------------------------------------------
Step 1 (SEO): Optimize page title/meta descriptions and build sitemaps.
Step 2 (Social): Publish 3 punchy updates on Twitter/X and LinkedIn.
Step 3 (Email): Send follow-up launch notes to early testers.
Step 4 (Referral): Create a clear CTA offering discounts to referring users.`;

            document.getElementById('text-output').value = plan;
            updateBreakdown("<p class='text-success'>Marketing plan timeline drafted.</p>");
        """
    },
    {
        "category": "AI & Productivity Generators",
        "name": "Content Calendar Generator",
        "slug": "content-calendar-generator",
        "desc": "Generate 7-day social media content calendars.",
        "formula": "7-day post schedule grids",
        "formula_desc": "Outputs a weekly schedule listing daily topics, platform recommendations, and caption tags.",
        "icon": "📅",
        "inputs": [
            {"id": "cal-niche", "label": "Content Niche:", "type": "text", "default": "Coding Tips"}
        ],
        "outputs": [
            {"id": "text-output", "label": "7-Day Content Calendar:", "type": "textarea"}
        ],
        "calc_js": """
            const niche = document.getElementById('cal-niche').value.trim();
            if (!niche) {
                showToast("Please enter your niche.", "error");
                return;
            }

            const cal = `7-Day Content Calendar: ${niche}
--------------------------------------------------
Mon: Behind-the-scenes update (Format: Image)
Tue: 3 common mistakes in ${niche} (Format: Text)
Wed: Useful tools/libs list (Format: Link)
Thu: Quick Q&A with followers (Format: Q&A)
Fri: Quote/Meme related to ${niche} (Format: Image)
Sat: Weekly wrap-up & future goals (Format: Video)
Sun: Review feedback & rest.`;

            document.getElementById('text-output').value = cal;
            updateBreakdown("<p class='text-success'>7-day content calendar drafted.</p>");
        """
    },
    {
        "category": "AI & Productivity Generators",
        "name": "Goal Planner Generator",
        "slug": "goal-planner-generator",
        "desc": "Generate SMART goal planner worksheets.",
        "formula": "SMART goal worksheet mapping",
        "formula_desc": "Expands user targets into Specific, Measurable, Achievable, Relevant, and Time-bound segments.",
        "icon": "🎯",
        "inputs": [
            {"id": "goal-kw", "label": "Your Core Goal:", "type": "text", "default": "Learn programming"}
        ],
        "outputs": [
            {"id": "text-output", "label": "SMART Goal Sheet:", "type": "textarea"}
        ],
        "calc_js": """
            const goal = document.getElementById('goal-kw').value.trim();
            if (!goal) {
                showToast("Please enter a goal.", "error");
                return;
            }

            const sheet = `SMART Goal Worksheet: "${goal}"
--------------------------------------------------
S (Specific): Clearly define your goal: "${goal}".
M (Measurable): How will you track progress? (e.g. 1 exercise completed per day).
A (Achievable): Is it realistic? Yes, by starting with free online tutorials.
R (Relevant): Why does this matter? To build side projects and boost efficiency.
T (Time-bound): What is the deadline? Achieve the core target within 90 days.`;

            document.getElementById('text-output').value = sheet;
            updateBreakdown("<p class='text-success'>SMART goal worksheet formulated.</p>");
        """
    }
]

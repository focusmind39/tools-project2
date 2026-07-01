# -*- coding: utf-8 -*-
"""
Date & Time, SEO & Marketing, and Lifestyle Calculators Data
"""

TIME_CALCS = [
    {
        "name": "Age In Days Calculator",
        "slug": "age-in-days-calculator",
        "category": "Date & Time",
        "icon": "🕒",
        "desc": "Calculate your exact age in days based on your birthdate.",
        "formula": "Age in Days = Current Date - Birthdate",
        "formula_desc": "Finds the difference in milliseconds between two timestamps and converts to total elapsed days.",
        "inputs": [
            {"id": "aid-birth", "label": "Select Date of Birth", "type": "date", "default": ""}
        ],
        "outputs": [
            {"id": "out-aid-days", "label": "Total Age in Days", "prefix": "", "suffix": " days"},
            {"id": "out-aid-hours", "label": "Approx. Age in Hours", "prefix": "", "suffix": " hours"}
        ],
        "calc_js": """
            const birthStr = document.getElementById('aid-birth').value;
            if (!birthStr) {
                showToast("Please select your birthdate.", "error");
                return;
            }

            const birth = new Date(birthStr);
            const today = new Date();

            if (birth > today) {
                showToast("Birthdate cannot be in the future.", "error");
                return;
            }

            const diffTime = today - birth;
            const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
            const diffHours = diffDays * 24;

            document.getElementById('out-aid-days').textContent = diffDays.toLocaleString();
            document.getElementById('out-aid-hours').textContent = diffHours.toLocaleString();
        """
    },
    {
        "name": "Days Between Dates Calculator",
        "slug": "days-between-dates-calculator",
        "category": "Date & Time",
        "icon": "🕒",
        "desc": "Calculate the total number of calendar days between two selected dates.",
        "formula": "Days = |Date 2 - Date 1|",
        "formula_desc": "Solves absolute difference intervals in standard solar days.",
        "inputs": [
            {"id": "dbd-d1", "label": "Start Date", "type": "date", "default": ""},
            {"id": "dbd-d2", "label": "End Date", "type": "date", "default": ""}
        ],
        "outputs": [
            {"id": "out-dbd-days", "label": "Total Elapsed Days", "prefix": "", "suffix": " days"},
            {"id": "out-dbd-weeks", "label": "Equivalent Weeks", "prefix": "", "suffix": " weeks"}
        ],
        "calc_js": """
            const d1Str = document.getElementById('dbd-d1').value;
            const d2Str = document.getElementById('dbd-d2').value;

            if (!d1Str || !d2Str) {
                showToast("Please choose both start and end dates.", "error");
                return;
            }

            const d1 = new Date(d1Str);
            const d2 = new Date(d2Str);

            const diffTime = Math.abs(d2 - d1);
            const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
            const weeks = (diffDays / 7).toFixed(1);

            document.getElementById('out-dbd-days').textContent = diffDays.toLocaleString();
            document.getElementById('out-dbd-weeks').textContent = weeks;
        """
    },
    {
        "name": "Business Days Calculator",
        "slug": "business-days-calculator",
        "category": "Date & Time",
        "icon": "🕒",
        "desc": "Calculate the count of business working days (excluding weekends) between two dates.",
        "formula": "Working Days = Total Days - Weekends (Saturdays & Sundays)",
        "formula_desc": "Excludes weekend days systematically from calendar day intervals.",
        "inputs": [
            {"id": "bd-d1", "label": "Start Date", "type": "date", "default": ""},
            {"id": "bd-d2", "label": "End Date", "type": "date", "default": ""}
        ],
        "outputs": [
            {"id": "out-bd-working", "label": "Business Days", "prefix": "", "suffix": " working days"},
            {"id": "out-bd-weekends", "label": "Weekend Days Excluded", "prefix": "", "suffix": " weekend days"}
        ],
        "calc_js": """
            const d1Str = document.getElementById('bd-d1').value;
            const d2Str = document.getElementById('bd-d2').value;

            if (!d1Str || !d2Str) {
                showToast("Select both dates.", "error");
                return;
            }

            let start = new Date(d1Str);
            let end = new Date(d2Str);

            if (start > end) {
                // Swap dates
                let temp = start; start = end; end = temp;
            }

            let workingCount = 0;
            let weekendCount = 0;
            let cur = new Date(start.getTime());

            while (cur <= end) {
                const day = cur.getDay();
                if (day === 0 || day === 6) {
                    weekendCount++;
                } else {
                    workingCount++;
                }
                cur.setDate(cur.getDate() + 1);
            }

            document.getElementById('out-bd-working').textContent = workingCount;
            document.getElementById('out-bd-weekends').textContent = weekendCount;
        """
    },
    {
        "name": "Hours Between Times Calculator",
        "slug": "hours-between-times-calculator",
        "category": "Date & Time",
        "icon": "🕒",
        "desc": "Calculate exact hours and minutes elapsed between two active daily time nodes.",
        "formula": "Time Duration = Time 2 - Time 1",
        "formula_desc": "Solves minute offsets between time selectors.",
        "inputs": [
            {"id": "hbt-t1", "label": "Start Time", "type": "select", "options": [
                ("09:00", "09:00 AM"), ("10:00", "10:00 AM"), ("12:00", "12:00 PM"), ("13:00", "01:00 PM"), ("17:00", "05:00 PM"), ("22:00", "10:00 PM")
            ]},
            {"id": "hbt-t2", "label": "End Time", "type": "select", "options": [
                ("17:00", "05:00 PM"), ("18:00", "06:00 PM"), ("22:00", "10:00 PM"), ("23:00", "11:00 PM"), ("09:00", "09:00 AM"), ("12:00", "12:00 PM")
            ]}
        ],
        "outputs": [
            {"id": "out-hbt-hours", "label": "Duration (Hours)", "prefix": "", "suffix": " hours"},
            {"id": "out-hbt-minutes", "label": "Duration (Minutes)", "prefix": "", "suffix": " minutes"}
        ],
        "calc_js": """
            const t1 = document.getElementById('hbt-t1').value;
            const t2 = document.getElementById('hbt-t2').value;

            const [h1, m1] = t1.split(':').map(Number);
            const [h2, m2] = t2.split(':').map(Number);

            let diffMins = (h2 * 60 + m2) - (h1 * 60 + m1);
            if (diffMins < 0) {
                // cross midnight
                diffMins += 24 * 60;
            }

            const hrs = diffMins / 60;
            document.getElementById('out-hbt-hours').textContent = hrs.toFixed(2);
            document.getElementById('out-hbt-minutes').textContent = diffMins;
        """
    },
    {
        "name": "Time Duration Calculator",
        "slug": "time-duration-calculator",
        "category": "Date & Time",
        "icon": "🕒",
        "desc": "Add or subtract custom periods of days, hours, and minutes.",
        "formula": "Total Seconds = Days*86400 + Hours*3600 + Minutes*60",
        "formula_desc": "Combines time variables into standard SI time seconds units.",
        "inputs": [
            {"id": "td-days", "label": "Days", "type": "number", "default": "2", "min": "0", "max": "1000", "step": "1"},
            {"id": "td-hours", "label": "Hours", "type": "number", "default": "14", "min": "0", "max": "23", "step": "1"},
            {"id": "td-mins", "label": "Minutes", "type": "number", "default": "30", "min": "0", "max": "59", "step": "1"}
        ],
        "outputs": [
            {"id": "out-td-hours", "label": "Total Cumulative Hours", "prefix": "", "suffix": " hours"},
            {"id": "out-td-mins", "label": "Total Cumulative Minutes", "prefix": "", "suffix": " minutes"}
        ],
        "calc_js": """
            const d = parseFloat(document.getElementById('td-days').value) || 0;
            const h = parseFloat(document.getElementById('td-hours').value) || 0;
            const m = parseFloat(document.getElementById('td-mins').value) || 0;

            if (d < 0 || h < 0 || m < 0) {
                showToast("Values must be positive.", "error");
                return;
            }

            const totalHours = (d * 24) + h + (m / 60);
            const totalMins = (d * 24 * 60) + (h * 60) + m;

            document.getElementById('out-td-hours').textContent = totalHours.toFixed(2);
            document.getElementById('out-td-mins').textContent = totalMins;
        """
    },
    {
        "name": "Countdown Calculator",
        "slug": "countdown-calculator",
        "category": "Date & Time",
        "icon": "🕒",
        "desc": "Calculate time remaining (days, hours, minutes) until a target future event.",
        "formula": "Time Remaining = Target Future Date - Current Date",
        "formula_desc": "Resolves millisecond intervals from the active clock to future milestones.",
        "inputs": [
            {"id": "cnt-target", "label": "Future Event Target Date", "type": "date", "default": ""}
        ],
        "outputs": [
            {"id": "out-cnt-days", "label": "Days Remaining", "prefix": "", "suffix": " days"},
            {"id": "out-cnt-hours", "label": "Total Hours Remaining", "prefix": "", "suffix": " hours"}
        ],
        "calc_js": """
            const targetStr = document.getElementById('cnt-target').value;
            if (!targetStr) {
                showToast("Please choose target future date.", "error");
                return;
            }

            const target = new Date(targetStr);
            const today = new Date();

            if (target <= today) {
                showToast("Target date must be in the future.", "error");
                return;
            }

            const diffTime = target - today;
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
            const diffHours = Math.ceil(diffTime / (1000 * 60 * 60));

            document.getElementById('out-cnt-days').textContent = diffDays.toLocaleString();
            document.getElementById('out-cnt-hours').textContent = diffHours.toLocaleString();
        """
    },
    {
        "name": "Leap Year Calculator",
        "slug": "leap-year-calculator",
        "category": "Date & Time",
        "icon": "🕒",
        "desc": "Check if a calendar year is a leap year containing 366 days.",
        "formula": "Leap Year = (Year % 4 == 0) && (Year % 100 != 0 || Year % 400 == 0)",
        "formula_desc": "Applies standard leap year alignment rules.",
        "inputs": [
            {"id": "ly-year", "label": "Calendar Year", "type": "number", "default": "2028", "min": "1", "max": "9999", "step": "1"}
        ],
        "outputs": [
            {"id": "out-ly-status", "label": "Is Leap Year?", "prefix": "", "suffix": ""},
            {"id": "out-ly-days", "label": "Total Days in Year", "prefix": "", "suffix": " days"}
        ],
        "calc_js": """
            const y = parseFloat(document.getElementById('ly-year').value);

            if (isNaN(y) || y < 1) {
                showToast("Please enter a valid year.", "error");
                return;
            }

            const isLeap = (y % 4 === 0 && y % 100 !== 0) || (y % 400 === 0);
            
            document.getElementById('out-ly-status').textContent = isLeap ? "Yes, Leap Year" : "No, Standard Year";
            document.getElementById('out-ly-days').textContent = isLeap ? "366" : "365";
        """
    },
    {
        "name": "Week Number Calculator",
        "slug": "week-number-calculator",
        "category": "Date & Time",
        "icon": "🕒",
        "desc": "Find the ISO-8601 week number for any selected date.",
        "formula": "ISO Week Number calculation",
        "formula_desc": "Identifies week indexes by mapping date structures to calendar week arrays.",
        "inputs": [
            {"id": "wk-date", "label": "Select Date", "type": "date", "default": ""}
        ],
        "outputs": [
            {"id": "out-wk-num", "label": "Week Number (ISO)", "prefix": "Week ", "suffix": ""},
            {"id": "out-wk-year", "label": "ISO Year", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const dateStr = document.getElementById('wk-date').value;
            if (!dateStr) {
                showToast("Please select a date.", "error");
                return;
            }

            const d = new Date(dateStr);
            // ISO week date math
            const target = new Date(d.valueOf());
            const dayNr = (d.getDay() + 6) % 7;
            target.setDate(target.getDate() - dayNr + 3);
            const firstThursday = target.valueOf();
            target.setMonth(0, 1);
            if (target.getDay() !== 4) {
                target.setMonth(0, 1 + ((4 - target.getDay()) + 7) % 7);
            }
            const weekNum = 1 + Math.ceil((firstThursday - target) / (7 * 24 * 60 * 60 * 1000));

            document.getElementById('out-wk-num').textContent = weekNum;
            document.getElementById('out-wk-year').textContent = target.getFullYear();
        """
    },
    {
        "name": "Unix Timestamp Calculator",
        "slug": "unix-timestamp-calculator",
        "category": "Date & Time",
        "icon": "🕒",
        "desc": "Convert standard dates to Unix epoch timestamps.",
        "formula": "Unix Timestamp = Seconds elapsed since January 1, 1970",
        "formula_desc": "Extracts milliseconds since the Unix epoch and divides by 1000.",
        "inputs": [
            {"id": "ut-date", "label": "Select Date & Time", "type": "date", "default": ""}
        ],
        "outputs": [
            {"id": "out-ut-sec", "label": "Unix Timestamp", "prefix": "", "suffix": " seconds"},
            {"id": "out-ut-ms", "label": "Milliseconds epoch", "prefix": "", "suffix": " ms"}
        ],
        "calc_js": """
            const dateStr = document.getElementById('ut-date').value;
            if (!dateStr) {
                showToast("Please select a date.", "error");
                return;
            }

            const d = new Date(dateStr);
            const ms = d.getTime();
            const sec = Math.floor(ms / 1000);

            document.getElementById('out-ut-sec').textContent = sec;
            document.getElementById('out-ut-ms').textContent = ms;
        """
    }
]

SEO_CALCS = [
    {
        "name": "Advertising ROI Calculator",
        "slug": "advertising-roi-calculator",
        "category": "SEO & Marketing",
        "icon": "🌐",
        "desc": "Calculate Return on Ad Spend (ROAS) and ROI for digital marketing campaigns.",
        "formula": "Ad ROI (%) = ((Campaign Revenue - Ad Spend) / Ad Spend) * 100",
        "formula_desc": "Divides net returns by budget spend to evaluate digital advertising efficiency.",
        "inputs": [
            {"id": "aroi-rev", "label": "Revenue Generated ($)", "type": "number", "default": "4500", "min": "0", "max": "100000000", "step": "100"},
            {"id": "aroi-spend", "label": "Total Ad Spend ($)", "type": "number", "default": "1500", "min": "1", "max": "100000000", "step": "100"}
        ],
        "outputs": [
            {"id": "out-aroi-pct", "label": "Advertising ROI", "prefix": "", "suffix": "%"},
            {"id": "out-aroi-roas", "label": "ROAS (Revenue/Spend)", "prefix": "", "suffix": "x"}
        ],
        "calc_js": """
            const rev = parseFloat(document.getElementById('aroi-rev').value) || 0;
            const spend = parseFloat(document.getElementById('aroi-spend').value);

            if (isNaN(spend) || spend <= 0) {
                showToast("Please enter positive ad spend.", "error");
                return;
            }

            const roi = ((rev - spend) / spend) * 100;
            const roas = rev / spend;

            document.getElementById('out-aroi-pct').textContent = roi.toFixed(2);
            document.getElementById('out-aroi-roas').textContent = roas.toFixed(2);
        """
    },
    {
        "name": "CPC Calculator",
        "slug": "cpc-calculator",
        "category": "SEO & Marketing",
        "icon": "🌐",
        "desc": "Calculate Cost Per Click (CPC) for pay-per-click marketing campaigns.",
        "formula": "CPC = Total Ad Cost / Total Clicks",
        "formula_desc": "Divides campaign budget costs by click logs to determine click expenses.",
        "inputs": [
            {"id": "cpc-cost", "label": "Total Campaign Cost ($)", "type": "number", "default": "800", "min": "1", "max": "10000000", "step": "10"},
            {"id": "cpc-clicks", "label": "Total Clicks Received", "type": "number", "default": "500", "min": "1", "max": "100000000", "step": "10"}
        ],
        "outputs": [
            {"id": "out-cpc-val", "label": "Cost Per Click (CPC)", "prefix": "$", "suffix": " /click"}
        ],
        "calc_js": """
            const cost = parseFloat(document.getElementById('cpc-cost').value);
            const clicks = parseFloat(document.getElementById('cpc-clicks').value);

            if (isNaN(cost) || isNaN(clicks) || cost <= 0 || clicks <= 0) {
                showToast("Please check cost and click inputs.", "error");
                return;
            }

            const cpc = cost / clicks;
            document.getElementById('out-cpc-val').textContent = cpc.toFixed(2);
        """
    },
    {
        "name": "CPM Calculator",
        "slug": "cpm-calculator",
        "category": "SEO & Marketing",
        "icon": "🌐",
        "desc": "Calculate Cost Per Mille (CPM) - the advertising cost per 1,000 impressions.",
        "formula": "CPM = (Total Cost / Total Impressions) * 1000",
        "formula_desc": "Determines ad pricing per thousand views.",
        "inputs": [
            {"id": "cpm-cost", "label": "Total Campaign Cost ($)", "type": "number", "default": "1200", "min": "1", "max": "10000000", "step": "10"},
            {"id": "cpm-imp", "label": "Total Impressions", "type": "number", "default": "250000", "min": "1", "max": "1000000000", "step": "100"}
        ],
        "outputs": [
            {"id": "out-cpm-val", "label": "Cost Per Mille (CPM)", "prefix": "$", "suffix": " /1k views"}
        ],
        "calc_js": """
            const cost = parseFloat(document.getElementById('cpm-cost').value);
            const imp = parseFloat(document.getElementById('cpm-imp').value);

            if (isNaN(cost) || isNaN(imp) || cost <= 0 || imp <= 0) {
                showToast("Please check CPM inputs.", "error");
                return;
            }

            const cpm = (cost / imp) * 1000;
            document.getElementById('out-cpm-val').textContent = cpm.toFixed(2);
        """
    },
    {
        "name": "CTR Calculator",
        "slug": "ctr-calculator",
        "category": "SEO & Marketing",
        "icon": "🌐",
        "desc": "Calculate Click-Through Rate (CTR) for links, emails, and ads.",
        "formula": "CTR (%) = (Total Clicks / Total Impressions) * 100",
        "formula_desc": "Solves for relative interaction rates of campaign impressions.",
        "inputs": [
            {"id": "ctr-clicks", "label": "Total Clicks", "type": "number", "default": "150", "min": "0", "max": "100000000", "step": "10"},
            {"id": "ctr-imp", "label": "Total Impressions / Views", "type": "number", "default": "5000", "min": "1", "max": "1000000000", "step": "100"}
        ],
        "outputs": [
            {"id": "out-ctr-pct", "label": "Click-Through Rate (CTR)", "prefix": "", "suffix": "%"}
        ],
        "calc_js": """
            const clicks = parseFloat(document.getElementById('ctr-clicks').value) || 0;
            const imp = parseFloat(document.getElementById('ctr-imp').value);

            if (isNaN(imp) || imp <= 0 || clicks > imp) {
                showToast("Impressions must be greater than clicks.", "error");
                return;
            }

            const ctr = (clicks / imp) * 100;
            document.getElementById('out-ctr-pct').textContent = ctr.toFixed(2);
        """
    },
    {
        "name": "Conversion Rate Calculator",
        "slug": "conversion-rate-calculator",
        "category": "SEO & Marketing",
        "icon": "🌐",
        "desc": "Calculate the conversion rate for sign-ups, sales, or lead generation campaigns.",
        "formula": "Conversion Rate (%) = (Conversions / Total Visitors) * 100",
        "formula_desc": "Calculates visitor-to-customer conversion percentages.",
        "inputs": [
            {"id": "cr-conv", "label": "Conversions Achieved", "type": "number", "default": "45", "min": "0", "max": "10000000", "step": "1"},
            {"id": "cr-vis", "label": "Total Web Visitors", "type": "number", "default": "1500", "min": "1", "max": "1000000000", "step": "10"}
        ],
        "outputs": [
            {"id": "out-cr-pct", "label": "Conversion Rate", "prefix": "", "suffix": "%"}
        ],
        "calc_js": """
            const conv = parseFloat(document.getElementById('cr-conv').value) || 0;
            const vis = parseFloat(document.getElementById('cr-vis').value);

            if (isNaN(vis) || vis <= 0 || conv > vis) {
                showToast("Total visitors must exceed conversions.", "error");
                return;
            }

            const cr = (conv / vis) * 100;
            document.getElementById('out-cr-pct').textContent = cr.toFixed(2);
        """
    },
    {
        "name": "Email Open Rate Calculator",
        "slug": "email-open-rate-calculator",
        "category": "SEO & Marketing",
        "icon": "🌐",
        "desc": "Calculate the open rate of your email marketing campaigns.",
        "formula": "Open Rate (%) = (Emails Opened / Emails Delivered) * 100",
        "formula_desc": "Solves for recipient interaction rates of delivered email envelopes.",
        "inputs": [
            {"id": "eor-open", "label": "Opened Emails", "type": "number", "default": "250", "min": "0", "max": "10000000", "step": "10"},
            {"id": "eor-deliv", "label": "Delivered Emails", "type": "number", "default": "1000", "min": "1", "max": "100000000", "step": "10"}
        ],
        "outputs": [
            {"id": "out-eor-pct", "label": "Email Open Rate", "prefix": "", "suffix": "%"}
        ],
        "calc_js": """
            const open = parseFloat(document.getElementById('eor-open').value) || 0;
            const deliv = parseFloat(document.getElementById('eor-deliv').value);

            if (isNaN(deliv) || deliv <= 0 || open > deliv) {
                showToast("Delivered emails must exceed opened emails.", "error");
                return;
            }

            const rate = (open / deliv) * 100;
            document.getElementById('out-eor-pct').textContent = rate.toFixed(2);
        """
    },
    {
        "name": "Social Media Engagement Calculator",
        "slug": "social-media-engagement-calculator",
        "category": "SEO & Marketing",
        "icon": "🌐",
        "desc": "Calculate your engagement rate based on likes, comments, shares, and followers.",
        "formula": "Engagement Rate (%) = ((Likes + Comments + Shares) / Followers) * 100",
        "formula_desc": "Aggregates social interactions against total profile audience sizes.",
        "inputs": [
            {"id": "sme-inter", "label": "Interactions (Likes + Comments + Shares)", "type": "number", "default": "450", "min": "0", "max": "100000000", "step": "10"},
            {"id": "sme-fol", "label": "Total Followers", "type": "number", "default": "10000", "min": "1", "max": "1000000000", "step": "100"}
        ],
        "outputs": [
            {"id": "out-sme-rate", "label": "Engagement Rate", "prefix": "", "suffix": "%"}
        ],
        "calc_js": """
            const inter = parseFloat(document.getElementById('sme-inter').value) || 0;
            const fol = parseFloat(document.getElementById('sme-fol').value);

            if (isNaN(fol) || fol <= 0) {
                showToast("Followers must exceed zero.", "error");
                return;
            }

            const rate = (inter / fol) * 100;
            document.getElementById('out-sme-rate').textContent = rate.toFixed(2);
        """
    },
    {
        "name": "Affiliate Earnings Calculator",
        "slug": "affiliate-earnings-calculator",
        "category": "SEO & Marketing",
        "icon": "🌐",
        "desc": "Estimate affiliate marketing revenue based on referral traffic and commission rates.",
        "formula": "Earnings = Traffic * (Conversion Rate / 100) * Avg Order Value * (Commission / 100)",
        "formula_desc": "Multiplies referral traffic by conversion rates and commission splits to project commissions.",
        "inputs": [
            {"id": "aff-clicks", "label": "Referral Clicks / Traffic", "type": "number", "default": "5000", "min": "1", "max": "100000000", "step": "100"},
            {"id": "aff-cr", "label": "Conversion Rate (%)", "type": "number", "default": "2.0", "min": "0.1", "max": "50", "step": "0.1"},
            {"id": "aff-aov", "label": "Average Order Value (AOV) ($)", "type": "number", "default": "75.00", "min": "1", "max": "5000", "step": "5"},
            {"id": "aff-comm", "label": "Commission Rate (%)", "type": "number", "default": "8", "min": "0.1", "max": "90", "step": "0.5"}
        ],
        "outputs": [
            {"id": "out-aff-earnings", "label": "Estimated Commissions", "prefix": "$", "suffix": ""},
            {"id": "out-aff-sales", "label": "Total Sales Volume", "prefix": "", "suffix": " sales"}
        ],
        "calc_js": """
            const clicks = parseFloat(document.getElementById('aff-clicks').value);
            const cr = parseFloat(document.getElementById('aff-cr').value);
            const aov = parseFloat(document.getElementById('aff-aov').value);
            const comm = parseFloat(document.getElementById('aff-comm').value);

            if (isNaN(clicks) || isNaN(cr) || isNaN(aov) || isNaN(comm) || clicks <= 0 || cr <= 0 || aov <= 0 || comm <= 0) {
                showToast("Please check numeric fields.", "error");
                return;
            }

            const sales = clicks * (cr / 100);
            const earnings = sales * aov * (comm / 100);

            document.getElementById('out-aff-earnings').textContent = earnings.toFixed(2);
            document.getElementById('out-aff-sales').textContent = Math.round(sales);
        """
    },
    {
        "name": "Influencer Rate Calculator",
        "slug": "influencer-rate-calculator",
        "category": "SEO & Marketing",
        "icon": "🌐",
        "desc": "Estimate earnings per sponsored post based on follower size and engagement rates.",
        "formula": "Estimated rate = Follower multiplier * Engagement multiplier",
        "formula_desc": "Calculates post prices using follower sizes scaled by audience engagement rates.",
        "inputs": [
            {"id": "inf-fol", "label": "Social Followers Count", "type": "number", "default": "25000", "min": "100", "max": "100000000", "step": "500"},
            {"id": "inf-er", "label": "Engagement Rate (%)", "type": "number", "default": "3.5", "min": "0.1", "max": "50", "step": "0.1"}
        ],
        "outputs": [
            {"id": "out-inf-low", "label": "Estimated Lower Range Price", "prefix": "$", "suffix": ""},
            {"id": "out-inf-high", "label": "Estimated Upper Range Price", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const fol = parseFloat(document.getElementById('inf-fol').value);
            const er = parseFloat(document.getElementById('inf-er').value);

            if (isNaN(fol) || isNaN(er) || fol <= 0 || er <= 0) {
                showToast("Please check influencer inputs.", "error");
                return;
            }

            // Estimate base rate: $10 per 1,000 followers, scaled by ER ratio (average ER assumed to be 2.5%)
            const baseRate = (fol / 1000) * 10;
            const erScale = er / 2.5;
            
            const estRate = baseRate * erScale;
            const low = estRate * 0.8;
            const high = estRate * 1.2;

            document.getElementById('out-inf-low').textContent = Math.round(low);
            document.getElementById('out-inf-high').textContent = Math.round(high);
        """
    },
    {
        "name": "Keyword Density Calculator",
        "slug": "keyword-density-calculator",
        "category": "SEO & Marketing",
        "icon": "🌐",
        "desc": "Find the keyword density of a specific target keyword within your article content.",
        "formula": "Density (%) = (Keyword Occurrence / Total Words Count) * 100",
        "formula_desc": "Solves keyword iteration rates inside articles.",
        "inputs": [
            {"id": "kd-text", "label": "Enter Content / Article Text", "type": "text", "default": "Learn SEO tips and how to search keywords. Keyword research is crucial for ranking online."},
            {"id": "kd-key", "label": "Target Keyword", "type": "text", "default": "keyword"}
        ],
        "outputs": [
            {"id": "out-kd-pct", "label": "Keyword Density", "prefix": "", "suffix": "%"},
            {"id": "out-kd-count", "label": "Keyword Occurrences", "prefix": "", "suffix": " times"},
            {"id": "out-kd-words", "label": "Total Words audited", "prefix": "", "suffix": " words"}
        ],
        "calc_js": """
            const text = document.getElementById('kd-text').value.trim();
            const key = document.getElementById('kd-key').value.trim().toLowerCase();

            if (!text || !key) {
                showToast("Please check text and keyword inputs.", "error");
                return;
            }

            const words = text.split(/\\s+/);
            const totalWords = words.length;

            // Simple occurrence check (matches keyword substring cases)
            const cleanText = text.toLowerCase();
            let count = 0;
            let pos = cleanText.indexOf(key);
            while (pos !== -1) {
                count++;
                pos = cleanText.indexOf(key, pos + key.length);
            }

            const pct = (count / totalWords) * 100;

            document.getElementById('out-kd-pct').textContent = pct.toFixed(2);
            document.getElementById('out-kd-count').textContent = count;
            document.getElementById('out-kd-words').textContent = totalWords;
        """
    }
]

LIFE_CALCS = [
    {
        "name": "Love Calculator",
        "slug": "love-calculator",
        "category": "Lifestyle",
        "icon": "💖",
        "desc": "Estimate romantic compatibility percentages between two partner names.",
        "formula": "Love % = Characters hash calculations (For fun purpose)",
        "formula_desc": "Combines string character hashes to generate stable fun compatibility percentages.",
        "inputs": [
            {"id": "lv-name1", "label": "Your Name", "type": "text", "default": "John Doe"},
            {"id": "lv-name2", "label": "Partner Name", "type": "text", "default": "Jane Doe"}
        ],
        "outputs": [
            {"id": "out-lv-pct", "label": "Love Compatibility", "prefix": "", "suffix": "%"},
            {"id": "out-lv-status", "label": "Relationship Outlook", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const n1 = document.getElementById('lv-name1').value.trim().toLowerCase();
            const n2 = document.getElementById('lv-name2').value.trim().toLowerCase();

            if (!n1 || !n2) {
                showToast("Please enter both names.", "error");
                return;
            }

            // Simple deterministic algorithm based on characters
            let sum = 0;
            for (let i = 0; i < n1.length; i++) sum += n1.charCodeAt(i);
            for (let i = 0; i < n2.length; i++) sum += n2.charCodeAt(i);

            const pct = (sum % 51) + 50; // Generate stable number between 50 and 100

            let outlook = "Good Match";
            if (pct > 85) outlook = "Perfect Match! Soulmates";
            else if (pct < 65) outlook = "Needs Mutual effort";

            document.getElementById('out-lv-pct').textContent = pct;
            document.getElementById('out-lv-status').textContent = outlook;
        """
    },
    {
        "name": "Compatibility Calculator",
        "slug": "compatibility-calculator",
        "category": "Lifestyle",
        "icon": "💖",
        "desc": "Calculate astrological compatibility percentages based on zodiac signs.",
        "formula": "Astrological Element alignments (For fun)",
        "formula_desc": "Matches zodiac signs based on elements (Fire, Earth, Air, Water) to score relative compatibility.",
        "inputs": [
            {"id": "cmp-z1", "label": "Your Zodiac Sign", "type": "select", "options": [
                ("aries", "Aries"), ("taurus", "Taurus"), ("gemini", "Gemini"), ("cancer", "Cancer"), ("leo", "Leo"), ("virgo", "Virgo"),
                ("libra", "Libra"), ("scorpio", "Scorpio"), ("sagittarius", "Sagittarius"), ("capricorn", "Capricorn"), ("aquarius", "Aquarius"), ("pisces", "Pisces")
            ]},
            {"id": "cmp-z2", "label": "Partner Zodiac Sign", "type": "select", "options": [
                ("leo", "Leo"), ("aries", "Aries"), ("taurus", "Taurus"), ("gemini", "Gemini"), ("cancer", "Cancer"), ("virgo", "Virgo"),
                ("libra", "Libra"), ("scorpio", "Scorpio"), ("sagittarius", "Sagittarius"), ("capricorn", "Capricorn"), ("aquarius", "Aquarius"), ("pisces", "Pisces")
            ]}
        ],
        "outputs": [
            {"id": "out-cmp-pct", "label": "Zodiac Compatibility", "prefix": "", "suffix": "%"},
            {"id": "out-cmp-text", "label": "Core Element Match", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const z1 = document.getElementById('cmp-z1').value;
            const z2 = document.getElementById('cmp-z2').value;

            // Element mapping: fire, earth, air, water
            const elements = {
                aries: "fire", leo: "fire", sagittarius: "fire",
                taurus: "earth", virgo: "earth", capricorn: "earth",
                gemini: "air", libra: "air", aquarius: "air",
                cancer: "water", scorpio: "water", pisces: "water"
            };

            const e1 = elements[z1];
            const e2 = elements[z2];

            let pct = 70; // baseline
            let matchText = "Harmonious elements";

            if (e1 === e2) {
                pct = 90;
                matchText = "Same element (" + e1.toUpperCase() + ") - High Synergy!";
            } else if ((e1 === "fire" && e2 === "air") || (e1 === "air" && e2 === "fire")) {
                pct = 85;
                matchText = "Fire & Air (Exerting & Inspiring)";
            } else if ((e1 === "earth" && e2 === "water") || (e1 === "water" && e2 === "earth")) {
                pct = 85;
                matchText = "Earth & Water (Nourishing & Productive)";
            } else {
                pct = 55;
                matchText = "Contradicting elements - Needs compromise";
            }

            document.getElementById('out-cmp-pct').textContent = pct;
            document.getElementById('out-cmp-text').textContent = matchText;
        """
    },
    {
        "name": "Birthday Calculator",
        "slug": "birthday-calculator",
        "category": "Lifestyle",
        "icon": "🎂",
        "desc": "Calculate days remaining until your next birthday and check your astrological profiles.",
        "formula": "Days = Next Birthday Date - Today",
        "formula_desc": "Tracks day intervals from the active date to the next occurrence of your birthdate.",
        "inputs": [
            {"id": "bdc-date", "label": "Select Birthday Date", "type": "date", "default": ""}
        ],
        "outputs": [
            {"id": "out-bdc-days", "label": "Days until next birthday", "prefix": "", "suffix": " days"},
            {"id": "out-bdc-sign", "label": "Astrological Sign", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const birthStr = document.getElementById('bdc-date').value;
            if (!birthStr) {
                showToast("Please select a date.", "error");
                return;
            }

            const birth = new Date(birthStr);
            const today = new Date();
            
            // Calculate next birthday date
            const nextBD = new Date(today.getFullYear(), birth.getMonth(), birth.getDate());
            if (nextBD < today) {
                nextBD.setFullYear(today.getFullYear() + 1);
            }

            const diffTime = nextBD - today;
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

            // Determine zodiac
            const m = birth.getMonth() + 1;
            const d = birth.getDate();
            let sign = "";
            if ((m === 3 && d >= 21) || (m === 4 && d <= 19)) sign = "Aries";
            else if ((m === 4 && d >= 20) || (m === 5 && d <= 20)) sign = "Taurus";
            else if ((m === 5 && d >= 21) || (m === 6 && d <= 20)) sign = "Gemini";
            else if ((m === 6 && d >= 21) || (m === 7 && d <= 22)) sign = "Cancer";
            else if ((m === 7 && d >= 23) || (m === 8 && d <= 22)) sign = "Leo";
            else if ((m === 8 && d >= 23) || (m === 9 && d <= 22)) sign = "Virgo";
            else if ((m === 9 && d >= 23) || (m === 10 && d <= 22)) sign = "Libra";
            else if ((m === 10 && d >= 23) || (m === 11 && d <= 21)) sign = "Scorpio";
            else if ((m === 11 && d >= 22) || (m === 12 && d <= 21)) sign = "Sagittarius";
            else if ((m === 12 && d >= 22) || (m === 1 && d <= 19)) sign = "Capricorn";
            else if ((m === 1 && d >= 20) || (m === 2 && d <= 18)) sign = "Aquarius";
            else sign = "Pisces";

            document.getElementById('out-bdc-days').textContent = diffDays;
            document.getElementById('out-bdc-sign').textContent = sign;
        """
    },
    {
        "name": "Pet Age Calculator",
        "slug": "pet-age-calculator",
        "category": "Lifestyle",
        "icon": "🐾",
        "desc": "Convert standard dog and cat ages to equivalent human years.",
        "formula": "1st year = 15 human years, 2nd year = 9, subsequent years = 4 (Dog/Cat)",
        "formula_desc": "Applies standard veterinary metabolic aging metrics for domestic pets.",
        "inputs": [
            {"id": "pa-type", "label": "Pet Type", "type": "select", "options": [("dog", "Dog"), ("cat", "Cat")]},
            {"id": "pa-age", "label": "Pet Age (Calendar Years)", "type": "number", "default": "4", "min": "1", "max": "25", "step": "1"}
        ],
        "outputs": [
            {"id": "out-pa-human", "label": "Equivalent Human Age", "prefix": "", "suffix": " years old"}
        ],
        "calc_js": """
            const type = document.getElementById('pa-type').value;
            const age = parseFloat(document.getElementById('pa-age').value);

            if (isNaN(age) || age < 1) {
                showToast("Pet age must be at least 1 year.", "error");
                return;
            }

            let human = 0;
            if (age === 1) {
                human = 15;
            } else if (age === 2) {
                human = 24;
            } else {
                human = 24 + (age - 2) * 4;
            }

            document.getElementById('out-pa-human').textContent = human;
        """
    },
    {
        "name": "Zodiac Calculator",
        "slug": "zodiac-calculator",
        "category": "Lifestyle",
        "icon": "✨",
        "desc": "Calculate your zodiac sign and elemental alignment based on birthdate.",
        "formula": "Zodiac sign determined by solar calendar date range boundaries",
        "formula_desc": "Maps birthdate month and day against traditional astrological intervals.",
        "inputs": [
            {"id": "zd-birth", "label": "Choose Date of Birth", "type": "date", "default": ""}
        ],
        "outputs": [
            {"id": "out-zd-sign", "label": "Zodiac Sign", "prefix": "", "suffix": ""},
            {"id": "out-zd-elem", "label": "Element Assignment", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const dateStr = document.getElementById('zd-birth').value;
            if (!dateStr) {
                showToast("Please choose your date.", "error");
                return;
            }

            const birth = new Date(dateStr);
            const m = birth.getMonth() + 1;
            const d = birth.getDate();

            let sign = "";
            let elem = "";

            if ((m === 3 && d >= 21) || (m === 4 && d <= 19)) { sign = "Aries"; elem = "Fire"; }
            else if ((m === 4 && d >= 20) || (m === 5 && d <= 20)) { sign = "Taurus"; elem = "Earth"; }
            else if ((m === 5 && d >= 21) || (m === 6 && d <= 20)) { sign = "Gemini"; elem = "Air"; }
            else if ((m === 6 && d >= 21) || (m === 7 && d <= 22)) { sign = "Cancer"; elem = "Water"; }
            else if ((m === 7 && d >= 23) || (m === 8 && d <= 22)) { sign = "Leo"; elem = "Fire"; }
            else if ((m === 8 && d >= 23) || (m === 9 && d <= 22)) { sign = "Virgo"; elem = "Earth"; }
            else if ((m === 9 && d >= 23) || (m === 10 && d <= 22)) { sign = "Libra"; elem = "Air"; }
            else if ((m === 10 && d >= 23) || (m === 11 && d <= 21)) { sign = "Scorpio"; elem = "Water"; }
            else if ((m === 11 && d >= 22) || (m === 12 && d <= 21)) { sign = "Sagittarius"; elem = "Fire"; }
            else if ((m === 12 && d >= 22) || (m === 1 && d <= 19)) { sign = "Capricorn"; elem = "Earth"; }
            else if ((m === 1 && d >= 20) || (m === 2 && d <= 18)) { sign = "Aquarius"; elem = "Air"; }
            else { sign = "Pisces"; elem = "Water"; }

            document.getElementById('out-zd-sign').textContent = sign;
            document.getElementById('out-zd-elem').textContent = elem;
        """
    },
    {
        "name": "Life Path Number Calculator",
        "slug": "life-path-number-calculator",
        "category": "Lifestyle",
        "icon": "✨",
        "desc": "Calculate your numerology Life Path Number based on your birthdate.",
        "formula": "Life Path Number = Sum of birth digits reduced to single digit or master numbers (11, 22, 33)",
        "formula_desc": "Combines month, day, and year integers, reducing them to numerology units.",
        "inputs": [
            {"id": "lpn-birth", "label": "Choose Date of Birth", "type": "date", "default": ""}
        ],
        "outputs": [
            {"id": "out-lpn-val", "label": "Life Path Number", "prefix": "", "suffix": ""},
            {"id": "out-lpn-trait", "label": "Core Numerology Trait", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const dateStr = document.getElementById('lpn-birth').value;
            if (!dateStr) {
                showToast("Please choose your date.", "error");
                return;
            }

            const parts = dateStr.split('-');
            const yearStr = parts[0];
            const monthStr = parts[1];
            const dayStr = parts[2];

            const reduce = (numStr) => {
                let sum = numStr.split('').map(Number).reduce((a,b)=>a+b, 0);
                if (sum > 9 && sum !== 11 && sum !== 22 && sum !== 33) {
                    return reduce(sum.toString());
                }
                return sum;
            };

            const rY = reduce(yearStr);
            const rM = reduce(monthStr);
            const rD = reduce(dayStr);

            let finalSum = rY + rM + rD;
            while (finalSum > 9 && finalSum !== 11 && finalSum !== 22 && finalSum !== 33) {
                finalSum = finalSum.toString().split('').map(Number).reduce((a,b)=>a+b, 0);
            }

            const traits = {
                1: "The Leader (Independence, original thinker)",
                2: "The Peacekeeper (Diplomatic, intuitive)",
                3: "The Creator (Creative expression, social)",
                4: "The Builder (Practical, organized)",
                5: "The Explorer (Freedom lover, traveler)",
                6: "The Nurturer (Responsible, caring)",
                7: "The Seeker (Analytical, spiritual)",
                8: "The Achiever (Ambitious, material builder)",
                9: "The Humanitarian (Compassionate, artistic)",
                11: "The Intuitive Messenger (Master Number - Spiritual insight)",
                22: "The Master Builder (Master Number - High manifestation)",
                33: "The Master Teacher (Master Number - Universal devotion)"
            };

            document.getElementById('out-lpn-val').textContent = finalSum;
            document.getElementById('out-lpn-trait').textContent = traits[finalSum] || "Balanced path";
        """
    },
    {
        "name": "Daily Water Calculator",
        "slug": "daily-water-calculator",
        "category": "Lifestyle",
        "icon": "💧",
        "desc": "Calculate standard daily baseline drinking water requirements based on body weight.",
        "formula": "Daily Water Target = Weight (kg) * 35 ml",
        "formula_desc": "Multiplies body mass index variables to estimate standard personal daily fluid needs.",
        "inputs": [
            {"id": "dw-weight", "label": "Body Weight (kg)", "type": "number", "default": "70", "min": "20", "max": "250", "step": "1"}
        ],
        "outputs": [
            {"id": "out-dw-liters", "label": "Target (Liters)", "prefix": "", "suffix": " L"},
            {"id": "out-dw-glasses", "label": "Target (Glasses - 250ml each)", "prefix": "", "suffix": " glasses"}
        ],
        "calc_js": """
            const w = parseFloat(document.getElementById('dw-weight').value);

            if (isNaN(w) || w <= 0) {
                showToast("Please check weight input.", "error");
                return;
            }

            const liters = (w * 35) / 1000;
            const glasses = (w * 35) / 250;

            document.getElementById('out-dw-liters').textContent = liters.toFixed(2);
            document.getElementById('out-dw-glasses').textContent = glasses.toFixed(1);
        """
    },
    {
        "name": "Screen Time Calculator",
        "slug": "screen-time-calculator",
        "category": "Lifestyle",
        "icon": "📱",
        "desc": "Calculate how much of your life is spent looking at screens (phones, computers, TV).",
        "formula": "Waking Life Screen Time % = (Daily Screen Hours / 16 Waking Hours) * 100",
        "formula_desc": "Compares daily digital screen usage against standard 16-hour waking days.",
        "inputs": [
            {"id": "scr-hours", "label": "Daily Screen Usage (Hours)", "type": "number", "default": "6", "min": "0.1", "max": "24", "step": "0.5"}
        ],
        "outputs": [
            {"id": "out-scr-waking", "label": "Percentage of Waking Life", "prefix": "", "suffix": "%"},
            {"id": "out-scr-year", "label": "Total Days per Year", "prefix": "", "suffix": " days"}
        ],
        "calc_js": """
            const hrs = parseFloat(document.getElementById('scr-hours').value);

            if (isNaN(hrs) || hrs <= 0 || hrs > 24) {
                showToast("Hours must be between 0 and 24.", "error");
                return;
            }

            const wakingPct = (hrs / 16) * 100;
            const yearDays = (hrs * 365) / 24;

            document.getElementById('out-scr-waking').textContent = wakingPct.toFixed(1);
            document.getElementById('out-scr-year').textContent = Math.round(yearDays);

            updateBreakdown(`
                <p>Spending ${hrs} hours daily is equivalent to spent <strong>${Math.round(yearDays)} full days</strong> in screen time per year.</p>
            `);
        """
    },
    {
        "name": "Carbon Footprint Calculator",
        "slug": "carbon-footprint-calculator",
        "category": "Lifestyle",
        "icon": "🍃",
        "desc": "Estimate your average carbon emissions based on home utilities and driving habits.",
        "formula": "Carbon (kg CO2e) = Electricity (kWh) * 0.4 + Gas (therms) * 5.3 + Driving (km) * 0.2",
        "formula_desc": "Applies standard greenhouse gas emission factors to electricity, heating, and vehicle usage values.",
        "inputs": [
            {"id": "cfp-elec", "label": "Monthly Electricity Bill (kWh)", "type": "number", "default": "300", "min": "0", "max": "5000", "step": "10"},
            {"id": "cfp-gas", "label": "Monthly Natural Gas (Therms)", "type": "number", "default": "25", "min": "0", "max": "500", "step": "5"},
            {"id": "cfp-drive", "label": "Monthly Vehicle Mileage (km)", "type": "number", "default": "1000", "min": "0", "max": "20000", "step": "100"}
        ],
        "outputs": [
            {"id": "out-cfp-co2", "label": "Estimated Monthly Carbon Emissions", "prefix": "", "suffix": " kg CO₂"},
            {"id": "out-cfp-annual", "label": "Estimated Annual Carbon Footprint", "prefix": "", "suffix": " tons CO₂"}
        ],
        "calc_js": """
            const elec = parseFloat(document.getElementById('cfp-elec').value) || 0;
            const gas = parseFloat(document.getElementById('cfp-gas').value) || 0;
            const drive = parseFloat(document.getElementById('cfp-drive').value) || 0;

            // Emission factors: 0.4 kg CO2 per kWh, 5.3 kg per Therm, 0.2 kg per km driving
            const monthlyCo2 = (elec * 0.4) + (gas * 5.3) + (drive * 0.2);
            const annualTons = (monthlyCo2 * 12) / 1000;

            document.getElementById('out-cfp-co2').textContent = Math.round(monthlyCo2).toLocaleString();
            document.getElementById('out-cfp-annual').textContent = annualTons.toFixed(2);
        """
    }
]

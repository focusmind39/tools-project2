# -*- coding: utf-8 -*-
"""
Database of Education Tools, Random Number Tools, & Math Generators (30 tools)
"""

EDUCATION_RANDOM_GEN_TOOLS = [
    {
        "category": "Education Tools",
        "name": "GPA Calculator",
        "slug": "gpa-calculator-math",
        "desc": "Calculate your grade point average (GPA) based on class grades and credit weights.",
        "formula": "GPA = Sum(Grade Points * Credits) / Sum(Credits)",
        "formula_desc": "Multiplies each numerical grade point by course credits, aggregates them, and divides by total credits.",
        "icon": "🎓",
        "inputs": [
            {"id": "gpa-g1", "label": "Course 1 Grade (A=4, B=3, C=2, D=1, F=0):", "type": "number", "default": "4"},
            {"id": "gpa-c1", "label": "Course 1 Credits:", "type": "number", "default": "3"},
            {"id": "gpa-g2", "label": "Course 2 Grade:", "type": "number", "default": "3"},
            {"id": "gpa-c2", "label": "Course 2 Credits:", "type": "number", "default": "4"}
        ],
        "outputs": [
            {"id": "gpa-result", "label": "Calculated GPA:", "type": "text"}
        ],
        "calc_js": """
            const g1 = parseFloat(document.getElementById('gpa-g1').value);
            const c1 = parseFloat(document.getElementById('gpa-c1').value);
            const g2 = parseFloat(document.getElementById('gpa-g2').value);
            const c2 = parseFloat(document.getElementById('gpa-c2').value);

            if ([g1,c1,g2,c2].some(isNaN) || c1 <= 0 || c2 <= 0) {
                showToast("Please enter positive credits and numeric grades.", "error");
                return;
            }

            const totalPoints = (g1 * c1) + (g2 * c2);
            const totalCredits = c1 + c2;
            const gpa = totalPoints / totalCredits;

            document.getElementById('gpa-result').textContent = gpa.toFixed(2);

            let steps = `<p>Course 1 Points: <code>${g1} * ${c1}</code> = ${g1*c1}</p>`;
            steps += `<p>Course 2 Points: <code>${g2} * ${c2}</code> = ${g2*c2}</p>`;
            steps += `<p>Total Credits: <code>${totalCredits}</code></p>`;
            steps += `<p>GPA = <code>${totalPoints} / ${totalCredits}</code> = <strong>${gpa.toFixed(4)}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Education Tools",
        "name": "CGPA Calculator",
        "slug": "cgpa-calculator-math",
        "desc": "Calculate your cumulative grade point average (CGPA) from semester GPAs.",
        "formula": "CGPA = Sum(Semester GPA) / Total Semesters",
        "formula_desc": "Computes the standard average of grade point averages obtained across semesters.",
        "icon": "🎓",
        "inputs": [
            {"id": "cgpa-list", "label": "Semester GPAs (comma-separated):", "type": "text", "default": "8.5, 9.0, 7.8, 8.2"}
        ],
        "outputs": [
            {"id": "cgpa-result", "label": "Calculated CGPA:", "type": "text"}
        ],
        "calc_js": """
            const raw = document.getElementById('cgpa-list').value;
            const arr = raw.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));

            if (!arr.length) {
                showToast("Please enter semester GPAs.", "error");
                return;
            }

            const sum = arr.reduce((acc, curr) => acc + curr, 0);
            const cgpa = sum / arr.length;

            document.getElementById('cgpa-result').textContent = cgpa.toFixed(2);
            updateBreakdown(`<p>Total semester GPAs: <code>${arr.length}</code></p><p>CGPA = <code>(${arr.join(' + ')}) / ${arr.length}</code> = <strong>${cgpa.toFixed(4)}</strong></p>`);
        """
    },
    {
        "category": "Education Tools",
        "name": "Marks Percentage Calculator",
        "slug": "marks-percentage-calculator-math",
        "desc": "Calculate your score percentage from obtained and maximum possible marks.",
        "formula": "Percentage = (Obtained / Max) * 100",
        "formula_desc": "Divides obtained marks by maximum possible marks and scales by 100.",
        "icon": "📝",
        "inputs": [
            {"id": "marks-obt", "label": "Marks Obtained:", "type": "number", "default": "420"},
            {"id": "marks-max", "label": "Maximum Marks:", "type": "number", "default": "500"}
        ],
        "outputs": [
            {"id": "marks-pct", "label": "Percentage Output:", "type": "text"}
        ],
        "calc_js": """
            const obt = parseFloat(document.getElementById('marks-obt').value);
            const max = parseFloat(document.getElementById('marks-max').value);

            if (isNaN(obt) || isNaN(max) || max <= 0 || obt < 0) {
                showToast("Please enter positive marks.", "error");
                return;
            }

            const pct = (obt / max) * 100;
            document.getElementById('marks-pct').textContent = pct.toFixed(2) + "%";

            let steps = `<p>Percentage = <code>(${obt} / ${max}) * 100</code> = <strong>${pct.toFixed(4)}%</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Education Tools",
        "name": "Grade Calculator",
        "slug": "grade-calculator-math",
        "desc": "Estimate the final class grade using homework, exam, and quiz weight percentages.",
        "formula": "Grade = Sum(Score * Weight)",
        "formula_desc": "Multiplies each category score by its syllabus weight percentage and sums the results.",
        "icon": "🎓",
        "inputs": [
            {"id": "grd-s1", "label": "Homework Score (%):", "type": "number", "default": "90"},
            {"id": "grd-w1", "label": "Homework Weight (%):", "type": "number", "default": "30"},
            {"id": "grd-s2", "label": "Exam Score (%):", "type": "number", "default": "80"},
            {"id": "grd-w2", "label": "Exam Weight (%):", "type": "number", "default": "70"}
        ],
        "outputs": [
            {"id": "grd-result", "label": "Weighted Grade:", "type": "text"}
        ],
        "calc_js": """
            const s1 = parseFloat(document.getElementById('grd-s1').value);
            const w1 = parseFloat(document.getElementById('grd-w1').value) / 100;
            const s2 = parseFloat(document.getElementById('grd-s2').value);
            const w2 = parseFloat(document.getElementById('grd-w2').value) / 100;

            if ([s1,w1,s2,w2].some(isNaN) || s1 < 0 || s2 < 0) {
                showToast("Please enter valid positive values.", "error");
                return;
            }

            const total = (s1 * w1) + (s2 * w2);
            document.getElementById('grd-result').textContent = total.toFixed(2) + "%";

            let steps = `<p>Weighted Homework: <code>${s1}% * ${(w1*100)}%</code> = ${(s1*w1).toFixed(2)}%</p>`;
            steps += `<p>Weighted Exam: <code>${s2}% * ${(w2*100)}%</code> = ${(s2*w2).toFixed(2)}%</p>`;
            steps += `<p>Final Class Grade: <strong>${total.toFixed(2)}%</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Education Tools",
        "name": "Attendance Calculator",
        "slug": "attendance-calculator-math",
        "desc": "Calculate attendance percentage or classes needed to hit target percentage.",
        "formula": "Attendance = (Present / Conducted) * 100",
        "formula_desc": "Divides present class count by total conducted classes to yield attendance rate.",
        "icon": "📅",
        "inputs": [
            {"id": "att-pres", "label": "Classes Present:", "type": "number", "default": "45"},
            {"id": "att-tot", "label": "Total Classes Conducted:", "type": "number", "default": "50"},
            {"id": "att-target", "label": "Target Percentage (%, e.g. 75):", "type": "number", "default": "75"}
        ],
        "outputs": [
            {"id": "att-result", "label": "Current Attendance:", "type": "text"},
            {"id": "att-needed", "label": "Status / Classes Needed:", "type": "text"}
        ],
        "calc_js": """
            const present = parseInt(document.getElementById('att-pres').value);
            const conducted = parseInt(document.getElementById('att-tot').value);
            const target = parseFloat(document.getElementById('att-target').value);

            if (isNaN(present) || isNaN(conducted) || isNaN(target) || conducted <= 0 || present < 0 || present > conducted) {
                showToast("Please enter valid conducted and present class values.", "error");
                return;
            }

            const current = (present / conducted) * 100;
            document.getElementById('att-result').textContent = current.toFixed(2) + "%";

            let explanation = "";
            let statusText = "";
            if (current >= target) {
                statusText = "Above Target! You can skip classes.";
                explanation = `<p>Current attendance <strong>${current.toFixed(2)}%</strong> exceeds your target of ${target}%.</p>`;
            } else {
                // Solve for x: (present + x) / (conducted + x) = target / 100
                const targetFactor = target / 100;
                const needed = Math.ceil((targetFactor * conducted - present) / (1 - targetFactor));
                statusText = `Attend ${needed} more classes`;
                explanation = `<p>To hit target of ${target}%, you must attend <strong>${needed}</strong> consecutive classes without skips.</p>`;
            }

            document.getElementById('att-needed').textContent = statusText;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Education Tools",
        "name": "Study Time Calculator",
        "slug": "study-time-calculator-math",
        "desc": "Calculate average study time allocations required to prepare for exams.",
        "formula": "Time = Total Pages / Reading Speed",
        "formula_desc": "Divides curriculum reading workload by individual page reading speed estimates.",
        "icon": "🕒",
        "inputs": [
            {"id": "std-pages", "label": "Syllabus Pages count:", "type": "number", "default": "300"},
            {"id": "std-speed", "label": "Reading Speed (Pages per Hour):", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "std-result", "label": "Hours Needed:", "type": "text"}
        ],
        "calc_js": """
            const pages = parseFloat(document.getElementById('std-pages').value);
            const speed = parseFloat(document.getElementById('std-speed').value);

            if (isNaN(pages) || isNaN(speed) || speed <= 0 || pages < 0) {
                showToast("Reading speed must be positive.", "error");
                return;
            }

            const hours = pages / speed;
            document.getElementById('std-result').textContent = hours.toFixed(1) + " hours";
            updateBreakdown(`<p>Total hours needed to review curriculum: <code>${pages} pages / ${speed} pages/hr</code> = <strong>${hours.toFixed(1)} hours</strong></p>`);
        """
    },
    {
        "category": "Education Tools",
        "name": "Score Calculator",
        "slug": "score-calculator",
        "desc": "Find your test score based on total questions and incorrect answers.",
        "formula": "Score = ((Total - Incorrect) / Total) * 100",
        "formula_desc": "Subtracts wrong answers from total queries and calculates correct percentage representation.",
        "icon": "🎓",
        "inputs": [
            {"id": "sc-tot", "label": "Total Questions:", "type": "number", "default": "60"},
            {"id": "sc-wrong", "label": "Wrong Answers:", "type": "number", "default": "6"}
        ],
        "outputs": [
            {"id": "sc-result", "label": "Test Score:", "type": "text"}
        ],
        "calc_js": """
            const tot = parseInt(document.getElementById('sc-tot').value);
            const wrong = parseInt(document.getElementById('sc-wrong').value);

            if (isNaN(tot) || isNaN(wrong) || tot <= 0 || wrong < 0 || wrong > tot) {
                showToast("Invalid question counts.", "error");
                return;
            }

            const score = ((tot - wrong) / tot) * 100;
            document.getElementById('sc-result').textContent = score.toFixed(2) + "%";
            updateBreakdown(`<p>Correct answers: <code>${tot - wrong}</code> out of ${tot}</p><p>Score percentage: <strong>${score.toFixed(4)}%</strong></p>`);
        """
    },
    {
        "category": "Education Tools",
        "name": "Exam Percentage Calculator",
        "slug": "exam-percentage-calculator",
        "desc": "Calculate the percentage weight contribution of an exam score to your final grade.",
        "formula": "Contribution = Exam Score * Weight",
        "formula_desc": "Evaluates the portion of your overall grade contributed by a specific test.",
        "icon": "🎓",
        "inputs": [
            {"id": "ep-score", "label": "Exam Score Obtained (%):", "type": "number", "default": "85"},
            {"id": "ep-weight", "label": "Exam Grade Weight (%):", "type": "number", "default": "40"}
        ],
        "outputs": [
            {"id": "ep-result", "label": "Grade Contribution:", "type": "text"}
        ],
        "calc_js": """
            const score = parseFloat(document.getElementById('ep-score').value);
            const weight = parseFloat(document.getElementById('ep-weight').value) / 100;

            if (isNaN(score) || isNaN(weight) || score < 0) {
                showToast("Please enter positive values.", "error");
                return;
            }

            const contribution = score * weight;
            document.getElementById('ep-result').textContent = contribution.toFixed(2) + "%";
            updateBreakdown(`<p>Exam score contribution: <code>${score}% * ${(weight*100)}%</code> = <strong>${contribution.toFixed(2)}%</strong> of overall class grade.</p>`);
        """
    },
    {
        "category": "Education Tools",
        "name": "Ranking Calculator",
        "slug": "ranking-calculator",
        "desc": "Convert a numerical rank into a percentile ranking class.",
        "formula": "Percentile = ((Total - Rank) / Total) * 100",
        "formula_desc": "Computes relative standing rank inside a total sample size population.",
        "icon": "🎓",
        "inputs": [
            {"id": "rn-rank", "label": "Your Rank:", "type": "number", "default": "5"},
            {"id": "rn-tot", "label": "Total Candidates:", "type": "number", "default": "100"}
        ],
        "outputs": [
            {"id": "rn-result", "label": "Percentile Ranking:", "type": "text"}
        ],
        "calc_js": """
            const rank = parseInt(document.getElementById('rn-rank').value);
            const total = parseInt(document.getElementById('rn-tot').value);

            if (isNaN(rank) || isNaN(total) || total <= 0 || rank <= 0 || rank > total) {
                showToast("Invalid ranking values.", "error");
                return;
            }

            const percentile = ((total - rank) / total) * 100;
            document.getElementById('rn-result').textContent = percentile.toFixed(2) + "th Percentile";
            updateBreakdown(`<p>Relative rank position: <code>((${total} - ${rank}) / ${total}) * 100</code> = <strong>${percentile.toFixed(4)}%</strong></p>`);
        """
    },
    {
        "category": "Education Tools",
        "name": "Academic Average Calculator",
        "slug": "academic-average-calculator",
        "desc": "Calculate average scores across multiple class semesters.",
        "formula": "Average = Sum(Semester Grades) / count",
        "formula_desc": "Computes the standard average of list items.",
        "icon": "🎓",
        "inputs": [
            {"id": "ac-list", "label": "Semester Marks (comma-separated):", "type": "text", "default": "82, 85, 90, 78, 88"}
        ],
        "outputs": [
            {"id": "ac-result", "label": "Average Marks:", "type": "text"}
        ],
        "calc_js": """
            const raw = document.getElementById('ac-list').value;
            const arr = raw.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));

            if (!arr.length) {
                showToast("Please enter semester marks.", "error");
                return;
            }

            const sum = arr.reduce((acc, curr) => acc + curr, 0);
            const avg = sum / arr.length;

            document.getElementById('ac-result').textContent = avg.toFixed(2) + "%";
            updateBreakdown(`<p>Academic Average = <code>(${arr.join(' + ')}) / ${arr.length}</code> = <strong>${avg.toFixed(4)}%</strong></p>`);
        """
    },
    {
        "category": "Random Number Tools",
        "name": "Random Number Generator",
        "slug": "random-number-generator-math",
        "desc": "Generate custom random integers within select boundaries.",
        "formula": "Standard floor math random math model",
        "formula_desc": "Uses standard random entropy multipliers and floors values to yield uniform distribution integers.",
        "icon": "🎲",
        "inputs": [
            {"id": "rng-min", "label": "Minimum Limit:", "type": "number", "default": "1"},
            {"id": "rng-max", "label": "Maximum Limit:", "type": "number", "default": "100"}
        ],
        "outputs": [
            {"id": "rng-result", "label": "Random Number:", "type": "text"}
        ],
        "calc_js": """
            const min = parseInt(document.getElementById('rng-min').value);
            const max = parseInt(document.getElementById('rng-max').value);

            if (isNaN(min) || isNaN(max) || max < min) {
                showToast("Invalid boundary range.", "error");
                return;
            }

            const rand = Math.floor(Math.random() * (max - min + 1)) + min;
            document.getElementById('rng-result').textContent = rand;
            updateBreakdown(`<p>Generated integer: <strong>${rand}</strong> inside range [${min}, ${max}]</p>`);
        """
    },
    {
        "category": "Random Number Tools",
        "name": "Random Decimal Generator",
        "slug": "random-decimal-generator",
        "desc": "Generate random floats/decimal numbers within a range.",
        "formula": "Float interval mapping",
        "formula_desc": "Maps Math.random() values to a selected min/max real number range.",
        "icon": "🎲",
        "inputs": [
            {"id": "rd-min", "label": "Min Value:", "type": "number", "default": "0"},
            {"id": "rd-max", "label": "Max Value:", "type": "number", "default": "1"},
            {"id": "rd-prec", "label": "Decimal Precision:", "type": "number", "default": "4"}
        ],
        "outputs": [
            {"id": "rd-result", "label": "Random Decimal:", "type": "text"}
        ],
        "calc_js": """
            const min = parseFloat(document.getElementById('rd-min').value);
            const max = parseFloat(document.getElementById('rd-max').value);
            const prec = parseInt(document.getElementById('rd-prec').value);

            if (isNaN(min) || isNaN(max) || isNaN(prec) || max < min || prec < 0) {
                showToast("Please enter valid parameters.", "error");
                return;
            }

            const rand = Math.random() * (max - min) + min;
            document.getElementById('rd-result').textContent = rand.toFixed(prec);
            updateBreakdown(`<p>Generated decimal: <strong>${rand.toFixed(prec)}</strong></p>`);
        """
    },
    {
        "category": "Random Number Tools",
        "name": "Random Integer Generator",
        "slug": "random-integer-generator",
        "desc": "Generate multiple random whole integers in one execution.",
        "formula": "Uniform random distribution generator",
        "formula_desc": "Generates multiple unique random integers within range bounds.",
        "icon": "🎲",
        "inputs": [
            {"id": "ri-min", "label": "Min Limit:", "type": "number", "default": "1"},
            {"id": "ri-max", "label": "Max Limit:", "type": "number", "default": "100"},
            {"id": "ri-count", "label": "Numbers count (Max 100):", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "ri-result", "label": "Generated Integers:", "type": "textarea"}
        ],
        "calc_js": """
            const min = parseInt(document.getElementById('ri-min').value);
            const max = parseInt(document.getElementById('ri-max').value);
            const count = parseInt(document.getElementById('ri-count').value);

            if (isNaN(min) || isNaN(max) || isNaN(count) || count <= 0 || max < min) {
                showToast("Please check range parameters.", "error");
                return;
            }
            if (count > 100) {
                showToast("Maximum quantity per request is 100.", "error");
                return;
            }

            let nums = [];
            for (let i = 0; i < count; i++) {
                nums.push(Math.floor(Math.random() * (max - min + 1)) + min);
            }

            document.getElementById('ri-result').value = nums.join(', ');
            updateBreakdown(`<p>Generated <strong>${count}</strong> numbers.</p>`);
        """
    },
    {
        "category": "Random Number Tools",
        "name": "Lottery Number Generator",
        "slug": "lottery-number-generator",
        "desc": "Generate custom random lottery numbers with no duplicates.",
        "formula": "Unique random item select",
        "formula_desc": "Sequentially draws random numbers within limit bounds, checking to reject duplicates.",
        "icon": "🔮",
        "inputs": [
            {"id": "lot-count", "label": "Balls to Draw (e.g. 6):", "type": "number", "default": "6"},
            {"id": "lot-max", "label": "Range Maximum (e.g. 49):", "type": "number", "default": "49"}
        ],
        "outputs": [
            {"id": "lot-result", "label": "Winning Numbers:", "type": "text"}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('lot-count').value);
            const max = parseInt(document.getElementById('lot-max').value);

            if (isNaN(count) || isNaN(max) || count <= 0 || max <= 0 || count > max) {
                showToast("Draw count cannot exceed range maximum.", "error");
                return;
            }

            let pool = [];
            for (let i = 1; i <= max; i++) pool.push(i);

            let chosen = [];
            for (let i = 0; i < count; i++) {
                const idx = Math.floor(Math.random() * pool.length);
                chosen.push(pool[idx]);
                pool.splice(idx, 1);
            }
            chosen.sort((a, b) => a - b);

            document.getElementById('lot-result').textContent = chosen.join(' - ');
            updateBreakdown(`<p>Drawn numbers sorted: <strong>${chosen.join(', ')}</strong></p>`);
        """
    },
    {
        "category": "Random Number Tools",
        "name": "Dice Roller",
        "slug": "dice-roller",
        "desc": "Roll virtual dice (standard D6, D20, or custom sides count) for games.",
        "formula": "Random discrete mapping",
        "formula_desc": "Generates a random integer value matching the faces count of the target die.",
        "icon": "🎲",
        "inputs": [
            {"id": "dice-sides", "label": "Dice Sides (e.g. 6, 20):", "type": "number", "default": "6"},
            {"id": "dice-count", "label": "Number of Dice to Roll:", "type": "number", "default": "2"}
        ],
        "outputs": [
            {"id": "dice-result", "label": "Roll Outcomes:", "type": "text"},
            {"id": "dice-sum", "label": "Sum of Rolls:", "type": "text"}
        ],
        "calc_js": """
            const sides = parseInt(document.getElementById('dice-sides').value);
            const count = parseInt(document.getElementById('dice-count').value);

            if (isNaN(sides) || isNaN(count) || sides <= 1 || count <= 0) {
                showToast("Please check dice values.", "error");
                return;
            }
            if (count > 50) {
                showToast("Maximum dice quantity is 50.", "error");
                return;
            }

            let rolls = [];
            let sum = 0;
            for (let i = 0; i < count; i++) {
                const r = Math.floor(Math.random() * sides) + 1;
                rolls.push(r);
                sum += r;
            }

            document.getElementById('dice-result').textContent = rolls.join(', ');
            document.getElementById('dice-sum').textContent = sum;
            updateBreakdown(`<p>Rolled <code>${count}d${sides}</code>. Sum = <strong>${sum}</strong></p>`);
        """
    },
    {
        "category": "Random Number Tools",
        "name": "Coin Flip Simulator",
        "slug": "coin-flip-simulator",
        "desc": "Simulate random coin flips and track heads vs. tails statistics.",
        "formula": "Binary event selection",
        "formula_desc": "Evaluates random float values to draw a Heads (>= 0.5) or Tails (< 0.5) outcome.",
        "icon": "🪙",
        "inputs": [
            {"id": "coin-flips", "label": "Flips Count:", "type": "number", "default": "100"}
        ],
        "outputs": [
            {"id": "coin-heads", "label": "Heads count:", "type": "text"},
            {"id": "coin-tails", "label": "Tails count:", "type": "text"}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('coin-flips').value);
            if (isNaN(count) || count <= 0) {
                showToast("Please enter a valid flips count.", "error");
                return;
            }
            if (count > 100000) {
                showToast("Maximum coin flips is 100,000.", "error");
                return;
            }

            let heads = 0;
            for (let i = 0; i < count; i++) {
                if (Math.random() >= 0.5) heads++;
            }
            const tails = count - heads;

            document.getElementById('coin-heads').textContent = heads.toLocaleString();
            document.getElementById('coin-tails').textContent = tails.toLocaleString();

            let explanation = `<p>Total flips: <strong>${count}</strong></p>`;
            explanation += `<p>Heads: <code>${((heads/count)*100).toFixed(2)}%</code>, Tails: <code>${((tails/count)*100).toFixed(2)}%</code></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Random Number Tools",
        "name": "Random Selection Generator",
        "slug": "random-selection-generator",
        "desc": "Randomly pick item names from a custom comma-separated list.",
        "formula": "Discrete choice index mapping",
        "formula_desc": "Draws a random index matching the array size boundaries.",
        "icon": "🎯",
        "inputs": [
            {"id": "sel-list", "label": "List Items (comma-separated):", "type": "textarea", "default": "Apple, Banana, Orange, Mango, Grape"},
            {"id": "sel-count", "label": "Items to Select:", "type": "number", "default": "1"}
        ],
        "outputs": [
            {"id": "sel-result", "label": "Selected Item(s):", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('sel-list').value;
            const count = parseInt(document.getElementById('sel-count').value);
            const items = raw.split(',').map(v => v.trim()).filter(v => v !== "");

            if (!items.length || isNaN(count) || count <= 0 || count > items.length) {
                showToast("Please enter valid items and select count less than total items.", "error");
                return;
            }

            let pool = [...items];
            let chosen = [];
            for (let i = 0; i < count; i++) {
                const idx = Math.floor(Math.random() * pool.length);
                chosen.push(pool[idx]);
                pool.splice(idx, 1);
            }

            document.getElementById('sel-result').value = chosen.join(', ');
            updateBreakdown(`<p>Picked item(s): <strong>${chosen.join(', ')}</strong></p>`);
        """
    },
    {
        "category": "Random Number Tools",
        "name": "Random Sequence Generator",
        "slug": "random-sequence-generator-math",
        "desc": "Shuffle a sequence of numbers randomly.",
        "formula": "Fisher-Yates shuffle algorithm",
        "formula_desc": "Sequentially swaps elements with random index elements to generate unbiased arrangements.",
        "icon": "🔢",
        "inputs": [
            {"id": "shuf-vals", "label": "Numbers to Shuffle (comma-separated):", "type": "textarea", "default": "1, 2, 3, 4, 5, 6, 7, 8"}
        ],
        "outputs": [
            {"id": "shuf-result", "label": "Shuffled Sequence:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('shuf-vals').value;
            const arr = raw.split(',').map(v => v.trim()).filter(v => v !== "");

            if (!arr.length) {
                showToast("Please enter items.", "error");
                return;
            }

            // Fisher-Yates Shuffle
            let shuffled = [...arr];
            for (let i = shuffled.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
            }

            document.getElementById('shuf-result').value = shuffled.join(', ');
            updateBreakdown(`<p>Sequence shuffled cleanly.</p>`);
        """
    },
    {
        "category": "Random Number Tools",
        "name": "Random Combination Generator",
        "slug": "random-combination-generator",
        "desc": "Generate random combinations (n choose k) from a list of values.",
        "formula": "Combinatorics subset selection",
        "formula_desc": "Selects unique subsets of size k from a list of size n.",
        "icon": "🔮",
        "inputs": [
            {"id": "comb-list", "label": "Items List (comma-separated):", "type": "textarea", "default": "A, B, C, D, E, F"},
            {"id": "comb-k", "label": "Subset Size k:", "type": "number", "default": "3"}
        ],
        "outputs": [
            {"id": "comb-result", "label": "Random Combination:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('comb-list').value;
            const k = parseInt(document.getElementById('comb-k').value);
            const items = raw.split(',').map(v => v.trim()).filter(v => v !== "");

            if (!items.length || isNaN(k) || k <= 0 || k > items.length) {
                showToast("Please check parameters.", "error");
                return;
            }

            let pool = [...items];
            let comb = [];
            for (let i = 0; i < k; i++) {
                const idx = Math.floor(Math.random() * pool.length);
                comb.push(pool[idx]);
                pool.splice(idx, 1);
            }
            comb.sort();

            document.getElementById('comb-result').value = comb.join(', ');
            updateBreakdown(`<p>Combination: <strong>${comb.join(', ')}</strong></p>`);
        """
    },
    {
        "category": "Random Number Tools",
        "name": "Random Statistics Generator",
        "slug": "random-statistics-generator",
        "desc": "Generate random normal-distributed data sets.",
        "formula": "Box-Muller transform algorithm",
        "formula_desc": "Translates uniform random float variables to standard normal distribution variables.",
        "icon": "📊",
        "inputs": [
            {"id": "rs-mean", "label": "Mean μ:", "type": "number", "default": "50"},
            {"id": "rs-sd", "label": "SD σ:", "type": "number", "default": "10"},
            {"id": "rs-size", "label": "Sample size (Max 100):", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "rs-result", "label": "Normal Dataset:", "type": "textarea"}
        ],
        "calc_js": """
            const mean = parseFloat(document.getElementById('rs-mean').value);
            const sd = parseFloat(document.getElementById('rs-sd').value);
            const size = parseInt(document.getElementById('rs-size').value);

            if (isNaN(mean) || isNaN(sd) || isNaN(size) || size <= 0 || sd < 0) {
                showToast("Please check parameters.", "error");
                return;
            }
            if (size > 100) {
                showToast("Maximum sample size is 100.", "error");
                return;
            }

            // Box-Muller transform
            function randn() {
                let u = 0, v = 0;
                while(u === 0) u = Math.random();
                while(v === 0) v = Math.random();
                return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
            }

            let samples = [];
            for (let i = 0; i < size; i++) {
                const val = mean + sd * randn();
                samples.push(val.toFixed(4));
            }

            document.getElementById('rs-result').value = samples.join(', ');
            updateBreakdown(`<p>Generated <strong>${size}</strong> normal-distributed samples.</p>`);
        """
    },
    {
        "category": "Math Generators",
        "name": "Multiplication Table Generator",
        "slug": "multiplication-table-generator",
        "desc": "Generate custom multiplication matrices tables for kids and worksheets.",
        "formula": "Multiplier expansion matrix",
        "formula_desc": "Multiplies row index by column index iteratively up to table limits.",
        "icon": "✖️",
        "inputs": [
            {"id": "tbl-num", "label": "Multiplication Number:", "type": "number", "default": "7"},
            {"id": "tbl-limit", "label": "Multiply Up To:", "type": "number", "default": "12"}
        ],
        "outputs": [
            {"id": "tbl-result", "label": "Multiplication Table:", "type": "textarea"}
        ],
        "calc_js": """
            const num = parseInt(document.getElementById('tbl-num').value);
            const limit = parseInt(document.getElementById('tbl-limit').value);

            if (isNaN(num) || isNaN(limit) || limit <= 0) {
                showToast("Please enter valid parameters.", "error");
                return;
            }
            if (limit > 100) {
                showToast("Maximum limit is 100.", "error");
                return;
            }

            let lines = [];
            for (let i = 1; i <= limit; i++) {
                lines.push(`${num} × ${i} = ${num * i}`);
            }

            document.getElementById('tbl-result').value = lines.join('\\n');
            updateBreakdown(`<p>Generated table for <strong>${num}</strong>.</p>`);
        """
    },
    {
        "category": "Math Generators",
        "name": "Worksheet Generator",
        "slug": "worksheet-generator",
        "desc": "Create standard practice worksheet tests for mathematics arithmetic.",
        "formula": "Randomized arithmetic question generator",
        "formula_desc": "Builds worksheets by drawing random operands and operator flags.",
        "icon": "📝",
        "inputs": [
            {"id": "ws-type", "label": "Operation Type:", "type": "select", "options": [
                ["add", "Addition"],
                ["sub", "Subtraction"],
                ["mixed", "Mixed Ops"]
            ]},
            {"id": "ws-count", "label": "Number of Problems:", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "ws-result", "label": "Worksheet Problems:", "type": "textarea"}
        ],
        "calc_js": """
            const type = document.getElementById('ws-type').value;
            const count = parseInt(document.getElementById('ws-count').value);

            if (isNaN(count) || count <= 0) {
                showToast("Please enter a valid count.", "error");
                return;
            }

            let problems = [];
            const ops = ["+", "-"];

            for (let i = 1; i <= count; i++) {
                const op = type === "mixed" ? ops[Math.floor(Math.random()*ops.length)] : (type === "add" ? "+" : "-");
                const o1 = Math.floor(Math.random() * 90) + 10;
                const o2 = Math.floor(Math.random() * 90) + 10;
                problems.push(`${i})  ${o1} ${op} ${o2} = ______`);
            }

            document.getElementById('ws-result').value = problems.join('\\n\\n');
            updateBreakdown(`<p>Generated arithmetic worksheet.</p>`);
        """
    },
    {
        "category": "Math Generators",
        "name": "Math Quiz Generator",
        "slug": "math-quiz-generator",
        "desc": "Generate custom mathematics quizzes with accompanying answer sheets.",
        "formula": "Random math problem generators",
        "formula_desc": "Generates math questions along with key solutions.",
        "icon": "🧠",
        "inputs": [
            {"id": "qz-diff", "label": "Difficulty:", "type": "select", "options": [
                ["easy", "Easy (Single digits)"],
                ["hard", "Hard (Double digits)"]
            ]},
            {"id": "qz-count", "label": "Quiz Size:", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "qz-questions", "label": "Questions List:", "type": "textarea"},
            {"id": "qz-answers", "label": "Answers Key:", "type": "textarea"}
        ],
        "calc_js": """
            const diff = document.getElementById('qz-diff').value;
            const count = parseInt(document.getElementById('qz-count').value);

            if (isNaN(count) || count <= 0) {
                showToast("Please enter a valid count.", "error");
                return;
            }

            let qList = [];
            let aList = [];
            const maxVal = diff === "easy" ? 10 : 100;

            for (let i = 1; i <= count; i++) {
                const o1 = Math.floor(Math.random() * maxVal) + 2;
                const o2 = Math.floor(Math.random() * maxVal) + 2;
                const op = Math.random() >= 0.5 ? "+" : "×";
                const ans = op === "+" ? o1 + o2 : o1 * o2;

                qList.push(`${i}. What is ${o1} ${op} ${o2}?`);
                aList.push(`${i}. Answer: ${ans}`);
            }

            document.getElementById('qz-questions').value = qList.join('\\n');
            document.getElementById('qz-answers').value = aList.join('\\n');
            updateBreakdown(`<p>Quiz generated successfully.</p>`);
        """
    },
    {
        "category": "Math Generators",
        "name": "Arithmetic Problem Generator",
        "slug": "arithmetic-problem-generator",
        "desc": "Generate random practice arithmetic problems for tests.",
        "formula": "Standard randomized operator mappings",
        "formula_desc": "Draws numbers and operators to generate valid arithmetic problems.",
        "icon": "➕",
        "inputs": [
            {"id": "ap-count", "label": "Number of Problems:", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "ap-result", "label": "Generated Problems:", "type": "textarea"}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('ap-count').value);
            if (isNaN(count) || count <= 0) {
                showToast("Invalid count.", "error");
                return;
            }

            let problems = [];
            for (let i = 1; i <= count; i++) {
                const o1 = Math.floor(Math.random() * 50) + 10;
                const o2 = Math.floor(Math.random() * 40) + 5;
                problems.push(`${i}.  ${o1} + ${o2} = ?`);
            }

            document.getElementById('ap-result').value = problems.join('\\n');
            updateBreakdown(`<p>Generated ${count} arithmetic questions.</p>`);
        """
    },
    {
        "category": "Math Generators",
        "name": "Algebra Problem Generator",
        "slug": "algebra-problem-generator",
        "desc": "Generate basic linear equation algebra problems.",
        "formula": "Random linear coefficient mappings",
        "formula_desc": "Generates expressions of the form ax + b = c.",
        "icon": "📐",
        "inputs": [
            {"id": "algp-count", "label": "Number of Equations:", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "algp-result", "label": "Algebra Problems:", "type": "textarea"}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('algp-count').value);
            if (isNaN(count) || count <= 0) {
                showToast("Please enter a valid count.", "error");
                return;
            }

            let problems = [];
            for (let i = 1; i <= count; i++) {
                const a = Math.floor(Math.random() * 8) + 2;
                const x = Math.floor(Math.random() * 9) + 2;
                const b = Math.floor(Math.random() * 15) + 1;
                const c = a * x + b;
                problems.push(`${i}. Solve: ${a}x + ${b} = ${c}  (Answer: x = ${x})`);
            }

            document.getElementById('algp-result').value = problems.join('\\n');
            updateBreakdown(`<p>Algebra worksheet compiled.</p>`);
        """
    },
    {
        "category": "Math Generators",
        "name": "Geometry Problem Generator",
        "slug": "geometry-problem-generator",
        "desc": "Generate area/perimeter geometry questions.",
        "formula": "Standard shape area calculations",
        "formula_desc": "Generates shapes with random dimensions to calculate area or perimeter.",
        "icon": "📐",
        "inputs": [
            {"id": "gp-count", "label": "Number of Problems:", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "gp-result", "label": "Geometry Problems:", "type": "textarea"}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('gp-count').value);
            if (isNaN(count) || count <= 0) {
                showToast("Please enter a count.", "error");
                return;
            }

            let problems = [];
            for (let i = 1; i <= count; i++) {
                const w = Math.floor(Math.random() * 12) + 4;
                const h = Math.floor(Math.random() * 15) + 4;
                problems.push(`${i}. Find the area of a rectangle with width = ${w}m and height = ${h}m. (Answer: ${w*h} m²)`);
            }

            document.getElementById('gp-result').value = problems.join('\\n');
            updateBreakdown(`<p>Generated ${count} geometry problems.</p>`);
        """
    },
    {
        "category": "Math Generators",
        "name": "Fraction Problem Generator",
        "slug": "fraction-problem-generator",
        "desc": "Generate fraction addition and subtraction questions.",
        "formula": "Random fraction arithmetic",
        "formula_desc": "Generates problems involving fractions.",
        "icon": "➗",
        "inputs": [
            {"id": "fp-count", "label": "Number of Problems:", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "fp-result", "label": "Fraction Problems:", "type": "textarea"}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('fp-count').value);
            if (isNaN(count) || count <= 0) {
                showToast("Please enter a valid count.", "error");
                return;
            }

            let problems = [];
            for (let i = 1; i <= count; i++) {
                const d1 = Math.floor(Math.random() * 8) + 2;
                const d2 = Math.floor(Math.random() * 8) + 2;
                const n1 = Math.floor(Math.random() * (d1 - 1)) + 1;
                const n2 = Math.floor(Math.random() * (d2 - 1)) + 1;
                problems.push(`${i}.  ${n1}/${d1} + ${n2}/${d2} = ?`);
            }

            document.getElementById('fp-result').value = problems.join('\\n');
            updateBreakdown(`<p>Fraction questions generated.</p>`);
        """
    },
    {
        "category": "Math Generators",
        "name": "Equation Generator",
        "slug": "equation-generator",
        "desc": "Generate algebraic linear and quadratic equations for testing.",
        "formula": "Random linear/quadratic generators",
        "formula_desc": "Builds equations with random constants and variable multipliers.",
        "icon": "📐",
        "inputs": [
            {"id": "eqg-type", "label": "Equation Type:", "type": "select", "options": [
                ["linear", "Linear (ax + b = c)"],
                ["quadratic", "Quadratic (ax² + bx + c = 0)"]
            ]},
            {"id": "eqg-count", "label": "Count:", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "eqg-result", "label": "Equations List:", "type": "textarea"}
        ],
        "calc_js": """
            const type = document.getElementById('eqg-type').value;
            const count = parseInt(document.getElementById('eqg-count').value);

            if (isNaN(count) || count <= 0) {
                showToast("Please enter a valid count.", "error");
                return;
            }

            let list = [];
            for (let i = 1; i <= count; i++) {
                if (type === "linear") {
                    const a = Math.floor(Math.random()*9)+2;
                    const b = Math.floor(Math.random()*20)+1;
                    const c = Math.floor(Math.random()*50)+20;
                    list.push(`${i}. Solve: ${a}x + ${b} = ${c}`);
                } else {
                    const a = 1;
                    const x1 = Math.floor(Math.random()*8)+1;
                    const x2 = Math.floor(Math.random()*8)+1;
                    const b = -(x1 + x2);
                    const c = x1 * x2;
                    list.push(`${i}. Solve: x² ${b >= 0 ? '+' : '-'} ${Math.abs(b)}x ${c >= 0 ? '+' : '-'} ${Math.abs(c)} = 0`);
                }
            }

            document.getElementById('eqg-result').value = list.join('\\n');
            updateBreakdown(`<p>Equations list generated.</p>`);
        """
    },
    {
        "category": "Math Generators",
        "name": "Number Pattern Generator",
        "slug": "number-pattern-generator-math",
        "desc": "Generate custom arithmetic or geometric number patterns.",
        "formula": "Number pattern arithmetic progressions",
        "formula_desc": "Generates sequences.",
        "icon": "🧬",
        "inputs": [
            {"id": "npg-count", "label": "Number of elements:", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "npg-result", "label": "Pattern Output:", "type": "textarea"}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('npg-count').value);
            if (isNaN(count) || count <= 0) {
                showToast("Please enter a valid count.", "error");
                return;
            }

            let pattern = [];
            let current = 2;
            for (let i = 0; i < count; i++) {
                pattern.push(current);
                current = current * 2 - 1; // custom mathematical pattern rule
            }

            document.getElementById('npg-result').value = pattern.join(', ');
            updateBreakdown(`<p>Generated custom number sequence.</p>`);
        """
    },
    {
        "category": "Math Generators",
        "name": "Practice Test Generator",
        "slug": "practice-test-generator",
        "desc": "Generate a comprehensive practice math test.",
        "formula": "Random math problem selectors",
        "formula_desc": "Selects mixed problems from basic math categories.",
        "icon": "📝",
        "inputs": [
            {"id": "pt-size", "label": "Test Size (Questions):", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "pt-result", "label": "Practice Test:", "type": "textarea"}
        ],
        "calc_js": """
            const size = parseInt(document.getElementById('pt-size').value);
            if (isNaN(size) || size <= 0) {
                showToast("Please check parameters.", "error");
                return;
            }

            let test = [];
            for (let i = 1; i <= size; i++) {
                const op = Math.random() >= 0.5 ? "+" : "×";
                const o1 = Math.floor(Math.random() * 12) + 2;
                const o2 = Math.floor(Math.random() * 12) + 2;
                test.push(`${i}.  Calculate: ${o1} ${op} ${o2} = ?`);
            }

            document.getElementById('pt-result').value = test.join('\\n\\n');
            updateBreakdown(`<p>Practice test with ${size} questions generated.</p>`);
        """
    }
]

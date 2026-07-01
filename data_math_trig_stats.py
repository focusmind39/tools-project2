# -*- coding: utf-8 -*-
"""
Database of Trigonometry Tools & Statistics Tools (20 tools)
"""

TRIG_STATS_TOOLS = [
    {
        "category": "Trigonometry Tools",
        "name": "Sine Calculator",
        "slug": "sine-calculator",
        "desc": "Calculate the sine value of any angle in degrees or radians.",
        "formula": "sin(x)",
        "formula_desc": "Evaluates the sine trigonometric function of the input angle.",
        "icon": "📐",
        "inputs": [
            {"id": "sin-val", "label": "Angle Value:", "type": "number", "default": "30"},
            {"id": "sin-unit", "label": "Angle Unit:", "type": "select", "options": [
                ["deg", "Degrees (°)"],
                ["rad", "Radians (rad)"]
            ]}
        ],
        "outputs": [
            {"id": "sin-result", "label": "Sine Value:", "type": "text"}
        ],
        "calc_js": """
            const val = parseFloat(document.getElementById('sin-val').value);
            const unit = document.getElementById('sin-unit').value;

            if (isNaN(val)) {
                showToast("Please enter a numeric angle value.", "error");
                return;
            }

            const rad = unit === "deg" ? (val * Math.PI) / 180 : val;
            const res = Math.sin(rad);

            document.getElementById('sin-result').textContent = res.toLocaleString(undefined, {maximumFractionDigits: 6});

            let steps = `<p>Input angle: <strong>${val} ${unit === 'deg' ? 'degrees' : 'radians'}</strong></p>`;
            if (unit === "deg") {
                steps += `<p>1. Convert degrees to radians: <code>(${val} * π) / 180</code> = <strong>${rad.toFixed(6)} rad</strong></p>`;
            }
            steps += `<p>2. Evaluate: <code>sin(${rad.toFixed(6)})</code> = <strong>${res}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Trigonometry Tools",
        "name": "Cosine Calculator",
        "slug": "cosine-calculator",
        "desc": "Calculate the cosine value of an angle in degrees or radians.",
        "formula": "cos(x)",
        "formula_desc": "Evaluates the cosine trigonometric function of the input angle.",
        "icon": "📐",
        "inputs": [
            {"id": "cos-val", "label": "Angle Value:", "type": "number", "default": "60"},
            {"id": "cos-unit", "label": "Angle Unit:", "type": "select", "options": [
                ["deg", "Degrees (°)"],
                ["rad", "Radians (rad)"]
            ]}
        ],
        "outputs": [
            {"id": "cos-result", "label": "Cosine Value:", "type": "text"}
        ],
        "calc_js": """
            const val = parseFloat(document.getElementById('cos-val').value);
            const unit = document.getElementById('cos-unit').value;

            if (isNaN(val)) {
                showToast("Please enter an angle.", "error");
                return;
            }

            const rad = unit === "deg" ? (val * Math.PI) / 180 : val;
            const res = Math.cos(rad);

            document.getElementById('cos-result').textContent = res.toLocaleString(undefined, {maximumFractionDigits: 6});

            let steps = `<p>Input angle: <strong>${val} ${unit === 'deg' ? 'degrees' : 'radians'}</strong></p>`;
            if (unit === "deg") {
                steps += `<p>1. Convert degrees to radians: <code>(${val} * π) / 180</code> = <strong>${rad.toFixed(6)} rad</strong></p>`;
            }
            steps += `<p>2. Evaluate: <code>cos(${rad.toFixed(6)})</code> = <strong>${res}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Trigonometry Tools",
        "name": "Tangent Calculator",
        "slug": "tangent-calculator",
        "desc": "Calculate the tangent value of an angle in degrees or radians.",
        "formula": "tan(x) = sin(x) / cos(x)",
        "formula_desc": "Evaluates the ratio of sine to cosine for the given angle, flagging undefined boundaries.",
        "icon": "📐",
        "inputs": [
            {"id": "tan-val", "label": "Angle Value:", "type": "number", "default": "45"},
            {"id": "tan-unit", "label": "Angle Unit:", "type": "select", "options": [
                ["deg", "Degrees (°)"],
                ["rad", "Radians (rad)"]
            ]}
        ],
        "outputs": [
            {"id": "tan-result", "label": "Tangent Value:", "type": "text"}
        ],
        "calc_js": """
            const val = parseFloat(document.getElementById('tan-val').value);
            const unit = document.getElementById('tan-unit').value;

            if (isNaN(val)) {
                showToast("Please enter an angle.", "error");
                return;
            }

            const rad = unit === "deg" ? (val * Math.PI) / 180 : val;
            // Check for undefined tan points (e.g. 90, 270 deg etc)
            if (unit === "deg" && Math.abs(val % 180) === 90) {
                document.getElementById('tan-result').textContent = "Undefined";
                updateBreakdown("<p class='text-danger'>Tangent is undefined for odd multiples of 90°.</p>");
                return;
            }

            const res = Math.tan(rad);
            document.getElementById('tan-result').textContent = res.toLocaleString(undefined, {maximumFractionDigits: 6});

            let steps = `<p>Input angle: <strong>${val} ${unit === 'deg' ? 'degrees' : 'radians'}</strong></p>`;
            if (unit === "deg") {
                steps += `<p>1. Convert to radians: <code>(${val} * π) / 180</code> = <strong>${rad.toFixed(6)} rad</strong></p>`;
            }
            steps += `<p>2. Evaluate: <code>tan(${rad.toFixed(6)})</code> = <strong>${res}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Trigonometry Tools",
        "name": "Inverse Trigonometry Calculator",
        "slug": "inverse-trigonometry-calculator",
        "desc": "Calculate inverse trig values (arcsin, arccos, arctan) in degrees or radians.",
        "formula": "asin(x), acos(x), atan(x)",
        "formula_desc": "Evaluates standard inverse trigonometric operations, checking for out-of-range inputs.",
        "icon": "📐",
        "inputs": [
            {"id": "itrig-type", "label": "Function:", "type": "select", "options": [
                ["asin", "Arcsin (sin⁻¹)"],
                ["acos", "Arccos (cos⁻¹)"],
                ["atan", "Arctan (tan⁻¹)"]
            ]},
            {"id": "itrig-val", "label": "Value x (Between -1 and 1 for arcsin/arccos):", "type": "number", "default": "0.5"},
            {"id": "itrig-unit", "label": "Output Unit:", "type": "select", "options": [
                ["deg", "Degrees (°)"],
                ["rad", "Radians (rad)"]
            ]}
        ],
        "outputs": [
            {"id": "itrig-result", "label": "Angle Result:", "type": "text"}
        ],
        "calc_js": """
            const type = document.getElementById('itrig-type').value;
            const x = parseFloat(document.getElementById('itrig-val').value);
            const unit = document.getElementById('itrig-unit').value;

            if (isNaN(x)) {
                showToast("Please enter a numeric input.", "error");
                return;
            }

            if ((type === "asin" || type === "acos") && (x < -1 || x > 1)) {
                showToast("Input value for arcsin/arccos must be between -1 and 1.", "error");
                return;
            }

            let rad = 0;
            if (type === "asin") rad = Math.asin(x);
            else if (type === "acos") rad = Math.acos(x);
            else rad = Math.atan(x);

            const outVal = unit === "deg" ? (rad * 180) / Math.PI : rad;

            document.getElementById('itrig-result').textContent = outVal.toLocaleString(undefined, {maximumFractionDigits: 6}) + (unit === "deg" ? "°" : "");

            let steps = `<p>Inverse function: <strong>${type}</strong> for value <strong>${x}</strong></p>`;
            steps += `<p>Result in radians: <code>${rad.toFixed(6)} rad</code></p>`;
            if (unit === "deg") {
                steps += `<p>Converted to degrees: <code>(${rad.toFixed(6)} * 180) / π</code> = <strong>${outVal.toFixed(4)}°</strong></p>`;
            }
            updateBreakdown(steps);
        """
    },
    {
        "category": "Trigonometry Tools",
        "name": "Right Triangle Solver",
        "slug": "right-triangle-solver",
        "desc": "Solve for missing sides and angles in a right-angled triangle.",
        "formula": "Trigonometric ratios & Pythagorean theorem",
        "formula_desc": "Solves using sin(θ) = opposite/hypotenuse, cos(θ) = adjacent/hypotenuse, and side² + side² = hypotenuse².",
        "icon": "📐",
        "inputs": [
            {"id": "rt-a", "label": "Side a (Opposite):", "type": "number", "default": "3"},
            {"id": "rt-b", "label": "Side b (Adjacent):", "type": "number", "default": "4"},
            {"id": "rt-c", "label": "Side c (Hypotenuse - Leave blank to solve):", "type": "number", "default": ""}
        ],
        "outputs": [
            {"id": "rt-result", "label": "Solved Value:", "type": "text"}
        ],
        "calc_js": """
            const aStr = document.getElementById('rt-a').value.trim();
            const bStr = document.getElementById('rt-b').value.trim();
            const cStr = document.getElementById('rt-c').value.trim();

            const a = parseFloat(aStr);
            const b = parseFloat(bStr);
            const c = parseFloat(cStr);

            let res = "";
            let explanation = "";

            if (cStr === "") {
                if (isNaN(a) || isNaN(b) || a <= 0 || b <= 0) {
                    showToast("Please enter positive values for side a and b.", "error");
                    return;
                }
                const solvedC = Math.sqrt(a * a + b * b);
                const angleA = Math.atan(a / b) * 180 / Math.PI;
                const angleB = 90 - angleA;

                res = `Hypotenuse c: ${solvedC.toFixed(4)}`;
                explanation = `<p>Pythagorean Theorem: <code>c = sqrt(a² + b²) = sqrt(${a}² + ${b}²)</code> = <strong>${solvedC.toFixed(4)}</strong></p>`;
                explanation += `<p>Angle A: <code>atan(a/b)</code> = <strong>${angleA.toFixed(2)}°</strong></p>`;
                explanation += `<p>Angle B: <code>90 - A</code> = <strong>${angleB.toFixed(2)}°</strong></p>`;
            } else {
                if (isNaN(c) || c <= 0) {
                    showToast("Please enter positive values.", "error");
                    return;
                }
                if (aStr === "") {
                    if (c <= b) { showToast("Hypotenuse c must be larger than side b.", "error"); return; }
                    const solvedA = Math.sqrt(c * c - b * b);
                    res = `Side a: ${solvedA.toFixed(4)}`;
                    explanation = `<p>Pythagorean Theorem: <code>a = sqrt(c² - b²) = sqrt(${c}² - ${b}²)</code> = <strong>${solvedA.toFixed(4)}</strong></p>`;
                } else if (bStr === "") {
                    if (c <= a) { showToast("Hypotenuse c must be larger than side a.", "error"); return; }
                    const solvedB = Math.sqrt(c * c - a * a);
                    res = `Side b: ${solvedB.toFixed(4)}`;
                    explanation = `<p>Pythagorean Theorem: <code>b = sqrt(c² - a²) = sqrt(${c}² - ${a}²)</code> = <strong>${solvedB.toFixed(4)}</strong></p>`;
                }
            }

            document.getElementById('rt-result').textContent = res;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Trigonometry Tools",
        "name": "Pythagorean Theorem Calculator",
        "slug": "pythagorean-theorem-calculator-math",
        "desc": "Calculate missing lengths of right triangle sides using standard Pythagorean rules.",
        "formula": "a^2 + b^2 = c^2",
        "formula_desc": "Solves for the hypotenuse or either leg of a right triangle.",
        "icon": "📐",
        "inputs": [
            {"id": "py-a", "label": "Side a (Leg):", "type": "number", "default": "5"},
            {"id": "py-b", "label": "Side b (Leg):", "type": "number", "default": "12"},
            {"id": "py-c", "label": "Hypotenuse c (Leave blank to solve):", "type": "number", "default": ""}
        ],
        "outputs": [
            {"id": "py-result", "label": "Solved Value:", "type": "text"}
        ],
        "calc_js": """
            const a = parseFloat(document.getElementById('py-a').value);
            const b = parseFloat(document.getElementById('py-b').value);
            const cStr = document.getElementById('py-c').value.trim();

            let result = 0;
            let explanation = "";

            if (cStr === "") {
                if (isNaN(a) || isNaN(b) || a <= 0 || b <= 0) {
                    showToast("Please enter positive values for leg a and b.", "error");
                    return;
                }
                result = Math.sqrt(a * a + b * b);
                explanation = `<p>Solving for hypotenuse c: <code>c = sqrt(a² + b²) = sqrt(${a}² + ${b}²)</code> = <strong>${result.toFixed(4)}</strong></p>`;
            } else {
                const c = parseFloat(cStr);
                if (isNaN(c) || c <= 0) {
                    showToast("Please enter a positive value for hypotenuse c.", "error");
                    return;
                }
                if (isNaN(a)) {
                    if (c <= b) { showToast("Hypotenuse must be larger than side b.", "error"); return; }
                    result = Math.sqrt(c * c - b * b);
                    explanation = `<p>Solving for leg a: <code>a = sqrt(c² - b²) = sqrt(${c}² - ${b}²)</code> = <strong>${result.toFixed(4)}</strong></p>`;
                } else {
                    if (c <= a) { showToast("Hypotenuse must be larger than side a.", "error"); return; }
                    result = Math.sqrt(c * c - a * a);
                    explanation = `<p>Solving for leg b: <code>b = sqrt(c² - a²) = sqrt(${c}² - ${a}²)</code> = <strong>${result.toFixed(4)}</strong></p>`;
                }
            }

            document.getElementById('py-result').textContent = result.toLocaleString(undefined, {maximumFractionDigits: 6});
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Trigonometry Tools",
        "name": "Angle Converter",
        "slug": "angle-converter",
        "desc": "Convert angles bidirectionally between degrees, radians, gradians, and turns.",
        "formula": "Standard angle unit ratios",
        "formula_desc": "Converts input angle to degrees first, then translates it to all other target unit types.",
        "icon": "📐",
        "inputs": [
            {"id": "ang-val", "label": "Angle value:", "type": "number", "default": "180"},
            {"id": "ang-unit", "label": "From Unit:", "type": "select", "options": [
                ["deg", "Degrees (°)"],
                ["rad", "Radians (rad)"],
                ["grad", "Gradians (grad)"],
                ["turn", "Turns (turn)"]
            ]}
        ],
        "outputs": [
            {"id": "ang-deg", "label": "Degrees:", "type": "text"},
            {"id": "ang-rad", "label": "Radians:", "type": "text"},
            {"id": "ang-grad", "label": "Gradians:", "type": "text"}
        ],
        "calc_js": """
            const val = parseFloat(document.getElementById('ang-val').value);
            const unit = document.getElementById('ang-unit').value;

            if (isNaN(val)) {
                showToast("Please enter a valid numeric angle value.", "error");
                return;
            }

            // Convert to degrees first
            let deg = 0;
            if (unit === "deg") deg = val;
            else if (unit === "rad") deg = (val * 180) / Math.PI;
            else if (unit === "grad") deg = (val * 9) / 10;
            else if (unit === "turn") deg = val * 360;

            const rad = (deg * Math.PI) / 180;
            const grad = (deg * 10) / 9;
            const turn = deg / 360;

            document.getElementById('ang-deg').textContent = deg.toFixed(4).replace(/\\.0+$/, '') + "°";
            document.getElementById('ang-rad').textContent = rad.toFixed(6).replace(/\\.0+$/, '') + " rad";
            document.getElementById('ang-grad').textContent = grad.toFixed(4).replace(/\\.0+$/, '') + " grad";

            let steps = `<p>Input angle: <strong>${val} ${unit}</strong></p>`;
            steps += `<p>Normalized to degrees: <strong>${deg.toFixed(4)}°</strong></p>`;
            steps += `<p>Equivalent in turns: <strong>${turn.toFixed(6)} turns</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Trigonometry Tools",
        "name": "Degree To Radian Converter",
        "slug": "degree-to-radian-converter",
        "desc": "Quickly convert angles from degrees to radians.",
        "formula": "Radians = Degrees * (pi / 180)",
        "formula_desc": "Multiplies degree value by pi and divides by 180 to convert it to radians.",
        "icon": "📐",
        "inputs": [
            {"id": "d2r-val", "label": "Degrees (°):", "type": "number", "default": "90"}
        ],
        "outputs": [
            {"id": "d2r-result", "label": "Radians (rad):", "type": "text"}
        ],
        "calc_js": """
            const val = parseFloat(document.getElementById('d2r-val').value);
            if (isNaN(val)) {
                showToast("Please enter degrees.", "error");
                return;
            }

            const rad = (val * Math.PI) / 180;
            document.getElementById('d2r-result').textContent = rad.toLocaleString(undefined, {maximumFractionDigits: 6});

            let explanation = `<p>Formula: <code>rad = deg * (π / 180)</code></p>`;
            explanation += `<p>Calculation: <code>${val} * (${Math.PI.toFixed(6)} / 180)</code> = <strong>${rad.toFixed(6)} rad</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Trigonometry Tools",
        "name": "Radian To Degree Converter",
        "slug": "radian-to-degree-converter",
        "desc": "Quickly convert angles from radians to degrees.",
        "formula": "Degrees = Radians * (180 / pi)",
        "formula_desc": "Multiplies radian values by 180 and divides by the mathematical constant pi.",
        "icon": "📐",
        "inputs": [
            {"id": "r2d-val", "label": "Radians (rad):", "type": "number", "default": "1"}
        ],
        "outputs": [
            {"id": "r2d-result", "label": "Degrees (°):", "type": "text"}
        ],
        "calc_js": """
            const val = parseFloat(document.getElementById('r2d-val').value);
            if (isNaN(val)) {
                showToast("Please enter radians.", "error");
                return;
            }

            const deg = (val * 180) / Math.PI;
            document.getElementById('r2d-result').textContent = deg.toLocaleString(undefined, {maximumFractionDigits: 6}) + "°";

            let explanation = `<p>Formula: <code>deg = rad * (180 / π)</code></p>`;
            explanation += `<p>Calculation: <code>${val} * (180 / ${Math.PI.toFixed(6)})</code> = <strong>${deg.toFixed(4)}°</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Trigonometry Tools",
        "name": "Trigonometry Solver",
        "slug": "trigonometry-solver",
        "desc": "Solve for basic ratios: sine, cosine, tangent, cosecant, secant, and cotangent of an angle.",
        "formula": "All six trigonometric ratios evaluation",
        "formula_desc": "Evaluates base and reciprocal trigonometric functions for any given angle value.",
        "icon": "📐",
        "inputs": [
            {"id": "trig-s-val", "label": "Angle in Degrees (°):", "type": "number", "default": "45"}
        ],
        "outputs": [
            {"id": "trig-s-sin", "label": "sin(x):", "type": "text"},
            {"id": "trig-s-cos", "label": "cos(x):", "type": "text"},
            {"id": "trig-s-tan", "label": "tan(x):", "type": "text"}
        ],
        "calc_js": """
            const deg = parseFloat(document.getElementById('trig-s-val').value);
            if (isNaN(deg)) {
                showToast("Please enter an angle.", "error");
                return;
            }

            const rad = (deg * Math.PI) / 180;
            const s = Math.sin(rad);
            const c = Math.cos(rad);

            let t = Math.abs(deg % 180) === 90 ? "Undefined" : Math.tan(rad).toFixed(6).replace(/\\.0+$/, '');

            document.getElementById('trig-s-sin').textContent = s.toFixed(6).replace(/\\.0+$/, '');
            document.getElementById('trig-s-cos').textContent = c.toFixed(6).replace(/\\.0+$/, '');
            document.getElementById('trig-s-tan').textContent = t;

            let steps = `<p>Reciprocals calculated:</p>`;
            steps += `<p>csc(x) = <code>1/sin(x)</code> = <strong>${s === 0 ? 'Undefined' : (1/s).toFixed(6)}</strong></p>`;
            steps += `<p>sec(x) = <code>1/cos(x)</code> = <strong>${c === 0 ? 'Undefined' : (1/c).toFixed(6)}</strong></p>`;
            steps += `<p>cot(x) = <code>1/tan(x)</code> = <strong>${t === "Undefined" || s === 0 ? 'Undefined' : (1/Math.tan(rad)).toFixed(6)}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Statistics Tools",
        "name": "Mean Calculator",
        "slug": "mean-calculator-stats",
        "desc": "Calculate Arithmetic Mean of a set of statistical numbers.",
        "formula": "Sum of values / count",
        "formula_desc": "Finds the average central value by dividing the sum of all elements by the dataset length.",
        "icon": "📊",
        "inputs": [
            {"id": "m-vals", "label": "Comma-Separated Numbers:", "type": "textarea", "default": "10, 20, 30, 40, 50"}
        ],
        "outputs": [
            {"id": "m-result", "label": "Arithmetic Mean:", "type": "text"}
        ],
        "calc_js": """
            const raw = document.getElementById('m-vals').value;
            const arr = raw.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));

            if (!arr.length) {
                showToast("Please enter numbers.", "error");
                return;
            }

            const sum = arr.reduce((acc, curr) => acc + curr, 0);
            const mean = sum / arr.length;

            document.getElementById('m-result').textContent = mean.toLocaleString(undefined, {maximumFractionDigits: 6});
            updateBreakdown(`<p>Sum of elements: <code>${sum}</code></p><p>Count of elements: <code>${arr.length}</code></p><p>Mean = <code>${sum} / ${arr.length}</code> = <strong>${mean}</strong></p>`);
        """
    },
    {
        "category": "Statistics Tools",
        "name": "Median Calculator",
        "slug": "median-calculator-math",
        "desc": "Locate the middle value element in a sorted numerical dataset.",
        "formula": "Sorted index offset positioning",
        "formula_desc": "Sorts the data and finds the middle element (or average of two middle elements for even lengths).",
        "icon": "📊",
        "inputs": [
            {"id": "med-vals", "label": "Comma-Separated Numbers:", "type": "textarea", "default": "7, 12, 3, 21, 15, 9"}
        ],
        "outputs": [
            {"id": "med-result", "label": "Median Value:", "type": "text"}
        ],
        "calc_js": """
            const raw = document.getElementById('med-vals').value;
            const arr = raw.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));

            if (!arr.length) {
                showToast("Please enter numbers.", "error");
                return;
            }

            const sorted = [...arr].sort((a, b) => a - b);
            const mid = Math.floor(sorted.length / 2);
            const median = sorted.length % 2 !== 0 ? sorted[mid] : (sorted[mid - 1] + sorted[mid]) / 2;

            document.getElementById('med-result').textContent = median.toLocaleString();

            let steps = `<p>1. Sort the numbers: <code>[${sorted.join(', ')}]</code></p>`;
            if (sorted.length % 2 !== 0) {
                steps += `<p>2. Length is odd. Middle element is at index ${mid}: <strong>${median}</strong></p>`;
            } else {
                steps += `<p>2. Length is even. Average of middle two elements (<code>${sorted[mid - 1]}</code> and <code>${sorted[mid]}</code>) is: <strong>${median}</strong></p>`;
            }
            updateBreakdown(steps);
        """
    },
    {
        "category": "Statistics Tools",
        "name": "Mode Calculator",
        "slug": "mode-calculator-math",
        "desc": "Locate the most frequent value element(s) in a numerical series.",
        "formula": "Frequency distribution peaks",
        "formula_desc": "Tallies occurrences of each unique value and finds the maximum frequency.",
        "icon": "📊",
        "inputs": [
            {"id": "mode-vals", "label": "Comma-Separated Numbers:", "type": "textarea", "default": "4, 5, 4, 2, 8, 5, 4, 3"}
        ],
        "outputs": [
            {"id": "mode-result", "label": "Mode(s):", "type": "text"}
        ],
        "calc_js": """
            const raw = document.getElementById('mode-vals').value;
            const arr = raw.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));

            if (!arr.length) {
                showToast("Please enter numbers.", "error");
                return;
            }

            const freqs = {};
            let maxFreq = 0;
            arr.forEach(num => {
                freqs[num] = (freqs[num] || 0) + 1;
                if (freqs[num] > maxFreq) {
                    maxFreq = freqs[num];
                }
            });

            let modes = [];
            for (let num in freqs) {
                if (freqs[num] === maxFreq) {
                    modes.push(num);
                }
            }

            let resStr = "";
            if (maxFreq === 1 && arr.length > 1) {
                resStr = "No Mode (All numbers appear once)";
            } else {
                resStr = modes.join(', ') + ` (Appears ${maxFreq} times)`;
            }

            document.getElementById('mode-result').textContent = resStr;

            let explanation = `<p>Frequencies computed:</p><ul>`;
            for (let num in freqs) {
                explanation += `<li>Value <code>${num}</code>: appears ${freqs[num]} time(s)</li>`;
            }
            explanation += `</ul>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Statistics Tools",
        "name": "Range Calculator",
        "slug": "range-calculator",
        "desc": "Calculate the difference between the highest and lowest values in a statistical group.",
        "formula": "Max - Min",
        "formula_desc": "Subtracts the smallest number in the dataset from the largest number.",
        "icon": "📊",
        "inputs": [
            {"id": "range-vals", "label": "Comma-Separated Numbers:", "type": "textarea", "default": "12, 45, 8, 23, 75, 19"}
        ],
        "outputs": [
            {"id": "range-result", "label": "Range Value:", "type": "text"}
        ],
        "calc_js": """
            const raw = document.getElementById('range-vals').value;
            const arr = raw.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));

            if (!arr.length) {
                showToast("Please enter numbers.", "error");
                return;
            }

            const min = Math.min(...arr);
            const max = Math.max(...arr);
            const range = max - min;

            document.getElementById('range-result').textContent = range.toLocaleString();
            updateBreakdown(`<p>Maximum value: <strong>${max}</strong></p><p>Minimum value: <strong>${min}</strong></p><p>Range = <code>${max} - ${min}</code> = <strong>${range}</strong></p>`);
        """
    },
    {
        "category": "Statistics Tools",
        "name": "Standard Deviation Calculator",
        "slug": "standard-deviation-calculator-math",
        "desc": "Calculate population or sample standard deviation metrics for a set of numbers.",
        "formula": "sqrt(Sum((x - mean)^2) / N)",
        "formula_desc": "Measures statistical dispersion by squaring differences from the mean, averaging them, and taking the square root.",
        "icon": "📊",
        "inputs": [
            {"id": "sd-vals", "label": "Comma-Separated Numbers:", "type": "textarea", "default": "10, 12, 23, 23, 16, 23, 21, 16"},
            {"id": "sd-type", "label": "SD Type:", "type": "select", "options": [
                ["sample", "Sample SD (Denominator N - 1)"],
                ["population", "Population SD (Denominator N)"]
            ]}
        ],
        "outputs": [
            {"id": "sd-result", "label": "Standard Deviation:", "type": "text"}
        ],
        "calc_js": """
            const raw = document.getElementById('sd-vals').value;
            const type = document.getElementById('sd-type').value;
            const arr = raw.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));

            if (arr.length < 2) {
                showToast("Please enter at least 2 numbers.", "error");
                return;
            }

            const mean = arr.reduce((acc, curr) => acc + curr, 0) / arr.length;
            const sqDiffs = arr.map(v => Math.pow(v - mean, 2));
            const sumSqDiffs = sqDiffs.reduce((acc, curr) => acc + curr, 0);

            const denom = type === "sample" ? arr.length - 1 : arr.length;
            const variance = sumSqDiffs / denom;
            const sd = Math.sqrt(variance);

            document.getElementById('sd-result').textContent = sd.toLocaleString(undefined, {maximumFractionDigits: 6});

            let steps = `<p>Mean of dataset: <strong>${mean.toFixed(4)}</strong></p>`;
            steps += `<p>Sum of squared differences: <code>${sumSqDiffs.toFixed(4)}</code></p>`;
            steps += `<p>Variance (type: ${type}): <code>${sumSqDiffs.toFixed(4)} / ${denom}</code> = <strong>${variance.toFixed(4)}</strong></p>`;
            steps += `<p>SD = <code>sqrt(${variance.toFixed(4)})</code> = <strong>${sd.toFixed(6)}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Statistics Tools",
        "name": "Variance Calculator",
        "slug": "variance-calculator",
        "desc": "Calculate statistical variance of a list of numbers.",
        "formula": "Sum((x - mean)^2) / N",
        "formula_desc": "Evaluates standard variance (sample or population) to inspect spread metrics.",
        "icon": "📊",
        "inputs": [
            {"id": "var-vals", "label": "Comma-Separated Numbers:", "type": "textarea", "default": "4, 8, 12, 16, 20"},
            {"id": "var-type", "label": "Variance Type:", "type": "select", "options": [
                ["sample", "Sample Variance (N - 1)"],
                ["population", "Population Variance (N)"]
            ]}
        ],
        "outputs": [
            {"id": "var-result", "label": "Variance Value:", "type": "text"}
        ],
        "calc_js": """
            const raw = document.getElementById('var-vals').value;
            const type = document.getElementById('var-type').value;
            const arr = raw.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));

            if (arr.length < 2) {
                showToast("Please enter at least 2 numbers.", "error");
                return;
            }

            const mean = arr.reduce((acc, curr) => acc + curr, 0) / arr.length;
            const sqDiffs = arr.map(v => Math.pow(v - mean, 2));
            const sumSqDiffs = sqDiffs.reduce((acc, curr) => acc + curr, 0);

            const denom = type === "sample" ? arr.length - 1 : arr.length;
            const variance = sumSqDiffs / denom;

            document.getElementById('var-result').textContent = variance.toLocaleString(undefined, {maximumFractionDigits: 6});

            let steps = `<p>Mean of dataset: <strong>${mean.toFixed(4)}</strong></p>`;
            steps += `<p>Variance = <code>Sum((x - mean)²) / ${denom}</code> = <strong>${variance.toFixed(6)}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Statistics Tools",
        "name": "Probability Calculator",
        "slug": "probability-calculator-math",
        "desc": "Calculate single event probabilities, union, intersection, and conditional probability properties.",
        "formula": "P(A) = favorable outcomes / total outcomes",
        "formula_desc": "Computes standard fractional occurrences, or solves P(A union B) = P(A) + P(B) - P(A intersection B).",
        "icon": "📊",
        "inputs": [
            {"id": "prob-a", "label": "Probability of Event A (P(A), e.g. 0.5):", "type": "number", "default": "0.4"},
            {"id": "prob-b", "label": "Probability of Event B (P(B)):", "type": "number", "default": "0.5"},
            {"id": "prob-inter", "label": "Intersection P(A ∩ B) (If independent, leave blank):", "type": "number", "default": ""}
        ],
        "outputs": [
            {"id": "prob-union", "label": "Union P(A ∪ B):", "type": "text"},
            {"id": "prob-cond", "label": "Conditional P(A|B):", "type": "text"}
        ],
        "calc_js": """
            const pa = parseFloat(document.getElementById('prob-a').value);
            const pb = parseFloat(document.getElementById('prob-b').value);
            const pInterStr = document.getElementById('prob-inter').value.trim();

            if (isNaN(pa) || isNaN(pb) || pa < 0 || pa > 1 || pb < 0 || pb > 1) {
                showToast("Probabilities must be between 0 and 1.", "error");
                return;
            }

            let pInter = 0;
            let independent = false;
            if (pInterStr === "") {
                pInter = pa * pb; // assume independent
                independent = true;
            } else {
                pInter = parseFloat(pInterStr);
                if (isNaN(pInter) || pInter < 0 || pInter > Math.min(pa, pb)) {
                    showToast("Invalid intersection probability value.", "error");
                    return;
                }
            }

            const pUnion = pa + pb - pInter;
            const pCond = pb === 0 ? 0 : pInter / pb;

            document.getElementById('prob-union').textContent = pUnion.toFixed(4);
            document.getElementById('prob-cond').textContent = pCond.toFixed(4);

            let steps = `<p>P(A) = ${pa}, P(B) = ${pb}</p>`;
            if (independent) {
                steps += `<p>Assumed independent events: <code>P(A ∩ B) = P(A) * P(B) = ${pa} * ${pb}</code> = <strong>${pInter.toFixed(4)}</strong></p>`;
            } else {
                steps += `<p>Given intersection P(A ∩ B) = <strong>${pInter}</strong></p>`;
            }
            steps += `<p>P(A ∪ B) = <code>P(A) + P(B) - P(A ∩ B) = ${pa} + ${pb} - ${pInter.toFixed(4)}</code> = <strong>${pUnion.toFixed(4)}</strong></p>`;
            steps += `<p>P(A|B) = <code>P(A ∩ B) / P(B) = ${pInter.toFixed(4)} / ${pb}</code> = <strong>${pCond.toFixed(4)}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Statistics Tools",
        "name": "Percentile Calculator",
        "slug": "percentile-calculator",
        "desc": "Calculate the k-th percentile value of an input set of numbers.",
        "formula": "Interpolated rank position",
        "formula_desc": "Orders elements and finds target position index via linear interpolation logic.",
        "icon": "📊",
        "inputs": [
            {"id": "perc-vals", "label": "Comma-Separated Numbers:", "type": "textarea", "default": "15, 20, 35, 40, 50"},
            {"id": "perc-k", "label": "Percentile Rank k (0 to 100):", "type": "number", "default": "75"}
        ],
        "outputs": [
            {"id": "perc-result", "label": "Percentile Value:", "type": "text"}
        ],
        "calc_js": """
            const raw = document.getElementById('perc-vals').value;
            const k = parseFloat(document.getElementById('perc-k').value);
            const arr = raw.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));

            if (!arr.length || isNaN(k) || k < 0 || k > 100) {
                showToast("Please enter valid inputs (k between 0 and 100).", "error");
                return;
            }

            const sorted = [...arr].sort((a, b) => a - b);
            
            // Linear interpolation method
            const index = (k / 100) * (sorted.length - 1);
            const low = Math.floor(index);
            const high = Math.ceil(index);
            const val = sorted[low] + (index - low) * (sorted[high] - sorted[low]);

            document.getElementById('perc-result').textContent = val.toLocaleString(undefined, {maximumFractionDigits: 4});

            let steps = `<p>Sorted dataset: <code>[${sorted.join(', ')}]</code></p>`;
            steps += `<p>Rank index: <code>(${k} / 100) * (${sorted.length} - 1)</code> = <strong>${index.toFixed(4)}</strong></p>`;
            steps += `<p>Interpolated percentile value: <strong>${val}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Statistics Tools",
        "name": "Z-Score Calculator",
        "slug": "z-score-calculator",
        "desc": "Calculate standard score (z-score) indicating deviations from the mean.",
        "formula": "z = (x - mean) / SD",
        "formula_desc": "Measures how many standard deviations a value x is from the dataset mean.",
        "icon": "📊",
        "inputs": [
            {"id": "z-val", "label": "Raw Score x:", "type": "number", "default": "85"},
            {"id": "z-mean", "label": "Mean μ:", "type": "number", "default": "70"},
            {"id": "z-sd", "label": "Standard Deviation σ:", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "z-result", "label": "Z-Score:", "type": "text"}
        ],
        "calc_js": """
            const x = parseFloat(document.getElementById('z-val').value);
            const mean = parseFloat(document.getElementById('z-mean').value);
            const sd = parseFloat(document.getElementById('z-sd').value);

            if (isNaN(x) || isNaN(mean) || isNaN(sd)) {
                showToast("Please enter numbers.", "error");
                return;
            }
            if (sd <= 0) {
                showToast("Standard deviation must be positive.", "error");
                return;
            }

            const z = (x - mean) / sd;
            document.getElementById('z-result').textContent = z.toLocaleString(undefined, {maximumFractionDigits: 4});

            let explanation = `<p>Formula: <code>z = (x - μ) / σ</code></p>`;
            explanation += `<p>Calculation: <code>(${x} - ${mean}) / ${sd}</code> = <strong>${z.toFixed(4)}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Statistics Tools",
        "name": "Statistics Calculator",
        "slug": "statistics-calculator",
        "desc": "Perform comprehensive statistical analysis on a set of numbers.",
        "formula": "Aggregated statistical algorithms",
        "formula_desc": "Calculates mean, median, standard deviation, and variance in one pass.",
        "icon": "📊",
        "inputs": [
            {"id": "stat-vals", "label": "Comma-Separated Dataset:", "type": "textarea", "default": "2, 4, 4, 4, 5, 5, 7, 9"}
        ],
        "outputs": [
            {"id": "stat-mean", "label": "Mean:", "type": "text"},
            {"id": "stat-median", "label": "Median:", "type": "text"},
            {"id": "stat-sd", "label": "Sample SD:", "type": "text"}
        ],
        "calc_js": """
            const raw = document.getElementById('stat-vals').value;
            const arr = raw.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));

            if (arr.length < 2) {
                showToast("Please enter at least 2 numbers.", "error");
                return;
            }

            // Mean
            const mean = arr.reduce((acc, curr) => acc + curr, 0) / arr.length;

            // Median
            const sorted = [...arr].sort((a, b) => a - b);
            const mid = Math.floor(sorted.length / 2);
            const median = sorted.length % 2 !== 0 ? sorted[mid] : (sorted[mid - 1] + sorted[mid]) / 2;

            // SD
            const sqDiffs = arr.map(v => Math.pow(v - mean, 2));
            const sumSqDiffs = sqDiffs.reduce((acc, curr) => acc + curr, 0);
            const sd = Math.sqrt(sumSqDiffs / (arr.length - 1));

            document.getElementById('stat-mean').textContent = mean.toFixed(4).replace(/\\.0+$/, '');
            document.getElementById('stat-median').textContent = median.toLocaleString();
            document.getElementById('stat-sd').textContent = sd.toFixed(4).replace(/\\.0+$/, '');

            let steps = `<p>Total count: <strong>${arr.length}</strong></p>`;
            steps += `<p>Sorted list: <code>[${sorted.join(', ')}]</code></p>`;
            steps += `<p>Standard deviation: <strong>${sd.toFixed(6)}</strong></p>`;
            updateBreakdown(steps);
        """
    }
]

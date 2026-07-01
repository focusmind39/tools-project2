# -*- coding: utf-8 -*-
"""
Database of Basic Math Tools & Number Calculators (20 tools)
"""

BASIC_MATH_TOOLS = [
    {
        "category": "Basic Math Tools",
        "name": "Calculator",
        "slug": "calculator",
        "desc": "A clean, functional online calculator for basic arithmetic operations.",
        "formula": "Arithmetic expression evaluation",
        "formula_desc": "Evaluates standard algebraic order of operations (addition, subtraction, multiplication, division).",
        "icon": "🧮",
        "inputs": [
            {"id": "calc-expr", "label": "Enter Expression (e.g. 12 + 4 * 5):", "type": "text", "default": "100 / (12 - 2)"}
        ],
        "outputs": [
            {"id": "calc-result", "label": "Result:", "type": "text"}
        ],
        "calc_js": """
            const expr = document.getElementById('calc-expr').value.trim();
            if (!expr) {
                showToast("Please enter an expression to calculate.", "error");
                return;
            }
            // Sanitize inputs to allow only math tokens
            const sanitized = expr.replace(/[^0-9+\\-*/%().\\s]/g, '');
            try {
                const res = Function('"use strict";return (' + sanitized + ')')();
                document.getElementById('calc-result').textContent = Number(res).toLocaleString(undefined, {maximumFractionDigits: 6});
                
                let steps = `<p class='text-success'><strong>Calculation Successful!</strong></p>`;
                steps += `<p>Expression evaluated: <code>${sanitized}</code></p>`;
                steps += `<p>Result: <strong>${res}</strong></p>`;
                updateBreakdown(steps);
            } catch (err) {
                showToast("Invalid arithmetic expression.", "error");
            }
        """
    },
    {
        "category": "Basic Math Tools",
        "name": "Scientific Calculator",
        "slug": "scientific-calculator",
        "desc": "Perform advanced scientific operations like trigonometry, exponents, and logarithms.",
        "formula": "Extended math evaluation engine",
        "formula_desc": "Applies standard algebraic rules along with trigonometric, log, and exponential Math methods.",
        "icon": "🧪",
        "inputs": [
            {"id": "sci-expr", "label": "Scientific Expression (e.g. sin(pi/4) * sqrt(16)):", "type": "text", "default": "log(100) + sin(pi/6)"}
        ],
        "outputs": [
            {"id": "sci-result", "label": "Result:", "type": "text"}
        ],
        "calc_js": """
            const expr = document.getElementById('sci-expr').value.trim();
            if (!expr) {
                showToast("Please enter an expression.", "error");
                return;
            }
            // Map common functions to JS Math equivalents
            let jsExpr = expr.toLowerCase()
                .replace(/sin/g, 'Math.sin')
                .replace(/cos/g, 'Math.cos')
                .replace(/tan/g, 'Math.tan')
                .replace(/sqrt/g, 'Math.sqrt')
                .replace(/log/g, 'Math.log10')
                .replace(/ln/g, 'Math.log')
                .replace(/pi/g, 'Math.PI')
                .replace(/e/g, 'Math.E')
                .replace(/\\^/g, '**');

            const sanitized = jsExpr.replace(/[^a-zA-Z0-9+\\-*/%().\\s,*]/g, '');
            try {
                // Ensure only Math functions are executed
                if (/[a-zA-Z]/.test(sanitized.replace(/Math/g, ''))) {
                     throw new Error("Invalid tokens");
                }
                const res = Function('"use strict";return (' + sanitized + ')')();
                document.getElementById('sci-result').textContent = Number(res).toLocaleString(undefined, {maximumFractionDigits: 6});
                
                let steps = `<p class='text-success'><strong>Scientific Evaluation Complete</strong></p>`;
                steps += `<p>Parsed formula: <code>${sanitized}</code></p>`;
                steps += `<p>Result: <strong>${res}</strong></p>`;
                updateBreakdown(steps);
            } catch (err) {
                showToast("Invalid scientific expression.", "error");
            }
        """
    },
    {
        "category": "Basic Math Tools",
        "name": "Percentage Calculator",
        "slug": "percentage-calculator-math",
        "desc": "Calculate basic percentage values, increases, and differences instantly.",
        "formula": "Percentage standard formulas",
        "formula_desc": "Uses standard percentage formulas: (Part / Whole) * 100, or Change = ((New - Old) / Old) * 100.",
        "icon": "📊",
        "inputs": [
            {"id": "pct-type", "label": "Calculation Type:", "type": "select", "options": [
                ["value", "What is X% of Y?"],
                ["percent", "X is what percent of Y?"],
                ["change", "Percentage increase/decrease from X to Y?"]
            ]},
            {"id": "pct-x", "label": "Value X:", "type": "number", "default": "20"},
            {"id": "pct-y", "label": "Value Y:", "type": "number", "default": "250"}
        ],
        "outputs": [
            {"id": "pct-result", "label": "Percentage Output:", "type": "text"}
        ],
        "calc_js": """
            const type = document.getElementById('pct-type').value;
            const x = parseFloat(document.getElementById('pct-x').value);
            const y = parseFloat(document.getElementById('pct-y').value);

            if (isNaN(x) || isNaN(y)) {
                showToast("Please enter valid numeric inputs.", "error");
                return;
            }

            let res = 0;
            let explanation = "";

            if (type === "value") {
                res = (x / 100) * y;
                explanation = `<p>${x}% of ${y} is calculated as: <code>(${x} / 100) * ${y}</code> = <strong>${res}</strong></p>`;
            } else if (type === "percent") {
                if (y === 0) {
                    showToast("Value Y cannot be zero for percent calculation.", "error");
                    return;
                }
                res = (x / y) * 100;
                explanation = `<p>${x} is what percent of ${y} is calculated as: <code>(${x} / ${y}) * 100</code> = <strong>${res.toFixed(4)}%</strong></p>`;
            } else if (type === "change") {
                if (x === 0) {
                    showToast("Starting value X cannot be zero for percentage change.", "error");
                    return;
                }
                res = ((y - x) / x) * 100;
                const changeWord = res >= 0 ? "increase" : "decrease";
                explanation = `<p>Percentage change from ${x} to ${y} is: <code>((${y} - ${x}) / ${x}) * 100</code> = <strong>${res.toFixed(4)}%</strong> (${changeWord})</p>`;
            }

            document.getElementById('pct-result').textContent = res.toLocaleString(undefined, {maximumFractionDigits: 4}) + (type !== "value" ? "%" : "");
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Basic Math Tools",
        "name": "Fraction Calculator",
        "slug": "fraction-calculator",
        "desc": "Add, subtract, multiply, and divide fractions with simplified outputs.",
        "formula": "Fractions arithmetic algorithms",
        "formula_desc": "Finds a common denominator for additions and subtractions, and applies standard cross-multiplication for division.",
        "icon": "➗",
        "inputs": [
            {"id": "frac-n1", "label": "Fraction 1 Numerator:", "type": "number", "default": "1"},
            {"id": "frac-d1", "label": "Fraction 1 Denominator:", "type": "number", "default": "2"},
            {"id": "frac-op", "label": "Operator:", "type": "select", "options": [
                ["+", "Addition (+)"],
                ["-", "Subtraction (-)"],
                ["*", "Multiplication (*)"],
                ["/", "Division (/)"]
            ]},
            {"id": "frac-n2", "label": "Fraction 2 Numerator:", "type": "number", "default": "2"},
            {"id": "frac-d2", "label": "Fraction 2 Denominator:", "type": "number", "default": "3"}
        ],
        "outputs": [
            {"id": "frac-result", "label": "Result Fraction:", "type": "text"},
            {"id": "frac-decimal", "label": "Decimal Value:", "type": "text"}
        ],
        "calc_js": """
            const n1 = parseInt(document.getElementById('frac-n1').value);
            const d1 = parseInt(document.getElementById('frac-d1').value);
            const op = document.getElementById('frac-op').value;
            const n2 = parseInt(document.getElementById('frac-n2').value);
            const d2 = parseInt(document.getElementById('frac-d2').value);

            if (isNaN(n1) || isNaN(d1) || isNaN(n2) || isNaN(d2)) {
                showToast("Please enter integer numbers.", "error");
                return;
            }
            if (d1 === 0 || d2 === 0) {
                showToast("Denominators cannot be zero.", "error");
                return;
            }

            // Function to find Greatest Common Divisor
            function gcd(a, b) {
                return b ? gcd(b, a % b) : Math.abs(a);
            }

            let num = 0;
            let den = 1;

            if (op === "+") {
                num = n1 * d2 + n2 * d1;
                den = d1 * d2;
            } else if (op === "-") {
                num = n1 * d2 - n2 * d1;
                den = d1 * d2;
            } else if (op === "*") {
                num = n1 * n2;
                den = d1 * d2;
            } else if (op === "/") {
                if (n2 === 0) {
                    showToast("Cannot divide by zero fraction.", "error");
                    return;
                }
                num = n1 * d2;
                den = d1 * n2;
            }

            const divisor = gcd(num, den);
            const finalNum = num / divisor;
            const finalDen = den / divisor;
            const decVal = finalNum / finalDen;

            const resStr = finalDen === 1 ? `${finalNum}` : `${finalNum}/${finalDen}`;
            document.getElementById('frac-result').textContent = resStr;
            document.getElementById('frac-decimal').textContent = decVal.toFixed(6).replace(/\\.0+$/, '');

            let explanation = `<p>Original operation: <code>${n1}/${d1} ${op} ${n2}/${d2}</code></p>`;
            explanation += `<p>Common denominator calculation: <code>${num}/${den}</code></p>`;
            explanation += `<p>Simplified by dividing by Greatest Common Divisor (${divisor}): <strong>${resStr}</strong></p>`;
            explanation += `<p>Decimal value: <strong>${decVal}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Basic Math Tools",
        "name": "Decimal Calculator",
        "slug": "decimal-calculator",
        "desc": "Convert decimals to fractions or percentages and round them to selected decimals.",
        "formula": "Fractional base mapping",
        "formula_desc": "Multiplies by matching power of 10 to extract fraction form, then simplifies by finding the greatest common divisor.",
        "icon": "🔢",
        "inputs": [
            {"id": "dec-val", "label": "Decimal Number:", "type": "text", "default": "0.375"},
            {"id": "dec-round", "label": "Round To (Places):", "type": "number", "default": "2"}
        ],
        "outputs": [
            {"id": "dec-frac", "label": "Fraction Equivalent:", "type": "text"},
            {"id": "dec-pct", "label": "Percent Equivalent:", "type": "text"},
            {"id": "dec-rounded", "label": "Rounded Value:", "type": "text"}
        ],
        "calc_js": """
            const valStr = document.getElementById('dec-val').value.trim();
            const precision = parseInt(document.getElementById('dec-round').value);
            const val = parseFloat(valStr);

            if (isNaN(val) || isNaN(precision)) {
                showToast("Please enter a valid decimal number.", "error");
                return;
            }

            // Convert to fraction
            const len = (valStr.split('.')[1] || '').length;
            const den = Math.pow(10, len);
            const num = Math.round(val * den);

            function gcd(a, b) {
                return b ? gcd(b, a % b) : Math.abs(a);
            }
            const divisor = gcd(num, den);
            const simpNum = num / divisor;
            const simpDen = den / divisor;

            const roundedVal = val.toFixed(precision);
            const pctVal = (val * 100).toFixed(4).replace(/\\.0+$/, '') + "%";

            document.getElementById('dec-frac').textContent = `${simpNum}/${simpDen}`;
            document.getElementById('dec-pct').textContent = pctVal;
            document.getElementById('dec-rounded').textContent = roundedVal;

            let explanation = `<p>Decimal input: <strong>${val}</strong></p>`;
            explanation += `<p>Base fraction: <code>${num} / ${den}</code></p>`;
            explanation += `<p>Greatest Common Divisor is <code>${divisor}</code>. Simplified fraction: <strong>${simpNum}/${simpDen}</strong></p>`;
            explanation += `<p>Percentage equivalence: <code>${val} * 100</code> = <strong>${pctVal}</strong></p>`;
            explanation += `<p>Rounded value (to ${precision} places): <strong>${roundedVal}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Basic Math Tools",
        "name": "Ratio Calculator",
        "slug": "ratio-calculator",
        "desc": "Simplify a ratio A:B, or solve ratio equations like A:B = C:D for missing terms.",
        "formula": "Equilateral ratio proportion solver",
        "formula_desc": "Solves D = (C * B) / A when C is given, or simplifies ratios using Greatest Common Divisor.",
        "icon": "⚖️",
        "inputs": [
            {"id": "ratio-a", "label": "Ratio Term A:", "type": "number", "default": "4"},
            {"id": "ratio-b", "label": "Ratio Term B:", "type": "number", "default": "6"},
            {"id": "ratio-c", "label": "Ratio Term C (Leave blank to simplify A:B):", "type": "number", "default": ""}
        ],
        "outputs": [
            {"id": "ratio-simp", "label": "Simplified / Solved Term D:", "type": "text"}
        ],
        "calc_js": """
            const a = parseFloat(document.getElementById('ratio-a').value);
            const b = parseFloat(document.getElementById('ratio-b').value);
            const cStr = document.getElementById('ratio-c').value.trim();

            if (isNaN(a) || isNaN(b) || a === 0) {
                showToast("Please enter non-zero values for A and B.", "error");
                return;
            }

            let result = "";
            let explanation = "";

            if (cStr === "") {
                // Simplify A:B
                function gcd(x, y) {
                    return y ? gcd(y, x % y) : Math.abs(x);
                }
                const divisor = gcd(a, b);
                result = `${a / divisor} : ${b / divisor}`;
                explanation = `<p>Simplifying ratio <code>${a} : ${b}</code> by dividing by GCD (${divisor}) yields <strong>${result}</strong></p>`;
            } else {
                const c = parseFloat(cStr);
                if (isNaN(c)) {
                    showToast("Please enter a valid numeric value for term C.", "error");
                    return;
                }
                const d = (c * b) / a;
                result = d.toLocaleString(undefined, {maximumFractionDigits: 6});
                explanation = `<p>Solving <code>${a} : ${b} = ${c} : D</code></p>`;
                explanation += `<p>Formula: <code>D = (C * B) / A</code></p>`;
                explanation += `<p>Calculation: <code>(${c} * ${b}) / ${a}</code> = <strong>${d}</strong></p>`;
            }

            document.getElementById('ratio-simp').textContent = result;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Basic Math Tools",
        "name": "Proportion Calculator",
        "slug": "proportion-calculator",
        "desc": "Solve for missing variables in proportional values format A/B = C/D.",
        "formula": "Cross-multiplication proportion algebra",
        "formula_desc": "Solves any missing value by cross-multiplying and dividing by the remaining variable.",
        "icon": "⚖️",
        "inputs": [
            {"id": "prop-a", "label": "Term A (Upper Left):", "type": "text", "default": "10"},
            {"id": "prop-b", "label": "Term B (Lower Left):", "type": "text", "default": "20"},
            {"id": "prop-c", "label": "Term C (Upper Right):", "type": "text", "default": "x"},
            {"id": "prop-d", "label": "Term D (Lower Right):", "type": "text", "default": "50"}
        ],
        "outputs": [
            {"id": "prop-result", "label": "Solved Variable Value:", "type": "text"}
        ],
        "calc_js": """
            let a = document.getElementById('prop-a').value.trim().toLowerCase();
            let b = document.getElementById('prop-b').value.trim().toLowerCase();
            let c = document.getElementById('prop-c').value.trim().toLowerCase();
            let d = document.getElementById('prop-d').value.trim().toLowerCase();

            let missingCount = 0;
            let missingVar = '';
            if (a === 'x' || a === '') { missingCount++; missingVar = 'A'; }
            if (b === 'x' || b === '') { missingCount++; missingVar = 'B'; }
            if (c === 'x' || c === '') { missingCount++; missingVar = 'C'; }
            if (d === 'x' || d === '') { missingCount++; missingVar = 'D'; }

            if (missingCount !== 1) {
                showToast("Please enter numbers in exactly three inputs and leave one input as 'x' or blank.", "error");
                return;
            }

            let solved = 0;
            let step = "";

            if (missingVar === 'A') {
                const bVal = parseFloat(b); const cVal = parseFloat(c); const dVal = parseFloat(d);
                if (dVal === 0) { showToast("Denominator D cannot be zero.", "error"); return; }
                solved = (bVal * cVal) / dVal;
                step = `A = (B * C) / D = (${bVal} * ${cVal}) / ${dVal}`;
            } else if (missingVar === 'B') {
                const aVal = parseFloat(a); const cVal = parseFloat(c); const dVal = parseFloat(d);
                if (cVal === 0) { showToast("Term C cannot be zero.", "error"); return; }
                solved = (aVal * dVal) / cVal;
                step = `B = (A * D) / C = (${aVal} * ${dVal}) / ${cVal}`;
            } else if (missingVar === 'C') {
                const aVal = parseFloat(a); const bVal = parseFloat(b); const dVal = parseFloat(d);
                if (bVal === 0) { showToast("Denominator B cannot be zero.", "error"); return; }
                solved = (aVal * dVal) / bVal;
                step = `C = (A * D) / B = (${aVal} * ${dVal}) / ${bVal}`;
            } else if (missingVar === 'D') {
                const aVal = parseFloat(a); const bVal = parseFloat(b); const cVal = parseFloat(c);
                if (aVal === 0) { showToast("Term A cannot be zero.", "error"); return; }
                solved = (bVal * cVal) / aVal;
                step = `D = (B * C) / A = (${bVal} * ${cVal}) / ${aVal}`;
            }

            document.getElementById('prop-result').textContent = solved.toLocaleString(undefined, {maximumFractionDigits: 6});
            updateBreakdown(`<p>Solved variable <strong>${missingVar}</strong></p><p>Formula: <code>${step}</code> = <strong>${solved}</strong></p>`);
        """
    },
    {
        "category": "Basic Math Tools",
        "name": "Average Calculator",
        "slug": "average-calculator",
        "desc": "Find the sum, count, and average value of a series of numbers.",
        "formula": "Sum of values / total count",
        "formula_desc": "Adds all listed input numbers together and divides by the total number count.",
        "icon": "📈",
        "inputs": [
            {"id": "avg-vals", "label": "Comma-Separated Numbers:", "type": "textarea", "default": "12, 15, 23, 42, 8, 19"}
        ],
        "outputs": [
            {"id": "avg-sum", "label": "Sum:", "type": "text"},
            {"id": "avg-count", "label": "Count:", "type": "text"},
            {"id": "avg-result", "label": "Average:", "type": "text"}
        ],
        "calc_js": """
            const raw = document.getElementById('avg-vals').value;
            const arr = raw.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));
            if (!arr.length) {
                showToast("Please provide at least one valid number.", "error");
                return;
            }

            const sum = arr.reduce((acc, curr) => acc + curr, 0);
            const count = arr.length;
            const avg = sum / count;

            document.getElementById('avg-sum').textContent = sum.toLocaleString();
            document.getElementById('avg-count').textContent = count.toLocaleString();
            document.getElementById('avg-result').textContent = avg.toLocaleString(undefined, {maximumFractionDigits: 4});

            let steps = `<p>Numbers processed: <code>[${arr.join(', ')}]</code></p>`;
            steps += `<p>Sum calculation: <code>${arr.join(' + ')}</code> = <strong>${sum}</strong></p>`;
            steps += `<p>Average calculation: <code>${sum} / ${count}</code> = <strong>${avg}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Basic Math Tools",
        "name": "Mean Calculator",
        "slug": "mean-calculator",
        "desc": "Calculate Arithmetic Mean, Geometric Mean, and Harmonic Mean of a group of numbers.",
        "formula": "Multiple mean representations",
        "formula_desc": "Computes arithmetic (sum/N), geometric (product^(1/N)), and harmonic (N/sum(1/x)) means.",
        "icon": "📐",
        "inputs": [
            {"id": "mean-vals", "label": "Comma-Separated Values (positive numbers for geometric/harmonic):", "type": "textarea", "default": "4, 8, 16, 23, 42"}
        ],
        "outputs": [
            {"id": "mean-arith", "label": "Arithmetic Mean:", "type": "text"},
            {"id": "mean-geom", "label": "Geometric Mean:", "type": "text"},
            {"id": "mean-harm", "label": "Harmonic Mean:", "type": "text"}
        ],
        "calc_js": """
            const raw = document.getElementById('mean-vals').value;
            const arr = raw.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));
            if (!arr.length) {
                showToast("Please enter numbers.", "error");
                return;
            }

            // Arithmetic
            const sum = arr.reduce((acc, curr) => acc + curr, 0);
            const arMean = sum / arr.length;

            // Geometric
            let geMean = 0;
            const hasNegative = arr.some(v => v <= 0);
            if (!hasNegative) {
                const logSum = arr.reduce((acc, curr) => acc + Math.log(curr), 0);
                geMean = Math.exp(logSum / arr.length);
            }

            // Harmonic
            let harMean = 0;
            if (!hasNegative) {
                const invSum = arr.reduce((acc, curr) => acc + (1 / curr), 0);
                harMean = arr.length / invSum;
            }

            document.getElementById('mean-arith').textContent = arMean.toFixed(4).replace(/\\.0+$/, '');
            document.getElementById('mean-geom').textContent = hasNegative ? "N/A (Non-positive value)" : geMean.toFixed(4).replace(/\\.0+$/, '');
            document.getElementById('mean-harm').textContent = hasNegative ? "N/A (Non-positive value)" : harMean.toFixed(4).replace(/\\.0+$/, '');

            let explanation = `<p>Dataset: <code>[${arr.join(', ')}]</code></p>`;
            explanation += `<p>Arithmetic Mean = <code>(${arr.join(' + ')}) / ${arr.length}</code> = <strong>${arMean.toFixed(4)}</strong></p>`;
            if (!hasNegative) {
                explanation += `<p>Geometric Mean = <code>(${arr.join(' * ')})^(1/${arr.length})</code> = <strong>${geMean.toFixed(4)}</strong></p>`;
                explanation += `<p>Harmonic Mean = <code>${arr.length} / (${arr.map(x => `1/${x}`).join(' + ')})</code> = <strong>${harMean.toFixed(4)}</strong></p>`;
            }
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Basic Math Tools",
        "name": "Weighted Average Calculator",
        "slug": "weighted-average-calculator",
        "desc": "Calculate the weighted average of values associated with different weights.",
        "formula": "Sum(value * weight) / Sum(weight)",
        "formula_desc": "Multiplies each value by its weight, sums the results, and divides by the sum of all weights.",
        "icon": "⚖️",
        "inputs": [
            {"id": "w-vals", "label": "Comma-Separated Values:", "type": "text", "default": "90, 80, 70"},
            {"id": "w-weights", "label": "Comma-Separated Weights:", "type": "text", "default": "1, 2, 3"}
        ],
        "outputs": [
            {"id": "w-result", "label": "Weighted Average:", "type": "text"}
        ],
        "calc_js": """
            const vals = document.getElementById('w-vals').value.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));
            const weights = document.getElementById('w-weights').value.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));

            if (vals.length !== weights.length || !vals.length) {
                showToast("Values count must exactly match weights count.", "error");
                return;
            }

            let sumProducts = 0;
            let sumWeights = 0;
            let stepStr = [];

            for (let i = 0; i < vals.length; i++) {
                sumProducts += vals[i] * weights[i];
                sumWeights += weights[i];
                stepStr.push(`(${vals[i]} * ${weights[i]})`);
            }

            if (sumWeights === 0) {
                showToast("Sum of weights cannot be zero.", "error");
                return;
            }

            const wAvg = sumProducts / sumWeights;
            document.getElementById('w-result').textContent = wAvg.toFixed(4).replace(/\\.0+$/, '');

            let explanation = `<p>Weighted values: <code>${stepStr.join(' + ')}</code> = <strong>${sumProducts}</strong></p>`;
            explanation += `<p>Total weight: <code>${sumWeights}</code></p>`;
            explanation += `<p>Weighted Average: <code>${sumProducts} / ${sumWeights}</code> = <strong>${wAvg.toFixed(4)}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Number Calculators",
        "name": "Prime Number Checker",
        "slug": "prime-number-checker",
        "desc": "Check if a number is prime and retrieve its divisor breakdown.",
        "formula": "Trial division square root boundary",
        "formula_desc": "Checks odd divisors up to the square root of the target integer value.",
        "icon": "🔢",
        "inputs": [
            {"id": "prime-val", "label": "Integer Number to Check:", "type": "number", "default": "7919"}
        ],
        "outputs": [
            {"id": "prime-status", "label": "Is Prime:", "type": "text"},
            {"id": "prime-factors", "label": "Factors:", "type": "text"}
        ],
        "calc_js": """
            const num = parseInt(document.getElementById('prime-val').value);
            if (isNaN(num) || num <= 1) {
                document.getElementById('prime-status').textContent = "No";
                document.getElementById('prime-factors').textContent = "None";
                showToast("Please enter an integer greater than 1.", "error");
                return;
            }

            let isPrime = true;
            let factors = [];
            
            // Gather factors
            for (let i = 1; i <= Math.sqrt(num); i++) {
                if (num % i === 0) {
                    factors.push(i);
                    if (i !== num / i) {
                        factors.push(num / i);
                    }
                }
            }
            factors.sort((a, b) => a - b);
            isPrime = factors.length === 2;

            document.getElementById('prime-status').textContent = isPrime ? "Yes" : "No";
            document.getElementById('prime-factors').textContent = factors.join(', ');

            let steps = `<p>Target number: <strong>${num}</strong></p>`;
            if (isPrime) {
                steps += `<p class='text-success'><strong>This number is prime!</strong> It is only divisible by 1 and itself.</p>`;
            } else {
                steps += `<p class='text-danger'><strong>This number is composite!</strong> Found factors: <code>[${factors.join(', ')}]</code></p>`;
            }
            updateBreakdown(steps);
        """
    },
    {
        "category": "Number Calculators",
        "name": "Prime Number Generator",
        "slug": "prime-number-generator",
        "desc": "Generate a list of prime numbers within a specified boundary range.",
        "formula": "Sieve of Eratosthenes algorithm",
        "formula_desc": "Flags non-primes progressively for all values starting from two up to the range maximum value.",
        "icon": "🔢",
        "inputs": [
            {"id": "prime-start", "label": "Start Number:", "type": "number", "default": "1"},
            {"id": "prime-limit", "label": "End Limit (Max 50000):", "type": "number", "default": "100"}
        ],
        "outputs": [
            {"id": "prime-gen-list", "label": "Primes Found:", "type": "textarea"},
            {"id": "prime-gen-count", "label": "Total Primes Count:", "type": "text"}
        ],
        "calc_js": """
            const start = parseInt(document.getElementById('prime-start').value);
            const limit = parseInt(document.getElementById('prime-limit').value);

            if (isNaN(start) || isNaN(limit) || start < 1 || limit < start) {
                showToast("Invalid range boundaries.", "error");
                return;
            }
            if (limit > 50000) {
                showToast("Maximum generator limit is 50,000.", "error");
                return;
            }

            // Sieve of Eratosthenes
            let sieve = new Array(limit + 1).fill(true);
            sieve[0] = sieve[1] = false;
            for (let i = 2; i * i <= limit; i++) {
                if (sieve[i]) {
                    for (let j = i * i; j <= limit; j += i) {
                        sieve[j] = false;
                    }
                }
            }

            let primes = [];
            for (let i = Math.max(2, start); i <= limit; i++) {
                if (sieve[i]) primes.push(i);
            }

            document.getElementById('prime-gen-list').value = primes.join(', ');
            document.getElementById('prime-gen-count').textContent = primes.length.toLocaleString();

            let explanation = `<p>Found <strong>${primes.length}</strong> prime numbers between ${start} and ${limit}.</p>`;
            explanation += `<p>Primes: <code>${primes.slice(0, 10).join(', ')}${primes.length > 10 ? '...' : ''}</code></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Number Calculators",
        "name": "Even Odd Checker",
        "slug": "even-odd-checker",
        "desc": "Quickly verify if an integer is even or odd.",
        "formula": "Modulo 2 division",
        "formula_desc": "Checks if the remainder of the division of the number by 2 is zero.",
        "icon": "⚖️",
        "inputs": [
            {"id": "eo-num", "label": "Enter Integer:", "type": "number", "default": "45281"}
        ],
        "outputs": [
            {"id": "eo-result", "label": "Result:", "type": "text"}
        ],
        "calc_js": """
            const val = parseInt(document.getElementById('eo-num').value);
            if (isNaN(val)) {
                showToast("Please enter an integer.", "error");
                return;
            }

            const isEven = val % 2 === 0;
            const res = isEven ? "Even" : "Odd";
            document.getElementById('eo-result').textContent = res;

            let nextNums = [];
            for (let i = 1; i <= 5; i++) {
                nextNums.push(val + (i * 2));
            }

            let steps = `<p>Number: <strong>${val}</strong></p>`;
            steps += `<p>Calculation: <code>${val} % 2</code> = <strong>${Math.abs(val % 2)}</strong></p>`;
            steps += `<p>Since remainder is ${isEven ? 'zero' : 'one'}, the number is <strong>${res}</strong>.</p>`;
            steps += `<p>Next 5 matching ${res} numbers: <code>${nextNums.join(', ')}</code></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Number Calculators",
        "name": "Number To Words Converter",
        "slug": "number-to-words-converter",
        "desc": "Convert numbers to their English word representation.",
        "formula": "Linguistic scale parsing",
        "formula_desc": "Splits numbers into hundreds, thousands, and millions blocks to convert numbers to word groups.",
        "icon": "📝",
        "inputs": [
            {"id": "n2w-val", "label": "Number (Max 999 Trillion):", "type": "number", "default": "1234567"}
        ],
        "outputs": [
            {"id": "n2w-words", "label": "Words Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = parseInt(document.getElementById('n2w-val').value);
            if (isNaN(val)) {
                showToast("Please enter a valid number.", "error");
                return;
            }

            const ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
            const tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
            const scales = ["", "thousand", "million", "billion", "trillion"];

            function convertSection(num) {
                let s = "";
                if (num >= 100) {
                    s += ones[Math.floor(num / 100)] + " hundred ";
                    num %= 100;
                }
                if (num >= 20) {
                    s += tens[Math.floor(num / 10)] + " ";
                    num %= 10;
                }
                if (num > 0) {
                    s += ones[num] + " ";
                }
                return s.trim();
            }

            function convert(num) {
                if (num === 0) return "zero";
                let isNeg = num < 0;
                num = Math.abs(num);

                let words = "";
                let scaleIdx = 0;

                while (num > 0) {
                    let part = num % 1000;
                    if (part > 0) {
                        let partWords = convertSection(part);
                        words = partWords + " " + scales[scaleIdx] + " " + words;
                    }
                    num = Math.floor(num / 1000);
                    scaleIdx++;
                }

                return (isNeg ? "negative " : "") + words.trim();
            }

            const result = convert(val);
            document.getElementById('n2w-words').value = result.charAt(0).toUpperCase() + result.slice(1);
            updateBreakdown(`<p>Number converted: <strong>${val}</strong></p><p>Text result: <em>${result}</em></p>`);
        """
    },
    {
        "category": "Number Calculators",
        "name": "Words To Number Converter",
        "slug": "words-to-number-converter",
        "desc": "Translate written English words into numeric digits.",
        "formula": "Linguistic value synthesis",
        "formula_desc": "Maps matching nouns to integer scales (hundred, thousand, million) and compiles cumulative sums.",
        "icon": "📝",
        "inputs": [
            {"id": "w2n-text", "label": "Number in English Words:", "type": "textarea", "default": "Two million three hundred forty-five thousand six hundred seventy-eight"}
        ],
        "outputs": [
            {"id": "w2n-result", "label": "Digits Output:", "type": "text"}
        ],
        "calc_js": """
            const words = document.getElementById('w2n-text').value.trim();
            if (!words) {
                showToast("Please enter numbers in words.", "error");
                return;
            }

            const numMap = {
                "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
                "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
                "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40,
                "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
            };
            const scaleMap = {
                "hundred": 100, "thousand": 1000, "million": 1000000, "billion": 1000000000, "trillion": 1000000000000
            };

            const cleanWords = words.toLowerCase().replace(/-/g, ' ').replace(/ and /g, ' ').split(/\\s+/);
            
            let total = 0;
            let current = 0;
            let isNeg = cleanWords[0] === "negative";

            for (let i = isNeg ? 1 : 0; i < cleanWords.length; i++) {
                const w = cleanWords[i];
                if (numMap[w] !== undefined) {
                    current += numMap[w];
                } else if (w === "hundred") {
                    current *= 100;
                } else if (scaleMap[w] !== undefined) {
                    current *= scaleMap[w];
                    total += current;
                    current = 0;
                } else if (w !== "") {
                    showToast("Unrecognized number term: " + w, "error");
                    return;
                }
            }
            total += current;
            if (isNeg) total = -total;

            document.getElementById('w2n-result').textContent = total.toLocaleString();
            updateBreakdown(`<p>Input text: <em>${words}</em></p><p>Numeric result: <strong>${total}</strong></p>`);
        """
    },
    {
        "category": "Number Calculators",
        "name": "Number Sequence Generator",
        "slug": "number-sequence-generator",
        "desc": "Generate custom arithmetic or geometric series progression listings.",
        "formula": "Recursive progression functions",
        "formula_desc": "Recursively adds the step constant or multiplies by the ratio variable step-by-step.",
        "icon": "🔢",
        "inputs": [
            {"id": "seq-start", "label": "Start Number A:", "type": "number", "default": "5"},
            {"id": "seq-factor", "label": "Step / Ratio Value:", "type": "number", "default": "3"},
            {"id": "seq-count", "label": "Numbers to Generate:", "type": "number", "default": "15"},
            {"id": "seq-type", "label": "Sequence Type:", "type": "select", "options": [
                ["arithmetic", "Arithmetic (+)"],
                ["geometric", "Geometric (*)"]
            ]}
        ],
        "outputs": [
            {"id": "seq-list", "label": "Generated Sequence:", "type": "textarea"}
        ],
        "calc_js": """
            const start = parseFloat(document.getElementById('seq-start').value);
            const factor = parseFloat(document.getElementById('seq-factor').value);
            const count = parseInt(document.getElementById('seq-count').value);
            const type = document.getElementById('seq-type').value;

            if (isNaN(start) || isNaN(factor) || isNaN(count) || count <= 0) {
                showToast("Please enter valid numeric parameters.", "error");
                return;
            }
            if (count > 1000) {
                showToast("Maximum sequence length is 1000.", "error");
                return;
            }

            let seq = [];
            let current = start;

            for (let i = 0; i < count; i++) {
                seq.push(current);
                if (type === "arithmetic") {
                    current += factor;
                } else {
                    current *= factor;
                }
            }

            document.getElementById('seq-list').value = seq.join(', ');

            let steps = `<p>Sequence Type: <strong>${type.toUpperCase()}</strong></p>`;
            steps += `<p>Formula: <code>${type === 'arithmetic' ? 'A_n = A + n*d' : 'A_n = A * r^n'}</code></p>`;
            steps += `<p>Generated list values: <code>[${seq.slice(0, 5).join(', ')}${seq.length > 5 ? ', ...' : ''}]</code></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Number Calculators",
        "name": "Number Pattern Generator",
        "slug": "number-pattern-generator",
        "desc": "Generate famous mathematical sequences like Fibonacci, square, and triangular patterns.",
        "formula": "Standard mathematical sequence formulas",
        "formula_desc": "Uses mathematical formulas (e.g. F_n = F_{n-1} + F_{n-2} for Fibonacci) to build number series.",
        "icon": "🧬",
        "inputs": [
            {"id": "pat-type", "label": "Pattern Type:", "type": "select", "options": [
                ["fibonacci", "Fibonacci Sequence"],
                ["squares", "Square Numbers (n^2)"],
                ["cubes", "Cube Numbers (n^3)"],
                ["triangular", "Triangular Numbers (n*(n+1)/2)"]
            ]},
            {"id": "pat-count", "label": "Count (Max 500):", "type": "number", "default": "20"}
        ],
        "outputs": [
            {"id": "pat-list", "label": "Generated Pattern:", "type": "textarea"}
        ],
        "calc_js": """
            const type = document.getElementById('pat-type').value;
            const count = parseInt(document.getElementById('pat-count').value);

            if (isNaN(count) || count <= 0) {
                showToast("Please enter a valid count.", "error");
                return;
            }
            if (count > 500) {
                showToast("Maximum limit is 500 elements.", "error");
                return;
            }

            let seq = [];

            if (type === "fibonacci") {
                let a = 0, b = 1;
                for (let i = 0; i < count; i++) {
                    seq.push(a);
                    let temp = a + b;
                    a = b;
                    b = temp;
                }
            } else if (type === "squares") {
                for (let i = 1; i <= count; i++) {
                    seq.push(i * i);
                }
            } else if (type === "cubes") {
                for (let i = 1; i <= count; i++) {
                    seq.push(i * i * i);
                }
            } else if (type === "triangular") {
                for (let i = 1; i <= count; i++) {
                    seq.push((i * (i + 1)) / 2);
                }
            }

            document.getElementById('pat-list').value = seq.join(', ');
            updateBreakdown(`<p>Pattern: <strong>${type}</strong> generated with ${count} numbers.</p>`);
        """
    },
    {
        "category": "Number Calculators",
        "name": "Number Comparator",
        "slug": "number-comparator",
        "desc": "Compare multiple numbers to find minimum, maximum, and sort them.",
        "formula": "Array sorting and bounds checks",
        "formula_desc": "Analyzes numeric values using min/max logic and sorts elements in ascending or descending sequence.",
        "icon": "⚖️",
        "inputs": [
            {"id": "comp-nums", "label": "Comma-Separated Numbers:", "type": "textarea", "default": "45, -12, 88.5, 0, 102, -5.2"}
        ],
        "outputs": [
            {"id": "comp-min", "label": "Minimum Value:", "type": "text"},
            {"id": "comp-max", "label": "Maximum Value:", "type": "text"},
            {"id": "comp-asc", "label": "Sorted Ascending:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('comp-nums').value;
            const arr = raw.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));

            if (!arr.length) {
                showToast("Please provide numeric values.", "error");
                return;
            }

            const min = Math.min(...arr);
            const max = Math.max(...arr);
            const asc = [...arr].sort((a, b) => a - b);
            const desc = [...arr].sort((a, b) => b - a);

            document.getElementById('comp-min').textContent = min;
            document.getElementById('comp-max').textContent = max;
            document.getElementById('comp-asc').value = asc.join(', ');

            let steps = `<p>Min value: <strong>${min}</strong></p>`;
            steps += `<p>Max value: <strong>${max}</strong></p>`;
            steps += `<p>Sorted Ascending: <code>[${asc.join(', ')}]</code></p>`;
            steps += `<p>Sorted Descending: <code>[${desc.join(', ')}]</code></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Number Calculators",
        "name": "Number Splitter",
        "slug": "number-splitter",
        "desc": "Split numbers into place values or generate their prime factorization.",
        "formula": "Positional digits split and divisor loop",
        "formula_desc": "Extracts digit weights (10^n place values) and divides targets progressively by prime factors.",
        "icon": "🪓",
        "inputs": [
            {"id": "split-val", "label": "Positive Integer Number:", "type": "number", "default": "4582"}
        ],
        "outputs": [
            {"id": "split-place", "label": "Place Value Breakdown:", "type": "textarea"},
            {"id": "split-factor", "label": "Prime Factorization:", "type": "text"}
        ],
        "calc_js": """
            const num = parseInt(document.getElementById('split-val').value);
            if (isNaN(num) || num <= 0) {
                showToast("Please enter a positive integer.", "error");
                return;
            }

            // Digit place value breakdown
            const digits = num.toString().split('');
            let placeVals = [];
            for (let i = 0; i < digits.length; i++) {
                const weight = Math.pow(10, digits.length - 1 - i);
                const val = parseInt(digits[i]) * weight;
                if (val > 0) {
                    placeVals.push(`${digits[i]} * ${weight} (${val})`);
                }
            }

            // Prime factorization
            let temp = num;
            let pFactors = [];
            let divisor = 2;
            while (temp >= 2) {
                if (temp % divisor === 0) {
                    pFactors.push(divisor);
                    temp /= divisor;
                } else {
                    divisor++;
                }
            }

            document.getElementById('split-place').value = placeVals.join(' + \\n');
            document.getElementById('split-factor').textContent = pFactors.join(' * ');

            let steps = `<p>Input Number: <strong>${num}</strong></p>`;
            steps += `<p>Place value expansion: <code>${placeVals.map(x => x.split(' ')[0]).join(' + ')}</code></p>`;
            steps += `<p>Prime factors: <code>${pFactors.join(' * ')}</code> = <strong>${num}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Number Calculators",
        "name": "Number Joiner",
        "slug": "number-joiner",
        "desc": "Join separate digits or comma-separated number items into a single integer using custom separators.",
        "formula": "String collection join",
        "formula_desc": "Combines numeric string arrays using custom separation rules and parses output values.",
        "icon": "🔗",
        "inputs": [
            {"id": "join-vals", "label": "Digits or Numbers to Join:", "type": "text", "default": "4, 8, 15, 16, 23, 42"},
            {"id": "join-sep", "label": "Separator (Leave empty for none):", "type": "text", "default": ""}
        ],
        "outputs": [
            {"id": "join-result", "label": "Joined String:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('join-vals').value.trim();
            const sep = document.getElementById('join-sep').value;
            const items = raw.split(',').map(v => v.trim()).filter(v => v !== "");

            if (!items.length) {
                showToast("Please enter numbers.", "error");
                return;
            }

            const joined = items.join(sep);
            document.getElementById('join-result').value = joined;

            let steps = `<p>Input items count: <strong>${items.length}</strong></p>`;
            steps += `<p>Separator: <code>"${sep}"</code></p>`;
            steps += `<p>Result: <strong>${joined}</strong></p>`;
            updateBreakdown(steps);
        """
    }
]

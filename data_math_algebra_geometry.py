# -*- coding: utf-8 -*-
"""
Database of Algebra Tools & Geometry Tools (20 tools)
"""

ALGEBRA_GEOMETRY_TOOLS = [
    {
        "category": "Algebra Tools",
        "name": "Algebra Calculator",
        "slug": "algebra-calculator",
        "desc": "Evaluate linear and basic algebraic expressions step-by-step.",
        "formula": "Linear equation reduction ax + b = c",
        "formula_desc": "Solves for x by performing variable isolation arithmetic operations.",
        "icon": "📐",
        "inputs": [
            {"id": "alg-a", "label": "Coefficient a (for ax + b = c):", "type": "number", "default": "3"},
            {"id": "alg-b", "label": "Constant b:", "type": "number", "default": "5"},
            {"id": "alg-c", "label": "Target value c:", "type": "number", "default": "17"}
        ],
        "outputs": [
            {"id": "alg-x", "label": "Value of x:", "type": "text"}
        ],
        "calc_js": """
            const a = parseFloat(document.getElementById('alg-a').value);
            const b = parseFloat(document.getElementById('alg-b').value);
            const c = parseFloat(document.getElementById('alg-c').value);

            if (isNaN(a) || isNaN(b) || isNaN(c)) {
                showToast("Please enter numbers.", "error");
                return;
            }
            if (a === 0) {
                showToast("Coefficient 'a' cannot be zero.", "error");
                return;
            }

            const x = (c - b) / a;
            document.getElementById('alg-x').textContent = x.toLocaleString(undefined, {maximumFractionDigits: 6});

            let explanation = `<p>Equation: <code>${a}x + ${b} = ${c}</code></p>`;
            explanation += `<p>Step 1: Subtract ${b} from both sides: <code>${a}x = ${c} - ${b}</code> => <code>${a}x = ${c - b}</code></p>`;
            explanation += `<p>Step 2: Divide by ${a}: <code>x = ${c - b} / ${a}</code></p>`;
            explanation += `<p>Result: <strong>x = ${x}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Algebra Tools",
        "name": "Equation Solver",
        "slug": "equation-solver",
        "desc": "Solve mathematical equations of standard format ax + b = cx + d.",
        "formula": "Variables isolation algorithm",
        "formula_desc": "Combines variables to one side and constants to the other, then divides to isolate x.",
        "icon": "📐",
        "inputs": [
            {"id": "eq-a", "label": "Coefficient a (for ax + b = cx + d):", "type": "number", "default": "5"},
            {"id": "eq-b", "label": "Constant b:", "type": "number", "default": "10"},
            {"id": "eq-c", "label": "Coefficient c:", "type": "number", "default": "2"},
            {"id": "eq-d", "label": "Constant d:", "type": "number", "default": "22"}
        ],
        "outputs": [
            {"id": "eq-result", "label": "Value of x:", "type": "text"}
        ],
        "calc_js": """
            const a = parseFloat(document.getElementById('eq-a').value);
            const b = parseFloat(document.getElementById('eq-b').value);
            const c = parseFloat(document.getElementById('eq-c').value);
            const d = parseFloat(document.getElementById('eq-d').value);

            if (isNaN(a) || isNaN(b) || isNaN(c) || isNaN(d)) {
                showToast("Please enter numbers.", "error");
                return;
            }
            if (a === c) {
                showToast("Coefficients a and c cannot be equal (creates divide by zero).", "error");
                return;
            }

            const x = (d - b) / (a - c);
            document.getElementById('eq-result').textContent = x.toLocaleString(undefined, {maximumFractionDigits: 6});

            let explanation = `<p>Equation: <code>${a}x + ${b} = ${c}x + ${d}</code></p>`;
            explanation += `<p>Step 1: Move variable terms to left: <code>(${a} - ${c})x = ${d} - ${b}</code></p>`;
            explanation += `<p>Step 2: Simplify: <code>${a - c}x = ${d - b}</code></p>`;
            explanation += `<p>Step 3: Divide: <code>x = ${d - b} / ${a - c}</code></p>`;
            explanation += `<p>Result: <strong>x = ${x}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Algebra Tools",
        "name": "Linear Equation Solver",
        "slug": "linear-equation-solver",
        "desc": "Solve systems of two linear equations in two variables: a1 x + b1 y = c1 and a2 x + b2 y = c2.",
        "formula": "Cramer's Rule determinant system",
        "formula_desc": "Computes determinants Dx, Dy, and D to resolve x = Dx/D and y = Dy/D values.",
        "icon": "📐",
        "inputs": [
            {"id": "lin-a1", "label": "a1 coefficient:", "type": "number", "default": "2"},
            {"id": "lin-b1", "label": "b1 coefficient:", "type": "number", "default": "1"},
            {"id": "lin-c1", "label": "c1 constant:", "type": "number", "default": "11"},
            {"id": "lin-a2", "label": "a2 coefficient:", "type": "number", "default": "1"},
            {"id": "lin-b2", "label": "b2 coefficient:", "type": "number", "default": "-1"},
            {"id": "lin-c2", "label": "c2 constant:", "type": "number", "default": "1"}
        ],
        "outputs": [
            {"id": "lin-x", "label": "Value of x:", "type": "text"},
            {"id": "lin-y", "label": "Value of y:", "type": "text"}
        ],
        "calc_js": """
            const a1 = parseFloat(document.getElementById('lin-a1').value);
            const b1 = parseFloat(document.getElementById('lin-b1').value);
            const c1 = parseFloat(document.getElementById('lin-c1').value);
            const a2 = parseFloat(document.getElementById('lin-a2').value);
            const b2 = parseFloat(document.getElementById('lin-b2').value);
            const c2 = parseFloat(document.getElementById('lin-c2').value);

            if (isNaN(a1) || isNaN(b1) || isNaN(c1) || isNaN(a2) || isNaN(b2) || isNaN(c2)) {
                showToast("Please enter valid parameters.", "error");
                return;
            }

            const det = a1 * b2 - b1 * a2;
            if (det === 0) {
                showToast("The system of equations has no unique solution (determinant is zero).", "error");
                return;
            }

            const x = (c1 * b2 - b1 * c2) / det;
            const y = (a1 * c2 - c1 * a2) / det;

            document.getElementById('lin-x').textContent = x.toLocaleString(undefined, {maximumFractionDigits: 6});
            document.getElementById('lin-y').textContent = y.toLocaleString(undefined, {maximumFractionDigits: 6});

            let steps = `<p>System determinants:</p>`;
            steps += `<p>D = <code>(${a1} * ${b2}) - (${b1} * ${a2})</code> = <strong>${det}</strong></p>`;
            steps += `<p>Dx = <code>(${c1} * ${b2}) - (${b1} * ${c2})</code> = <strong>${c1*b2 - b1*c2}</strong></p>`;
            steps += `<p>Dy = <code>(${a1} * ${c2}) - (${c1} * ${a2})</code> = <strong>${a1*c2 - c1*a2}</strong></p>`;
            steps += `<p>Solutions: <code>x = Dx/D</code> = <strong>${x}</strong>, <code>y = Dy/D</code> = <strong>${y}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Algebra Tools",
        "name": "Quadratic Equation Solver",
        "slug": "quadratic-equation-solver",
        "desc": "Solve quadratic equations of standard form ax^2 + bx + c = 0.",
        "formula": "Quadratic formula solver",
        "formula_desc": "Applies quadratic formula x = (-b +/- sqrt(b^2 - 4ac)) / 2a, identifying real and complex roots.",
        "icon": "📐",
        "inputs": [
            {"id": "quad-a", "label": "Coefficient a (x^2):", "type": "number", "default": "1"},
            {"id": "quad-b", "label": "Coefficient b (x):", "type": "number", "default": "-5"},
            {"id": "quad-c", "label": "Constant c:", "type": "number", "default": "6"}
        ],
        "outputs": [
            {"id": "quad-r1", "label": "Root 1:", "type": "text"},
            {"id": "quad-r2", "label": "Root 2:", "type": "text"}
        ],
        "calc_js": """
            const a = parseFloat(document.getElementById('quad-a').value);
            const b = parseFloat(document.getElementById('quad-b').value);
            const c = parseFloat(document.getElementById('quad-c').value);

            if (isNaN(a) || isNaN(b) || isNaN(c)) {
                showToast("Please enter numbers.", "error");
                return;
            }
            if (a === 0) {
                showToast("Coefficient 'a' cannot be zero in quadratic equation.", "error");
                return;
            }

            const disc = b * b - 4 * a * c;
            let r1 = "", r2 = "";
            let steps = `<p>Equation: <code>${a}x² + (${b})x + (${c}) = 0</code></p>`;
            steps += `<p>Discriminant: <code>Δ = b² - 4ac = (${b})² - 4*(${a})*(${c})</code> = <strong>${disc}</strong></p>`;

            if (disc >= 0) {
                const root1 = (-b + Math.sqrt(disc)) / (2 * a);
                const root2 = (-b - Math.sqrt(disc)) / (2 * a);
                r1 = root1.toLocaleString(undefined, {maximumFractionDigits: 6});
                r2 = root2.toLocaleString(undefined, {maximumFractionDigits: 6});
                steps += `<p>Real roots found using quadratic formula:</p>`;
                steps += `<p>x1 = <code>(-(${b}) + sqrt(${disc})) / (2*${a})</code> = <strong>${root1}</strong></p>`;
                steps += `<p>x2 = <code>(-(${b}) - sqrt(${disc})) / (2*${a})</code> = <strong>${root2}</strong></p>`;
            } else {
                const real = -b / (2 * a);
                const imag = Math.sqrt(-disc) / (2 * a);
                r1 = `${real.toFixed(4)} + ${imag.toFixed(4)}i`;
                r2 = `${real.toFixed(4)} - ${imag.toFixed(4)}i`;
                steps += `<p>Complex roots found:</p>`;
                steps += `<p>x = <strong>${r1}</strong>, <strong>${r2}</strong></p>`;
            }

            document.getElementById('quad-r1').textContent = r1;
            document.getElementById('quad-r2').textContent = r2;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Algebra Tools",
        "name": "Polynomial Calculator",
        "slug": "polynomial-calculator",
        "desc": "Evaluate polynomial expressions at a given point x.",
        "formula": "Polynomial synthetic evaluation",
        "formula_desc": "Evaluates polynomial values P(x) = a_n*x^n + ... + a_0 using Horner's method.",
        "icon": "📐",
        "inputs": [
            {"id": "poly-coeffs", "label": "Coefficients (comma-separated, high to low degree, e.g. 1, -4, 3 for x^2 - 4x + 3):", "type": "text", "default": "1, -4, 3"},
            {"id": "poly-x", "label": "Evaluate at value x:", "type": "number", "default": "2"}
        ],
        "outputs": [
            {"id": "poly-result", "label": "P(x) Value:", "type": "text"}
        ],
        "calc_js": """
            const coeffs = document.getElementById('poly-coeffs').value.split(',').map(v => parseFloat(v.trim())).filter(v => !isNaN(v));
            const x = parseFloat(document.getElementById('poly-x').value);

            if (!coeffs.length || isNaN(x)) {
                showToast("Please enter valid inputs.", "error");
                return;
            }

            // Horner's Method evaluation
            let result = coeffs[0];
            let stepStr = [`a_${coeffs.length-1} = ${coeffs[0]}`];

            for (let i = 1; i < coeffs.length; i++) {
                const nextVal = result * x + coeffs[i];
                stepStr.push(`P_${i} = (${result}) * ${x} + (${coeffs[i]}) = ${nextVal}`);
                result = nextVal;
            }

            document.getElementById('poly-result').textContent = result.toLocaleString();
            updateBreakdown(`<p>Evaluation steps using Horner's method:</p><p><code>${stepStr.join('<br>')}</code></p><p>Result P(${x}) = <strong>${result}</strong></p>`);
        """
    },
    {
        "category": "Algebra Tools",
        "name": "Factorization Calculator",
        "slug": "factorization-calculator",
        "desc": "Find factors and factorizations of quadratic equations or numeric values.",
        "formula": "Quadratic factoring check / prime factorization",
        "formula_desc": "Splits quadratic forms ax^2+bx+c into binomial products based on roots, or lists integer divisors.",
        "icon": "📐",
        "inputs": [
            {"id": "fac-type", "label": "Factor Target:", "type": "select", "options": [
                ["number", "Integer Number"],
                ["quadratic", "Quadratic Expression ax^2 + bx + c"]
            ]},
            {"id": "fac-val", "label": "Enter Value (Integer OR a,b,c coefficients comma-separated):", "type": "text", "default": "1, -5, 6"}
        ],
        "outputs": [
            {"id": "fac-result", "label": "Factored Form:", "type": "textarea"}
        ],
        "calc_js": """
            const type = document.getElementById('fac-type').value;
            const input = document.getElementById('fac-val').value.trim();

            if (!input) {
                showToast("Please enter target values.", "error");
                return;
            }

            let result = "";
            let explanation = "";

            if (type === "number") {
                const num = parseInt(input);
                if (isNaN(num) || num <= 0) {
                    showToast("Please enter a positive integer.", "error");
                    return;
                }
                let divs = [];
                for (let i = 1; i <= num; i++) {
                    if (num % i === 0) divs.push(i);
                }
                result = divs.join(', ');
                explanation = `<p>Factors of integer ${num} are all numbers that divide it evenly: <strong>${result}</strong></p>`;
            } else {
                const parts = input.split(',').map(v => parseFloat(v.trim()));
                if (parts.length !== 3 || parts.some(isNaN)) {
                    showToast("Please enter coefficients a, b, c separated by commas.", "error");
                    return;
                }
                const a = parts[0];
                const b = parts[1];
                const c = parts[2];

                if (a === 0) {
                    showToast("Coefficient 'a' cannot be zero.", "error");
                    return;
                }

                const disc = b * b - 4 * a * c;
                if (disc < 0) {
                    result = "Cannot factor over real numbers (roots are complex).";
                    explanation = `<p>Discriminant ${disc} is negative. No real factors exist.</p>`;
                } else {
                    const r1 = (-b + Math.sqrt(disc)) / (2 * a);
                    const r2 = (-b - Math.sqrt(disc)) / (2 * a);

                    const sign1 = r1 >= 0 ? "-" : "+";
                    const sign2 = r2 >= 0 ? "-" : "+";
                    const term1 = `(x ${sign1} ${Math.abs(r1)})`;
                    const term2 = `(x ${sign2} ${Math.abs(r2)})`;
                    
                    result = (a === 1 ? "" : a) + term1 + term2;
                    explanation = `<p>Roots: x1 = ${r1}, x2 = ${r2}</p>`;
                    explanation += `<p>Factored expression: <strong>${result}</strong></p>`;
                }
            }

            document.getElementById('fac-result').value = result;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Algebra Tools",
        "name": "Simplify Expression Calculator",
        "slug": "simplify-expression-calculator",
        "desc": "Expand and simplify standard algebraic mathematical expressions like a(bx + c) + d.",
        "formula": "Distributive algebra expansion rules",
        "formula_desc": "Multiplies coefficients out and collects identical variable and constant parts.",
        "icon": "📐",
        "inputs": [
            {"id": "simp-term", "label": "Enter Formula in format a(bx + c) + dx + e:", "type": "text", "default": "3(2x + 4) - 5x + 6"}
        ],
        "outputs": [
            {"id": "simp-result", "label": "Simplified Output:", "type": "text"}
        ],
        "calc_js": """
            const expr = document.getElementById('simp-term').value.trim();
            if (!expr) {
                showToast("Please enter an expression.", "error");
                return;
            }

            // Simple parser for standard format: a(bx + c) + dx + e
            const regex = /^([+-]?\\d*)\\s*\\(\\s*([+-]?\\d*)x\\s*([+-]?\\d*)\\s*\\)\\s*([+-]?\\d*)x\\s*([+-]?\\d*)$/;
            const normalized = expr.replace(/\\s+/g, '');
            const match = normalized.match(regex);

            if (!match) {
                showToast("Please use standard format, e.g. 3(2x+4)-5x+6", "error");
                return;
            }

            const a = parseFloat(match[1] === "" || match[1] === "+" ? 1 : (match[1] === "-" ? -1 : match[1]));
            const b = parseFloat(match[2] === "" || match[2] === "+" ? 1 : (match[2] === "-" ? -1 : match[2]));
            const c = parseFloat(match[3]);
            const d = parseFloat(match[4] === "" || match[4] === "+" ? 1 : (match[4] === "-" ? -1 : match[4]));
            const e = parseFloat(match[5]);

            const finalX = a * b + d;
            const finalConst = a * c + e;

            const resStr = `${finalX}x ${finalConst >= 0 ? '+' : '-'} ${Math.abs(finalConst)}`;
            document.getElementById('simp-result').textContent = resStr;

            let steps = `<p>Input expression: <code>${expr}</code></p>`;
            steps += `<p>1. Distribute coefficient ${a} over parentheses: <code>${a * b}x + ${a * c}</code></p>`;
            steps += `<p>2. Collect terms: <code>(${a * b}x + ${d}x) + (${a * c} + ${e})</code></p>`;
            steps += `<p>Simplified output: <strong>${resStr}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Algebra Tools",
        "name": "Logarithm Calculator",
        "slug": "logarithm-calculator",
        "desc": "Calculate logarithms for any positive base value.",
        "formula": "Base change formula log_b(x) = ln(x) / ln(b)",
        "formula_desc": "Uses native natural logarithms to evaluate logs for any base.",
        "icon": "📐",
        "inputs": [
            {"id": "log-base", "label": "Log Base b (e.g. 10, e, 2):", "type": "text", "default": "10"},
            {"id": "log-val", "label": "Value x (Positive number):", "type": "number", "default": "100"}
        ],
        "outputs": [
            {"id": "log-result", "label": "Logarithm Result:", "type": "text"}
        ],
        "calc_js": """
            let baseStr = document.getElementById('log-base').value.trim().toLowerCase();
            const x = parseFloat(document.getElementById('log-val').value);

            if (isNaN(x) || x <= 0) {
                showToast("Value x must be greater than zero.", "error");
                return;
            }

            let base = 10;
            if (baseStr === "e") {
                base = Math.E;
            } else {
                base = parseFloat(baseStr);
            }

            if (isNaN(base) || base <= 0 || base === 1) {
                showToast("Base b must be positive and not equal to 1.", "error");
                return;
            }

            const result = Math.log(x) / Math.log(base);
            document.getElementById('log-result').textContent = result.toLocaleString(undefined, {maximumFractionDigits: 6});

            let explanation = `<p>Solving <code>log_${baseStr === 'e' ? 'e' : base}(${x})</code></p>`;
            explanation += `<p>Formula: <code>ln(${x}) / ln(${baseStr === 'e' ? 'e' : base})</code></p>`;
            explanation += `<p>Calculation: <code>${Math.log(x).toFixed(6)} / ${Math.log(base).toFixed(6)}</code> = <strong>${result}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Algebra Tools",
        "name": "Exponent Calculator",
        "slug": "exponent-calculator",
        "desc": "Raise values to any power base instantly.",
        "formula": "Exponent rules x^y",
        "formula_desc": "Computes the base multiplied by itself power times, resolving negative and fractional exponents.",
        "icon": "📐",
        "inputs": [
            {"id": "exp-base", "label": "Base x:", "type": "number", "default": "2"},
            {"id": "exp-power", "label": "Exponent / Power y:", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "exp-result", "label": "Calculated Power:", "type": "text"}
        ],
        "calc_js": """
            const base = parseFloat(document.getElementById('exp-base').value);
            const power = parseFloat(document.getElementById('exp-power').value);

            if (isNaN(base) || isNaN(power)) {
                showToast("Please enter valid base and exponent values.", "error");
                return;
            }

            const result = Math.pow(base, power);
            document.getElementById('exp-result').textContent = result.toLocaleString(undefined, {maximumFractionDigits: 6});

            let explanation = `<p>Formula: <code>${base} ^ ${power}</code></p>`;
            explanation += `<p>Calculated as: <strong>${result}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Algebra Tools",
        "name": "Root Calculator",
        "slug": "root-calculator",
        "desc": "Calculate square root, cube root, or any custom nth root value.",
        "formula": "Root exponent translation x^(1/n)",
        "formula_desc": "Finds the number which when multiplied by itself n times equals the target input value.",
        "icon": "📐",
        "inputs": [
            {"id": "root-val", "label": "Value x (Positive number):", "type": "number", "default": "16"},
            {"id": "root-degree", "label": "Degree n (e.g. 2 for square root, 3 for cube root):", "type": "number", "default": "2"}
        ],
        "outputs": [
            {"id": "root-result", "label": "Nth Root Result:", "type": "text"}
        ],
        "calc_js": """
            const x = parseFloat(document.getElementById('root-val').value);
            const n = parseFloat(document.getElementById('root-degree').value);

            if (isNaN(x) || isNaN(n) || n === 0) {
                showToast("Please enter valid inputs.", "error");
                return;
            }
            if (x < 0 && n % 2 === 0) {
                showToast("Even roots of negative numbers are not real.", "error");
                return;
            }

            let result = 0;
            if (x >= 0) {
                result = Math.pow(x, 1 / n);
            } else {
                result = -Math.pow(-x, 1 / n);
            }

            document.getElementById('root-result').textContent = result.toLocaleString(undefined, {maximumFractionDigits: 6});

            let explanation = `<p>Formula: <code>${x} ^ (1 / ${n})</code></p>`;
            explanation += `<p>Result: <strong>${result}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Geometry Tools",
        "name": "Area Calculator",
        "slug": "area-calculator-math",
        "desc": "Calculate the surface area of basic geometrical shapes (Circle, Rectangle, Triangle).",
        "formula": "Standard geometric area formulas",
        "formula_desc": "Uses shape formulas: Circle (pi*r^2), Rectangle (w*h), Triangle (b*h/2).",
        "icon": "📐",
        "inputs": [
            {"id": "area-shape", "label": "Select Shape:", "type": "select", "options": [
                ["circle", "Circle"],
                ["rectangle", "Rectangle"],
                ["triangle", "Triangle"]
            ]},
            {"id": "area-p1", "label": "Dimension 1 (Radius / Length / Base):", "type": "number", "default": "5"},
            {"id": "area-p2", "label": "Dimension 2 (Width / Height - Ignore for Circle):", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "area-result", "label": "Calculated Area:", "type": "text"}
        ],
        "calc_js": """
            const shape = document.getElementById('area-shape').value;
            const p1 = parseFloat(document.getElementById('area-p1').value);
            const p2 = parseFloat(document.getElementById('area-p2').value);

            if (isNaN(p1) || p1 <= 0) {
                showToast("Please enter positive values.", "error");
                return;
            }

            let area = 0;
            let explanation = "";

            if (shape === "circle") {
                area = Math.PI * p1 * p1;
                explanation = `<p>Circle Area formula: <code>π * r² = π * ${p1}²</code> = <strong>${area.toFixed(4)}</strong></p>`;
            } else {
                if (isNaN(p2) || p2 <= 0) {
                    showToast("Please enter a valid second dimension.", "error");
                    return;
                }
                if (shape === "rectangle") {
                    area = p1 * p2;
                    explanation = `<p>Rectangle Area formula: <code>Length * Width = ${p1} * ${p2}</code> = <strong>${area}</strong></p>`;
                } else if (shape === "triangle") {
                    area = 0.5 * p1 * p2;
                    explanation = `<p>Triangle Area formula: <code>0.5 * Base * Height = 0.5 * ${p1} * ${p2}</code> = <strong>${area}</strong></p>`;
                }
            }

            document.getElementById('area-result').textContent = area.toLocaleString(undefined, {maximumFractionDigits: 4});
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Geometry Tools",
        "name": "Perimeter Calculator",
        "slug": "perimeter-calculator",
        "desc": "Calculate perimeter boundaries for circles, rectangles, and regular polygons.",
        "formula": "Geometric perimeter rules",
        "formula_desc": "Sum of border sides: Circle (2*pi*r), Rectangle (2*(w+h)), Polygon (n*side).",
        "icon": "📐",
        "inputs": [
            {"id": "peri-shape", "label": "Shape Type:", "type": "select", "options": [
                ["circle", "Circle (Circumference)"],
                ["rectangle", "Rectangle"],
                ["polygon", "Regular Polygon"]
            ]},
            {"id": "peri-p1", "label": "Radius / Length / Side Length:", "type": "number", "default": "6"},
            {"id": "peri-p2", "label": "Width / Sides Count (Ignore for Circle):", "type": "number", "default": "4"}
        ],
        "outputs": [
            {"id": "peri-result", "label": "Calculated Perimeter:", "type": "text"}
        ],
        "calc_js": """
            const shape = document.getElementById('peri-shape').value;
            const p1 = parseFloat(document.getElementById('peri-p1').value);
            const p2 = parseFloat(document.getElementById('peri-p2').value);

            if (isNaN(p1) || p1 <= 0) {
                showToast("Please enter positive values.", "error");
                return;
            }

            let perimeter = 0;
            let explanation = "";

            if (shape === "circle") {
                perimeter = 2 * Math.PI * p1;
                explanation = `<p>Circle Circumference: <code>2 * π * r = 2 * π * ${p1}</code> = <strong>${perimeter.toFixed(4)}</strong></p>`;
            } else {
                if (isNaN(p2) || p2 <= 0) {
                    showToast("Please enter valid secondary dimensions.", "error");
                    return;
                }
                if (shape === "rectangle") {
                    perimeter = 2 * (p1 + p2);
                    explanation = `<p>Rectangle Perimeter: <code>2 * (Length + Width) = 2 * (${p1} + ${p2})</code> = <strong>${perimeter}</strong></p>`;
                } else if (shape === "polygon") {
                    perimeter = p1 * p2;
                    explanation = `<p>Polygon Perimeter: <code>Sides Count * Side Length = ${p2} * ${p1}</code> = <strong>${perimeter}</strong></p>`;
                }
            }

            document.getElementById('peri-result').textContent = perimeter.toLocaleString(undefined, {maximumFractionDigits: 4});
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Geometry Tools",
        "name": "Volume Calculator",
        "slug": "volume-calculator-math",
        "desc": "Calculate volume metrics for solid geometric shapes (Cylinder, Sphere, Cube).",
        "formula": "Standard three-dimensional volume equations",
        "formula_desc": "Computes values: Cylinder (pi*r^2*h), Sphere (4/3*pi*r^3), Cube (side^3).",
        "icon": "📐",
        "inputs": [
            {"id": "vol-shape", "label": "Select Shape:", "type": "select", "options": [
                ["cylinder", "Cylinder"],
                ["sphere", "Sphere"],
                ["cube", "Cube"]
            ]},
            {"id": "vol-p1", "label": "Dimension 1 (Radius / Side):", "type": "number", "default": "4"},
            {"id": "vol-p2", "label": "Dimension 2 (Height - Ignore for Sphere / Cube):", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "vol-result", "label": "Calculated Volume:", "type": "text"}
        ],
        "calc_js": """
            const shape = document.getElementById('vol-shape').value;
            const p1 = parseFloat(document.getElementById('vol-p1').value);
            const p2 = parseFloat(document.getElementById('vol-p2').value);

            if (isNaN(p1) || p1 <= 0) {
                showToast("Please enter positive values.", "error");
                return;
            }

            let volume = 0;
            let explanation = "";

            if (shape === "cylinder") {
                if (isNaN(p2) || p2 <= 0) {
                    showToast("Please enter positive height value.", "error");
                    return;
                }
                volume = Math.PI * p1 * p1 * p2;
                explanation = `<p>Cylinder Volume: <code>π * r² * h = π * ${p1}² * ${p2}</code> = <strong>${volume.toFixed(4)}</strong></p>`;
            } else if (shape === "sphere") {
                volume = (4 / 3) * Math.PI * Math.pow(p1, 3);
                explanation = `<p>Sphere Volume: <code>(4/3) * π * r³ = (4/3) * π * ${p1}³</code> = <strong>${volume.toFixed(4)}</strong></p>`;
            } else if (shape === "cube") {
                volume = Math.pow(p1, 3);
                explanation = `<p>Cube Volume: <code>Side³ = ${p1}³</code> = <strong>${volume}</strong></p>`;
            }

            document.getElementById('vol-result').textContent = volume.toLocaleString(undefined, {maximumFractionDigits: 4});
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Geometry Tools",
        "name": "Surface Area Calculator",
        "slug": "surface-area-calculator-math",
        "desc": "Calculate total boundary surface area of cylinders, spheres, and cubes.",
        "formula": "Standard boundary surface area equations",
        "formula_desc": "Uses surface formulas: Cylinder (2*pi*r*(r+h)), Sphere (4*pi*r^2), Cube (6*side^2).",
        "icon": "📐",
        "inputs": [
            {"id": "sa-shape", "label": "Select Shape:", "type": "select", "options": [
                ["cylinder", "Cylinder"],
                ["sphere", "Sphere"],
                ["cube", "Cube"]
            ]},
            {"id": "sa-p1", "label": "Dimension 1 (Radius / Side):", "type": "number", "default": "4"},
            {"id": "sa-p2", "label": "Dimension 2 (Height - Ignore for Sphere / Cube):", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "sa-result", "label": "Calculated Surface Area:", "type": "text"}
        ],
        "calc_js": """
            const shape = document.getElementById('sa-shape').value;
            const p1 = parseFloat(document.getElementById('sa-p1').value);
            const p2 = parseFloat(document.getElementById('sa-p2').value);

            if (isNaN(p1) || p1 <= 0) {
                showToast("Please enter positive values.", "error");
                return;
            }

            let sa = 0;
            let explanation = "";

            if (shape === "cylinder") {
                if (isNaN(p2) || p2 <= 0) {
                    showToast("Please enter height.", "error");
                    return;
                }
                sa = 2 * Math.PI * p1 * (p1 + p2);
                explanation = `<p>Cylinder Surface Area: <code>2 * π * r * (r + h) = 2 * π * ${p1} * (${p1} + ${p2})</code> = <strong>${sa.toFixed(4)}</strong></p>`;
            } else if (shape === "sphere") {
                sa = 4 * Math.PI * p1 * p1;
                explanation = `<p>Sphere Surface Area: <code>4 * π * r² = 4 * π * ${p1}²</code> = <strong>${sa.toFixed(4)}</strong></p>`;
            } else if (shape === "cube") {
                sa = 6 * p1 * p1;
                explanation = `<p>Cube Surface Area: <code>6 * Side² = 6 * ${p1}²</code> = <strong>${sa}</strong></p>`;
            }

            document.getElementById('sa-result').textContent = sa.toLocaleString(undefined, {maximumFractionDigits: 4});
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Geometry Tools",
        "name": "Triangle Calculator",
        "slug": "triangle-calculator-math",
        "desc": "Calculate angles, sides, perimeter, and area parameters of triangles.",
        "formula": "Trigonometric and geometric triangle properties",
        "formula_desc": "Applies law of cosines, law of sines, and Heron's formula based on available inputs.",
        "icon": "📐",
        "inputs": [
            {"id": "tri-side-a", "label": "Side A Length:", "type": "number", "default": "3"},
            {"id": "tri-side-b", "label": "Side B Length:", "type": "number", "default": "4"},
            {"id": "tri-side-c", "label": "Side C Length:", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "tri-area", "label": "Area (Heron's Formula):", "type": "text"},
            {"id": "tri-peri", "label": "Perimeter:", "type": "text"}
        ],
        "calc_js": """
            const a = parseFloat(document.getElementById('tri-side-a').value);
            const b = parseFloat(document.getElementById('tri-side-b').value);
            const c = parseFloat(document.getElementById('tri-side-c').value);

            if (isNaN(a) || isNaN(b) || isNaN(c) || a <= 0 || b <= 0 || c <= 0) {
                showToast("Please enter positive values for all sides.", "error");
                return;
            }
            if (a + b <= c || a + c <= b || b + c <= a) {
                showToast("The given lengths do not satisfy the triangle inequality theorem.", "error");
                return;
            }

            const perimeter = a + b + c;
            const s = perimeter / 2; // semiperimeter
            const area = Math.sqrt(s * (s - a) * (s - b) * (s - c));

            document.getElementById('tri-area').textContent = area.toLocaleString(undefined, {maximumFractionDigits: 4});
            document.getElementById('tri-peri').textContent = perimeter.toLocaleString();

            let explanation = `<p>Triangle with sides: A = ${a}, B = ${b}, C = ${c}</p>`;
            explanation += `<p>Semiperimeter: <code>s = (A + B + C) / 2 = ${s}</code></p>`;
            explanation += `<p>Area (Heron's formula): <code>sqrt(s*(s-A)*(s-B)*(s-C))</code> = <strong>${area.toFixed(4)}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Geometry Tools",
        "name": "Circle Calculator",
        "slug": "circle-calculator-math",
        "desc": "Calculate circle parameters like area, circumference, diameter, and radius.",
        "formula": "Standard circle parameters mapping",
        "formula_desc": "Converts parameters based on radius (r): Diameter = 2r, Circumference = 2*pi*r, Area = pi*r^2.",
        "icon": "📐",
        "inputs": [
            {"id": "circ-val", "label": "Circle Radius:", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "circ-diam", "label": "Diameter:", "type": "text"},
            {"id": "circ-area", "label": "Area:", "type": "text"},
            {"id": "circ-circum", "label": "Circumference:", "type": "text"}
        ],
        "calc_js": """
            const r = parseFloat(document.getElementById('circ-val').value);
            if (isNaN(r) || r <= 0) {
                showToast("Please enter a positive radius.", "error");
                return;
            }

            const diam = 2 * r;
            const area = Math.PI * r * r;
            const circum = 2 * Math.PI * r;

            document.getElementById('circ-diam').textContent = diam.toLocaleString(undefined, {maximumFractionDigits: 4});
            document.getElementById('circ-area').textContent = area.toLocaleString(undefined, {maximumFractionDigits: 4});
            document.getElementById('circ-circum').textContent = circum.toLocaleString(undefined, {maximumFractionDigits: 4});

            let steps = `<p>Input Radius: <strong>${r}</strong></p>`;
            steps += `<p>Diameter = <code>2 * r = 2 * ${r}</code> = <strong>${diam}</strong></p>`;
            steps += `<p>Area = <code>π * r² = π * ${r}²</code> = <strong>${area.toFixed(4)}</strong></p>`;
            steps += `<p>Circumference = <code>2 * π * r = 2 * π * ${r}</code> = <strong>${circum.toFixed(4)}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Geometry Tools",
        "name": "Rectangle Calculator",
        "slug": "rectangle-calculator-math",
        "desc": "Compute perimeter, area, and diagonal lengths of a rectangle.",
        "formula": "Rectangle geometry equations",
        "formula_desc": "Computes values: Area = w * h, Perimeter = 2 * (w + h), Diagonal = sqrt(w^2 + h^2).",
        "icon": "📐",
        "inputs": [
            {"id": "rect-w", "label": "Width:", "type": "number", "default": "8"},
            {"id": "rect-h", "label": "Height:", "type": "number", "default": "15"}
        ],
        "outputs": [
            {"id": "rect-area", "label": "Area:", "type": "text"},
            {"id": "rect-peri", "label": "Perimeter:", "type": "text"},
            {"id": "rect-diag", "label": "Diagonal:", "type": "text"}
        ],
        "calc_js": """
            const w = parseFloat(document.getElementById('rect-w').value);
            const h = parseFloat(document.getElementById('rect-h').value);

            if (isNaN(w) || isNaN(h) || w <= 0 || h <= 0) {
                showToast("Please enter positive width and height.", "error");
                return;
            }

            const area = w * h;
            const peri = 2 * (w + h);
            const diag = Math.sqrt(w * w + h * h);

            document.getElementById('rect-area').textContent = area.toLocaleString();
            document.getElementById('rect-peri').textContent = peri.toLocaleString();
            document.getElementById('rect-diag').textContent = diag.toLocaleString(undefined, {maximumFractionDigits: 4});

            let steps = `<p>Dimensions: Width = ${w}, Height = ${h}</p>`;
            steps += `<p>Area = <code>Width * Height = ${w} * ${h}</code> = <strong>${area}</strong></p>`;
            steps += `<p>Perimeter = <code>2 * (Width + Height) = 2 * (${w} + ${h})</code> = <strong>${peri}</strong></p>`;
            steps += `<p>Diagonal = <code>sqrt(Width² + Height²) = sqrt(${w}² + ${h}²)</code> = <strong>${diag.toFixed(4)}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Geometry Tools",
        "name": "Square Calculator",
        "slug": "square-calculator-math",
        "desc": "Calculate perimeter, area, and diagonal dimensions of a square given its side.",
        "formula": "Square geometric mappings",
        "formula_desc": "Computes parameters from side (s): Area = s^2, Perimeter = 4s, Diagonal = s * sqrt(2).",
        "icon": "📐",
        "inputs": [
            {"id": "sq-side", "label": "Side Length:", "type": "number", "default": "6"}
        ],
        "outputs": [
            {"id": "sq-area", "label": "Area:", "type": "text"},
            {"id": "sq-peri", "label": "Perimeter:", "type": "text"},
            {"id": "sq-diag", "label": "Diagonal:", "type": "text"}
        ],
        "calc_js": """
            const s = parseFloat(document.getElementById('sq-side').value);
            if (isNaN(s) || s <= 0) {
                showToast("Please enter a positive side length.", "error");
                return;
            }

            const area = s * s;
            const peri = 4 * s;
            const diag = s * Math.sqrt(2);

            document.getElementById('sq-area').textContent = area.toLocaleString();
            document.getElementById('sq-peri').textContent = peri.toLocaleString();
            document.getElementById('sq-diag').textContent = diag.toLocaleString(undefined, {maximumFractionDigits: 4});

            let steps = `<p>Square Side: <strong>${s}</strong></p>`;
            steps += `<p>Area = <code>Side² = ${s}²</code> = <strong>${area}</strong></p>`;
            steps += `<p>Perimeter = <code>4 * Side = 4 * ${s}</code> = <strong>${peri}</strong></p>`;
            steps += `<p>Diagonal = <code>Side * sqrt(2) = ${s} * ${Math.sqrt(2).toFixed(6)}</code> = <strong>${diag.toFixed(4)}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Geometry Tools",
        "name": "Trapezoid Calculator",
        "slug": "trapezoid-calculator-math",
        "desc": "Calculate the area and height properties of a trapezoid shape.",
        "formula": "Trapezoid area formula Area = 0.5 * (a + b) * h",
        "formula_desc": "Computes the area of a trapezoid using the average of parallel bases multiplied by height.",
        "icon": "📐",
        "inputs": [
            {"id": "trap-a", "label": "Base Side a:", "type": "number", "default": "5"},
            {"id": "trap-b", "label": "Base Side b:", "type": "number", "default": "9"},
            {"id": "trap-h", "label": "Height h:", "type": "number", "default": "6"}
        ],
        "outputs": [
            {"id": "trap-area", "label": "Calculated Area:", "type": "text"}
        ],
        "calc_js": """
            const a = parseFloat(document.getElementById('trap-a').value);
            const b = parseFloat(document.getElementById('trap-b').value);
            const h = parseFloat(document.getElementById('trap-h').value);

            if (isNaN(a) || isNaN(b) || isNaN(h) || a <= 0 || b <= 0 || h <= 0) {
                showToast("Please enter positive values for bases and height.", "error");
                return;
            }

            const area = 0.5 * (a + b) * h;
            document.getElementById('trap-area').textContent = area.toLocaleString();

            let explanation = `<p>Bases: a = ${a}, b = ${b}, Height: h = ${h}</p>`;
            explanation += `<p>Formula: <code>0.5 * (a + b) * h</code></p>`;
            explanation += `<p>Calculation: <code>0.5 * (${a} + ${b}) * ${h}</code> = <strong>${area}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Geometry Tools",
        "name": "Polygon Calculator",
        "slug": "polygon-calculator-math",
        "desc": "Calculate properties like interior angles and area for regular polygons.",
        "formula": "Regular polygon geometry formulas",
        "formula_desc": "Computes: Area = (n * s^2) / (4 * tan(pi/n)) and Interior Angle = (n - 2) * 180 / n.",
        "icon": "📐",
        "inputs": [
            {"id": "poly-n", "label": "Number of Sides n (Integer >= 3):", "type": "number", "default": "5"},
            {"id": "poly-s", "label": "Side Length s:", "type": "number", "default": "6"}
        ],
        "outputs": [
            {"id": "poly-area", "label": "Area:", "type": "text"},
            {"id": "poly-angle", "label": "Interior Angle:", "type": "text"}
        ],
        "calc_js": """
            const n = parseInt(document.getElementById('poly-n').value);
            const s = parseFloat(document.getElementById('poly-s').value);

            if (isNaN(n) || isNaN(s) || n < 3 || s <= 0) {
                showToast("Please enter valid parameters (sides n >= 3, side s > 0).", "error");
                return;
            }

            const angle = ((n - 2) * 180) / n;
            const area = (n * s * s) / (4 * Math.tan(Math.PI / n));

            document.getElementById('poly-area').textContent = area.toLocaleString(undefined, {maximumFractionDigits: 4});
            document.getElementById('poly-angle').textContent = angle.toLocaleString() + "°";

            let steps = `<p>Regular Polygon: ${n} sides of length ${s}</p>`;
            steps += `<p>Interior Angle = <code>((n - 2) * 180) / n = ((${n} - 2) * 180) / ${n}</code> = <strong>${angle}°</strong></p>`;
            steps += `<p>Area = <code>(n * s²) / (4 * tan(π/n)) = (${n} * ${s}²) / (4 * tan(π/${n}))</code> = <strong>${area.toFixed(4)}</strong></p>`;
            updateBreakdown(steps);
        """
    }
]

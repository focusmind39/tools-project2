# -*- coding: utf-8 -*-
"""
Database of Advanced Math Tools & Financial Math Tools (20 tools)
"""

ADVANCED_FINANCIAL_TOOLS = [
    {
        "category": "Advanced Math Tools",
        "name": "Matrix Calculator",
        "slug": "matrix-calculator-math",
        "desc": "Add, subtract, and multiply 2x2 matrices.",
        "formula": "Matrix linear algebra properties",
        "formula_desc": "Evaluates matrix addition/subtraction component-wise, and matrix multiplication using row-column dot products.",
        "icon": "🔢",
        "inputs": [
            {"id": "mat-a11", "label": "Matrix A (1,1):", "type": "number", "default": "1"},
            {"id": "mat-a12", "label": "Matrix A (1,2):", "type": "number", "default": "2"},
            {"id": "mat-a21", "label": "Matrix A (2,1):", "type": "number", "default": "3"},
            {"id": "mat-a22", "label": "Matrix A (2,2):", "type": "number", "default": "4"},
            {"id": "mat-op", "label": "Operation:", "type": "select", "options": [
                ["+", "Addition (A + B)"],
                ["-", "Subtraction (A - B)"],
                ["*", "Multiplication (A * B)"]
            ]},
            {"id": "mat-b11", "label": "Matrix B (1,1):", "type": "number", "default": "5"},
            {"id": "mat-b12", "label": "Matrix B (1,2):", "type": "number", "default": "6"},
            {"id": "mat-b21", "label": "Matrix B (2,1):", "type": "number", "default": "7"},
            {"id": "mat-b22", "label": "Matrix B (2,2):", "type": "number", "default": "8"}
        ],
        "outputs": [
            {"id": "mat-res11", "label": "Result (1,1):", "type": "text"},
            {"id": "mat-res12", "label": "Result (1,2):", "type": "text"},
            {"id": "mat-res21", "label": "Result (2,1):", "type": "text"},
            {"id": "mat-res22", "label": "Result (2,2):", "type": "text"}
        ],
        "calc_js": """
            const a11 = parseFloat(document.getElementById('mat-a11').value);
            const a12 = parseFloat(document.getElementById('mat-a12').value);
            const a21 = parseFloat(document.getElementById('mat-a21').value);
            const a22 = parseFloat(document.getElementById('mat-a22').value);
            const op = document.getElementById('mat-op').value;
            const b11 = parseFloat(document.getElementById('mat-b11').value);
            const b12 = parseFloat(document.getElementById('mat-b12').value);
            const b21 = parseFloat(document.getElementById('mat-b21').value);
            const b22 = parseFloat(document.getElementById('mat-b22').value);

            if ([a11,a12,a21,a22,b11,b12,b21,b22].some(isNaN)) {
                showToast("Please enter numbers in all matrix slots.", "error");
                return;
            }

            let r11 = 0, r12 = 0, r21 = 0, r22 = 0;
            let steps = "";

            if (op === "+") {
                r11 = a11 + b11; r12 = a12 + b12;
                r21 = a21 + b21; r22 = a22 + b22;
                steps = `<p>Adding components: <code>[a_ij] + [b_ij]</code></p>`;
            } else if (op === "-") {
                r11 = a11 - b11; r12 = a12 - b12;
                r21 = a21 - b21; r22 = a22 - b22;
                steps = `<p>Subtracting components: <code>[a_ij] - [b_ij]</code></p>`;
            } else if (op === "*") {
                r11 = a11 * b11 + a12 * b21;
                r12 = a11 * b12 + a12 * b22;
                r21 = a21 * b11 + a22 * b21;
                r22 = a21 * b12 + a22 * b22;
                steps = `<p>Multiplying rows by columns:</p>`;
                steps += `<p>R11 = <code>${a11}*${b11} + ${a12}*${b21}</code> = <strong>${r11}</strong></p>`;
                steps += `<p>R12 = <code>${a11}*${b12} + ${a12}*${b22}</code> = <strong>${r12}</strong></p>`;
            }

            document.getElementById('mat-res11').textContent = r11;
            document.getElementById('mat-res12').textContent = r12;
            document.getElementById('mat-res21').textContent = r21;
            document.getElementById('mat-res22').textContent = r22;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Advanced Math Tools",
        "name": "Matrix Determinant Calculator",
        "slug": "matrix-determinant-calculator",
        "desc": "Calculate the determinant of a 2x2 matrix.",
        "formula": "det(A) = ad - bc",
        "formula_desc": "Computes diagonal products difference: a11*a22 - a12*a21.",
        "icon": "🔢",
        "inputs": [
            {"id": "det-a11", "label": "a11:", "type": "number", "default": "4"},
            {"id": "det-a12", "label": "a12:", "type": "number", "default": "3"},
            {"id": "det-a21", "label": "a21:", "type": "number", "default": "2"},
            {"id": "det-a22", "label": "a22:", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "det-result", "label": "Determinant:", "type": "text"}
        ],
        "calc_js": """
            const a11 = parseFloat(document.getElementById('det-a11').value);
            const a12 = parseFloat(document.getElementById('det-a12').value);
            const a21 = parseFloat(document.getElementById('det-a21').value);
            const a22 = parseFloat(document.getElementById('det-a22').value);

            if ([a11,a12,a21,a22].some(isNaN)) {
                showToast("Please enter numeric inputs.", "error");
                return;
            }

            const det = a11 * a22 - a12 * a21;
            document.getElementById('det-result').textContent = det;

            let explanation = `<p>Formula: <code>det = (a11 * a22) - (a12 * a21)</code></p>`;
            explanation += `<p>Calculation: <code>(${a11} * ${a22}) - (${a12} * ${a21})</code> = <strong>${det}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Advanced Math Tools",
        "name": "Matrix Inverse Calculator",
        "slug": "matrix-inverse-calculator",
        "desc": "Calculate the inverse of a 2x2 matrix.",
        "formula": "A^-1 = (1 / det) * adj(A)",
        "formula_desc": "Divides the adjugate matrix by the determinant value, checking that determinant is non-zero.",
        "icon": "🔢",
        "inputs": [
            {"id": "inv-a11", "label": "a11:", "type": "number", "default": "1"},
            {"id": "inv-a12", "label": "a12:", "type": "number", "default": "2"},
            {"id": "inv-a21", "label": "a21:", "type": "number", "default": "3"},
            {"id": "inv-a22", "label": "a22:", "type": "number", "default": "4"}
        ],
        "outputs": [
            {"id": "inv-res11", "label": "Inv(1,1):", "type": "text"},
            {"id": "inv-res12", "label": "Inv(1,2):", "type": "text"},
            {"id": "inv-res21", "label": "Inv(2,1):", "type": "text"},
            {"id": "inv-res22", "label": "Inv(2,2):", "type": "text"}
        ],
        "calc_js": """
            const a11 = parseFloat(document.getElementById('inv-a11').value);
            const a12 = parseFloat(document.getElementById('inv-a12').value);
            const a21 = parseFloat(document.getElementById('inv-a21').value);
            const a22 = parseFloat(document.getElementById('inv-a22').value);

            if ([a11,a12,a21,a22].some(isNaN)) {
                showToast("Please enter numbers.", "error");
                return;
            }

            const det = a11 * a22 - a12 * a21;
            if (det === 0) {
                showToast("Determinant is zero. Matrix is singular and cannot be inverted.", "error");
                return;
            }

            const r11 = a22 / det;
            const r12 = -a12 / det;
            const r21 = -a21 / det;
            const r22 = a11 / det;

            document.getElementById('inv-res11').textContent = r11.toFixed(4).replace(/\\.0+$/, '');
            document.getElementById('inv-res12').textContent = r12.toFixed(4).replace(/\\.0+$/, '');
            document.getElementById('inv-res21').textContent = r21.toFixed(4).replace(/\\.0+$/, '');
            document.getElementById('inv-res22').textContent = r22.toFixed(4).replace(/\\.0+$/, '');

            let explanation = `<p>Determinant = <code>(${a11} * ${a22}) - (${a12} * ${a21}) = ${det}</code></p>`;
            explanation += `<p>Inverse components multiplied by <code>1 / ${det}</code></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Advanced Math Tools",
        "name": "Vector Calculator",
        "slug": "vector-calculator",
        "desc": "Calculate vector addition, dot product, and cross product for two 3D vectors.",
        "formula": "Vector algebraic properties",
        "formula_desc": "Computes dot product sum(u_i * v_i) and cross product determinant arrays.",
        "icon": "📐",
        "inputs": [
            {"id": "vec-u1", "label": "Vector U (x):", "type": "number", "default": "1"},
            {"id": "vec-u2", "label": "Vector U (y):", "type": "number", "default": "2"},
            {"id": "vec-u3", "label": "Vector U (z):", "type": "number", "default": "3"},
            {"id": "vec-op", "label": "Operation:", "type": "select", "options": [
                ["dot", "Dot Product (U · V)"],
                ["cross", "Cross Product (U x V)"]
            ]},
            {"id": "vec-v1", "label": "Vector V (x):", "type": "number", "default": "4"},
            {"id": "vec-v2", "label": "Vector V (y):", "type": "number", "default": "5"},
            {"id": "vec-v3", "label": "Vector V (z):", "type": "number", "default": "6"}
        ],
        "outputs": [
            {"id": "vec-result", "label": "Result:", "type": "textarea"}
        ],
        "calc_js": """
            const u1 = parseFloat(document.getElementById('vec-u1').value);
            const u2 = parseFloat(document.getElementById('vec-u2').value);
            const u3 = parseFloat(document.getElementById('vec-u3').value);
            const op = document.getElementById('vec-op').value;
            const v1 = parseFloat(document.getElementById('vec-v1').value);
            const v2 = parseFloat(document.getElementById('vec-v2').value);
            const v3 = parseFloat(document.getElementById('vec-v3').value);

            if ([u1,u2,u3,v1,v2,v3].some(isNaN)) {
                showToast("Please enter numbers.", "error");
                return;
            }

            let result = "";
            let explanation = "";

            if (op === "dot") {
                const dot = u1 * v1 + u2 * v2 + u3 * v3;
                result = `Dot Product: ${dot}`;
                explanation = `<p>Formula: <code>u1*v1 + u2*v2 + u3*v3</code></p>`;
                explanation += `<p>Calculation: <code>(${u1}*${v1}) + (${u2}*${v2}) + (${u3}*${v3})</code> = <strong>${dot}</strong></p>`;
            } else if (op === "cross") {
                const cx = u2 * v3 - u3 * v2;
                const cy = u3 * v1 - u1 * v3;
                const cz = u1 * v2 - u2 * v1;
                result = `Cross Product: [${cx}, ${cy}, ${cz}]`;
                explanation = `<p>Formula: <code>[u2*v3 - u3*v2, u3*v1 - u1*v3, u1*v2 - u2*v1]</code></p>`;
                explanation += `<p>Calculation results: <strong>[${cx}, ${cy}, ${cz}]</strong></p>`;
            }

            document.getElementById('vec-result').value = result;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Advanced Math Tools",
        "name": "Complex Number Calculator",
        "slug": "complex-number-calculator",
        "desc": "Add, subtract, and multiply complex numbers of format a + bi.",
        "formula": "Complex imaginary mathematics rules",
        "formula_desc": "Evaluates products using imaginary factor i^2 = -1 standard rule.",
        "icon": "🧪",
        "inputs": [
            {"id": "comp-r1", "label": "Complex A Real (a):", "type": "number", "default": "3"},
            {"id": "comp-i1", "label": "Complex A Imaginary (b):", "type": "number", "default": "2"},
            {"id": "comp-op", "label": "Operation:", "type": "select", "options": [
                ["+", "Addition (+)"],
                ["-", "Subtraction (-)"],
                ["*", "Multiplication (*)"]
            ]},
            {"id": "comp-r2", "label": "Complex B Real (c):", "type": "number", "default": "1"},
            {"id": "comp-i2", "label": "Complex B Imaginary (d):", "type": "number", "default": "-4"}
        ],
        "outputs": [
            {"id": "comp-result", "label": "Complex Output:", "type": "text"}
        ],
        "calc_js": """
            const r1 = parseFloat(document.getElementById('comp-r1').value);
            const i1 = parseFloat(document.getElementById('comp-i1').value);
            const op = document.getElementById('comp-op').value;
            const r2 = parseFloat(document.getElementById('comp-r2').value);
            const i2 = parseFloat(document.getElementById('comp-i2').value);

            if ([r1,i1,r2,i2].some(isNaN)) {
                showToast("Please enter numbers.", "error");
                return;
            }

            let real = 0, imag = 0;
            let explanation = "";

            if (op === "+") {
                real = r1 + r2;
                imag = i1 + i2;
                explanation = `<p>Add components: <code>(${r1} + ${r2}) + (${i1} + ${i2})i</code></p>`;
            } else if (op === "-") {
                real = r1 - r2;
                imag = i1 - i2;
                explanation = `<p>Subtract components: <code>(${r1} - ${r2}) + (${i1} - ${i2})i</code></p>`;
            } else if (op === "*") {
                real = r1 * r2 - i1 * i2;
                imag = r1 * i2 + i1 * r2;
                explanation = `<p>Multiply components: <code>(a*c - b*d) + (a*d + b*c)i</code></p>`;
                explanation += `<p>Calculation: <code>(${r1}*${r2} - ${i1}*${i2}) + (${r1}*${i2} + ${i1}*${r2})i</code></p>`;
            }

            const resStr = `${real} ${imag >= 0 ? '+' : '-'} ${Math.abs(imag)}i`;
            document.getElementById('comp-result').textContent = resStr;
            updateBreakdown(explanation + `<p>Result: <strong>${resStr}</strong></p>`);
        """
    },
    {
        "category": "Advanced Math Tools",
        "name": "Scientific Notation Calculator",
        "slug": "scientific-notation-calculator-math",
        "desc": "Multiply or divide numbers configured in scientific notations format (a * 10^b).",
        "formula": "Exponents multiplication laws",
        "formula_desc": "Multiplies mantissas and adds indices, or divides mantissas and subtracts indices.",
        "icon": "📐",
        "inputs": [
            {"id": "sn-a1", "label": "First Mantissa a1:", "type": "number", "default": "3.2"},
            {"id": "sn-e1", "label": "First Exponent e1:", "type": "number", "default": "5"},
            {"id": "sn-op", "label": "Operation:", "type": "select", "options": [
                ["*", "Multiplication (*)"],
                ["/", "Division (/)"]
            ]},
            {"id": "sn-a2", "label": "Second Mantissa a2:", "type": "number", "default": "2.0"},
            {"id": "sn-e2", "label": "Second Exponent e2:", "type": "number", "default": "3"}
        ],
        "outputs": [
            {"id": "sn-result", "label": "Scientific Notation Output:", "type": "text"}
        ],
        "calc_js": """
            const a1 = parseFloat(document.getElementById('sn-a1').value);
            const e1 = parseInt(document.getElementById('sn-e1').value);
            const op = document.getElementById('sn-op').value;
            const a2 = parseFloat(document.getElementById('sn-a2').value);
            const e2 = parseInt(document.getElementById('sn-e2').value);

            if (isNaN(a1) || isNaN(e1) || isNaN(a2) || isNaN(e2)) {
                showToast("Please enter numbers.", "error");
                return;
            }

            let resA = 0;
            let resE = 0;
            if (op === "*") {
                resA = a1 * a2;
                resE = e1 + e2;
            } else {
                if (a2 === 0) { showToast("Cannot divide by zero.", "error"); return; }
                resA = a1 / a2;
                resE = e1 - e2;
            }

            // Normalize scientific notation
            if (resA !== 0) {
                while (Math.abs(resA) >= 10) {
                    resA /= 10;
                    resE += 1;
                }
                while (Math.abs(resA) < 1) {
                    resA *= 10;
                    resE -= 1;
                }
            }

            const resStr = `${resA.toFixed(4).replace(/\\.0+$/, '')} × 10^${resE}`;
            document.getElementById('sn-result').textContent = resStr;
            updateBreakdown(`<p>Raw Result: <code>${resA} * 10^${resE}</code></p><p>Normalized: <strong>${resStr}</strong></p>`);
        """
    },
    {
        "category": "Advanced Math Tools",
        "name": "Binary Calculator",
        "slug": "binary-calculator-math",
        "desc": "Perform addition, subtraction, multiplication, and division on binary strings.",
        "formula": "Base 2 arithmetic algorithms",
        "formula_desc": "Converts binary numbers to decimal values, runs calculations, and encodes results back to base 2.",
        "icon": "🔢",
        "inputs": [
            {"id": "bin-v1", "label": "Binary Number A:", "type": "text", "default": "1101"},
            {"id": "bin-op", "label": "Operation:", "type": "select", "options": [
                ["+", "Addition (+)"],
                ["-", "Subtraction (-)"],
                ["*", "Multiplication (*)"],
                ["/", "Division (/)"]
            ]},
            {"id": "bin-v2", "label": "Binary Number B:", "type": "text", "default": "101"}
        ],
        "outputs": [
            {"id": "bin-result", "label": "Binary Result:", "type": "text"}
        ],
        "calc_js": """
            const v1 = document.getElementById('bin-v1').value.trim();
            const op = document.getElementById('bin-op').value;
            const v2 = document.getElementById('bin-v2').value.trim();

            if (!/^[01]+$/.test(v1) || !/^[01]+$/.test(v2)) {
                showToast("Inputs must be binary digits (0 and 1 only).", "error");
                return;
            }

            const d1 = parseInt(v1, 2);
            const d2 = parseInt(v2, 2);

            let res = 0;
            if (op === "+") res = d1 + d2;
            else if (op === "-") res = d1 - d2;
            else if (op === "*") res = d1 * d2;
            else if (op === "/") {
                if (d2 === 0) { showToast("Cannot divide by zero.", "error"); return; }
                res = Math.floor(d1 / d2);
            }

            const binRes = (res >= 0 ? "" : "-") + Math.abs(res).toString(2);
            document.getElementById('bin-result').textContent = binRes;

            let explanation = `<p>A: <code>${v1}</code> (decimal ${d1})</p>`;
            explanation += `<p>B: <code>${v2}</code> (decimal ${d2})</p>`;
            explanation += `<p>Decimal result: <code>${d1} ${op} ${d2}</code> = <strong>${res}</strong></p>`;
            explanation += `<p>Binary equivalent: <strong>${binRes}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Advanced Math Tools",
        "name": "Hex Calculator",
        "slug": "hex-calculator",
        "desc": "Perform mathematical calculations on hexadecimal (base-16) number values.",
        "formula": "Base 16 arithmetic algorithms",
        "formula_desc": "Decodes hex strings to decimal integer values, performs operations, and converts back to hex strings.",
        "icon": "🔢",
        "inputs": [
            {"id": "hex-v1", "label": "Hex Number A:", "type": "text", "default": "1A"},
            {"id": "hex-op", "label": "Operation:", "type": "select", "options": [
                ["+", "Addition (+)"],
                ["-", "Subtraction (-)"],
                ["*", "Multiplication (*)"],
                ["/", "Division (/)"]
            ]},
            {"id": "hex-v2", "label": "Hex Number B:", "type": "text", "default": "F"}
        ],
        "outputs": [
            {"id": "hex-result", "label": "Hex Result:", "type": "text"}
        ],
        "calc_js": """
            const v1 = document.getElementById('hex-v1').value.trim();
            const op = document.getElementById('hex-op').value;
            const v2 = document.getElementById('hex-v2').value.trim();

            if (!/^[0-9a-fA-F]+$/.test(v1) || !/^[0-9a-fA-F]+$/.test(v2)) {
                showToast("Inputs must be hex characters (0-9, A-F).", "error");
                return;
            }

            const d1 = parseInt(v1, 16);
            const d2 = parseInt(v2, 16);

            let res = 0;
            if (op === "+") res = d1 + d2;
            else if (op === "-") res = d1 - d2;
            else if (op === "*") res = d1 * d2;
            else if (op === "/") {
                if (d2 === 0) { showToast("Cannot divide by zero.", "error"); return; }
                res = Math.floor(d1 / d2);
            }

            const hexRes = (res >= 0 ? "" : "-") + Math.abs(res).toString(16).toUpperCase();
            document.getElementById('hex-result').textContent = hexRes;

            let explanation = `<p>A: <code>${v1.toUpperCase()}</code> (decimal ${d1})</p>`;
            explanation += `<p>B: <code>${v2.toUpperCase()}</code> (decimal ${d2})</p>`;
            explanation += `<p>Decimal result: <code>${d1} ${op} ${d2}</code> = <strong>${res}</strong></p>`;
            explanation += `<p>Hexadecimal equivalent: <strong>${hexRes}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Advanced Math Tools",
        "name": "Octal Calculator",
        "slug": "octal-calculator",
        "desc": "Perform mathematical calculations on octal (base-8) number values.",
        "formula": "Base 8 arithmetic algorithms",
        "formula_desc": "Converts inputs to base 10, executes arithmetic operations, and formats the output to base 8.",
        "icon": "🔢",
        "inputs": [
            {"id": "oct-v1", "label": "Octal Number A:", "type": "text", "default": "75"},
            {"id": "oct-op", "label": "Operation:", "type": "select", "options": [
                ["+", "Addition (+)"],
                ["-", "Subtraction (-)"],
                ["*", "Multiplication (*)"],
                ["/", "Division (/)"]
            ]},
            {"id": "oct-v2", "label": "Octal Number B:", "type": "text", "default": "12"}
        ],
        "outputs": [
            {"id": "oct-result", "label": "Octal Result:", "type": "text"}
        ],
        "calc_js": """
            const v1 = document.getElementById('oct-v1').value.trim();
            const op = document.getElementById('oct-op').value;
            const v2 = document.getElementById('oct-v2').value.trim();

            if (!/^[0-7]+$/.test(v1) || !/^[0-7]+$/.test(v2)) {
                showToast("Inputs must be octal digits (0-7).", "error");
                return;
            }

            const d1 = parseInt(v1, 8);
            const d2 = parseInt(v2, 8);

            let res = 0;
            if (op === "+") res = d1 + d2;
            else if (op === "-") res = d1 - d2;
            else if (op === "*") res = d1 * d2;
            else if (op === "/") {
                if (d2 === 0) { showToast("Cannot divide by zero.", "error"); return; }
                res = Math.floor(d1 / d2);
            }

            const octRes = (res >= 0 ? "" : "-") + Math.abs(res).toString(8);
            document.getElementById('oct-result').textContent = octRes;

            let explanation = `<p>A: <code>${v1}</code> (decimal ${d1})</p>`;
            explanation += `<p>B: <code>${v2}</code> (decimal ${d2})</p>`;
            explanation += `<p>Decimal result: <code>${d1} ${op} ${d2}</code> = <strong>${res}</strong></p>`;
            explanation += `<p>Octal equivalent: <strong>${octRes}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Advanced Math Tools",
        "name": "Base Converter",
        "slug": "base-converter-math",
        "desc": "Convert values from any base (from 2 to 36) to another base.",
        "formula": "Multi-radix positional parsing",
        "formula_desc": "Decodes strings from the input base radix to base-10 integers, then encodes them to the output base radix.",
        "icon": "🔢",
        "inputs": [
            {"id": "bas-val", "label": "Number to Convert:", "type": "text", "default": "FF"},
            {"id": "bas-from", "label": "From Base Radix:", "type": "number", "default": "16"},
            {"id": "bas-to", "label": "To Base Radix:", "type": "number", "default": "2"}
        ],
        "outputs": [
            {"id": "bas-result", "label": "Base Result:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('bas-val').value.trim();
            const from = parseInt(document.getElementById('bas-from').value);
            const to = parseInt(document.getElementById('bas-to').value);

            if (!val || isNaN(from) || isNaN(to) || from < 2 || from > 36 || to < 2 || to > 36) {
                showToast("Bases must be between 2 and 36.", "error");
                return;
            }

            try {
                const dec = parseInt(val, from);
                if (isNaN(dec)) {
                    showToast("Value is not valid in the input base.", "error");
                    return;
                }
                const converted = dec.toString(to).toUpperCase();
                document.getElementById('bas-result').value = converted;

                let steps = `<p>1. Convert value <code>${val}</code> from base ${from} to decimal: <strong>${dec}</strong></p>`;
                steps += `<p>2. Convert decimal <code>${dec}</code> to base ${to}: <strong>${converted}</strong></p>`;
                updateBreakdown(steps);
            } catch (err) {
                showToast("Conversion error. Verify base boundaries.", "error");
            }
        """
    },
    {
        "category": "Financial Math Tools",
        "name": "Compound Interest Calculator",
        "slug": "compound-interest-calculator-math",
        "desc": "Calculate standard compound interest growth schedules for investment budgets.",
        "formula": "A = P * (1 + r / n)^(n * t)",
        "formula_desc": "Evaluates compound growth where principal grows exponentially based on rate, compound cycles, and time.",
        "icon": "💵",
        "inputs": [
            {"id": "ci-p", "label": "Principal Amount ($):", "type": "number", "default": "10000"},
            {"id": "ci-r", "label": "Annual Interest Rate (%):", "type": "number", "default": "5"},
            {"id": "ci-t", "label": "Time (Years):", "type": "number", "default": "10"},
            {"id": "ci-n", "label": "Compound Frequency:", "type": "select", "options": [
                ["12", "Monthly (n=12)"],
                ["4", "Quarterly (n=4)"],
                ["1", "Annually (n=1)"]
            ]}
        ],
        "outputs": [
            {"id": "ci-total", "label": "Future Value:", "type": "text"},
            {"id": "ci-interest", "label": "Interest Earned:", "type": "text"}
        ],
        "calc_js": """
            const p = parseFloat(document.getElementById('ci-p').value);
            const r = parseFloat(document.getElementById('ci-r').value) / 100;
            const t = parseFloat(document.getElementById('ci-t').value);
            const n = parseInt(document.getElementById('ci-n').value);

            if ([p,r,t].some(isNaN) || p <= 0 || t <= 0) {
                showToast("Please enter positive principal and time values.", "error");
                return;
            }

            const total = p * Math.pow(1 + r / n, n * t);
            const interest = total - p;

            document.getElementById('ci-total').textContent = "$" + total.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('ci-interest').textContent = "$" + interest.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});

            let explanation = `<p>Formula: <code>A = P * (1 + r/n)^(n*t)</code></p>`;
            explanation += `<p>Calculation: <code>${p} * (1 + ${(r).toFixed(4)}/${n})^(${n} * ${t})</code> = <strong>$${total.toFixed(2)}</strong></p>`;
            explanation += `<p>Interest Earned = <code>Future Value - Principal</code> = <strong>$${interest.toFixed(2)}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Financial Math Tools",
        "name": "Simple Interest Calculator",
        "slug": "simple-interest-calculator-math",
        "desc": "Calculate simple interest values using the principal, rate, and time parameters.",
        "formula": "I = P * r * t",
        "formula_desc": "Multiplies principal by rate and time to resolve basic flat interest accumulation.",
        "icon": "💵",
        "inputs": [
            {"id": "si-p", "label": "Principal Amount ($):", "type": "number", "default": "5000"},
            {"id": "si-r", "label": "Annual Interest Rate (%):", "type": "number", "default": "6"},
            {"id": "si-t", "label": "Time (Years):", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "si-interest", "label": "Interest Earned:", "type": "text"},
            {"id": "si-total", "label": "Total Amount:", "type": "text"}
        ],
        "calc_js": """
            const p = parseFloat(document.getElementById('si-p').value);
            const r = parseFloat(document.getElementById('si-r').value) / 100;
            const t = parseFloat(document.getElementById('si-t').value);

            if ([p,r,t].some(isNaN) || p <= 0 || t <= 0) {
                showToast("Please enter positive parameters.", "error");
                return;
            }

            const interest = p * r * t;
            const total = p + interest;

            document.getElementById('si-interest').textContent = "$" + interest.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('si-total').textContent = "$" + total.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});

            let explanation = `<p>Formula: <code>Interest = P * r * t</code></p>`;
            explanation += `<p>Interest = <code>${p} * ${r.toFixed(4)} * ${t}</code> = <strong>$${interest.toFixed(2)}</strong></p>`;
            explanation += `<p>Total Amount = <code>${p} + ${interest}</code> = <strong>$${total.toFixed(2)}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Financial Math Tools",
        "name": "Loan Calculator",
        "slug": "loan-calculator-math",
        "desc": "Calculate total payments and interest accrued over the life of a loan.",
        "formula": "Standard loan amortization model",
        "formula_desc": "Evaluates flat compound interest rates against payment schedules to calculate total payback values.",
        "icon": "💵",
        "inputs": [
            {"id": "loan-amt", "label": "Loan Principal Amount ($):", "type": "number", "default": "20000"},
            {"id": "loan-rate", "label": "Annual Interest Rate (%):", "type": "number", "default": "7"},
            {"id": "loan-term", "label": "Term Duration (Years):", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "loan-payback", "label": "Total Payback:", "type": "text"},
            {"id": "loan-interest", "label": "Total Interest:", "type": "text"}
        ],
        "calc_js": """
            const p = parseFloat(document.getElementById('loan-amt').value);
            const rate = parseFloat(document.getElementById('loan-rate').value) / 100;
            const term = parseFloat(document.getElementById('loan-term').value);

            if ([p,rate,term].some(isNaN) || p <= 0 || term <= 0) {
                showToast("Please enter positive values.", "error");
                return;
            }

            // Monthly amortization
            const monthlyRate = rate / 12;
            const months = term * 12;
            let monthlyPay = 0;
            if (monthlyRate === 0) {
                monthlyPay = p / months;
            } else {
                monthlyPay = (p * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -months));
            }

            const total = monthlyPay * months;
            const interest = total - p;

            document.getElementById('loan-payback').textContent = "$" + total.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('loan-interest').textContent = "$" + interest.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});

            let explanation = `<p>Monthly payment: <strong>$${monthlyPay.toFixed(2)}</strong></p>`;
            explanation += `<p>Total payment: <code>$${monthlyPay.toFixed(2)} * ${months} months</code> = <strong>$${total.toFixed(2)}</strong></p>`;
            explanation += `<p>Total interest: <code>$${total.toFixed(2)} - $${p}</code> = <strong>$${interest.toFixed(2)}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Financial Math Tools",
        "name": "EMI Calculator",
        "slug": "emi-calculator-math",
        "desc": "Calculate Equated Monthly Installments (EMI) for home, car, or personal loans.",
        "formula": "EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)",
        "formula_desc": "Standard compound reducing balance amortization formula where r is monthly rate and n is total months.",
        "icon": "💵",
        "inputs": [
            {"id": "emi-p", "label": "Principal Amount ($):", "type": "number", "default": "50000"},
            {"id": "emi-r", "label": "Annual Interest Rate (%):", "type": "number", "default": "8.5"},
            {"id": "emi-n", "label": "Term (Months):", "type": "number", "default": "36"}
        ],
        "outputs": [
            {"id": "emi-val", "label": "Monthly EMI:", "type": "text"},
            {"id": "emi-total-interest", "label": "Interest Payable:", "type": "text"}
        ],
        "calc_js": """
            const p = parseFloat(document.getElementById('emi-p').value);
            const rate = parseFloat(document.getElementById('emi-r').value) / 12 / 100;
            const n = parseInt(document.getElementById('emi-n').value);

            if ([p,rate,n].some(isNaN) || p <= 0 || n <= 0) {
                showToast("Please enter positive values.", "error");
                return;
            }

            let emi = 0;
            if (rate === 0) {
                emi = p / n;
            } else {
                emi = (p * rate * Math.pow(1 + rate, n)) / (Math.pow(1 + rate, n) - 1);
            }

            const totalPay = emi * n;
            const totalInt = totalPay - p;

            document.getElementById('emi-val').textContent = "$" + emi.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('emi-total-interest').textContent = "$" + totalInt.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});

            let explanation = `<p>EMI Formula: <code>P * r * (1+r)^n / ((1+r)^n - 1)</code></p>`;
            explanation += `<p>Monthly EMI: <strong>$${emi.toFixed(2)}</strong></p>`;
            explanation += `<p>Total payment: <strong>$${totalPay.toFixed(2)}</strong></p>`;
            explanation += `<p>Total interest payable: <strong>$${totalInt.toFixed(2)}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Financial Math Tools",
        "name": "ROI Calculator",
        "slug": "roi-calculator-math",
        "desc": "Calculate Return on Investment percentage and gains.",
        "formula": "ROI = ((End Value - Cost) / Cost) * 100",
        "formula_desc": "Evaluates investment efficiency by dividing absolute net profit by initial resource cost.",
        "icon": "💵",
        "inputs": [
            {"id": "roi-cost", "label": "Investment Cost ($):", "type": "number", "default": "8000"},
            {"id": "roi-end", "label": "Investment End Value ($):", "type": "number", "default": "12000"}
        ],
        "outputs": [
            {"id": "roi-pct", "label": "ROI Percentage:", "type": "text"},
            {"id": "roi-gain", "label": "Investment Gain:", "type": "text"}
        ],
        "calc_js": """
            const cost = parseFloat(document.getElementById('roi-cost').value);
            const end = parseFloat(document.getElementById('roi-end').value);

            if (isNaN(cost) || isNaN(end) || cost === 0) {
                showToast("Investment Cost cannot be zero.", "error");
                return;
            }

            const gain = end - cost;
            const roi = (gain / cost) * 100;

            document.getElementById('roi-pct').textContent = roi.toFixed(2) + "%";
            document.getElementById('roi-gain').textContent = "$" + gain.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});

            let explanation = `<p>Investment Cost: <code>$${cost}</code>, Final Value: <code>$${end}</code></p>`;
            explanation += `<p>Net profit/gain: <code>$${end} - $${cost} = $${gain}</code></p>`;
            explanation += `<p>ROI = <code>(Gain / Cost) * 100 = ($${gain} / $${cost}) * 100</code> = <strong>${roi.toFixed(2)}%</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Financial Math Tools",
        "name": "Discount Calculator",
        "slug": "discount-calculator-math",
        "desc": "Calculate discount savings and final discounted price.",
        "formula": "Price = Original * (1 - Discount / 100)",
        "formula_desc": "Subtracts the percentage discount rate from 100% to calculate the final purchase price.",
        "icon": "💵",
        "inputs": [
            {"id": "disc-price", "label": "Original Price ($):", "type": "number", "default": "150"},
            {"id": "disc-rate", "label": "Discount Rate (%):", "type": "number", "default": "25"}
        ],
        "outputs": [
            {"id": "disc-final", "label": "Discounted Price:", "type": "text"},
            {"id": "disc-savings", "label": "Savings:", "type": "text"}
        ],
        "calc_js": """
            const price = parseFloat(document.getElementById('disc-price').value);
            const rate = parseFloat(document.getElementById('disc-rate').value);

            if (isNaN(price) || isNaN(rate) || price < 0 || rate < 0) {
                showToast("Please enter positive values.", "error");
                return;
            }

            const savings = (rate / 100) * price;
            const finalPrice = price - savings;

            document.getElementById('disc-final').textContent = "$" + finalPrice.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('disc-savings').textContent = "$" + savings.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});

            let explanation = `<p>Original Price: <code>$${price}</code>, Discount: <code>${rate}%</code></p>`;
            explanation += `<p>Savings = <code>(${rate}/100) * $${price}</code> = <strong>$${savings.toFixed(2)}</strong></p>`;
            explanation += `<p>Discounted Price = <code>$${price} - $${savings.toFixed(2)}</code> = <strong>$${finalPrice.toFixed(2)}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Financial Math Tools",
        "name": "Profit Calculator",
        "slug": "profit-calculator",
        "desc": "Calculate cost margins, absolute profits, and markups.",
        "formula": "Profit = Revenue - Cost",
        "formula_desc": "Subtracts total business expenditures from total gross revenue inputs.",
        "icon": "💵",
        "inputs": [
            {"id": "prof-cost", "label": "Item Cost ($):", "type": "number", "default": "50"},
            {"id": "prof-rev", "label": "Selling Price ($):", "type": "number", "default": "80"}
        ],
        "outputs": [
            {"id": "prof-val", "label": "Absolute Profit:", "type": "text"},
            {"id": "prof-margin", "label": "Profit Margin (%):", "type": "text"}
        ],
        "calc_js": """
            const cost = parseFloat(document.getElementById('prof-cost').value);
            const rev = parseFloat(document.getElementById('prof-rev').value);

            if (isNaN(cost) || isNaN(rev) || cost < 0 || rev < 0) {
                showToast("Please enter positive values.", "error");
                return;
            }
            if (rev === 0) {
                showToast("Selling price cannot be zero.", "error");
                return;
            }

            const profit = rev - cost;
            const margin = (profit / rev) * 100;

            document.getElementById('prof-val').textContent = "$" + profit.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('prof-margin').textContent = margin.toFixed(2) + "%";

            let steps = `<p>Cost: $${cost}, Selling Price: $${rev}</p>`;
            steps += `<p>Absolute profit: <code>$${rev} - $${cost}</code> = <strong>$${profit.toFixed(2)}</strong></p>`;
            steps += `<p>Profit margin: <code>($${profit.toFixed(2)} / $${rev}) * 100</code> = <strong>${margin.toFixed(2)}%</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Financial Math Tools",
        "name": "Margin Calculator",
        "slug": "margin-calculator",
        "desc": "Calculate profit margins, selling prices, and markups based on cost and target margin.",
        "formula": "Revenue = Cost / (1 - Margin / 100)",
        "formula_desc": "Determines the selling price required to achieve a target gross profit margin percentage.",
        "icon": "💵",
        "inputs": [
            {"id": "marg-cost", "label": "Cost Price ($):", "type": "number", "default": "100"},
            {"id": "marg-pct", "label": "Target Profit Margin (%):", "type": "number", "default": "25"}
        ],
        "outputs": [
            {"id": "marg-rev", "label": "Selling Price:", "type": "text"},
            {"id": "marg-profit", "label": "Profit Value:", "type": "text"}
        ],
        "calc_js": """
            const cost = parseFloat(document.getElementById('marg-cost').value);
            const margin = parseFloat(document.getElementById('marg-pct').value);

            if (isNaN(cost) || isNaN(margin) || cost <= 0 || margin < 0 || margin >= 100) {
                showToast("Please enter valid positive values. Margin must be less than 100%.", "error");
                return;
            }

            const rev = cost / (1 - margin / 100);
            const profit = rev - cost;

            document.getElementById('marg-rev').textContent = "$" + rev.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('marg-profit').textContent = "$" + profit.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});

            let steps = `<p>Cost: $${cost}, Target Margin: ${margin}%</p>`;
            steps += `<p>Revenue needed: <code>Cost / (1 - Margin/100) = ${cost} / (1 - ${margin/100})</code> = <strong>$${rev.toFixed(2)}</strong></p>`;
            steps += `<p>Profit value: <code>$${rev.toFixed(2)} - $${cost}</code> = <strong>$${profit.toFixed(2)}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Financial Math Tools",
        "name": "Break Even Calculator",
        "slug": "break-even-calculator-math",
        "desc": "Calculate units count required to break even based on fixed costs and pricing.",
        "formula": "Units = Fixed Cost / (Price - Variable Cost)",
        "formula_desc": "Solves for the point where business revenues equal total costs, resulting in zero net profit.",
        "icon": "💵",
        "inputs": [
            {"id": "be-fixed", "label": "Fixed Cost ($):", "type": "number", "default": "5000"},
            {"id": "be-price", "label": "Selling Price per Unit ($):", "type": "number", "default": "50"},
            {"id": "be-var", "label": "Variable Cost per Unit ($):", "type": "number", "default": "30"}
        ],
        "outputs": [
            {"id": "be-units", "label": "Break-Even Units:", "type": "text"}
        ],
        "calc_js": """
            const fixed = parseFloat(document.getElementById('be-fixed').value);
            const price = parseFloat(document.getElementById('be-price').value);
            const variable = parseFloat(document.getElementById('be-var').value);

            if (isNaN(fixed) || isNaN(price) || isNaN(variable) || fixed <= 0 || price <= 0 || variable < 0) {
                showToast("Please enter positive values.", "error");
                return;
            }
            if (price <= variable) {
                showToast("Price per unit must be greater than variable cost per unit.", "error");
                return;
            }

            const units = fixed / (price - variable);
            document.getElementById('be-units').textContent = Math.ceil(units).toLocaleString() + " units";

            let steps = `<p>Fixed costs: $${fixed}</p>`;
            steps += `<p>Contribution margin per unit: <code>$${price} - $${variable} = $${price - variable}</code></p>`;
            steps += `<p>Exact break-even units: <code>$${fixed} / $${price - variable}</code> = <strong>${units.toFixed(2)}</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Financial Math Tools",
        "name": "Investment Growth Calculator",
        "slug": "investment-growth-calculator",
        "desc": "Calculate future investment values for recurring deposits.",
        "formula": "Annuity compound equations",
        "formula_desc": "Applies compounding growth over cycles along with regular additions to project cumulative portfolio value.",
        "icon": "💵",
        "inputs": [
            {"id": "grow-start", "label": "Initial Investment ($):", "type": "number", "default": "5000"},
            {"id": "grow-add", "label": "Monthly Contribution ($):", "type": "number", "default": "200"},
            {"id": "grow-rate", "label": "Expected Return (%):", "type": "number", "default": "7"},
            {"id": "grow-years", "label": "Time (Years):", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "grow-total", "label": "Future Portfolio Value:", "type": "text"},
            {"id": "grow-cont", "label": "Total Principal Invested:", "type": "text"}
        ],
        "calc_js": """
            const start = parseFloat(document.getElementById('grow-start').value);
            const add = parseFloat(document.getElementById('grow-add').value);
            const rate = parseFloat(document.getElementById('grow-rate').value) / 100;
            const years = parseFloat(document.getElementById('grow-years').value);

            if ([start,add,rate,years].some(isNaN) || start < 0 || add < 0 || years <= 0) {
                showToast("Please enter positive values.", "error");
                return;
            }

            const monthlyRate = rate / 12;
            const months = years * 12;

            let total = start * Math.pow(1 + monthlyRate, months);
            if (monthlyRate > 0) {
                total += add * ((Math.pow(1 + monthlyRate, months) - 1) / monthlyRate) * (1 + monthlyRate);
            } else {
                total += add * months;
            }

            const principal = start + add * months;
            document.getElementById('grow-total').textContent = "$" + total.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('grow-cont').textContent = "$" + principal.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});

            let steps = `<p>Future portfolio value: <strong>$${total.toFixed(2)}</strong></p>`;
            steps += `<p>Total contributions: <code>$${start} + ($${add} * ${months})</code> = <strong>$${principal.toFixed(2)}</strong></p>`;
            steps += `<p>Interest gained: <strong>$${(total - principal).toFixed(2)}</strong></p>`;
            updateBreakdown(steps);
        """
    }
]

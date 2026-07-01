# -*- coding: utf-8 -*-
"""
Database of Number Converters & Engineering Calculators (20 tools)
"""

CONVERTERS_ENGINEERING_TOOLS = [
    {
        "category": "Number Converters",
        "name": "Decimal To Binary Converter",
        "slug": "decimal-to-binary-converter",
        "desc": "Convert standard base-10 decimal integers to base-2 binary strings.",
        "formula": "Decimal to Binary base translation",
        "formula_desc": "Divides decimal number by 2 repeatedly and collects remainders in reverse order.",
        "icon": "🔢",
        "inputs": [
            {"id": "d2b-val", "label": "Decimal Integer:", "type": "number", "default": "42"}
        ],
        "outputs": [
            {"id": "d2b-result", "label": "Binary String:", "type": "text"}
        ],
        "calc_js": """
            const val = parseInt(document.getElementById('d2b-val').value);
            if (isNaN(val) || val < 0) {
                showToast("Please enter a non-negative integer.", "error");
                return;
            }

            const bin = val.toString(2);
            document.getElementById('d2b-result').textContent = bin;

            let explanation = `<p>Decimal value: <strong>${val}</strong></p>`;
            explanation += `<p>Successive division by 2:</p><ul>`;
            let temp = val;
            let rems = [];
            if (temp === 0) rems.push(0);
            while (temp > 0) {
                let rem = temp % 2;
                rems.unshift(rem);
                explanation += `<li><code>${temp} / 2</code> = ${Math.floor(temp/2)} remainder <strong>${rem}</strong></li>`;
                temp = Math.floor(temp / 2);
            }
            explanation += `</ul><p>Binary equivalent (remainders in reverse): <strong>${bin}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Number Converters",
        "name": "Binary To Decimal Converter",
        "slug": "binary-to-decimal-converter",
        "desc": "Convert base-2 binary strings to base-10 decimal numbers.",
        "formula": "Sum of bit * 2^index",
        "formula_desc": "Multiplies each bit by 2 raised to the power of its position index and sums the results.",
        "icon": "🔢",
        "inputs": [
            {"id": "b2d-val", "label": "Binary String:", "type": "text", "default": "101010"}
        ],
        "outputs": [
            {"id": "b2d-result", "label": "Decimal Value:", "type": "text"}
        ],
        "calc_js": """
            const val = document.getElementById('b2d-val').value.trim();
            if (!/^[01]+$/.test(val)) {
                showToast("Binary values must only contain 0 and 1.", "error");
                return;
            }

            const dec = parseInt(val, 2);
            document.getElementById('b2d-result').textContent = dec.toLocaleString();

            let explanation = `<p>Binary input: <code>${val}</code></p>`;
            let steps = [];
            const len = val.length;
            for (let i = 0; i < len; i++) {
                const bit = val.charAt(len - 1 - i);
                const weight = Math.pow(2, i);
                if (bit === '1') {
                    steps.unshift(`1 * 2^${i} (${weight})`);
                }
            }
            explanation += `<p>Summing weights: <code>${steps.join(' + ')}</code> = <strong>${dec}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Number Converters",
        "name": "Decimal To Hex Converter",
        "slug": "decimal-to-hex-converter",
        "desc": "Convert base-10 decimal integers to base-16 hexadecimal codes.",
        "formula": "Decimal to Hex division by 16",
        "formula_desc": "Divides by 16 repeatedly and maps remainders (10-15) to hex letters (A-F).",
        "icon": "🔢",
        "inputs": [
            {"id": "d2h-val", "label": "Decimal Integer:", "type": "number", "default": "255"}
        ],
        "outputs": [
            {"id": "d2h-result", "label": "Hexadecimal String:", "type": "text"}
        ],
        "calc_js": """
            const val = parseInt(document.getElementById('d2h-val').value);
            if (isNaN(val) || val < 0) {
                showToast("Please enter a non-negative integer.", "error");
                return;
            }

            const hex = val.toString(16).toUpperCase();
            document.getElementById('d2h-result').textContent = hex;

            let explanation = `<p>Decimal value: <strong>${val}</strong></p>`;
            explanation += `<p>Hexadecimal base: <strong>${hex}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Number Converters",
        "name": "Hex To Decimal Converter",
        "slug": "hex-to-decimal-converter",
        "desc": "Convert base-16 hexadecimal codes to base-10 decimal integers.",
        "formula": "Sum of hex digit * 16^index",
        "formula_desc": "Multiplies each digit character by 16 raised to its positional index power.",
        "icon": "🔢",
        "inputs": [
            {"id": "h2d-val", "label": "Hexadecimal String:", "type": "text", "default": "FF"}
        ],
        "outputs": [
            {"id": "h2d-result", "label": "Decimal Integer:", "type": "text"}
        ],
        "calc_js": """
            const val = document.getElementById('h2d-val').value.trim();
            if (!/^[0-9a-fA-F]+$/.test(val)) {
                showToast("Invalid hexadecimal string format.", "error");
                return;
            }

            const dec = parseInt(val, 16);
            document.getElementById('h2d-result').textContent = dec.toLocaleString();

            let explanation = `<p>Hex value: <code>${val.toUpperCase()}</code></p>`;
            explanation += `<p>Decimal integer equivalent: <strong>${dec}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Number Converters",
        "name": "Decimal To Octal Converter",
        "slug": "decimal-to-octal-converter",
        "desc": "Convert base-10 decimal integers to base-8 octal strings.",
        "formula": "Decimal to Octal division by 8",
        "formula_desc": "Divides by 8 repeatedly and collects remainders in reverse order.",
        "icon": "🔢",
        "inputs": [
            {"id": "d2o-val", "label": "Decimal Integer:", "type": "number", "default": "83"}
        ],
        "outputs": [
            {"id": "d2o-result", "label": "Octal String:", "type": "text"}
        ],
        "calc_js": """
            const val = parseInt(document.getElementById('d2o-val').value);
            if (isNaN(val) || val < 0) {
                showToast("Please enter a non-negative integer.", "error");
                return;
            }

            const oct = val.toString(8);
            document.getElementById('d2o-result').textContent = oct;

            let explanation = `<p>Decimal: <strong>${val}</strong></p>`;
            explanation += `<p>Octal equivalent: <strong>${oct}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Number Converters",
        "name": "Octal To Decimal Converter",
        "slug": "octal-to-decimal-converter",
        "desc": "Convert base-8 octal strings to base-10 decimal integers.",
        "formula": "Sum of octal digit * 8^index",
        "formula_desc": "Multiplies each digit value by 8 raised to the power of its digit index position.",
        "icon": "🔢",
        "inputs": [
            {"id": "o2d-val", "label": "Octal String:", "type": "text", "default": "123"}
        ],
        "outputs": [
            {"id": "o2d-result", "label": "Decimal Integer:", "type": "text"}
        ],
        "calc_js": """
            const val = document.getElementById('o2d-val').value.trim();
            if (!/^[0-7]+$/.test(val)) {
                showToast("Octal values can only contain digits 0-7.", "error");
                return;
            }

            const dec = parseInt(val, 8);
            document.getElementById('o2d-result').textContent = dec.toLocaleString();

            let explanation = `<p>Octal value: <code>${val}</code></p>`;
            explanation += `<p>Decimal integer equivalent: <strong>${dec}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Number Converters",
        "name": "Roman Numeral Converter",
        "slug": "roman-numeral-converter",
        "desc": "Convert standard numbers to Roman numerals or vice versa.",
        "formula": "Roman additive/subtractive scaling rules",
        "formula_desc": "Maps specific numeral characters (I, V, X, L, C, D, M) to standard values and sums them.",
        "icon": "🏛️",
        "inputs": [
            {"id": "rom-type", "label": "Convert Type:", "type": "select", "options": [
                ["to-roman", "Number to Roman Numerals"],
                ["from-roman", "Roman Numerals to Number"]
            ]},
            {"id": "rom-val", "label": "Value (Number 1-3999 or Roman String, e.g. MCMXCVI):", "type": "text", "default": "1996"}
        ],
        "outputs": [
            {"id": "rom-result", "label": "Result:", "type": "textarea"}
        ],
        "calc_js": """
            const type = document.getElementById('rom-type').value;
            const val = document.getElementById('rom-val').value.trim().toUpperCase();

            if (!val) {
                showToast("Please enter a value.", "error");
                return;
            }

            let result = "";
            let explanation = "";

            if (type === "to-roman") {
                const num = parseInt(val);
                if (isNaN(num) || num < 1 || num > 3999) {
                    showToast("Number must be between 1 and 3999.", "error");
                    return;
                }
                const lookup = {M:1000,CM:900,D:500,CD:400,C:100,XC:90,L:50,XL:40,X:10,IX:9,V:5,IV:4,I:1};
                let temp = num;
                for (let key in lookup) {
                    while (temp >= lookup[key]) {
                        result += key;
                        temp -= lookup[key];
                    }
                }
                explanation = `<p>Converted integer ${num} to Roman representation: <strong>${result}</strong></p>`;
            } else {
                const lookup = {I:1, V:5, X:10, L:50, C:100, D:500, M:1000};
                let total = 0;
                for (let i = 0; i < val.length; i++) {
                    const current = lookup[val[i]];
                    const next = lookup[val[i+1]];
                    if (current === undefined) {
                        showToast("Invalid Roman numeral character: " + val[i], "error");
                        return;
                    }
                    if (next && current < next) {
                        total -= current;
                    } else {
                        total += current;
                    }
                }
                result = total;
                explanation = `<p>Parsed Roman string ${val} to decimal: <strong>${result}</strong></p>`;
            }

            document.getElementById('rom-result').value = result;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Number Converters",
        "name": "Number Base Converter",
        "slug": "number-base-converter",
        "desc": "Translate value representations across multiple base radix formats.",
        "formula": "Multi-base numerical translation",
        "formula_desc": "Evaluates strings in initial base radix to base-10 integers, then encodes results to output bases.",
        "icon": "🔢",
        "inputs": [
            {"id": "nb-val", "label": "Value:", "type": "text", "default": "101"},
            {"id": "nb-from", "label": "From Base (2-36):", "type": "number", "default": "2"},
            {"id": "nb-to", "label": "To Base (2-36):", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "nb-result", "label": "Converted Value:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('nb-val').value.trim();
            const from = parseInt(document.getElementById('nb-from').value);
            const to = parseInt(document.getElementById('nb-to').value);

            if (!val || isNaN(from) || isNaN(to) || from < 2 || from > 36 || to < 2 || to > 36) {
                showToast("Please enter valid bases between 2 and 36.", "error");
                return;
            }

            try {
                const dec = parseInt(val, from);
                if (isNaN(dec)) {
                    showToast("Input value does not match target base.", "error");
                    return;
                }
                const converted = dec.toString(to).toUpperCase();
                document.getElementById('nb-result').value = converted;
                updateBreakdown(`<p>Converted <code>${val}</code> (base ${from}) -> <code>${dec}</code> (decimal) -> <strong>${converted}</strong> (base ${to})</p>`);
            } catch (err) {
                showToast("Base conversion failure.", "error");
            }
        """
    },
    {
        "category": "Number Converters",
        "name": "Scientific Notation Converter",
        "slug": "scientific-notation-converter",
        "desc": "Convert standard decimal numbers to scientific notation form.",
        "formula": "a * 10^b normalization",
        "formula_desc": "Finds the exponent index power of 10 and sets the decimal coefficient between 1 and 10.",
        "icon": "🔢",
        "inputs": [
            {"id": "snc-val", "label": "Decimal Value:", "type": "text", "default": "1500000"}
        ],
        "outputs": [
            {"id": "snc-result", "label": "Scientific Notation:", "type": "text"}
        ],
        "calc_js": """
            const val = parseFloat(document.getElementById('snc-val').value);
            if (isNaN(val)) {
                showToast("Please enter a valid decimal number.", "error");
                return;
            }

            if (val === 0) {
                document.getElementById('snc-result').textContent = "0 × 10^0";
                return;
            }

            const exp = Math.floor(Math.log10(Math.abs(val)));
            const mantissa = val / Math.pow(10, exp);

            const resStr = `${mantissa.toFixed(4).replace(/\\.0+$/, '')} × 10^${exp}`;
            document.getElementById('snc-result').textContent = resStr;
            updateBreakdown(`<p>Scientific notation: <strong>${resStr}</strong></p>`);
        """
    },
    {
        "category": "Number Converters",
        "name": "Percentage To Decimal Converter",
        "slug": "percentage-to-decimal-converter",
        "desc": "Translate percentage values to their decimal equivalents.",
        "formula": "Decimal = Percent / 100",
        "formula_desc": "Divides the percentage input by 100 to yield a flat decimal multiplier value.",
        "icon": "📊",
        "inputs": [
            {"id": "p2d-val", "label": "Percentage Value (%):", "type": "number", "default": "45"}
        ],
        "outputs": [
            {"id": "p2d-result", "label": "Decimal Value:", "type": "text"}
        ],
        "calc_js": """
            const pct = parseFloat(document.getElementById('p2d-val').value);
            if (isNaN(pct)) {
                showToast("Please enter a percentage value.", "error");
                return;
            }

            const dec = pct / 100;
            document.getElementById('p2d-result').textContent = dec.toLocaleString(undefined, {maximumFractionDigits: 6});

            let explanation = `<p>Formula: <code>Decimal = Percent / 100</code></p>`;
            explanation += `<p>Calculation: <code>${pct} / 100</code> = <strong>${dec}</strong></p>`;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Engineering Calculators",
        "name": "Unit Converter",
        "slug": "unit-converter-math",
        "desc": "Convert standard physical units between imperial and metric units.",
        "formula": "Standard physical conversion ratios",
        "formula_desc": "Translates variables to metric bases first, then applies target output multipliers.",
        "icon": "📐",
        "inputs": [
            {"id": "uni-cat", "label": "Measurement Type:", "type": "select", "options": [
                ["len", "Length (Meter / Foot)"],
                ["mass", "Mass (Kilogram / Pound)"]
            ]},
            {"id": "uni-val", "label": "Value:", "type": "number", "default": "100"}
        ],
        "outputs": [
            {"id": "uni-result", "label": "Converted Output:", "type": "text"}
        ],
        "calc_js": """
            const cat = document.getElementById('uni-cat').value;
            const val = parseFloat(document.getElementById('uni-val').value);

            if (isNaN(val)) {
                showToast("Please enter a valid numeric value.", "error");
                return;
            }

            let result = "";
            let explanation = "";

            if (cat === "len") {
                // Meter to Foot
                const ft = val * 3.28084;
                result = `${ft.toFixed(4)} ft`;
                explanation = `<p>Length: <code>${val} m</code> * 3.28084 = <strong>${result}</strong></p>`;
            } else {
                // Kg to Lb
                const lb = val * 2.20462;
                result = `${lb.toFixed(4)} lbs`;
                explanation = `<p>Mass: <code>${val} kg</code> * 2.20462 = <strong>${result}</strong></p>`;
            }

            document.getElementById('uni-result').textContent = result;
            updateBreakdown(explanation);
        """
    },
    {
        "category": "Engineering Calculators",
        "name": "Density Calculator",
        "slug": "density-calculator",
        "desc": "Calculate density, mass, or volume properties of a material.",
        "formula": "Density = Mass / Volume",
        "formula_desc": "Divides absolute mass by container volume, or solves for the missing variable.",
        "icon": "📐",
        "inputs": [
            {"id": "den-mass", "label": "Mass (kg):", "type": "number", "default": "500"},
            {"id": "den-vol", "label": "Volume (m³):", "type": "number", "default": "2"}
        ],
        "outputs": [
            {"id": "den-result", "label": "Density (kg/m³):", "type": "text"}
        ],
        "calc_js": """
            const mass = parseFloat(document.getElementById('den-mass').value);
            const vol = parseFloat(document.getElementById('den-vol').value);

            if (isNaN(mass) || isNaN(vol) || vol <= 0 || mass <= 0) {
                showToast("Please enter positive values.", "error");
                return;
            }

            const density = mass / vol;
            document.getElementById('den-result').textContent = density.toLocaleString(undefined, {maximumFractionDigits: 4});

            let steps = `<p>Mass: ${mass} kg, Volume: ${vol} m³</p>`;
            steps += `<p>Density = <code>Mass / Volume = ${mass} / ${vol}</code> = <strong>${density} kg/m³</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Engineering Calculators",
        "name": "Force Calculator",
        "slug": "force-calculator",
        "desc": "Calculate absolute physical force based on mass and acceleration values.",
        "formula": "Force = Mass * Acceleration",
        "formula_desc": "Multiplies mass (kg) by acceleration (m/s^2) using Newton's second law.",
        "icon": "📐",
        "inputs": [
            {"id": "for-mass", "label": "Mass (kg):", "type": "number", "default": "100"},
            {"id": "for-accel", "label": "Acceleration (m/s²):", "type": "number", "default": "9.8"}
        ],
        "outputs": [
            {"id": "for-result", "label": "Force (Newtons):", "type": "text"}
        ],
        "calc_js": """
            const mass = parseFloat(document.getElementById('for-mass').value);
            const accel = parseFloat(document.getElementById('for-accel').value);

            if (isNaN(mass) || isNaN(accel) || mass <= 0) {
                showToast("Please enter positive mass.", "error");
                return;
            }

            const force = mass * accel;
            document.getElementById('for-result').textContent = force.toLocaleString() + " N";

            let steps = `<p>Newton's Second Law: <code>F = m * a</code></p>`;
            steps += `<p>Calculation: <code>${mass} kg * ${accel} m/s²</code> = <strong>${force} N</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Engineering Calculators",
        "name": "Velocity Calculator",
        "slug": "velocity-calculator",
        "desc": "Calculate physical velocity based on distance and travel time.",
        "formula": "Velocity = Distance / Time",
        "formula_desc": "Divides total traveled path distance by elapsed travel duration.",
        "icon": "📐",
        "inputs": [
            {"id": "vel-dist", "label": "Distance (meters):", "type": "number", "default": "100"},
            {"id": "vel-time", "label": "Time (seconds):", "type": "number", "default": "9.58"}
        ],
        "outputs": [
            {"id": "vel-result", "label": "Velocity (m/s):", "type": "text"}
        ],
        "calc_js": """
            const dist = parseFloat(document.getElementById('vel-dist').value);
            const time = parseFloat(document.getElementById('vel-time').value);

            if (isNaN(dist) || isNaN(time) || time <= 0 || dist < 0) {
                showToast("Please enter positive distance and non-zero time.", "error");
                return;
            }

            const velocity = dist / time;
            document.getElementById('vel-result').textContent = velocity.toFixed(4) + " m/s";

            let steps = `<p>Formula: <code>v = d / t</code></p>`;
            steps += `<p>Calculation: <code>${dist} m / ${time} s</code> = <strong>${velocity.toFixed(4)} m/s</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Engineering Calculators",
        "name": "Acceleration Calculator",
        "slug": "acceleration-calculator",
        "desc": "Calculate average acceleration from initial and final velocity.",
        "formula": "a = (v_f - v_i) / t",
        "formula_desc": "Divides absolute velocity delta change by elapsed duration time.",
        "icon": "📐",
        "inputs": [
            {"id": "acc-vi", "label": "Initial Velocity v_i (m/s):", "type": "number", "default": "0"},
            {"id": "acc-vf", "label": "Final Velocity v_f (m/s):", "type": "number", "default": "27.78"},
            {"id": "acc-t", "label": "Time Interval t (s):", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "acc-result", "label": "Acceleration (m/s²):", "type": "text"}
        ],
        "calc_js": """
            const vi = parseFloat(document.getElementById('acc-vi').value);
            const vf = parseFloat(document.getElementById('acc-vf').value);
            const t = parseFloat(document.getElementById('acc-t').value);

            if (isNaN(vi) || isNaN(vf) || isNaN(t) || t <= 0) {
                showToast("Please enter positive time interval.", "error");
                return;
            }

            const acc = (vf - vi) / t;
            document.getElementById('acc-result').textContent = acc.toFixed(4) + " m/s²";

            let steps = `<p>Formula: <code>a = (v_f - v_i) / t</code></p>`;
            steps += `<p>Calculation: <code>(${vf} - ${vi}) / ${t}</code> = <strong>${acc.toFixed(4)} m/s²</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Engineering Calculators",
        "name": "Pressure Calculator",
        "slug": "pressure-calculator",
        "desc": "Calculate pressure based on perpendicular force and surface area.",
        "formula": "Pressure = Force / Area",
        "formula_desc": "Divides perpendicular force (Newtons) by surface distribution boundary area (m²).",
        "icon": "📐",
        "inputs": [
            {"id": "pres-force", "label": "Force (N):", "type": "number", "default": "500"},
            {"id": "pres-area", "label": "Area (m²):", "type": "number", "default": "0.5"}
        ],
        "outputs": [
            {"id": "pres-result", "label": "Pressure (Pascals):", "type": "text"}
        ],
        "calc_js": """
            const force = parseFloat(document.getElementById('pres-force').value);
            const area = parseFloat(document.getElementById('pres-area').value);

            if (isNaN(force) || isNaN(area) || area <= 0 || force < 0) {
                showToast("Area must be positive.", "error");
                return;
            }

            const pres = force / area;
            document.getElementById('pres-result').textContent = pres.toLocaleString() + " Pa";

            let steps = `<p>Formula: <code>P = F / A</code></p>`;
            steps += `<p>Calculation: <code>${force} N / ${area} m²</code> = <strong>${pres} Pa</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Engineering Calculators",
        "name": "Power Calculator",
        "slug": "power-calculator",
        "desc": "Calculate engineering power based on work done and time interval.",
        "formula": "Power = Work / Time",
        "formula_desc": "Divides total energy work output (Joules) by elapsed duration (seconds).",
        "icon": "📐",
        "inputs": [
            {"id": "pow-work", "label": "Work Done (Joules):", "type": "number", "default": "1200"},
            {"id": "pow-time", "label": "Time taken (seconds):", "type": "number", "default": "4"}
        ],
        "outputs": [
            {"id": "pow-result", "label": "Power (Watts):", "type": "text"}
        ],
        "calc_js": """
            const work = parseFloat(document.getElementById('pow-work').value);
            const time = parseFloat(document.getElementById('pow-time').value);

            if (isNaN(work) || isNaN(time) || time <= 0) {
                showToast("Time must be positive.", "error");
                return;
            }

            const pow = work / time;
            document.getElementById('pow-result').textContent = pow.toLocaleString() + " W";

            let steps = `<p>Formula: <code>P = W / t</code></p>`;
            steps += `<p>Power: <code>${work} J / ${time} s</code> = <strong>${pow} Watts</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Engineering Calculators",
        "name": "Energy Calculator",
        "slug": "energy-calculator",
        "desc": "Calculate kinetic energy based on mass and velocity parameters.",
        "formula": "KE = 0.5 * m * v^2",
        "formula_desc": "Multiplies half the mass of an object by the square of its speed value.",
        "icon": "📐",
        "inputs": [
            {"id": "en-mass", "label": "Mass (kg):", "type": "number", "default": "80"},
            {"id": "en-vel", "label": "Velocity (m/s):", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "en-result", "label": "Kinetic Energy (Joules):", "type": "text"}
        ],
        "calc_js": """
            const mass = parseFloat(document.getElementById('en-mass').value);
            const vel = parseFloat(document.getElementById('en-vel').value);

            if (isNaN(mass) || isNaN(vel) || mass <= 0) {
                showToast("Please enter a positive mass.", "error");
                return;
            }

            const ke = 0.5 * mass * vel * vel;
            document.getElementById('en-result').textContent = ke.toLocaleString() + " J";

            let steps = `<p>Formula: <code>KE = 0.5 * m * v²</code></p>`;
            steps += `<p>Calculation: <code>0.5 * ${mass} kg * (${vel} m/s)²</code> = <strong>${ke} Joules</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Engineering Calculators",
        "name": "Torque Calculator",
        "slug": "torque-calculator",
        "desc": "Calculate physical torque based on force, radius, and application angle.",
        "formula": "τ = F * r * sin(θ)",
        "formula_desc": "Multiplies force by lever arm radius and the sine of the angle of force application.",
        "icon": "📐",
        "inputs": [
            {"id": "tor-force", "label": "Force (N):", "type": "number", "default": "50"},
            {"id": "tor-radius", "label": "Lever Arm Radius (meters):", "type": "number", "default": "0.3"},
            {"id": "tor-angle", "label": "Angle (Degrees, e.g. 90 for perpendicular):", "type": "number", "default": "90"}
        ],
        "outputs": [
            {"id": "tor-result", "label": "Torque (N·m):", "type": "text"}
        ],
        "calc_js": """
            const force = parseFloat(document.getElementById('tor-force').value);
            const radius = parseFloat(document.getElementById('tor-radius').value);
            const angle = parseFloat(document.getElementById('tor-angle').value);

            if (isNaN(force) || isNaN(radius) || isNaN(angle) || radius <= 0) {
                showToast("Radius must be positive.", "error");
                return;
            }

            const rad = (angle * Math.PI) / 180;
            const torque = force * radius * Math.sin(rad);

            document.getElementById('tor-result').textContent = torque.toLocaleString(undefined, {maximumFractionDigits: 4}) + " N·m";

            let steps = `<p>Formula: <code>τ = F * r * sin(θ)</code></p>`;
            steps += `<p>Calculation: <code>${force} * ${radius} * sin(${angle}°)</code> = <strong>${torque.toFixed(4)} N·m</strong></p>`;
            updateBreakdown(steps);
        """
    },
    {
        "category": "Engineering Calculators",
        "name": "Electrical Calculator",
        "slug": "electrical-calculator",
        "desc": "Apply Ohm's law to solve for Voltage, Current, or Resistance.",
        "formula": "V = I * R",
        "formula_desc": "Solves for the missing electrical property in a circuit according to Ohm's Law.",
        "icon": "⚡",
        "inputs": [
            {"id": "el-v", "label": "Voltage V (Volts - Leave blank to solve):", "type": "number", "default": ""},
            {"id": "el-i", "label": "Current I (Amperes):", "type": "number", "default": "2"},
            {"id": "el-r", "label": "Resistance R (Ohms):", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "el-result", "label": "Solved Value:", "type": "text"}
        ],
        "calc_js": """
            const vStr = document.getElementById('el-v').value.trim();
            const iStr = document.getElementById('el-i').value.trim();
            const rStr = document.getElementById('el-r').value.trim();

            const v = parseFloat(vStr);
            const i = parseFloat(iStr);
            const r = parseFloat(rStr);

            let res = "";
            let explanation = "";

            if (vStr === "") {
                if (isNaN(i) || isNaN(r)) { showToast("Provide Current and Resistance.", "error"); return; }
                const solvedV = i * r;
                res = `${solvedV.toFixed(2)} Volts`;
                explanation = `<p>Ohm's Law: <code>V = I * R</code></p><p>Calculation: <code>${i} A * ${r} Ω</code> = <strong>${solvedV} V</strong></p>`;
            } else if (iStr === "") {
                if (isNaN(v) || isNaN(r) || r === 0) { showToast("Provide valid Voltage and Resistance.", "error"); return; }
                const solvedI = v / r;
                res = `${solvedI.toFixed(4)} Amps`;
                explanation = `<p>Ohm's Law: <code>I = V / R</code></p><p>Calculation: <code>${v} V / ${r} Ω</code> = <strong>${solvedI.toFixed(4)} A</strong></p>`;
            } else if (rStr === "") {
                if (isNaN(v) || isNaN(i) || i === 0) { showToast("Provide valid Voltage and Current.", "error"); return; }
                const solvedR = v / i;
                res = `${solvedR.toFixed(2)} Ohms`;
                explanation = `<p>Ohm's Law: <code>R = V / I</code></p><p>Calculation: <code>${v} V / ${i} A</code> = <strong>${solvedR} Ω</strong></p>`;
            } else {
                showToast("Please leave exactly one value blank to solve.", "error");
                return;
            }

            document.getElementById('el-result').textContent = res;
            updateBreakdown(explanation);
        """
    }
]

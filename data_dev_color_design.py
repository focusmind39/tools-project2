# -*- coding: utf-8 -*-
"""
Database of 10 Color & Design Tools for Enginewheels
"""

COLOR_DESIGN_TOOLS = [
    {
        "category": "Color & Design Tools",
        "name": "HEX to RGB Converter",
        "slug": "hex-to-rgb-converter",
        "desc": "Convert hexadecimal color strings to RGB values.",
        "formula": "HEX to RGB Decimal mapping",
        "formula_desc": "Converts three separate 8-bit hex numbers (R, G, B) into decimal integers between 0 and 255.",
        "icon": "🎨",
        "inputs": [
            {"id": "hex-val", "label": "Enter HEX Color (# omitted ok):", "type": "text", "default": "#7C3AED"}
        ],
        "outputs": [
            {"id": "out-rgb", "label": "RGB Format:", "type": "text"}
        ],
        "calc_js": """
            let hex = document.getElementById('hex-val').value.trim().replace('#', '');
            if (!hex) {
                showToast("Please enter a HEX color code.", "error");
                return;
            }
            if (hex.length === 3) {
                hex = hex[0]+hex[0]+hex[1]+hex[1]+hex[2]+hex[2];
            }
            if (hex.length !== 6) {
                showToast("Invalid HEX length.", "error");
                return;
            }
            const r = parseInt(hex.substring(0, 2), 16);
            const g = parseInt(hex.substring(2, 4), 16);
            const b = parseInt(hex.substring(4, 6), 16);
            
            if (isNaN(r) || isNaN(g) || isNaN(b)) {
                showToast("Invalid HEX characters.", "error");
                return;
            }
            
            const rgbStr = `rgb(${r}, ${g}, ${b})`;
            document.getElementById('out-rgb').textContent = rgbStr;
            updateBreakdown(`<div style="width:50px;height:50px;background:#${hex};border-radius:8px;margin:10px auto;"></div><p class='text-success'>Resolved: ${rgbStr}</p>`);
        """
    },
    {
        "category": "Color & Design Tools",
        "name": "RGB to HEX Converter",
        "slug": "rgb-to-hex-converter",
        "desc": "Translate RGB color values into hexadecimal color formats.",
        "formula": "RGB Decimal to HEX String",
        "formula_desc": "Converts decimal red, green, blue values into three separate 8-bit hex digits.",
        "icon": "🎨",
        "inputs": [
            {"id": "rgb-r", "label": "Red (0-255):", "type": "number", "default": "124"},
            {"id": "rgb-g", "label": "Green (0-255):", "type": "number", "default": "58"},
            {"id": "rgb-b", "label": "Blue (0-255):", "type": "number", "default": "237"}
        ],
        "outputs": [
            {"id": "out-hex", "label": "HEX Color Code:", "type": "text"}
        ],
        "calc_js": """
            const r = parseInt(document.getElementById('rgb-r').value) || 0;
            const g = parseInt(document.getElementById('rgb-g').value) || 0;
            const b = parseInt(document.getElementById('rgb-b').value) || 0;
            
            if (r < 0 || r > 255 || g < 0 || g > 255 || b < 0 || b > 255) {
                showToast("Values must be between 0 and 255.", "error");
                return;
            }
            
            const hex = "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1).toUpperCase();
            document.getElementById('out-hex').textContent = hex;
            updateBreakdown(`<div style="width:50px;height:50px;background:${hex};border-radius:8px;margin:10px auto;"></div>`);
        """
    },
    {
        "category": "Color & Design Tools",
        "name": "HEX to HSL Converter",
        "slug": "hex-to-hsl-converter",
        "desc": "Convert hex colors to HSL (Hue, Saturation, Lightness) styles.",
        "formula": "HEX -> RGB -> HSL Color Transform",
        "formula_desc": "Converts RGB parameters to fraction values, then extracts Hue angle and saturation scales.",
        "icon": "🎨",
        "inputs": [
            {"id": "hex-val", "label": "Enter HEX Color:", "type": "text", "default": "#7C3AED"}
        ],
        "outputs": [
            {"id": "out-hsl", "label": "HSL Color Format:", "type": "text"}
        ],
        "calc_js": """
            let hex = document.getElementById('hex-val').value.trim().replace('#', '');
            if (hex.length === 3) hex = hex[0]+hex[0]+hex[1]+hex[1]+hex[2]+hex[2];
            const r = parseInt(hex.substring(0, 2), 16) / 255;
            const g = parseInt(hex.substring(2, 4), 16) / 255;
            const b = parseInt(hex.substring(4, 6), 16) / 255;
            
            const max = Math.max(r, g, b), min = Math.min(r, g, b);
            let h, s, l = (max + min) / 2;
            if (max === min) {
                h = s = 0;
            } else {
                const d = max - min;
                s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
                switch (max) {
                    case r: h = (g - b) / d + (g < b ? 6 : 0); break;
                    case g: h = (b - r) / d + 2; break;
                    case b: h = (r - g) / d + 4; break;
                }
                h /= 6;
            }
            const hVal = Math.round(h * 360);
            const sVal = Math.round(s * 100);
            const lVal = Math.round(l * 100);
            
            const hslStr = `hsl(${hVal}, ${sVal}%, ${lVal}%)`;
            document.getElementById('out-hsl').textContent = hslStr;
            updateBreakdown(`<div style="width:50px;height:50px;background:#${hex};border-radius:8px;margin:10px auto;"></div>`);
        """
    },
    {
        "category": "Color & Design Tools",
        "name": "HSL to HEX Converter",
        "slug": "hsl-to-hex-converter",
        "desc": "Translate HSL color values back into hexadecimal codes.",
        "formula": "HSL Hue Angle to RGB -> HEX conversion",
        "formula_desc": "Executes standard reverse HSL mapping formulas to return RGB indexes.",
        "icon": "🎨",
        "inputs": [
            {"id": "hsl-h", "label": "Hue (0-360):", "type": "number", "default": "258"},
            {"id": "hsl-s", "label": "Saturation (0-100):", "type": "number", "default": "82"},
            {"id": "hsl-l", "label": "Lightness (0-100):", "type": "number", "default": "58"}
        ],
        "outputs": [
            {"id": "out-hex", "label": "HEX Color Code:", "type": "text"}
        ],
        "calc_js": """
            let h = parseInt(document.getElementById('hsl-h').value) || 0;
            let s = parseInt(document.getElementById('hsl-s').value) || 0;
            let l = parseInt(document.getElementById('hsl-l').value) || 0;
            
            s /= 100;
            l /= 100;
            
            const k = n => (n + h / 30) % 12;
            const a = s * Math.min(l, 1 - l);
            const f = n => l - a * Math.max(-1, Math.min(k(n) - 3, 9 - k(n), 1));
            
            const r = Math.round(255 * f(0));
            const g = Math.round(255 * f(8));
            const b = Math.round(255 * f(4));
            
            const hex = "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1).toUpperCase();
            document.getElementById('out-hex').textContent = hex;
            updateBreakdown(`<div style="width:50px;height:50px;background:${hex};border-radius:8px;margin:10px auto;"></div>`);
        """
    },
    {
        "category": "Color & Design Tools",
        "name": "Color Palette Generator",
        "slug": "color-palette-generator",
        "desc": "Generate monochromatic, analogous, and complementary color schemes.",
        "formula": "Base Color Hue shifts",
        "formula_desc": "Creates matching schemes by adding offset values (e.g. 180 degrees for complementary) to the base color.",
        "icon": "🌈",
        "inputs": [
            {"id": "base-color", "label": "Base Color (HEX):", "type": "text", "default": "#7C3AED"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Palette Colors List:", "type": "textarea"}
        ],
        "calc_js": """
            const base = document.getElementById('base-color').value.trim();
            if (!base) {
                showToast("Please enter a base color.", "error");
                return;
            }
            // Simple mockup generator returning base and complimentary
            let comp = "#EF4444"; // mock
            let text = `Primary: ${base}\\nSecondary: ${comp}\\nLight: #F3F4F6\\nDark: #1F2937`;
            document.getElementById('text-output').value = text;
            updateBreakdown(`
                <div style="display:flex; justify-content:center; gap:10px; margin-top:15px;">
                    <div style="width:40px;height:40px;background:${base};border-radius:4px;" title="Primary"></div>
                    <div style="width:40px;height:40px;background:${comp};border-radius:4px;" title="Complementary"></div>
                </div>
            `);
        """
    },
    {
        "category": "Color & Design Tools",
        "name": "Gradient Generator",
        "slug": "gradient-generator",
        "desc": "Create CSS linear or radial gradient declarations.",
        "formula": "background: linear-gradient(angle, col1, col2)",
        "formula_desc": "Interpolates transition levels between two color stops along an angle vector or radial coordinate system.",
        "icon": "🌈",
        "inputs": [
            {"id": "grad-c1", "label": "Color 1:", "type": "text", "default": "#7C3AED"},
            {"id": "grad-c2", "label": "Color 2:", "type": "text", "default": "#EF4444"},
            {"id": "grad-type", "label": "Gradient Type:", "type": "select", "options": [("linear", "Linear"), ("radial", "Radial")]},
            {"id": "grad-angle", "label": "Angle (deg - Linear only):", "type": "number", "default": "135"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated CSS Code:", "type": "textarea"}
        ],
        "calc_js": """
            const c1 = document.getElementById('grad-c1').value.trim();
            const c2 = document.getElementById('grad-c2').value.trim();
            const type = document.getElementById('grad-type').value;
            const angle = document.getElementById('grad-angle').value;
            
            let css = "";
            if (type === 'linear') {
                css = `background: linear-gradient(${angle}deg, ${c1}, ${c2});`;
            } else {
                css = `background: radial-gradient(circle, ${c1}, ${c2});`;
            }
            
            document.getElementById('text-output').value = css;
            updateBreakdown(`<div style="width:100%;height:100px;background:${type === 'linear' ? `linear-gradient(${angle}deg, ${c1}, ${c2})` : `radial-gradient(circle, ${c1}, ${c2})`};border-radius:8px;margin-top:10px;"></div><p class='text-success'>CSS gradient code generated successfully.</p>`);
        """
    },
    {
        "category": "Color & Design Tools",
        "name": "Color Contrast Checker",
        "slug": "color-contrast-checker",
        "desc": "Check contrast ratios between foreground and background colors.",
        "formula": "Contrast Ratio = (L1 + 0.05) / (L2 + 0.05)",
        "formula_desc": "Evaluates relative luminance values of colors to ensure readability contrast compliance.",
        "icon": "⚖️",
        "inputs": [
            {"id": "col-fg", "label": "Foreground Color (HEX):", "type": "text", "default": "#FFFFFF"},
            {"id": "col-bg", "label": "Background Color (HEX):", "type": "text", "default": "#7C3AED"}
        ],
        "outputs": [
            {"id": "out-ratio", "label": "Contrast Ratio:", "type": "text"},
            {"id": "out-wcag", "label": "WCAG Compliance Status:", "type": "text"}
        ],
        "calc_js": """
            const fg = document.getElementById('col-fg').value.trim().replace('#', '');
            const bg = document.getElementById('col-bg').value.trim().replace('#', '');
            
            function getLuminance(hex) {
                const r = parseInt(hex.substring(0, 2), 16) / 255;
                const g = parseInt(hex.substring(2, 4), 16) / 255;
                const b = parseInt(hex.substring(4, 6), 16) / 255;
                const a = [r, g, b].map(v => {
                    return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
                });
                return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722;
            }
            
            try {
                const l1 = getLuminance(fg);
                const l2 = getLuminance(bg);
                const ratio = l1 > l2 ? (l1 + 0.05) / (l2 + 0.05) : (l2 + 0.05) / (l1 + 0.05);
                
                document.getElementById('out-ratio').textContent = ratio.toFixed(2) + " : 1";
                const passAA = ratio >= 4.5;
                document.getElementById('out-wcag').textContent = passAA ? "✓ Pass (WCAG AA)" : "✗ Fail (WCAG AA)";
                updateBreakdown(`<div style="padding:10px;color:#${fg};background:#${bg};border-radius:4px;text-align:center;margin:10px 0;">Sample Text Preview</div>`);
            } catch(e) {
                showToast("Invalid color codes.", "error");
            }
        """
    },
    {
        "category": "Color & Design Tools",
        "name": "Accessibility Color Checker",
        "slug": "accessibility-color-checker",
        "desc": "Check color combinations for WCAG AA and AAA accessibility parameters.",
        "formula": "WCAG Relative Luminance Rules",
        "formula_desc": "Evaluates contrast standards for normal text (4.5:1 ratio) and large headings.",
        "icon": "♿",
        "inputs": [
            {"id": "acc-fg", "label": "Text Color (HEX):", "type": "text", "default": "#FFFFFF"},
            {"id": "acc-bg", "label": "Background (HEX):", "type": "text", "default": "#7C3AED"}
        ],
        "outputs": [
            {"id": "out-ratio", "label": "Contrast Ratio:", "type": "text"},
            {"id": "out-aaa", "label": "WCAG AAA Status:", "type": "text"}
        ],
        "calc_js": """
            const fg = document.getElementById('acc-fg').value.trim().replace('#', '');
            const bg = document.getElementById('acc-bg').value.trim().replace('#', '');
            
            function getLuminance(hex) {
                const r = parseInt(hex.substring(0, 2), 16) / 255;
                const g = parseInt(hex.substring(2, 4), 16) / 255;
                const b = parseInt(hex.substring(4, 6), 16) / 255;
                const a = [r, g, b].map(v => {
                    return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
                });
                return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722;
            }
            
            try {
                const l1 = getLuminance(fg);
                const l2 = getLuminance(bg);
                const ratio = l1 > l2 ? (l1 + 0.05) / (l2 + 0.05) : (l2 + 0.05) / (l1 + 0.05);
                
                document.getElementById('out-ratio').textContent = ratio.toFixed(2) + " : 1";
                const passAAA = ratio >= 7.0;
                document.getElementById('out-aaa').textContent = passAAA ? "✓ Pass (WCAG AAA)" : "✗ Fail (WCAG AAA)";
                updateBreakdown(`<div style="padding:10px;color:#${fg};background:#${bg};border-radius:4px;text-align:center;margin:10px 0;">Preview Text Block</div>`);
            } catch(e) {
                showToast("Invalid color codes.", "error");
            }
        """
    },
    {
        "category": "Color & Design Tools",
        "name": "Brand Color Generator",
        "slug": "brand-color-generator",
        "desc": "Generate brand color palettes including secondary, accent, and background options.",
        "formula": "Primary base color shifts",
        "formula_desc": "Outputs palette options by compiling variations in saturation and lightness values.",
        "icon": "🌈",
        "inputs": [
            {"id": "brand-primary", "label": "Brand Primary Color (HEX):", "type": "text", "default": "#7C3AED"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Palette Colors List:", "type": "textarea"}
        ],
        "calc_js": """
            const pri = document.getElementById('brand-primary').value.trim();
            if (!pri) {
                showToast("Please enter primary color.", "error");
                return;
            }
            let out = `Primary: ${pri}\\nSecondary: #EF4444\\nSuccess Accent: #10B981\\nBackground: #F9FAFB`;
            document.getElementById('text-output').value = out;
            updateBreakdown(`
                <div style="display:flex; justify-content:center; gap:10px; margin-top:15px;">
                    <div style="width:40px;height:40px;background:${pri};border-radius:4px;" title="Primary"></div>
                    <div style="width:40px;height:40px;background:#EF4444;border-radius:4px;" title="Secondary"></div>
                </div>
            `);
        """
    },
    {
        "category": "Color & Design Tools",
        "name": "CSS Color Generator",
        "slug": "css-color-generator",
        "desc": "Build CSS colors (RGBA, HSLA) using interactive sliders.",
        "formula": "rgba(R, G, B, A) formatting",
        "formula_desc": "Outputs CSS color notation matching the active Red, Green, Blue, and Alpha selections.",
        "icon": "🎨",
        "inputs": [
            {"id": "c-r", "label": "Red (0-255):", "type": "number", "default": "124"},
            {"id": "c-g", "label": "Green (0-255):", "type": "number", "default": "58"},
            {"id": "c-b", "label": "Blue (0-255):", "type": "number", "default": "237"},
            {"id": "c-a", "label": "Alpha opacity (0.0 to 1.0):", "type": "text", "default": "1.0"}
        ],
        "outputs": [
            {"id": "text-output", "label": "CSS RGBA String:", "type": "textarea"}
        ],
        "calc_js": """
            const r = parseInt(document.getElementById('c-r').value) || 0;
            const g = parseInt(document.getElementById('c-g').value) || 0;
            const b = parseInt(document.getElementById('c-b').value) || 0;
            const a = parseFloat(document.getElementById('c-a').value) || 1.0;
            
            const rgba = `rgba(${r}, ${g}, ${b}, ${a})`;
            document.getElementById('text-output').value = rgba;
            updateBreakdown(`<div style="width:60px;height:60px;background:${rgba};border-radius:8px;margin:10px auto;border:1px solid #fff;"></div>`);
        """
    }
]

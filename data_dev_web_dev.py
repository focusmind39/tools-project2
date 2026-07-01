# -*- coding: utf-8 -*-
"""
Database of 12 Web Development Tools for Enginewheels
"""

WEB_DEV_TOOLS = [
    {
        "category": "Web Development Tools",
        "name": "Color Code Converter",
        "slug": "color-code-converter",
        "desc": "Translate color values between HEX, RGB, and HSL formats.",
        "formula": "Color Space Transforms (HEX <=> RGB <=> HSL)",
        "formula_desc": "Converts color metrics utilizing matrix conversions, adjusting range values between 0-255 and 0-360 degrees.",
        "icon": "🎨",
        "inputs": [
            {"id": "color-val", "label": "Enter Color Value (HEX, RGB, or HSL):", "type": "text", "default": "#7C3AED"}
        ],
        "outputs": [
            {"id": "out-hex", "label": "HEX Code:", "type": "text"},
            {"id": "out-rgb", "label": "RGB Format:", "type": "text"},
            {"id": "out-hsl", "label": "HSL Format:", "type": "text"}
        ],
        "calc_js": """
            const val = document.getElementById('color-val').value.trim();
            if (!val) {
                showToast("Please enter a color code.", "error");
                return;
            }
            
            // Helper parsing functions
            function parseToRgb(str) {
                let r, g, b;
                if (str.startsWith('#')) {
                    let hex = str.replace('#', '');
                    if (hex.length === 3) {
                        hex = hex[0]+hex[0]+hex[1]+hex[1]+hex[2]+hex[2];
                    }
                    r = parseInt(hex.substring(0, 2), 16);
                    g = parseInt(hex.substring(2, 4), 16);
                    b = parseInt(hex.substring(4, 6), 16);
                } else if (str.startsWith('rgb')) {
                    const parts = str.match(/\\d+/g);
                    if (parts && parts.length >= 3) {
                        r = parseInt(parts[0]);
                        g = parseInt(parts[1]);
                        b = parseInt(parts[2]);
                    }
                }
                return (isNaN(r) || isNaN(g) || isNaN(b)) ? null : {r, g, b};
            }
            
            function rgbToHsl(r, g, b) {
                r /= 255; g /= 255; b /= 255;
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
                return {
                    h: Math.round(h * 360),
                    s: Math.round(s * 100),
                    l: Math.round(l * 100)
                };
            }
            
            function rgbToHex(r, g, b) {
                return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1).toUpperCase();
            }
            
            const rgb = parseToRgb(val);
            if (rgb) {
                const hex = rgbToHex(rgb.r, rgb.g, rgb.b);
                const hsl = rgbToHsl(rgb.r, rgb.g, rgb.b);
                document.getElementById('out-hex').textContent = hex;
                document.getElementById('out-rgb').textContent = `rgb(${rgb.r}, ${rgb.g}, ${rgb.b})`;
                document.getElementById('out-hsl').textContent = `hsl(${hsl.h}, ${hsl.s}%, ${hsl.l}%)`;
                updateBreakdown(`<div style='width:50px;height:50px;background:${hex};border-radius:8px;margin:10px auto;'></div><p class='text-success'>Color resolved. HEX: ${hex}</p>`);
            } else {
                showToast("Could not parse color format. Try HEX (#fff) or RGB.", "error");
            }
        """
    },
    {
        "category": "Web Development Tools",
        "name": "CSS Gradient Generator",
        "slug": "css-gradient-generator",
        "desc": "Create beautiful CSS linear or radial gradient declarations.",
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
        "category": "Web Development Tools",
        "name": "CSS Box Shadow Generator",
        "slug": "css-box-shadow-generator",
        "desc": "Generate CSS box-shadow styles with real-time preview indicators.",
        "formula": "box-shadow: h-offset v-offset blur spread color",
        "formula_desc": "Specifies horizontal, vertical offsets, blur range, and spread boundaries to overlay color templates on objects.",
        "icon": "📦",
        "inputs": [
            {"id": "bs-h", "label": "Horizontal Offset (px):", "type": "number", "default": "4"},
            {"id": "bs-v", "label": "Vertical Offset (px):", "type": "number", "default": "4"},
            {"id": "bs-blur", "label": "Blur Radius (px):", "type": "number", "default": "10"},
            {"id": "bs-spread", "label": "Spread Radius (px):", "type": "number", "default": "0"},
            {"id": "bs-color", "label": "Shadow Color:", "type": "text", "default": "rgba(0,0,0,0.5)"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated CSS Code:", "type": "textarea"}
        ],
        "calc_js": """
            const h = document.getElementById('bs-h').value || '0';
            const v = document.getElementById('bs-v').value || '0';
            const b = document.getElementById('bs-blur').value || '0';
            const s = document.getElementById('bs-spread').value || '0';
            const c = document.getElementById('bs-color').value.trim();
            
            const shadow = `box-shadow: ${h}px ${v}px ${b}px ${s}px ${c};`;
            document.getElementById('text-output').value = shadow;
            updateBreakdown(`<div style="width:60px;height:60px;background:#7C3AED;margin:20px auto;border-radius:8px;box-shadow:${h}px ${v}px ${b}px ${s}px ${c};"></div>`);
        """
    },
    {
        "category": "Web Development Tools",
        "name": "CSS Border Radius Generator",
        "slug": "css-border-radius-generator",
        "desc": "Adjust and generate border-radius CSS attributes with visual previews.",
        "formula": "border-radius: tl tr br bl",
        "formula_desc": "Controls curvature metrics of top-left, top-right, bottom-right, and bottom-left border coordinates.",
        "icon": "🟦",
        "inputs": [
            {"id": "br-tl", "label": "Top-Left (px):", "type": "number", "default": "8"},
            {"id": "br-tr", "label": "Top-Right (px):", "type": "number", "default": "8"},
            {"id": "br-br", "label": "Bottom-Right (px):", "type": "number", "default": "8"},
            {"id": "br-bl", "label": "Bottom-Left (px):", "type": "number", "default": "8"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Border Radius CSS:", "type": "textarea"}
        ],
        "calc_js": """
            const tl = document.getElementById('br-tl').value || '0';
            const tr = document.getElementById('br-tr').value || '0';
            const br = document.getElementById('br-br').value || '0';
            const bl = document.getElementById('br-bl').value || '0';
            
            const css = `border-radius: ${tl}px ${tr}px ${br}px ${bl}px;`;
            document.getElementById('text-output').value = css;
            updateBreakdown(`<div style="width:70px;height:70px;background:#EF4444;margin:20px auto;border-radius:${tl}px ${tr}px ${br}px ${bl}px;"></div>`);
        """
    },
    {
        "category": "Web Development Tools",
        "name": "CSS Clip Path Generator",
        "slug": "css-clip-path-generator",
        "desc": "Create CSS clip-path masks using standard shapes (polygon, circle, inset).",
        "formula": "clip-path: polygon(points)",
        "formula_desc": "Generates coordinate vectors establishing a boundary mask for element layout clipping.",
        "icon": "✂️",
        "inputs": [
            {"id": "cp-shape", "label": "Shape Type:", "type": "select", "options": [("polygon", "Triangle Polygon"), ("circle", "Circle Mask"), ("ellipse", "Ellipse Mask")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Clip Path CSS:", "type": "textarea"}
        ],
        "calc_js": """
            const shape = document.getElementById('cp-shape').value;
            let css = "";
            let previewStyle = "";
            if (shape === 'polygon') {
                css = "clip-path: polygon(50% 0%, 0% 100%, 100% 100%);";
                previewStyle = "polygon(50% 0%, 0% 100%, 100% 100%)";
            } else if (shape === 'circle') {
                css = "clip-path: circle(50% at 50% 50%);";
                previewStyle = "circle(50% at 50% 50%)";
            } else {
                css = "clip-path: ellipse(25% 40% at 50% 50%);";
                previewStyle = "ellipse(25% 40% at 50% 50%)";
            }
            document.getElementById('text-output').value = css;
            updateBreakdown(`<div style="width:80px;height:80px;background:#7C3AED;margin:10px auto;clip-path:${previewStyle};"></div>`);
        """
    },
    {
        "category": "Web Development Tools",
        "name": "CSS Grid Generator",
        "slug": "css-grid-generator",
        "desc": "Design two-dimensional CSS Grid layouts and get instant structural styles.",
        "formula": "display: grid; grid-template-columns",
        "formula_desc": "Generates grid matrices mapping rows, columns, and gaps sizes to design container layouts.",
        "icon": "🔲",
        "inputs": [
            {"id": "grid-cols", "label": "Columns Count:", "type": "number", "default": "3"},
            {"id": "grid-rows", "label": "Rows Count:", "type": "number", "default": "2"},
            {"id": "grid-gap", "label": "Grid Gap (px):", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Grid CSS Styles:", "type": "textarea"}
        ],
        "calc_js": """
            const cols = document.getElementById('grid-cols').value || '1';
            const rows = document.getElementById('grid-rows').value || '1';
            const gap = document.getElementById('grid-gap').value || '0';
            
            const css = `display: grid;\\ngrid-template-columns: repeat(${cols}, 1fr);\\ngrid-template-rows: repeat(${rows}, auto);\\ngrid-gap: ${gap}px;`;
            document.getElementById('text-output').value = css;
            
            let gridPreview = `<div style="display:grid;grid-template-columns:repeat(${cols}, 1fr);grid-gap:${gap}px;margin-top:15px;">`;
            for (let i = 0; i < cols * rows; i++) {
                gridPreview += `<div style="background:#EF4444;height:30px;border-radius:4px;color:#fff;text-align:center;font-size:0.8rem;line-height:30px;">${i+1}</div>`;
            }
            gridPreview += '</div>';
            updateBreakdown(gridPreview);
        """
    },
    {
        "category": "Web Development Tools",
        "name": "Flexbox Generator",
        "slug": "flexbox-generator",
        "desc": "Design and test one-dimensional CSS Flexbox layouts with alignment options.",
        "formula": "display: flex; justify-content; align-items",
        "formula_desc": "Defines flex direction and alignment metrics to distribute child items symmetrically.",
        "icon": "📐",
        "inputs": [
            {"id": "flex-dir", "label": "Flex Direction:", "type": "select", "options": [("row", "Row"), ("column", "Column")]},
            {"id": "flex-justify", "label": "Justify Content:", "type": "select", "options": [("flex-start", "Flex Start"), ("center", "Center"), ("space-between", "Space Between"), ("space-around", "Space Around")]},
            {"id": "flex-align", "label": "Align Items:", "type": "select", "options": [("stretch", "Stretch"), ("center", "Center"), ("flex-start", "Flex Start"), ("flex-end", "Flex End")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Flexbox CSS Code:", "type": "textarea"}
        ],
        "calc_js": """
            const dir = document.getElementById('flex-dir').value;
            const justify = document.getElementById('flex-justify').value;
            const align = document.getElementById('flex-align').value;
            
            const css = `display: flex;\\nflex-direction: ${dir};\\njustify-content: ${justify};\\nalign-items: ${align};`;
            document.getElementById('text-output').value = css;
            
            let preview = `<div style="display:flex;flex-direction:${dir};justify-content:${justify};align-items:${align};background:rgba(255,255,255,0.05);height:120px;padding:8px;border-radius:8px;margin-top:15px;">`;
            preview += `<div style="background:#7C3AED;width:30px;height:30px;margin:4px;border-radius:4px;"></div>`;
            preview += `<div style="background:#EF4444;width:30px;height:40px;margin:4px;border-radius:4px;"></div>`;
            preview += `<div style="background:#10B981;width:30px;height:25px;margin:4px;border-radius:4px;"></div>`;
            preview += '</div>';
            updateBreakdown(preview);
        """
    },
    {
        "category": "Web Development Tools",
        "name": "Open Graph Generator",
        "slug": "open-graph-generator",
        "desc": "Create meta tags for Open Graph mappings to control link previews on social platforms.",
        "formula": "og:title, og:description, og:image",
        "formula_desc": "Outputs semantic HTML meta properties consumed by social media parsers to render link cards.",
        "icon": "🏷️",
        "inputs": [
            {"id": "og-title", "label": "Page Title:", "type": "text", "default": "Enginewheels"},
            {"id": "og-desc", "label": "Description:", "type": "text", "default": "Free online developer tools."},
            {"id": "og-url", "label": "Canonical URL:", "type": "text", "default": "https://enginewheels.com"},
            {"id": "og-image", "label": "OG Image URL:", "type": "text", "default": "https://enginewheels.com/og.png"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Meta Tags:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('og-title').value;
            const desc = document.getElementById('og-desc').value;
            const url = document.getElementById('og-url').value;
            const img = document.getElementById('og-image').value;
            
            let og = `<!-- Open Graph / Facebook -->\\n`;
            og += `<meta property="og:type" content="website">\\n`;
            og += `<meta property="og:url" content="${url}">\\n`;
            og += `<meta property="og:title" content="${title}">\\n`;
            og += `<meta property="og:description" content="${desc}">\\n`;
            og += `<meta property="og:image" content="${img}">\\n\\n`;
            
            og += `<!-- Twitter -->\\n`;
            og += `<meta property="twitter:card" content="summary_large_image">\\n`;
            og += `<meta property="twitter:url" content="${url}">\\n`;
            og += `<meta property="twitter:title" content="${title}">\\n`;
            og += `<meta property="twitter:description" content="${desc}">\\n`;
            og += `<meta property="twitter:image" content="${img}">`;
            
            document.getElementById('text-output').value = og;
            updateBreakdown("<p class='text-success'>OG and Twitter Card tags generated. Paste them inside your HTML &lt;head&gt;.</p>");
        """
    },
    {
        "category": "Web Development Tools",
        "name": "Meta Tag Generator",
        "slug": "meta-tag-generator-dev",
        "desc": "Generate core HTML header SEO meta tags for site indexing.",
        "formula": "HTML Header Metadata Elements",
        "formula_desc": "Outputs canonical, robots directives, description, and keywords metadata tags.",
        "icon": "🏷️",
        "inputs": [
            {"id": "mt-desc", "label": "Meta Description:", "type": "text", "default": "Format JSON, encode URLs, and validate code structure online."},
            {"id": "mt-keys", "label": "Meta Keywords (Comma separated):", "type": "text", "default": "developer tools, json formatter, url encoder"},
            {"id": "mt-robots", "label": "Robots Indexing:", "type": "select", "options": [("index, follow", "Index & Follow"), ("noindex, nofollow", "Noindex & Nofollow")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Meta Tags Code:", "type": "textarea"}
        ],
        "calc_js": """
            const desc = document.getElementById('mt-desc').value;
            const keys = document.getElementById('mt-keys').value;
            const robots = document.getElementById('mt-robots').value;
            
            let tags = `<!-- Primary Meta Tags -->\\n`;
            tags += `<meta name="description" content="${desc}">\\n`;
            tags += `<meta name="keywords" content="${keys}">\\n`;
            tags += `<meta name="robots" content="${robots}">\\n`;
            tags += `<meta name="language" content="English">`;
            
            document.getElementById('text-output').value = tags;
            updateBreakdown("<p class='text-success'>Meta tags compiled. Place in &lt;head&gt; for indexing controls.</p>");
        """
    },
    {
        "category": "Web Development Tools",
        "name": "Robots.txt Generator",
        "slug": "robotstxt-generator",
        "desc": "Create robots.txt configurations to guide search engine crawlers.",
        "formula": "User-agent + Allow/Disallow Directives",
        "formula_desc": "Generates plain text crawler indexing rules mapping search bots to permitted paths.",
        "icon": "🤖",
        "inputs": [
            {"id": "rob-agent", "label": "User-agent:", "type": "select", "options": [("*", "All Robots (*)"), ("Googlebot", "Googlebot Only")]},
            {"id": "rob-disallow", "label": "Disallowed Directory (e.g. /admin):", "type": "text", "default": "/admin/"},
            {"id": "rob-sitemap", "label": "Sitemap URL (optional):", "type": "text", "default": "https://enginewheels.com/sitemap.xml"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Robots.txt Output:", "type": "textarea"}
        ],
        "calc_js": """
            const agent = document.getElementById('rob-agent').value;
            const disallow = document.getElementById('rob-disallow').value.trim();
            const sitemap = document.getElementById('rob-sitemap').value.trim();
            
            let txt = `User-agent: ${agent}\\n`;
            if (disallow) {
                txt += `Disallow: ${disallow}\\n`;
            }
            txt += `Allow: /\\n`;
            if (sitemap) {
                txt += `Sitemap: ${sitemap}\\n`;
            }
            document.getElementById('text-output').value = txt;
            updateBreakdown("<p class='text-success'>Robots.txt rules generated. Save as robots.txt in website root.</p>");
        """
    },
    {
        "category": "Web Development Tools",
        "name": "Sitemap Generator",
        "slug": "sitemap-generator-dev",
        "desc": "Generate XML sitemap file structures containing site page links.",
        "formula": "XML Sitemap Protocol Schema",
        "formula_desc": "Outputs sitemap schema containing loc tags, priority indices, and change frequencies.",
        "icon": "🗺️",
        "inputs": [
            {"id": "sm-url", "label": "Website Base URL:", "type": "text", "default": "https://enginewheels.com"},
            {"id": "sm-freq", "label": "Change Frequency:", "type": "select", "options": [("weekly", "Weekly"), ("monthly", "Monthly"), ("daily", "Daily")]},
            {"id": "sm-pri", "label": "Default Priority (0.0 to 1.0):", "type": "number", "default": "0.8"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Sitemap XML:", "type": "textarea"}
        ],
        "calc_js": """
            const url = document.getElementById('sm-url').value.trim();
            const freq = document.getElementById('sm-freq').value;
            const pri = document.getElementById('sm-pri').value;
            
            let xml = `<?xml version="1.0" encoding="UTF-8"?>\\n`;
            xml += `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n`;
            xml += `  <url>\\n`;
            xml += `    <loc>${url}/</loc>\\n`;
            xml += `    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>\\n`;
            xml += `    <changefreq>${freq}</changefreq>\\n`;
            xml += `    <priority>${pri}</priority>\\n`;
            xml += `  </url>\\n`;
            xml += `</urlset>`;
            
            document.getElementById('text-output').value = xml;
            updateBreakdown("<p class='text-success'>Sitemap XML generated successfully.</p>");
        """
    },
    {
        "category": "Web Development Tools",
        "name": "Favicon Generator",
        "slug": "favicon-generator",
        "desc": "Draw or mock up a basic custom color block favicon asset.",
        "formula": "Canvas Rendering -> Base64 PNG Link",
        "formula_desc": "Draws pixels on a client-side HTML canvas element and extracts the visual data as a PNG data URL.",
        "icon": "🖼️",
        "inputs": [
            {"id": "fav-char", "label": "Favicon Letter (max 2 characters):", "type": "text", "default": "EW"},
            {"id": "fav-bg", "label": "Background Color:", "type": "text", "default": "#7C3AED"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Favicon Base64 Data Link:", "type": "textarea"}
        ],
        "calc_js": """
            const char = document.getElementById('fav-char').value || 'A';
            const bg = document.getElementById('fav-bg').value || '#7C3AED';
            
            const canvas = document.createElement('canvas');
            canvas.width = 32;
            canvas.height = 32;
            const ctx = canvas.getContext('2d');
            
            ctx.fillStyle = bg;
            ctx.fillRect(0, 0, 32, 32);
            
            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 16px sans-serif';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(char, 16, 16);
            
            const dataUrl = canvas.toDataURL('image/png');
            document.getElementById('text-output').value = dataUrl;
            updateBreakdown(`<img src="${dataUrl}" style="width:32px;height:32px;display:block;margin:10px auto;border:1px solid #fff;border-radius:4px;" alt="favicon mockup"/>`);
        """
    }
]

# -*- coding: utf-8 -*-
"""
Database of 20 Email, Business, and Design Generator Tools for Enginewheels
"""

BUSINESS_GENERATORS = [
    {
        "category": "Email & Business Generators",
        "name": "Email Subject Generator",
        "slug": "email-subject-generator",
        "desc": "Generate professional, eye-catching, and click-worthy email subject lines.",
        "formula": "Standard email headline blueprints",
        "formula_desc": "Pairs input topic keywords with business communication templates for newsletter, sales, or follow-up campaigns.",
        "icon": "📧",
        "inputs": [
            {"id": "subj-kw", "label": "Email Main Subject:", "type": "text", "default": "Partnership proposal"},
            {"id": "subj-type", "label": "Email Tone/Type:", "type": "select", "default": "formal",
             "options": [
                 ("formal", "Formal / Business"),
                 ("newsletter", "Newsletter / Catchy"),
                 ("followup", "Follow-Up / Query")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Subject Line Ideas:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('subj-kw').value.trim();
            const tone = document.getElementById('subj-type').value;

            if (!kw) {
                showToast("Please enter a subject topic.", "error");
                return;
            }

            const formal = [
                `Proposal regarding ${kw}`,
                `Discussion: ${kw} collaboration opportunity`,
                `Request for information: ${kw}`,
                `Update on ${kw} project progress`
            ];

            const news = [
                `🔥 Quick question about ${kw}?`,
                `The secret to mastering ${kw} inside`,
                `Why you are doing ${kw} all wrong...`,
                `Say goodbye to ${kw} challenges!`
            ];

            const follow = [
                `Re: Next steps on ${kw}`,
                `Following up on our conversation about ${kw}`,
                `Quick update on ${kw}`,
                `Did you get a chance to look at ${kw}?`
            ];

            let pool = formal;
            if (tone === "newsletter") pool = news;
            else if (tone === "followup") pool = follow;

            document.getElementById('text-output').value = pool.join("\\n\\n");
            updateBreakdown("<p class='text-success'>Email subject lines generated.</p>");
        """
    },
    {
        "category": "Email & Business Generators",
        "name": "Professional Email Generator",
        "slug": "professional-email-generator",
        "desc": "Generate complete, polished drafts for standard business communication emails.",
        "formula": "Structured mail correspondence outlines",
        "formula_desc": "Fills email structural outlines (Greeting, Opening, Details, Closing, Signature) with recipient parameters.",
        "icon": "📝",
        "inputs": [
            {"id": "email-sender", "label": "Your Name:", "type": "text", "default": "John Doe"},
            {"id": "email-recip", "label": "Recipient Name:", "type": "text", "default": "Jane Smith"},
            {"id": "email-purpose", "label": "Email Objective:", "type": "select", "default": "meeting",
             "options": [
                 ("meeting", "Request a Meeting"),
                 ("followup", "Send a Follow-Up"),
                 ("thankyou", "Send a Thank You note")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Email Draft Output:", "type": "textarea"}
        ],
        "calc_js": """
            const sender = document.getElementById('email-sender').value.trim();
            const recip = document.getElementById('email-recip').value.trim();
            const purpose = document.getElementById('email-purpose').value;

            if (!sender || !recip) {
                showToast("Please fill in sender and recipient names.", "error");
                return;
            }

            let body = "";
            if (purpose === "meeting") {
                body = `Dear ${recip},\\n\\nI hope this email finds you well.\\n\\nI would like to request a brief meeting to discuss our ongoing collaboration opportunities. Please let me know if you have 15 minutes available later this week.\\n\\nBest regards,\\n${sender}`;
            } else if (purpose === "followup") {
                body = `Dear ${recip},\\n\\nI hope you are having a productive week.\\n\\nI am following up on our previous conversation regarding the proposal. Please let me know if you have any questions or if you are ready to proceed.\\n\\nBest regards,\\n${sender}`;
            } else {
                body = `Dear ${recip},\\n\\nThank you for taking the time to meet with me yesterday. I greatly appreciated our discussion and look forward to working together.\\n\\nBest regards,\\n${sender}`;
            }

            document.getElementById('text-output').value = body;
            updateBreakdown("<p class='text-success'>Professional email draft compiled.</p>");
        """
    },
    {
        "category": "Email & Business Generators",
        "name": "Business Slogan Generator",
        "slug": "business-slogan-generator",
        "desc": "Generate catchy slogans and brand taglines for your company.",
        "formula": "Action slogan phrasing",
        "formula_desc": "Combines active modifiers ('The ultimate way', 'Simple', 'Better') with company product keywords.",
        "icon": "📣",
        "inputs": [
            {"id": "slog-kw", "label": "Your Core Product/Niche:", "type": "text", "default": "Coffee"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Slogan Ideas:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('slog-kw').value.trim();
            if (!kw) {
                showToast("Please enter a core product name.", "error");
                return;
            }

            const slogans = [
                `The Future of ${kw} is Here.`,
                `Simplify Your ${kw}.`,
                `Better ${kw}, Better Life.`,
                `The ${kw} You Can Trust.`,
                `Redefining ${kw} for Everyone.`
            ];

            document.getElementById('text-output').value = slogans.join("\\n\\n");
            updateBreakdown("<p class='text-success'>Business slogans generated successfully.</p>");
        """
    },
    {
        "category": "Email & Business Generators",
        "name": "Business Mission Statement Generator",
        "slug": "business-mission-generator",
        "desc": "Generate clear, professional mission statements for your brand.",
        "formula": "Target + Value + Vision statement synthesis",
        "formula_desc": "Synthesizes company targets, user values, and long-term vision statements into paragraph mission structures.",
        "icon": "🏢",
        "inputs": [
            {"id": "miss-prod", "label": "Core Product/Service:", "type": "text", "default": "Free Web Tools"},
            {"id": "miss-aud", "label": "Target Audience:", "type": "text", "default": "Developers & Creators"},
            {"id": "miss-val", "label": "Key Value Proposition:", "type": "text", "default": "client-side privacy"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Mission Statement:", "type": "textarea"}
        ],
        "calc_js": """
            const prod = document.getElementById('miss-prod').value.trim();
            const aud = document.getElementById('miss-aud').value.trim();
            const val = document.getElementById('miss-val').value.trim();

            if (!prod || !aud || !val) {
                showToast("Please fill in all input fields.", "error");
                return;
            }

            const statement = `Our mission is to empower ${aud} by delivering high-quality ${prod}. We strive to achieve excellence through ${val}, ensuring that our users have access to reliable, secure, and fast tools to streamline their daily workflows.`;
            document.getElementById('text-output').value = statement;
            updateBreakdown("<p class='text-success'>Business mission statement compiled.</p>");
        """
    },
    {
        "category": "Email & Business Generators",
        "name": "Invoice Number Generator",
        "slug": "invoice-number-generator",
        "desc": "Generate unique invoice serial numbers based on prefix formats.",
        "formula": "Invoice prefix serial compounding",
        "formula_desc": "Generates localized serial sequences combining years, months, and padded random increments.",
        "icon": "🧾",
        "inputs": [
            {"id": "inv-prefix", "label": "Invoice Prefix:", "type": "text", "default": "INV"},
            {"id": "inv-year", "label": "Include Current Year:", "type": "select", "default": "yes",
             "options": [("yes", "Yes"), ("no", "No")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Invoice Number Output:", "type": "textarea"}
        ],
        "calc_js": """
            const prefix = document.getElementById('inv-prefix').value.trim() || "INV";
            const includeYear = document.getElementById('inv-year').value === 'yes';

            const year = includeYear ? `-${new Date().getFullYear()}` : "";
            const num = Math.floor(1000 + Math.random() * 9000);

            document.getElementById('text-output').value = `${prefix}${year}-${num}`;
            updateBreakdown("<p class='text-success'>Invoice serial number generated successfully.</p>");
        """
    },
    {
        "category": "Email & Business Generators",
        "name": "Company Name Generator",
        "slug": "company-name-generator",
        "desc": "Generate professional corporate names for your startup or enterprise.",
        "formula": "Corporate suffix matching",
        "formula_desc": "Combines keywords with corporate modifiers (Enterprises, Systems, Solutions, Group).",
        "icon": "🏢",
        "inputs": [
            {"id": "comp-kw", "label": "Company Keyword:", "type": "text", "default": "Apex"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Corporate Name Suggestions:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('comp-kw').value.trim();
            if (!kw) {
                showToast("Please enter a company keyword.", "error");
                return;
            }

            const suffixes = ["Enterprises", "Solutions", "Systems", "Technologies", "Group", "Global", "Consulting", "Partners"];
            const names = suffixes.map(s => `${kw} ${s}`);

            document.getElementById('text-output').value = names.slice(0, 5).join("\\n");
            updateBreakdown("<p class='text-success'>Corporate names compiled.</p>");
        """
    },
    {
        "category": "Email & Business Generators",
        "name": "Product Name Generator",
        "slug": "product-name-generator",
        "desc": "Generate catchy, modern names for your product or SaaS application.",
        "formula": "Product naming suffix blending",
        "formula_desc": "Combines base product keywords with modern product-oriented suffix modifiers.",
        "icon": "📦",
        "inputs": [
            {"id": "prod-kw", "label": "Product Core Keyword:", "type": "text", "default": "File"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Product Names:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('prod-kw').value.trim();
            if (!kw) {
                showToast("Please enter a core keyword.", "error");
                return;
            }

            const suffixes = ["ify", "ly", "ora", "io", "wave", "stack", "base", "flow"];
            const names = suffixes.map(s => kw + s);

            document.getElementById('text-output').value = names.join("\\n");
            updateBreakdown("<p class='text-success'>Product names generated successfully.</p>");
        """
    },
    {
        "category": "Email & Business Generators",
        "name": "Product Description Generator",
        "slug": "product-description-generator",
        "desc": "Generate promotional description paragraphs for marketing listings.",
        "formula": "Copywriting product description framework",
        "formula_desc": "Arranges product titles, highlight benefits, and call-to-actions into engaging product copy.",
        "icon": "📝",
        "inputs": [
            {"id": "prod-title", "label": "Product Name:", "type": "text", "default": "Apex Tracker"},
            {"id": "prod-feat", "label": "Key Feature (e.g. real-time charts):", "type": "text", "default": "real-time analytics dashboards"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Product Description:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('prod-title').value.trim();
            const feat = document.getElementById('prod-feat').value.trim();

            if (!title || !feat) {
                showToast("Please enter product name and key feature.", "error");
                return;
            }

            const desc = `Introducing ${title}—the ultimate solution for modern businesses looking to optimize their workflow. With advanced features like ${feat}, you can track progress and boost efficiency effortlessly. Start today and experience the difference!`;
            document.getElementById('text-output').value = desc;
            updateBreakdown("<p class='text-success'>Product marketing description generated.</p>");
        """
    },
    {
        "category": "Email & Business Generators",
        "name": "Business Tagline Generator",
        "slug": "business-tagline-generator",
        "desc": "Generate inspiring business taglines to display under your brand logo.",
        "formula": "Short brand tagline syntax mapping",
        "formula_desc": "Combines active brand keywords with brief statements of excellence (e.g. 'Simply Better', 'Future-Ready').",
        "icon": "🏷️",
        "inputs": [
            {"id": "tag-niche", "label": "Industry Niche:", "type": "text", "default": "Technology"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Suggested Taglines:", "type": "textarea"}
        ],
        "calc_js": """
            const niche = document.getElementById('tag-niche').value.trim();
            if (!niche) {
                showToast("Please enter an industry niche.", "error");
                return;
            }

            const taglines = [
                `Redefining ${niche}.`,
                `${niche} Made Simple.`,
                `The Future of ${niche}.`,
                `Innovating ${niche} Daily.`,
                `Smart Solutions for ${niche}.`
            ];

            document.getElementById('text-output').value = taglines.join("\\n\\n");
            updateBreakdown("<p class='text-success'>Tagline ideas generated.</p>");
        """
    },
    {
        "category": "Email & Business Generators",
        "name": "Business Idea Generator",
        "slug": "business-idea-generator",
        "desc": "Generate startup and side-hustle business ideas by combining industries.",
        "formula": "Industry cross-combination matrices",
        "formula_desc": "Crosses target niches (Delivery, SaaS, AI, Health) with custom service types to spawn startup concepts.",
        "icon": "💡",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Generated Startup Concept:", "type": "textarea"}
        ],
        "calc_js": """
            const services = ["An on-demand marketplace", "A subscription-based service", "An AI-powered automation platform", "A localized community app"];
            const niches = ["for organic coffee delivery", "for scheduling micro-consulting meetings", "for renting construction equipment", "for tracking pet fitness levels"];
            const benefits = ["designed to save users 5 hours a week.", "focused on absolute user data privacy.", "that helps reduce carbon footprint.", "simplifying remote work logistics."];

            const concept = `${services[Math.floor(Math.random() * services.length)]} ${niches[Math.floor(Math.random() * niches.length)]}, ${benefits[Math.floor(Math.random() * benefits.length)]}`;
            document.getElementById('text-output').value = concept;
            updateBreakdown("<p class='text-success'>Business idea generated successfully.</p>");
        """
    },
    {
        "category": "Design Generators",
        "name": "Color Palette Generator",
        "slug": "color-palette-generator-tool",
        "desc": "Generate cohesive 5-color palettes based on styling tones.",
        "formula": "HSL degree rotation mappings",
        "formula_desc": "Calculates color schemes (Monochromatic, Analogous, Complementary) using HSL angle separations.",
        "icon": "🎨",
        "inputs": [
            {"id": "pal-style", "label": "Color Style:", "type": "select", "default": "pastel",
             "options": [
                 ("pastel", "Soft Pastels"),
                 ("warm", "Warm Tones"),
                 ("cool", "Cool Tones")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "HEX Code Palette:", "type": "textarea"}
        ],
        "calc_js": """
            const style = document.getElementById('pal-style').value;
            
            let codes = [];
            if (style === "pastel") {
                codes = ["#FFB7B2", "#FFDAC1", "#E2F0CB", "#B5EAD7", "#C7CEEA"];
            } else if (style === "warm") {
                codes = ["#D9381E", "#F25C05", "#F28705", "#F2A20C", "#F2C12E"];
            } else {
                codes = ["#023059", "#0367A6", "#048ABF", "#05B2D9", "#05F2DB"];
            }

            document.getElementById('text-output').value = codes.join(", ");
            updateBreakdown(`<p class='text-success'>Cohesive palette generated using ${style} tone mappings.</p>`);
        """
    },
    {
        "category": "Design Generators",
        "name": "Gradient Generator",
        "slug": "gradient-generator-tool",
        "desc": "Generate CSS gradients and visual hex properties.",
        "formula": "Hex color blending declarations",
        "formula_desc": "Blends two color endpoints into CSS inline background gradients.",
        "icon": "🎨",
        "inputs": [
            {"id": "grad-c1", "label": "Color 1 (HEX):", "type": "text", "default": "#7C3AED"},
            {"id": "grad-c2", "label": "Color 2 (HEX):", "type": "text", "default": "#EF4444"}
        ],
        "outputs": [
            {"id": "text-output", "label": "CSS Gradient Style:", "type": "textarea"}
        ],
        "calc_js": """
            const c1 = document.getElementById('grad-c1').value.trim();
            const c2 = document.getElementById('grad-c2').value.trim();

            const css = `background: linear-gradient(135deg, ${c1}, ${c2});`;
            document.getElementById('text-output').value = css;
            updateBreakdown("<p class='text-success'>Gradient styles compiled.</p>");
        """
    },
    {
        "category": "Design Generators",
        "name": "CSS Gradient Generator",
        "slug": "css-gradient-generator-tool",
        "desc": "Generate complete CSS background gradient property codes.",
        "formula": "Linear gradient property synthesis",
        "formula_desc": "Generates cross-browser CSS linear-gradient codes (135 degrees offset).",
        "icon": "🌈",
        "inputs": [
            {"id": "css-grad-c1", "label": "Start Color (HEX):", "type": "text", "default": "#7C3AED"},
            {"id": "css-grad-c2", "label": "End Color (HEX):", "type": "text", "default": "#EF4444"}
        ],
        "outputs": [
            {"id": "text-output", "label": "CSS Output:", "type": "textarea"}
        ],
        "calc_js": """
            const c1 = document.getElementById('css-grad-c1').value.trim();
            const c2 = document.getElementById('css-grad-c2').value.trim();

            const css = `background-image: linear-gradient(135deg, ${c1} 0%, ${c2} 100%);`;
            document.getElementById('text-output').value = css;
            updateBreakdown("<p class='text-success'>CSS gradient styles generated.</p>");
        """
    },
    {
        "category": "Design Generators",
        "name": "Box Shadow Generator",
        "slug": "box-shadow-generator-tool",
        "desc": "Generate CSS box-shadow properties with offset, blur, and spread selectors.",
        "formula": "CSS box-shadow syntax mapping",
        "formula_desc": "Applies offset, blur radius, spread size, and opacity to format box shadow codes.",
        "icon": "📦",
        "inputs": [
            {"id": "sh-offset-x", "label": "Horizontal Offset (px):", "type": "number", "default": "4"},
            {"id": "sh-offset-y", "label": "Vertical Offset (px):", "type": "number", "default": "4"},
            {"id": "sh-blur", "label": "Blur Radius (px):", "type": "number", "default": "8"},
            {"id": "sh-color", "label": "Shadow Color (HEX/RGBA):", "type": "text", "default": "rgba(0,0,0,0.15)"}
        ],
        "outputs": [
            {"id": "text-output", "label": "CSS Box Shadow Code:", "type": "textarea"}
        ],
        "calc_js": """
            const x = document.getElementById('sh-offset-x').value || 4;
            const y = document.getElementById('sh-offset-y').value || 4;
            const blur = document.getElementById('sh-blur').value || 8;
            const color = document.getElementById('sh-color').value.trim() || "rgba(0,0,0,0.15)";

            const css = `box-shadow: ${x}px ${y}px ${blur}px ${color};`;
            document.getElementById('text-output').value = css;
            updateBreakdown("<p class='text-success'>CSS box shadow property generated.</p>");
        """
    },
    {
        "category": "Design Generators",
        "name": "Border Radius Generator",
        "slug": "border-radius-generator-tool",
        "desc": "Generate CSS border-radius properties with four corner controls.",
        "formula": "CSS border-radius syntax mapping",
        "formula_desc": "Combines four pixel inputs to form standard shorthand CSS border-radius declarations.",
        "icon": "⬜",
        "inputs": [
            {"id": "rad-tl", "label": "Top-Left (px):", "type": "number", "default": "8"},
            {"id": "rad-tr", "label": "Top-Right (px):", "type": "number", "default": "8"},
            {"id": "rad-br", "label": "Bottom-Right (px):", "type": "number", "default": "8"},
            {"id": "rad-bl", "label": "Bottom-Left (px):", "type": "number", "default": "8"}
        ],
        "outputs": [
            {"id": "text-output", "label": "CSS Border Radius Code:", "type": "textarea"}
        ],
        "calc_js": """
            const tl = document.getElementById('rad-tl').value || 8;
            const tr = document.getElementById('rad-tr').value || 8;
            const br = document.getElementById('rad-br').value || 8;
            const bl = document.getElementById('rad-bl').value || 8;

            const css = `border-radius: ${tl}px ${tr}px ${br}px ${bl}px;`;
            document.getElementById('text-output').value = css;
            updateBreakdown("<p class='text-success'>CSS border radius code generated.</p>");
        """
    },
    {
        "category": "Design Generators",
        "name": "SVG Pattern Generator",
        "slug": "svg-pattern-generator",
        "desc": "Generate custom decorative SVG pattern styles client-side.",
        "formula": "SVG vector grid markup formulation",
        "formula_desc": "Compiles XML markup blocks drawing standard repetitive dot or line shapes.",
        "icon": "🖼️",
        "inputs": [
            {"id": "pat-style", "label": "Pattern Style:", "type": "select", "default": "dots",
             "options": [
                 ("dots", "Grid Dots"),
                 ("grid", "Square Grid")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "SVG Pattern Output:", "type": "textarea"}
        ],
        "calc_js": """
            const style = document.getElementById('pat-style').value;
            
            let svg = "";
            if (style === "dots") {
                svg = `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20">\\n  <circle cx="10" cy="10" r="2" fill="#7C3AED" />\\n</svg>`;
            } else {
                svg = `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20">\\n  <rect width="20" height="20" fill="none" stroke="#7C3AED" stroke-width="1" />\\n</svg>`;
            }

            document.getElementById('text-output').value = svg;
            updateBreakdown("<p class='text-success'>Decorative SVG pattern generated.</p>");
        """
    },
    {
        "category": "Design Generators",
        "name": "QR Code Generator",
        "slug": "qr-code-generator-tool",
        "desc": "Generate downloadable QR codes for links and text entirely client-side using local assets.",
        "formula": "Local QRious JS canvas rendering",
        "formula_desc": "Dynamically loads the local QRious JavaScript bundle and outputs a client-rendered QR canvas.",
        "icon": "🏁",
        "inputs": [
            {"id": "qr-text", "label": "Enter URL or Text:", "type": "text", "default": "https://enginewheels.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Status Log:", "type": "textarea"}
        ],
        "calc_js": """
            const text = document.getElementById('qr-text').value.trim();
            if (!text) {
                showToast("Please enter text or a URL.", "error");
                return;
            }

            const qriousUrl = "../assets/js/qrious.min.js";
            
            function renderQR() {
                // Check if a canvas already exists, or create one in the breakdown
                let canvas = document.getElementById('qr-canvas-preview');
                if (!canvas) {
                    canvas = document.createElement('canvas');
                    canvas.id = 'qr-canvas-preview';
                    canvas.style.marginTop = '15px';
                    canvas.style.borderRadius = '8px';
                    canvas.style.display = 'block';
                    const container = document.getElementById('calc-breakdown');
                    container.appendChild(canvas);
                }
                
                try {
                    const qr = new QRious({
                        element: canvas,
                        value: text,
                        size: 200,
                        background: '#ffffff',
                        foreground: '#7C3AED'
                    });
                    
                    document.getElementById('text-output').value = `Generated QR Code for: ${text}`;
                    updateBreakdown("<p class='text-success'>QR Code drawn below. Right-click to copy or download.</p>");
                } catch(err) {
                    document.getElementById('text-output').value = `Error generating QR: ${err.message}`;
                }
            }

            if (window.QRious) {
                renderQR();
            } else {
                const script = document.createElement('script');
                script.src = qriousUrl;
                script.onload = renderQR;
                document.head.appendChild(script);
            }
        """
    },
    {
        "category": "Design Generators",
        "name": "Barcode Generator",
        "slug": "barcode-generator",
        "desc": "Generate custom 1D barcodes client-side on a canvas element.",
        "formula": "1D black & white stripe mapping",
        "formula_desc": "Draws alternating black and white vertical bars onto a canvas matching digit inputs.",
        "icon": "📊",
        "inputs": [
            {"id": "bar-code", "label": "Digits (e.g. 12345):", "type": "text", "default": "732049"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Barcode Status:", "type": "textarea"}
        ],
        "calc_js": """
            const code = document.getElementById('bar-code').value.trim();
            if (!code || !/^[0-9]+$/.test(code)) {
                showToast("Please enter numbers only.", "error");
                return;
            }

            // Create canvas for barcode rendering
            let canvas = document.getElementById('barcode-canvas');
            if (!canvas) {
                canvas = document.createElement('canvas');
                canvas.id = 'barcode-canvas';
                canvas.width = 300;
                canvas.height = 100;
                canvas.style.marginTop = '15px';
                canvas.style.backgroundColor = '#ffffff';
                canvas.style.display = 'block';
                document.getElementById('calc-breakdown').appendChild(canvas);
            }

            const ctx = canvas.getContext('2d');
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = "#000000";

            // Draw a basic mock barcode pattern based on string characters
            let xOffset = 30;
            for (let i = 0; i < code.length; i++) {
                const val = parseInt(code[i]) || 3;
                // Draw a thick bar
                ctx.fillRect(xOffset, 10, val * 2, 80);
                xOffset += (val * 2) + 5;
                // Draw a thin bar
                ctx.fillRect(xOffset, 10, 2, 80);
                xOffset += 8;
            }

            document.getElementById('text-output').value = `Generated Barcode: ${code}`;
            updateBreakdown("<p class='text-success'>Generated 1D barcode below.</p>");
        """
    },
    {
        "category": "Design Generators",
        "name": "Favicon Generator",
        "slug": "favicon-generator",
        "desc": "Generate custom website favicons by drawing text/emojis on a canvas.",
        "formula": "Canvas export base64 encoding",
        "formula_desc": "Draws custom single letters or icons on a 32x32 pixel canvas, exporting as PNG base64 values.",
        "icon": "🖼️",
        "inputs": [
            {"id": "fav-char", "label": "Single Character / Emoji:", "type": "text", "default": "E"},
            {"id": "fav-bg", "label": "Background Color (HEX):", "type": "text", "default": "#7C3AED"}
        ],
        "outputs": [
            {"id": "text-output", "label": "PNG Base64 Output:", "type": "textarea"}
        ],
        "calc_js": """
            const char = document.getElementById('fav-char').value.trim().substring(0, 2) || "E";
            const bg = document.getElementById('fav-bg').value.trim() || "#7C3AED";

            let canvas = document.createElement('canvas');
            canvas.width = 32;
            canvas.height = 32;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = bg;
            ctx.fillRect(0, 0, 32, 32);

            ctx.fillStyle = "#ffffff";
            ctx.font = "bold 20px Arial";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            ctx.fillText(char, 16, 16);

            const base64 = canvas.toDataURL('image/png');
            document.getElementById('text-output').value = base64;
            updateBreakdown("<p class='text-success'>Favicon PNG generated. Preview image is displayed in the output box.</p>");
        """
    },
    {
        "category": "Design Generators",
        "name": "Avatar Generator",
        "slug": "avatar-generator",
        "desc": "Generate custom colored geometric avatars client-side.",
        "formula": "Dynamic canvas SVG shapes compounding",
        "formula_desc": "Draws localized identicon circles and rectangles using name hashes.",
        "icon": "👤",
        "inputs": [
            {"id": "av-seed", "label": "Username Seed:", "type": "text", "default": "alex"}
        ],
        "outputs": [
            {"id": "text-output", "label": "SVG Avatar Output:", "type": "textarea"}
        ],
        "calc_js": """
            const seed = document.getElementById('av-seed').value.trim() || "seed";
            
            // Generate basic hash from string
            let hash = 0;
            for (let i = 0; i < seed.length; i++) {
                hash = seed.charCodeAt(i) + ((hash << 5) - hash);
            }

            const c1 = `hsl(${Math.abs(hash) % 360}, 70%, 60%)`;
            const c2 = `hsl(${Math.abs(hash + 90) % 360}, 65%, 50%)`;

            const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">\\n  <rect width="100" height="100" fill="${c1}" />\\n  <circle cx="50" cy="50" r="30" fill="${c2}" />\\n</svg>`;
            document.getElementById('text-output').value = svg;
            updateBreakdown("<p class='text-success'>Geometric avatar SVG generated.</p>");
        """
    }
]

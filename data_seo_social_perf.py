# -*- coding: utf-8 -*-
"""
Database of 20 Social Media and Web Performance Tools for Enginewheels
"""

SOCIAL_PERF_TOOLS = [
    {
        "category": "Social Media SEO Tools",
        "name": "Hashtag Generator",
        "slug": "hashtag-generator",
        "desc": "Generate relevant hashtags based on a seed keyword to expand your social media reach.",
        "formula": "Seed phrase suffix mapping",
        "formula_desc": "Combines search terms with popular viral modifiers and social hashtags to build tag clouds.",
        "icon": "#️⃣",
        "inputs": [
            {"id": "hash-seed", "label": "Enter Seed Keyword:", "type": "text", "default": "seo tips"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Hashtags List:", "type": "textarea"}
        ],
        "calc_js": """
            const seed = document.getElementById('hash-seed').value.trim().toLowerCase().replace(/\\s+/g, "");
            if (!seed) {
                showToast("Please enter a seed keyword.", "error");
                return;
            }
            
            const suffixes = ["daily", "guide", "life", "expert", "hacks", "marketing", "trends", "goals", "community", "business"];
            const list = [`#${seed}`];
            
            suffixes.forEach(s => {
                list.push(`#${seed}${s}`);
                list.push(`#${s}${seed}`);
            });
            
            document.getElementById('text-output').value = list.join(" ");
            updateBreakdown(`<p class='text-success'>Generated <strong>${list.length}</strong> hashtags.</p>`);
        """
    },
    {
        "category": "Social Media SEO Tools",
        "name": "Social Preview Generator",
        "slug": "social-preview-generator",
        "desc": "Preview how shared links appear on popular social networks like Facebook and LinkedIn.",
        "formula": "Card viewport mockup",
        "formula_desc": "Renders visual mockups mimicking social media layouts, card image constraints, and text lengths.",
        "icon": "💬",
        "inputs": [
            {"id": "prv-title", "label": "Social Title:", "type": "text", "default": "Free XML Beautifier Online - Enginewheels"},
            {"id": "prv-desc", "label": "Social Description:", "type": "text", "default": "Optimize XML snippets inside your browser session locally and privately."},
            {"id": "prv-image", "label": "Social Image Link:", "type": "text", "default": "https://enginewheels.com/assets/img/og-preview.png"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Social Preview Status:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('prv-title').value.trim();
            const desc = document.getElementById('prv-desc').value.trim();
            const img = document.getElementById('prv-image').value.trim();
            
            let status = `Title characters: ${title.length}\\n`;
            status += `Description characters: ${desc.length}\\n\\n`;
            status += `Status: Preview Mockup rendered below.`;
            
            document.getElementById('text-output').value = status;
            
            const cardHtml = `
                <div style="background:#fff; color:#1c1e21; border:1px solid #dddfe2; border-radius:8px; overflow:hidden; font-family:Helvetica,Arial,sans-serif; text-align:left; max-width:480px; margin:15px auto;">
                    <div style="height:250px; background:#f0f2f5 url('${img}') no-repeat center; background-size:cover;"></div>
                    <div style="padding:12px; background:#f2f3f5; border-top:1px solid #dddfe2;">
                        <div style="font-size:12px; color:#606770; text-transform:uppercase; margin-bottom:4px;">enginewheels.com</div>
                        <div style="font-size:16px; font-weight:600; color:#1c1e21; margin-bottom:4px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${title}</div>
                        <div style="font-size:14px; color:#606770; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; line-height:18px;">${desc}</div>
                    </div>
                </div>
            `;
            updateBreakdown(cardHtml);
        """
    },
    {
        "category": "Social Media SEO Tools",
        "name": "Open Graph Preview Tool",
        "slug": "open-graph-preview-tool",
        "desc": "Check Open Graph properties and display a Facebook style social preview.",
        "formula": "OG tag key extraction check",
        "formula_desc": "Locates og:title, og:description, and og:image property attributes to preview layout tags.",
        "icon": "🌐",
        "inputs": [
            {"id": "og-snippet", "label": "Paste HTML Header Snippet:", "type": "textarea", "default": '<meta property="og:title" content="Sitemap Tool">\\n<meta property="og:description" content="Verify sitemaps.xml online.">\\n<meta property="og:image" content="https://enginewheels.com/preview.png">'}
        ],
        "outputs": [
            {"id": "text-output", "label": "OG Audit Summary:", "type": "textarea"}
        ],
        "calc_js": """
            const html = document.getElementById('og-snippet').value.trim();
            if (!html) {
                showToast("Please enter an HTML snippet.", "error");
                return;
            }
            
            const titleMatch = html.match(/property=['\"]og:title['\"][^>]+content=['\"]([^'\"]+)['\"]/i);
            const descMatch = html.match(/property=['\"]og:description['\"][^>]+content=['\"]([^'\"]+)['\"]/i);
            const imgMatch = html.match(/property=['\"]og:image['\"][^>]+content=['\"]([^'\"]+)['\"]/i);
            
            const title = titleMatch ? titleMatch[1] : "No Title Found";
            const desc = descMatch ? descMatch[1] : "No Description Found";
            const img = imgMatch ? imgMatch[1] : "";
            
            let report = `OG Title: ${title}\\n`;
            report += `OG Description: ${desc}\\n`;
            report += `OG Image URL: ${img || "None"}\\n\\n`;
            
            if (titleMatch && descMatch) {
                report += "[✔] Critical OG properties are valid.";
            } else {
                report += "[WARNING] Some OpenGraph properties are missing.";
            }
            
            document.getElementById('text-output').value = report;
            
            const card = `
                <div style="background:#fff; border:1px solid #dddfe2; border-radius:8px; max-width:400px; margin:15px auto; overflow:hidden; font-family:Helvetica,sans-serif; text-align:left; color:#000;">
                    <div style="height:200px; background:#e9ebee url('${img}') no-repeat center; background-size:cover;"></div>
                    <div style="padding:10px; background:#f2f3f5;">
                        <div style="font-size:12px; color:#90949c;">ENGINEWHEELS.COM</div>
                        <div style="font-size:14px; font-weight:bold; margin-top:2px;">${title}</div>
                        <div style="font-size:12px; color:#4b4f56; margin-top:2px;">${desc}</div>
                    </div>
                </div>
            `;
            updateBreakdown(card);
        """
    },
    {
        "category": "Social Media SEO Tools",
        "name": "Twitter Card Preview Tool",
        "slug": "twitter-card-preview-tool",
        "desc": "Check Twitter Card tags and render a Twitter (X) post mockup preview.",
        "formula": "Twitter key parsing check",
        "formula_desc": "Pulls twitter:card, twitter:title, and twitter:image tags to construct an X snippet box.",
        "icon": "🐦",
        "inputs": [
            {"id": "tw-snippet", "label": "Paste Twitter Tags:", "type": "textarea", "default": '<meta name="twitter:title" content="Developer Tools">\\n<meta name="twitter:description" content="Free text utilities.">\\n<meta name="twitter:image" content="https://enginewheels.com/card.png">'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Twitter Card Audit:", "type": "textarea"}
        ],
        "calc_js": """
            const html = document.getElementById('tw-snippet').value.trim();
            if (!html) {
                showToast("Please enter an HTML snippet.", "error");
                return;
            }
            
            const titleMatch = html.match(/name=['\"]twitter:title['\"][^>]+content=['\"]([^'\"]+)['\"]/i);
            const descMatch = html.match(/name=['\"]twitter:description['\"][^>]+content=['\"]([^'\"]+)['\"]/i);
            const imgMatch = html.match(/name=['\"]twitter:image['\"][^>]+content=['\"]([^'\"]+)['\"]/i);
            
            const title = titleMatch ? titleMatch[1] : "No Title Found";
            const desc = descMatch ? descMatch[1] : "No Description Found";
            const img = imgMatch ? imgMatch[1] : "";
            
            let report = `Twitter Title: ${title}\\n`;
            report += `Twitter Description: ${desc}\\n`;
            report += `Twitter Image: ${img || "None"}\\n\\n`;
            
            if (titleMatch && descMatch) {
                report += "[✔] Twitter Card properties are valid.";
            } else {
                report += "[WARNING] Critical Twitter tags are missing.";
            }
            
            document.getElementById('text-output').value = report;
            
            const card = `
                <div style="background:#000; color:#fff; border:1px solid #2f3336; border-radius:16px; max-width:400px; margin:15px auto; overflow:hidden; font-family:system-ui,sans-serif; text-align:left;">
                    <div style="height:200px; background:#15181c url('${img}') no-repeat center; background-size:cover;"></div>
                    <div style="padding:12px;">
                        <div style="font-size:13px; color:#71767b;">enginewheels.com</div>
                        <div style="font-size:15px; font-weight:bold; margin-top:2px;">${title}</div>
                        <div style="font-size:13px; color:#71767b; margin-top:2px;">${desc}</div>
                    </div>
                </div>
            `;
            updateBreakdown(card);
        """
    },
    {
        "category": "Social Media SEO Tools",
        "name": "YouTube Tag Generator",
        "slug": "youtube-tag-generator",
        "desc": "Generate relevant video tags to optimize your YouTube video rankings.",
        "formula": "Topic tag compounding",
        "formula_desc": "Combines search keywords with standard video categories (tutorial, review, guide, tips) to generate metadata tags.",
        "icon": "📺",
        "inputs": [
            {"id": "yt-keyword", "label": "Video Main Keyword:", "type": "text", "default": "how to build websites"}
        ],
        "outputs": [
            {"id": "text-output", "label": "YouTube Tags Output:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('yt-keyword').value.trim().toLowerCase();
            if (!kw) {
                showToast("Please enter a main keyword.", "error");
                return;
            }
            
            const suffixes = ["tutorial", "for beginners", "guide", "tips", "tricks", "walkthrough", "easy", "demo", "training"];
            const list = [kw];
            
            suffixes.forEach(s => {
                list.push(`${kw} ${s}`);
                list.push(`${s} ${kw}`);
            });
            
            document.getElementById('text-output').value = list.join(", ");
            updateBreakdown(`<p class='text-success'>Generated <strong>${list.length}</strong> video tags.</p>`);
        """
    },
    {
        "category": "Social Media SEO Tools",
        "name": "YouTube SEO Analyzer",
        "slug": "youtube-seo-analyzer",
        "desc": "Analyze YouTube video titles and descriptions to verify formatting standards.",
        "formula": "YT character length audit check",
        "formula_desc": "Checks length parameters of video titles, descriptions, and verifies tag limits.",
        "icon": "🔬",
        "inputs": [
            {"id": "yt-title", "label": "Video Title:", "type": "text", "default": "Learn Web Design Fast - Beginner Tutorial"},
            {"id": "yt-desc", "label": "Video Description:", "type": "textarea", "default": "In this video we learn design tips. Check out the links below.\\nhttps://site.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "SEO Analyzer Report:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('yt-title').value.trim();
            const desc = document.getElementById('yt-desc').value.trim();
            
            let report = "YOUTUBE SEO ANALYSIS\\n=====================\\n\\n";
            
            // Title Check
            const tLen = title.length;
            report += `Title Length: ${tLen} characters (Limit: 100)\\n`;
            if (tLen === 0) {
                report += "- [ERROR] Title is empty!\\n";
            } else if (tLen > 70) {
                report += "- [WARNING] Title is long (>70 chars) and might get truncated in search listings.\\n";
            } else {
                report += "- [OK] Title length is good.\\n";
            }
            
            // Description check
            const dLen = desc.length;
            report += `\\nDescription Length: ${dLen} characters (Limit: 5000)\\n`;
            if (dLen < 150) {
                report += "- [WARNING] Description is short. Try expanding it to at least 150 characters.\\n";
            } else {
                report += "- [OK] Description length is good.\\n";
            }
            
            if (desc.includes("http://") || desc.includes("https://")) {
                report += "- [OK] Description contains link references for viewer redirection.\\n";
            } else {
                report += "- [WARNING] Description lacks external link references. Add link references.\\n";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>YouTube SEO analysis completed.</p>");
        """
    },
    {
        "category": "Social Media SEO Tools",
        "name": "Video Title Generator",
        "slug": "video-title-generator",
        "desc": "Generate click-worthy and viral YouTube video titles using keyword templates.",
        "formula": "CTR hook concatenation",
        "formula_desc": "Blends keywords with click-through rate booster prefixes (e.g. Stop Doing, Avoid, Ultimate Guide) to construct titles.",
        "icon": "📺",
        "inputs": [
            {"id": "yt-keyword", "label": "Main Keyword:", "type": "text", "default": "SEO Hacks"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Video Titles:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('yt-keyword').value.trim();
            if (!kw) {
                showToast("Please enter a keyword.", "error");
                return;
            }
            
            const hooks = [
                `The Ultimate Guide to ${kw} (Step-by-Step)`,
                `Avoid These 5 Common ${kw} Mistakes!`,
                `How to Master ${kw} in 10 Minutes`,
                `Why Your ${kw} is Failing (And How to Fix It)`,
                `5 Simple ${kw} Tips to Double Your Traffic`
            ];
            
            document.getElementById('text-output').value = hooks.join("\\n");
            updateBreakdown("<p class='text-success'>YouTube title concepts compiled.</p>");
        """
    },
    {
        "category": "Social Media SEO Tools",
        "name": "Video Description Generator",
        "slug": "video-description-generator",
        "desc": "Generate formatted description copy blueprints for your YouTube video uploads.",
        "formula": "Section block template compounding",
        "formula_desc": "Combines video intro sections, links, social channels, and disclaimers into descriptions blocks.",
        "icon": "📝",
        "inputs": [
            {"id": "desc-intro", "label": "Video Introduction Details:", "type": "textarea", "default": "Learn how to optimize sitemaps and improve crawling visibility."},
            {"id": "desc-links", "label": "Reference Links (One per line):", "type": "textarea", "default": "https://enginewheels.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Video Description:", "type": "textarea"}
        ],
        "calc_js": """
            const intro = document.getElementById('desc-intro').value.trim();
            const links = document.getElementById('desc-links').value.trim();
            
            let desc = `ABOUT THIS VIDEO\\n${intro}\\n\\n`;
            if (links) {
                desc += `RESOURCES & LINKS\\n${links}\\n\\n`;
            }
            desc += "TIMESTAMPS\\n0:00 - Introduction\\n1:30 - Core Demonstration\\n5:00 - Outro & Summary\\n\\n";
            desc += "---------------------\\nDon't forget to Like, Comment, and Subscribe for more developer and webmaster tutorials!";
            
            document.getElementById('text-output').value = desc;
            updateBreakdown("<p class='text-success'>Video description layout generated.</p>");
        """
    },
    {
        "category": "Social Media SEO Tools",
        "name": "Social Bio Generator",
        "slug": "social-bio-generator",
        "desc": "Generate custom biography copy for Twitter, Instagram, or LinkedIn profiles.",
        "formula": "Tone-based keyword layout",
        "formula_desc": "Synthesizes bio profiles combining tags, keywords, and call-to-actions based on selected tones.",
        "icon": "👤",
        "inputs": [
            {"id": "bio-keywords", "label": "Skills / Keyword Tags:", "type": "text", "default": "SEO Consultant, Developer"},
            {"id": "bio-tone", "label": "Bio Tone Style:", "type": "select", "default": "professional",
             "options": [
                 ("professional", "Professional (LinkedIn style)"),
                 ("creative", "Creative & Emoji-rich (Instagram style)"),
                 ("short", "Minimal & Punchy (Twitter style)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Profile Bio:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('bio-keywords').value.trim();
            const tone = document.getElementById('bio-tone').value;
            
            if (!kw) {
                showToast("Please enter skills or keywords.", "error");
                return;
            }
            
            let result = "";
            if (tone === "professional") {
                result = `${kw} | Dedicated to building and optimizing modern web platforms. Helping startups scale search traffic. Contact for consultations.`;
            } else if (tone === "creative") {
                result = `✨ ${kw} ✨\\n🚀 Designing the future of the web\\n💻 Coding client-side tools\\n👇 Check out my utilities!`;
            } else {
                result = `${kw}. Code & optimization.`;
            }
            
            document.getElementById('text-output').value = result;
            updateBreakdown("<p class='text-success'>Social bio copy compiled.</p>");
        """
    },
    {
        "category": "Social Media SEO Tools",
        "name": "Social Caption Generator",
        "slug": "social-caption-generator",
        "desc": "Generate captions with structured spacing, emojis, and hashtags for social posts.",
        "formula": "Tag formatting layout",
        "formula_desc": "Combines title hooks, body text blocks, hashtags, and spacing elements into social captions.",
        "icon": "💬",
        "inputs": [
            {"id": "cap-hook", "label": "Headline Hook:", "type": "text", "default": "Stop wasting time on local CLI setups!"},
            {"id": "cap-body", "label": "Main Post Message:", "type": "textarea", "default": "We built 130 online SEO tools that run locally inside your browser."},
            {"id": "cap-tags", "label": "Hashtags (Comma separated):", "type": "text", "default": "seo, webmaster"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted Caption Output:", "type": "textarea"}
        ],
        "calc_js": """
            const hook = document.getElementById('cap-hook').value.trim();
            const body = document.getElementById('cap-body').value.trim();
            const tagsRaw = document.getElementById('cap-tags').value.trim();
            
            if (!hook || !body) {
                showToast("Hook and Post Message are required.", "error");
                return;
            }
            
            const tags = tagsRaw.split(",").map(t => "#" + t.trim().replace(/^#/, "")).join(" ");
            let caption = `🚨 ${hook.toUpperCase()} 🚨\\n\\n`;
            caption += `${body}\\n\\n`;
            if (tags) {
                caption += `.\\n.\\n${tags}`;
            }
            
            document.getElementById('text-output').value = caption;
            updateBreakdown("<p class='text-success'>Social media caption formatted.</p>");
        """
    },
    {
        "category": "Web Performance Tools",
        "name": "Page Size Calculator",
        "slug": "page-size-calculator",
        "desc": "Calculate the total weight of a page based on files sizes of HTML, CSS, images, and script assets.",
        "formula": "Page Weight = HTML + CSS + JS + Images",
        "formula_desc": "Sums the file sizes of all page resources to estimate total page weight and page load speed.",
        "icon": "⚖️",
        "inputs": [
            {"id": "sz-html", "label": "HTML Code Size (KB):", "type": "number", "default": "25", "min": "0"},
            {"id": "sz-css", "label": "CSS Stylesheets Size (KB):", "type": "number", "default": "50", "min": "0"},
            {"id": "sz-js", "label": "JavaScript Files Size (KB):", "type": "number", "default": "120", "min": "0"},
            {"id": "sz-img", "label": "Images & Assets Size (KB):", "type": "number", "default": "450", "min": "0"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Total Page Size Audit:", "type": "textarea"}
        ],
        "calc_js": """
            const html = parseFloat(document.getElementById('sz-html').value) || 0;
            const css = parseFloat(document.getElementById('sz-css').value) || 0;
            const js = parseFloat(document.getElementById('sz-js').value) || 0;
            const img = parseFloat(document.getElementById('sz-img').value) || 0;
            
            const total = html + css + js + img;
            let report = `Total Page Weight: ${total.toFixed(1)} KB (${(total/1024).toFixed(2)} MB)\\n\\n`;
            
            if (total > 2048) {
                report += "[✘] Page size is heavy (> 2MB). Mobile users on 3G connections will experience slow load times. Optimize images and compress scripts.";
            } else if (total > 1024) {
                report += "[WARNING] Page weight is moderate (1-2MB). Try enabling lazy loading for images and minifying stylesheets.";
            } else {
                report += "[✔] Page weight is optimal (< 1MB). Excellent performance target.";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Total calculated page weight is <strong>${total.toFixed(1)} KB</strong>.</p>`);
        """
    },
    {
        "category": "Web Performance Tools",
        "name": "Asset Size Analyzer",
        "slug": "asset-size-analyzer",
        "desc": "Calculate file size reductions and compression savings (Gzip/Brotli).",
        "formula": "Savings % = ((Original - Compressed) / Original) * 100",
        "formula_desc": "Estimates typical Gzip (70% savings) and Brotli (75% savings) compression metrics based on input file sizes.",
        "icon": "📦",
        "inputs": [
            {"id": "orig-size", "label": "Original File Size (KB):", "type": "number", "default": "150", "min": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Compression Savings Report:", "type": "textarea"}
        ],
        "calc_js": """
            const size = parseFloat(document.getElementById('orig-size').value) || 0;
            if (size <= 0) {
                showToast("Please enter a valid positive file size.", "error");
                return;
            }
            
            const gzip = size * 0.3; // 70% savings
            const brotli = size * 0.25; // 75% savings
            
            let report = `Original File Size: ${size} KB\\n\\n`;
            report += `Estimated Gzip Size: ${gzip.toFixed(1)} KB (70% compression savings)\\n`;
            report += `Estimated Brotli Size: ${brotli.toFixed(1)} KB (75% compression savings)\\n\\n`;
            report += "Note: Enabling Gzip or Brotli compression on your web server (Nginx/Apache) significantly reduces page load times for text assets (HTML, CSS, JS).";
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Compression estimates compiled.</p>");
        """
    },
    {
        "category": "Web Performance Tools",
        "name": "Image SEO Analyzer",
        "slug": "image-seo-analyzer",
        "desc": "Check image tag code blocks for missing alt tags, incorrect sizes, and formatting issues.",
        "formula": "Image tag metadata verification",
        "formula_desc": "Checks image tags for alt attributes, file extension formats, and checks if filenames contain dashes instead of underscores.",
        "icon": "🖼️",
        "inputs": [
            {"id": "img-tag", "label": "Paste HTML Image Tag:", "type": "text", "default": '<img src="logo_main.png" width="200">'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Image SEO Analysis:", "type": "textarea"}
        ],
        "calc_js": """
            const html = document.getElementById('img-tag').value.trim();
            if (!html || !html.startsWith("<img")) {
                showToast("Please paste a valid HTML <img> tag.", "error");
                return;
            }
            
            let report = "IMAGE SEO AUDIT\\n===============\\n\\n";
            
            // Check alt
            const altMatch = html.match(/alt=['\"]([^'\"]*)['\"]/i);
            if (altMatch) {
                report += `[✔] Alt Attribute Found: "${altMatch[1]}"\\n`;
                if (altMatch[1].trim() === "") {
                    report += "  - [WARNING] Alt text is empty. Describe the image for better search indexing.\\n";
                }
            } else {
                report += "[✘] Alt Attribute Missing! Search engines use alt text to index images.\\n";
            }
            
            // Check src filename
            const srcMatch = html.match(/src=['\"]([^'\"]+)['\"]/i);
            if (srcMatch) {
                const filename = srcMatch[1].split('/').pop();
                report += `Filename: "${filename}"\\n`;
                if (/_/.test(filename)) {
                    report += "  - [WARNING] Filename contains underscores (_). Use hyphens (-) for search optimization.\\n";
                }
                if (/\\.(png|jpe?g)$/i.test(filename)) {
                    report += "  - [NOTE] Consider converting PNG/JPG images to next-gen formats like WebP for faster page loads.\\n";
                }
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Image tag audited.</p>");
        """
    },
    {
        "category": "Web Performance Tools",
        "name": "CSS Minifier",
        "slug": "css-minifier",
        "desc": "Minify CSS code by stripping spaces, comments, and line breaks to improve page load speed.",
        "formula": "CSS compression parsing rules",
        "formula_desc": "Strips CSS block comments, collapses sequential whitespaces, and removes line breaks.",
        "icon": "🎨",
        "inputs": [
            {"id": "css-raw", "label": "Paste Raw CSS Code:", "type": "textarea", "default": "/* Theme style block */\\nbody {\\n  background-color: #000;\\n  color: #fff;\\n}"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Minified CSS Output:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('css-raw').value.trim();
            if (!raw) {
                showToast("Please paste some CSS code.", "error");
                return;
            }
            
            // Basic regex CSS minifier
            let clean = raw.replace(/\\/\\*[^*]*\\*+([^/*][^*]*\\*+)*\\//g, ''); // Remove comments
            clean = clean.replace(/\\s*([{}|:;,])\\s*/g, '$1'); // Collapse spacing
            clean = clean.replace(/\\s+/g, ' '); // Collapse whitespaces
            clean = clean.trim();
            
            document.getElementById('text-output').value = clean;
            
            const reduction = ((raw.length - clean.length) / raw.length * 100).toFixed(1);
            updateBreakdown(`<p class='text-success'>CSS minified successfully. Size reduced by <strong>${reduction}%</strong>.</p>`);
        """
    },
    {
        "category": "Web Performance Tools",
        "name": "JavaScript Minifier",
        "slug": "javascript-minifier",
        "desc": "Minify JavaScript code by removing comments, spacing, and line breaks.",
        "formula": "JS syntax spacing compression",
        "formula_desc": "Strips single-line and multi-line comments, collapses whitespaces, and removes line breaks.",
        "icon": "⚡",
        "inputs": [
            {"id": "js-raw", "label": "Paste Raw JavaScript Code:", "type": "textarea", "default": "// Simple log helper\\nfunction logMsg(msg) {\\n  console.log(msg);\\n}"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Minified JavaScript Output:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('js-raw').value.trim();
            if (!raw) {
                showToast("Please enter JavaScript code.", "error");
                return;
            }
            
            // Basic regex JS minifier
            let clean = raw.replace(/\\/\\*[^*]*\\*+([^/*][^*]*\\*+)*\\//g, ''); // Block comments
            clean = clean.replace(/\\/\\/.*$/gm, ''); // Inline comments
            clean = clean.replace(/\\s+/g, ' '); // Spaces
            clean = clean.trim();
            
            document.getElementById('text-output').value = clean;
            const reduction = ((raw.length - clean.length) / raw.length * 100).toFixed(1);
            updateBreakdown(`<p class='text-success'>JavaScript minified. Size reduced by <strong>${reduction}%</strong>.</p>`);
        """
    },
    {
        "category": "Web Performance Tools",
        "name": "HTML Minifier",
        "slug": "html-minifier",
        "desc": "Minify HTML source code by removing comments and unnecessary spaces.",
        "formula": "HTML parsing compression",
        "formula_desc": "Strips HTML comment blocks and collapses whitespaces between elements.",
        "icon": "🌐",
        "inputs": [
            {"id": "html-raw", "label": "Paste HTML Source Code:", "type": "textarea", "default": '<!-- Main header -->\\n<div class="container">\\n  <h1>Title</h1>\\n</div>'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Minified HTML Output:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('html-raw').value.trim();
            if (!raw) {
                showToast("Please enter HTML code.", "error");
                return;
            }
            
            // Basic HTML minifier
            let clean = raw.replace(/<!--[\\s\\S]*?-->/g, ''); // Comments
            clean = clean.replace(/\\s+/g, ' '); // Spaces
            clean = clean.replace(/>\\s+</g, '><'); // Inter-element spaces
            clean = clean.trim();
            
            document.getElementById('text-output').value = clean;
            const reduction = ((raw.length - clean.length) / raw.length * 100).toFixed(1);
            updateBreakdown(`<p class='text-success'>HTML minified. Size reduced by <strong>${reduction}%</strong>.</p>`);
        """
    },
    {
        "category": "WebPerformance Tools",
        "name": "WebP Optimization Tool",
        "slug": "webp-optimization-tool",
        "desc": "Calculate size reductions and loading speed benefits of converting files to WebP.",
        "formula": "WebP size mapping calculations",
        "formula_desc": "Calculates file size savings (typically 80% for PNG and 35% for JPEG) when converting images to WebP.",
        "icon": "🖼️",
        "inputs": [
            {"id": "img-type", "label": "Image Format:", "type": "select", "default": "png",
             "options": [
                 ("png", "PNG (Lossless Image)"),
                 ("jpg", "JPEG (Photographic Image)")
             ]},
            {"id": "img-size", "label": "Original Image Size (KB):", "type": "number", "default": "500", "min": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "WebP Savings Report:", "type": "textarea"}
        ],
        "calc_js": """
            const type = document.getElementById('img-type').value;
            const size = parseFloat(document.getElementById('img-size').value) || 0;
            
            if (size <= 0) {
                showToast("Please provide a valid file size.", "error");
                return;
            }
            
            const savingsFactor = type === "png" ? 0.8 : 0.35; // PNG 80% reduction, JPG 35%
            const savings = size * savingsFactor;
            const finalSize = size - savings;
            
            let report = `Original Format: ${type.toUpperCase()}\\n`;
            report += `Original Size: ${size} KB\\n\\n`;
            report += `Estimated WebP Size: ${finalSize.toFixed(1)} KB\\n`;
            report += `Estimated Savings: ${savings.toFixed(1)} KB (${(savingsFactor*100).toFixed(0)}% smaller)\\n\\n`;
            report += "Recommendation: Converting assets to WebP reduces bandwidth usage and improves page load speed.";
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>WebP size calculations completed.</p>");
        """
    },
    {
        "category": "Web Performance Tools",
        "name": "Lazy Load Generator",
        "slug": "lazy-load-generator",
        "desc": "Generate HTML image tags with loading=lazy attributes to improve page load speed.",
        "formula": "HTML image tag loading interpolation",
        "formula_desc": "Generates image tags configured with loading='lazy' attributes to defer off-screen image loading.",
        "icon": "🖼️",
        "inputs": [
            {"id": "img-src", "label": "Image File Link:", "type": "text", "default": "/assets/img/hero.png"},
            {"id": "img-alt", "label": "Alt Description Text:", "type": "text", "default": "Hero Image Banner"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated HTML Image Tag:", "type": "textarea"}
        ],
        "calc_js": """
            const src = document.getElementById('img-src').value.trim();
            const alt = document.getElementById('img-alt').value.trim();
            
            if (!src) {
                showToast("Please provide an image link.", "error");
                return;
            }
            
            const tag = `<img src="${src}" alt="${alt.replace(/"/g, '&quot;')}" loading="lazy">`;
            document.getElementById('text-output').value = tag;
            updateBreakdown("<p class='text-success'>Lazy-loading image tag generated.</p>");
        """
    },
    {
        "category": "Web Performance Tools",
        "name": "Core Web Vitals Guide Tool",
        "slug": "core-web-vitals-guide-tool",
        "desc": "Rate loading performance and stability based on Core Web Vitals metric inputs.",
        "formula": "Threshold rating alignment",
        "formula_desc": "Grades input LCP, FID, and CLS scores against Google's Core Web Vitals rating thresholds.",
        "icon": "📊",
        "inputs": [
            {"id": "lcp-val", "label": "Largest Contentful Paint (LCP) in seconds:", "type": "number", "default": "2.2", "step": "0.1", "min": "0"},
            {"id": "fid-val", "label": "First Input Delay (FID) in milliseconds:", "type": "number", "default": "80", "min": "0"},
            {"id": "cls-val", "label": "Cumulative Layout Shift (CLS):", "type": "number", "default": "0.08", "step": "0.01", "min": "0"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Core Web Vitals Report:", "type": "textarea"}
        ],
        "calc_js": """
            const lcp = parseFloat(document.getElementById('lcp-val').value) || 0;
            const fid = parseFloat(document.getElementById('fid-val').value) || 0;
            const cls = parseFloat(document.getElementById('cls-val').value) || 0;
            
            let report = "CORE WEB VITALS PERFORMANCE AUDIT\\n==================================\\n\\n";
            let goodCount = 0;
            
            // LCP Audit
            report += `LCP: ${lcp}s -> `;
            if (lcp <= 2.5) { report += "GOOD\\n"; goodCount++; }
            else if (lcp <= 4.0) { report += "NEEDS IMPROVEMENT\\n"; }
            else { report += "POOR\\n"; }
            
            // FID Audit
            report += `FID: ${fid}ms -> `;
            if (fid <= 100) { report += "GOOD\\n"; goodCount++; }
            else if (fid <= 300) { report += "NEEDS IMPROVEMENT\\n"; }
            else { report += "POOR\\n"; }
            
            // CLS Audit
            report += `CLS: ${cls} -> `;
            if (cls <= 0.1) { report += "GOOD\\n"; goodCount++; }
            else if (cls <= 0.25) { report += "NEEDS IMPROVEMENT\\n"; }
            else { report += "POOR\\n"; }
            
            report += `\\nPerformance Status: ${goodCount}/3 Metrics meet optimal thresholds.`;
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Core Web Vitals metrics audited.</p>");
        """
    },
    {
        "category": "Web Performance Tools",
        "name": "Resource Optimization Analyzer",
        "slug": "resource-optimization-analyzer",
        "desc": "Generate browser resource directives (preconnect, dns-prefetch, preload) to speed up asset loading.",
        "formula": "Resource directive tag compilation",
        "formula_desc": "Outputs HTML link tags configured with preconnect, dns-prefetch, or preload attributes for target URLs.",
        "icon": "⚡",
        "inputs": [
            {"id": "res-url", "label": "Resource / Asset URL:", "type": "text", "default": "https://fonts.googleapis.com"},
            {"id": "res-rel", "label": "Link Relationship (rel):", "type": "select", "default": "preconnect",
             "options": [
                 ("preconnect", "Preconnect (Resolve DNS, TCP, and TLS)"),
                 ("dns-prefetch", "DNS-Prefetch (Resolve DNS only)"),
                 ("preload", "Preload (High-priority download asset)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Link Tag:", "type": "textarea"}
        ],
        "calc_js": """
            const url = document.getElementById('res-url').value.trim();
            const rel = document.getElementById('res-rel').value;
            
            if (!url) {
                showToast("Please provide a resource URL.", "error");
                return;
            }
            
            let tag = `<link rel="${rel}" href="${url}">`;
            if (rel === "preload") {
                tag = `<link rel="preload" href="${url}" as="script">`;
            }
            
            document.getElementById('text-output').value = tag;
            updateBreakdown("<p class='text-success'>Resource loading directive generated.</p>");
        """
    }
]

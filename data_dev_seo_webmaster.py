# -*- coding: utf-8 -*-
"""
Database of 6 unique SEO & Webmaster Tools for Enginewheels (excluding duplicates)
"""

SEO_WEBMASTER_TOOLS = [
    {
        "category": "SEO & Webmaster Tools",
        "name": "Twitter Card Generator",
        "slug": "twitter-card-generator",
        "desc": "Generate custom Twitter Card meta tags for responsive social media previews.",
        "formula": "twitter:card, twitter:title, twitter:description",
        "formula_desc": "Compiles Twitter metadata tags used by Twitter crawlers to construct link cards.",
        "icon": "🐦",
        "inputs": [
            {"id": "tc-handle", "label": "Twitter Username (@):", "type": "text", "default": "@enginewheels"},
            {"id": "tc-title", "label": "Card Title:", "type": "text", "default": "Free Developer Tools"},
            {"id": "tc-desc", "label": "Card Description:", "type": "text", "default": "Optimize and format code online."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Twitter Card Meta Tags:", "type": "textarea"}
        ],
        "calc_js": """
            const handle = document.getElementById('tc-handle').value.trim();
            const title = document.getElementById('tc-title').value.trim();
            const desc = document.getElementById('tc-desc').value.trim();
            
            let tags = `<!-- Twitter Card Metadata -->\\n`;
            tags += `<meta name="twitter:card" content="summary_large_image">\\n`;
            if (handle) tags += `<meta name="twitter:site" content="${handle}">\\n`;
            tags += `<meta name="twitter:title" content="${title}">\\n`;
            tags += `<meta name="twitter:description" content="${desc}">`;
            
            document.getElementById('text-output').value = tags;
            updateBreakdown("<p class='text-success'>Twitter card tags generated. Paste them inside your HTML header.</p>");
        """
    },
    {
        "category": "SEO & Webmaster Tools",
        "name": "Canonical URL Generator",
        "slug": "canonical-url-generator",
        "desc": "Generate canonical link tags to resolve duplicate page indexing issues.",
        "formula": "link rel='canonical' href='url'",
        "formula_desc": "Outputs HTML canonical tags telling crawlers which URL is the master version of the page.",
        "icon": "🔗",
        "inputs": [
            {"id": "can-url", "label": "Canonical URL:", "type": "text", "default": "https://enginewheels.com/tools/json-formatter.html"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Canonical Link Tag:", "type": "textarea"}
        ],
        "calc_js": """
            const url = document.getElementById('can-url').value.trim();
            if (!url) {
                showToast("Please enter a URL.", "error");
                return;
            }
            const tag = `<link rel="canonical" href="${url}">`;
            document.getElementById('text-output').value = tag;
            updateBreakdown("<p class='text-success'>Canonical tag generated.</p>");
        """
    },
    {
        "category": "SEO & Webmaster Tools",
        "name": "Schema Markup Generator",
        "slug": "schema-markup-generator",
        "desc": "Generate structured JSON-LD schema scripts for Rich Snippets.",
        "formula": "JSON-LD structured data schema schema.org",
        "formula_desc": "Assembles structured organization metadata tags consumed by Google search crawlers.",
        "icon": "🛠️",
        "inputs": [
            {"id": "sch-name", "label": "Organization / Site Name:", "type": "text", "default": "Enginewheels"},
            {"id": "sch-url", "label": "Website URL:", "type": "text", "default": "https://enginewheels.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "JSON-LD Script Output:", "type": "textarea"}
        ],
        "calc_js": """
            const name = document.getElementById('sch-name').value.trim();
            const url = document.getElementById('sch-url').value.trim();
            
            const schema = {
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": name,
                "url": url
            };
            
            const script = '<script type="application/' + 'ld+json">\\n' + JSON.stringify(schema, null, 2) + '\\n</' + 'script>';
            document.getElementById('text-output').value = script;
            updateBreakdown("<p class='text-success'>JSON-LD website schema generated. Place inside HTML head or body.</p>");
        """
    },
    {
        "category": "SEO & Webmaster Tools",
        "name": "Keyword Density Checker",
        "slug": "keyword-density-checker",
        "desc": "Check the occurrences and frequency percentage of keywords in your copy.",
        "formula": "Density = (Word count / Total Words) * 100",
        "formula_desc": "Strips punctuation, splits text into words, aggregates counts, and outputs sorted frequency ratios.",
        "icon": "📈",
        "inputs": [
            {"id": "text-input", "label": "Paste Copy Text:", "type": "textarea", "default": "Format JSON, encode URLs, and validate code structure online with tools."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Density Log:", "type": "textarea"}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            if (!text) {
                showToast("Please enter some text.", "error");
                return;
            }
            const clean = text.toLowerCase().replace(/[^a-zA-Z0-9\\s]/g, '');
            const words = clean.split(/\\s+/).filter(w => w !== '');
            const total = words.length;
            
            const freq = {};
            words.forEach(w => freq[w] = (freq[w] || 0) + 1);
            
            const sorted = Object.keys(freq).map(k => {
                return { word: k, count: freq[k], pct: (freq[k] / total * 100).toFixed(1) };
            }).sort((a, b) => b.count - a.count);
            
            let out = `Total Words parsed: ${total}\\n\\nKeyword Density Report:\\n`;
            sorted.slice(0, 15).forEach(item => {
                out += `"${item.word}": ${item.count} times (${item.pct}%)\\n`;
            });
            document.getElementById('text-output').value = out;
            updateBreakdown("<p class='text-success'>Keyword frequency calculated successfully.</p>");
        """
    },
    {
        "category": "SEO & Webmaster Tools",
        "name": "Redirect Generator",
        "slug": "redirect-generator",
        "desc": "Generate Nginx redirects or Apache .htaccess rules.",
        "formula": "Redirect OldPath NewURL config rules",
        "formula_desc": "Outputs standard server redirection configuration scripts.",
        "icon": "🔄",
        "inputs": [
            {"id": "red-old", "label": "Old Path (e.g. /old-page):", "type": "text", "default": "/old-page"},
            {"id": "red-new", "label": "New Destination URL:", "type": "text", "default": "https://enginewheels.com/new-page"},
            {"id": "red-type", "label": "Server Config Type:", "type": "select", "options": [("htaccess", "Apache .htaccess"), ("nginx", "Nginx Config")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Redirect Code Output:", "type": "textarea"}
        ],
        "calc_js": """
            const old = document.getElementById('red-old').value.trim();
            const dest = document.getElementById('red-new').value.trim();
            const type = document.getElementById('red-type').value;
            
            let code = "";
            if (type === 'htaccess') {
                code = `Redirect 301 ${old} ${dest}`;
            } else {
                code = `rewrite ^${old}$ ${dest} permanent;`;
            }
            document.getElementById('text-output').value = code;
            updateBreakdown("<p class='text-success'>Server redirect rule created.</p>");
        """
    },
    {
        "category": "SEO & Webmaster Tools",
        "name": "Hreflang Generator",
        "slug": "hreflang-generator",
        "desc": "Create alternate hreflang tags for multi-language search engine index targeting.",
        "formula": "link rel='alternate' hreflang='lang' href='url'",
        "formula_desc": "Outputs alternate link tags instructing search bots about regional page variations.",
        "icon": "🌐",
        "inputs": [
            {"id": "href-url", "label": "Page URL:", "type": "text", "default": "https://enginewheels.com/es/"},
            {"id": "href-lang", "label": "Language Code (e.g. es, fr, en):", "type": "text", "default": "es"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Alternate Hreflang Tag:", "type": "textarea"}
        ],
        "calc_js": """
            const url = document.getElementById('href-url').value.trim();
            const lang = document.getElementById('href-lang').value.trim().toLowerCase();
            if (!url || !lang) {
                showToast("URL and language codes are required.", "error");
                return;
            }
            const tag = `<link rel="alternate" hreflang="${lang}" href="${url}">`;
            document.getElementById('text-output').value = tag;
            updateBreakdown("<p class='text-success'>Hreflang translation alternate tag generated.</p>");
        """
    }
]

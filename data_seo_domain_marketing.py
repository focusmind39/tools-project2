# -*- coding: utf-8 -*-
"""
Database of 20 Domain/URL and Marketing Tools for Enginewheels
"""

DOMAIN_MARKETING_TOOLS = [
    {
        "category": "Domain & URL Tools",
        "name": "Domain Name Generator",
        "slug": "domain-name-generator-seo",
        "desc": "Generate search-friendly domain name ideas based on brand seed terms.",
        "formula": "Extension compound mapping",
        "formula_desc": "Combines brand keywords with tech/business extensions (.com, .io, .co, .net) and modifier prefixes.",
        "icon": "🌐",
        "inputs": [
            {"id": "dom-keyword", "label": "Enter Brand Keyword:", "type": "text", "default": "seo flow"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Domain Name Ideas:", "type": "textarea"}
        ],
        "calc_js": """
            const seed = document.getElementById('dom-keyword').value.trim().toLowerCase().replace(/[^a-z0-9]/g, '');
            if (!seed) {
                showToast("Please enter a brand keyword.", "error");
                return;
            }
            
            const prefixes = ["get", "try", "go", "my", "the", "smart"];
            const extensions = [".com", ".net", ".io", ".co", ".app", ".dev"];
            const list = [];
            
            extensions.forEach(ext => {
                list.push(`${seed}${ext}`);
                prefixes.forEach(p => {
                    list.push(`${p}${seed}${ext}`);
                });
            });
            
            document.getElementById('text-output').value = list.slice(0, 15).join("\\n");
            updateBreakdown("<p class='text-success'>Domain ideas generated.</p>");
        """
    },
    {
        "category": "Domain & URL Tools",
        "name": "URL Encoder",
        "slug": "url-encoder-seo",
        "desc": "Encode special characters in URLs using standard escape characters.",
        "formula": "encodeURIComponent character escaping",
        "formula_desc": "Escapes unsafe query parameters into standard percent-encoded characters using browser APIs.",
        "icon": "🔒",
        "inputs": [
            {"id": "url-raw", "label": "Enter Plain URL / String:", "type": "textarea", "default": "https://enginewheels.com/search?q=seo tools&id=10"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Encoded URL:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('url-raw').value.trim();
            if (!raw) {
                showToast("Please enter a URL to encode.", "error");
                return;
            }
            
            try {
                // If it is a full URL, encode parameters only, or encode the full string
                const encoded = encodeURIComponent(raw);
                document.getElementById('text-output').value = encoded;
                updateBreakdown("<p class='text-success'>String encoded successfully.</p>");
            } catch (e) {
                showToast("Encoding failed: " + e, "error");
            }
        """
    },
    {
        "category": "Domain & URL Tools",
        "name": "URL Decoder",
        "slug": "url-decoder-seo",
        "desc": "Decode percent-encoded URL parameters back to standard text strings.",
        "formula": "decodeURIComponent conversion rules",
        "formula_desc": "Translates percent-encoded characters back into readable UTF-8 strings.",
        "icon": "🔓",
        "inputs": [
            {"id": "url-encoded", "label": "Enter Encoded URL:", "type": "textarea", "default": "https%3A%2F%2Fenginewheels.com%2Fsearch%3Fq%3Dseo%2520tools"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded URL Output:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('url-encoded').value.trim();
            if (!raw) {
                showToast("Please enter an encoded URL.", "error");
                return;
            }
            
            try {
                const decoded = decodeURIComponent(raw);
                document.getElementById('text-output').value = decoded;
                updateBreakdown("<p class='text-success'>URL decoded successfully.</p>");
            } catch (e) {
                showToast("Decoding failed. Invalid format.", "error");
            }
        """
    },
    {
        "category": "Domain & URL Tools",
        "name": "URL Parser",
        "slug": "url-parser",
        "desc": "Parse URL strings into hostname, pathname, port, and query parameter tokens.",
        "formula": "URL component tokenization",
        "formula_desc": "Extracts protocol schema, port settings, paths, and query variables using the native browser URL constructor.",
        "icon": "🔎",
        "inputs": [
            {"id": "url-raw", "label": "Enter URL:", "type": "text", "default": "https://enginewheels.com:443/category/seo-web-tools.html?q=sitemaps#top"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Parsed URL Details:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('url-raw').value.trim();
            if (!raw) {
                showToast("Please provide a URL.", "error");
                return;
            }
            
            try {
                const url = new URL(raw);
                let report = `Protocol: ${url.protocol}\\n`;
                report += `Hostname: ${url.hostname}\\n`;
                report += `Port: ${url.port || "Default"}\\n`;
                report += `Pathname: ${url.pathname}\\n`;
                report += `Search Parameters: ${url.search || "None"}\\n`;
                report += `Hash Fragment: ${url.hash || "None"}`;
                
                document.getElementById('text-output').value = report;
                updateBreakdown("<p class='text-success'>URL parsed successfully.</p>");
            } catch (e) {
                showToast("Invalid URL format. Include protocol.", "error");
            }
        """
    },
    {
        "category": "Domain & URL Tools",
        "name": "URL Slug Generator",
        "slug": "url-slug-generator",
        "desc": "Convert text headlines into SEO-friendly URL slug strings.",
        "formula": "String sanitization mapping",
        "formula_desc": "Converts strings to lowercase, deletes non-alphanumeric marks, and replaces spacing with hyphens.",
        "icon": "🐌",
        "inputs": [
            {"id": "text-title", "label": "Enter Page Headline:", "type": "text", "default": "Free XML Formatter - Safe & Client-Side!"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated URL Slug:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('text-title').value.trim();
            if (!title) {
                showToast("Please enter headline text.", "error");
                return;
            }
            
            const slug = title.toLowerCase()
                .replace(/[^a-z0-9\\s-]/g, '') // Remove special characters
                .replace(/\\s+/g, '-')          // Replace spaces with hyphens
                .replace(/-+/g, '-')            // Collapse multiple hyphens
                .trim();
                
            document.getElementById('text-output').value = slug;
            updateBreakdown("<p class='text-success'>URL slug generated successfully.</p>");
        """
    },
    {
        "category": "Domain & URL Tools",
        "name": "URL Rewriter",
        "slug": "url-rewriter",
        "desc": "Generate search-friendly URL rewrite rules from parameters-heavy links.",
        "formula": "RewriteRule syntax mapping",
        "formula_desc": "Converts parameterized routes (e.g. page.php?id=12) into clean Apache/Nginx URL paths (e.g. page/12).",
        "icon": "🔃",
        "inputs": [
            {"id": "url-dyn", "label": "Dynamic Parameter Link:", "type": "text", "default": "https://site.com/product.php?id=15"}
        ],
        "outputs": [
            {"id": "text-output", "label": "URL Rewrite Rule:", "type": "textarea"}
        ],
        "calc_js": """
            const dyn = document.getElementById('url-dyn').value.trim();
            if (!dyn) {
                showToast("Please enter a link.", "error");
                return;
            }
            
            try {
                const url = new URL(dyn);
                const searchParams = new URLSearchParams(url.search);
                const file = url.pathname.split('/').pop();
                
                let keys = [];
                for (let key of searchParams.keys()) {
                    keys.push(key);
                }
                
                if (keys.length === 0) {
                    document.getElementById('text-output').value = "No query parameters detected in the link.";
                    return;
                }
                
                let rule = `# Apache .htaccess RewriteRule\\n`;
                rule += `RewriteEngine On\\n`;
                rule += `RewriteRule ^product/([^/]+)$ ${file}?${keys[0]}=$1 [L]`;
                
                document.getElementById('text-output').value = rule;
                updateBreakdown("<p class='text-success'>Rewrite Rule compiled.</p>");
            } catch (e) {
                showToast("Invalid URL format.", "error");
            }
        """
    },
    {
        "category": "Domain & URL Tools",
        "name": "Hreflang Generator",
        "slug": "hreflang-generator",
        "desc": "Generate hreflang link tags to declare localized versions of your pages to search engines.",
        "formula": "Hreflang attribute compilation",
        "formula_desc": "Serializes language ISO codes and relative links into standard alternate link properties.",
        "icon": "🌐",
        "inputs": [
            {"id": "lang-code", "label": "Language Code (e.g. es, fr):", "type": "text", "default": "es"},
            {"id": "lang-url", "label": "Localized Page URL:", "type": "text", "default": "https://enginewheels.com/es/index.html"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Hreflang Tag:", "type": "textarea"}
        ],
        "calc_js": """
            const lang = document.getElementById('lang-code').value.trim();
            const url = document.getElementById('lang-url').value.trim();
            
            if (!lang || !url) {
                showToast("Language and URL fields are required.", "error");
                return;
            }
            
            const tag = `<link rel="alternate" hreflang="${lang}" href="${url}">`;
            document.getElementById('text-output').value = tag;
            updateBreakdown("<p class='text-success'>Hreflang tag generated.</p>");
        """
    },
    {
        "category": "Domain & URL Tools",
        "name": "Hreflang Validator",
        "slug": "hreflang-validator",
        "desc": "Check hreflang link tags for formatting structure and valid ISO codes.",
        "formula": "ISO code syntax validation",
        "formula_desc": "Checks if the hreflang parameter matches standard 2-letter language (ISO 639-1) or region (ISO 3166-1) codes.",
        "icon": "🔎",
        "inputs": [
            {"id": "hreflang-raw", "label": "Paste Hreflang Tags:", "type": "textarea", "default": '<link rel="alternate" hreflang="es" href="https://site.com/es/">'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Hreflang Checker Report:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('hreflang-raw').value.trim();
            if (!raw) {
                showToast("Please enter hreflang tag.", "error");
                return;
            }
            
            const match = raw.match(/hreflang=['\"]([^'\"]+)['\"]/i);
            if (match) {
                const lang = match[1].toLowerCase().trim();
                let report = `Hreflang tag detected: hreflang="${lang}"\\n`;
                
                // Check if language length is 2 or 5 (e.g. en-us)
                if (lang.length === 2 || (lang.length === 5 && lang.charAt(2) === "-")) {
                    report += "[✔] Code format matches ISO requirements.\\n";
                } else {
                    report += "[WARNING] Suboptimal code format. Recommended 2-letter ISO (e.g. es, fr) or region (e.g. en-us).\\n";
                }
                
                document.getElementById('text-output').value = report;
                updateBreakdown("<p class='text-success'>Hreflang tag checked.</p>");
            } else {
                document.getElementById('text-output').value = "No hreflang attribute detected in the input code.";
            }
        """
    },
    {
        "category": "Domain & URL Tools",
        "name": "Domain Authority Tracker",
        "slug": "domain-authority-tracker",
        "desc": "Estimate search authority indicators based on backlinks profiles and domain age.",
        "formula": "Authority = 0.5 * BacklinksScore + 0.5 * AgeScore",
        "formula_desc": "Estimates simulated authority metrics using logarithmic backlinks scales and registration age details.",
        "icon": "⚖️",
        "inputs": [
            {"id": "backlinks-count", "label": "Referring Backlinks Count:", "type": "number", "default": "2500", "min": "0"},
            {"id": "age-years", "label": "Domain Age in Years:", "type": "number", "default": "4", "min": "0"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Domain Authority Score:", "type": "textarea"}
        ],
        "calc_js": """
            const links = parseFloat(document.getElementById('backlinks-count').value) || 0;
            const age = parseFloat(document.getElementById('age-years').value) || 0;
            
            // Logarithmic scale for backlinks
            const linkFactor = Math.min(100, Math.max(1, Math.log10(links + 1) * 20));
            const ageFactor = Math.min(100, Math.max(1, age * 10));
            
            const da = Math.round(0.6 * linkFactor + 0.4 * ageFactor);
            
            let report = `Estimated Domain Authority (DA): ${da}/100\\n`;
            report += `Backlinks Factor: ${linkFactor.toFixed(1)}/100\\n`;
            report += `Age Factor: ${ageFactor.toFixed(1)}/100\\n\\n`;
            report += "Note: Domain Authority is a simulated ranking indicator. Building authoritative natural links over time boosts ranking authority.";
            
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Estimated Domain Authority calculated as <strong>${da}/100</strong>.</p>`);
        """
    },
    {
        "category": "Domain & URL Tools",
        "name": "Domain Age Checker",
        "slug": "domain-age-checker",
        "desc": "Calculate a domain's age in years, months, and days based on its registration date.",
        "formula": "Date difference scanning",
        "formula_desc": "Finds the difference in days between the user-input creation date and the current date.",
        "icon": "📅",
        "inputs": [
            {"id": "reg-date", "label": "Registration Date:", "type": "date"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Domain Age Audit:", "type": "textarea"}
        ],
        "calc_js": """
            const dateStr = document.getElementById('reg-date').value;
            if (!dateStr) {
                showToast("Please select a registration date.", "error");
                return;
            }
            
            const reg = new Date(dateStr);
            const now = new Date();
            const diff = now - reg;
            
            if (diff < 0) {
                showToast("Registration date cannot be in the future.", "error");
                return;
            }
            
            const days = Math.floor(diff / (1000 * 60 * 60 * 24));
            const years = Math.floor(days / 365);
            const remDays = days % 365;
            
            let report = `Domain Age: ${years} year(s), ${Math.floor(remDays/30)} month(s), ${remDays % 30} day(s)\\n`;
            report += `Total Days Registered: ${days.toLocaleString()} days\\n\\n`;
            if (years > 5) {
                report += "[✔] Trust factor: Domain is established and has a solid history.";
            } else {
                report += "[OK] Brand age: Domain is relatively new. Focus on building solid SEO history.";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Domain age calculated.</p>");
        """
    },
    {
        "category": "Marketing Tools",
        "name": "CTR Calculator",
        "slug": "ctr-calculator",
        "desc": "Calculate the Click-Through Rate (CTR) of your marketing campaigns and organic listings.",
        "formula": "CTR % = (Clicks / Impressions) * 100",
        "formula_desc": "Measures user click interactions relative to total impressions shown.",
        "icon": "📊",
        "inputs": [
            {"id": "ctr-clicks", "label": "Total Clicks:", "type": "number", "default": "450", "min": "0"},
            {"id": "ctr-impr", "label": "Total Impressions:", "type": "number", "default": "10000", "min": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "CTR Calculation:", "type": "textarea"}
        ],
        "calc_js": """
            const clicks = parseFloat(document.getElementById('ctr-clicks').value) || 0;
            const impr = parseFloat(document.getElementById('ctr-impr').value) || 0;
            
            if (impr <= 0) {
                showToast("Impressions must be a positive number.", "error");
                return;
            }
            
            const ctr = (clicks / impr) * 100;
            let report = `Click-Through Rate (CTR): ${ctr.toFixed(2)}%\\n\\n`;
            report += `Clicks: ${clicks.toLocaleString()}\\n`;
            report += `Impressions: ${impr.toLocaleString()}`;
            
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Click-Through Rate calculated as <strong>${ctr.toFixed(2)}%</strong>.</p>`);
        """
    },
    {
        "category": "Marketing Tools",
        "name": "CPM Calculator",
        "slug": "cpm-calculator",
        "desc": "Calculate ad campaign costs per mille (thousand impressions).",
        "formula": "CPM = (Cost / Impressions) * 1000",
        "formula_desc": "Measures marketing spend relative to each block of 1000 visual impressions.",
        "icon": "💰",
        "inputs": [
            {"id": "cpm-cost", "label": "Total Campaign Cost ($):", "type": "number", "default": "150", "min": "0", "step": "0.01"},
            {"id": "cpm-impr", "label": "Impressions Count:", "type": "number", "default": "50000", "min": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "CPM Output Result:", "type": "textarea"}
        ],
        "calc_js": """
            const cost = parseFloat(document.getElementById('cpm-cost').value) || 0;
            const impr = parseFloat(document.getElementById('cpm-impr').value) || 0;
            
            if (impr <= 0) {
                showToast("Impressions must be positive.", "error");
                return;
            }
            
            const cpm = (cost / impr) * 1000;
            let report = `Cost Per Mille (CPM): $${cpm.toFixed(2)}\\n\\n`;
            report += `Total Spend: $${cost.toFixed(2)}\\n`;
            report += `Impressions: ${impr.toLocaleString()}`;
            
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Campaign Cost Per Mille calculated as <strong>$${cpm.toFixed(2)}</strong>.</p>`);
        """
    },
    {
        "category": "Marketing Tools",
        "name": "CPC Calculator",
        "slug": "cpc-calculator",
        "desc": "Calculate the average Cost Per Click (CPC) for pay-per-click ad groups.",
        "formula": "CPC = Total Spend / Clicks",
        "formula_desc": "Calculates campaign cost divided by total click interactions.",
        "icon": "💸",
        "inputs": [
            {"id": "cpc-cost", "label": "Total Spend ($):", "type": "number", "default": "200", "min": "0", "step": "0.01"},
            {"id": "cpc-clicks", "label": "Total Clicks:", "type": "number", "default": "250", "min": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "CPC Output Result:", "type": "textarea"}
        ],
        "calc_js": """
            const cost = parseFloat(document.getElementById('cpc-cost').value) || 0;
            const clicks = parseFloat(document.getElementById('cpc-clicks').value) || 0;
            
            if (clicks <= 0) {
                showToast("Clicks must be greater than zero.", "error");
                return;
            }
            
            const cpc = cost / clicks;
            let report = `Average Cost Per Click (CPC): $${cpc.toFixed(2)}\\n\\n`;
            report += `Total Cost: $${cost.toFixed(2)}\\n`;
            report += `Total Clicks: ${clicks.toLocaleString()}`;
            
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Average CPC calculated as <strong>$${cpc.toFixed(2)}</strong>.</p>`);
        """
    },
    {
        "category": "Marketing Tools",
        "name": "Conversion Rate Calculator",
        "slug": "conversion-rate-calculator",
        "desc": "Calculate campaign conversion rates to measure lead and sales quality.",
        "formula": "Conversion Rate % = (Conversions / Visits) * 100",
        "formula_desc": "Measures goal achievements relative to total landing page visitor counts.",
        "icon": "📈",
        "inputs": [
            {"id": "conv-actions", "label": "Total Conversions:", "type": "number", "default": "35", "min": "0"},
            {"id": "conv-visits", "label": "Total Clicks / Visits:", "type": "number", "default": "1000", "min": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Conversion Rate Output:", "type": "textarea"}
        ],
        "calc_js": """
            const conv = parseFloat(document.getElementById('conv-actions').value) || 0;
            const visits = parseFloat(document.getElementById('conv-visits').value) || 0;
            
            if (visits <= 0) {
                showToast("Visits must be positive.", "error");
                return;
            }
            
            const cr = (conv / visits) * 100;
            let report = `Conversion Rate: ${cr.toFixed(2)}%\\n\\n`;
            report += `Conversions: ${conv.toLocaleString()}\\n`;
            report += `Visits: ${visits.toLocaleString()}`;
            
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Conversion Rate calculated as <strong>${cr.toFixed(2)}%</strong>.</p>`);
        """
    },
    {
        "category": "Marketing Tools",
        "name": "ROI Calculator",
        "slug": "roi-calculator",
        "desc": "Calculate Return on Investment (ROI) percentages for marketing and business budgets.",
        "formula": "ROI % = ((Gain - Cost) / Cost) * 100",
        "formula_desc": "Measures financial returns relative to initial capital costs.",
        "icon": "📊",
        "inputs": [
            {"id": "roi-revenue", "label": "Total Revenue / Gain ($):", "type": "number", "default": "1500", "min": "0", "step": "0.01"},
            {"id": "roi-cost", "label": "Total Investment Cost ($):", "type": "number", "default": "1000", "min": "1", "step": "0.01"}
        ],
        "outputs": [
            {"id": "text-output", "label": "ROI Output Result:", "type": "textarea"}
        ],
        "calc_js": """
            const rev = parseFloat(document.getElementById('roi-revenue').value) || 0;
            const cost = parseFloat(document.getElementById('roi-cost').value) || 0;
            
            if (cost <= 0) {
                showToast("Investment Cost must be greater than zero.", "error");
                return;
            }
            
            const roi = ((rev - cost) / cost) * 100;
            const net = rev - cost;
            
            let report = `Return on Investment (ROI): ${roi.toFixed(2)}%\\n`;
            report += `Net Profit/Loss: $${net.toFixed(2)}\\n\\n`;
            report += `Total Revenue: $${rev.toLocaleString(undefined, {minimumFractionDigits: 2})}\\n`;
            report += `Total Investment: $${cost.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Campaign ROI calculated as <strong>${roi.toFixed(2)}%</strong>.</p>`);
        """
    },
    {
        "category": "Marketing Tools",
        "name": "Marketing Budget Calculator",
        "slug": "marketing-budget-calculator",
        "desc": "Calculate target budget splits across SEO, PPC, and social media channels.",
        "formula": "Strategic marketing weight splits",
        "formula_desc": "Divides marketing budgets (SEO: 40%, PPC: 30%, Social: 20%, Email: 10%) based on industry standards.",
        "icon": "💰",
        "inputs": [
            {"id": "budget-total", "label": "Total Marketing Budget ($):", "type": "number", "default": "5000", "min": "10"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Recommended Budget Splits:", "type": "textarea"}
        ],
        "calc_js": """
            const budget = parseFloat(document.getElementById('budget-total').value) || 0;
            if (budget <= 0) {
                showToast("Please enter a valid budget.", "error");
                return;
            }
            
            const seo = budget * 0.40;
            const ppc = budget * 0.30;
            const social = budget * 0.20;
            const email = budget * 0.10;
            
            let report = `Recommended Channel Spend Allocation:\\n\\n`;
            report += `- Organic SEO (40%): $${seo.toLocaleString()}\\n`;
            report += `- Paid PPC Ads (30%): $${ppc.toLocaleString()}\\n`;
            report += `- Social Media Ads (20%): $${social.toLocaleString()}\\n`;
            report += `- Email Marketing (10%): $${email.toLocaleString()}`;
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Budget allocation computed.</p>");
        """
    },
    {
        "category": "Marketing Tools",
        "name": "Ad Copy Generator",
        "slug": "ad-copy-generator",
        "desc": "Generate Google Ads style search ad headlines and descriptions matching keyword seeds.",
        "formula": "Ad template compounding",
        "formula_desc": "Constructs structured Google search headlines and description lines based on target terms.",
        "icon": "📝",
        "inputs": [
            {"id": "ad-keyword", "label": "Target Keyword:", "type": "text", "default": "Fast JSON Formatter"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Google Search Ad:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('ad-keyword').value.trim();
            if (!kw) {
                showToast("Please enter a target keyword.", "error");
                return;
            }
            
            let ad = `Google Search Ad Blueprint:\\n\\n`;
            ad += `Headline 1: ${kw} Online\\n`;
            ad += `Headline 2: Free, Fast & 100% Private\\n`;
            ad += `Headline 3: Enginewheels Web Tools\\n\\n`;
            ad += `Description 1: Format and optimize ${kw} snippets instantly in your browser tab. Safe and secure client-side tools.\\n`;
            ad += `Description 2: No installation required. Ad-free webmaster utilities for developers. Try it free today!`;
            
            document.getElementById('text-output').value = ad;
            updateBreakdown("<p class='text-success'>Google Ad copy generated.</p>");
        """
    },
    {
        "category": "Marketing Tools",
        "name": "Call-To-Action Generator",
        "slug": "call-to-action-generator",
        "desc": "Generate high-converting Call-To-Action button copy and hooks.",
        "formula": "Persuasive verb mapping",
        "formula_desc": "Combines action verbs (e.g. Try, Start, Download, Get) with value propositions to generate marketing hooks.",
        "icon": "⚡",
        "inputs": [
            {"id": "cta-offer", "label": "Offer / Benefit Name:", "type": "text", "default": "Free SEO Tools"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated CTA Options:", "type": "textarea"}
        ],
        "calc_js": """
            const offer = document.getElementById('cta-offer').value.trim();
            if (!offer) {
                showToast("Please enter an offer name.", "error");
                return;
            }
            
            const list = [
                `Start Using ${offer} Now (No Sign-Up Required)`,
                `Try ${offer} Free Today`,
                `Get Access to ${offer} Instantly`,
                `Optimize Your Site with ${offer}`,
                `Claim Your ${offer} Account`
            ];
            
            document.getElementById('text-output').value = list.join("\\n");
            updateBreakdown("<p class='text-success'>Call-To-Action options generated.</p>");
        """
    },
    {
        "category": "Marketing Tools",
        "name": "Landing Page Headline Generator",
        "slug": "landing-page-headline-generator",
        "desc": "Generate landing page headlines based on product benefits and target audiences.",
        "formula": "Value proposition template layout",
        "formula_desc": "Fills in headline templates with benefits, target audiences, and product details.",
        "icon": "📝",
        "inputs": [
            {"id": "lp-prod", "label": "Product Name:", "type": "text", "default": "Enginewheels Web Tools"},
            {"id": "lp-benefit", "label": "Core Benefit:", "type": "text", "default": "optimize page metadata in a single click"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Headlines:", "type": "textarea"}
        ],
        "calc_js": """
            const prod = document.getElementById('lp-prod').value.trim();
            const benefit = document.getElementById('lp-benefit').value.trim();
            
            if (!prod || !benefit) {
                showToast("Please provide both Product and Benefit.", "error");
                return;
            }
            
            const headlines = [
                `The Smart Way to ${benefit} with ${prod}`,
                `Scale Your Organic Reach: How ${prod} Helps You ${benefit}`,
                `Stop Wasting Time: Use ${prod} to ${benefit} Instantly`,
                `Build Better Web layouts and ${benefit} with ${prod}`
            ];
            
            document.getElementById('text-output').value = headlines.join("\\n\\n");
            updateBreakdown("<p class='text-success'>Landing page headlines compiled.</p>");
        """
    },
    {
        "category": "Marketing Tools",
        "name": "Campaign Name Generator",
        "slug": "campaign-name-generator",
        "desc": "Generate clean marketing campaign name tokens matching standard parameters.",
        "formula": "Parameter serialization joining",
        "formula_desc": "Groups advertising variables (source, type, promotional tags, dates) into formatted string identifiers.",
        "icon": "⚙️",
        "inputs": [
            {"id": "cp-channel", "label": "Marketing Channel (e.g. email, ppc):", "type": "text", "default": "ppc"},
            {"id": "cp-promo", "label": "Promo / Tag (e.g. promo10):", "type": "text", "default": "meta_launch"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Campaign Name:", "type": "textarea"}
        ],
        "calc_js": """
            const chan = document.getElementById('cp-channel').value.trim().toLowerCase().replace(/\\s+/g, "_");
            const promo = document.getElementById('cp-promo').value.trim().toLowerCase().replace(/\\s+/g, "_");
            
            if (!chan || !promo) {
                showToast("Please provide channel and promo details.", "error");
                return;
            }
            
            const date = new Date().toISOString().split('T')[0].replace(/-/g, "");
            const name = `${date}_${chan}_${promo}`;
            
            document.getElementById('text-output').value = name;
            updateBreakdown("<p class='text-success'>Campaign name token generated.</p>");
        """
    }
]

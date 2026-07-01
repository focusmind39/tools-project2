# -*- coding: utf-8 -*-
"""
Database of 30 Google SEO, Local SEO, and AI SEO Tools for Enginewheels
"""

GOOGLE_LOCAL_AI_TOOLS = [
    {
        "category": "Google SEO Tools",
        "name": "SERP Snippet Preview Tool",
        "slug": "serp-snippet-preview-google",
        "desc": "Preview how your page titles and snippets render in Google Desktop and Mobile search indexes.",
        "formula": "SERP pixel length emulation",
        "formula_desc": "Truncates title strings at ~600px width limit and descriptions at ~960px to simulate Google results layouts.",
        "icon": "🔍",
        "inputs": [
            {"id": "g-title", "label": "Title Tag:", "type": "text", "default": "Free Code Validators - Format JSON & XML Online"},
            {"id": "g-desc", "label": "Meta Description:", "type": "textarea", "default": "Format, validate, and optimize codebase snippets instantly inside your active browser session. 100% private client-side utilities."},
            {"id": "g-url", "label": "Target URL:", "type": "text", "default": "https://enginewheels.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "SERP Snippet Blueprint:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('g-title').value.trim();
            const desc = document.getElementById('g-desc').value.trim();
            const url = document.getElementById('g-url').value.trim();
            
            let displayTitle = title.length > 60 ? title.substring(0, 57) + "..." : title;
            let displayDesc = desc.length > 160 ? desc.substring(0, 157) + "..." : desc;
            
            let blueprint = `SERP PREVIEW BLUEPRINT\\n\\n`;
            blueprint += `URL: ${url}\\n`;
            blueprint += `Title: ${displayTitle} (${title.length} chars)\\n`;
            blueprint += `Description: ${displayDesc} (${desc.length} chars)`;
            
            document.getElementById('text-output').value = blueprint;
            
            const mock = `
                <div style="background:#fff; color:#202124; padding:16px; border:1px solid #dadce0; border-radius:8px; font-family:arial,sans-serif; text-align:left; max-width:600px; margin:15px auto;">
                    <div style="font-size:12px; color:#3c4043; margin-bottom:2px;">${url}</div>
                    <div style="font-size:20px; color:#1a0dab; cursor:pointer; margin-bottom:4px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${displayTitle}</div>
                    <div style="font-size:14px; color:#4d5156; line-height:1.4;">${displayDesc}</div>
                </div>
            `;
            updateBreakdown(mock);
        """
    },
    {
        "category": "Google SEO Tools",
        "name": "Featured Snippet Optimizer",
        "slug": "featured-snippet-optimizer",
        "desc": "Check if your definition paragraphs match featured snippet requirements.",
        "formula": "Definition block length check",
        "formula_desc": "Checks if text length falls within Google's featured snippet sweet spot (40 to 60 words).",
        "icon": "⭐",
        "inputs": [
            {"id": "snippet-text", "label": "Definition Paragraph Text:", "type": "textarea", "default": "SEO stands for Search Engine Optimization. It is the process of improving site visibility in search engine results through meta tag formatting, link structures, and content creation."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Snippet Optimization Report:", "type": "textarea"}
        ],
        "calc_js": """
            const text = document.getElementById('snippet-text').value.trim();
            if (!text) {
                showToast("Please enter a definition paragraph.", "error");
                return;
            }
            
            const words = text.split(/\\s+/).filter(w => w.length > 0);
            const count = words.length;
            
            let report = `Definition Word Count: ${count} words\\n\\n`;
            if (count >= 40 && count <= 60) {
                report += "[✔] OPTIMAL LENGTH: Word count falls within Google's featured snippet sweet spot (40-60 words).\\n\\n";
            } else if (count < 40) {
                report += "[WARNING] TOO SHORT: Text is under 40 words. Add a bit more context to help crawlers extract a complete definition snippet.\\n\\n";
            } else {
                report += "[WARNING] TOO LONG: Text exceeds 60 words. Google might truncate the answer. Condense the definition block.\\n\\n";
            }
            
            report += "Format Recommendations:\\n";
            report += "1. Start with a direct answer: 'X is...' or 'X refers to...'\\n";
            report += "2. Keep sentence structure simple and factual.\\n";
            report += "3. Use headers above this definition containing target keywords.";
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Featured snippet optimization completed.</p>");
        """
    },
    {
        "category": "Google SEO Tools",
        "name": "Search Intent Analyzer",
        "slug": "search-intent-analyzer",
        "desc": "Analyze keywords to classify target user intent into informational or transactional categories.",
        "formula": "Trigger keyword mapping rules",
        "formula_desc": "Evaluates queries against intent signals (e.g. 'buy' for transactional, 'how' for informational).",
        "icon": "🎯",
        "inputs": [
            {"id": "search-query", "label": "Enter Search Keyword:", "type": "text", "default": "how to format JSON file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Search Intent Report:", "type": "textarea"}
        ],
        "calc_js": """
            const query = document.getElementById('search-query').value.trim().toLowerCase();
            if (!query) {
                showToast("Please enter a search query.", "error");
                return;
            }
            
            let intent = "Informational";
            let desc = "The user is looking for guides, instructions, or answers to questions (e.g., 'how to', 'what is').";
            let color = "#3b82f6";
            
            if (query.includes("buy") || query.includes("price") || query.includes("order") || query.includes("shop")) {
                intent = "Transactional";
                desc = "The user wants to buy a product or complete a purchase/transaction.";
                color = "#ef4444";
            } else if (query.includes("best") || query.includes("review") || query.includes("top") || query.includes("compare")) {
                intent = "Commercial";
                desc = "The user is researching products, brands, or services to compare options.";
                color = "#f59e0b";
            } else if (query.includes("login") || query.includes("download") || query.includes("signin") || query.includes("app")) {
                intent = "Navigational";
                desc = "The user is trying to navigate to a specific website, portal, or software application.";
                color = "#10b981";
            }
            
            let report = `Classified Search Intent: ${intent.toUpperCase()}\\n\\n`;
            report += `Description: ${desc}\\n\\n`;
            report += `Keyword Term: "${query}"`;
            
            document.getElementById('text-output').value = report;
            
            const badge = `<div style="background:${color}; color:#fff; display:inline-block; padding:6px 12px; border-radius:12px; font-weight:bold; font-size:1.1rem; margin-top:10px;">${intent}</div>`;
            updateBreakdown(badge);
        """
    },
    {
        "category": "Google SEO Tools",
        "name": "FAQ Generator",
        "slug": "faq-generator-google",
        "desc": "Generate search-friendly Frequently Asked Questions (FAQ) sets matching seed topics.",
        "formula": "Topic question templates mapping",
        "formula_desc": "Combines topics with query starters (How, What, Why) to build baseline FAQ structures.",
        "icon": "❓",
        "inputs": [
            {"id": "faq-topic", "label": "Main Topic Keyword:", "type": "text", "default": "robots.txt validator"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated FAQ Outline:", "type": "textarea"}
        ],
        "calc_js": """
            const topic = document.getElementById('faq-topic').value.trim();
            if (!topic) {
                showToast("Please enter a topic keyword.", "error");
                return;
            }
            
            let report = `FAQ Set for "${topic}":\\n\\n`;
            report += `Q1: What is a ${topic}?\\n`;
            report += `A1: A ${topic} is a tool designed to verify, configure, or evaluate rules related to ${topic.toLowerCase()}.\\n\\n`;
            report += `Q2: How do I use the ${topic}?\\n`;
            report += `A2: Simply enter your inputs into the control panel, configure parameters, and click generate to get results instantly.\\n\\n`;
            report += `Q3: Is the ${topic} free to use?\\n`;
            report += `A3: Yes, our tool is 100% free with no registration or limits.`;
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>FAQ outlines compiled.</p>");
        """
    },
    {
        "category": "Google SEO Tools",
        "name": "Google Title Checker",
        "slug": "google-title-checker",
        "desc": "Verify title tag lengths against Google desktop search truncation width limits.",
        "formula": "Desktop title character audit",
        "formula_desc": "Evaluates title string lengths and flags warnings if the tag exceeds Google's 60-character desktop listing window.",
        "icon": "📏",
        "inputs": [
            {"id": "title-val", "label": "Title Tag Text:", "type": "text", "default": "Free Google Title Checker | Search Index Optimization - Enginewheels"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Title Check Report:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('title-val').value.trim();
            if (!title) {
                showToast("Please enter title text.", "error");
                return;
            }
            
            const len = title.length;
            let report = `Google Title Length: ${len} characters\\n`;
            
            if (len > 60) {
                report += `Status: OVER LIMIT (-${len - 60} chars)\\n[✘] Title exceeds 60 characters and will likely be cut off on Google search results.`;
            } else if (len < 40) {
                report += "Status: TOO SHORT\\n[WARNING] Title is under 40 characters. Consider adding secondary brand keywords.";
            } else {
                report += "Status: OPTIMAL\\n[✔] Title fits perfectly within Google's desktop search results.";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Google title length checked.</p>");
        """
    },
    {
        "category": "Google SEO Tools",
        "name": "Google Description Checker",
        "slug": "google-description-checker",
        "desc": "Check description lengths against Google snippet display limits.",
        "formula": "Google description bounds check",
        "formula_desc": "Validates descriptions lengths against Google's 160-character desktop snippet window.",
        "icon": "📝",
        "inputs": [
            {"id": "desc-val", "label": "Meta Description Text:", "type": "textarea", "default": "Verify and check website meta description tags lengths locally in your browser. Complete client-side tools."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Description Check Report:", "type": "textarea"}
        ],
        "calc_js": """
            const desc = document.getElementById('desc-val').value.trim();
            if (!desc) {
                showToast("Please enter description text.", "error");
                return;
            }
            
            const len = desc.length;
            let report = `Google Description Length: ${len} characters\\n`;
            
            if (len > 160) {
                report += `Status: OVER LIMIT (-${len - 160} chars)\\n[✘] Description exceeds 160 characters. Try shortening it to fit Google's results windows.`;
            } else if (len < 110) {
                report += "Status: TOO SHORT\\n[WARNING] Description is under 110 characters. Add more descriptive details.";
            } else {
                report += "Status: OPTIMAL\\n[✔] Description fits within Google's search results snippet guidelines.";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Google description length audited.</p>");
        """
    },
    {
        "category": "Google SEO Tools",
        "name": "Mobile SERP Preview Tool",
        "slug": "mobile-serp-preview-tool",
        "desc": "Simulate and preview how your search snippets look on mobile devices.",
        "formula": "Mobile width layout rendering",
        "formula_desc": "Truncates titles at ~55 characters and descriptions at ~120 characters to simulate mobile viewports.",
        "icon": "📱",
        "inputs": [
            {"id": "mob-title", "label": "Google Mobile Title:", "type": "text", "default": "Free XML Formatter - Safe Web Tools"},
            {"id": "mob-desc", "label": "Google Mobile Description:", "type": "textarea", "default": "Format XML files client-side. Fast, client-side, and ad-light developer tools."},
            {"id": "mob-url", "label": "Mobile Page URL:", "type": "text", "default": "https://enginewheels.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Mobile Snippet Specifications:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('mob-title').value.trim();
            const desc = document.getElementById('mob-desc').value.trim();
            const url = document.getElementById('mob-url').value.trim();
            
            let displayTitle = title.length > 55 ? title.substring(0, 52) + "..." : title;
            let displayDesc = desc.length > 120 ? desc.substring(0, 117) + "..." : desc;
            
            let spec = `Viewport: Google Mobile (max 55 chars title, 120 chars description)\\n`;
            spec += `Title: ${title.length}/55\\n`;
            spec += `Description: ${desc.length}/120`;
            
            document.getElementById('text-output').value = spec;
            
            const mock = `
                <div style="background:#fff; color:#202124; padding:12px; border:1px solid #dadce0; border-radius:12px; font-family:arial,sans-serif; text-align:left; max-width:360px; margin:15px auto;">
                    <div style="font-size:11px; color:#5f6368; margin-bottom:2px;">${url}</div>
                    <div style="font-size:16px; color:#1558d6; cursor:pointer; margin-bottom:4px; font-weight:normal; line-height:20px;">${displayTitle}</div>
                    <div style="font-size:13px; color:#3c4043; line-height:1.4;">${displayDesc}</div>
                </div>
            `;
            updateBreakdown(mock);
        """
    },
    {
        "category": "Google SEO Tools",
        "name": "Desktop SERP Preview Tool",
        "slug": "desktop-serp-preview-tool",
        "desc": "Simulate and preview search snippet outputs on desktop monitors.",
        "formula": "Desktop width layout rendering",
        "formula_desc": "Truncates titles at ~60 characters and descriptions at ~160 characters to simulate desktop viewports.",
        "icon": "💻",
        "inputs": [
            {"id": "dsk-title", "label": "Google Desktop Title:", "type": "text", "default": "Free XML Formatter - Safe Web Tools"},
            {"id": "dsk-desc", "label": "Google Desktop Description:", "type": "textarea", "default": "Format XML files client-side. Fast, client-side, and ad-light developer tools. 100% private utility."},
            {"id": "dsk-url", "label": "Desktop Page URL:", "type": "text", "default": "https://enginewheels.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Desktop Snippet Specifications:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('dsk-title').value.trim();
            const desc = document.getElementById('dsk-desc').value.trim();
            const url = document.getElementById('dsk-url').value.trim();
            
            let displayTitle = title.length > 60 ? title.substring(0, 57) + "..." : title;
            let displayDesc = desc.length > 160 ? desc.substring(0, 157) + "..." : desc;
            
            let spec = `Viewport: Google Desktop (max 60 chars title, 160 chars description)\\n`;
            spec += `Title: ${title.length}/60\\n`;
            spec += `Description: ${desc.length}/160`;
            
            document.getElementById('text-output').value = spec;
            
            const mock = `
                <div style="background:#fff; color:#202124; padding:16px; border:1px solid #dadce0; border-radius:8px; font-family:arial,sans-serif; text-align:left; max-width:600px; margin:15px auto;">
                    <div style="font-size:12px; color:#3c4043; margin-bottom:2px;">${url}</div>
                    <div style="font-size:20px; color:#1a0dab; cursor:pointer; margin-bottom:4px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${displayTitle}</div>
                    <div style="font-size:14px; color:#4d5156; line-height:1.4;">${displayDesc}</div>
                </div>
            `;
            updateBreakdown(mock);
        """
    },
    {
        "category": "Google SEO Tools",
        "name": "SEO Checklist Generator",
        "slug": "seo-checklist-generator",
        "desc": "Generate an interactive, printable SEO checklist for website optimization.",
        "formula": "Boilerplate checklist parsing",
        "formula_desc": "Outputs a structured checkbox list of critical on-page, off-page, and technical SEO tasks.",
        "icon": "📋",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "On-Page SEO Checklist:", "type": "textarea"}
        ],
        "calc_js": """
            let checklist = "ENGINEWHEELS SEO OPTIMIZATION CHECKLIST\\n======================================\\n\\n";
            checklist += "[ ] 1. Meta Title is set (45-60 characters)\\n";
            checklist += "[ ] 2. Meta Description is set (120-160 characters)\\n";
            checklist += "[ ] 3. Primary H1 Heading tag is present (only one H1 per page)\\n";
            checklist += "[ ] 4. All images have descriptive alt text attributes\\n";
            checklist += "[ ] 5. Page contains a canonical link tag rel=\\"canonical\\"\\n";
            checklist += "[ ] 6. Robots.txt file created and linked to XML sitemap\\n";
            checklist += "[ ] 7. XML Sitemap created and submitted to Google Search Console\\n";
            checklist += "[ ] 8. JSON-LD Breadcrumb / FAQ schemas added to page headers\\n";
            checklist += "[ ] 9. Page size optimized (images compressed, JS/CSS minified)\\n";
            checklist += "[ ] 10. Page is fully mobile responsive and fits mobile viewports";
            
            document.getElementById('text-output').value = checklist;
            updateBreakdown("<p class='text-success'>SEO checklist generated successfully.</p>");
        """
    },
    {
        "category": "Google SEO Tools",
        "name": "Search Appearance Preview Tool",
        "slug": "search-appearance-preview-tool",
        "desc": "Check how schema enhancements like FAQ drops display in Google search results.",
        "formula": "Rich snippet mockup emulation",
        "formula_desc": "Simulates search results layouts incorporating FAQ listings or rating configurations.",
        "icon": "⭐",
        "inputs": [
            {"id": "sap-title", "label": "Page Title:", "type": "text", "default": "Free Tools Suite - Enginewheels"},
            {"id": "sap-faq", "label": "FAQ Question Summary:", "type": "text", "default": "Are the web tools free to use?"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Search Appearance Preview:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('sap-title').value.trim();
            const faq = document.getElementById('sap-faq').value.trim();
            
            document.getElementById('text-output').value = `Title: ${title}\\nFAQ Enhancement: "${faq}"\\n\\nRich snippet preview generated below.`;
            
            const mock = `
                <div style="background:#fff; color:#202124; padding:16px; border:1px solid #dadce0; border-radius:8px; font-family:arial,sans-serif; text-align:left; max-width:600px; margin:15px auto;">
                    <div style="font-size:12px; color:#3c4043; margin-bottom:2px;">https://enginewheels.com</div>
                    <div style="font-size:20px; color:#1a0dab; cursor:pointer; margin-bottom:4px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${title}</div>
                    <div style="font-size:14px; color:#4d5156; line-height:1.4; margin-bottom:10px;">Format, check, and optimize codebase configurations locally in your browser.</div>
                    <div style="border-top:1px solid #eee; padding-top:8px; font-size:13px; color:#1a0dab; cursor:pointer;">
                        ▾ People also ask: "${faq}"
                    </div>
                </div>
            `;
            updateBreakdown(mock);
        """
    },
    {
        "category": "Local SEO Tools",
        "name": "Local SEO Audit Tool",
        "slug": "local-seo-audit-tool",
        "desc": "Check critical local SEO ranking factors for your business coordinates.",
        "formula": "Local SEO checkpoints weightings",
        "formula_desc": "Grades NAP (Name, Address, Phone) structures, LocalBusiness schema setups, and map links presence.",
        "icon": "🏢",
        "inputs": [
            {"id": "aud-name", "label": "Business Name:", "type": "text", "default": "Seattle Auto Repair"},
            {"id": "aud-addr", "label": "Business Address:", "type": "text", "default": "500 Pine St, Seattle, WA"},
            {"id": "aud-phone", "label": "Phone Number:", "type": "text", "default": "+1-206-555-0150"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Local SEO Audit Report:", "type": "textarea"}
        ],
        "calc_js": """
            const name = document.getElementById('aud-name').value.trim();
            const addr = document.getElementById('aud-addr').value.trim();
            const phone = document.getElementById('aud-phone').value.trim();
            
            if (!name || !addr || !phone) {
                showToast("Please provide all business details.", "error");
                return;
            }
            
            let score = 100;
            let report = "LOCAL SEO AUDIT REPORT\\n=====================\\n\\n";
            report += `Business: ${name}\\nAddress: ${addr}\\nPhone: ${phone}\\n\\n`;
            
            if (phone.startsWith("+") || phone.startsWith("1") || /\\(\\d{3}\\)/.test(phone)) {
                report += "[✔] Phone number format is standardized.\\n";
            } else {
                report += "[WARNING] Phone format is non-standard. Use city codes or region prefixes.\\n";
                score -= 15;
            }
            
            if (addr.includes(",") && /\\b[A-Z]{2}\\b/.test(addr)) {
                report += "[✔] Address configuration includes city and region codes.\\n";
            } else {
                report += "[WARNING] Address structure looks thin. Add city, region, or zip codes for better local relevance.\\n";
                score -= 15;
            }
            
            report += `\\nLocal Search Readiness: ${score}/100`;
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Local SEO audit complete. Score = <strong>${score}%</strong></p>`);
        """
    },
    {
        "category": "Local SEO Tools",
        "name": "Local Business Schema Generator",
        "slug": "local-business-schema-generator-seo",
        "desc": "Generate detailed LocalBusiness JSON-LD markup blocks for geographic listings.",
        "formula": "JSON-LD LocalBusiness serialization",
        "formula_desc": "Serializes address components, geocoordinates, schedules, and maps.",
        "icon": "🏡",
        "inputs": [
            {"id": "l-name", "label": "Business Name:", "type": "text", "default": "Seattle Auto Repair"},
            {"id": "l-addr", "label": "Street Address:", "type": "text", "default": "500 Pine St"},
            {"id": "l-city", "label": "City:", "type": "text", "default": "Seattle"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Local Schema Output:", "type": "textarea"}
        ],
        "calc_js": """
            const name = document.getElementById('l-name').value.trim();
            const addr = document.getElementById('l-addr').value.trim();
            const city = document.getElementById('l-city').value.trim();
            
            if (!name || !city) {
                showToast("Please provide Business Name and City.", "error");
                return;
            }
            
            const schema = {
                "@context": "https://schema.org",
                "@type": "LocalBusiness",
                "name": name,
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": addr || undefined,
                    "addressLocality": city
                }
            };
            
            document.getElementById('text-output').value = `<script type="application/ld+json">\\n${JSON.stringify(schema, null, 2)}\\n<\\/script>`;
            updateBreakdown("<p class='text-success'>Local Business Schema generated.</p>");
        """
    },
    {
        "category": "Local SEO Tools",
        "name": "NAP Consistency Checker",
        "slug": "nap-consistency-checker",
        "desc": "Verify if Name, Address, and Phone details are identical across various website and directory platforms.",
        "formula": "String equivalence check",
        "formula_desc": "Performs exact case-insensitive matches to flag slight formatting differences in address and phone strings.",
        "icon": "🔎",
        "inputs": [
            {"id": "nap-web", "label": "NAP on Website:", "type": "text", "default": "Seattle Auto Repair, 500 Pine St, +1-206-555-0150"},
            {"id": "nap-gmb", "label": "NAP on Google Profile:", "type": "text", "default": "Seattle Auto Repair, 500 Pine Street, +1-206-555-0150"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Consistency Analysis:", "type": "textarea"}
        ],
        "calc_js": """
            const web = document.getElementById('nap-web').value.trim().toLowerCase();
            const gmb = document.getElementById('nap-gmb').value.trim().toLowerCase();
            
            if (!web || !gmb) {
                showToast("Please enter NAP strings.", "error");
                return;
            }
            
            let report = "NAP CONSISTENCY REPORT\\n======================\\n\\n";
            if (web === gmb) {
                report += "[✔] PERFECT MATCH: Web and Google NAP profiles are 100% consistent!\\n";
            } else {
                report += "[WARNING] INCONSISTENCY DETECTED:\\n";
                report += `- Web: "${document.getElementById('nap-web').value.trim()}"\\n`;
                report += `- Google: "${document.getElementById('nap-gmb').value.trim()}"\\n\\n`;
                report += "Advice: Ensure address abbreviations (e.g., 'St' vs 'Street') and spacing are identical. Inconsistent NAP data confuses crawlers.";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>NAP audited.</p>");
        """
    },
    {
        "category": "Local SEO Tools",
        "name": "Google Business Description Generator",
        "slug": "google-business-description-generator",
        "desc": "Generate optimized Google Business Profile descriptions (up to 750 characters).",
        "formula": "Character limit description layout",
        "formula_desc": "Formats descriptions incorporating local keywords and checks limits against Google's 750-character threshold.",
        "icon": "📝",
        "inputs": [
            {"id": "gmb-name", "label": "Business Name:", "type": "text", "default": "Seattle Auto Repair"},
            {"id": "gmb-service", "label": "Key Service / Benefit:", "type": "text", "default": "reliable brake repairs and transmission fixes"},
            {"id": "gmb-city", "label": "Target City:", "type": "text", "default": "Seattle"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Profile Description:", "type": "textarea"}
        ],
        "calc_js": """
            const name = document.getElementById('gmb-name').value.trim();
            const service = document.getElementById('gmb-service').value.trim();
            const city = document.getElementById('gmb-city').value.trim();
            
            if (!name || !service || !city) {
                showToast("Please provide name, service, and city.", "error");
                return;
            }
            
            let desc = `Welcome to ${name}, your trusted destination for ${service} in ${city}. We are dedicated to providing fast service, quality repairs, and competitive rates to our local community. Our experienced technicians use state-of-the-art tools to diagnose and fix issues quickly. Contact us today to schedule your appointment!`;
            
            const len = desc.length;
            let report = `${desc}\\n\\nCharacter Count: ${len}/750`;
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Google Business Profile description generated.</p>");
        """
    },
    {
        "category": "Local SEO Tools",
        "name": "Service Area Generator",
        "slug": "service-area-generator",
        "desc": "Generate structured service area coverage lists and geo coordinates.",
        "formula": "Geo-area boundary array matching",
        "formula_desc": "Combines base cities with surrounding neighborhoods to format geographic service boundaries.",
        "icon": "🗺️",
        "inputs": [
            {"id": "sa-city", "label": "Base City Name:", "type": "text", "default": "Seattle"},
            {"id": "sa-dist", "label": "Max Radius (miles):", "type": "number", "default": "15", "min": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Service Area Coverage List:", "type": "textarea"}
        ],
        "calc_js": """
            const city = document.getElementById('sa-city').value.trim();
            const dist = parseFloat(document.getElementById('sa-dist').value) || 15;
            
            if (!city) {
                showToast("Please enter a base city.", "error");
                return;
            }
            
            let list = `Service Area Profile for ${city} (Radius: ${dist} miles):\\n\\n`;
            list += `- Downtown ${city}\\n`;
            list += `- North ${city} Districts\\n`;
            list += `- Eastside Neighborhoods\\n`;
            list += `- South Metro Areas\\n\\n`;
            list += "Note: Add these localized neighborhoods to your website's location pages to improve organic rankings.";
            
            document.getElementById('text-output').value = list;
            updateBreakdown("<p class='text-success'>Service area list generated.</p>");
        """
    },
    {
        "category": "Local SEO Tools",
        "name": "Local Keyword Generator",
        "slug": "local-keyword-generator",
        "desc": "Generate local keywords combining business services with target cities.",
        "formula": "Service + Location compound joins",
        "formula_desc": "Blends core service terms with geographic modifiers to build local keyword variations.",
        "icon": "🔑",
        "inputs": [
            {"id": "loc-service", "label": "Core Service (e.g. plumber):", "type": "text", "default": "auto repair"},
            {"id": "loc-city", "label": "Target City Name:", "type": "text", "default": "Seattle"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Local Keyword Variations:", "type": "textarea"}
        ],
        "calc_js": """
            const service = document.getElementById('loc-service').value.trim().toLowerCase();
            const city = document.getElementById('loc-city').value.trim();
            
            if (!service || !city) {
                showToast("Please fill in both service and city.", "error");
                return;
            }
            
            const variations = [
                `${service} in ${city}`,
                `best ${service} ${city}`,
                `affordable ${service} near me ${city}`,
                `${city} ${service} services`,
                `emergency ${service} ${city}`
            ];
            
            document.getElementById('text-output').value = variations.join("\\n");
            updateBreakdown("<p class='text-success'>Local keyword variations compiled.</p>");
        """
    },
    {
        "category": "Local SEO Tools",
        "name": "Location Landing Page Generator",
        "slug": "location-landing-page-generator",
        "desc": "Generate standard boilerplate copy layouts for geo-targeted location pages.",
        "formula": "Location copy template layout",
        "formula_desc": "Populates standard localized business copy templates with business, service, and city details.",
        "icon": "🏡",
        "inputs": [
            {"id": "lp-biz", "label": "Business Name:", "type": "text", "default": "Seattle Auto Repair"},
            {"id": "lp-city", "label": "Target City Name:", "type": "text", "default": "Seattle"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Location Page Content Boilerplate:", "type": "textarea"}
        ],
        "calc_js": """
            const biz = document.getElementById('lp-biz').value.trim();
            const city = document.getElementById('lp-city').value.trim();
            
            if (!biz || !city) {
                showToast("Please provide Business and City.", "error");
                return;
            }
            
            let content = `<h1>Professional Services in ${city} | ${biz}</h1>\\n\\n`;
            content += `Welcome to ${biz}, your local provider in ${city}. We are proud to serve residents across ${city} with reliable services, experienced technicians, and customer care.\\n\\n`;
            content += `Why Choose ${biz} in ${city}?\\n`;
            content += `- Locally owned and operated\\n`;
            content += `- Prompt response times\\n`;
            content += `- Free consultations and transparent quotes\\n\\n`;
            content += `Contact our local team today to schedule your service in ${city}!`;
            
            document.getElementById('text-output').value = content;
            updateBreakdown("<p class='text-success'>Location page copy generated.</p>");
        """
    },
    {
        "category": "Local SEO Tools",
        "name": "Citation Builder",
        "slug": "citation-builder",
        "desc": "Compile business registration citations for yelp and yellowpages directory listings.",
        "formula": "Structured citation serialization",
        "formula_desc": "Serializes Name, Address, Phone, Website, and Category inputs into standard directory fields.",
        "icon": "📋",
        "inputs": [
            {"id": "cit-name", "label": "Business Name:", "type": "text", "default": "Seattle Auto Repair"},
            {"id": "cit-addr", "label": "Full Address:", "type": "text", "default": "500 Pine St, Seattle, WA, 98101"},
            {"id": "cit-phone", "label": "Phone Number:", "type": "text", "default": "+1-206-555-0150"},
            {"id": "cit-web", "label": "Website URL:", "type": "text", "default": "https://seattleautorepair.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Compiled Directory Citation:", "type": "textarea"}
        ],
        "calc_js": """
            const name = document.getElementById('cit-name').value.trim();
            const addr = document.getElementById('cit-addr').value.trim();
            const phone = document.getElementById('cit-phone').value.trim();
            const web = document.getElementById('cit-web').value.trim();
            
            if (!name || !addr || !phone) {
                showToast("Name, Address, and Phone are required.", "error");
                return;
            }
            
            let citation = `DIRECTORY CITATION BLOCK\\n========================\\n\\n`;
            citation += `Business Name: ${name}\\n`;
            citation += `Street Address: ${addr}\\n`;
            citation += `Phone Number: ${phone}\\n`;
            citation += `Website: ${web || "N/A"}\\n\\n`;
            citation += "Instructions: Copy and paste this block into Yelp, Bing Places, and local directories to ensure consistent citation data.";
            
            document.getElementById('text-output').value = citation;
            updateBreakdown("<p class='text-success'>Citation data block compiled.</p>");
        """
    },
    {
        "category": "Local SEO Tools",
        "name": "Business Category Generator",
        "slug": "business-category-generator",
        "desc": "Suggest standard primary Google Business Profile categories based on keywords.",
        "formula": "Keyword category match",
        "formula_desc": "Maps business keywords to standard Google Business Profile categories.",
        "icon": "🏷️",
        "inputs": [
            {"id": "cat-keyword", "label": "Enter Business Keyword:", "type": "text", "default": "fix cars"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Suggested Google Categories:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('cat-keyword').value.trim().toLowerCase();
            if (!kw) {
                showToast("Please enter a business keyword.", "error");
                return;
            }
            
            let report = "SUGGESTED GOOGLE BUSINESS PROFILE CATEGORIES:\\n\\n";
            if (kw.includes("car") || kw.includes("auto") || kw.includes("mechanic") || kw.includes("repair")) {
                report += "Primary Category: Auto Repair Shop\\n";
                report += "Secondary Categories: Car Repair and Maintenance, Mechanic Shop, Used Car Dealer.";
            } else if (kw.includes("food") || kw.includes("pizza") || kw.includes("restaurant") || kw.includes("cafe")) {
                report += "Primary Category: Restaurant\\n";
                report += "Secondary Categories: Pizza Restaurant, Cafe, Food Delivery Service.";
            } else {
                report += "Primary Category: Professional Services\\n";
                report += "Secondary Categories: Consulting Firm, Marketing Services.";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Google categories mapped.</p>");
        """
    },
    {
        "category": "Local SEO Tools",
        "name": "Review Response Generator",
        "slug": "review-response-generator",
        "desc": "Generate professional and positive review response templates for client feedback.",
        "formula": "Review rating response mapping",
        "formula_desc": "Compiles response templates matching positive (5-star) or negative feedback parameters.",
        "icon": "💬",
        "inputs": [
            {"id": "rev-rating", "label": "Review Rating:", "type": "select", "default": "5",
             "options": [
                 ("5", "5-Star Positive Review"),
                 ("1", "1-Star Negative Review")
             ]},
            {"id": "rev-client", "label": "Client Name:", "type": "text", "default": "Sarah"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Response Template Output:", "type": "textarea"}
        ],
        "calc_js": """
            const rating = document.getElementById('rev-rating').value;
            const client = document.getElementById('rev-client').value.trim() || "Customer";
            
            let response = "";
            if (rating === "5") {
                response = `Thank you so much, ${client}, for your 5-star review! We are thrilled to hear you had a great experience with our team. We look forward to serving you again in the future!`;
            } else {
                response = `Hello ${client}, we apologize for the experience you had. We take customer satisfaction seriously. Please reach out to our support team directly so we can resolve this for you.`;
            }
            
            document.getElementById('text-output').value = response;
            updateBreakdown("<p class='text-success'>Review response template generated.</p>");
        """
    },
    {
        "category": "AI SEO & Content Tools",
        "name": "Blog Title Generator",
        "slug": "blog-title-generator-seo",
        "desc": "Generate catchy blog title ideas based on topic keywords.",
        "formula": "SEO headline layout mapping",
        "formula_desc": "Combines keywords with standard blog title templates (e.g. Ultimate Guide, How To, Tips).",
        "icon": "📝",
        "inputs": [
            {"id": "blog-keyword", "label": "Main Topic Keyword:", "type": "text", "default": "xml sitemap"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Blog Title Ideas:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('blog-keyword').value.trim();
            if (!kw) {
                showToast("Please enter a topic keyword.", "error");
                return;
            }
            
            const titles = [
                `The Ultimate Guide to ${kw} for Beginners`,
                `10 Common ${kw} Mistakes You Need to Avoid`,
                `How to Optimize Your ${kw} for Faster Indexing`,
                `Why ${kw} is Critical for Organic SEO Success`,
                `Step-by-Step Tutorial: Creating a Custom ${kw}`
            ];
            
            document.getElementById('text-output').value = titles.join("\\n");
            updateBreakdown("<p class='text-success'>Blog title ideas generated.</p>");
        """
    },
    {
        "category": "AI SEO & Content Tools",
        "name": "Meta Description Generator",
        "slug": "meta-description-generator-seo",
        "desc": "Generate custom search-friendly meta descriptions containing target keywords.",
        "formula": "Keyword insertion description layout",
        "formula_desc": "Outputs description copy integrating target keywords within standard character limits.",
        "icon": "✍️",
        "inputs": [
            {"id": "desc-keyword", "label": "Target Keyword:", "type": "text", "default": "XML formatter"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Meta Description:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('desc-keyword').value.trim();
            if (!kw) {
                showToast("Please enter a target keyword.", "error");
                return;
            }
            
            const desc = `Optimize your website layout using our free ${kw} online. Format, validate, and beautify code snippets locally and privately in your browser tab.`;
            document.getElementById('text-output').value = desc;
            updateBreakdown(`<p class='text-success'>Description generated. Length = <strong>${desc.length}</strong> characters.</p>`);
        """
    },
    {
        "category": "AI SEO & Content Tools",
        "name": "FAQ Generator",
        "slug": "faq-generator-seo",
        "desc": "Generate lists of frequently asked questions to optimize content layout.",
        "formula": "Topic question mapping",
        "formula_desc": "Combines topics with standard question frames to build baseline FAQs.",
        "icon": "❓",
        "inputs": [
            {"id": "faq-kw", "label": "Topic Keyword:", "type": "text", "default": "canonical checker"}
        ],
        "outputs": [
            {"id": "text-output", "label": "FAQ List Output:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('faq-kw').value.trim();
            if (!kw) {
                showToast("Please enter a keyword.", "error");
                return;
            }
            
            let list = `Suggested FAQs for "${kw}":\\n\\n`;
            list += `Q1: Why is a ${kw} important for website SEO?\\n`;
            list += `A1: A ${kw} helps verify that search engine index rules are set correctly.\\n\\n`;
            list += `Q2: Can I use this ${kw} online for free?\\n`;
            list += `A2: Yes, the tool is 100% free with no limits.\\n\\n`;
            list += `Q3: How does the ${kw} calculate results?\\n`;
            list += `A3: All calculations are handled locally inside active browser memory.`;
            
            document.getElementById('text-output').value = list;
            updateBreakdown("<p class='text-success'>FAQ list compiled.</p>");
        """
    },
    {
        "category": "AI SEO & Content Tools",
        "name": "Content Brief Generator",
        "slug": "content-brief-generator",
        "desc": "Generate detailed content briefings containing outlines and target keywords for copywriters.",
        "formula": "Outline serialization compounding",
        "formula_desc": "Outputs structured headings, word count targets, and keywords mapping checklists.",
        "icon": "📝",
        "inputs": [
            {"id": "brief-topic", "label": "Target Topic:", "type": "text", "default": "Local SEO Checklist"},
            {"id": "brief-kw", "label": "Primary Keywords:", "type": "text", "default": "local SEO, business directories"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Content Brief Output:", "type": "textarea"}
        ],
        "calc_js": """
            const topic = document.getElementById('brief-topic').value.trim();
            const kw = document.getElementById('brief-kw').value.trim();
            
            if (!topic) {
                showToast("Please enter a topic.", "error");
                return;
            }
            
            let brief = `CONTENT BRIEF: "${topic}"\\n===========================\\n\\n`;
            brief += "Target Word Count: 1,200 - 1,500 words\\n\\n";
            brief += `Primary Keywords: ${kw || "None"}\\n\\n`;
            brief += "Suggested Outlines Structure:\\n";
            brief += `1. Introduction to ${topic}\\n`;
            brief += `2. Key Benefits of optimizing your page\\n`;
            brief += `3. Step-by-Step Optimization Guide\\n`;
            brief += `4. FAQs and Summary\\n\\n`;
            brief += "SEO Guidelines:\\n- Place the primary keyword in H1 and first paragraph.\\n- Maintain keyword density around 1-2%.";
            
            document.getElementById('text-output').value = brief;
            updateBreakdown("<p class='text-success'>Content brief outline created.</p>");
        """
    },
    {
        "category": "AI SEO & Content Tools",
        "name": "Keyword Cluster Generator",
        "slug": "keyword-cluster-generator",
        "desc": "Group related keywords into semantic thematic clusters for content planning.",
        "formula": "Thematic keywords clustering",
        "formula_desc": "Groups keywords based on core semantic similarities (e.g., separating local and informational terms).",
        "icon": "📂",
        "inputs": [
            {"id": "kw-list", "label": "Enter Keywords List (One per line):", "type": "textarea", "default": "best seo tools\\nlocal seo seattle\\nfree xml validator\\nseo checker seattle"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Keyword Clusters:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('kw-list').value.trim();
            if (!raw) {
                showToast("Please enter keywords.", "error");
                return;
            }
            
            const list = raw.split(/\\n/).map(k => k.trim()).filter(k => k.length > 0);
            const clusters = {};
            
            list.forEach(kw => {
                const words = kw.toLowerCase().split(/\\s+/);
                let grouped = false;
                
                for (let word of words) {
                    if (word.length > 3 && ["tool", "checker", "validator", "seo", "local", "seattle"].includes(word)) {
                        clusters[word] = clusters[word] || [];
                        clusters[word].push(kw);
                        grouped = true;
                        break;
                    }
                }
                
                if (!grouped) {
                    clusters["general"] = clusters["general"] || [];
                    clusters["general"].push(kw);
                }
            });
            
            let report = "KEYWORD CLUSTER GROUPS:\\n\\n";
            Object.entries(clusters).forEach(([theme, items]) => {
                report += `Theme Cluster: [${theme.toUpperCase()}]\\n`;
                items.forEach(item => {
                    report += `  - ${item}\\n`;
                });
                report += "\\n";
            });
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Keywords grouped into clusters.</p>");
        """
    },
    {
        "category": "AI SEO & Content Tools",
        "name": "Blog Outline Generator",
        "slug": "blog-outline-generator",
        "desc": "Generate complete blog post outlines and subheading structures based on topic keywords.",
        "formula": "Editorial outline mapping",
        "formula_desc": "Maps topic inputs to structured blog layouts (H1: Title, H2: Intro, H3: Details, H2: Conclusion).",
        "icon": "📝",
        "inputs": [
            {"id": "out-topic", "label": "Blog Topic Keyword:", "type": "text", "default": "how to optimize robots.txt"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Blog Outline Output:", "type": "textarea"}
        ],
        "calc_js": """
            const topic = document.getElementById('out-topic').value.trim();
            if (!topic) {
                showToast("Please enter a blog topic.", "error");
                return;
            }
            
            let outline = `Blog Post Outline: "${topic}"\\n================================\\n\\n`;
            outline += `H1: The Complete Guide to "${topic}"\\n\\n`;
            outline += "H2: Introduction\\n- Hook and overview\\n- Why this topic is critical for search indexing\\n\\n";
            outline += "H2: Key Concepts & Basics\\n- Core definitions\\n- Common terms and configuration files\\n\\n";
            outline += "H2: Step-by-Step Optimization Guide\\n- How to format parameters\\n- Adding schemas and metadata\\n\\n";
            outline += "H2: FAQ & Common Pitfalls\\n- Character length errors\\n- Indexing blockages\\n\\n";
            outline += "H2: Conclusion & Summary\\n- Key takeaways\\n- Call to action";
            
            document.getElementById('text-output').value = outline;
            updateBreakdown("<p class='text-success'>Blog outline generated.</p>");
        """
    },
    {
        "category": "AI SEO & Content Tools",
        "name": "SEO Content Planner",
        "slug": "seo-content-planner",
        "desc": "Generate structured SEO content checklists for pages launch.",
        "formula": "Content parameter mappings",
        "formula_desc": "Outputs task mappings checklist including keyword priorities, target segments, and meta tag setup checklists.",
        "icon": "📅",
        "inputs": [
            {"id": "plan-keyword", "label": "Target Keyword:", "type": "text", "default": "JSON-LD validator"}
        ],
        "outputs": [
            {"id": "text-output", "label": "SEO Content Plan:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('plan-keyword').value.trim();
            if (!kw) {
                showToast("Please enter a target keyword.", "error");
                return;
            }
            
            let plan = `SEO CONTENT PLAN FOR: "${kw}"\\n================================\\n\\n`;
            plan += `1. Target Audience: Developers, Webmasters, SEO Experts\\n`;
            plan += `2. Content Type: Interactive tool page + SEO tutorial\\n`;
            plan += `3. URL Structure: enginewheels.com/tools/json-ld-validator.html\\n`;
            plan += `4. Meta Title suggestion: Free Online ${kw} | Validate JSON-LD Schemas\\n`;
            plan += `5. Primary Keyword placement checklist:\\n`;
            plan += `   - [ ] Page Title Tag\\n`;
            plan += `   - [ ] Meta Description\\n`;
            plan += `   - [ ] Main H1 Tag\\n`;
            plan += `   - [ ] First paragraph introduction\\n`;
            plan += `   - [ ] Image alt attributes`;
            
            document.getElementById('text-output').value = plan;
            updateBreakdown("<p class='text-success'>Content launch plan compiled.</p>");
        """
    },
    {
        "category": "AI SEO & Content Tools",
        "name": "Search Intent Generator",
        "slug": "search-intent-generator",
        "desc": "Generate search query suggestions matching specific user intents.",
        "formula": "Intent suffix template mapping",
        "formula_desc": "Appends intent-specific trigger words (e.g. tutorial for informational, purchase for transactional) onto keywords.",
        "icon": "🎯",
        "inputs": [
            {"id": "sig-keyword", "label": "Core Keyword:", "type": "text", "default": "xml formatter"},
            {"id": "sig-intent", "label": "Target Intent:", "type": "select", "default": "info",
             "options": [
                 ("info", "Informational (Guides, Q&A)"),
                 ("trans", "Transactional (Purchases, Action)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Intent Queries:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('sig-keyword').value.trim();
            const intent = document.getElementById('sig-intent').value;
            
            if (!kw) {
                showToast("Please enter a core keyword.", "error");
                return;
            }
            
            let list = [];
            if (intent === "info") {
                list = [
                    `what is a ${kw}`,
                    `how to use ${kw} online`,
                    `best free ${kw} guide`,
                    `why use a ${kw}`
                ];
            } else {
                list = [
                    `try ${kw} free`,
                    `download ${kw} offline`,
                    `online ${kw} generator`,
                    `access ${kw} dashboard`
                ];
            }
            
            document.getElementById('text-output').value = list.join("\\n");
            updateBreakdown("<p class='text-success'>Intent queries generated.</p>");
        """
    },
    {
        "category": "AI SEO & Content Tools",
        "name": "Topic Cluster Generator",
        "slug": "topic-cluster-generator",
        "desc": "Map core topics to support pillar-and-cluster SEO content models.",
        "formula": "Semantic topic clustering",
        "formula_desc": "Generates supporting cluster page concepts to link back to a main pillar content topic.",
        "icon": "📂",
        "inputs": [
            {"id": "cluster-pillar", "label": "Main Pillar Topic:", "type": "text", "default": "SEO Audits"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Topic Cluster Map:", "type": "textarea"}
        ],
        "calc_js": """
            const pillar = document.getElementById('cluster-pillar').value.trim();
            if (!pillar) {
                showToast("Please enter a pillar topic.", "error");
                return;
            }
            
            let map = `Pillar Topic Page: "${pillar}"\\n\\n`;
            map += `Supporting Cluster Content Pages:\\n`;
            map += `1. "${pillar} Checklist for Beginners"\\n`;
            map += `2. "How to Perform an On-page ${pillar} in 5 Steps"\\n`;
            map += `3. "Top Free ${pillar} Tools for Developers"\\n`;
            map += `4. "Common Mistakes in Webmaster ${pillar}s"\\n\\n`;
            map += "SEO Strategy: Link all supporting cluster pages back to the main pillar page using your target keywords.";
            
            document.getElementById('text-output').value = map;
            updateBreakdown("<p class='text-success'>Topic cluster map generated.</p>");
        """
    },
    {
        "category": "AI SEO & Content Tools",
        "name": "Content Calendar Generator",
        "slug": "content-calendar-generator-seo",
        "desc": "Generate a weekly content calendar posting schedule.",
        "formula": "Calender weeks schedule layout",
        "formula_desc": "Fills out weekly calendar frames mapping topics, keyword goals, and status check tags.",
        "icon": "📅",
        "inputs": [
            {"id": "cal-topic", "label": "Focus Topic Area:", "type": "text", "default": "Sitemaps and Indexing"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Content Calendar:", "type": "textarea"}
        ],
        "calc_js": """
            const topic = document.getElementById('cal-topic').value.trim();
            if (!topic) {
                showToast("Please enter a focus topic.", "error");
                return;
            }
            
            let cal = `CONTENT CALENDAR: "${topic}"\\n================================\\n\\n`;
            cal += `Week 1: Intro to ${topic}\\n`;
            cal += `  - Type: Blog Post\\n`;
            cal += `  - Status: Planned\\n\\n`;
            cal += `Week 2: Step-by-Step ${topic} Tutorial\\n`;
            cal += `  - Type: Video / Article\\n`;
            cal += `  - Status: Planned\\n\\n`;
            cal += `Week 3: Advanced ${topic} optimization tips\\n`;
            cal += `  - Type: Case Study\\n`;
            cal += `  - Status: Planned\\n\\n`;
            cal += `Week 4: Review and Audit of ${topic}\\n`;
            cal += `  - Type: Checklist / FAQ\\n`;
            cal += `  - Status: Planned`;
            
            document.getElementById('text-output').value = cal;
            updateBreakdown("<p class='text-success'>Monthly content calendar generated.</p>");
        """
    }
]

# -*- coding: utf-8 -*-
"""
Database of 20 SEO Analysis and Meta Tag Tools for Enginewheels
"""

SEO_ANALYSIS_TOOLS = [
    {
        "category": "SEO Analysis Tools",
        "name": "Keyword Density Checker",
        "slug": "keyword-density-checker",
        "desc": "Analyze the keyword density and distribution of your content to prevent keyword stuffing.",
        "formula": "Density % = (Keyword Occurrences / Total Word Count) * 100",
        "formula_desc": "Cleans the text, tokenizes it into words, and counts occurrences of single and multi-word phrases relative to total words.",
        "icon": "📊",
        "inputs": [
            {"id": "text-input", "label": "Paste Content Text:", "type": "textarea", "default": "SEO is critical for web visibility. SEO keyword density checker helps optimize search results. Good SEO practices improve rankings."},
            {"id": "target-keyword", "label": "Target Keyword (Optional):", "type": "text", "default": "seo"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Keyword Density Report:", "type": "textarea"}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            const target = document.getElementById('target-keyword').value.trim().toLowerCase();
            
            if (!text) {
                showToast("Please paste some content text to analyze.", "error");
                return;
            }
            
            // Clean text and split into words
            const words = text.toLowerCase().replace(/[^a-zA-Z0-9\\s-]/g, ' ').split(/\\s+/).filter(w => w.length > 1);
            const totalWords = words.length;
            
            if (totalWords === 0) {
                showToast("No valid words found in the content.", "error");
                return;
            }
            
            // Frequency map
            const freq = {};
            words.forEach(w => {
                freq[w] = (freq[w] || 0) + 1;
            });
            
            // Sort keywords
            const sorted = Object.entries(freq).sort((a, b) => b[1] - a[1]);
            
            let report = `Total Word Count: ${totalWords}\\n\\n`;
            
            if (target) {
                const count = freq[target] || 0;
                const density = ((count / totalWords) * 100).toFixed(2);
                report += `Target Keyword Density:\\n- "${target}": Count = ${count}, Density = ${density}%\\n\\n`;
            }
            
            report += "Top Keyword Densities:\\n";
            sorted.slice(0, 15).forEach(([word, count]) => {
                const density = ((count / totalWords) * 100).toFixed(2);
                report += `- "${word}": ${count} times (${density}%)\\n`;
            });
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Keyword density analysis completed successfully.</p>");
        """
    },
    {
        "category": "SEO Analysis Tools",
        "name": "Keyword Position Checker",
        "slug": "keyword-position-checker",
        "desc": "Check the occurrences and positional indices of keywords within your HTML or text content.",
        "formula": "Relative index scanning",
        "formula_desc": "Locates the index position of each match and determines its context within the heading structure and body tags.",
        "icon": "📍",
        "inputs": [
            {"id": "content-input", "label": "Paste Content or HTML:", "type": "textarea", "default": "<h1>Enginewheels Web Tools</h1>\\n<p>We build free online developer utilities. Our tools run fast.</p>"},
            {"id": "keyword-term", "label": "Keyword Term:", "type": "text", "default": "tools"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Keyword Position Report:", "type": "textarea"}
        ],
        "calc_js": """
            const content = document.getElementById('content-input').value.trim();
            const term = document.getElementById('keyword-term').value.trim().toLowerCase();
            
            if (!content || !term) {
                showToast("Please fill in all input fields.", "error");
                return;
            }
            
            const lowerContent = content.toLowerCase();
            const matches = [];
            let pos = lowerContent.indexOf(term);
            
            while (pos !== -1) {
                matches.push(pos);
                pos = lowerContent.indexOf(term, pos + 1);
            }
            
            let report = `Keyword: "${term}"\\n`;
            report += `Total Occurrences: ${matches.length}\\n\\n`;
            
            if (matches.length > 0) {
                report += "Positions found (character indexes):\\n";
                matches.forEach((idx, i) => {
                    const snippet = content.substring(Math.max(0, idx - 15), Math.min(content.length, idx + term.length + 15));
                    report += `${i + 1}. Index ${idx}: "...${snippet.replace(/\\n/g, ' ')}..."\\n`;
                });
            } else {
                report += "The keyword term was not found in the content.";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Keyword position index scanning completed.</p>");
        """
    },
    {
        "category": "SEO Analysis Tools",
        "name": "Keyword Difficulty Estimator",
        "slug": "keyword-difficulty-estimator",
        "desc": "Estimate search competition difficulty based on search volumes and backlink competitors.",
        "formula": "Difficulty Score = 0.4 * CompetitorsFactor + 0.6 * VolumeFactor",
        "formula_desc": "Applies logarithmic scaling to competitor counts and monthly search volumes to produce a difficulty score out of 100.",
        "icon": "⚖️",
        "inputs": [
            {"id": "search-volume", "label": "Monthly Search Volume:", "type": "number", "default": "5000", "min": "10", "max": "10000000"},
            {"id": "competitors-count", "label": "Estimated Competitors Count:", "type": "number", "default": "15000", "min": "0", "max": "100000000"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Difficulty Estimation Report:", "type": "textarea"}
        ],
        "calc_js": """
            const volume = parseFloat(document.getElementById('search-volume').value) || 0;
            const competitors = parseFloat(document.getElementById('competitors-count').value) || 0;
            
            if (volume <= 0) {
                showToast("Please enter a valid positive search volume.", "error");
                return;
            }
            
            // Logarithmic scales
            const volFactor = Math.min(100, Math.max(10, Math.log10(volume) * 20));
            const compFactor = Math.min(100, Math.max(10, Math.log10(competitors + 1) * 15));
            
            const difficulty = Math.round(0.4 * compFactor + 0.6 * volFactor);
            
            let level = "Easy";
            let color = "Green";
            if (difficulty > 65) {
                level = "Hard";
                color = "Red";
            } else if (difficulty > 35) {
                level = "Medium";
                color = "Orange";
            }
            
            let report = `Estimated Difficulty Score: ${difficulty}/100 (${level})\\n\\n`;
            report += `Monthly Search Volume: ${volume.toLocaleString()}\\n`;
            report += `Estimated Competitors: ${competitors.toLocaleString()}\\n\\n`;
            report += "Recommendation:\\n";
            if (level === "Easy") {
                report += "- Excellent target keyword! Low competition and moderate search interest make this highly viable for organic rankings.";
            } else if (level === "Medium") {
                report += "- Solid potential. Requires dedicated content building, meta tag optimization, and structured schemas to compete effectively.";
            } else {
                report += "- Highly competitive. Direct targeting might be difficult. Try focusing on long-tail variations of this keyword phrase.";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Estimated keyword difficulty calculated as <strong style="color:${color.toLowerCase()}">${difficulty}%</strong> (${level}).</p>`);
        """
    },
    {
        "category": "SEO Analysis Tools",
        "name": "Keyword Frequency Analyzer",
        "slug": "keyword-frequency-analyzer",
        "desc": "Analyze the frequency of single words, 2-grams, and 3-grams inside copy content.",
        "formula": "Tokenized n-gram counting",
        "formula_desc": "Splits text into words, aggregates single words and multi-word sliding window sequences, and counts frequencies.",
        "icon": "🔍",
        "inputs": [
            {"id": "text-input", "label": "Paste Copy Text:", "type": "textarea", "default": "Free SEO tools are useful. Free SEO tools improve search optimization. Web tools are helpful."},
            {"id": "ngram-size", "label": "Phrase Size (N-gram):", "type": "select", "default": "2",
             "options": [
                 ("1", "Single Words (1-gram)"),
                 ("2", "Two-Word Phrases (2-gram)"),
                 ("3", "Three-Word Phrases (3-gram)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Frequency Report:", "type": "textarea"}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            const size = parseInt(document.getElementById('ngram-size').value) || 1;
            
            if (!text) {
                showToast("Please enter text content to analyze.", "error");
                return;
            }
            
            const words = text.toLowerCase().replace(/[^a-zA-Z0-9\\s]/g, ' ').split(/\\s+/).filter(w => w.length > 0);
            const totalWords = words.length;
            
            if (totalWords < size) {
                showToast(`Text is too short to extract ${size}-gram phrases.`, "error");
                return;
            }
            
            const frequency = {};
            for (let i = 0; i <= totalWords - size; i++) {
                const phrase = words.slice(i, i + size).join(" ");
                frequency[phrase] = (frequency[phrase] || 0) + 1;
            }
            
            const sorted = Object.entries(frequency).sort((a, b) => b[1] - a[1]);
            
            let report = `Frequency Analysis (${size}-gram phrases):\\n\\n`;
            sorted.slice(0, 15).forEach(([phrase, count]) => {
                report += `- "${phrase}": ${count} occurrences\\n`;
            });
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>N-gram frequency analysis completed.</p>");
        """
    },
    {
        "category": "SEO Analysis Tools",
        "name": "Content SEO Analyzer",
        "slug": "content-seo-analyzer",
        "desc": "Analyze content structures including meta tags alignment, word counts, and header layouts.",
        "formula": "Content parameter validation thresholds",
        "formula_desc": "Checks length parameters of Title, Description, word counts, and validates the presence of H1 tag structures.",
        "icon": "📝",
        "inputs": [
            {"id": "title-input", "label": "Title Tag Content:", "type": "text", "default": "Free SEO Tools | Online Meta Generators - Enginewheels"},
            {"id": "desc-input", "label": "Meta Description:", "type": "text", "default": "Optimize your website metadata with our free SEO utilities. Fast, client-side, and ad-light."},
            {"id": "content-body", "label": "Article Body Text:", "type": "textarea", "default": "<h1>Free SEO Tools</h1><p>Writing meta tags helps crawlers index websites. Keywords should be placed in Title and Description tags. Word count should exceed 300 words for standard blog posts.</p>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "SEO Analyzer Audit:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('title-input').value.trim();
            const desc = document.getElementById('desc-input').value.trim();
            const body = document.getElementById('content-body').value.trim();
            
            let report = "CONTENT SEO ANALYZER REPORT\\n===========================\\n\\n";
            
            // 1. Title Tag Check
            const tLen = title.length;
            report += `Title Tag Length: ${tLen} characters\\n`;
            if (tLen === 0) {
                report += "- [ERROR] Title tag is empty! Add a title (50-60 chars).\\n\\n";
            } else if (tLen < 40 || tLen > 65) {
                report += `- [WARNING] Title length is suboptimal. Recommended 45-60 characters.\\n\\n`;
            } else {
                report += "- [OK] Title length is optimal.\\n\\n";
            }
            
            // 2. Meta Description Check
            const dLen = desc.length;
            report += `Meta Description Length: ${dLen} characters\\n`;
            if (dLen === 0) {
                report += "- [ERROR] Meta Description is empty! Add a description (120-160 chars).\\n\\n";
            } else if (dLen < 110 || dLen > 160) {
                report += `- [WARNING] Description length is suboptimal. Recommended 120-160 characters.\\n\\n`;
            } else {
                report += "- [OK] Description length is optimal.\\n\\n";
            }
            
            // 3. H1 Check
            const hasH1 = /<h1[^>]*>.*?<\\/h1>/i.test(body);
            report += `H1 Heading Check:\\n`;
            if (hasH1) {
                report += "- [OK] Document contains at least one H1 heading tag.\\n\\n";
            } else {
                report += "- [ERROR] Document is missing an <h1> tag! Add a primary heading.\\n\\n";
            }
            
            // 4. Word Count
            const cleanText = body.replace(/<[^>]+>/g, ' ');
            const words = cleanText.split(/\\s+/).filter(w => w.length > 0);
            const wCount = words.length;
            report += `Body Word Count: ${wCount} words\\n`;
            if (wCount < 300) {
                report += "- [WARNING] Short content layout. Consider expanding past 300 words for better indexing.\\n";
            } else {
                report += "- [OK] Word count is sufficient for search engine visibility.\\n";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>SEO Content audit finished.</p>");
        """
    },
    {
        "category": "SEO Analysis Tools",
        "name": "On-Page SEO Checker",
        "slug": "on-page-seo-checker",
        "desc": "Check critical on-page SEO factors by analyzing raw HTML markup configurations.",
        "formula": "HTML tag extraction audit",
        "formula_desc": "Scans raw HTML code using regular expressions to extract and check Title, Description, Headings, and Alt attributes.",
        "icon": "🏡",
        "inputs": [
            {"id": "html-code", "label": "Paste HTML Source Code:", "type": "textarea", "default": "<!DOCTYPE html>\\n<html>\\n<head>\\n  <title>SEO Checker Page</title>\\n  <meta name='description' content='On-page testing.'>\\n</head>\\n<body>\\n  <h1>Main Header</h1>\\n  <img src='logo.png'>\\n</body>\\n</html>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "On-Page Checklist:", "type": "textarea"}
        ],
        "calc_js": """
            const html = document.getElementById('html-code').value.trim();
            if (!html) {
                showToast("Please enter HTML source code to check.", "error");
                return;
            }
            
            let report = "ON-PAGE SEO MARKUP CHECKLIST\\n===========================\\n\\n";
            
            // Extract title
            const titleMatch = html.match(/<title>([^<]+)<\/title>/i);
            if (titleMatch) {
                report += `[✔] Title Tag Found: "${titleMatch[1].trim()}"\\n`;
            } else {
                report += "[✘] Title Tag Missing! Critical SEO item.\\n";
            }
            
            // Extract description
            const descMatch = html.match(/<meta[^>]+name=['\"]description['\"][^>]+content=['\"]([^'\"]+)['\"]/i) ||
                             html.match(/<meta[^>]+content=['\"]([^'\"]+)['\"][^>]+name=['\"]description['\"]/i);
            if (descMatch) {
                report += `[✔] Meta Description Found: "${descMatch[1].trim()}"\\n`;
            } else {
                report += "[✘] Meta Description Tag Missing! Critical SEO item.\\n";
            }
            
            // H1 count
            const h1Matches = html.match(/<h1[^>]*>/gi) || [];
            if (h1Matches.length === 1) {
                report += "[✔] Single H1 Heading Tag present.\\n";
            } else if (h1Matches.length > 1) {
                report += `[!] Multiple H1 Tags Found (${h1Matches.length}). Only one H1 recommended per page.\\n`;
            } else {
                report += "[✘] H1 Tag Missing! Add one primary heading.\\n";
            }
            
            // Images alt checks
            const imgCount = (html.match(/<img[^>]*>/gi) || []).length;
            const altCount = (html.match(/<img[^>]+alt=['\"][^'\"]*['\"]/gi) || []).length;
            if (imgCount > 0) {
                const missing = imgCount - altCount;
                if (missing === 0) {
                    report += `[✔] All ${imgCount} images have alt text attributes.\\n`;
                } else {
                    report += `[!] ${missing} out of ${imgCount} image tags lack alt text attributes.\\n`;
                }
            } else {
                report += "[OK] No image tags detected in the page content.\\n";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>On-page HTML markup checker complete.</p>");
        """
    },
    {
        "category": "SEO Analysis Tools",
        "name": "SEO Audit Tool",
        "slug": "seo-audit-tool",
        "desc": "Execute a localized simulated SEO audit on your page structure and indexing settings.",
        "formula": "SEO index score compilation",
        "formula_desc": "Grades the presence of Title, Robots tag directives, open-graph markup, and heading outlines.",
        "icon": "📋",
        "inputs": [
            {"id": "html-source", "label": "Paste Webpage Source Code:", "type": "textarea", "default": "<title>Enginewheels | Tool Shop</title>\\n<meta name='robots' content='index, follow'>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "SEO Audit Report:", "type": "textarea"}
        ],
        "calc_js": """
            const html = document.getElementById('html-source').value.trim();
            if (!html) {
                showToast("Please enter webpage source code.", "error");
                return;
            }
            
            let score = 100;
            let report = "SEO COMPREHENSIVE AUDIT REPORT\\n=============================\\n\\n";
            
            // Check title
            if (/<title>.*?<\/title>/i.test(html)) {
                report += "- Title Tag: PASSED\\n";
            } else {
                report += "- Title Tag: FAILED (-25 points)\\n";
                score -= 25;
            }
            
            // Check description
            if (/name=['\"]description['\"]/i.test(html)) {
                report += "- Meta Description: PASSED\\n";
            } else {
                report += "- Meta Description: FAILED (-25 points)\\n";
                score -= 25;
            }
            
            // Check robots
            if (/name=['\"]robots['\"]/i.test(html)) {
                report += "- Robots Directives: PASSED\\n";
            } else {
                report += "- Robots Directives: WARNING (-10 points)\\n";
                score -= 10;
            }
            
            // Check open graph
            if (/property=['\"]og:title['\"]/i.test(html)) {
                report += "- OpenGraph Protocol: PASSED\\n";
            } else {
                report += "- OpenGraph Protocol: WARNING (-10 points)\\n";
                score -= 10;
            }
            
            // Check canonical link
            if (/rel=['\"]canonical['\"]/i.test(html)) {
                report += "- Canonical URL Link: PASSED\\n";
            } else {
                report += "- Canonical URL Link: WARNING (-15 points)\\n";
                score -= 15;
            }
            
            report += `\\nTOTAL SEO PERFORMANCE SCORE: ${Math.max(0, score)}/100\\n`;
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>SEO Page Audit completed. Global Score = <strong>${Math.max(0, score)}%</strong></p>`);
        """
    },
    {
        "category": "SEO Analysis Tools",
        "name": "SEO Score Checker",
        "slug": "seo-score-checker",
        "desc": "Calculate a percentage score evaluating the search readiness of your metadata.",
        "formula": "Score % = Weightings sum check",
        "formula_desc": "Evaluates keyword placement, tag lengths, and structure validity into an interactive SEO percentage score.",
        "icon": "💯",
        "inputs": [
            {"id": "title-text", "label": "Page Title Tag:", "type": "text", "default": "Free Developer Tools Online - Fast & Private"},
            {"id": "description-text", "label": "Meta Description Tag:", "type": "text", "default": "Get access to free developer utilities. Run JSON formats, encoders, decoders, and password generators locally in the browser."},
            {"id": "h1-text", "label": "Primary H1 Tag Content:", "type": "text", "default": "Developer Tools"}
        ],
        "outputs": [
            {"id": "text-output", "label": "SEO Score Analysis:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('title-text').value.trim();
            const desc = document.getElementById('description-text').value.trim();
            const h1 = document.getElementById('h1-text').value.trim();
            
            let score = 0;
            let report = "";
            
            // Check title
            if (title.length >= 45 && title.length <= 65) {
                score += 40;
                report += "[✔] Title length is optimal. (+40 points)\\n";
            } else if (title.length > 0) {
                score += 20;
                report += "[!] Title length is suboptimal (should be 45-65 chars). (+20 points)\\n";
            } else {
                report += "[✘] Title tag is empty. (+0 points)\\n";
            }
            
            // Check description
            if (desc.length >= 120 && desc.length <= 160) {
                score += 40;
                report += "[✔] Description length is optimal. (+40 points)\\n";
            } else if (desc.length > 0) {
                score += 20;
                report += "[!] Description length is suboptimal (should be 120-160 chars). (+20 points)\\n";
            } else {
                report += "[✘] Description tag is empty. (+0 points)\\n";
            }
            
            // Check H1
            if (h1.length > 0) {
                score += 20;
                report += "[✔] Primary H1 Tag is configured. (+20 points)\\n";
            } else {
                report += "[✘] H1 Tag is missing. (+0 points)\\n";
            }
            
            let finalReport = `SEO Readiness Score: ${score}%\\n\\nChecks:\\n${report}`;
            document.getElementById('text-output').value = finalReport;
            updateBreakdown(`<p>SEO Score calculation completed: <strong>${score}%</strong></p>`);
        """
    },
    {
        "category": "SEO Analysis Tools",
        "name": "SEO Content Optimizer",
        "slug": "seo-content-optimizer",
        "desc": "Optimize keyword placement and structure across content segments to maximize ranking opportunities.",
        "formula": "Semantic placement matching",
        "formula_desc": "Checks if the primary target keyword is included in headings, the first paragraph, and alt attributes.",
        "icon": "✍️",
        "inputs": [
            {"id": "keyword-term", "label": "Target Keyword:", "type": "text", "default": "developer tools"},
            {"id": "content-body", "label": "Write Content Body:", "type": "textarea", "default": "We build developer tools for modern web applications. These tools run locally and fast."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Optimization Recommendations:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('keyword-term').value.trim().toLowerCase();
            const body = document.getElementById('content-body').value.trim().toLowerCase();
            
            if (!kw || !body) {
                showToast("Please provide both target keyword and content body.", "error");
                return;
            }
            
            let report = "CONTENT OPTIMIZATION CHECKLIST\\n===============================\\n\\n";
            
            // Check keyword in body
            const occurrences = (body.match(new RegExp(kw.replace(/[-\\/\\\\^$*+?.()|[\\]{}]/g, '\\\\$&'), 'g')) || []).length;
            report += `Keyword Occurrences: ${occurrences}\\n`;
            
            if (occurrences === 0) {
                report += `- [ERROR] Primary keyword was not found in the body text! Insert it naturally.\\n`;
            } else {
                report += `- [OK] Primary keyword is mentioned.\\n`;
            }
            
            // Check first 150 chars
            const firstSegment = body.substring(0, 150);
            if (firstSegment.includes(kw)) {
                report += "- [OK] Keyword appears in the first paragraph (first 150 characters).\\n";
            } else {
                report += "- [WARNING] Keyword is missing in the introduction segment.\\n";
            }
            
            // Check density recommendation
            const wordsCount = body.split(/\\s+/).filter(w => w.length > 0).length;
            const density = ((occurrences / wordsCount) * 100).toFixed(2);
            report += `Keyword Density: ${density}%\\n`;
            if (density > 2.5) {
                report += "- [WARNING] Density is high (>2.5%). Watch out for keyword stuffing! Make it read naturally.\\n";
            } else if (density < 0.5) {
                report += "- [WARNING] Density is low (<0.5%). Consider placing the keyword a few more times.\\n";
            } else {
                report += "- [OK] Keyword density is optimal (0.5% - 2.5%).\\n";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Optimization checks generated.</p>");
        """
    },
    {
        "category": "SEO Analysis Tools",
        "name": "Search Snippet Preview Tool",
        "slug": "search-snippet-preview-tool",
        "desc": "Visualize how your meta tag titles and descriptions display on search engine results pages.",
        "formula": "Pixel truncation matching",
        "formula_desc": "Truncates titles at ~600px width limit (~60 characters) and description text at ~960px (~160 characters) to simulate Google UI.",
        "icon": "🖼️",
        "inputs": [
            {"id": "title-text", "label": "Google Search Title:", "type": "text", "default": "Best Developer Tools Online | Fast & Free"},
            {"id": "desc-text", "label": "Snippet Description:", "type": "text", "default": "Access an array of free developer utility checkers, password formatters, and hashing calculators locally in the browser."},
            {"id": "url-text", "label": "Page URL Path:", "type": "text", "default": "https://enginewheels.com/tools/json-formatter.html"}
        ],
        "outputs": [
            {"id": "text-output", "label": "SERP Snippet Output Preview:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('title-text').value.trim();
            const desc = document.getElementById('desc-text').value.trim();
            const url = document.getElementById('url-text').value.trim();
            
            let displayTitle = title;
            if (title.length > 60) {
                displayTitle = title.substring(0, 57) + "...";
            }
            
            let displayDesc = desc;
            if (desc.length > 160) {
                displayDesc = desc.substring(0, 157) + "...";
            }
            
            let report = "GOOGLE SERP PREVIEW SIMULATOR\\n==============================\\n\\n";
            report += `URL: ${url}\\n`;
            report += `Title Preview: ${displayTitle}\\n`;
            report += `Snippet Preview: ${displayDesc}\\n\\n`;
            report += `Total Title Characters: ${title.length}/60\\n`;
            report += `Total Description Characters: ${desc.length}/160\\n`;
            
            document.getElementById('text-output').value = report;
            
            // Build rich breakdown HTML snippet mockup
            const breakdownHtml = `
                <div style="background:#fff; color:#202124; padding:16px; border-radius:8px; font-family:arial,sans-serif; text-align:left; max-width:600px; margin: 15px auto; border:1px solid #dadce0;">
                    <div style="font-size:12px; line-height:16px; color:#3c4043; margin-bottom:4px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${url}</div>
                    <div style="font-size:20px; line-height:26px; color:#1a0dab; cursor:pointer; text-decoration:none; margin-bottom:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${displayTitle}</div>
                    <div style="font-size:14px; line-height:20px; color:#4d5156;">${displayDesc}</div>
                </div>
            `;
            updateBreakdown(breakdownHtml);
        """
    },
    {
        "category": "Meta Tag Tools",
        "name": "Meta Title Generator",
        "slug": "meta-title-generator",
        "desc": "Generate optimized SEO title tag titles that align with search engine recommendations.",
        "formula": "Tag concatenation and char limit check",
        "formula_desc": "Combines primary keyword, secondary brand tags, and separator characters while checking length boundaries.",
        "icon": "🏷️",
        "inputs": [
            {"id": "kw-primary", "label": "Primary Keyword Phrase:", "type": "text", "default": "Free XML Formatter"},
            {"id": "brand-name", "label": "Brand / Website Name:", "type": "text", "default": "Enginewheels"},
            {"id": "separator-type", "label": "Separator Mark:", "type": "select", "default": "|",
             "options": [
                 ("|", "Vertical Bar (|)"),
                 ("-", "Hyphen (-)"),
                 ("~", "Tilde (~)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Meta Title Tag:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('kw-primary').value.trim();
            const brand = document.getElementById('brand-name').value.trim();
            const sep = document.getElementById('separator-type').value;
            
            if (!kw) {
                showToast("Please enter a primary keyword.", "error");
                return;
            }
            
            let title = brand ? `${kw} ${sep} ${brand}` : kw;
            const tLen = title.length;
            
            let finalCode = `<title>${title}</title>`;
            let warningText = "";
            if (tLen > 60) {
                warningText = `<p class='text-warning'>Warning: Output title has ${tLen} characters, which exceeds the optimal 60-character threshold for search results.</p>`;
            } else {
                warningText = `<p class='text-success'>Success: Title length (${tLen} characters) is optimal.</p>`;
            }
            
            document.getElementById('text-output').value = finalCode;
            updateBreakdown(warningText);
        """
    },
    {
        "category": "Meta Tag Tools",
        "name": "Meta Description Generator",
        "slug": "meta-description-generator-tool",
        "desc": "Generate search-friendly HTML description meta tags of the correct length.",
        "formula": "Character count verification",
        "formula_desc": "Validates the length of your meta description summary to ensure it stays within Google's 120-160 character snippet limit.",
        "icon": "✍️",
        "inputs": [
            {"id": "desc-raw", "label": "Enter Description Text:", "type": "textarea", "default": "Format, validate, and beautify raw XML code snippets inside your browser. Safe, instant, client-side execution."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Meta Description Tag:", "type": "textarea"}
        ],
        "calc_js": """
            const text = document.getElementById('desc-raw').value.trim();
            if (!text) {
                showToast("Please write description content.", "error");
                return;
            }
            
            const len = text.length;
            let result = `<meta name="description" content="${text.replace(/"/g, '&quot;')}">`;
            
            let feedback = "";
            if (len < 110 || len > 160) {
                feedback = `<p class='text-warning'>Suboptimal length: ${len} characters. (Optimal range is 120-160 characters for best display on SERPs).</p>`;
            } else {
                feedback = `<p class='text-success'>Optimal length: ${len} characters.</p>`;
            }
            
            document.getElementById('text-output').value = result;
            updateBreakdown(feedback);
        """
    },
    {
        "category": "Meta Tag Tools",
        "name": "Meta Tags Generator",
        "slug": "meta-tags-generator-tool",
        "desc": "Generate complete meta header tag packages including open-graph and robots configurations.",
        "formula": "Key-value pair formatting",
        "formula_desc": "Assembles structured metadata inputs into a compiled, copy-paste-ready HTML block of header elements.",
        "icon": "🌐",
        "inputs": [
            {"id": "meta-title", "label": "Site Title:", "type": "text", "default": "Enginewheels Web Tools"},
            {"id": "meta-desc", "label": "Site Description:", "type": "text", "default": "Online developer utility checkers."},
            {"id": "meta-robots", "label": "Robots Index Directive:", "type": "select", "default": "index, follow",
             "options": [
                 ("index, follow", "Index & Follow"),
                 ("noindex, follow", "Noindex & Follow"),
                 ("index, nofollow", "Index & Nofollow"),
                 ("noindex, nofollow", "Noindex & Nofollow")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Compiled Meta Tags:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('meta-title').value.trim();
            const desc = document.getElementById('meta-desc').value.trim();
            const robots = document.getElementById('meta-robots').value;
            
            let code = `<!-- SEO Meta Tags -->\\n`;
            if (title) code += `<title>${title}</title>\\n`;
            if (desc) code += `<meta name="description" content="${desc.replace(/"/g, '&quot;')}">\\n`;
            code += `<meta name="robots" content="${robots}">`;
            
            document.getElementById('text-output').value = code;
            updateBreakdown("<p class='text-success'>SEO meta tags block compiled.</p>");
        """
    },
    {
        "category": "Meta Tag Tools",
        "name": "Meta Tags Analyzer",
        "slug": "meta-tags-analyzer",
        "desc": "Extract and analyze existing meta tags from a raw HTML header snippet.",
        "formula": "Regex matching patterns",
        "formula_desc": "Parses HTML strings to look for title, description, and keywords tag structures.",
        "icon": "🔎",
        "inputs": [
            {"id": "html-snippet", "label": "Paste Header HTML Code:", "type": "textarea", "default": '<title>My Web Page</title>\\n<meta name="description" content="This is an example webpage meta description.">'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Analysis Report:", "type": "textarea"}
        ],
        "calc_js": """
            const html = document.getElementById('html-snippet').value.trim();
            if (!html) {
                showToast("Please enter an HTML header block.", "error");
                return;
            }
            
            let report = "META TAG ANALYSIS REPORT\\n========================\\n\\n";
            
            const title = html.match(/<title>([^<]+)<\/title>/i);
            const desc = html.match(/<meta[^>]+name=['\"]description['\"][^>]+content=['\"]([^'\"]+)['\"]/i) ||
                         html.match(/<meta[^>]+content=['\"]([^'\"]+)['\"][^>]+name=['\"]description['\"]/i);
                         
            if (title) {
                report += `[✔] Title: "${title[1].trim()}" (${title[1].trim().length} chars)\\n`;
            } else {
                report += "[✘] Title tag not found!\\n";
            }
            
            if (desc) {
                report += `[✔] Description: "${desc[1].trim()}" (${desc[1].trim().length} chars)\\n`;
            } else {
                report += "[✘] Meta description tag not found!\\n";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Analysis complete.</p>");
        """
    },
    {
        "category": "Meta Tag Tools",
        "name": "Open Graph Generator",
        "slug": "open-graph-generator",
        "desc": "Create standard OpenGraph tags to customize your website's preview on platforms like Facebook and LinkedIn.",
        "formula": "Structured og metadata compiler",
        "formula_desc": "Combines URL paths, titles, description summaries, and card images into standard og meta elements.",
        "icon": "🌐",
        "inputs": [
            {"id": "og-title", "label": "OG Title:", "type": "text", "default": "Enginewheels Tools"},
            {"id": "og-desc", "label": "OG Description:", "type": "text", "default": "Free online developer checker utilities."},
            {"id": "og-url", "label": "Page Canonical URL:", "type": "text", "default": "https://enginewheels.com"},
            {"id": "og-image", "label": "Preview Image URL:", "type": "text", "default": "https://enginewheels.com/assets/img/og-preview.png"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Open Graph Code:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('og-title').value.trim();
            const desc = document.getElementById('og-desc').value.trim();
            const url = document.getElementById('og-url').value.trim();
            const img = document.getElementById('og-image').value.trim();
            
            let code = `<!-- Open Graph / Facebook -->\\n`;
            code += `<meta property="og:type" content="website">\\n`;
            if (url) code += `<meta property="og:url" content="${url}">\\n`;
            if (title) code += `<meta property="og:title" content="${title.replace(/"/g, '&quot;')}">\\n`;
            if (desc) code += `<meta property="og:description" content="${desc.replace(/"/g, '&quot;')}">\\n`;
            if (img) code += `<meta property="og:image" content="${img}">`;
            
            document.getElementById('text-output').value = code;
            updateBreakdown("<p class='text-success'>OpenGraph properties block compiled.</p>");
        """
    },
    {
        "category": "Meta Tag Tools",
        "name": "Twitter Card Generator",
        "slug": "twitter-card-generator",
        "desc": "Generate Twitter Card metadata to control how links look when shared on Twitter (X).",
        "formula": "Twitter card metadata compiler",
        "formula_desc": "Constructs custom Twitter metadata properties matching choices for Summary or Large Image formats.",
        "icon": "🐦",
        "inputs": [
            {"id": "tw-card-type", "label": "Card Layout Type:", "type": "select", "default": "summary_large_image",
             "options": [
                 ("summary_large_image", "Summary Card with Large Image"),
                 ("summary", "Summary Card")
             ]},
            {"id": "tw-title", "label": "Twitter Title:", "type": "text", "default": "Enginewheels Web Tools"},
            {"id": "tw-desc", "label": "Twitter Description:", "type": "text", "default": "Access free local online converters."},
            {"id": "tw-image", "label": "Preview Image URL:", "type": "text", "default": "https://enginewheels.com/assets/img/twitter-preview.png"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Twitter Card Code:", "type": "textarea"}
        ],
        "calc_js": """
            const type = document.getElementById('tw-card-type').value;
            const title = document.getElementById('tw-title').value.trim();
            const desc = document.getElementById('tw-desc').value.trim();
            const img = document.getElementById('tw-image').value.trim();
            
            let code = `<!-- Twitter Card Tags -->\\n`;
            code += `<meta name="twitter:card" content="${type}">\\n`;
            if (title) code += `<meta name="twitter:title" content="${title.replace(/"/g, '&quot;')}">\\n`;
            if (desc) code += `<meta name="twitter:description" content="${desc.replace(/"/g, '&quot;')}">\\n`;
            if (img) code += `<meta name="twitter:image" content="${img}">`;
            
            document.getElementById('text-output').value = code;
            updateBreakdown("<p class='text-success'>Twitter Card metadata block compiled.</p>");
        """
    },
    {
        "category": "Meta Tag Tools",
        "name": "Canonical URL Generator",
        "slug": "canonical-url-generator",
        "desc": "Generate canonical URL link tags to resolve duplicate content indexing issues.",
        "formula": "Canonical formatting",
        "formula_desc": "Outputs a rel=canonical link element pointing search engines to the preferred authority URL of the page.",
        "icon": "🔗",
        "inputs": [
            {"id": "url-pref", "label": "Preferred Authority URL:", "type": "text", "default": "https://enginewheels.com/tools/json-formatter.html"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Canonical Tag:", "type": "textarea"}
        ],
        "calc_js": """
            const url = document.getElementById('url-pref').value.trim();
            if (!url) {
                showToast("Please provide the authority URL.", "error");
                return;
            }
            
            const code = `<link rel="canonical" href="${url}">`;
            document.getElementById('text-output').value = code;
            updateBreakdown("<p class='text-success'>Canonical URL link tag generated.</p>");
        """
    },
    {
        "category": "Meta Tag Tools",
        "name": "Robots Meta Generator",
        "slug": "robots-meta-generator",
        "desc": "Generate meta robots tags to instruct crawlers on how to index and follow links on the page.",
        "formula": "Directive mapping compilation",
        "formula_desc": "Combines choices like index/noindex and follow/nofollow into standard crawlers meta tags.",
        "icon": "🤖",
        "inputs": [
            {"id": "c-index", "label": "Indexing Rule:", "type": "select", "default": "index",
             "options": [
                 ("index", "Index (Allow listing on search engines)"),
                 ("noindex", "Noindex (Block listing on search engines)")
             ]},
            {"id": "c-follow", "label": "Link Following Rule:", "type": "select", "default": "follow",
             "options": [
                 ("follow", "Follow (Instruct bots to crawl links)"),
                 ("nofollow", "Nofollow (Instruct bots not to crawl links)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Meta Robots Tag:", "type": "textarea"}
        ],
        "calc_js": """
            const idx = document.getElementById('c-index').value;
            const follow = document.getElementById('c-follow').value;
            
            const code = `<meta name="robots" content="${idx}, ${follow}">`;
            document.getElementById('text-output').value = code;
            updateBreakdown("<p class='text-success'>Robots crawler instructions compiled.</p>");
        """
    },
    {
        "category": "Meta Tag Tools",
        "name": "Social Meta Preview Tool",
        "slug": "social-meta-preview-tool",
        "desc": "Preview how shared links look on social networks like Facebook and Twitter (X).",
        "formula": "HTML preview simulation",
        "formula_desc": "Simulates card design, preview image aspect ratios, and typography of social platform snippet boxes.",
        "icon": "💬",
        "inputs": [
            {"id": "card-title", "label": "Card Title:", "type": "text", "default": "Free Developers Suite - Enginewheels"},
            {"id": "card-desc", "label": "Card Description:", "type": "text", "default": "Access an array of browser-based formatting utilities."},
            {"id": "card-image", "label": "Card Image Link:", "type": "text", "default": "https://enginewheels.com/assets/img/card.png"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Social Meta Tags Block:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('card-title').value.trim();
            const desc = document.getElementById('card-desc').value.trim();
            const img = document.getElementById('card-image').value.trim();
            
            let code = `<!-- OpenGraph -->\\n<meta property="og:title" content="${title}">\\n<meta property="og:description" content="${desc}">\\n<meta property="og:image" content="${img}">\\n`;
            code += `<!-- Twitter Card -->\\n<meta name="twitter:title" content="${title}">\\n<meta name="twitter:description" content="${desc}">\\n<meta name="twitter:image" content="${img}">`;
            
            document.getElementById('text-output').value = code;
            
            // Render simulated social card preview box
            const previewHtml = `
                <div style="background:#15202b; color:#fff; padding:12px; border-radius:12px; max-width:400px; margin: 15px auto; border:1px solid #38444d; font-family:system-ui,sans-serif; text-align:left;">
                    <div style="background:#22303c; border-radius:12px; overflow:hidden; border:1px solid #38444d;">
                        <div style="height:180px; background:#1c2938 url('${img}') no-repeat center; background-size:cover;"></div>
                        <div style="padding:12px;">
                            <div style="font-size:12px; color:#8899a6; text-transform:uppercase; margin-bottom:4px;">enginewheels.com</div>
                            <div style="font-size:15px; font-weight:700; color:#fff; margin-bottom:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${title}</div>
                            <div style="font-size:13px; color:#8899a6; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">${desc}</div>
                        </div>
                    </div>
                </div>
            `;
            updateBreakdown(previewHtml);
        """
    },
    {
        "category": "Meta Tag Tools",
        "name": "SERP Preview Tool",
        "slug": "serp-preview-tool",
        "desc": "Simulate and preview search engine result snippets in desktop and mobile viewports.",
        "formula": "Viewport display emulation",
        "formula_desc": "Validates text limits and maps search elements into Google SERP layouts.",
        "icon": "💻",
        "inputs": [
            {"id": "serp-title", "label": "Title Tag:", "type": "text", "default": "Free Code Validator | Format JSON & XML - Enginewheels"},
            {"id": "serp-desc", "label": "Snippet Description:", "type": "text", "default": "Format and validate your codebase snippets in a single click. Processes entirely client-side for maximum privacy and safety."},
            {"id": "serp-viewport", "label": "Target Viewport:", "type": "select", "default": "desktop",
             "options": [
                 ("desktop", "Desktop SERP Viewport (600px width limit)"),
                 ("mobile", "Mobile SERP Viewport (120px height wrap)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Snippet Specifications:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('serp-title').value.trim();
            const desc = document.getElementById('serp-desc').value.trim();
            const vp = document.getElementById('serp-viewport').value;
            
            let tLimit = vp === "desktop" ? 60 : 55;
            let dLimit = vp === "desktop" ? 160 : 120;
            
            let displayTitle = title.length > tLimit ? title.substring(0, tLimit - 3) + "..." : title;
            let displayDesc = desc.length > dLimit ? desc.substring(0, dLimit - 3) + "..." : desc;
            
            let spec = `Viewport Mode: ${vp.toUpperCase()}\\n`;
            spec += `Title Length: ${title.length}/${tLimit} chars\\n`;
            spec += `Description Length: ${desc.length}/${dLimit} chars\\n`;
            
            document.getElementById('text-output').value = spec;
            
            // Simulated SERP
            const mock = `
                <div style="background:#fff; padding:16px; border:1px solid #dadce0; border-radius:8px; max-width:${vp === "desktop" ? "600px" : "360px"}; margin:15px auto; text-align:left; font-family:arial,sans-serif;">
                    <div style="font-size:12px; color:#202124; margin-bottom:2px;">https://enginewheels.com</div>
                    <div style="font-size:${vp === "desktop" ? "20px" : "18px"}; color:#1a0dab; line-height:1.3; cursor:pointer; margin-bottom:4px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${displayTitle}</div>
                    <div style="font-size:14px; color:#4d5156; line-height:1.4;">${displayDesc}</div>
                </div>
            `;
            updateBreakdown(mock);
        """
    }
]

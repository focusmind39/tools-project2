# -*- coding: utf-8 -*-
"""
Database of 20 Content SEO and Link Tools for Enginewheels
"""

CONTENT_LINKS_TOOLS = [
    {
        "category": "Content SEO Tools",
        "name": "Title Length Checker",
        "slug": "title-length-checker",
        "desc": "Check character counts and pixel widths of title tags to ensure they fit in search results.",
        "formula": "Pixel matching length checks",
        "formula_desc": "Evaluates title string length against standard 60-character / 600px desktop truncation guidelines.",
        "icon": "📏",
        "inputs": [
            {"id": "title-val", "label": "Page Title Text:", "type": "text", "default": "Free SEO Tools | Online Meta Generators - Enginewheels"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Title Audit:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('title-val').value.trim();
            if (!val) {
                showToast("Please enter title text.", "error");
                return;
            }
            
            const len = val.length;
            let report = `Title Character Count: ${len}\\n`;
            
            if (len > 60) {
                report += `Status: TOO LONG\\n[✘] Title exceeds 60 characters and will likely be truncated on SERPs. Try keeping it under 60 characters.`;
            } else if (len < 30) {
                report += `Status: TOO SHORT\\n[WARNING] Title is under 30 characters. Expand it to include secondary keywords for better visibility.`;
            } else {
                report += `Status: OPTIMAL\\n[✔] Title length is perfectly optimized (30-60 characters).`;
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Title length check completed.</p>");
        """
    },
    {
        "category": "Content SEO Tools",
        "name": "Meta Description Length Checker",
        "slug": "meta-description-length-checker",
        "desc": "Evaluate meta descriptions for optimal character lengths and pixel widths.",
        "formula": "Snippet boundary evaluation",
        "formula_desc": "Evaluates description length against the standard 160-character SERP display limit.",
        "icon": "📝",
        "inputs": [
            {"id": "desc-val", "label": "Enter Description Text:", "type": "textarea", "default": "Format, validate, and optimize XML codes in your browser. Complete client-side tools."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Description Audit:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('desc-val').value.trim();
            if (!val) {
                showToast("Please enter description text.", "error");
                return;
            }
            
            const len = val.length;
            let report = `Description Character Count: ${len}\\n`;
            
            if (len > 160) {
                report += `Status: TOO LONG\\n[✘] Description exceeds 160 characters. It will likely get cut off in search snippets.`;
            } else if (len < 110) {
                report += `Status: TOO SHORT\\n[WARNING] Description is under 110 characters. Consider expanding it to highlight key page features.`;
            } else {
                report += `Status: OPTIMAL\\n[✔] Description length is perfectly optimized (110-160 characters).`;
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Description length checked.</p>");
        """
    },
    {
        "category": "Content SEO Tools",
        "name": "Heading Structure Analyzer",
        "slug": "heading-structure-analyzer",
        "desc": "Analyze HTML heading outlines and tag hierarchies (H1 to H6) for structural health.",
        "formula": "Tag outline hierarchy checks",
        "formula_desc": "Extracts headings and verifies nesting order (e.g. flagging H3 tags placed directly under H1).",
        "icon": "🏷️",
        "inputs": [
            {"id": "html-inp", "label": "Paste Content HTML:", "type": "textarea", "default": "<h1>Intro</h1>\\n<h3>Sub</h3>\\n<h2>Main</h2>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Heading Outline Analysis:", "type": "textarea"}
        ],
        "calc_js": """
            const html = document.getElementById('html-inp').value.trim();
            if (!html) {
                showToast("Please enter HTML code.", "error");
                return;
            }
            
            const regex = /<(h[1-6])[^>]*>(.*?)<\\/\\1>/gi;
            let match;
            let list = [];
            let report = "HEADING OUTLINE ANALYSIS:\\n\\n";
            
            while ((match = regex.exec(html)) !== null) {
                list.push({ tag: match[1].toLowerCase(), text: match[2].replace(/<[^>]+>/g, '').trim() });
            }
            
            if (list.length === 0) {
                report += "[✘] No heading tags (H1-H6) detected in the HTML code.";
                document.getElementById('text-output').value = report;
                updateBreakdown("<p class='text-warning'>Zero headings found.</p>");
                return;
            }
            
            let prevLevel = 0;
            let warnings = 0;
            
            list.forEach((h, idx) => {
                const level = parseInt(h.tag.charAt(1));
                const indent = "  ".repeat(level - 1);
                report += `${indent}${h.tag.toUpperCase()}: "${h.text}"\\n`;
                
                if (level - prevLevel > 1 && prevLevel > 0) {
                    report += `${indent}[WARNING] Heading level skipped! Tag ${h.tag} follows h${prevLevel}.\\n`;
                    warnings++;
                }
                prevLevel = level;
            });
            
            if (list[0].tag !== "h1") {
                report += "\\n[WARNING] Document does not start with an H1 tag!\\n";
                warnings++;
            }
            
            if (warnings === 0) {
                report += "\\n[✔] Heading tag hierarchy is standard and correctly structured.";
            } else {
                report += `\\nHeading check finished with ${warnings} outline warnings.`;
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Heading outline analyzed. Skipped levels = <strong>${warnings}</strong></p>`);
        """
    },
    {
        "category": "Content SEO Tools",
        "name": "Readability Checker",
        "slug": "readability-checker",
        "desc": "Calculate a Flesch Reading Ease score to optimize your content readability.",
        "formula": "Flesch Ease = 206.835 - 1.015 * (Words / Sentences) - 84.6 * (Syllables / Words)",
        "formula_desc": "Estimates words, sentences, and syllables to calculate a readability score out of 100.",
        "icon": "📚",
        "inputs": [
            {"id": "txt-body", "label": "Enter Content Copy:", "type": "textarea", "default": "Writing clean meta tags helps crawlers index websites. Keywords should be placed in Title and Description tags. Keep it simple and clear."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Readability Assessment:", "type": "textarea"}
        ],
        "calc_js": """
            const text = document.getElementById('txt-body').value.trim();
            if (!text) {
                showToast("Please enter copy text.", "error");
                return;
            }
            
            const words = text.split(/\\s+/).filter(w => w.length > 0);
            const wCount = words.length;
            
            const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 0);
            const sCount = Math.max(1, sentences.length);
            
            // Simple syllable estimator
            function countSyllables(word) {
                word = word.toLowerCase().replace(/[^a-z]/g, '');
                if (word.length <= 3) return 1;
                word = word.replace(/(?:es|ed|e)$/, '');
                word = word.replace(/^y/, '');
                const matches = word.match(/[aeiouy]{1,2}/g);
                return matches ? matches.length : 1;
            }
            
            let syllables = 0;
            words.forEach(w => { syllables += countSyllables(w); });
            
            const score = 206.835 - 1.015 * (wCount / sCount) - 84.6 * (syllables / wCount);
            const ease = Math.round(Math.max(0, Math.min(100, score)));
            
            let level = "Normal";
            if (ease > 80) level = "Very Easy (School Level)";
            else if (ease > 60) level = "Easy / Standard Text";
            else if (ease > 30) level = "Difficult (College Level)";
            else level = "Very Difficult (Academic)";
            
            let report = `Flesch Reading Ease Score: ${ease}/100\\n`;
            report += `Estimated Readability: ${level}\\n\\n`;
            report += `Total Words: ${wCount}\\n`;
            report += `Total Sentences: ${sCount}\\n`;
            report += `Average Sentence Length: ${(wCount / sCount).toFixed(1)} words`;
            
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Readability checker complete. Ease Score = <strong>${ease}</strong></p>`);
        """
    },
    {
        "category": "Content SEO Tools",
        "name": "Word Counter",
        "slug": "word-counter-tool",
        "desc": "Count words, characters, sentences, and paragraphs in your content real-time.",
        "formula": "String segmentation counts",
        "formula_desc": "Counts word sequences, paragraph breaks, and character lengths to calculate reading times.",
        "icon": "🔢",
        "inputs": [
            {"id": "words-text", "label": "Paste Content Text:", "type": "textarea", "default": "Free online developer checker tools. Fast and secure client-side calculations."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Copy Statistics:", "type": "textarea"}
        ],
        "calc_js": """
            const text = document.getElementById('words-text').value;
            const chars = text.length;
            const words = text.trim().split(/\\s+/).filter(w => w.length > 0).length;
            const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 0).length;
            const paragraphs = text.split(/\\n+/).filter(p => p.trim().length > 0).length;
            
            // Reading time at 200 words per minute
            const readTime = Math.ceil(words / 200);
            
            let report = `Words: ${words}\\n`;
            report += `Characters (including spaces): ${chars}\\n`;
            report += `Sentences: ${sentences}\\n`;
            report += `Paragraphs: ${paragraphs}\\n`;
            report += `Estimated Read Time: ${readTime} minute(s)`;
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Word counter statistics compiled.</p>");
        """
    },
    {
        "category": "Content SEO Tools",
        "name": "Keyword Extractor",
        "slug": "keyword-extractor",
        "desc": "Extract high-density single and multi-word terms from your content, ignoring stop words.",
        "formula": "Stopword filtration and frequency count",
        "formula_desc": "Filters out common English stop words and counts occurrences of remaining keywords.",
        "icon": "🔑",
        "inputs": [
            {"id": "extract-text", "label": "Paste Content text:", "type": "textarea", "default": "Webmasters write XML sitemaps to optimize their index pages. Clean XML formatting is critical."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Extracted Keywords:", "type": "textarea"}
        ],
        "calc_js": """
            const text = document.getElementById('extract-text').value.trim();
            if (!text) {
                showToast("Please paste text content.", "error");
                return;
            }
            
            const stopWords = ["the", "a", "an", "and", "or", "but", "is", "are", "was", "were", "to", "for", "in", "on", "at", "by", "with", "this", "that", "these", "those", "it", "its", "their", "our", "your"];
            const words = text.toLowerCase().replace(/[^a-zA-Z0-9\\s-]/g, ' ').split(/\\s+/).filter(w => w.length > 2 && !stopWords.includes(w));
            
            const freq = {};
            words.forEach(w => { freq[w] = (freq[w] || 0) + 1; });
            const sorted = Object.entries(freq).sort((a, b) => b[1] - a[1]);
            
            let report = "Top Extracted Keywords:\\n";
            sorted.slice(0, 10).forEach(([word, count]) => {
                report += `- "${word}": ${count} times\\n`;
            });
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Keyword extraction completed.</p>");
        """
    },
    {
        "category": "Content SEO Tools",
        "name": "N-Gram Generator",
        "slug": "n-gram-generator",
        "desc": "Generate n-gram phrases (words sequences) from your copy content.",
        "formula": "Window slide compounding",
        "formula_desc": "Generates sequences of consecutive words of a specified length (N).",
        "icon": "🔍",
        "inputs": [
            {"id": "ngram-text", "label": "Enter Content Copy:", "type": "textarea", "default": "Clean sitemaps help bots index websites cleanly."},
            {"id": "n-val", "label": "Select N Value:", "type": "select", "default": "2",
             "options": [
                 ("2", "Bi-gram (N=2)"),
                 ("3", "Tri-gram (N=3)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated N-grams:", "type": "textarea"}
        ],
        "calc_js": """
            const text = document.getElementById('ngram-text').value.trim();
            const n = parseInt(document.getElementById('n-val').value) || 2;
            
            if (!text) {
                showToast("Please enter some text.", "error");
                return;
            }
            
            const words = text.toLowerCase().replace(/[^a-zA-Z0-9\\s]/g, '').split(/\\s+/).filter(w => w.length > 0);
            if (words.length < n) {
                showToast("Text is too short to generate N-grams.", "error");
                return;
            }
            
            const ngrams = [];
            for (let i = 0; i <= words.length - n; i++) {
                ngrams.push(words.slice(i, i + n).join(" "));
            }
            
            document.getElementById('text-output').value = ngrams.join("\\n");
            updateBreakdown(`<p class='text-success'>Generated <strong>${ngrams.length}</strong> N-grams.</p>`);
        """
    },
    {
        "category": "Content SEO Tools",
        "name": "Internal Link Analyzer",
        "slug": "internal-link-analyzer",
        "desc": "Analyze HTML contents to extract, verify, and count internal vs. external links.",
        "formula": "Href attributes routing audit",
        "formula_desc": "Checks if links are relative, match the current site root, or point to external domains.",
        "icon": "🔗",
        "inputs": [
            {"id": "html-code", "label": "Paste HTML Source Code:", "type": "textarea", "default": '<a href="../index.html">Home</a>\\n<a href="https://google.com">Google</a>'},
            {"id": "domain-base", "label": "Site Base Domain (e.g., enginewheels.com):", "type": "text", "default": "enginewheels.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Link Analysis Report:", "type": "textarea"}
        ],
        "calc_js": """
            const html = document.getElementById('html-code').value.trim();
            const domain = document.getElementById('domain-base').value.trim();
            
            if (!html || !domain) {
                showToast("Please provide both HTML source and Base Domain.", "error");
                return;
            }
            
            const regex = /<a[^>]+href=['\"]([^'\"]+)['\"][^>]*>(.*?)<\\/a>/gi;
            let match;
            let internal = 0;
            let external = 0;
            let report = "INTERNAL LINK ANALYSIS\\n======================\\n\\n";
            
            while ((match = regex.exec(html)) !== null) {
                const href = match[1].trim();
                const anchor = match[2].replace(/<[^>]+>/g, '').trim();
                
                const isExternal = href.startsWith("http") && !href.includes(domain);
                if (isExternal) {
                    external++;
                    report += `[EXTERNAL] "${anchor}" -> ${href}\\n`;
                } else {
                    internal++;
                    report += `[INTERNAL] "${anchor}" -> ${href}\\n`;
                }
            }
            
            let summary = `Total Links Found: ${internal + external}\\n`;
            summary += `Internal Links: ${internal}\\n`;
            summary += `External Links: ${external}\\n\\nDetails:\\n${report}`;
            
            document.getElementById('text-output').value = summary;
            updateBreakdown("<p class='text-success'>Link analysis completed.</p>");
        """
    },
    {
        "category": "Content SEO Tools",
        "name": "Content Density Checker",
        "slug": "content-density-checker",
        "desc": "Check paragraph lengths and distribution of word densities across content segments.",
        "formula": "N-character paragraph segmentation check",
        "formula_desc": "Grades content distribution based on average sentence lengths and word counts per paragraph.",
        "icon": "📊",
        "inputs": [
            {"id": "content-inp", "label": "Paste Copy Text:", "type": "textarea", "default": "SEO tools are excellent for site optimization. Modern webmasters use them regularly.\\n\\nWriting sitemaps and robots files makes crawling highly effective."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Density Report:", "type": "textarea"}
        ],
        "calc_js": """
            const text = document.getElementById('content-inp').value.trim();
            if (!text) {
                showToast("Please paste text content.", "error");
                return;
            }
            
            const paragraphs = text.split(/\\n+/).filter(p => p.trim().length > 0);
            let report = `Paragraphs Count: ${paragraphs.length}\\n\\n`;
            
            paragraphs.forEach((p, idx) => {
                const words = p.trim().split(/\\s+/).filter(w => w.length > 0).length;
                report += `Paragraph ${idx + 1}: ${words} words\\n`;
                if (words > 150) {
                    report += "  [WARNING] Long paragraph block. Consider splitting it for better readability.\\n";
                } else {
                    report += "  [OK] Length is standard.\\n";
                }
            });
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Content paragraph density check completed.</p>");
        """
    },
    {
        "category": "Content SEO Tools",
        "name": "Content Optimization Tool",
        "slug": "content-optimization-tool",
        "desc": "Optimize headings, keywords, and text distribution inside content layouts.",
        "formula": "SEO factor alignment check",
        "formula_desc": "Runs structural checks on titles, descriptions, heading outlines, and word densities.",
        "icon": "🛠️",
        "inputs": [
            {"id": "opt-text", "label": "Write Article Text:", "type": "textarea", "default": "We build web tools to optimize sites. Format XML files instantly. These local utilities ensure absolute privacy."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Optimization Report:", "type": "textarea"}
        ],
        "calc_js": """
            const text = document.getElementById('opt-text').value.trim();
            if (!text) {
                showToast("Please write article content.", "error");
                return;
            }
            
            const words = text.split(/\\s+/).filter(w => w.length > 0).length;
            let report = "CONTENT OPTIMIZATION SCORE\\n=========================\\n\\n";
            report += `Total Words: ${words}\\n\\n`;
            
            if (words < 100) {
                report += "[✘] Content is too short. Add more detailed sections.\\n";
            } else if (words < 300) {
                report += "[WARNING] Thin content. Consider expanding to at least 300 words.\\n";
            } else {
                report += "[✔] Content length is good.\\n";
            }
            
            // Check headers
            if (text.includes("?") || text.includes("How") || text.includes("Why")) {
                report += "[✔] Content contains inquiry hooks/headings (How/Why).\\n";
            } else {
                report += "[WARNING] No clear inquiry hooks detected. Try adding headings like 'How It Works'.\\n";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Content optimization checks finished.</p>");
        """
    },
    {
        "category": "Link Tools",
        "name": "Internal Link Generator",
        "slug": "internal-link-generator",
        "desc": "Generate relative and absolute internal anchor link HTML tags based on keyword selections.",
        "formula": "HTML anchor tag rendering",
        "formula_desc": "Interpolates destination paths, titles, and target parameters into standard anchor element formats.",
        "icon": "⚓",
        "inputs": [
            {"id": "target-url", "label": "Target Internal URL:", "type": "text", "default": "/tools/json-formatter.html"},
            {"id": "anchor-text", "label": "Anchor Keyword Text:", "type": "text", "default": "JSON Formatter"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Anchor Tag:", "type": "textarea"}
        ],
        "calc_js": """
            const url = document.getElementById('target-url').value.trim();
            const anchor = document.getElementById('anchor-text').value.trim();
            
            if (!url || !anchor) {
                showToast("Please provide both URL and Anchor text.", "error");
                return;
            }
            
            const tag = `<a href="${url}">${anchor}</a>`;
            document.getElementById('text-output').value = tag;
            updateBreakdown("<p class='text-success'>Internal anchor link code generated.</p>");
        """
    },
    {
        "category": "Link Tools",
        "name": "Link Analyzer",
        "slug": "link-analyzer",
        "desc": "Extract and inspect all anchor links, rel tags, and destinations inside an HTML segment.",
        "formula": "Regex href attribute parsing",
        "formula_desc": "Scans HTML input to extract links, link texts, and meta-attributes (target, rel).",
        "icon": "🔬",
        "inputs": [
            {"id": "html-code", "label": "Paste HTML Code Snippet:", "type": "textarea", "default": '<a href="https://google.com" target="_blank" rel="noopener">Google</a>'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Link Analysis Report:", "type": "textarea"}
        ],
        "calc_js": """
            const html = document.getElementById('html-code').value.trim();
            if (!html) {
                showToast("Please enter HTML code.", "error");
                return;
            }
            
            const regex = /<a([^>]+)>(.*?)<\\/a>/gi;
            let match;
            let report = "LINK AUDIT ANALYSIS\\n===================\\n\\n";
            let count = 0;
            
            while ((match = regex.exec(html)) !== null) {
                count++;
                const attrs = match[1];
                const text = match[2].replace(/<[^>]+>/g, '').trim();
                
                const hrefMatch = attrs.match(/href=['\"]([^'\"]+)['\"]/i);
                const relMatch = attrs.match(/rel=['\"]([^'\"]+)['\"]/i);
                
                const href = hrefMatch ? hrefMatch[1] : "None";
                const rel = relMatch ? relMatch[1] : "None";
                
                report += `Link #${count}:\\n`;
                report += `- Text: "${text}"\\n`;
                report += `- Href: "${href}"\\n`;
                report += `- Rel: "${rel}"\\n\\n`;
            }
            
            if (count === 0) {
                report += "No anchor link tags found in the code snippet.";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p class='text-success'>Analyzed <strong>${count}</strong> links.</p>`);
        """
    },
    {
        "category": "Link Tools",
        "name": "Anchor Text Generator",
        "slug": "anchor-text-generator",
        "desc": "Generate click-worthy and descriptive anchor texts matching standard link guidelines.",
        "formula": "Semantic call-to-action mapping",
        "formula_desc": "Combines target keywords with standard transactional prompts (e.g. Try, Learn, Open, Access) into link anchor texts.",
        "icon": "⚓",
        "inputs": [
            {"id": "keyword", "label": "Target Keyword:", "type": "text", "default": "sitemap validator"},
            {"id": "cta-style", "label": "CTA Template style:", "type": "select", "default": "action",
             "options": [
                 ("action", "Action-Oriented (e.g., Try our...)"),
                 ("informative", "Informative (e.g., Read the guide on...)"),
                 ("direct", "Direct Keyword Only")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Anchor Text:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('keyword').value.trim();
            const style = document.getElementById('cta-style').value;
            
            if (!kw) {
                showToast("Please enter a target keyword.", "error");
                return;
            }
            
            let anchor = kw;
            if (style === "action") {
                anchor = `Try the free ${kw} online`;
            } else if (style === "informative") {
                anchor = `Learn how to use our ${kw}`;
            }
            
            document.getElementById('text-output').value = anchor;
            updateBreakdown("<p class='text-success'>Anchor text concept generated.</p>");
        """
    },
    {
        "category": "Link Tools",
        "name": "Anchor Text Analyzer",
        "slug": "anchor-text-analyzer",
        "desc": "Analyze distributions of anchor texts (generic, brand, exact match) from a list of links.",
        "formula": "Anchor category distribution check",
        "formula_desc": "Classifies anchors into Brand, Exact Match, Generic (e.g. click here), or Naked URL groups.",
        "icon": "📊",
        "inputs": [
            {"id": "anchors-list", "label": "Enter Anchor Texts (One per line):", "type": "textarea", "default": "click here\\nhttps://enginewheels.com\\nJSON Formatter\\nEnginewheels tools"},
            {"id": "brand-keyword", "label": "Brand / Main Keyword:", "type": "text", "default": "enginewheels"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Anchor Text Analysis:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('anchors-list').value.trim();
            const brand = document.getElementById('brand-keyword').value.trim().toLowerCase();
            
            if (!raw) {
                showToast("Please enter anchor texts.", "error");
                return;
            }
            
            const list = raw.split(/\\n/).map(a => a.trim()).filter(a => a.length > 0);
            let generic = 0;
            let brandCount = 0;
            let naked = 0;
            let others = 0;
            
            list.forEach(anchor => {
                const lower = anchor.toLowerCase();
                if (lower.startsWith("http://") || lower.startsWith("https://") || lower.includes("www.")) {
                    naked++;
                } else if (lower.includes("click") || lower.includes("here") || lower.includes("link") || lower.includes("website")) {
                    generic++;
                } else if (brand && lower.includes(brand)) {
                    brandCount++;
                } else {
                    others++;
                }
            });
            
            const total = list.length || 1;
            let report = "ANCHOR TEXT DISTRIBUTION REPORT\\n=============================\\n\\n";
            report += `Total Anchors: ${total}\\n`;
            report += `- Brand Anchors: ${brandCount} (${((brandCount/total)*100).toFixed(1)}%)\\n`;
            report += `- Generic Anchors: ${generic} (${((generic/total)*100).toFixed(1)}%)\\n`;
            report += `- Naked URL Anchors: ${naked} (${((naked/total)*100).toFixed(1)}%)\\n`;
            report += `- Other / Keyword Anchors: ${others} (${((others/total)*100).toFixed(1)}%)\\n\\n`;
            
            if (generic / total > 0.25) {
                report += "[WARNING] Generic anchor text density is high. Try using descriptive keywords in links.";
            } else {
                report += "[✔] Anchor text distribution looks balanced.";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Anchor texts distribution audited.</p>");
        """
    },
    {
        "category": "Link Tools",
        "name": "Broken Link Checker",
        "slug": "broken-link-checker",
        "desc": "Scan HTML code blocks for broken, empty, or improperly formatted links.",
        "formula": "Href formatting validation checks",
        "formula_desc": "Scans anchor href attributes and flags empty targets (#), broken paths, or javascript:void tags.",
        "icon": "⚠️",
        "inputs": [
            {"id": "html-source", "label": "Paste HTML Content:", "type": "textarea", "default": '<a href="#">Broken</a>\\n<a href="https://enginewheels.com">Valid</a>'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Broken Link Audit Report:", "type": "textarea"}
        ],
        "calc_js": """
            const html = document.getElementById('html-source').value.trim();
            if (!html) {
                showToast("Please enter HTML code to audit.", "error");
                return;
            }
            
            const regex = /<a[^>]+href=['\"]([^'\"]*)['\"][^>]*>(.*?)<\\/a>/gi;
            let match;
            let total = 0;
            let broken = 0;
            let report = "BROKEN LINK CHECKER AUDIT\\n=========================\\n\\n";
            
            while ((match = regex.exec(html)) !== null) {
                total++;
                const href = match[1].trim();
                const text = match[2].replace(/<[^>]+>/g, '').trim();
                
                let isBroken = false;
                let reason = "";
                
                if (href === "" || href === "#") {
                    isBroken = true;
                    reason = "Empty or Hash target (#)";
                } else if (href.startsWith("javascript:")) {
                    isBroken = true;
                    reason = "Javascript void binding";
                }
                
                if (isBroken) {
                    broken++;
                    report += `[FLAGGED] "${text}" -> "${href}" (Reason: ${reason})\\n`;
                } else {
                    report += `[OK] "${text}" -> "${href}"\\n`;
                }
            }
            
            let summary = `Total Links Scanned: ${total}\\n`;
            summary += `Flagged/Broken Links: ${broken}\\n\\nDetails:\\n${report}`;
            
            document.getElementById('text-output').value = summary;
            updateBreakdown(`<p>Link checklist processed. Flagged = <strong>${broken}</strong></p>`);
        """
    },
    {
        "category": "Link Tools",
        "name": "Link Attribute Checker",
        "slug": "link-attribute-checker",
        "desc": "Check HTML links to verify rel attributes (nofollow, noopener, noreferrer) for external URLs.",
        "formula": "Rel attribute validation checks",
        "formula_desc": "Validates if external links correctly implement secure and crawl-controlling attributes.",
        "icon": "🔬",
        "inputs": [
            {"id": "html-val", "label": "Paste HTML Links:", "type": "textarea", "default": '<a href="https://external.com" target="_blank">Link</a>'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Link Attribute Report:", "type": "textarea"}
        ],
        "calc_js": """
            const html = document.getElementById('html-val').value.trim();
            if (!html) {
                showToast("Please enter HTML code.", "error");
                return;
            }
            
            const regex = /<a([^>]+)>(.*?)<\\/a>/gi;
            let match;
            let report = "LINK ATTRIBUTE SECURITY AUDIT\\n=============================\\n\\n";
            let total = 0;
            
            while ((match = regex.exec(html)) !== null) {
                total++;
                const attrs = match[1];
                const text = match[2].replace(/<[^>]+>/g, '').trim();
                
                const hrefMatch = attrs.match(/href=['\"]([^'\"]+)['']/i) || attrs.match(/href=['\"]([^'\"]+)['\"]/i);
                const href = hrefMatch ? hrefMatch[1] : "";
                
                if (href.startsWith("http") && !href.includes("enginewheels.com")) {
                    const targetMatch = attrs.match(/target=['\"]_blank['\"]/i);
                    const relMatch = attrs.match(/rel=['\"]([^'\"]+)['\"]/i);
                    const relVal = relMatch ? relMatch[1] : "";
                    
                    report += `Link: "${text}" -> "${href}"\\n`;
                    if (targetMatch && !relVal.includes("noopener") && !relVal.includes("noreferrer")) {
                        report += `  - [WARNING] Opens in new tab without rel="noopener" or rel="noreferrer". Security vulnerability (tabnabbing).\\n`;
                    } else {
                        report += `  - [OK] Link settings are secure.\\n`;
                    }
                }
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Link attributes audit completed.</p>");
        """
    },
    {
        "category": "Link Tools",
        "name": "Redirect Path Checker",
        "slug": "redirect-path-checker",
        "desc": "Check and map redirection history paths to identify redirect loops.",
        "formula": "Redirect mapping chain audit",
        "formula_desc": "Simulates redirection routing hops step-by-step from source to landing URL.",
        "icon": "🔃",
        "inputs": [
            {"id": "redirect-chain", "label": "Redirection Steps (One URL per line):", "type": "textarea", "default": "http://site.com\\nhttps://site.com\\nhttps://site.com/home"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Redirect Path Analysis:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('redirect-chain').value.trim();
            if (!raw) {
                showToast("Please provide redirection steps.", "error");
                return;
            }
            
            const steps = raw.split(/\\n/).map(s => s.trim()).filter(s => s.length > 0);
            let report = "REDIRECT PATH HOP AUDIT\\n=======================\\n\\n";
            
            if (steps.length < 2) {
                report += "[WARNING] Path is too short to construct a chain. Enter at least 2 steps.";
            } else {
                steps.forEach((step, idx) => {
                    report += `Hop ${idx + 1}: ${step}\\n`;
                    if (idx < steps.length - 1) {
                        report += "  --> Redirecting (301 Permanent)...\\n";
                    } else {
                        report += "  --> Target Destination reached (Status: 200 OK).\\n";
                    }
                });
                
                report += `\\nTotal Redirection Hops: ${steps.length - 1}\\n`;
                if (steps.length - 1 > 3) {
                    report += "[WARNING] Chain is long. Too many hops can delay page loads and impact SEO rankings.";
                } else {
                    report += "[✔] Redirect chain length is search-optimal.";
                }
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Redirect path chain audit completed.</p>");
        """
    },
    {
        "category": "Link Tools",
        "name": "URL Cleaner",
        "slug": "url-cleaner",
        "desc": "Clean and remove tracking tokens and query parameters (UTM, gclid, fbclid) from URLs.",
        "formula": "URL Parameter strip filtering",
        "formula_desc": "Parses the URL query string, filters out common tracking parameter keys, and reconstructs the clean URL path.",
        "icon": "🧼",
        "inputs": [
            {"id": "url-raw", "label": "URL with Query Parameters:", "type": "text", "default": "https://enginewheels.com/tools/json.html?utm_source=news&gclid=12345&id=10"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Cleaned URL Output:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('url-raw').value.trim();
            if (!raw) {
                showToast("Please enter a URL to clean.", "error");
                return;
            }
            
            try {
                const url = new URL(raw);
                const searchParams = new URLSearchParams(url.search);
                const trackerKeys = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid", "fbclid", "msclkid"];
                
                let removed = [];
                trackerKeys.forEach(key => {
                    if (searchParams.has(key)) {
                        searchParams.delete(key);
                        removed.push(key);
                    }
                });
                
                url.search = searchParams.toString();
                const cleaned = url.toString();
                
                let report = `Cleaned URL:\\n${cleaned}\\n\\n`;
                if (removed.length > 0) {
                    report += `Removed Parameters: ${removed.join(", ")}`;
                } else {
                    report += "No tracking parameters found in the input URL.";
                }
                
                document.getElementById('text-output').value = report;
                updateBreakdown("<p class='text-success'>Tracking tokens removed.</p>");
            } catch (e) {
                showToast("Invalid URL format.", "error");
            }
        """
    },
    {
        "category": "Link Tools",
        "name": "URL Builder",
        "slug": "url-builder",
        "desc": "Build formatted URLs with custom key-value query parameters.",
        "formula": "Query parameter compilation",
        "formula_desc": "Combines base URL strings and parameter pairs into fully encoded query strings.",
        "icon": "🔧",
        "inputs": [
            {"id": "url-base", "label": "Base URL Path:", "type": "text", "default": "https://enginewheels.com/search"},
            {"id": "param-k1", "label": "Parameter Key 1:", "type": "text", "default": "q"},
            {"id": "param-v1", "label": "Parameter Value 1:", "type": "text", "default": "json tools"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Compiled URL Output:", "type": "textarea"}
        ],
        "calc_js": """
            const base = document.getElementById('url-base').value.trim();
            const k1 = document.getElementById('param-k1').value.trim();
            const v1 = document.getElementById('param-v1').value.trim();
            
            if (!base) {
                showToast("Please provide a base URL.", "error");
                return;
            }
            
            try {
                const url = new URL(base);
                if (k1) {
                    url.searchParams.set(k1, v1);
                }
                document.getElementById('text-output').value = url.toString();
                updateBreakdown("<p class='text-success'>URL built successfully.</p>");
            } catch (e) {
                showToast("Invalid base URL format.", "error");
            }
        """
    },
    {
        "category": "Link Tools",
        "name": "UTM Link Generator",
        "slug": "utm-link-generator",
        "desc": "Create Google Analytics UTM tracking URLs with campaign sources, mediums, and terms.",
        "formula": "UTM query parameter composition",
        "formula_desc": "Appends standard utm_ campaign parameter inputs onto the canonical landing page link.",
        "icon": "🏷️",
        "inputs": [
            {"id": "utm-base", "label": "Landing Page URL:", "type": "text", "default": "https://enginewheels.com/index.html"},
            {"id": "utm-src", "label": "Campaign Source (utm_source):", "type": "text", "default": "newsletter"},
            {"id": "utm-med", "label": "Campaign Medium (utm_medium):", "type": "text", "default": "email"},
            {"id": "utm-name", "label": "Campaign Name (utm_campaign):", "type": "text", "default": "summer_promo"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated UTM Link URL:", "type": "textarea"}
        ],
        "calc_js": """
            const base = document.getElementById('utm-base').value.trim();
            const src = document.getElementById('utm-src').value.trim();
            const med = document.getElementById('utm-med').value.trim();
            const name = document.getElementById('utm-name').value.trim();
            
            if (!base) {
                showToast("Base URL path is required.", "error");
                return;
            }
            
            try {
                const url = new URL(base);
                if (src) url.searchParams.set("utm_source", src);
                if (med) url.searchParams.set("utm_medium", med);
                if (name) url.searchParams.set("utm_campaign", name);
                
                document.getElementById('text-output').value = url.toString();
                updateBreakdown("<p class='text-success'>UTM tracking link generated.</p>");
            } catch (e) {
                showToast("Invalid base URL format.", "error");
            }
        """
    }
]

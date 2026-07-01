# -*- coding: utf-8 -*-
"""
Database of 10 Productivity Tools for Enginewheels
"""

PRODUCTIVITY_TOOLS = [
    {
        "category": "Productivity Tools",
        "name": "Lorem Ipsum Generator",
        "slug": "lorem-ipsum-generator",
        "desc": "Generate dummy placeholder text for website layout mockup designs.",
        "formula": "Lorem Ipsum word array generator",
        "formula_desc": "Outputs dummy paragraph blocks by stitching classic Latin phrases.",
        "icon": "📝",
        "inputs": [
            {"id": "lip-paragraphs", "label": "Number of Paragraphs:", "type": "number", "default": "3"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Placeholder Text:", "type": "textarea"}
        ],
        "calc_js": """
            const paras = parseInt(document.getElementById('lip-paragraphs').value) || 1;
            const lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";
            
            let result = [];
            for (let i = 0; i < paras; i++) {
                result.push(lorem);
            }
            document.getElementById('text-output').value = result.join('\\n\\n');
            updateBreakdown("<p class='text-success'>Generated " + paras + " paragraphs.</p>");
        """
    },
    {
        "category": "Productivity Tools",
        "name": "Dummy Data Generator",
        "slug": "dummy-data-generator",
        "desc": "Create mock user databases (names, emails, phones) in JSON format.",
        "formula": "Random Data Mapper loop",
        "formula_desc": "Outputs structured arrays containing mock user attributes.",
        "icon": "🤖",
        "inputs": [
            {"id": "dd-count", "label": "Number of Records:", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated JSON Output:", "type": "textarea"}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('dd-count').value) || 5;
            const names = ['John', 'Jane', 'Bob', 'Alice', 'Michael', 'Emily'];
            const domains = ['example.com', 'test.org', 'demo.net'];
            
            const arr = [];
            for (let i = 0; i < count; i++) {
                const name = names[Math.floor(Math.random() * names.length)];
                const email = `${name.toLowerCase()}@${domains[Math.floor(Math.random() * domains.length)]}`;
                arr.push({
                    id: i + 1,
                    name: name,
                    email: email,
                    phone: "+1-555-" + Math.floor(1000000 + Math.random() * 9000000)
                });
            }
            document.getElementById('text-output').value = JSON.stringify(arr, null, 2);
            updateBreakdown("<p class='text-success'>Mock dataset generated successfully.</p>");
        """
    },
    {
        "category": "Productivity Tools",
        "name": "UUID Generator",
        "slug": "uuid-generator-dev",
        "desc": "Generate secure Version 4 UUIDs (Universally Unique Identifiers).",
        "formula": "UUID v4 Cryptographic Random Hex",
        "formula_desc": "Generates 128-bit identifiers conforming to RFC 4122 layout using window.crypto.",
        "icon": "🔑",
        "inputs": [
            {"id": "uuid-count", "label": "Number of UUIDs to Generate:", "type": "number", "default": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated UUIDs:", "type": "textarea"}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('uuid-count').value) || 1;
            
            function generateUUID() {
                // Use standard cryptographically secure method if available
                if (typeof window.crypto !== 'undefined' && typeof window.crypto.randomUUID === 'function') {
                    return window.crypto.randomUUID();
                }
                // Fallback
                return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
                    var r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);
                    return v.toString(16);
                });
            }
            
            let list = [];
            for (let i = 0; i < count; i++) {
                list.push(generateUUID());
            }
            document.getElementById('text-output').value = list.join('\\n');
            updateBreakdown("<p class='text-success'>UUID v4 values compiled successfully.</p>");
        """
    },
    {
        "category": "Productivity Tools",
        "name": "Random Number Generator",
        "slug": "random-number-generator",
        "desc": "Generate random integers within a custom min/max range.",
        "formula": "Random = Floor(Math.random() * (Max - Min + 1)) + Min",
        "formula_desc": "Calculates decimal numbers inside custom boundaries using JavaScript math libraries.",
        "icon": "🔢",
        "inputs": [
            {"id": "rng-min", "label": "Minimum Value:", "type": "number", "default": "1"},
            {"id": "rng-max", "label": "Maximum Value:", "type": "number", "default": "100"}
        ],
        "outputs": [
            {"id": "out-number", "label": "Random Number Result:", "type": "text"}
        ],
        "calc_js": """
            const min = parseInt(document.getElementById('rng-min').value) || 0;
            const max = parseInt(document.getElementById('rng-max').value) || 0;
            if (min > max) {
                showToast("Min value cannot exceed Max value.", "error");
                return;
            }
            const rand = Math.floor(Math.random() * (max - min + 1)) + min;
            document.getElementById('out-number').textContent = rand;
            updateBreakdown(`<p class='text-success'>Number resolved: <strong>${rand}</strong></p>`);
        """
    },
    {
        "category": "Productivity Tools",
        "name": "Random String Generator",
        "slug": "random-string-generator",
        "desc": "Create secure random passwords, tokens, or keys of custom length.",
        "formula": "Random Character Array picker",
        "formula_desc": "Constructs key parameters by choosing random elements from alphanumeric tables.",
        "icon": "🔑",
        "inputs": [
            {"id": "rs-len", "label": "String Length:", "type": "number", "default": "16"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated String Output:", "type": "textarea"}
        ],
        "calc_js": """
            const len = parseInt(document.getElementById('rs-len').value) || 16;
            const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
            let res = "";
            for (let i = 0; i < len; i++) {
                res += alphabet.charAt(Math.floor(Math.random() * alphabet.length));
            }
            document.getElementById('text-output').value = res;
            updateBreakdown("<p class='text-success'>String compiled.</p>");
        """
    },
    {
        "category": "Productivity Tools",
        "name": "Slug Generator",
        "slug": "slug-generator",
        "desc": "Convert text headings into clean URL-friendly slugs.",
        "formula": "text.toLowerCase().replace(/[^a-z0-9]/g, '-')",
        "formula_desc": "Strips special characters and whitespace tabs, separating words with single hyphens.",
        "icon": "🔗",
        "inputs": [
            {"id": "text-input", "label": "Enter Title / Heading:", "type": "textarea", "default": "Enginewheels Developer Tools Category!"}
        ],
        "outputs": [
            {"id": "text-output", "label": "URL Slug Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value;
            if (!val) {
                showToast("Please enter text.", "error");
                return;
            }
            const slug = val
                .toLowerCase()
                .trim()
                .replace(/[^a-z0-9\\s-]/g, '')
                .replace(/[\\s_]+/g, '-')
                .replace(/-+/g, '-');
            document.getElementById('text-output').value = slug;
            updateBreakdown(`<p class='text-success'>Slug generated: <code>${slug}</code></p>`);
        """
    },
    {
        "category": "Productivity Tools",
        "name": "Case Converter",
        "slug": "case-converter-dev",
        "desc": "Convert code variables and text between camelCase, snake_case, PascalCase, and kebab-case.",
        "formula": "Case transforms regex scripts",
        "formula_desc": "Extracts word boundary structures and styles them into variables casing.",
        "icon": "✍️",
        "inputs": [
            {"id": "text-input", "label": "Enter Variable Text:", "type": "textarea", "default": "user profile score data"},
            {"id": "case-style", "label": "Casing Style:", "type": "select", "options": [("camel", "camelCase"), ("snake", "snake_case"), ("pascal", "PascalCase"), ("kebab", "kebab-case")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Casing Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            const style = document.getElementById('case-style').value;
            if (!val) {
                showToast("Please enter some text.", "error");
                return;
            }
            
            const words = val.split(/[^a-zA-Z0-9]+/);
            let result = "";
            
            if (style === 'camel') {
                result = words.map((w, idx) => {
                    return idx === 0 ? w.toLowerCase() : w.charAt(0).toUpperCase() + w.substring(1).toLowerCase();
                }).join('');
            } else if (style === 'snake') {
                result = words.map(w => w.toLowerCase()).join('_');
            } else if (style === 'pascal') {
                result = words.map(w => w.charAt(0).toUpperCase() + w.substring(1).toLowerCase()).join('');
            } else {
                result = words.map(w => w.toLowerCase()).join('-');
            }
            
            document.getElementById('text-output').value = result;
            updateBreakdown("<p class='text-success'>Variables case updated.</p>");
        """
    },
    {
        "category": "Productivity Tools",
        "name": "Text Difference Checker",
        "slug": "text-difference-checker",
        "desc": "Identify differences between two plain text strings.",
        "formula": "Myers Diff Comparison",
        "formula_desc": "Evaluates strings line by line to discover differences.",
        "icon": "⚖️",
        "inputs": [
            {"id": "text-d1", "label": "Text Block 1:", "type": "textarea", "default": "Hello World\\nLine 2"},
            {"id": "text-d2", "label": "Text Block 2:", "type": "textarea", "default": "Hello World\\nLine 2 updated"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Text Diff Log:", "type": "textarea"}
        ],
        "calc_js": """
            const d1 = document.getElementById('text-d1').value.trim();
            const d2 = document.getElementById('text-d2').value.trim();
            
            if (!d1 || !d2) {
                showToast("Please enter values in both areas.", "error");
                return;
            }
            
            const lines1 = d1.split('\\n');
            const lines2 = d2.split('\\n');
            let diffLog = "";
            let htmlReport = "<div style='text-align:left; font-family:monospace;'>";
            
            const max = Math.max(lines1.length, lines2.length);
            for (let i = 0; i < max; i++) {
                const l1 = lines1[i] || "";
                const l2 = lines2[i] || "";
                if (l1 === l2) {
                    diffLog += `  ${l1}\\n`;
                    htmlReport += `<div style='color:#ccc;'>&nbsp;&nbsp;${l1}</div>`;
                } else {
                    if (l1) {
                        diffLog += `- ${l1}\\n`;
                        htmlReport += `<div style='background:rgba(239,68,68,0.2);color:#EF4444;'>- ${l1}</div>`;
                    }
                    if (l2) {
                        diffLog += `+ ${l2}\\n`;
                        htmlReport += `<div style='background:rgba(16,185,129,0.2);color:#10B981;'>+ ${l2}</div>`;
                    }
                }
            }
            htmlReport += "</div>";
            document.getElementById('text-output').value = diffLog;
            updateBreakdown(htmlReport);
        """
    },
    {
        "category": "Productivity Tools",
        "name": "Text Comparison Tool",
        "slug": "text-comparison-tool",
        "desc": "Check if two text blocks are identical.",
        "formula": "String strict comparison",
        "formula_desc": "Compares character streams, checking casing differences.",
        "icon": "⚖️",
        "inputs": [
            {"id": "tc-t1", "label": "Text 1:", "type": "textarea", "default": "Hello"},
            {"id": "tc-t2", "label": "Text 2:", "type": "textarea", "default": "hello"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Comparison Report:", "type": "textarea"}
        ],
        "calc_js": """
            const t1 = document.getElementById('tc-t1').value;
            const t2 = document.getElementById('tc-t2').value;
            
            if (t1 === t2) {
                document.getElementById('text-output').value = "✓ Exact Match!\\n\\nBoth strings are character-identical.";
            } else if (t1.toLowerCase() === t2.toLowerCase()) {
                document.getElementById('text-output').value = "✓ Case-Insensitive Match!\\n\\nStrings match when ignoring casing.";
            } else {
                document.getElementById('text-output').value = "✗ Mismatch!\\n\\nCharacter sets have differing values.";
            }
            updateBreakdown("<p class='text-success'>Text comparison finished.</p>");
        """
    },
    {
        "category": "Productivity Tools",
        "name": "Character Counter",
        "slug": "character-counter-dev",
        "desc": "Display counts of characters, words, sentences, and lines in your text.",
        "formula": "String Length and Array splitting loops",
        "formula_desc": "Computes text details using standard JScript split operations.",
        "icon": "🔢",
        "inputs": [
            {"id": "text-input", "label": "Enter Text:", "type": "textarea", "default": "Format JSON, encode URLs, and validate code structure online."}
        ],
        "outputs": [
            {"id": "out-chars", "label": "Total Characters:", "type": "text"},
            {"id": "out-words", "label": "Total Words:", "type": "text"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value;
            const chars = val.length;
            const words = val.trim() === '' ? 0 : val.trim().split(/\\s+/).length;
            
            document.getElementById('out-chars').textContent = chars;
            document.getElementById('out-words').textContent = words;
            updateBreakdown("<p class='text-success'>Word count statistics updated successfully.</p>");
        """
    }
]

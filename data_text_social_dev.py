# -*- coding: utf-8 -*-
"""
Social Media and Developer Text Tools Data
"""

SOCIAL_CALCS = [
    {
        "name": "Hashtag Generator",
        "slug": "hashtag-generator",
        "category": "Social Media Tools",
        "icon": "🏷️",
        "desc": "Generate relevant hashtags for Instagram, Twitter, and TikTok based on keywords.",
        "formula": "Hashtag mapping",
        "formula_desc": "Combines input words with popular social media category hash suffixes.",
        "inputs": [
            {"id": "text-input", "label": "Enter Keywords:", "type": "text", "default": "fitness travel"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Hashtags", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            if (text === '') {
                showToast("Please enter some keywords.", "error");
                return;
            }
            const words = text.toLowerCase().split(/[^a-zA-Z0-9]+/);
            let tags = [];
            for (let w of words) {
                if (w.length > 0) {
                    tags.push('#' + w);
                    tags.push('#' + w + 'life');
                    tags.push('#insta' + w);
                    tags.push('#' + w + '2026');
                }
            }
            document.getElementById('text-output').value = tags.join(' ');
            updateBreakdown(`<p>Generated ${tags.length} social tags from your input keywords.</p>`);
        """
    },
    {
        "name": "Instagram Caption Formatter",
        "slug": "instagram-caption-formatter",
        "category": "Social Media Tools",
        "icon": "📸",
        "desc": "Format Instagram captions with clean line breaks that will not collapse.",
        "formula": "Newline substitution",
        "formula_desc": "Replaces standard newlines with invisible space characters (U+200B/U+2800) to preserve IG layout.",
        "inputs": [
            {"id": "text-input", "label": "Enter Instagram Caption:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted Caption", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            // Replace standard newlines with invisible braille space
            const formatted = text.split('\\n').map(line => line === '' ? '⠀' : line).join('\\n');
            document.getElementById('text-output').value = formatted;
            updateBreakdown(`<p>Replaced blank lines with Braille spaces (U+2800) to prevent Instagram from collapsing paragraphs.</p>`);
        """
    },
    {
        "name": "Twitter Character Counter",
        "slug": "twitter-character-counter",
        "category": "Social Media Tools",
        "icon": "🐦",
        "desc": "Track your character counts against the Twitter/X 280 character limit limit.",
        "formula": "Chars = 280 - Text.length",
        "formula_desc": "Calculates remaining characters and highlights warnings if text exceeds 280 symbols.",
        "inputs": [
            {"id": "text-input", "label": "Enter Tweet text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Tweet Status", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const len = text.length;
            const remaining = 280 - len;
            let report = `Characters used: ${len} / 280\\n`;
            if (remaining >= 0) {
                report += `Status: Good! You have ${remaining} characters remaining.`;
            } else {
                report += `Status: Exceeded limit by ${Math.abs(remaining)} characters!`;
            }
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Twitter character limits target 280 characters for standard tweet posts.</p>`);
        """
    },
    {
        "name": "LinkedIn Post Formatter",
        "slug": "linkedin-post-formatter",
        "category": "Social Media Tools",
        "icon": "💼",
        "desc": "Format LinkedIn posts with emojis, clean lists, and line spacing.",
        "formula": "Readability spacing formatting",
        "formula_desc": "Formats posts with clean double spacing and lists to maximize post feed visibility.",
        "inputs": [
            {"id": "text-input", "label": "Enter LinkedIn Draft:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted Post", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const formatted = text.split('\\n').map(line => {
                if (line.trim().startsWith('-') || line.trim().startsWith('*')) {
                    return '🚀 ' + line.trim().substring(1).trim();
                }
                return line;
            }).join('\\n\\n');
            document.getElementById('text-output').value = formatted;
            updateBreakdown(`<p>Added double-spacing and replaced bullet lists with professional emojis.</p>`);
        """
    },
    {
        "name": "Facebook Text Formatter",
        "slug": "facebook-text-formatter",
        "category": "Social Media Tools",
        "icon": "👥",
        "desc": "Format Facebook posts with headers and call-to-action line spacings.",
        "formula": "FB visual formatting",
        "formula_desc": "Beautifies FB post draft layout for premium readability.",
        "inputs": [
            {"id": "text-input", "label": "Enter FB Draft:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const lines = text.split('\\n');
            let formatted = '';
            if (lines.length > 0) {
                formatted += '🔥 ' + lines[0].toUpperCase() + ' 🔥\\n\\n';
                formatted += lines.slice(1).join('\\n');
            }
            document.getElementById('text-output').value = formatted;
            updateBreakdown(`<p>Formatted the first line into a capitalized, high-impact header.</p>`);
        """
    },
    {
        "name": "Emoji Text Generator",
        "slug": "emoji-text-generator",
        "category": "Social Media Tools",
        "icon": "🎭",
        "desc": "Insert emojis between words or replace keywords with relevant emojis.",
        "formula": "Emoji key lookup substitution",
        "formula_desc": "Finds words like fire, rocket, star and appends emojis.",
        "inputs": [
            {"id": "text-input", "label": "Enter your Text:", "type": "textarea", "default": "This tool is fire and rocket speed."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Emoji Rich Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const map = {
                'fire': 'fire 🔥', 'rocket': 'rocket 🚀', 'star': 'star ⭐',
                'love': 'love ❤️', 'happy': 'happy 😊', 'cool': 'cool 😎',
                'money': 'money 💰', 'speed': 'speed ⚡', 'idea': 'idea 💡'
            };
            let result = text;
            for (let [word, emoji] of Object.entries(map)) {
                const regex = new RegExp('\\\\b' + word + '\\\\b', 'gi');
                result = result.replace(regex, emoji);
            }
            document.getElementById('text-output').value = result;
            updateBreakdown(`<p>Replaced matching sentiment keywords with corresponding emojis.</p>`);
        """
    },
    {
        "name": "Fancy Text Generator",
        "slug": "fancy-text-generator",
        "category": "Social Media Tools",
        "icon": "✨",
        "desc": "Convert normal text to cool fancy styles for bio descriptions.",
        "formula": "Unicode index offset mapping",
        "formula_desc": "Swaps standard ASCII characters for their stylized Unicode symbol counterparts.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Stylize:", "type": "text", "default": "hello"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Fancy Text Styles", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            const script = "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩0123456789";
            const bubble = "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ⓪①②③④⑤⑥⑦⑧⑨";
            
            let s1 = '', s2 = '';
            for (let c of text) {
                const idx = normal.indexOf(c);
                if (idx !== -1) {
                    s1 += script.substring(idx * 2, idx * 2 + 2); // unicode surrogate pairs
                    s2 += bubble.substring(idx * 2, idx * 2 + 2);
                } else {
                    s1 += c;
                    s2 += c;
                }
            }
            document.getElementById('text-output').value = `Script Style:\\n${s1}\\n\\nBubble Style:\\n${s2}`;
            updateBreakdown(`<p>Transferred ASCII character arrays into stylized Unicode surrogate blocks.</p>`);
        """
    },
    {
        "name": "Stylish Font Generator",
        "slug": "stylish-font-generator",
        "category": "Social Media Tools",
        "icon": "🖋️",
        "desc": "Generate stylish unicode fonts for social media profiles.",
        "formula": "Unicode fonts offset mapping",
        "formula_desc": "Transforms letters to monospace, bold, and double-struck unicode styles.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text:", "type": "text", "default": "stylish"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Stylish Fonts", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
            const doubleStruck = "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ";
            
            let result = '';
            for (let c of text) {
                const idx = normal.indexOf(c);
                if (idx !== -1) {
                    result += doubleStruck.substring(idx * 2, idx * 2 + 2);
                } else {
                    result += c;
                }
            }
            document.getElementById('text-output').value = result;
            updateBreakdown(`<p>Mapped standard alphabet arrays into Double-Struck mathematical fonts.</p>`);
        """
    },
    {
        "name": "Unicode Text Generator",
        "slug": "unicode-text-generator",
        "category": "Social Media Tools",
        "icon": "🔣",
        "desc": "Convert standard text to gothic, script, and serif unicode fonts.",
        "formula": "Unicode lookup offset",
        "formula_desc": "Swaps alphabet inputs with gothic and script math character blocks.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text:", "type": "text", "default": "gothic"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Unicode Styles", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
            const gothic = "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅𝔒𝔇𝔈𝔉𝔊𝔏𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔𝔕𝔖𝔗𝔘𝔙𝔚𝔛𝔜𝔏"; // standard gothic block representations
            
            let result = '';
            for (let c of text) {
                const idx = normal.indexOf(c);
                if (idx !== -1) {
                    result += gothic.substring(idx * 2, idx * 2 + 2);
                } else {
                    result += c;
                }
            }
            document.getElementById('text-output').value = result;
            updateBreakdown(`<p>Swapped characters with gothic unicode font blocks.</p>`);
        """
    },
    {
        "name": "Text Decorator",
        "slug": "text-decorator",
        "category": "Social Media Tools",
        "icon": "🎀",
        "desc": "Decorate your text with unique border stars, arrows, and shapes.",
        "formula": "Prefix + Text + Suffix",
        "formula_desc": "Adds custom text decoration borders to the input text.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text:", "type": "text", "default": "welcome"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decorated Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const decorated = `★·.·´¯`·.·★ ${text} ★·.·´¯`·.·★\\n` +
                              `ミ⛧ ${text} ⛧彡\\n` +
                              `◦•●◉✿ ${text} ✿◉●•◦`;
            document.getElementById('text-output').value = decorated;
            updateBreakdown(`<p>Appended stylized text borders and emojis to decorate inputs.</p>`);
        """
    }
]

DEVELOPER_CALCS = [
    {
        "name": "JSON Formatter",
        "slug": "json-formatter",
        "category": "Developer Text Tools",
        "icon": "💻",
        "desc": "Validate, beautify, indent, or minify your raw JSON code.",
        "formula": "JSON.stringify(JSON.parse(Text), null, 2)",
        "formula_desc": "Parses the input string to confirm valid JSON, then formats it with custom indentation.",
        "inputs": [
            {"id": "text-input", "label": "Enter raw JSON:", "type": "textarea", "default": '{"name":"enginewheels","type":"tools"}'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted JSON Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            if (text === '') return;
            try {
                const parsed = JSON.parse(text);
                document.getElementById('text-output').value = JSON.stringify(parsed, null, 2);
                updateBreakdown(`<p style="color:var(--color-green)">✔ Valid JSON parsed successfully.</p>`);
            } catch (e) {
                document.getElementById('text-output').value = `Error: ${e.message}`;
                updateBreakdown(`<p style="color:var(--color-red)">❌ Invalid JSON syntax: ${e.message}</p>`);
            }
        """
    },
    {
        "name": "XML Formatter",
        "slug": "xml-formatter",
        "category": "Developer Text Tools",
        "icon": "📦",
        "desc": "Beautify and format messy XML documents with indentations.",
        "formula": "Regex XML parsing",
        "formula_desc": "Adds linebreaks and tab spacing around open, close, and self-closing tags.",
        "inputs": [
            {"id": "text-input", "label": "Enter raw XML:", "type": "textarea", "default": "<root><child>data</child></root>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted XML Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            let formatted = '';
            let indent = '';
            const tab = '  ';
            const nodes = text.replace(/>\\s*</g, '><').split(/>/);
            
            for (let node of nodes) {
                if (node === '') continue;
                node = node + '>';
                if (node.startsWith('</')) {
                    indent = indent.substring(tab.length);
                    formatted += indent + node + '\\n';
                } else if (node.startsWith('<') && !node.endsWith('/>') && !node.includes('</')) {
                    formatted += indent + node + '\\n';
                    indent += tab;
                } else {
                    formatted += indent + node + '\\n';
                }
            }
            document.getElementById('text-output').value = formatted.trim();
            updateBreakdown(`<p>Indented tags systematically using depth metrics.</p>`);
        """
    },
    {
        "name": "SQL Formatter",
        "slug": "sql-formatter",
        "category": "Developer Text Tools",
        "icon": "🗄️",
        "desc": "Beautify database queries by capitalizing SQL commands and keywords.",
        "formula": "Keyword capitalization",
        "formula_desc": "Capitalizes SQL terms and structures variables with indentations.",
        "inputs": [
            {"id": "text-input", "label": "Enter SQL query:", "type": "textarea", "default": "select id, name from users where active = 1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted SQL Query", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const keywords = ['select', 'from', 'where', 'and', 'or', 'insert', 'update', 'delete', 'join', 'left', 'right', 'on', 'group', 'by', 'order', 'limit'];
            let sql = text;
            for (let kw of keywords) {
                const regex = new RegExp('\\\\b' + kw + '\\\\b', 'gi');
                sql = sql.replace(regex, kw.toUpperCase());
            }
            // Basic line break formatting
            sql = sql.replace(/\\b(FROM|WHERE|AND|OR|LEFT JOIN|RIGHT JOIN|ORDER BY|GROUP BY)\\b/g, '\\n$1');
            document.getElementById('text-output').value = sql.trim();
            updateBreakdown(`<p>Capitalized key database statements and aligned query constraints.</p>`);
        """
    },
    {
        "name": "HTML Formatter",
        "slug": "html-formatter",
        "category": "Developer Text Tools",
        "icon": "🌐",
        "desc": "Clean and format HTML code with proper tag indentations.",
        "formula": "HTML tag sorting",
        "formula_desc": "Uses element tag splitting to format HTML pages.",
        "inputs": [
            {"id": "text-input", "label": "Enter raw HTML:", "type": "textarea", "default": "<div><p>hello</p></div>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted HTML", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            let formatted = '';
            let indent = '';
            const tab = '  ';
            const elements = text.replace(/>\\s*</g, '><').split(/>/);
            
            for (let el of elements) {
                if (el === '') continue;
                el = el + '>';
                if (el.startsWith('</')) {
                    indent = indent.substring(tab.length);
                    formatted += indent + el + '\\n';
                } else if (el.startsWith('<') && !el.endsWith('/>') && !el.includes('</') && !el.startsWith('<!')) {
                    formatted += indent + el + '\\n';
                    indent += tab;
                } else {
                    formatted += indent + el + '\\n';
                }
            }
            document.getElementById('text-output').value = formatted.trim();
            updateBreakdown(`<p>Beautified HTML tag indents locally.</p>`);
        """
    },
    {
        "name": "CSS Formatter",
        "slug": "css-formatter",
        "category": "Developer Text Tools",
        "icon": "🎨",
        "desc": "Format messy CSS style blocks with clean linebreaks and tab spacings.",
        "formula": "Brace and colon spacing replacement",
        "formula_desc": "Inserts spacing around curly braces and semicolons to format CSS rules.",
        "inputs": [
            {"id": "text-input", "label": "Enter raw CSS:", "type": "textarea", "default": "body{color:#fff;background:black;}"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted CSS Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            // Basic CSS formatting
            let formatted = text.replace(/\\s*\\{\\s*/g, ' {\\n  ');
            formatted = formatted.replace(/;\\s*/g, ';\\n  ');
            formatted = formatted.replace(/\\s*\\}\\s*/g, '\\n}\\n\\n');
            formatted = formatted.replace(/\\s*:\\s*/g, ': ');
            formatted = formatted.replace(/\\n\\s*\\n/g, '\\n');
            formatted = formatted.replace(/\\s*\\}\\s*$/g, '\\n}');
            
            document.getElementById('text-output').value = formatted.trim();
            updateBreakdown(`<p>Organized CSS properties and rules into formatted blocks.</p>`);
        """
    },
    {
        "name": "JavaScript Formatter",
        "slug": "javascript-formatter",
        "category": "Developer Text Tools",
        "icon": "⚙️",
        "desc": "Beautify JS scripts with consistent brace matching and semicolon splits.",
        "formula": "Syntax spacing formatting",
        "formula_desc": "Arranges line structures after curly braces and statement endings.",
        "inputs": [
            {"id": "text-input", "label": "Enter raw JS:", "type": "textarea", "default": "function test(){console.log('hi');}"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted JavaScript", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            // Basic formatting
            let formatted = text.replace(/\\s*\\{\\s*/g, ' {\\n  ');
            formatted = formatted.replace(/;\\s*/g, ';\\n  ');
            formatted = formatted.replace(/\\s*\\}\\s*/g, '\\n}\\n');
            formatted = formatted.replace(/\\n\\s*\\n/g, '\\n');
            document.getElementById('text-output').value = formatted.trim();
            updateBreakdown(`<p>Indented code blocks based on curly brace boundaries.</p>`);
        """
    },
    {
        "name": "Markdown Formatter",
        "slug": "markdown-formatter",
        "category": "Developer Text Tools",
        "icon": "📝",
        "desc": "Standardize Markdown files by fixing blank spacing under headers.",
        "formula": "Standard Markdown rules",
        "formula_desc": "Cleans headings and checks spacing around lists and blockquotes.",
        "inputs": [
            {"id": "text-input", "label": "Enter raw Markdown:", "type": "textarea", "default": "# Header\\nsome text\\n## Subheader"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted MD", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            // Ensure single empty line before headers
            let formatted = text.replace(/\\n*(#+ )/g, '\\n\\n$1');
            formatted = formatted.replace(/^\\n\\n/, ''); // clean top
            document.getElementById('text-output').value = formatted;
            updateBreakdown(`<p>Normalized empty line gaps surrounding title markers.</p>`);
        """
    },
    {
        "name": "YAML Formatter",
        "slug": "yaml-formatter",
        "category": "Developer Text Tools",
        "icon": "📋",
        "desc": "Check and format YAML files, correcting indentations and key-value margins.",
        "formula": "YAML key-value format parsing",
        "formula_desc": "Validates indentation properties on YAML config configurations.",
        "inputs": [
            {"id": "text-input", "label": "Enter raw YAML:", "type": "textarea", "default": "name: enginewheels\\ntools:\\n- word-counter"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted YAML", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            const lines = text.split('\\n');
            let formatted = lines.map(line => {
                if (line.includes(':')) {
                    const idx = line.indexOf(':');
                    const key = line.substring(0, idx).trimEnd();
                    const val = line.substring(idx + 1).trim();
                    return key + ': ' + val;
                }
                return line;
            }).join('\\n');
            document.getElementById('text-output').value = formatted;
            updateBreakdown(`<p>Standardized space gaps surrounding colon dividers.</p>`);
        """
    },
    {
        "name": "CSV Formatter",
        "slug": "csv-formatter",
        "category": "Developer Text Tools",
        "icon": "📊",
        "desc": "Convert raw CSV files into cleanly formatted Markdown tables.",
        "formula": "CSV table formatting",
        "formula_desc": "Parses comma values and outputs markdown table syntax.",
        "inputs": [
            {"id": "text-input", "label": "Enter raw CSV data:", "type": "textarea", "default": "Name,Role,Status\\nAntigravity,AI Agent,Active\\nUser,Partner,Active"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Markdown Table Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            if (text === '') return;
            const lines = text.split('\\n');
            let mdTable = '';
            
            for (let i = 0; i < lines.length; i++) {
                const cols = lines[i].split(',').map(c => c.trim());
                mdTable += '| ' + cols.join(' | ') + ' |\\n';
                if (i === 0) {
                    mdTable += '| ' + cols.map(() => '---').join(' | ') + ' |\\n';
                }
            }
            document.getElementById('text-output').value = mdTable;
            updateBreakdown(`<p>Transformed CSV database lines into Markdown table elements.</p>`);
        """
    },
    {
        "name": "TSV Formatter",
        "slug": "tsv-formatter",
        "category": "Developer Text Tools",
        "icon": "📋",
        "desc": "Convert TSV (tab-separated values) data into formatted Markdown tables.",
        "formula": "TSV table formatting",
        "formula_desc": "Parses tab-delimited cells into column rows.",
        "inputs": [
            {"id": "text-input", "label": "Enter raw TSV data:", "type": "textarea", "default": "Name\\tRole\\tStatus\\nAntigravity\\tAI Agent\\tActive"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Markdown Table Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            if (text === '') return;
            const lines = text.split('\\n');
            let mdTable = '';
            
            for (let i = 0; i < lines.length; i++) {
                const cols = lines[i].split('\\t').map(c => c.trim());
                mdTable += '| ' + cols.join(' | ') + ' |\\n';
                if (i === 0) {
                    mdTable += '| ' + cols.map(() => '---').join(' | ') + ' |\\n';
                }
            }
            document.getElementById('text-output').value = mdTable;
            updateBreakdown(`<p>Transformed tab-separated entries into clean tables.</p>`);
        """
    }
]

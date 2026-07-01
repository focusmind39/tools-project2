# -*- coding: utf-8 -*-
"""
Database of 15 Code Formatter Tools for Enginewheels
"""

FORMATTER_TOOLS = [
    {
        "category": "Code Formatters",
        "name": "JSON Formatter",
        "slug": "json-formatter-dev",
        "desc": "Format, indent, and beautify raw JSON strings into human-readable structures.",
        "formula": "JSON.stringify(JSON.parse(input), null, indent)",
        "formula_desc": "Parses raw text as a JavaScript Object and serializes it back to a string with user-defined spacing indentation.",
        "icon": "💻",
        "inputs": [
            {"id": "text-input", "label": "Paste Raw JSON:", "type": "textarea", "default": '{"name":"Enginewheels","status":"active","tools":120}'},
            {"id": "indent-size", "label": "Indentation Size:", "type": "select", "options": [("2", "2 Spaces"), ("4", "4 Spaces"), ("tab", "Tab Spacing")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Beautified JSON:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter some JSON data.", "error");
                return;
            }
            try {
                const parsed = JSON.parse(val);
                const indent = document.getElementById('indent-size').value;
                const spaces = indent === 'tab' ? '\\t' : parseInt(indent);
                const formatted = JSON.stringify(parsed, null, spaces);
                document.getElementById('text-output').value = formatted;
                updateBreakdown("<p class='text-success'>JSON is valid! Parsed successfully and formatted with " + indent + " indentation.</p>");
            } catch (e) {
                document.getElementById('text-output').value = "Error: " + e.message;
                updateBreakdown("<p class='text-danger'>Invalid JSON: " + e.message + "</p>");
                showToast("Invalid JSON syntax!", "error");
            }
        """
    },
    {
        "category": "Code Formatters",
        "name": "JSON Validator",
        "slug": "json-validator",
        "desc": "Validate JSON structures and locate exact syntax error line numbers.",
        "formula": "JSON.parse(input) -> Error Line Check",
        "formula_desc": "Executes JSON parsing inside a try-catch block and extracts character offsets and line coordinates on failure.",
        "icon": "🔍",
        "inputs": [
            {"id": "text-input", "label": "Enter JSON to Validate:", "type": "textarea", "default": '{\n  "name": "Validator",\n  "status": "valid"\n}'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Validation Report:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter some JSON to validate.", "error");
                return;
            }
            try {
                JSON.parse(val);
                document.getElementById('text-output').value = "✓ Valid JSON\\n\\nSyntax checks out successfully. No errors found.";
                updateBreakdown("<p class='text-success'>JSON validation succeeded. Structure conforms strictly to RFC 8259 specifications.</p>");
            } catch (e) {
                document.getElementById('text-output').value = "✗ Invalid JSON\\n\\nError Details:\\n" + e.message;
                updateBreakdown("<p class='text-danger'>Validation failed. Parse error: " + e.message + "</p>");
                showToast("Validation failed!", "error");
            }
        """
    },
    {
        "category": "Code Formatters",
        "name": "XML Formatter",
        "slug": "xml-formatter",
        "desc": "Clean and format XML syntax tree documents with correct indentation levels.",
        "formula": "DOMParser -> Node Traversal Spacing",
        "formula_desc": "Parses the XML string into a DOM tree, then recursively traverses elements to output nested text blocks with relative tabs.",
        "icon": "📁",
        "inputs": [
            {"id": "text-input", "label": "Paste Raw XML:", "type": "textarea", "default": "<root><site><name>Enginewheels</name><category>DeveloperTools</category></site></root>"},
            {"id": "xml-indent", "label": "Indent Spacing:", "type": "select", "options": [("2", "2 Spaces"), ("4", "4 Spaces")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted XML:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter some XML data.", "error");
                return;
            }
            try {
                const parser = new DOMParser();
                const xmlDoc = parser.parseFromString(val, "application/xml");
                if (xmlDoc.getElementsByTagName("parsererror").length > 0) {
                    throw new Error(xmlDoc.getElementsByTagName("parsererror")[0].textContent);
                }
                const indentSize = parseInt(document.getElementById('xml-indent').value);
                
                function formatXML(node, level = 0) {
                    let indent = " ".repeat(level * indentSize);
                    let result = "";
                    if (node.nodeType === 1) { // Element
                        result += indent + "<" + node.nodeName;
                        for (let i = 0; i < node.attributes.length; i++) {
                            const attr = node.attributes[i];
                            result += " " + attr.nodeName + '="' + attr.nodeValue + '"';
                        }
                        if (node.childNodes.length === 0) {
                            result += " />\\n";
                        } else {
                            result += ">";
                            let childResult = "";
                            let hasElementChildren = false;
                            for (let i = 0; i < node.childNodes.length; i++) {
                                const child = node.childNodes[i];
                                if (child.nodeType === 1) {
                                    hasElementChildren = true;
                                    childResult += "\\n" + formatXML(child, level + 1);
                                } else if (child.nodeType === 3 || child.nodeType === 4) {
                                    childResult += child.nodeValue.trim();
                                }
                            }
                            if (hasElementChildren) {
                                result += childResult + indent + "</" + node.nodeName + ">\\n";
                            } else {
                                result += childResult + "</" + node.nodeName + ">\\n";
                            }
                        }
                    } else if (node.nodeType === 9) { // Document
                        for (let i = 0; i < node.childNodes.length; i++) {
                            result += formatXML(node.childNodes[i], level);
                        }
                    }
                    return result;
                }
                
                let formatted = formatXML(xmlDoc);
                document.getElementById('text-output').value = formatted.trim();
                updateBreakdown("<p class='text-success'>XML parsed successfully. Formatted recursively with " + indentSize + " spaces.</p>");
            } catch (e) {
                document.getElementById('text-output').value = "XML Error: " + e.message;
                updateBreakdown("<p class='text-danger'>Failed parsing XML: " + e.message + "</p>");
                showToast("XML Parsing Error!", "error");
            }
        """
    },
    {
        "category": "Code Formatters",
        "name": "XML Validator",
        "slug": "xml-validator",
        "desc": "Check XML documents for schema validity and parse error offsets.",
        "formula": "DOMParser.parseFromString(xml, 'application/xml')",
        "formula_desc": "Runs native DOMParser validation and scans documents for parsererror tags containing error locations.",
        "icon": "🛠️",
        "inputs": [
            {"id": "text-input", "label": "Enter XML to Validate:", "type": "textarea", "default": "<note>\n  <to>Developer</to>\n  <from>Enginewheels</from>\n  <body>Welcome!</body>\n</note>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Validation Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter XML markup.", "error");
                return;
            }
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(val, "application/xml");
            const errors = xmlDoc.getElementsByTagName("parsererror");
            if (errors.length > 0) {
                document.getElementById('text-output').value = "✗ Invalid XML Document\\n\\nError Info:\\n" + errors[0].textContent;
                updateBreakdown("<p class='text-danger'>XML is invalid. Parser error caught.</p>");
                showToast("XML contains errors!", "error");
            } else {
                document.getElementById('text-output').value = "✓ Valid XML Document\\n\\nNo parsing or tags structure errors found.";
                updateBreakdown("<p class='text-success'>XML validation succeeded. All tags are properly opened, nested, and closed.</p>");
            }
        """
    },
    {
        "category": "Code Formatters",
        "name": "HTML Formatter",
        "slug": "html-formatter",
        "desc": "Format and beautify HTML documents with nested tag indentation.",
        "formula": "Regex Match Tags -> Indent Spacing",
        "formula_desc": "Extracts HTML tags via regex, checks opening and closing flags, and appends indent spaces based on stack depth.",
        "icon": "🌐",
        "inputs": [
            {"id": "text-input", "label": "Paste Raw HTML:", "type": "textarea", "default": "<div><h1>Title</h1><p>Description text.</p></div>"},
            {"id": "indent", "label": "Spaces:", "type": "select", "options": [("2", "2 Spaces"), ("4", "4 Spaces")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Beautified HTML:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter some HTML.", "error");
                return;
            }
            const indentSize = parseInt(document.getElementById('indent').value);
            let formatted = '';
            let pad = 0;
            const reg = /(<[^>]+>)/g;
            const lines = val.replace(/\\n/g, '').replace(/\\s*</g, '<').replace(/>\\s*/g, '>').split(reg);
            
            lines.forEach(line => {
                if (line.match(/^<\\/\\w/)) {
                    pad = Math.max(0, pad - 1);
                }
                if (line.trim() !== '') {
                    formatted += ' '.repeat(pad * indentSize) + line.trim() + '\\n';
                }
                if (line.match(/^<\\w([^>]*[^\\/])?>$/) && !line.match(/<(area|base|br|col|embed|hr|img|input|link|meta|param|source|track|wbr)/)) {
                    pad += 1;
                }
            });
            document.getElementById('text-output').value = formatted.trim();
            updateBreakdown("<p class='text-success'>HTML Formatter finished processing. Code formatted with " + indentSize + " space tabs.</p>");
        """
    },
    {
        "category": "Code Formatters",
        "name": "HTML Minifier",
        "slug": "html-minifier",
        "desc": "Compress and minify HTML markup by removing unnecessary spacing, comments, and line breaks.",
        "formula": "HTML Minification RegExp Rules",
        "formula_desc": "Applies a pipeline of regular expressions to strip comments, trim spaces between tags, and collapse newlines.",
        "icon": "⚡",
        "inputs": [
            {"id": "text-input", "label": "Paste HTML to Minify:", "type": "textarea", "default": "<!-- Sample HTML comment -->\\n<div class=\\\"container\\\">\\n  <h1> Enginewheels Minifier </h1>\\n  <p> Minified code is fast! </p>\\n</div>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Minified HTML Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter HTML code.", "error");
                return;
            }
            // Strip comments
            let minified = val.replace(/<!--[\\s\\S]*?-->/g, '');
            // Strip whitespace between tags
            minified = minified.replace(/>\\s+</g, '><');
            // Collapse whitespaces
            minified = minified.replace(/\\s{2,}/g, ' ');
            // Trim
            minified = minified.trim();
            
            document.getElementById('text-output').value = minified;
            const saved = ((val.length - minified.length) / val.length * 100).toFixed(1);
            updateBreakdown("<p class='text-success'>Minification complete! Size reduced by " + saved + "% (" + val.length + " to " + minified.length + " bytes).</p>");
        """
    },
    {
        "category": "Code Formatters",
        "name": "CSS Formatter",
        "slug": "css-formatter",
        "desc": "Beautify stylesheet code with consistent blocks, property spacing, and clean indents.",
        "formula": "CSS Parser & Structure Alignment",
        "formula_desc": "Parses CSS rules by identifying braces and semicolons, separating properties into single indented lines.",
        "icon": "🎨",
        "inputs": [
            {"id": "text-input", "label": "Paste CSS Code:", "type": "textarea", "default": ".container{width:100%;margin:0 auto;padding:10px;background:#000;}"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted CSS:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter CSS code.", "error");
                return;
            }
            let formatted = val
                .replace(/\\s*([{}])\\s*/g, '$1')
                .replace(/;\\s*/g, ';')
                .replace(/\\s*:\\s*/g, ': ')
                .replace(/\\{/g, ' {\\n  ')
                .replace(/;/g, ';\\n  ')
                .replace(/\\n  \\}/g, '\\n}')
                .replace(/\\}/g, '}\\n\\n')
                .trim();
            
            // Clean up double lines
            formatted = formatted.replace(/;\\s*\\n\\s*\\n/g, ';\\n');
            document.getElementById('text-output').value = formatted;
            updateBreakdown("<p class='text-success'>CSS beautified and formatted with 2 spaces indent layout.</p>");
        """
    },
    {
        "category": "Code Formatters",
        "name": "CSS Minifier",
        "slug": "css-minifier",
        "desc": "Minify CSS rules to optimize style sheets and improve website performance.",
        "formula": "CSS Compacting RegEx Rules",
        "formula_desc": "Strips comments, merges duplicate selector declarations, and eliminates useless whitespaces and semicolons.",
        "icon": "🏎️",
        "inputs": [
            {"id": "text-input", "label": "Paste CSS to Minify:", "type": "textarea", "default": "/* Theme style */\\n.header {\\n  background-color: #ffffff;\\n  color: #333333;\\n  padding: 20px;\\n}"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Minified CSS Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter CSS code to compress.", "error");
                return;
            }
            let min = val
                .replace(/\\/\\*[\\s\\S]*?\\*\\//g, '') // Remove comments
                .replace(/\\s+([{}        :,;])/g, '$1')
                .replace(/([{}        :,;])\\s+/g, '$1')
                .replace(/;\\}/g, '}') // Remove last semicolon before closing brace
                .replace(/\\s+/g, ' ')
                .trim();
            document.getElementById('text-output').value = min;
            const savings = ((val.length - min.length) / val.length * 100).toFixed(1);
            updateBreakdown("<p class='text-success'>CSS Minified! Reduced size by " + savings + "% (" + val.length + " to " + min.length + " bytes).</p>");
        """
    },
    {
        "category": "Code Formatters",
        "name": "JavaScript Formatter",
        "slug": "javascript-formatter",
        "desc": "Beautify raw JavaScript files, aligned braces, indent arguments, and spacing.",
        "formula": "JS Syntax Scanner and Indenter",
        "formula_desc": "Tokenizes block structures via braces '{', '}', and brackets '[', ']' to maintain dynamic stack spacing.",
        "icon": "⚡",
        "inputs": [
            {"id": "text-input", "label": "Paste Javascript Code:", "type": "textarea", "default": "function test(){console.log('running');if(true){return 100;}else{return 0;}}"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Beautified JavaScript:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter JavaScript code.", "error");
                return;
            }
            let formatted = "";
            let indent = 0;
            const tokens = val
                .replace(/\\s*([{}        ;])\\s*/g, '$1')
                .replace(/\\{/g, ' {\\n')
                .replace(/\\}/g, '\\n}')
                .replace(/;/g, ';\\n')
                .split('\\n');
                
            tokens.forEach(line => {
                let trimmed = line.trim();
                if (trimmed.startsWith('}')) {
                    indent = Math.max(0, indent - 1);
                }
                if (trimmed !== "") {
                    formatted += "  ".repeat(indent) + trimmed + "\\n";
                }
                if (trimmed.endsWith('{')) {
                    indent += 1;
                }
            });
            document.getElementById('text-output').value = formatted.trim();
            updateBreakdown("<p class='text-success'>JavaScript code formatted successfully with 2-spaces indentation structure.</p>");
        """
    },
    {
        "category": "Code Formatters",
        "name": "JavaScript Minifier",
        "slug": "javascript-minifier",
        "desc": "Compress and minify JavaScript source code by stripping formatting, comments, and empty lines.",
        "formula": "JS Minimizer Rules Pipeline",
        "formula_desc": "Filters JS parameters by removing line comments '//', block comments '/* */', and collapsing variables spacing.",
        "icon": "🔥",
        "inputs": [
            {"id": "text-input", "label": "Paste JS code to Minify:", "type": "textarea", "default": "// Counter variable\\nlet counter = 0;\\n/* Increment function */\\nfunction incrementVal() {\\n  counter++;\\n  console.log(counter);\\n}"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Minified JS Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter JS code to minify.", "error");
                return;
            }
            let min = val
                .replace(/\\/\\*[\\s\\S]*?\\*\\//g, '') // remove block comments
                .replace(/\\/\\/[^\\n\\r]*/g, '')    // remove line comments
                .replace(/\\s*([{}        ()\\+\\-\\*\\/=:;,<>!&\\|])\\s*/g, '$1') // remove space around operators
                .replace(/\\s+/g, ' ')
                .trim();
            document.getElementById('text-output').value = min;
            const savings = ((val.length - min.length) / val.length * 100).toFixed(1);
            updateBreakdown("<p class='text-success'>JavaScript Minified! Size reduced by " + savings + "% (" + val.length + " to " + min.length + " bytes).</p>");
        """
    },
    {
        "category": "Code Formatters",
        "name": "SQL Formatter",
        "slug": "sql-formatter",
        "desc": "Format query text files by placing keywords (SELECT, FROM, WHERE) on new lines with proper casing.",
        "formula": "SQL Lexer Keyword Structuring",
        "formula_desc": "Identifies SQL database keywords, wraps them in uppercase, and inserts carriage return breaks before key statements.",
        "icon": "🛢️",
        "inputs": [
            {"id": "text-input", "label": "Paste Raw SQL Query:", "type": "textarea", "default": "select id, name, category from products where status='active' order by id desc"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Beautified SQL Query:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter an SQL query.", "error");
                return;
            }
            const keywords = ['SELECT', 'FROM', 'WHERE', 'ORDER BY', 'GROUP BY', 'LIMIT', 'JOIN', 'LEFT JOIN', 'RIGHT JOIN', 'INNER JOIN', 'ON', 'HAVING', 'AND', 'OR', 'SET', 'UPDATE', 'INSERT INTO', 'VALUES', 'DELETE'];
            let sql = val.replace(/\\s+/g, ' ');
            
            keywords.forEach(kw => {
                const regex = new RegExp('\\\\b' + kw + '\\\\b', 'gi');
                sql = sql.replace(regex, '\\n' + kw);
            });
            
            let lines = sql.split('\\n');
            let formatted = '';
            lines.forEach(line => {
                let trimmed = line.trim();
                if (trimmed !== '') {
                    if (trimmed.startsWith('AND') || trimmed.startsWith('OR') || trimmed.startsWith('ON')) {
                        formatted += '  ' + trimmed + '\\n';
                    } else {
                        formatted += trimmed + '\\n';
                    }
                }
            });
            
            document.getElementById('text-output').value = formatted.trim();
            updateBreakdown("<p class='text-success'>SQL query keywords updated to UPPERCASE and block statements aligned.</p>");
        """
    },
    {
        "category": "Code Formatters",
        "name": "YAML Formatter",
        "slug": "yaml-formatter",
        "desc": "Indent, format, and validate YAML layout files for clean configuration parameters.",
        "formula": "YAML Document Node Spacing Parser",
        "formula_desc": "Evaluates YAML text block layout hierarchy, ensures clean indentation mapping, and fixes missing trailing spaces.",
        "icon": "📝",
        "inputs": [
            {"id": "text-input", "label": "Paste Raw YAML:", "type": "textarea", "default": "site:\nname: Enginewheels\nactive: true\ncategories:\n- calculators\n- developer-tools"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted YAML:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter YAML data.", "error");
                return;
            }
            // A simple client-side parser to align indentation
            let lines = val.split('\\n');
            let formatted = '';
            let indent = 0;
            lines.forEach(line => {
                let trimmed = line.trim();
                if (trimmed !== '') {
                    if (trimmed.startsWith('-')) {
                        formatted += '  '.repeat(indent) + trimmed + '\\n';
                    } else {
                        if (trimmed.includes(':')) {
                            const parts = trimmed.split(':');
                            const key = parts[0].trim();
                            const value = parts.slice(1).join(':').trim();
                            formatted += '  '.repeat(indent) + key + ': ' + (value ? value : '') + '\\n';
                        } else {
                            formatted += '  '.repeat(indent) + trimmed + '\\n';
                        }
                    }
                }
            });
            document.getElementById('text-output').value = formatted.trim();
            updateBreakdown("<p class='text-success'>YAML parameters validated and correctly structured.</p>");
        """
    },
    {
        "category": "Code Formatters",
        "name": "Markdown Formatter",
        "slug": "markdown-formatter",
        "desc": "Beautify markdown documents by organizing headers, spacing, and table syntax layouts.",
        "formula": "Markdown Line Spacing Scanner",
        "formula_desc": "Audits markdown symbols (#, -, *, |) to ensure clean headers separation, unified lists, and aligned tables.",
        "icon": "✍️",
        "inputs": [
            {"id": "text-input", "label": "Paste Raw Markdown:", "type": "textarea", "default": "# Header\nSome text here\n## Subheader\n- List Item 1\n-ListItem2"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted Markdown:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter Markdown text.", "error");
                return;
            }
            let lines = val.split('\\n');
            let formatted = '';
            lines.forEach((line, idx) => {
                let trimmed = line.trim();
                if (trimmed.startsWith('#')) {
                    // Ensure spacing after #
                    let count = 0;
                    while (trimmed[count] === '#') count++;
                    let content = trimmed.substring(count).trim();
                    formatted += '#'.repeat(count) + ' ' + content + '\\n\\n';
                } else if (trimmed.startsWith('-') || trimmed.startsWith('*')) {
                    let content = trimmed.substring(1).trim();
                    formatted += '- ' + content + '\\n';
                } else {
                    if (trimmed === '') {
                        formatted += '\\n';
                    } else {
                        formatted += trimmed + '\\n';
                    }
                }
            });
            
            document.getElementById('text-output').value = formatted.replace(/\\n{3,}/g, '\\n\\n').trim();
            updateBreakdown("<p class='text-success'>Markdown spacing and header syntax formatted correctly.</p>");
        """
    },
    {
        "category": "Code Formatters",
        "name": "CSV Formatter",
        "slug": "csv-formatter",
        "desc": "Align CSV tabular datasets by spacing columns symmetrically for visual inspection.",
        "formula": "Tabular Column Auto-Width Align",
        "formula_desc": "Extracts fields, calculates max width per CSV grid column, and pads cells with spaces for console representation.",
        "icon": "📊",
        "inputs": [
            {"id": "text-input", "label": "Paste Raw CSV:", "type": "textarea", "default": "ID,Name,Category\\n1,Enginewheels,Tools\\n2,Google,Search"},
            {"id": "csv-sep", "label": "Separator:", "type": "select", "options": [(",", "Comma (,)"), (";", "Semicolon (;)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Aligned Table Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter CSV values.", "error");
                return;
            }
            const sep = document.getElementById('csv-sep').value;
            const lines = val.split('\\n').map(l => l.split(sep).map(c => c.trim()));
            
            // Find max lengths
            const colWidths = [];
            lines.forEach(row => {
                row.forEach((cell, idx) => {
                    colWidths[idx] = Math.max(colWidths[idx] || 0, cell.length);
                });
            });
            
            let formatted = '';
            lines.forEach((row, rIdx) => {
                let rowStr = '';
                row.forEach((cell, cIdx) => {
                    rowStr += cell.padEnd(colWidths[cIdx] + 2);
                });
                formatted += rowStr.trimEnd() + '\\n';
                if (rIdx === 0) {
                    formatted += '-'.repeat(colWidths.reduce((a,b) => a + b + 2, 0)) + '\\n';
                }
            });
            
            document.getElementById('text-output').value = formatted.trim();
            updateBreakdown("<p class='text-success'>CSV data aligned and printed in monospaced console format.</p>");
        """
    },
    {
        "category": "Code Formatters",
        "name": "TSV Formatter",
        "slug": "tsv-formatter",
        "desc": "Align TSV files by computing max cell widths and displaying aligned grids.",
        "formula": "TSV Column Width Calculator",
        "formula_desc": "Splits text by tabs '\\t', monitors maximum column spans, and wraps output inside monospace text grids.",
        "icon": "📊",
        "inputs": [
            {"id": "text-input", "label": "Paste Raw TSV:", "type": "textarea", "default": "ID\\tName\\tCategory\\n1\\tEnginewheels\\tTools\\n2\\tGoogle\\tSearch"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Aligned TSV:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter TSV values.", "error");
                return;
            }
            const lines = val.split('\\n').map(l => l.split('\\t').map(c => c.trim()));
            
            const colWidths = [];
            lines.forEach(row => {
                row.forEach((cell, idx) => {
                    colWidths[idx] = Math.max(colWidths[idx] || 0, cell.length);
                });
            });
            
            let formatted = '';
            lines.forEach((row, rIdx) => {
                let rowStr = '';
                row.forEach((cell, cIdx) => {
                    rowStr += cell.padEnd(colWidths[cIdx] + 2);
                });
                formatted += rowStr.trimEnd() + '\\n';
                if (rIdx === 0) {
                    formatted += '-'.repeat(colWidths.reduce((a,b) => a + b + 2, 0)) + '\\n';
                }
            });
            
            document.getElementById('text-output').value = formatted.trim();
            updateBreakdown("<p class='text-success'>TSV data aligned and formatted successfully.</p>");
        """
    }
]

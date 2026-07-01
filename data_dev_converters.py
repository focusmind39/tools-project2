# -*- coding: utf-8 -*-
"""
Database of 10 Code Converter Tools for Enginewheels
"""

CONVERTER_TOOLS = [
    {
        "category": "Code Converters",
        "name": "JSON to CSV Converter",
        "slug": "json-to-csv-converter",
        "desc": "Convert JSON array data into structured CSV spreadsheet files.",
        "formula": "JSON -> Table Keys -> CSV Cells",
        "formula_desc": "Parses input JSON array, extracts all unique keys as CSV column headers, and appends cell data rows separated by commas.",
        "icon": "🔄",
        "inputs": [
            {"id": "text-input", "label": "Paste JSON Array:", "type": "textarea", "default": '[\n  {"id": 1, "name": "Alice", "role": "Dev"},\n  {"id": 2, "name": "Bob", "role": "PM"}\n]'}
        ],
        "outputs": [
            {"id": "text-output", "label": "CSV Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter JSON data.", "error");
                return;
            }
            try {
                let obj = JSON.parse(val);
                if (!Array.isArray(obj)) {
                    obj = [obj];
                }
                const headers = Array.from(new Set(obj.flatMap(item => Object.keys(item))));
                let csv = headers.join(',') + '\\n';
                obj.forEach(item => {
                    let row = headers.map(header => {
                        let cell = item[header] === undefined ? '' : item[header];
                        let cellStr = typeof cell === 'object' ? JSON.stringify(cell) : String(cell);
                        if (cellStr.includes(',') || cellStr.includes('"') || cellStr.includes('\\n')) {
                            cellStr = '"' + cellStr.replace(/"/g, '""') + '"';
                        }
                        return cellStr;
                    });
                    csv += row.join(',') + '\\n';
                });
                document.getElementById('text-output').value = csv.trim();
                updateBreakdown("<p class='text-success'>Successfully converted JSON array to CSV data. Extracted headers: " + headers.join(', ') + "</p>");
            } catch (e) {
                document.getElementById('text-output').value = "Conversion Error: " + e.message;
                updateBreakdown("<p class='text-danger'>Could not convert JSON: " + e.message + "</p>");
                showToast("Invalid JSON syntax!", "error");
            }
        """
    },
    {
        "category": "Code Converters",
        "name": "CSV to JSON Converter",
        "slug": "csv-to-json-converter",
        "desc": "Translate comma-separated CSV rows into clean JSON object arrays.",
        "formula": "CSV Headers -> Rows Iteration -> JSON Objects",
        "formula_desc": "Parses CSV by separator, reads the first row as column headers, and constructs an array of key-value JSON objects.",
        "icon": "🔄",
        "inputs": [
            {"id": "text-input", "label": "Paste CSV Data:", "type": "textarea", "default": "id,name,role\n1,Alice,Dev\n2,Bob,PM"}
        ],
        "outputs": [
            {"id": "text-output", "label": "JSON Array Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter CSV data.", "error");
                return;
            }
            try {
                const lines = val.split('\\n').map(l => l.split(',').map(c => c.trim()));
                if (lines.length < 2) {
                    throw new Error("CSV must contain at least headers and one data row.");
                }
                const headers = lines[0];
                const jsonArr = [];
                for (let i = 1; i < lines.length; i++) {
                    const row = lines[i];
                    if (row.length === 1 && row[0] === '') continue; // Skip empty lines
                    const obj = {};
                    headers.forEach((header, idx) => {
                        let cell = row[idx] === undefined ? '' : row[idx];
                        // Try to parse numbers or booleans
                        if (cell.toLowerCase() === 'true') cell = true;
                        else if (cell.toLowerCase() === 'false') cell = false;
                        else if (!isNaN(cell) && cell !== '') cell = Number(cell);
                        obj[header] = cell;
                    });
                    jsonArr.push(obj);
                }
                document.getElementById('text-output').value = JSON.stringify(jsonArr, null, 2);
                updateBreakdown("<p class='text-success'>CSV successfully parsed into JSON array of " + jsonArr.length + " objects.</p>");
            } catch (e) {
                document.getElementById('text-output').value = "Parsing Error: " + e.message;
                updateBreakdown("<p class='text-danger'>CSV Parsing failed: " + e.message + "</p>");
                showToast("CSV Syntax Error!", "error");
            }
        """
    },
    {
        "category": "Code Converters",
        "name": "XML to JSON Converter",
        "slug": "xml-to-json-converter",
        "desc": "Convert XML documents into hierarchical JSON tree objects.",
        "formula": "XML DOM Document -> Recursive Node Traversal",
        "formula_desc": "Converts DOM structures dynamically by mapping nodes to JSON dictionary keys, aggregating child tags into lists.",
        "icon": "🔄",
        "inputs": [
            {"id": "text-input", "label": "Paste XML Data:", "type": "textarea", "default": "<site>\n  <name>Enginewheels</name>\n  <status>Active</status>\n</site>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "JSON Tree Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter XML data.", "error");
                return;
            }
            try {
                const parser = new DOMParser();
                const xmlDoc = parser.parseFromString(val, "application/xml");
                if (xmlDoc.getElementsByTagName("parsererror").length > 0) {
                    throw new Error(xmlDoc.getElementsByTagName("parsererror")[0].textContent);
                }
                
                function xmlToJson(node) {
                    let obj = {};
                    if (node.nodeType === 1) { // Element
                        if (node.attributes.length > 0) {
                            obj["@attributes"] = {};
                            for (let j = 0; j < node.attributes.length; j++) {
                                const attribute = node.attributes.item(j);
                                obj["@attributes"][attribute.nodeName] = attribute.nodeValue;
                            }
                        }
                    } else if (node.nodeType === 3) { // Text
                        obj = node.nodeValue;
                    }
                    
                    if (node.hasChildNodes()) {
                        for (let i = 0; i < node.childNodes.length; i++) {
                            const item = node.childNodes.item(i);
                            const nodeName = item.nodeName;
                            if (nodeName === "#text") {
                                const txtVal = item.nodeValue.trim();
                                if (txtVal) obj = txtVal;
                            } else {
                                if (obj[nodeName] === undefined) {
                                    obj[nodeName] = xmlToJson(item);
                                } else {
                                    if (!Array.isArray(obj[nodeName])) {
                                        const old = obj[nodeName];
                                        obj[nodeName] = [];
                                        obj[nodeName].push(old);
                                    }
                                    obj[nodeName].push(xmlToJson(item));
                                }
                            }
                        }
                    }
                    return obj;
                }
                
                const json = xmlToJson(xmlDoc.documentElement);
                const result = {};
                result[xmlDoc.documentElement.nodeName] = json;
                document.getElementById('text-output').value = JSON.stringify(result, null, 2);
                updateBreakdown("<p class='text-success'>Successfully converted XML node mappings to JSON.</p>");
            } catch (e) {
                document.getElementById('text-output').value = "XML Error: " + e.message;
                updateBreakdown("<p class='text-danger'>Could not map XML elements: " + e.message + "</p>");
                showToast("XML parse error!", "error");
            }
        """
    },
    {
        "category": "Code Converters",
        "name": "JSON to XML Converter",
        "slug": "json-to-xml-converter",
        "desc": "Generate custom XML document strings from JSON models.",
        "formula": "JSON Tree -> XML Tags Iteration",
        "formula_desc": "Recursively reads JSON key-value hierarchies and creates matching nested tag attributes.",
        "icon": "🔄",
        "inputs": [
            {"id": "text-input", "label": "Paste JSON Model:", "type": "textarea", "default": '{\n  "note": {\n    "to": "Developer",\n    "from": "Enginewheels",\n    "message": "Welcome"\n  }\n}'}
        ],
        "outputs": [
            {"id": "text-output", "label": "XML Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter JSON data.", "error");
                return;
            }
            try {
                const parsed = JSON.parse(val);
                
                function jsonToXml(obj, indent = 0) {
                    let xml = "";
                    let tabs = "  ".repeat(indent);
                    for (let key in obj) {
                        if (obj.hasOwnProperty(key)) {
                            let value = obj[key];
                            if (value instanceof Array) {
                                value.forEach(val => {
                                    xml += tabs + "<" + key + ">\\n";
                                    if (typeof val === 'object') {
                                        xml += jsonToXml(val, indent + 1);
                                    } else {
                                        xml += "  ".repeat(indent + 1) + val + "\\n";
                                    }
                                    xml += tabs + "</" + key + ">\\n";
                                });
                            } else if (typeof value === 'object' && value !== null) {
                                xml += tabs + "<" + key + ">\\n" + jsonToXml(value, indent + 1) + tabs + "</" + key + ">\\n";
                            } else {
                                xml += tabs + "<" + key + ">" + value + "</" + key + ">\\n";
                            }
                        }
                    }
                    return xml;
                }
                
                let result = "<?xml version=\\"1.0\\" encoding=\\"UTF-8\\" ?>\\n" + jsonToXml(parsed);
                document.getElementById('text-output').value = result.trim();
                updateBreakdown("<p class='text-success'>JSON structure mapped to XML layout successfully.</p>");
            } catch (e) {
                document.getElementById('text-output').value = "Error: " + e.message;
                updateBreakdown("<p class='text-danger'>JSON parsing failed: " + e.message + "</p>");
                showToast("Invalid JSON syntax!", "error");
            }
        """
    },
    {
        "category": "Code Converters",
        "name": "HTML to Markdown Converter",
        "slug": "html-to-markdown-converter",
        "desc": "Translate HTML elements (headers, lists, links) into clean Markdown files.",
        "formula": "HTML Tags Regex -> Markdown Symbols",
        "formula_desc": "Applies HTML parsing regex rules to transform markup structures into standard Markdown blocks.",
        "icon": "🔄",
        "inputs": [
            {"id": "text-input", "label": "Paste HTML Markup:", "type": "textarea", "default": "<h1>Welcome</h1>\n<p>This is a <strong>bold</strong> statement.</p>\n<ul>\n  <li>Item 1</li>\n</ul>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Markdown Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter HTML code.", "error");
                return;
            }
            let md = val
                .replace(/<h1>(.*?)<\\/h1>/gi, '# $1\\n\\n')
                .replace(/<h2>(.*?)<\\/h2>/gi, '## $1\\n\\n')
                .replace(/<h3>(.*?)<\\/h3>/gi, '### $1\\n\\n')
                .replace(/<strong>(.*?)<\\/strong>/gi, '**$1**')
                .replace(/<b>(.*?)<\\/b>/gi, '**$1**')
                .replace(/<em>(.*?)<\\/em>/gi, '*$1*')
                .replace(/<i>(.*?)<\\/i>/gi, '*$1*')
                .replace(/<p>(.*?)<\\/p>/gi, '$1\\n\\n')
                .replace(/<li[^>]*>(.*?)<\\/li>/gi, '- $1\\n')
                .replace(/<ul[^>]*>([\\s\\S]*?)<\\/ul>/gi, '$1\\n')
                .replace(/<ol[^>]*>([\\s\\S]*?)<\\/ol>/gi, '$1\\n')
                .replace(/<a\\s+href=["'](.*?)["'][^>]*>(.*?)<\\/a>/gi, '[$2]($1)')
                .replace(/<br\\s*\\/?>/gi, '\\n')
                .replace(/<[^>]+>/g, '') // remove remaining HTML tags
                .replace(/\\n{3,}/g, '\\n\\n')
                .trim();
            
            document.getElementById('text-output').value = md;
            updateBreakdown("<p class='text-success'>HTML parsed and translated to standard Markdown format.</p>");
        """
    },
    {
        "category": "Code Converters",
        "name": "Markdown to HTML Converter",
        "slug": "markdown-to-html-converter",
        "desc": "Compile Markdown syntax sheets into clean HTML tags.",
        "formula": "Markdown Regex -> HTML tags",
        "formula_desc": "Scans for Markdown formatting patterns and wraps matching blocks inside HTML semantic containers.",
        "icon": "🔄",
        "inputs": [
            {"id": "text-input", "label": "Enter Markdown Text:", "type": "textarea", "default": "# Main Heading\nThis is a **bold** and *italic* sentence.\n\n[Enginewheels](https://enginewheels.com)"}
        ],
        "outputs": [
            {"id": "text-output", "label": "HTML Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter Markdown content.", "error");
                return;
            }
            let html = val
                .replace(/^# (.*?)$/gm, '<h1>$1</h1>')
                .replace(/^## (.*?)$/gm, '<h2>$2</h2>')
                .replace(/^### (.*?)$/gm, '<h3>$3</h3>')
                .replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>')
                .replace(/\\*(.*?)\\*/g, '<em>$1</em>')
                .replace(/\\[(.*?)\\]\\((.*?)\\)/g, '<a href="$2">$1</a>')
                .replace(/\\n\\n/g, '</p>\\n<p>')
                .trim();
                
            html = '<p>' + html + '</p>';
            // Clean up empty tags
            html = html.replace(/<p><h/g, '<h').replace(/<\\/h(\\d)><\\/p>/g, '</h$1>');
            document.getElementById('text-output').value = html;
            updateBreakdown("<p class='text-success'>Markdown parsed and compiled into standard HTML structure.</p>");
        """
    },
    {
        "category": "Code Converters",
        "name": "CSV to XML Converter",
        "slug": "csv-to-xml-converter",
        "desc": "Convert tabular CSV datasets into formatted XML files.",
        "formula": "CSV Line Split -> Headers Tag Matching",
        "formula_desc": "Constructs structured XML documents by mapping CSV column indexes to tag elements inside recursive structures.",
        "icon": "🔄",
        "inputs": [
            {"id": "text-input", "label": "Paste Raw CSV:", "type": "textarea", "default": "id,name,role\n1,Alice,Dev\n2,Bob,PM"}
        ],
        "outputs": [
            {"id": "text-output", "label": "XML Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter CSV data.", "error");
                return;
            }
            try {
                const lines = val.split('\\n').map(l => l.split(',').map(c => c.trim()));
                if (lines.length < 2) {
                    throw new Error("CSV requires a header line and at least one data row.");
                }
                const headers = lines[0].map(h => h.replace(/[^a-zA-Z0-9]/g, '_')); // safe XML tag names
                let xml = '<?xml version="1.0" encoding="UTF-8" ?>\\n<dataset>\\n';
                for (let i = 1; i < lines.length; i++) {
                    const row = lines[i];
                    if (row.length === 1 && row[0] === '') continue;
                    xml += '  <record>\\n';
                    headers.forEach((header, idx) => {
                        const cell = row[idx] === undefined ? '' : row[idx];
                        xml += '    <' + header + '>' + cell + '</' + header + '>\\n';
                    });
                    xml += '  </record>\\n';
                }
                xml += '</dataset>';
                document.getElementById('text-output').value = xml;
                updateBreakdown("<p class='text-success'>CSV translated into structured XML records.</p>");
            } catch (e) {
                document.getElementById('text-output').value = "Error: " + e.message;
                updateBreakdown("<p class='text-danger'>Failed mapping CSV: " + e.message + "</p>");
                showToast("CSV Parse Error", "error");
            }
        """
    },
    {
        "category": "Code Converters",
        "name": "XML to CSV Converter",
        "slug": "xml-to-csv-converter",
        "desc": "Translate XML list structures into CSV sheet matrices.",
        "formula": "XML DOM Parsing -> Flat Row Aggregate",
        "formula_desc": "Locates repeating child elements, parses nested values into flat lists, and exports them as standard CSV.",
        "icon": "🔄",
        "inputs": [
            {"id": "text-input", "label": "Paste XML Data:", "type": "textarea", "default": "<dataset>\n  <record>\n    <id>1</id>\n    <name>Alice</name>\n  </record>\n  <record>\n    <id>2</id>\n    <name>Bob</name>\n  </record>\n</dataset>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "CSV Tabular Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter XML.", "error");
                return;
            }
            try {
                const parser = new DOMParser();
                const xmlDoc = parser.parseFromString(val, "application/xml");
                if (xmlDoc.getElementsByTagName("parsererror").length > 0) {
                    throw new Error(xmlDoc.getElementsByTagName("parsererror")[0].textContent);
                }
                const records = xmlDoc.documentElement.children;
                if (records.length === 0) {
                    throw new Error("No record tags found under root element.");
                }
                
                const headers = Array.from(new Set(Array.from(records).flatMap(rec => Array.from(rec.children).map(c => c.nodeName))));
                let csv = headers.join(',') + '\\n';
                
                for (let i = 0; i < records.length; i++) {
                    const record = records[i];
                    const row = headers.map(header => {
                        const child = record.getElementsByTagName(header)[0];
                        let txt = child ? child.textContent.trim() : '';
                        if (txt.includes(',') || txt.includes('"') || txt.includes('\\n')) {
                            txt = '"' + txt.replace(/"/g, '""') + '"';
                        }
                        return txt;
                    });
                    csv += row.join(',') + '\\n';
                }
                document.getElementById('text-output').value = csv.trim();
                updateBreakdown("<p class='text-success'>XML parsed and flattened to CSV rows. Found " + records.length + " records.</p>");
            } catch (e) {
                document.getElementById('text-output').value = "Conversion Error: " + e.message;
                updateBreakdown("<p class='text-danger'>Conversion failed: " + e.message + "</p>");
                showToast("XML Parse Error!", "error");
            }
        """
    },
    {
        "category": "Code Converters",
        "name": "YAML to JSON Converter",
        "slug": "yaml-to-json-converter",
        "desc": "Translate YAML configuration text streams into parseable JSON trees.",
        "formula": "YAML Key-Value Parsing -> JSON Object",
        "formula_desc": "Tokenizes lines by colons ':' and indents space scales to construct equivalent JSON objects.",
        "icon": "🔄",
        "inputs": [
            {"id": "text-input", "label": "Paste YAML Data:", "type": "textarea", "default": "config:\n  app: Enginewheels\n  version: 2.1\n  debug: false"}
        ],
        "outputs": [
            {"id": "text-output", "label": "JSON Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter YAML data.", "error");
                return;
            }
            try {
                // A simple layout-matching parser for mapping YAML to JSON
                let lines = val.split('\\n');
                let result = {};
                let stack = [result];
                let currentIndent = 0;
                
                lines.forEach(line => {
                    let trimmed = line.trim();
                    if (trimmed === '' || trimmed.startsWith('#')) return;
                    let indent = line.length - line.trimStart().length;
                    
                    if (trimmed.includes(':')) {
                        let parts = trimmed.split(':');
                        let key = parts[0].trim();
                        let value = parts.slice(1).join(':').trim();
                        if (value === 'true') value = true;
                        else if (value === 'false') value = false;
                        else if (!isNaN(value) && value !== '') value = Number(value);
                        
                        if (indent > currentIndent) {
                            // Find latest parent key and build subobject
                            let keys = Object.keys(stack[stack.length - 1]);
                            let lastKey = keys[keys.length - 1];
                            let newObj = {};
                            stack[stack.length - 1][lastKey] = newObj;
                            stack.push(newObj);
                            currentIndent = indent;
                        } else if (indent < currentIndent) {
                            while (currentIndent > indent && stack.length > 1) {
                                stack.pop();
                                currentIndent -= 2; // assume 2 spaces
                            }
                        }
                        
                        stack[stack.length - 1][key] = value !== '' ? value : {};
                    }
                });
                
                document.getElementById('text-output').value = JSON.stringify(result, null, 2);
                updateBreakdown("<p class='text-success'>YAML mapped to JSON successfully.</p>");
            } catch (e) {
                document.getElementById('text-output').value = "Error parsing YAML: " + e.message;
                updateBreakdown("<p class='text-danger'>YAML mapping failed.</p>");
                showToast("YAML Parse Error", "error");
            }
        """
    },
    {
        "category": "Code Converters",
        "name": "JSON to YAML Converter",
        "slug": "json-to-yaml-converter",
        "desc": "Format JSON models as clean YAML indentation configs.",
        "formula": "JSON Iteration -> YAML Blocks",
        "formula_desc": "Scans Javascript objects recursively, writing formatted block variables with matching space indentations.",
        "icon": "🔄",
        "inputs": [
            {"id": "text-input", "label": "Paste JSON Model:", "type": "textarea", "default": '{\n  "app": {\n    "name": "Enginewheels",\n    "port": 8080\n  }\n}'}
        ],
        "outputs": [
            {"id": "text-output", "label": "YAML Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter JSON data.", "error");
                return;
            }
            try {
                const parsed = JSON.parse(val);
                
                function jsonToYaml(obj, indent = 0) {
                    let yaml = "";
                    let tabs = "  ".repeat(indent);
                    for (let key in obj) {
                        if (obj.hasOwnProperty(key)) {
                            let value = obj[key];
                            if (value instanceof Array) {
                                yaml += tabs + key + ":\\n";
                                value.forEach(item => {
                                    if (typeof item === 'object') {
                                        yaml += tabs + "  - \\n" + jsonToYaml(item, indent + 2);
                                    } else {
                                        yaml += tabs + "  - " + item + "\\n";
                                    }
                                });
                            } else if (typeof value === 'object' && value !== null) {
                                yaml += tabs + key + ":\\n" + jsonToYaml(value, indent + 1);
                            } else {
                                yaml += tabs + key + ": " + value + "\\n";
                            }
                        }
                    }
                    return yaml;
                }
                
                document.getElementById('text-output').value = jsonToYaml(parsed).trim();
                updateBreakdown("<p class='text-success'>JSON model serialized to YAML successfully.</p>");
            } catch (e) {
                document.getElementById('text-output').value = "JSON Error: " + e.message;
                updateBreakdown("<p class='text-danger'>Could not convert: " + e.message + "</p>");
                showToast("Invalid JSON syntax!", "error");
            }
        """
    }
]

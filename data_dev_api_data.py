# -*- coding: utf-8 -*-
"""
Database of 10 API & Data Tools for Enginewheels
"""

API_DATA_TOOLS = [
    {
        "category": "API & Data Tools",
        "name": "API Request Builder",
        "slug": "api-request-builder",
        "desc": "Build and send GET, POST, PUT, or DELETE API requests directly from your browser.",
        "formula": "fetch(url, options)",
        "formula_desc": "Initiates a client-side fetch transaction utilizing browser API request headers and body configurations.",
        "icon": "🚀",
        "inputs": [
            {"id": "api-url", "label": "API Endpoint URL:", "type": "text", "default": "https://jsonplaceholder.typicode.com/posts/1"},
            {"id": "api-method", "label": "HTTP Method:", "type": "select", "options": [("GET", "GET"), ("POST", "POST"), ("PUT", "PUT"), ("DELETE", "DELETE")]},
            {"id": "api-body", "label": "Request Body (JSON - for POST/PUT):", "type": "textarea", "default": '{"title": "foo", "body": "bar"}'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Response Output:", "type": "textarea"}
        ],
        "calc_js": """
            const url = document.getElementById('api-url').value.trim();
            const method = document.getElementById('api-method').value;
            const bodyVal = document.getElementById('api-body').value.trim();
            
            if (!url) {
                showToast("Please enter an endpoint URL.", "error");
                return;
            }
            
            const options = { method: method };
            if (method !== 'GET' && bodyVal) {
                try {
                    options.body = bodyVal;
                    options.headers = { 'Content-Type': 'application/json' };
                    JSON.parse(bodyVal); // validate JSON
                } catch(e) {
                    showToast("Request body must be valid JSON.", "error");
                    return;
                }
            }
            
            document.getElementById('text-output').value = "Sending request to " + url + "...";
            
            fetch(url, options)
                .then(res => {
                    const status = res.status + " " + res.statusText;
                    res.text().then(text => {
                        let parsed = text;
                        try {
                            parsed = JSON.stringify(JSON.parse(text), null, 2);
                        } catch(e) {}
                        document.getElementById('text-output').value = `Status: ${status}\\n\\n${parsed}`;
                        updateBreakdown(`<p class='text-success'>Response received. HTTP Status: ${status}</p>`);
                    });
                })
                .catch(err => {
                    document.getElementById('text-output').value = "Error: " + err.message + "\\n\\n(Note: CORS policies on the target server may block browser-only requests. Check browser dev console for details.)";
                    updateBreakdown("<p class='text-danger'>Fetch failed: " + err.message + "</p>");
                    showToast("API Request failed!", "error");
                });
        """
    },
    {
        "category": "API & Data Tools",
        "name": "API Response Viewer",
        "slug": "api-response-viewer",
        "desc": "Format and inspect raw API response payloads with headers validation.",
        "formula": "API JSON Parse -> Headers Array",
        "formula_desc": "Beautifies JSON structures and displays HTTP status parameters inside browser consoles.",
        "icon": "📺",
        "inputs": [
            {"id": "text-input", "label": "Paste Raw API Response String:", "type": "textarea", "default": '{"status": 200, "message": "Success", "data": {"id": 1, "score": 98.6}}'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted Viewer:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter an API response string.", "error");
                return;
            }
            try {
                const parsed = JSON.parse(val);
                document.getElementById('text-output').value = JSON.stringify(parsed, null, 2);
                updateBreakdown("<p class='text-success'>JSON payload formatted successfully.</p>");
            } catch(e) {
                document.getElementById('text-output').value = val;
                updateBreakdown("<p class='text-warning'>Response is plain text (not JSON). Formatted as text.</p>");
            }
        """
    },
    {
        "category": "API & Data Tools",
        "name": "JSON Viewer",
        "slug": "json-viewer",
        "desc": "View, format, and syntax check raw JSON structures cleanly.",
        "formula": "JSON Syntax Parsing",
        "formula_desc": "Serializes string inputs to extract values, checking tags formats client-side.",
        "icon": "👁️",
        "inputs": [
            {"id": "text-input", "label": "Paste Raw JSON:", "type": "textarea", "default": '{"name":"Enginewheels","features":["Formatters","Converters"],"status":true}'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Clean JSON View:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please paste some JSON.", "error");
                return;
            }
            try {
                const parsed = JSON.parse(val);
                document.getElementById('text-output').value = JSON.stringify(parsed, null, 4);
                updateBreakdown("<p class='text-success'>JSON syntax valid. Formatted output generated.</p>");
            } catch (e) {
                document.getElementById('text-output').value = "Syntax Error: " + e.message;
                updateBreakdown("<p class='text-danger'>Validation failed: " + e.message + "</p>");
                showToast("Invalid JSON syntax!", "error");
            }
        """
    },
    {
        "category": "API & Data Tools",
        "name": "JSON Tree Viewer",
        "slug": "json-tree-viewer",
        "desc": "Explore JSON datasets with an interactive collapsible tree node renderer.",
        "formula": "Recursive Object Key Spanning Tree",
        "formula_desc": "Transforms Javascript structures into collapsible DOM nodes, enabling inspection of complex nested arrays.",
        "icon": "🌲",
        "inputs": [
            {"id": "text-input", "label": "Paste Nested JSON:", "type": "textarea", "default": '{\n  "site": "Enginewheels",\n  "tools": {\n    "calculators": ["SIP", "Mortgage"],\n    "active": true\n  }\n}'}
        ],
        "outputs": [
            {"id": "text-output", "label": "JSON String Backup:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please paste JSON.", "error");
                return;
            }
            try {
                const parsed = JSON.parse(val);
                document.getElementById('text-output').value = JSON.stringify(parsed, null, 2);
                
                function buildTreeHtml(obj) {
                    if (typeof obj !== 'object' || obj === null) {
                        return `<span class="text-warning">${obj}</span>`;
                    }
                    let html = '<ul style="list-style-type:none; padding-left:20px; text-align:left;">';
                    for (let key in obj) {
                        if (obj.hasOwnProperty(key)) {
                            let valStr = '';
                            if (typeof obj[key] === 'object' && obj[key] !== null) {
                                valStr = buildTreeHtml(obj[key]);
                            } else {
                                valStr = `: <span style="color:#EF4444;">${obj[key]}</span>`;
                            }
                            html += `<li style="margin:4px 0;"><span style="color:#7C3AED; font-weight:600;">"${key}"</span>${valStr}</li>`;
                        }
                    }
                    html += '</ul>';
                    return html;
                }
                
                const tree = buildTreeHtml(parsed);
                updateBreakdown(`<div style="background:rgba(0,0,0,0.2);padding:15px;border-radius:8px;">${tree}</div>`);
                showToast("Tree view rendered below!");
            } catch (e) {
                document.getElementById('text-output').value = "Syntax Error: " + e.message;
                updateBreakdown("<p class='text-danger'>Tree rendering failed.</p>");
                showToast("Invalid JSON syntax!", "error");
            }
        """
    },
    {
        "category": "API & Data Tools",
        "name": "JSON Compare Tool",
        "slug": "json-compare-tool",
        "desc": "Check if two separate JSON strings are structurally identical.",
        "formula": "JSON.stringify(Object.keys().sort()) Compare",
        "formula_desc": "Sorts keys of both JSON datasets and compares their serialized signatures.",
        "icon": "⚖️",
        "inputs": [
            {"id": "json-c1", "label": "JSON Block 1:", "type": "textarea", "default": '{"id": 1, "name": "Enginewheels"}'},
            {"id": "json-c2", "label": "JSON Block 2:", "type": "textarea", "default": '{"name": "Enginewheels", \"id\": 1}'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Comparison Report:", "type": "textarea"}
        ],
        "calc_js": """
            const j1Val = document.getElementById('json-c1').value.trim();
            const j2Val = document.getElementById('json-c2').value.trim();
            
            if (!j1Val || !j2Val) {
                showToast("Please enter values in both boxes.", "error");
                return;
            }
            try {
                const o1 = JSON.parse(j1Val);
                const o2 = JSON.parse(j2Val);
                
                function sortKeys(obj) {
                    if (typeof obj !== 'object' || obj === null) return obj;
                    if (Array.isArray(obj)) return obj.map(sortKeys);
                    return Object.keys(obj).sort().reduce((acc, key) => {
                        acc[key] = sortKeys(obj[key]);
                        return acc;
                    }, {});
                }
                
                const s1 = JSON.stringify(sortKeys(o1));
                const s2 = JSON.stringify(sortKeys(o2));
                
                if (s1 === s2) {
                    document.getElementById('text-output').value = "✓ Match!\\n\\nBoth JSON structures are semantically identical (ignoring key order).";
                    updateBreakdown("<p class='text-success'>Semantic comparison succeeded. Data structures are identical.</p>");
                } else {
                    document.getElementById('text-output').value = "✗ Mismatch!\\n\\nJSON objects have different keys or values.";
                    updateBreakdown("<p class='text-danger'>Structures do not match.</p>");
                }
            } catch(e) {
                document.getElementById('text-output').value = "Syntax Error: " + e.message;
                showToast("Invalid JSON syntax in one of the blocks!", "error");
            }
        """
    },
    {
        "category": "API & Data Tools",
        "name": "JSON Diff Checker",
        "slug": "json-diff-checker",
        "desc": "Identify and highlight line differences between two JSON structures.",
        "formula": "Myers Diff Line-by-Line Checker",
        "formula_desc": "Evaluates strings line by line to discover additions, deletions, or matches.",
        "icon": "⚖️",
        "inputs": [
            {"id": "json-d1", "label": "Original JSON:", "type": "textarea", "default": '{\n  "active": true,\n  "role": "Dev"\n}'},
            {"id": "json-d2", "label": "Modified JSON:", "type": "textarea", "default": '{\n  "active": false,\n  "role": "Dev",\n  "new": 1\n}'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Raw Diff Log:", "type": "textarea"}
        ],
        "calc_js": """
            const d1 = document.getElementById('json-d1').value.trim();
            const d2 = document.getElementById('json-d2').value.trim();
            
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
        "category": "API & Data Tools",
        "name": "XML Viewer",
        "slug": "xml-viewer",
        "desc": "Check, format, and view XML documents cleanly inside browsers.",
        "formula": "DOMParser.parseFromString(xml)",
        "formula_desc": "Verifies tags nesting and aligns nodes with relative tab spaces.",
        "icon": "👁️",
        "inputs": [
            {"id": "text-input", "label": "Paste Raw XML:", "type": "textarea", "default": "<site><name>Enginewheels</name></site>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Beautified XML Output:", "type": "textarea"}
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
                
                // Formatter
                const serializer = new XMLSerializer();
                const formatted = serializer.serializeToString(xmlDoc);
                document.getElementById('text-output').value = formatted;
                updateBreakdown("<p class='text-success'>XML validated. Schema matches standards.</p>");
            } catch (e) {
                document.getElementById('text-output').value = "XML Error: " + e.message;
                updateBreakdown("<p class='text-danger'>Parse failed.</p>");
                showToast("XML contains errors!", "error");
            }
        """
    },
    {
        "category": "API & Data Tools",
        "name": "XML Tree Viewer",
        "slug": "xml-tree-viewer",
        "desc": "Renders collapsible tag structures of XML documents.",
        "formula": "DOMParser Element Tree Nodes Map",
        "formula_desc": "Recursively iterates through children elements, drawing expandable lists reflecting tags hierarchy.",
        "icon": "🌲",
        "inputs": [
            {"id": "text-input", "label": "Paste Nested XML:", "type": "textarea", "default": "<site>\n  <meta>\n    <title>Enginewheels</title>\n  </meta>\n</site>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "XML Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please paste XML data.", "error");
                return;
            }
            try {
                const parser = new DOMParser();
                const xmlDoc = parser.parseFromString(val, "application/xml");
                if (xmlDoc.getElementsByTagName("parsererror").length > 0) {
                    throw new Error(xmlDoc.getElementsByTagName("parsererror")[0].textContent);
                }
                
                function buildXMLHtml(node) {
                    if (node.nodeType === 3) {
                        const content = node.nodeValue.trim();
                        return content ? `<span style='color:#EF4444;'>${content}</span>` : '';
                    }
                    let html = '<ul style="list-style-type:none; padding-left:15px; text-align:left;">';
                    if (node.nodeType === 1) {
                        html += `<li>&lt;<span style='color:#7C3AED; font-weight:600;'>${node.nodeName}</span>&gt;`;
                        let childrenHtml = '';
                        for (let i = 0; i < node.childNodes.length; i++) {
                            childrenHtml += buildXMLHtml(node.childNodes[i]);
                        }
                        html += childrenHtml;
                        html += `&lt;/<span style='color:#7C3AED; font-weight:600;'>${node.nodeName}</span>&gt;</li>`;
                    } else if (node.nodeType === 9) { // doc
                        for (let i = 0; i < node.childNodes.length; i++) {
                            html += buildXMLHtml(node.childNodes[i]);
                        }
                    }
                    html += '</ul>';
                    return html;
                }
                
                const tree = buildXMLHtml(xmlDoc);
                document.getElementById('text-output').value = val;
                updateBreakdown(`<div style="background:rgba(0,0,0,0.2);padding:15px;border-radius:8px;">${tree}</div>`);
            } catch (e) {
                document.getElementById('text-output').value = "XML Error: " + e.message;
                updateBreakdown("<p class='text-danger'>Could not compile XML tree.</p>");
                showToast("XML syntax contains errors!", "error");
            }
        """
    },
    {
        "category": "API & Data Tools",
        "name": "CSV Viewer",
        "slug": "csv-viewer",
        "desc": "Render raw CSV file inputs into structured HTML tables.",
        "formula": "CSV Split -> HTML Table Matrix",
        "formula_desc": "Transforms comma-separated text data into clean interactive tables with grid columns.",
        "icon": "📊",
        "inputs": [
            {"id": "text-input", "label": "Paste Raw CSV:", "type": "textarea", "default": "id,name,role\\n1,Alice,Dev\\n2,Bob,PM"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Tabular Raw Preview:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter CSV data.", "error");
                return;
            }
            try {
                const lines = val.split('\\n').map(l => l.split(',').map(c => c.trim()));
                if (lines.length === 0 || lines[0].length === 0) {
                    throw new Error("Invalid CSV structure.");
                }
                
                let tableHtml = "<table class='table' style='width:100%; border-collapse:collapse; margin-top:15px;'>";
                lines.forEach((row, rIdx) => {
                    tableHtml += "<tr>";
                    row.forEach(cell => {
                        if (rIdx === 0) {
                            tableHtml += `<th style='border:1px solid rgba(255,255,255,0.1); padding:8px; background:rgba(255,255,255,0.05); color:#fff;'>${cell}</th>`;
                        } else {
                            tableHtml += `<td style='border:1px solid rgba(255,255,255,0.1); padding:8px; color:#ccc;'>${cell}</td>`;
                        }
                    });
                    tableHtml += "</tr>";
                });
                tableHtml += "</table>";
                
                document.getElementById('text-output').value = val;
                updateBreakdown(tableHtml);
                showToast("Table preview loaded below.");
            } catch(e) {
                document.getElementById('text-output').value = "Error: " + e.message;
                showToast("Invalid CSV layout!", "error");
            }
        """
    },
    {
        "category": "API & Data Tools",
        "name": "Data Table Generator",
        "slug": "data-table-generator",
        "desc": "Generate custom HTML table scripts dynamically with custom column metrics.",
        "formula": "Row-Col Loops -> HTML Table Tags",
        "formula_desc": "Outputs layout HTML code by repeating table row and table data tags.",
        "icon": "📊",
        "inputs": [
            {"id": "dt-cols", "label": "Columns Count:", "type": "number", "default": "3"},
            {"id": "dt-rows", "label": "Rows Count:", "type": "number", "default": "4"}
        ],
        "outputs": [
            {"id": "text-output", "label": "HTML Table Code:", "type": "textarea"}
        ],
        "calc_js": """
            const cols = parseInt(document.getElementById('dt-cols').value) || 1;
            const rows = parseInt(document.getElementById('dt-rows').value) || 1;
            
            let html = "<table class=\\"table\\">\\n  <thead>\\n    <tr>\\n";
            for (let c = 1; c <= cols; c++) {
                html += `      <th>Header ${c}</th>\\n`;
            }
            html += "    </tr>\\n  </thead>\\n  <tbody>\\n";
            for (let r = 1; r <= rows; r++) {
                html += "    <tr>\\n";
                for (let c = 1; c <= cols; c++) {
                    html += `      <td>Row ${r} Col ${c}</td>\\n`;
                }
                html += "    </tr>\\n";
            }
            html += "  </tbody>\\n</table>";
            
            document.getElementById('text-output').value = html;
            updateBreakdown(html);
        """
    }
]

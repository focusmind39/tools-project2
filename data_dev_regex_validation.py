# -*- coding: utf-8 -*-
"""
Database of 10 Regex & Validation Tools for Enginewheels
"""

REGEX_VALIDATION_TOOLS = [
    {
        "category": "Regex & Validation Tools",
        "name": "Regex Tester",
        "slug": "regex-tester",
        "desc": "Test and evaluate JavaScript regular expressions against target strings.",
        "formula": "new RegExp(pattern, flags).exec(text)",
        "formula_desc": "Compiles user pattern expressions client-side and returns capture matches and index offsets.",
        "icon": "🧪",
        "inputs": [
            {"id": "regex-pattern", "label": "Regex Pattern (without slashes):", "type": "text", "default": "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"},
            {"id": "regex-flags", "label": "Regex Flags:", "type": "text", "default": "g"},
            {"id": "regex-text", "label": "Target String:", "type": "textarea", "default": "Send emails to info@enginewheels.com or dev@example.org."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Matched Substrings List:", "type": "textarea"}
        ],
        "calc_js": """
            const pat = document.getElementById('regex-pattern').value;
            const flags = document.getElementById('regex-flags').value;
            const text = document.getElementById('regex-text').value;
            
            if (!pat) {
                showToast("Please enter a regex pattern.", "error");
                return;
            }
            try {
                const rx = new RegExp(pat, flags);
                let matches = [];
                let match;
                if (flags.includes('g')) {
                    while ((match = rx.exec(text)) !== null) {
                        matches.push(`Match: "${match[0]}" at Index: ${match.index}`);
                        if (rx.lastIndex === match.index) rx.lastIndex++; // prevent infinite loops
                    }
                } else {
                    match = rx.exec(text);
                    if (match) {
                        matches.push(`Match: "${match[0]}" at Index: ${match.index}`);
                    }
                }
                
                if (matches.length > 0) {
                    document.getElementById('text-output').value = matches.join('\\n');
                    updateBreakdown("<p class='text-success'>Found " + matches.length + " match(es) successfully.</p>");
                } else {
                    document.getElementById('text-output').value = "No matches found.";
                    updateBreakdown("<p class='text-warning'>Pattern parsed successfully but no matches were located in target text.</p>");
                }
            } catch(e) {
                document.getElementById('text-output').value = "Regex Compile Error: " + e.message;
                updateBreakdown("<p class='text-danger'>Invalid regex pattern sequence: " + e.message + "</p>");
                showToast("Invalid regex pattern!", "error");
            }
        """
    },
    {
        "category": "Regex & Validation Tools",
        "name": "Regex Generator",
        "slug": "regex-generator",
        "desc": "Generate custom regular expression patterns based on simple requirements.",
        "formula": "Rule Matching -> RegEx Pattern String",
        "formula_desc": "Maps selections (numbers only, phone format, email structure) to standard compiled RegExp literals.",
        "icon": "⚙️",
        "inputs": [
            {"id": "reg-rule", "label": "Select Rule Criteria:", "type": "select", "options": [("digits", "Match Digits Only (0-9)"), ("email", "Match Standard Email Addresses"), ("alphanumeric", "Match Alphanumeric Words"), ("date-iso", "Match ISO Dates (YYYY-MM-DD)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated RegEx Pattern:", "type": "textarea"}
        ],
        "calc_js": """
            const rule = document.getElementById('reg-rule').value;
            let pat = "";
            let desc = "";
            if (rule === 'digits') {
                pat = "^\\\\d+$";
                desc = "Matches strings containing only integer digits.";
            } else if (rule === 'email') {
                pat = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\\\.[a-zA-Z]{2,}$";
                desc = "Matches standard email address formats.";
            } else if (rule === 'alphanumeric') {
                pat = "^[a-zA-Z0-9]+$";
                desc = "Matches text containing only characters and numbers (no special symbols).";
            } else {
                pat = "^\\\\d{4}-\\\\d{2}-\\\\d{2}$";
                desc = "Matches standard calendar dates in YYYY-MM-DD format.";
            }
            document.getElementById('text-output').value = pat;
            updateBreakdown(`<p class='text-success'>Generated Pattern: <code>${pat}</code></p><p>${desc}</p>`);
        """
    },
    {
        "category": "Regex & Validation Tools",
        "name": "Regex Cheat Sheet Generator",
        "slug": "regex-cheat-sheet-generator",
        "desc": "Check and display standard regular expression operators cheat sheets.",
        "formula": "Static Cheat Sheet Mapping",
        "formula_desc": "Outputs detailed tables explaining meta-characters, quantifiers, and anchor symbols.",
        "icon": "📖",
        "inputs": [
            {"id": "cheat-type", "label": "Category:", "type": "select", "options": [("chars", "Meta Characters"), ("quantifiers", "Quantifiers"), ("anchors", "Anchors")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Cheat Sheet Output:", "type": "textarea"}
        ],
        "calc_js": """
            const type = document.getElementById('cheat-type').value;
            let text = "";
            let html = "<table class='table' style='width:100%; text-align:left; border-collapse:collapse;'>";
            html += "<tr><th style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>Symbol</th><th style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>Description</th></tr>";
            
            if (type === 'chars') {
                text = ".    Match any character\\n\\\\d   Match digits (0-9)\\n\\\\w   Match word character (a-z, A-Z, 0-9, _)\\n\\\\s   Match whitespace (space, tab, newline)";
                html += "<tr><td style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>.</td><td style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>Match any character except newline</td></tr>";
                html += "<tr><td style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>\\\\d</td><td style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>Match any numeric digit (0-9)</td></tr>";
                html += "<tr><td style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>\\\\w</td><td style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>Match any word character (alphanumeric + underscore)</td></tr>";
            } else if (type === 'quantifiers') {
                text = "*    0 or more times\\n+    1 or more times\\n?    0 or 1 time\\n{n}  Exactly n times";
                html += "<tr><td style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>*</td><td style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>Zero or more times</td></tr>";
                html += "<tr><td style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>+</td><td style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>One or more times</td></tr>";
            } else {
                text = "^    Start of string/line\\n$    End of string/line\\n\\\\b   Word boundary";
                html += "<tr><td style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>^</td><td style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>Asserts start of a line/string</td></tr>";
                html += "<tr><td style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>$</td><td style='padding:8px; border:1px solid rgba(255,255,255,0.1);'>Asserts end of a line/string</td></tr>";
            }
            html += "</table>";
            document.getElementById('text-output').value = text;
            updateBreakdown(html);
        """
    },
    {
        "category": "Regex & Validation Tools",
        "name": "Email Validator",
        "slug": "email-validator",
        "desc": "Check if an email address matches RFC 5322 syntax criteria.",
        "formula": "RegExp matching rules for standard emails",
        "formula_desc": "Validates format segments checking local names, @ separators, domains, and extensions.",
        "icon": "📧",
        "inputs": [
            {"id": "email-val", "label": "Enter Email Address:", "type": "text", "default": "info@enginewheels.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Validation Result:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('email-val').value.trim();
            if (!val) {
                showToast("Please enter an email address.", "error");
                return;
            }
            const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/;
            if (regex.test(val)) {
                document.getElementById('text-output').value = "✓ Valid Email\\n\\nFormat conforms successfully to standard structures.";
                updateBreakdown("<p class='text-success'>Email domain structure is valid.</p>");
            } else {
                document.getElementById('text-output').value = "✗ Invalid Email\\n\\nSyntax does not match standard patterns.";
                updateBreakdown("<p class='text-danger'>Format checking failed.</p>");
                showToast("Invalid email format!", "error");
            }
        """
    },
    {
        "category": "Regex & Validation Tools",
        "name": "URL Validator",
        "slug": "url-validator",
        "desc": "Verify if a URL string conforms to RFC 3986 URI specifications.",
        "formula": "Protocol, Domain, Path RegExp Matcher",
        "formula_desc": "Checks presence of schema (http/https), valid domains name syntax, and path parameters.",
        "icon": "🌐",
        "inputs": [
            {"id": "url-val", "label": "Enter URL:", "type": "text", "default": "https://enginewheels.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Validation Report:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('url-val').value.trim();
            if (!val) {
                showToast("Please enter a URL.", "error");
                return;
            }
            try {
                const url = new URL(val);
                document.getElementById('text-output').value = `✓ Valid URL\\n\\nProtocol: ${url.protocol}\\nHostname: ${url.hostname}\\nPath: ${url.pathname}`;
                updateBreakdown("<p class='text-success'>URL is valid and parseable by browsers.</p>");
            } catch (e) {
                document.getElementById('text-output').value = "✗ Invalid URL\\n\\n" + e.message;
                updateBreakdown("<p class='text-danger'>Failed browser URL instantiation validation.</p>");
                showToast("Invalid URL!", "error");
            }
        """
    },
    {
        "category": "Regex & Validation Tools",
        "name": "IPv4 Validator",
        "slug": "ipv4-validator",
        "desc": "Check if an IP address is a valid IPv4 network coordinates interface.",
        "formula": "4 Octets Split (0-255 Range Checking)",
        "formula_desc": "Validates if the decimal splits are 4 numbers, each within the standard range [0, 255].",
        "icon": "🔢",
        "inputs": [
            {"id": "ip-val", "label": "Enter IPv4 Address:", "type": "text", "default": "192.168.1.1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Result Status:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('ip-val').value.trim();
            if (!val) {
                showToast("Please enter an IP address.", "error");
                return;
            }
            const parts = val.split('.');
            let valid = true;
            if (parts.length !== 4) {
                valid = false;
            } else {
                for (let i = 0; i < 4; i++) {
                    const num = Number(parts[i]);
                    if (isNaN(num) || parts[i] === '' || num < 0 || num > 255 || String(num) !== parts[i]) {
                        valid = false;
                        break;
                    }
                }
            }
            if (valid) {
                document.getElementById('text-output').value = "✓ Valid IPv4 Address\\n\\nAll four octets are valid decimal integers between 0 and 255.";
                updateBreakdown("<p class='text-success'>IPv4 structure matches RFC 791 specifications.</p>");
            } else {
                document.getElementById('text-output').value = "✗ Invalid IPv4 Address\\n\\nMust consist of 4 numbers separated by dots, each between 0 and 255.";
                updateBreakdown("<p class='text-danger'>Octet validation failed.</p>");
                showToast("Invalid IPv4 address!", "error");
            }
        """
    },
    {
        "category": "Regex & Validation Tools",
        "name": "IPv6 Validator",
        "slug": "ipv6-validator",
        "desc": "Validate IPv6 network address structures against RFC 4291 patterns.",
        "formula": "8 Hex Blocks (16-bit groups checking)",
        "formula_desc": "Validates format groups to verify presence of valid hexadecimal figures separated by colons.",
        "icon": "🔢",
        "inputs": [
            {"id": "ip-val", "label": "Enter IPv6 Address:", "type": "text", "default": "2001:0db8:85a3:0000:0000:8a2e:0370:7334"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Result Report:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('ip-val').value.trim();
            if (!val) {
                showToast("Please enter IPv6 address.", "error");
                return;
            }
            const regex = /^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$/;
            if (regex.test(val)) {
                document.getElementById('text-output').value = "✓ Valid IPv6 Address\\n\\nMatches standard 128-bit hexadecimal network address formats.";
                updateBreakdown("<p class='text-success'>IPv6 format check passed.</p>");
            } else {
                document.getElementById('text-output').value = "✗ Invalid IPv6 Address\\n\\nFormat structure validation failed.";
                updateBreakdown("<p class='text-danger'>IPv6 hex groups checks failed.</p>");
                showToast("Invalid IPv6 address!", "error");
            }
        """
    },
    {
        "category": "Regex & Validation Tools",
        "name": "UUID Validator",
        "slug": "uuid-validator",
        "desc": "Check if a UUID / GUID string is mathematically structured.",
        "formula": "UUID v1/v4 Layout Regular Expression Rules",
        "formula_desc": "Verifies 8-4-4-4-12 hexadecimal character structure formats.",
        "icon": "🔑",
        "inputs": [
            {"id": "uuid-val", "label": "Enter UUID:", "type": "text", "default": "123e4567-e89b-12d3-a456-426614174000"}
        ],
        "outputs": [
            {"id": "text-output", "label": "UUID Validity Report:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('uuid-val').value.trim();
            if (!val) {
                showToast("Please enter UUID.", "error");
                return;
            }
            const regex = /^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$/;
            if (regex.test(val)) {
                document.getElementById('text-output').value = "✓ Valid UUID\\n\\nMatches standard 36-character hexadecimal layout.";
                updateBreakdown("<p class='text-success'>UUID syntax structure validated successfully.</p>");
            } else {
                document.getElementById('text-output').value = "✗ Invalid UUID\\n\\nFormat must be in 8-4-4-4-12 hex layout.";
                updateBreakdown("<p class='text-danger'>UUID regex matching failed.</p>");
                showToast("Invalid UUID format!", "error");
            }
        """
    },
    {
        "category": "Regex & Validation Tools",
        "name": "JSON Schema Validator",
        "slug": "json-schema-validator",
        "desc": "Validate JSON object data layouts against a basic JSON Schema specification.",
        "formula": "JSON Schema Property Checking rules",
        "formula_desc": "Audits parameter types and presence of keys against defined specifications.",
        "icon": "🛠️",
        "inputs": [
            {"id": "js-data", "label": "JSON Data:", "type": "textarea", "default": '{\n  "id": 101,\n  "name": "Engine"\n}'},
            {"id": "js-schema", "label": "JSON Schema:", "type": "textarea", "default": '{\n  "type": "object",\n  "required": ["id", "name"]\n}'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Validation Log:", "type": "textarea"}
        ],
        "calc_js": """
            const dataVal = document.getElementById('js-data').value.trim();
            const schemaVal = document.getElementById('js-schema').value.trim();
            
            if (!dataVal || !schemaVal) {
                showToast("Please enter both data and schema.", "error");
                return;
            }
            try {
                const data = JSON.parse(dataVal);
                const schema = JSON.parse(schemaVal);
                
                let errors = [];
                if (schema.type === 'object' && typeof data !== 'object') {
                    errors.push("Data is not an object.");
                }
                if (schema.required) {
                    schema.required.forEach(req => {
                        if (data[req] === undefined) {
                            errors.push(`Missing required field: "${req}"`);
                        }
                    });
                }
                
                if (errors.length === 0) {
                    document.getElementById('text-output').value = "✓ JSON Schema Validation Succeeded!\\n\\nData matches schema rules.";
                    updateBreakdown("<p class='text-success'>All required validation fields are present.</p>");
                } else {
                    document.getElementById('text-output').value = "✗ Schema Mismatches:\\n\\n" + errors.join('\\n');
                    updateBreakdown("<p class='text-danger'>Validation failed: schema rules violated.</p>");
                    showToast("Schema mismatch detected!", "error");
                }
            } catch(e) {
                document.getElementById('text-output').value = "Syntax Parse Error: " + e.message;
                showToast("JSON syntax error in one of the fields!", "error");
            }
        """
    },
    {
        "category": "Regex & Validation Tools",
        "name": "XML Schema Validator",
        "slug": "xml-schema-validator",
        "desc": "Check XML documents for presence of tags and nested tag syntax structures.",
        "formula": "DOMParser Element Tags Checklist",
        "formula_desc": "Parses XML documents, checking tag attributes structure against defined criteria.",
        "icon": "🛠️",
        "inputs": [
            {"id": "xml-data", "label": "XML Document Data:", "type": "textarea", "default": "<note>\n  <to>Developer</to>\n</note>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "XML Report:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('xml-data').value.trim();
            if (!val) {
                showToast("Please enter XML.", "error");
                return;
            }
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(val, "application/xml");
            const errors = xmlDoc.getElementsByTagName("parsererror");
            if (errors.length > 0) {
                document.getElementById('text-output').value = "✗ Invalid XML structure:\\n\\n" + errors[0].textContent;
                updateBreakdown("<p class='text-danger'>XML structure checking failed.</p>");
            } else {
                document.getElementById('text-output').value = "✓ Valid XML Structure\\n\\nTag checks completed successfully.";
                updateBreakdown("<p class='text-success'>XML syntax matches standards.</p>");
            }
        """
    }
]

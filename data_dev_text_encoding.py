# -*- coding: utf-8 -*-
"""
Database of 11 Text & Encoding Tools for Enginewheels
"""

TEXT_ENCODING_TOOLS = [
    {
        "category": "Text & Encoding Tools",
        "name": "Base64 Encoder",
        "slug": "base64-encoder",
        "desc": "Encode raw text strings into secure Base64 format representations.",
        "formula": "btoa(unescape(encodeURIComponent(str)))",
        "formula_desc": "Converts input text bytes into 64 ASCII characters using 6-bit index binary mappings.",
        "icon": "🔐",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Encode:", "type": "textarea", "default": "Hello Enginewheels!"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Base64 Encoded Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value;
            if (!val) {
                showToast("Please enter some text.", "error");
                return;
            }
            try {
                const encoded = btoa(unescape(encodeURIComponent(val)));
                document.getElementById('text-output').value = encoded;
                updateBreakdown("<p class='text-success'>Text successfully encoded in Base64 format.</p>");
            } catch(e) {
                showToast("Encoding failed!", "error");
            }
        """
    },
    {
        "category": "Text & Encoding Tools",
        "name": "Base64 Decoder",
        "slug": "base64-decoder",
        "desc": "Decode Base64 strings back into human-readable text.",
        "formula": "decodeURIComponent(escape(atob(str)))",
        "formula_desc": "Restores original character mappings by reversing 6-bit index binary conversions.",
        "icon": "🔓",
        "inputs": [
            {"id": "text-input", "label": "Enter Base64 String:", "type": "textarea", "default": "SGVsbG8gRW5naW5ld2hlZWxzIQ=="}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Plain Text Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter Base64 code.", "error");
                return;
            }
            try {
                const decoded = decodeURIComponent(escape(atob(val)));
                document.getElementById('text-output').value = decoded;
                updateBreakdown("<p class='text-success'>Base64 string successfully decoded.</p>");
            } catch(e) {
                document.getElementById('text-output').value = "Decode Error: Invalid Base64 character sequences.";
                updateBreakdown("<p class='text-danger'>Failed decoding. Invalid Base64 structure: " + e.message + "</p>");
                showToast("Invalid Base64 sequence!", "error");
            }
        """
    },
    {
        "category": "Text & Encoding Tools",
        "name": "URL Encoder",
        "slug": "url-encoder",
        "desc": "Encode special characters into percent-escaped URL strings.",
        "formula": "encodeURIComponent(url)",
        "formula_desc": "Converts non-ASCII and special control characters into hexadecimal percent-escape sequences.",
        "icon": "🌐",
        "inputs": [
            {"id": "text-input", "label": "Enter URL or parameters:", "type": "textarea", "default": "https://enginewheels.com?name=Dev Tool&active=yes"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Encoded URL String:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value;
            if (!val) {
                showToast("Please enter text.", "error");
                return;
            }
            const res = encodeURIComponent(val);
            document.getElementById('text-output').value = res;
            updateBreakdown("<p class='text-success'>Special URL characters converted to hexadecimal codes.</p>");
        """
    },
    {
        "category": "Text & Encoding Tools",
        "name": "URL Decoder",
        "slug": "url-decoder",
        "desc": "Convert percent-escaped URL parameters back to original text.",
        "formula": "decodeURIComponent(url)",
        "formula_desc": "Replaces URL percent-hex numbers with matching UTF-8 characters.",
        "icon": "🌐",
        "inputs": [
            {"id": "text-input", "label": "Enter Encoded URL:", "type": "textarea", "default": "https%3A%2F%2Fenginewheels.com%3Fname%3DDev%20Tool%26active%3Dyes"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter URL text.", "error");
                return;
            }
            try {
                const res = decodeURIComponent(val);
                document.getElementById('text-output').value = res;
                updateBreakdown("<p class='text-success'>Percent characters translated back to characters.</p>");
            } catch(e) {
                document.getElementById('text-output').value = "Error: " + e.message;
                showToast("URL decode failed!", "error");
            }
        """
    },
    {
        "category": "Text & Encoding Tools",
        "name": "HTML Entity Encoder",
        "slug": "html-encoder",
        "desc": "Convert special HTML tags into matching character entity sequences.",
        "formula": "HTML Character Entity Escaper",
        "formula_desc": "Substitutes key tag markup characters (&, <, >, ', \") with their corresponding HTML entity values.",
        "icon": "🔣",
        "inputs": [
            {"id": "text-input", "label": "Enter HTML Text:", "type": "textarea", "default": "<h1>Enginewheels & Co.</h1>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Escaped Entities Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value;
            if (!val) {
                showToast("Please enter text.", "error");
                return;
            }
            const map = {
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                '"': '&quot;',
                "'": '&#x27;',
                '/': '&#x2F;'
            };
            const res = val.replace(/[&<>"'/]/g, m => map[m]);
            document.getElementById('text-output').value = res;
            updateBreakdown("<p class='text-success'>HTML entity replacements completed.</p>");
        """
    },
    {
        "category": "Text & Encoding Tools",
        "name": "HTML Entity Decoder",
        "slug": "html-decoder",
        "desc": "Translate escaped HTML character entities back to normal tags.",
        "formula": "HTML Entity Name Unescape mapping",
        "formula_desc": "Replaces standard entity identifiers with raw HTML characters.",
        "icon": "🔣",
        "inputs": [
            {"id": "text-input", "label": "Enter Escaped Text:", "type": "textarea", "default": "&lt;h1&gt;Enginewheels &amp; Co.&lt;/h1&gt;"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded HTML Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter text.", "error");
                return;
            }
            const doc = new DOMParser().parseFromString(val, "text/html");
            const res = doc.documentElement.textContent;
            document.getElementById('text-output').value = res;
            updateBreakdown("<p class='text-success'>HTML entities decoded to raw markup characters.</p>");
        """
    },
    {
        "category": "Text & Encoding Tools",
        "name": "Unicode Encoder",
        "slug": "unicode-encoder",
        "desc": "Translate characters into escaped Unicode code point sequences.",
        "formula": "\\\\uXXXX Escaped Sequence Mapper",
        "formula_desc": "Evaluates charCodeAt values for text inputs, returning hex strings padded to 4 digits.",
        "icon": "🔢",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Escape:", "type": "textarea", "default": "Hello! 😊"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Unicode Escape Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value;
            if (!val) {
                showToast("Please enter text.", "error");
                return;
            }
            let res = "";
            for (let i = 0; i < val.length; i++) {
                const code = val.charCodeAt(i);
                if (code > 127) {
                    let hex = code.toString(16).toUpperCase();
                    while (hex.length < 4) hex = '0' + hex;
                    res += '\\\\u' + hex;
                } else {
                    res += val[i];
                }
            }
            document.getElementById('text-output').value = res;
            updateBreakdown("<p class='text-success'>Non-ASCII symbols escaped with Unicode notation.</p>");
        """
    },
    {
        "category": "Text & Encoding Tools",
        "name": "Unicode Decoder",
        "slug": "unicode-decoder",
        "desc": "Unescape unicode escape sequences back into readable text.",
        "formula": "Unicode Regex -> String.fromCharCode()",
        "formula_desc": "Identifies hexadecimal sequences, converting them back to raw characters.",
        "icon": "🔢",
        "inputs": [
            {"id": "text-input", "label": "Enter Unicode Escaped String:", "type": "textarea", "default": "Hello! \\uD83D\\uDE0A"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Unicode Text:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter unicode code.", "error");
                return;
            }
            try {
                const res = val.replace(/\\\\u([0-9a-fA-F]{4})/g, (match, grp) => {
                    return String.fromCharCode(parseInt(grp, 16));
                });
                document.getElementById('text-output').value = res;
                updateBreakdown("<p class='text-success'>Unicode escape strings decoded successfully.</p>");
            } catch(e) {
                document.getElementById('text-output').value = "Error: " + e.message;
                showToast("Unicode decode failed!", "error");
            }
        """
    },
    {
        "category": "Text & Encoding Tools",
        "name": "ASCII Converter",
        "slug": "ascii-converter",
        "desc": "Convert text into decimal or binary representation of ASCII bytes.",
        "formula": "ASCII CharCode Mapping",
        "formula_desc": "Translates string characters into their decimal ASCII index code numbers.",
        "icon": "🔢",
        "inputs": [
            {"id": "text-input", "label": "Enter Plain Text:", "type": "textarea", "default": "Enginewheels"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decimal ASCII Codes:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value;
            if (!val) {
                showToast("Please enter text.", "error");
                return;
            }
            let res = [];
            for (let i = 0; i < val.length; i++) {
                res.push(val.charCodeAt(i));
            }
            document.getElementById('text-output').value = res.join(' ');
            updateBreakdown("<p class='text-success'>Text mapped to space-separated decimal ASCII bytes.</p>");
        """
    },
    {
        "category": "Text & Encoding Tools",
        "name": "Text Escape Tool",
        "slug": "text-escape-tool",
        "desc": "Escape programming control characters in plain text.",
        "formula": "JSON Stringify Character Escaping",
        "formula_desc": "Substitutes JScript string constants (carriage return, tabs, backslashes, quotes) with safe escape codes.",
        "icon": "🔣",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Escape:", "type": "textarea", "default": "Line 1\\nLine 2\\tTabbed \\\"quotes\\\""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Escaped Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value;
            if (!val) {
                showToast("Please enter text.", "error");
                return;
            }
            const res = JSON.stringify(val).slice(1, -1);
            document.getElementById('text-output').value = res;
            updateBreakdown("<p class='text-success'>Carriage returns, backslashes, and quote tokens escaped.</p>");
        """
    },
    {
        "category": "Text & Encoding Tools",
        "name": "Text Unescape Tool",
        "slug": "text-unescape-tool",
        "desc": "Restore escaped sequences back into raw string text formatting.",
        "formula": "JSON Parse Escaped Sequence Unescaper",
        "formula_desc": "Translates code escape patterns into JScript string output segments.",
        "icon": "🔣",
        "inputs": [
            {"id": "text-input", "label": "Enter Escaped Text:", "type": "textarea", "default": "Line 1\\\\nLine 2\\\\tTabbed \\\\\"quotes\\\\\""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Raw Text Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter escaped text.", "error");
                return;
            }
            try {
                const res = JSON.parse('"' + val.replace(/"/g, '\\\\"') + '"');
                document.getElementById('text-output').value = res;
                updateBreakdown("<p class='text-success'>Escaped character patterns restored successfully.</p>");
            } catch(e) {
                document.getElementById('text-output').value = "Unescape failed: " + e.message;
                showToast("Unescape failed!", "error");
            }
        """
    }
]

# -*- coding: utf-8 -*-
"""
Text Converters and URL & Encoding Tools Data
"""

CONVERTER_CALCS = [
    {
        "name": "Text To Binary",
        "slug": "text-to-binary",
        "category": "Text Converters",
        "icon": "🔢",
        "desc": "Convert standard text characters to binary code bytes (0s and 1s).",
        "formula": "Binary = Char.charCodeAt(0).toString(2)",
        "formula_desc": "Converts each character to its Unicode index value, then evaluates its 8-bit binary format.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Convert:", "type": "textarea", "default": "hello"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Binary Code Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            let binary = '';
            for (let i = 0; i < text.length; i++) {
                let bin = text.charCodeAt(i).toString(2);
                binary += '0'.repeat(8 - bin.length) + bin + ' ';
            }
            document.getElementById('text-output').value = binary.trim();
            updateBreakdown(`<p>Encoded ${text.length} characters into 8-bit binary structures.</p>`);
        """
    },
    {
        "name": "Binary To Text",
        "slug": "binary-to-text",
        "category": "Text Converters",
        "icon": "🔤",
        "desc": "Decode binary sequences (0s and 1s) back into readable text.",
        "formula": "Char = String.fromCharCode(parseInt(bin, 2))",
        "formula_desc": "Splits binary sequences, parses each as base-2 digits, and prints text.",
        "inputs": [
            {"id": "text-input", "label": "Enter Binary Code (separated by spaces):", "type": "textarea", "default": "01101000 01100101 01101100 01101100 01101111"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            if (text === '') return;
            const bytes = text.split(/\\s+/);
            let result = '';
            try {
                for (let b of bytes) {
                    result += String.fromCharCode(parseInt(b, 2));
                }
                document.getElementById('text-output').value = result;
                updateBreakdown(`<p>Decoded ${bytes.length} binary packets.</p>`);
            } catch (e) {
                document.getElementById('text-output').value = 'Error decoding binary. Ensure it contains only 0s, 1s, and spaces.';
            }
        """
    },
    {
        "name": "Text To ASCII",
        "slug": "text-to-ascii",
        "category": "Text Converters",
        "icon": "🔡",
        "desc": "Convert text characters to their corresponding ASCII code numbers.",
        "formula": "ASCII = Char.charCodeAt(0)",
        "formula_desc": "Retrieves the standard decimal character index code values of characters.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text:", "type": "textarea", "default": "hello"}
        ],
        "outputs": [
            {"id": "text-output", "label": "ASCII Decimal Codes Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            let result = [];
            for (let i = 0; i < text.length; i++) {
                result.push(text.charCodeAt(i));
            }
            document.getElementById('text-output').value = result.join(' ');
            updateBreakdown(`<p>Mapped ${text.length} letters to standard ASCII decimal values.</p>`);
        """
    },
    {
        "name": "ASCII To Text",
        "slug": "ascii-to-text",
        "category": "Text Converters",
        "icon": "🔠",
        "desc": "Convert ASCII decimal code numbers back into readable text.",
        "formula": "Char = String.fromCharCode(decimal)",
        "formula_desc": "Takes space-separated ASCII numbers, converts them to UTF-16, and outputs character lines.",
        "inputs": [
            {"id": "text-input", "label": "Enter ASCII Codes (space-separated):", "type": "textarea", "default": "104 101 108 108 111"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            if (text === '') return;
            const codes = text.split(/\\s+/);
            let result = '';
            try {
                for (let c of codes) {
                    result += String.fromCharCode(parseInt(c, 10));
                }
                document.getElementById('text-output').value = result;
                updateBreakdown(`<p>Decoded ${codes.length} decimal numbers to text.</p>`);
            } catch (e) {
                document.getElementById('text-output').value = 'Error parsing ASCII codes.';
            }
        """
    },
    {
        "name": "Text To Hex",
        "slug": "text-to-hex",
        "category": "Text Converters",
        "icon": "🔢",
        "desc": "Convert text strings to hexadecimal (base-16) representation format.",
        "formula": "Hex = Char.charCodeAt(0).toString(16)",
        "formula_desc": "Translates Unicode values into standard 2-digit base-16 strings.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text:", "type": "textarea", "default": "hello"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Hexadecimal Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            let hex = '';
            for (let i = 0; i < text.length; i++) {
                let h = text.charCodeAt(i).toString(16);
                hex += (h.length < 2 ? '0' + h : h) + ' ';
            }
            document.getElementById('text-output').value = hex.trim();
            updateBreakdown(`<p>Encoded ${text.length} characters to base-16 hex values.</p>`);
        """
    },
    {
        "name": "Hex To Text",
        "slug": "hex-to-text",
        "category": "Text Converters",
        "icon": "🔤",
        "desc": "Decode hexadecimal character strings back into readable text.",
        "formula": "Char = String.fromCharCode(parseInt(hex, 16))",
        "formula_desc": "Parses hex segments as base-16 integers, returning character text.",
        "inputs": [
            {"id": "text-input", "label": "Enter Hex Codes:", "type": "textarea", "default": "68 65 6c 6c 6f"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            if (text === '') return;
            const hexes = text.split(/\\s+/);
            let result = '';
            try {
                for (let h of hexes) {
                    result += String.fromCharCode(parseInt(h, 16));
                }
                document.getElementById('text-output').value = result;
                updateBreakdown(`<p>Decoded ${hexes.length} hex segments.</p>`);
            } catch (e) {
                document.getElementById('text-output').value = 'Error decoding hex. Ensure characters are valid hex blocks.';
            }
        """
    },
    {
        "name": "Text To Base64",
        "slug": "text-to-base64",
        "category": "Text Converters",
        "icon": "📦",
        "desc": "Convert text into Base64 encoding structure for binary safe transfers.",
        "formula": "Base64 = btoa(text)",
        "formula_desc": "Converts binary-safe UTF-8 sequences to ASCII characters using standard Base64 layouts.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Encode:", "type": "textarea", "default": "hello"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Base64 Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            try {
                const encoded = btoa(unescape(encodeURIComponent(text)));
                document.getElementById('text-output').value = encoded;
                updateBreakdown(`<p>Encoded text of length ${text.length} to Base64 block format.</p>`);
            } catch (e) {
                document.getElementById('text-output').value = 'Error encoding to Base64.';
            }
        """
    },
    {
        "name": "Base64 To Text",
        "slug": "base64-to-text",
        "category": "Text Converters",
        "icon": "🔤",
        "desc": "Decode Base64 encoded strings back into readable text format.",
        "formula": "Text = atob(base64)",
        "formula_desc": "Decodes Base64 data blocks to retrieve raw text representations.",
        "inputs": [
            {"id": "text-input", "label": "Enter Base64 to Decode:", "type": "textarea", "default": "aGVsbG8="}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            if (text === '') return;
            try {
                const decoded = decodeURIComponent(escape(atob(text)));
                document.getElementById('text-output').value = decoded;
                updateBreakdown(`<p>Successfully decoded Base64 content.</p>`);
            } catch (e) {
                document.getElementById('text-output').value = 'Error: Invalid Base64 string format.';
            }
        """
    },
    {
        "name": "Text To Morse Code",
        "slug": "text-to-morse-code",
        "category": "Text Converters",
        "icon": "📟",
        "desc": "Translate plain text letters and numbers to international Morse code.",
        "formula": "Morse translation rules",
        "formula_desc": "Replaces standard characters with their international dot and dash equivalent codes.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text:", "type": "textarea", "default": "hello"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Morse Code Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.toUpperCase();
            const morseMap = {
                'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
            };
            let result = [];
            for (let c of text) {
                if (morseMap[c]) {
                    result.push(morseMap[c]);
                }
            }
            document.getElementById('text-output').value = result.join(' ');
            updateBreakdown(`<p>Translated alphanumeric inputs into Morse signal sequences.</p>`);
        """
    },
    {
        "name": "Morse Code To Text",
        "slug": "morse-code-to-text",
        "category": "Text Converters",
        "icon": "📡",
        "desc": "Translate international Morse code (dots and dashes) back to plain text.",
        "formula": "Morse reverse mapping",
        "formula_desc": "Splits signal values by spaces, mapping dot-dash sequences to characters.",
        "inputs": [
            {"id": "text-input", "label": "Enter Morse Code (separated by spaces, words by /):", "type": "textarea", "default": ".... . .-.. .-.. ---"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Text Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            const morseReverse = {
                '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
                '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '/': ' '
            };
            const signals = text.split(/\\s+/);
            let result = '';
            for (let s of signals) {
                if (morseReverse[s]) {
                    result += morseReverse[s];
                }
            }
            document.getElementById('text-output').value = result;
            updateBreakdown(`<p>Parsed Morse code signals into alphabetical text.</p>`);
        """
    }
]

URL_CALCS = [
    {
        "name": "Text To Slug",
        "slug": "text-to-slug",
        "category": "URL & Encoding Tools",
        "icon": "🔗",
        "desc": "Convert text headings into clean, SEO-friendly URL slug strings.",
        "formula": "Slug = Text.replace(/[^a-z0-9]/, '-')",
        "formula_desc": "Converts string to lowercase, replaces spaces/symbols with hyphens, and removes duplicates.",
        "inputs": [
            {"id": "text-input", "label": "Enter Heading/Title:", "type": "text", "default": "New Website Feature Launch"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated URL Slug", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const slug = text.toString().toLowerCase().trim()
                .replace(/\\s+/g, '-')
                .replace(/&/g, '-and-')
                .replace(/[^\\w\\-]+/g, '')
                .replace(/\\-\\-+/g, '-')
                .replace(/^-+/, '')
                .replace(/-+$/, '');
            document.getElementById('text-output').value = slug;
            updateBreakdown(`<p>Created valid slug formatting, eliminating invalid URL path symbols.</p>`);
        """
    },
    {
        "name": "URL Slug Generator",
        "slug": "url-slug-generator",
        "category": "URL & Encoding Tools",
        "icon": "⛓️",
        "desc": "Generate web-optimized slugs for articles, pages, or routes.",
        "formula": "Hyphenated lowercase formatting",
        "formula_desc": "Strips spaces and non-word characters to build indexable web addresses.",
        "inputs": [
            {"id": "text-input", "label": "Enter Page Title:", "type": "text", "default": "My First Blog Post!"}
        ],
        "outputs": [
            {"id": "text-output", "label": "SEO Slug", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const slug = text.toString().toLowerCase().trim()
                .replace(/\\s+/g, '-')
                .replace(/[^\\w\\-]+/g, '')
                .replace(/\\-\\-+/g, '-')
                .replace(/^-+/, '')
                .replace(/-+$/, '');
            document.getElementById('text-output').value = slug;
            updateBreakdown(`<p>Created a URL-safe lowercase slug.</p>`);
        """
    },
    {
        "name": "URL Encoder",
        "slug": "url-encoder",
        "category": "URL & Encoding Tools",
        "icon": "🌐",
        "desc": "Encode text string components to standard percent-encoded URL formats.",
        "formula": "Encoded = encodeURIComponent(text)",
        "formula_desc": "Replaces special characters in a URI with their hexadecimal representation escape sequences.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Encode:", "type": "textarea", "default": "hello world & parameter"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Percent Encoded Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const encoded = encodeURIComponent(text);
            document.getElementById('text-output').value = encoded;
            updateBreakdown(`<p>Encoded query indicators to match standard HTTP parameter guidelines.</p>`);
        """
    },
    {
        "name": "URL Decoder",
        "slug": "url-decoder",
        "category": "URL & Encoding Tools",
        "icon": "🔓",
        "desc": "Decode percent-encoded URL components back to standard plain text.",
        "formula": "Decoded = decodeURIComponent(text)",
        "formula_desc": "Replaces hexadecimal percent escapes back to standard text characters.",
        "inputs": [
            {"id": "text-input", "label": "Enter Percent Encoded URL:", "type": "textarea", "default": "hello%20world%20%26%20parameter"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Text Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            try {
                const decoded = decodeURIComponent(text);
                document.getElementById('text-output').value = decoded;
                updateBreakdown(`<p>Parsed percent characters back into text segments.</p>`);
            } catch (e) {
                document.getElementById('text-output').value = 'Error decoding URL. Invalid percent-encoding sequence.';
            }
        """
    },
    {
        "name": "HTML Encoder",
        "slug": "html-encoder",
        "category": "URL & Encoding Tools",
        "icon": "🧬",
        "desc": "Convert special HTML characters like tags into escaped HTML entities.",
        "formula": "Entity replacement",
        "formula_desc": "Translates code symbols like < and > into safe XML entity values.",
        "inputs": [
            {"id": "text-input", "label": "Enter raw HTML:", "type": "textarea", "default": "<div>hello</div>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "HTML Escaped Code", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const map = {
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                '"': '&quot;',
                "'": '&#039;'
            };
            const encoded = text.replace(/[&<>"']/g, m => map[m]);
            document.getElementById('text-output').value = encoded;
            updateBreakdown(`<p>Escaped HTML elements to prevent browser rendering conflicts.</p>`);
        """
    },
    {
        "name": "HTML Decoder",
        "slug": "html-decoder",
        "category": "URL & Encoding Tools",
        "icon": "🔓",
        "desc": "Decode HTML entities (e.g. &amp;lt;) back to standard raw tags.",
        "formula": "Reverse entity conversion",
        "formula_desc": "Transforms safe entity sequences back to standard HTML symbols.",
        "inputs": [
            {"id": "text-input", "label": "Enter Escaped HTML:", "type": "textarea", "default": "&lt;div&gt;hello&lt;/div&gt;"}
        ],
        "outputs": [
            {"id": "text-output", "label": "HTML Code Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const temp = document.createElement('textarea');
            temp.innerHTML = text;
            const decoded = temp.value;
            document.getElementById('text-output').value = decoded;
            updateBreakdown(`<p>Decoded escaped entities back into raw programming characters.</p>`);
        """
    },
    {
        "name": "Unicode Encoder",
        "slug": "unicode-encoder",
        "category": "URL & Encoding Tools",
        "icon": "🔣",
        "desc": "Encode standard text strings to unicode code point format (\\uXXXX).",
        "formula": "\\\\u + Hex(CharCode)",
        "formula_desc": "Transforms characters into standard hexadecimal Unicode escapes.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text:", "type": "textarea", "default": "hello"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Unicode Escape Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            let result = '';
            for (let i = 0; i < text.length; i++) {
                let hex = text.charCodeAt(i).toString(16).toUpperCase();
                result += '\\\\u' + '0'.repeat(4 - hex.length) + hex;
            }
            document.getElementById('text-output').value = result;
            updateBreakdown(`<p>Converted characters into 16-bit unicode hex escapes.</p>`);
        """
    },
    {
        "name": "Unicode Decoder",
        "slug": "unicode-decoder",
        "category": "URL & Encoding Tools",
        "icon": "🔓",
        "desc": "Decode unicode escaped code points (\\uXXXX) back to normal text.",
        "formula": "Eval unicode escapes",
        "formula_desc": "Matches unicode escape strings and converts them back to text.",
        "inputs": [
            {"id": "text-input", "label": "Enter Unicode Escapes:", "type": "textarea", "default": "\\\\u0068\\\\u0065\\\\u006C\\\\u006C\\\\u006F"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Text Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            try {
                // Parse \\uXXXX escapes
                const decoded = text.replace(/\\\\u([0-9a-fA-F]{{4}})/g, (match, grp) => String.fromCharCode(parseInt(grp, 16)));
                document.getElementById('text-output').value = decoded;
                updateBreakdown(`<p>Successfully decoded Unicode hex escape characters.</p>`);
            } catch (e) {
                document.getElementById('text-output').value = 'Error decoding Unicode escapes.';
            }
        """
    },
    {
        "name": "Escape Text Tool",
        "slug": "escape-text-tool",
        "category": "URL & Encoding Tools",
        "icon": "🔒",
        "desc": "Escape programming variables by adding backslashes to quotes and slashes.",
        "formula": "Backslash escaping",
        "formula_desc": "Prepends backslashes to newlines, quotes, and tabs to create valid JS/C string inputs.",
        "inputs": [
            {"id": "text-input", "label": "Enter Raw text:", "type": "textarea", "default": "line 1\\nline \"2\""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Escaped Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const escaped = text.replace(/[\\\\\\'\\"\\/\\n\\r\\t\\b\\f]/g, (match) => {
                switch (match) {
                    case '\\\\': return '\\\\\\\\';
                    case '\\'': return '\\\\\\\'';
                    case '"': return '\\\\\\"';
                    case '/': return '\\\\/';
                    case '\\n': return '\\\\n';
                    case '\\r': return '\\\\r';
                    case '\\t': return '\\\\t';
                    case '\\b': return '\\\\b';
                    case '\\f': return '\\\\f';
                    default: return match;
                }
            });
            document.getElementById('text-output').value = escaped;
            updateBreakdown(`<p>Added escape character flags to variables.</p>`);
        """
    },
    {
        "name": "Unescape Text Tool",
        "slug": "unescape-text-tool",
        "category": "URL & Encoding Tools",
        "icon": "🔓",
        "desc": "Unescape programming strings by removing double backslashes and quotes escapes.",
        "formula": "Remove escaping backslashes",
        "formula_desc": "Transforms code escape symbols back into raw text characters.",
        "inputs": [
            {"id": "text-input", "label": "Enter Escaped text:", "type": "textarea", "default": 'line 1\\\\nline \\\\\\"2\\\\\\"'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Unescaped Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            // Parse escaped characters
            let unescaped = text;
            try {
                // Wrap in JSON quotes to parse safely or do regex parsing
                unescaped = text.replace(/\\\\(.)/g, (match, grp) => {
                    switch (grp) {
                        case '\\\\': return '\\\\';
                        case 'n': return '\\n';
                        case 'r': return '\\r';
                        case 't': return '\\t';
                        case 'b': return '\\b';
                        case 'f': return '\\f';
                        case '"': return '"';
                        case '\\'': return '\\'';
                        case '/': return '/';
                        default: return grp;
                    }
                });
                document.getElementById('text-output').value = unescaped;
                updateBreakdown(`<p>Unescaped backslashes and carriage returns.</p>`);
            } catch (e) {
                document.getElementById('text-output').value = 'Error unescaping string.';
            }
        """
    }
]

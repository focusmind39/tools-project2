# -*- coding: utf-8 -*-
"""
Encoding, Decoding, and Token/Key Generator Tools
"""

ENCODING_DECODING_TOOLS = [
    {
        "name": "Base64 Encoder",
        "slug": "base64-encoder",
        "category": "Encoding & Decoding Tools",
        "icon": "📦",
        "desc": "Encode raw text strings into Base64 format safely in your browser.",
        "formula": "Base64 = Window.btoa(Text)",
        "formula_desc": "Converts binary data into a set of 64 characters representing text values.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Encode:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Base64 Encoded Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            try {
                // Handle UTF-8 encoding support
                const words = CryptoJS.enc.Utf8.parse(text);
                const base64 = CryptoJS.enc.Base64.stringify(words);
                document.getElementById('text-output').value = base64;
                updateBreakdown(`<p>Encoded text of length ${text.length} into Base64 successfully.</p>`);
            } catch(e) {
                showToast("Could not encode string.", "error");
            }
        """
    },
    {
        "name": "Base64 Decoder",
        "slug": "base64-decoder",
        "category": "Encoding & Decoding Tools",
        "icon": "📦",
        "desc": "Decode Base64 encoded strings back to plain text format locally.",
        "formula": "Text = Window.atob(Base64)",
        "formula_desc": "Converts Base64 values back into their original binary/UTF-8 character forms.",
        "inputs": [
            {"id": "text-input", "label": "Enter Base64 to Decode:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Plain Text Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            if (!text) {
                showToast("Please enter Base64 code!", "error");
                return;
            }
            try {
                const parsedWords = CryptoJS.enc.Base64.parse(text);
                const decoded = CryptoJS.enc.Utf8.stringify(parsedWords);
                if (decoded === "") throw new Error("Invalid output");
                document.getElementById('text-output').value = decoded;
                updateBreakdown("<p>Decoded Base64 string successfully.</p>");
            } catch(e) {
                showToast("Invalid Base64 format!", "error");
                document.getElementById('text-output').value = "Error: Invalid Base64 string.";
            }
        """
    },
    {
        "name": "URL Encoder",
        "slug": "url-encoder",
        "category": "Encoding & Decoding Tools",
        "icon": "🌐",
        "desc": "Encode text strings to make them safe for URL queries and parameters.",
        "formula": "URL = encodeURIComponent(Text)",
        "formula_desc": "Replaces special non-alphanumeric characters with hex escape sequences prefixing with %.",
        "inputs": [
            {"id": "text-input", "label": "Enter URL or Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "URL Encoded Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const encoded = encodeURIComponent(text);
            document.getElementById('text-output').value = encoded;
            updateBreakdown("<p>URL encoded all non-alphanumeric parameter characters.</p>");
        """
    },
    {
        "name": "URL Decoder",
        "slug": "url-decoder",
        "category": "Encoding & Decoding Tools",
        "icon": "🌐",
        "desc": "Decode URL-encoded parameters back into clear text.",
        "formula": "Text = decodeURIComponent(URL)",
        "formula_desc": "Converts percent-encoded hex sequences back to readable letters and symbols.",
        "inputs": [
            {"id": "text-input", "label": "Enter Encoded URL:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "URL Decoded Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            try {
                const decoded = decodeURIComponent(text.replace(/\\+/g, ' '));
                document.getElementById('text-output').value = decoded;
                updateBreakdown("<p>Successfully decoded URL string.</p>");
            } catch(e) {
                showToast("Invalid URL encoding structure!", "error");
                document.getElementById('text-output').value = "Error: Malformed URL encoding.";
            }
        """
    },
    {
        "name": "HTML Encoder",
        "slug": "html-encoder",
        "category": "Encoding & Decoding Tools",
        "icon": "🔤",
        "desc": "Convert special HTML characters like <, >, and & into secure HTML entity equivalents.",
        "formula": "Entity = CharToHtmlEntityMap(Char)",
        "formula_desc": "Protects scripts from running by escaping HTML rendering tags.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Escape:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "HTML Encoded Code", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const div = document.createElement('div');
            div.textContent = text;
            document.getElementById('text-output').value = div.innerHTML;
            updateBreakdown("<p>Escaped active rendering tags into plain entities.</p>");
        """
    },
    {
        "name": "HTML Decoder",
        "slug": "html-decoder",
        "category": "Encoding & Decoding Tools",
        "icon": "🔤",
        "desc": "Decode escaped HTML entities back into plain characters.",
        "formula": "Char = EntityToCharMap(Entity)",
        "formula_desc": "Converts entities (e.g. &lt;) back to standard symbols.",
        "inputs": [
            {"id": "text-input", "label": "Enter Encoded HTML Entities:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const div = document.createElement('div');
            div.innerHTML = text;
            document.getElementById('text-output').value = div.textContent;
            updateBreakdown("<p>Restored HTML entities to standard characters.</p>");
        """
    },
    {
        "name": "Unicode Encoder",
        "slug": "unicode-encoder",
        "category": "Encoding & Decoding Tools",
        "icon": "✨",
        "desc": "Convert text characters into unicode escape sequences (e.g., \\uXXXX) easily.",
        "formula": "Escape = '\\\\u' + Hex(CharCode)",
        "formula_desc": "Replaces each character with its hex representation in standard 16-bit unicode notation.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Encode:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Unicode Escape Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            let result = "";
            for (let i = 0; i < text.length; i++) {
                const hex = text.charCodeAt(i).toString(16).toUpperCase().padStart(4, '0');
                result += "\\\\u" + hex;
            }
            document.getElementById('text-output').value = result;
            updateBreakdown("<p>Encoded text into 16-bit unicode escape runs.</p>");
        """
    },
    {
        "name": "Unicode Decoder",
        "slug": "unicode-decoder",
        "category": "Encoding & Decoding Tools",
        "icon": "✨",
        "desc": "Decode unicode hex sequences (\\uXXXX) back to standard readable text.",
        "formula": "Char = String.fromCharCode(HexCode)",
        "formula_desc": "Parses 4-character hex blocks and converts them back to matching string symbols.",
        "inputs": [
            {"id": "text-input", "label": "Enter Unicode Escapes:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Plain Text Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            try {
                const decoded = text.replace(/\\\\u([0-9a-fA-F]{4})/g, (match, grp) => {
                    return String.fromCharCode(parseInt(grp, 16));
                });
                document.getElementById('text-output').value = decoded;
                updateBreakdown("<p>Decoded unicode blocks into normal characters.</p>");
            } catch(e) {
                showToast("Invalid unicode escapes format!", "error");
            }
        """
    },
    {
        "name": "ASCII Encoder",
        "slug": "ascii-encoder",
        "category": "Encoding & Decoding Tools",
        "icon": "🔢",
        "desc": "Convert text strings to their decimal ASCII numerical values.",
        "formula": "ASCII = CharCodeAt(Index)",
        "formula_desc": "Iterates characters and fetches matching numbers from the standard ASCII index.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Encode:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "ASCII Code List", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            let codes = [];
            for (let i = 0; i < text.length; i++) {
                codes.push(text.charCodeAt(i));
            }
            document.getElementById('text-output').value = codes.join(" ");
            updateBreakdown("<p>Translated character array into standard base-10 ASCII digits.</p>");
        """
    },
    {
        "name": "ASCII Decoder",
        "slug": "ascii-decoder",
        "category": "Encoding & Decoding Tools",
        "icon": "🔢",
        "desc": "Convert decimal ASCII codes back to clear readable text characters.",
        "formula": "Char = String.fromCharCode(Code)",
        "formula_desc": "Converts space-separated base-10 numbers back to string characters.",
        "inputs": [
            {"id": "text-input", "label": "Enter ASCII Codes (space-separated):", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Plain Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            if (!text) {
                showToast("Please enter ASCII numbers!", "error");
                return;
            }
            const codes = text.split(/\\s+/);
            let result = "";
            try {
                for (let c of codes) {
                    const code = parseInt(c);
                    if (isNaN(code)) throw new Error();
                    result += String.fromCharCode(code);
                }
                document.getElementById('text-output').value = result;
                updateBreakdown("<p>Decoded ASCII digits back to text successfully.</p>");
            } catch(e) {
                showToast("Failed to parse codes! Ensure they are space-separated numbers.", "error");
            }
        """
    },
    {
        "name": "Binary Encoder",
        "slug": "binary-encoder",
        "category": "Encoding & Decoding Tools",
        "icon": "💻",
        "desc": "Convert your plain text characters into standard 8-bit binary representation.",
        "formula": "Binary = CharCode.toString(2).padStart(8, '0')",
        "formula_desc": "Transforms character decimal values to binary base-2 notation pad formatted to 8 bits.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Encode:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "8-Bit Binary Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            let result = [];
            for (let i = 0; i < text.length; i++) {
                const bin = text.charCodeAt(i).toString(2).padStart(8, '0');
                result.push(bin);
            }
            document.getElementById('text-output').value = result.join(" ");
            updateBreakdown("<p>Text characters translated to base-2 binary strings.</p>");
        """
    },
    {
        "name": "Binary Decoder",
        "slug": "binary-decoder",
        "category": "Encoding & Decoding Tools",
        "icon": "💻",
        "desc": "Decode base-2 binary strings (8-bit blocks) back to clear text representation.",
        "formula": "Char = String.fromCharCode(parseInt(Bin, 2))",
        "formula_desc": "Parses binary numbers back to base-10 values and translates them into matching characters.",
        "inputs": [
            {"id": "text-input", "label": "Enter Binary String (space-separated):", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Plain Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            if (!text) {
                showToast("Please enter binary code!", "error");
                return;
            }
            const bins = text.split(/\\s+/);
            let result = "";
            try {
                for (let b of bins) {
                    const charCode = parseInt(b, 2);
                    if (isNaN(charCode)) throw new Error();
                    result += String.fromCharCode(charCode);
                }
                document.getElementById('text-output').value = result;
                updateBreakdown("<p>Decoded binary representation successfully.</p>");
            } catch(e) {
                showToast("Malformed binary input. Ensure space-separated 8-bit blocks are provided.", "error");
            }
        """
    },
    {
        "name": "Hex Encoder",
        "slug": "hex-encoder",
        "category": "Encoding & Decoding Tools",
        "icon": "🔢",
        "desc": "Convert clear text strings into hexadecimal representation (base-16).",
        "formula": "Hex = CharCode.toString(16).padStart(2, '0')",
        "formula_desc": "Translates string characters into matching double-character base-16 symbols.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Encode:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Hexadecimal Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            let result = "";
            for (let i = 0; i < text.length; i++) {
                result += text.charCodeAt(i).toString(16).padStart(2, '0');
            }
            document.getElementById('text-output').value = result;
            updateBreakdown("<p>Translated character bytes into hex strings.</p>");
        """
    },
    {
        "name": "Hex Decoder",
        "slug": "hex-decoder",
        "category": "Encoding & Decoding Tools",
        "icon": "🔢",
        "desc": "Decode hexadecimal codes (base-16) back to clear plain text representation.",
        "formula": "Char = String.fromCharCode(parseInt(Hex, 16))",
        "formula_desc": "Groups hex characters in pairs, parses them, and translates them back to standard characters.",
        "inputs": [
            {"id": "text-input", "label": "Enter Hex String:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Plain Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim().replace(/\\s+/g, '');
            if (!text) {
                showToast("Please enter a hex string!", "error");
                return;
            }
            if (text.length % 2 !== 0) {
                showToast("Hex string length must be even!", "error");
                return;
            }
            let result = "";
            try {
                for (let i = 0; i < text.length; i += 2) {
                    const charCode = parseInt(text.substr(i, 2), 16);
                    if (isNaN(charCode)) throw new Error();
                    result += String.fromCharCode(charCode);
                }
                document.getElementById('text-output').value = result;
                updateBreakdown("<p>Hex representation decoded back to plaintext.</p>");
            } catch(e) {
                showToast("Invalid hexadecimal code input!", "error");
            }
        """
    },
    {
        "name": "ROT13 Encoder",
        "slug": "rot13-encoder",
        "category": "Encoding & Decoding Tools",
        "icon": "🔄",
        "desc": "Encode your text by shifting letters by 13 spaces along the alphabet.",
        "formula": "ROT13(Char) = CharShift(Char, 13)",
        "formula_desc": "Shifts letters by 13 positions, rolling back if they pass Z.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to ROT13 Encode:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "ROT13 Encoded Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const encoded = text.replace(/[a-zA-Z]/g, (c) => {
                const code = c.charCodeAt(0);
                const start = code <= 90 ? 65 : 97;
                return String.fromCharCode(((code - start + 13) % 26) + start);
            });
            document.getElementById('text-output').value = encoded;
            updateBreakdown("<p>Rotated alphabetical characters by 13 index positions.</p>");
        """
    },
    {
        "name": "ROT13 Decoder",
        "slug": "rot13-decoder",
        "category": "Encoding & Decoding Tools",
        "icon": "🔄",
        "desc": "Decode ROT13 text back to its original readable format.",
        "formula": "ROT13(ROT13(Char)) = Char",
        "formula_desc": "Applying the 13-shift again restores the character to its original value.",
        "inputs": [
            {"id": "text-input", "label": "Enter ROT13 Encoded Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Plain Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const decoded = text.replace(/[a-zA-Z]/g, (c) => {
                const code = c.charCodeAt(0);
                const start = code <= 90 ? 65 : 97;
                return String.fromCharCode(((code - start + 13) % 26) + start);
            });
            document.getElementById('text-output').value = decoded;
            updateBreakdown("<p>Reversed ROT13 shift by rotating letters an additional 13 spots.</p>");
        """
    }
]

TOKEN_KEY_GENERATOR_TOOLS = [
    {
        "name": "UUID Generator",
        "slug": "uuid-generator",
        "category": "Token & Key Generators",
        "icon": "🆔",
        "desc": "Generate cryptographically secure RFC 4122 Version 4 UUIDs instantly.",
        "formula": "UUIDv4 = RandomHex(8)-4Hex-4Hex-4Hex-12Hex",
        "formula_desc": "Generates 128-bit identifiers using CSPRNG with specific version and variant bits set.",
        "inputs": [
            {"id": "count", "label": "Number of UUIDs to Generate:", "type": "number", "default": "1", "min": "1", "max": "100"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated UUID(s)", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('count').value) || 1;
            
            function generateUUID() {
                const random = new Uint8Array(16);
                window.crypto.getRandomValues(random);
                
                // Set version to 4
                random[6] = (random[6] & 0x0f) | 0x40;
                // Set variant to RFC 4122
                random[8] = (random[8] & 0x3f) | 0x80;
                
                let uuid = "";
                for (let i = 0; i < 16; i++) {
                    if (i === 4 || i === 6 || i === 8 || i === 10) uuid += "-";
                    uuid += random[i].toString(16).padStart(2, '0');
                }
                return uuid;
            }

            let result = [];
            for (let i = 0; i < count; i++) {
                result.push(generateUUID());
            }

            document.getElementById('text-output').value = result.join("\\n");
            updateBreakdown(`<p>Generated ${count} UUID v4 identifier(s).</p>`);
        """
    },
    {
        "name": "UUID Validator",
        "slug": "uuid-validator",
        "category": "Token & Key Generators",
        "icon": "🆔",
        "desc": "Validate UUIDs to ensure they comply with standard RFC 4122 formatting rules.",
        "formula": "Match(Regex(RFC_4122))",
        "formula_desc": "Checks if the string matches the 8-4-4-4-12 hex character pattern and indicates the UUID version.",
        "inputs": [
            {"id": "uuid-input", "label": "Enter UUID to Validate:", "type": "text", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Validation Results", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const uuid = document.getElementById('uuid-input').value.trim();
            if (!uuid) {
                showToast("Please enter a UUID to validate!", "error");
                return;
            }

            const regex = /^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-([1-5])[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$/;
            const match = regex.exec(uuid);

            if (match) {
                const version = match[1];
                document.getElementById('text-output').value = 
                    `Result: ✅ VALID UUID\\n` +
                    `Format: RFC 4122 Compliant\\n` +
                    `Version: Version ${version}`;
            } else {
                document.getElementById('text-output').value = `Result: ❌ INVALID UUID\\n\\nDoes not match standard RFC 4122 format.`;
            }
            updateBreakdown("<p>Validated structure using standard RFC 4122 expressions.</p>");
        """
    },
    {
        "name": "Random Token Generator",
        "slug": "random-token-generator",
        "category": "Token & Key Generators",
        "icon": "🎲",
        "desc": "Generate high-entropy random tokens in HEX, Base64, or Alphanumeric formats.",
        "formula": "Token = CSPRNG(Length, Encoding)",
        "formula_desc": "Generates cryptographically secure random bytes and encodes them to the chosen format.",
        "inputs": [
            {"id": "token-len", "label": "Entropy Byte Length:", "type": "number", "default": "32", "min": "8", "max": "256"},
            {"id": "token-type", "label": "Token Format:", "type": "select", "options": [("HEX", "Hexadecimal"), ("BASE64", "Base64"), ("ALPHANUM", "Alphanumeric")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Token", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const len = parseInt(document.getElementById('token-len').value) || 32;
            const type = document.getElementById('token-type').value;

            const random = new Uint8Array(len);
            window.crypto.getRandomValues(random);

            let token = "";
            if (type === "HEX") {
                for (let i = 0; i < len; i++) {
                    token += random[i].toString(16).padStart(2, '0');
                }
            } else if (type === "BASE64") {
                const binary = String.fromCharCode.apply(null, random);
                token = btoa(binary);
            } else {
                const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
                for (let i = 0; i < len; i++) {
                    token += chars[random[i] % chars.length];
                }
            }

            document.getElementById('text-output').value = token;
            updateBreakdown(`<p>Generated a secure random token of ${len} bytes in ${type} format.</p>`);
        """
    },
    {
        "name": "API Key Generator",
        "slug": "api-key-generator",
        "category": "Token & Key Generators",
        "icon": "💻",
        "desc": "Generate custom API keys with configurable prefixes (e.g. ew_live_...) for your software services.",
        "formula": "APIKey = Prefix + '_' + CSPRNG(Hex, 32)",
        "formula_desc": "Appends a custom prefix to secure, high-entropy random bytes.",
        "inputs": [
            {"id": "prefix", "label": "Prefix (e.g. api_key, live):", "type": "text", "default": "ew_live"},
            {"id": "key-len", "label": "Random Part Length (bytes):", "type": "number", "default": "24", "min": "16", "max": "64"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated API Key", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const prefix = document.getElementById('prefix').value.trim();
            const len = parseInt(document.getElementById('key-len').value) || 24;

            const random = new Uint8Array(len);
            window.crypto.getRandomValues(random);

            let randomPart = "";
            for (let i = 0; i < len; i++) {
                randomPart += random[i].toString(16).padStart(2, '0');
            }

            const apiKey = prefix ? `${prefix}_${randomPart}` : randomPart;
            document.getElementById('text-output').value = apiKey;
            updateBreakdown("<p>Generated API key with secure prefix formatting.</p>");
        """
    },
    {
        "name": "Secret Key Generator",
        "slug": "secret-key-generator",
        "category": "Token & Key Generators",
        "icon": "🔑",
        "desc": "Generate high-entropy random secret keys for session cookies, Django, Flask, or Node applications.",
        "formula": "SecretKey = CryptoRandomString(Length)",
        "formula_desc": "Draws values from a complex, non-standard character set to prevent dictionary or guess attacks.",
        "inputs": [
            {"id": "key-length", "label": "Key Character Length:", "type": "number", "default": "50", "min": "16", "max": "128"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Secret Key", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const len = parseInt(document.getElementById('key-length').value) || 50;
            const pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(-_=+~[{}])";

            const random = new Uint32Array(len);
            window.crypto.getRandomValues(random);

            let key = "";
            for (let i = 0; i < len; i++) {
                key += pool[random[i] % pool.length];
            }

            document.getElementById('text-output').value = key;
            updateBreakdown(`<p>Generated custom secret key using a ${pool.length}-character high-entropy pool.</p>`);
        """
    },
    {
        "name": "Encryption Key Generator",
        "slug": "encryption-key-generator",
        "category": "Token & Key Generators",
        "icon": "🔐",
        "desc": "Generate secure symmetric encryption keys from passwords using PBKDF2 key derivation.",
        "formula": "DerivedKey = PBKDF2(Password, Salt, Iterations, KeySize)",
        "formula_desc": "Derives secure keys from passwords by running multiple hashing iterations with a random salt.",
        "inputs": [
            {"id": "password", "label": "Key Passphrase:", "type": "text", "default": "MySecurePassword"},
            {"id": "salt", "label": "Salt (HEX or Text):", "type": "text", "default": "rand_salt_123"},
            {"id": "iterations", "label": "PBKDF2 Iterations:", "type": "number", "default": "10000", "min": "1000", "max": "100000"},
            {"id": "bits", "label": "Key Size (Bits):", "type": "select", "options": [("256", "256-bit (AES-256)"), ("128", "128-bit (AES-128)"), ("192", "192-bit (Triple DES)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Derived Key (HEX)", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const pass = document.getElementById('password').value;
            const saltVal = document.getElementById('salt').value;
            const iter = parseInt(document.getElementById('iterations').value) || 10000;
            const keySizeBits = parseInt(document.getElementById('bits').value);

            if (!pass || !saltVal) {
                showToast("Passphrase and salt are required!", "error");
                return;
            }

            const keySizeWords = keySizeBits / 32;
            const derived = CryptoJS.PBKDF2(pass, saltVal, {
                keySize: keySizeWords,
                iterations: iter,
                hasher: CryptoJS.algo.SHA256
            });

            document.getElementById('text-output').value = derived.toString().toUpperCase();
            updateBreakdown(`<p>Derived standard <strong>${keySizeBits}-bit</strong> key using PBKDF2 with SHA-256.</p>`);
        """
    },
    {
        "name": "JWT Generator",
        "slug": "jwt-generator",
        "category": "Token & Key Generators",
        "icon": "🎟️",
        "desc": "Generate custom JSON Web Tokens (JWT) signed with HS256 (HMAC-SHA256) instantly.",
        "formula": "JWT = Base64Url(Header) + '.' + Base64Url(Payload) + '.' + Base64Url(HMAC(Header.Payload, Secret))",
        "formula_desc": "Generates a signed JWT with base64url encoding and a HMAC signature.",
        "inputs": [
            {"id": "payload-json", "label": "JWT Payload JSON:", "type": "textarea", "default": '{\\n  "sub": "1234567890",\\n  "name": "John Doe",\\n  "admin": true\\n}'},
            {"id": "secret-key", "label": "HMAC Secret Key (HMAC-SHA256):", "type": "text", "default": "super-secret-key-123"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated JWT String", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const payloadStr = document.getElementById('payload-json').value;
            const secret = document.getElementById('secret-key').value;

            if (!secret) {
                showToast("Secret key is required for signature!", "error");
                return;
            }

            try {
                const payloadObj = JSON.parse(payloadStr);
                
                const header = { "alg": "HS256", "typ": "JWT" };
                
                function base64UrlEncode(wordArray) {
                    let encoded = CryptoJS.enc.Base64.stringify(wordArray);
                    return encoded.replace(/=+$/, '').replace(/\\+/g, '-').replace(/\\//g, '_');
                }

                const encodedHeader = base64UrlEncode(CryptoJS.enc.Utf8.parse(JSON.stringify(header)));
                const encodedPayload = base64UrlEncode(CryptoJS.enc.Utf8.parse(JSON.stringify(payloadObj)));
                
                const signable = encodedHeader + "." + encodedPayload;
                const signature = base64UrlEncode(CryptoJS.HmacSHA256(signable, secret));

                const jwt = signable + "." + signature;
                document.getElementById('text-output').value = jwt;
                updateBreakdown("<p>Generated JSON Web Token signed with HMAC-SHA256.</p>");
            } catch(e) {
                showToast("Invalid Payload JSON structure!", "error");
            }
        """
    },
    {
        "name": "JWT Decoder",
        "slug": "jwt-decoder",
        "category": "Token & Key Generators",
        "icon": "🎟️",
        "desc": "Decode JSON Web Tokens (JWT) client-side to inspect the header and payload properties.",
        "formula": "Parts = JWT.split('.'); Decoded = Base64UrlDecode(Parts[0]) + Base64UrlDecode(Parts[1])",
        "formula_desc": "Splits the JWT into Header, Payload, and Signature, and decodes the base64url content.",
        "inputs": [
            {"id": "jwt-input", "label": "Enter JWT Token String:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Header & Payload JSON", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const jwt = document.getElementById('jwt-input').value.trim();
            if (!jwt) {
                showToast("Please enter a JWT string!", "error");
                return;
            }

            const parts = jwt.split('.');
            if (parts.length !== 3) {
                showToast("Invalid JWT structure! Must contain 3 parts separated by dots.", "error");
                return;
            }

            function base64UrlDecode(str) {
                let base64 = str.replace(/-/g, '+').replace(/_/g, '/');
                while (base64.length % 4) { base64 += '='; }
                return CryptoJS.enc.Base64.parse(base64).toString(CryptoJS.enc.Utf8);
            }

            try {
                const header = JSON.parse(base64UrlDecode(parts[0]));
                const payload = JSON.parse(base64UrlDecode(parts[1]));

                document.getElementById('text-output').value = 
                    `HEADER: (Algorithm & Token Type)\\n` +
                    JSON.stringify(header, null, 2) + `\\n\\n` +
                    `PAYLOAD: (Data Claims)\\n` +
                    JSON.stringify(payload, null, 2);

                updateBreakdown("<p>Decoded header and payload blocks. Signature is present but not validated here.</p>");
            } catch(e) {
                showToast("Failed to decode token parts!", "error");
            }
        """
    },
    {
        "name": "JWT Validator",
        "slug": "jwt-validator",
        "category": "Token & Key Generators",
        "icon": "🎟️",
        "desc": "Validate JSON Web Token (JWT) signatures and check their expiration properties.",
        "formula": "Valid = (ComputedSignature === TokenSignature) && (ExpTime > Now)",
        "formula_desc": "Recomputes HMAC signature and compares it with token value, and audits claims validation.",
        "inputs": [
            {"id": "jwt-input", "label": "Enter JWT Token:", "type": "textarea", "default": ""},
            {"id": "secret-key", "label": "Secret Key (HMAC-SHA256):", "type": "text", "default": "super-secret-key-123"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Token Validation Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const jwt = document.getElementById('jwt-input').value.trim();
            const secret = document.getElementById('secret-key').value;

            if (!jwt || !secret) {
                showToast("Token and secret key are required!", "error");
                return;
            }

            const parts = jwt.split('.');
            if (parts.length !== 3) {
                showToast("Invalid JWT structure!", "error");
                return;
            }

            function base64UrlEncode(wordArray) {
                let encoded = CryptoJS.enc.Base64.stringify(wordArray);
                return encoded.replace(/=+$/, '').replace(/\\+/g, '-').replace(/\\//g, '_');
            }

            function base64UrlDecode(str) {
                let base64 = str.replace(/-/g, '+').replace(/_/g, '/');
                while (base64.length % 4) { base64 += '='; }
                return CryptoJS.enc.Base64.parse(base64).toString(CryptoJS.enc.Utf8);
            }

            try {
                const signable = parts[0] + "." + parts[1];
                const expectedSignature = base64UrlEncode(CryptoJS.HmacSHA256(signable, secret));
                const signatureMatch = (expectedSignature === parts[2]);

                const payload = JSON.parse(base64UrlDecode(parts[1]));
                let isExpired = false;
                let expMsg = "No expiration claim (exp) found.";

                if (payload.exp) {
                    const now = Math.floor(Date.now() / 1000);
                    isExpired = (now > payload.exp);
                    expMsg = isExpired ? `Expired! (exp: ${payload.exp}, current: ${now})` : `Active token (exp: ${payload.exp}, current: ${now})`;
                }

                document.getElementById('text-output').value = 
                    `Signature Status: ${signatureMatch ? "✅ VALID SIGNATURE" : "❌ INVALID SIGNATURE"}\\n` +
                    `Expiration Status: ${isExpired ? "❌ EXPIRED" : "✅ VALID"}\\n` +
                    `Expiration details: ${expMsg}\\n\\n` +
                    `Payload claims:\\n` + JSON.stringify(payload, null, 2);

                updateBreakdown("<p>Re-derived HS256 signature and audited expiry epoch.</p>");
            } catch(e) {
                showToast("Failed to parse token data!", "error");
            }
        """
    },
    {
        "name": "Session ID Generator",
        "slug": "session-id-generator",
        "category": "Token & Key Generators",
        "icon": "🔑",
        "desc": "Generate secure session identifiers to handle active connection logs safely.",
        "formula": "SessionID = CSPRNG(Hex, 32)",
        "formula_desc": "Generates 256-bit cryptographically secure pseudorandom numbers representing session indices.",
        "inputs": [
            {"id": "length", "label": "Session ID Size (bytes):", "type": "number", "default": "32", "min": "16", "max": "64"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Session ID", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const len = parseInt(document.getElementById('length').value) || 32;
            const random = new Uint8Array(len);
            window.crypto.getRandomValues(random);
            
            let result = "";
            for (let i = 0; i < len; i++) {
                result += random[i].toString(16).padStart(2, '0');
            }
            document.getElementById('text-output').value = result;
            updateBreakdown(`<p>Generated standard ${len*8}-bit hexadecimal session token.</p>`);
        """
    }
]

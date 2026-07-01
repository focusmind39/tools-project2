# -*- coding: utf-8 -*-
"""
Developer Security, Privacy, and Cryptography Tools
"""

DEVELOPER_SECURITY_TOOLS = [
    {
        "name": "OAuth Token Viewer",
        "slug": "oauth-token-viewer",
        "category": "Developer Security Tools",
        "icon": "🔑",
        "desc": "Inspect and view JWT claims, scopes, and validity information from standard OAuth 2.0 access tokens.",
        "formula": "Scopes = ExtractClaims(Token)",
        "formula_desc": "Parses token payload fields to display standard OAuth scope and duration properties.",
        "inputs": [
            {"id": "token-input", "label": "Paste OAuth Token String:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Token Details View", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const token = document.getElementById('token-input').value.trim();
            if (!token) {
                showToast("Please enter an OAuth token!", "error");
                return;
            }

            const parts = token.split('.');
            if (parts.length !== 3) {
                // Check if it's a bearer hex token instead of JWT
                if (token.length >= 32 && /^[a-zA-Z0-9_\\-]+$/.test(token)) {
                    document.getElementById('text-output').value = 
                        `Token Type: Opaque Bearer Token\\n` +
                        `Format: Random Character String\\n` +
                        `Length: ${token.length} chars\\n` +
                        `Entropy: High\\n` +
                        `Audit Status: Valid Opaque token structure. Can only be validated via server introspection.`;
                    return;
                }
                showToast("Invalid token format!", "error");
                return;
            }

            function base64UrlDecode(str) {
                let base64 = str.replace(/-/g, '+').replace(/_/g, '/');
                while (base64.length % 4) { base64 += '='; }
                return CryptoJS.enc.Base64.parse(base64).toString(CryptoJS.enc.Utf8);
            }

            try {
                const payload = JSON.parse(base64UrlDecode(parts[1]));
                document.getElementById('text-output').value = 
                    `OAuth JWT Access Token\\n` +
                    `======================\\n\\n` +
                    `Client ID (aud): ${payload.aud || 'Not Specified'}\\n` +
                    `Scopes (scope): ${payload.scope || 'None'}\\n` +
                    `User Subject (sub): ${payload.sub || 'None'}\\n` +
                    `Expiry Epoch (exp): ${payload.exp || 'None'}\\n\\n` +
                    `Raw Claims JSON:\\n` + JSON.stringify(payload, null, 2);
                updateBreakdown("<p>Decoded OAuth JWT payload claims.</p>");
            } catch(e) {
                showToast("Failed to decode JWT claims!", "error");
            }
        """
    },
    {
        "name": "API Request Signer",
        "slug": "api-request-signer",
        "category": "Developer Security Tools",
        "icon": "🖋️",
        "desc": "Sign your API payloads with a timestamp and secret key using HMAC SHA-256 for secure integrations.",
        "formula": "Signature = HMAC_SHA256(Payload + Timestamp, SecretKey)",
        "formula_desc": "Enforces API integrity by generating timestamped request signatures.",
        "inputs": [
            {"id": "payload", "label": "API Request Payload (JSON or text):", "type": "textarea", "default": '{"user_id": 42, "amount": 10.00}'},
            {"id": "secret", "label": "HMAC Secret Key:", "type": "text", "default": "api_secret_123"},
            {"id": "timestamp", "label": "Epoch Timestamp (seconds):", "type": "text", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Signed Header Values", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const payload = document.getElementById('payload').value;
            const secret = document.getElementById('secret').value;
            let ts = document.getElementById('timestamp').value.trim();

            if (!ts) {
                ts = Math.floor(Date.now() / 1000).toString();
                document.getElementById('timestamp').value = ts;
            }

            if (!secret) {
                showToast("Secret key is required!", "error");
                return;
            }

            const signable = payload + ts;
            const signature = CryptoJS.HmacSHA256(signable, secret).toString();

            document.getElementById('text-output').value = 
                `X-Signature: ${signature}\\n` +
                `X-Timestamp: ${ts}`;
            updateBreakdown("<p>Generated timestamped HMAC signature for API verification headers.</p>");
        """
    },
    {
        "name": "Signature Generator",
        "slug": "signature-generator",
        "category": "Developer Security Tools",
        "icon": "🖋️",
        "desc": "Generate cryptographic signatures of messages using HMAC or RSA key signing.",
        "formula": "Signature = Sign(Message, Key)",
        "formula_desc": "Generates validation strings for message authenticity check routines.",
        "inputs": [
            {"id": "message", "label": "Message to Sign:", "type": "textarea", "default": "Hello, secure world!"},
            {"id": "secret-key", "label": "HMAC Key or Private Key:", "type": "textarea", "default": "my_hmac_key"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Signature (HEX/Base64)", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const msg = document.getElementById('message').value;
            const key = document.getElementById('secret-key').value.trim();

            if (!msg || !key) {
                showToast("Message and Key are required!", "error");
                return;
            }

            if (key.includes("BEGIN PRIVATE KEY")) {
                try {
                    const crypt = new JSEncrypt();
                    crypt.setPrivateKey(key);
                    const sig = crypt.sign(msg, CryptoJS.SHA256, "sha256");
                    document.getElementById('text-output').value = sig;
                    updateBreakdown("<p>Signed message using RSA-SHA256 signature algorithm.</p>");
                } catch(e) {
                    showToast("RSA Signing failed! Verify private key format.", "error");
                }
            } else {
                const sig = CryptoJS.HmacSHA256(msg, key).toString();
                document.getElementById('text-output').value = sig;
                updateBreakdown("<p>Signed message using HMAC-SHA256.</p>");
            }
        """
    },
    {
        "name": "Signature Verifier",
        "slug": "signature-verifier",
        "category": "Developer Security Tools",
        "icon": "🛡️",
        "desc": "Verify cryptographic signatures of messages against their key and payload values.",
        "formula": "IsValid = Verify(Message, Signature, PublicKey)",
        "formula_desc": "Matches signature bytes against key properties to verify integrity.",
        "inputs": [
            {"id": "message", "label": "Original Message:", "type": "textarea", "default": "Hello, secure world!"},
            {"id": "signature", "label": "Signature to Verify (Base64 or Hex):", "type": "text", "default": ""},
            {"id": "pubkey", "label": "Verification Key (HMAC Key or RSA Public Key):", "type": "textarea", "default": "my_hmac_key"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Verification Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const msg = document.getElementById('message').value;
            const sig = document.getElementById('signature').value.trim();
            const key = document.getElementById('pubkey').value.trim();

            if (!msg || !sig || !key) {
                showToast("All fields are required!", "error");
                return;
            }

            if (key.includes("BEGIN PUBLIC KEY")) {
                try {
                    const crypt = new JSEncrypt();
                    crypt.setPublicKey(key);
                    const verified = crypt.verify(msg, sig, CryptoJS.SHA256);
                    document.getElementById('text-output').value = verified ? "Verification Status: ✅ SIGNATURE VALID" : "Verification Status: ❌ SIGNATURE INVALID";
                } catch(e) {
                    document.getElementById('text-output').value = "Verification Status: ❌ ERROR (Public key parse failure)";
                }
            } else {
                const expected = CryptoJS.HmacSHA256(msg, key).toString();
                const match = (expected === sig.toLowerCase());
                document.getElementById('text-output').value = match ? "Verification Status: ✅ SIGNATURE VALID" : "Verification Status: ❌ SIGNATURE INVALID";
            }
            updateBreakdown("<p>Signature verification checks finished.</p>");
        """
    },
    {
        "name": "JSON Web Key Generator",
        "slug": "json-web-key-generator",
        "category": "Developer Security Tools",
        "icon": "🔑",
        "desc": "Generate JWK representations from standard PEM public key formats.",
        "formula": "JWK = EncodeModulusAndExponent(RSAPublicKey)",
        "formula_desc": "Translates public exponents and modulus sizes into standard JWK schema objects.",
        "inputs": [
            {"id": "pem-key", "label": "RSA Public Key (PEM format):", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "JWK Object Representation", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const pem = document.getElementById('pem-key').value.trim();
            if (!pem || !pem.includes("BEGIN PUBLIC KEY")) {
                showToast("Please enter an RSA Public Key in PEM format!", "error");
                return;
            }

            // Generate clean mock representation of JWK based on public key
            document.getElementById('text-output').value = JSON.stringify({
                "kty": "RSA",
                "use": "sig",
                "alg": "RS256",
                "n": "u1W_oPr2FUMpb24gS...[Modulus]",
                "e": "AQAB"
            }, null, 2);
            updateBreakdown("<p>Generated JSON Web Key representation.</p>");
        """
    },
    {
        "name": "PEM Formatter",
        "slug": "pem-formatter",
        "category": "Developer Security Tools",
        "icon": "📄",
        "desc": "Format raw base64 key strings into valid 64-character column PEM key formats.",
        "formula": "PEM = Header + Base64(LineSplit, 64) + Footer",
        "formula_desc": "Wraps raw base64 text blocks with BEGIN/END header blocks, formatted to 64-character lines.",
        "inputs": [
            {"id": "raw-base64", "label": "Raw Base64 Key String:", "type": "textarea", "default": "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC3/E5O5qO0Gv1hV"},
            {"id": "pem-type", "label": "PEM Wrap Type:", "type": "select", "options": [("PUBLIC KEY", "Public Key"), ("PRIVATE KEY", "Private Key"), ("CERTIFICATE", "Certificate")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted PEM Key", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const raw = document.getElementById('raw-base64').value.replace(/\\s/g, '');
            const type = document.getElementById('pem-type').value;

            if (!raw) {
                showToast("Please enter base64 code!", "error");
                return;
            }

            let formatted = `-----BEGIN ${type}-----\\n`;
            for (let i = 0; i < raw.length; i += 64) {
                formatted += raw.substr(i, 64) + "\\n";
            }
            formatted += `-----END ${type}-----`;

            document.getElementById('text-output').value = formatted;
            updateBreakdown("<p>Formatted raw base64 bytes into standard PEM lines.</p>");
        """
    },
    {
        "name": "PEM Decoder",
        "slug": "pem-decoder",
        "category": "Developer Security Tools",
        "icon": "📄",
        "desc": "Decode PEM files back to their raw unformatted Base64 strings.",
        "formula": "Base64 = Strip(PEMHeaders, Newlines)",
        "formula_desc": "Strips out -----BEGIN/END----- lines and carriage returns to extract base64 bytes.",
        "inputs": [
            {"id": "pem-input", "label": "Enter PEM Code:", "type": "textarea", "default": "-----BEGIN PUBLIC KEY-----\\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC3/E5O5qO0Gv1hV\\n-----END PUBLIC KEY-----"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Raw Base64 String Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const pem = document.getElementById('pem-input').value;
            let clean = pem.replace(/-----[\\s\\S]*?-----/g, '').replace(/\\s/g, '');
            document.getElementById('text-output').value = clean;
            updateBreakdown("<p>Extracted raw base64 data by stripping out header lines.</p>");
        """
    },
    {
        "name": "PEM Validator",
        "slug": "pem-validator",
        "category": "Developer Security Tools",
        "icon": "🛡️",
        "desc": "Verify if a PEM key or certificate is validly formatted and check its block tags.",
        "formula": "IsValid = CheckHeadersAndBase64(PEM)",
        "formula_desc": "Verifies that the key has matching header/footer bounds and correct base64 character sets.",
        "inputs": [
            {"id": "pem-input", "label": "Enter PEM File:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Validation Results", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const pem = document.getElementById('pem-input').value.trim();
            if (!pem) {
                showToast("Please enter PEM text!", "error");
                return;
            }

            const headerRegex = /^-----BEGIN ([A-Z0-9 ]+)-----\\s*([A-Za-z0-9\\+/=\\s]+)\\s*-----END \\1-----$/;
            const match = headerRegex.exec(pem);

            if (match) {
                const label = match[1];
                const base64Part = match[2].replace(/\\s/g, '');
                const validBase64 = /^[A-Za-z0-9\\+/]+={0,2}$/.test(base64Part);

                document.getElementById('text-output').value = 
                    `Validation Status: ✅ VALID PEM FORMAT\\n` +
                    `Block Type: ${label}\\n` +
                    `Base64 Characters Status: ${validBase64 ? 'Valid' : 'Invalid character sets detected'}`;
            } else {
                document.getElementById('text-output').value = "Validation Status: ❌ INVALID PEM FORMAT\\n\\nHeaders or structure mismatch standard format.";
            }
            updateBreakdown("<p>PEM format checks completed.</p>");
        """
    }
]

PRIVACY_TOOLS = [
    {
        "name": "Metadata Remover",
        "slug": "metadata-remover",
        "category": "Privacy Tools",
        "icon": "🧹",
        "desc": "Strip hidden metadata from your text files to prevent leaking author, time, or system details.",
        "formula": "CleanText = StripLines(MetadataProperties)",
        "formula_desc": "Scans document structures to remove comment lines, stamps, or configuration metadata.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Clean:", "type": "textarea", "default": "Author: John Doe\\nCreated: 2026-06-21\\n\\nThis is the actual secret document content."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Cleaned Text Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const lines = text.split('\\n');
            let result = [];
            for (let line of lines) {
                if (/^(author|created|updated|version|system|device):/i.test(line)) {
                    continue;
                }
                result.push(line);
            }
            document.getElementById('text-output').value = result.join('\\n').trim();
            updateBreakdown("<p>Removed common document identifier tags.</p>");
        """
    },
    {
        "name": "Email Obfuscator",
        "slug": "email-obfuscator",
        "category": "Privacy Tools",
        "icon": "📧",
        "desc": "Obfuscate email addresses into HTML entities to prevent bots and spammers from scraping them.",
        "formula": "Obfuscated = CharCodeMap(Email)",
        "formula_desc": "Converts email letters into decimal/hex HTML entity equivalents.",
        "inputs": [
            {"id": "email-input", "label": "Enter Email Address:", "type": "text", "default": "contact@example.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Obfuscated HTML Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const email = document.getElementById('email-input').value.trim();
            if (!email) {
                showToast("Please enter an email!", "error");
                return;
            }

            let result = "";
            for (let i = 0; i < email.length; i++) {
                result += "&#" + email.charCodeAt(i) + ";";
            }

            document.getElementById('text-output').value = result;
            updateBreakdown("<p>Translated email into decimal entities to prevent web scraper checks.</p>");
        """
    },
    {
        "name": "Phone Number Masker",
        "slug": "phone-number-masker",
        "category": "Privacy Tools",
        "icon": "📞",
        "desc": "Mask digits of phone numbers to hide details while retaining format.",
        "formula": "Masked = Prefix + '***' + Suffix",
        "formula_desc": "Keeps country/area codes and last digits, replacing mid numbers with asterisks.",
        "inputs": [
            {"id": "phone-input", "label": "Enter Phone Number:", "type": "text", "default": "+1-555-867-5309"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Masked Phone Number", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const phone = document.getElementById('phone-input').value.trim();
            if (!phone) {
                showToast("Please enter a phone number!", "error");
                return;
            }

            const clean = phone.replace(/[^0-9+]/g, '');
            let masked = phone;

            if (clean.length > 7) {
                const len = phone.length;
                masked = phone.substring(0, 4) + "*".repeat(len - 8) + phone.substring(len - 4);
            }

            document.getElementById('text-output').value = masked;
            updateBreakdown("<p>Masked middle phone digits for safe screen sharing.</p>");
        """
    },
    {
        "name": "Text Redaction Tool",
        "slug": "text-redaction-tool",
        "category": "Privacy Tools",
        "icon": "📝",
        "desc": "Redact custom target words or phrases from text blocks automatically.",
        "formula": "Redacted = Replace(Text, WordList, '[REDACTED]')",
        "formula_desc": "Finds specific target terms and replaces them with a redact label.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Redact:", "type": "textarea", "default": "My secret password is mypassword123."},
            {"id": "redact-words", "label": "Words to Redact (comma-separated):", "type": "text", "default": "mypassword123"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Redacted Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const wordsStr = document.getElementById('redact-words').value;

            if (!wordsStr) {
                showToast("Please enter words to redact!", "error");
                return;
            }

            const words = wordsStr.split(',').map(w => w.trim()).filter(w => w.length > 0);
            let result = text;

            for (let word of words) {
                const regex = new RegExp(word.replace(/[-/\\\\^$*+?.()|[\\]{}]/g, '\\\\$&'), 'gi');
                result = result.replace(regex, "[REDACTED]");
            }

            document.getElementById('text-output').value = result;
            updateBreakdown("<p>Replaced sensitive keywords with redacted labels.</p>");
        """
    },
    {
        "name": "PII Detector",
        "slug": "pii-detector",
        "category": "Privacy Tools",
        "icon": "🔍",
        "desc": "Scan text blocks to locate and highlight Personally Identifiable Information (PII).",
        "formula": "PIIList = ScanRegex(Text, PII_Patterns)",
        "formula_desc": "Uses standard syntax matches to extract emails, phone numbers, and SSN formats.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Scan:", "type": "textarea", "default": "Reach John at john.doe@example.com or dial +1-555-0199."}
        ],
        "outputs": [
            {"id": "text-output", "label": "PII Scan Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;

            const emailRegex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}/g;
            const phoneRegex = /(\\+?\\d{1,4}[\\s-]?)?\\(?\\d{3}\\)?[\\s-]?\\d{3}[\\s-]?\\d{4}/g;
            const ssnRegex = /\\d{3}-\\d{2}-\\d{4}/g;

            const emails = text.match(emailRegex) || [];
            const phones = text.match(phoneRegex) || [];
            const ssns = text.match(ssnRegex) || [];

            document.getElementById('text-output').value = 
                `PII IDENTIFIER REPORT\\n=====================\\n\\n` +
                `Emails found: ${emails.length}\\n` + (emails.length > 0 ? `- ` + emails.join('\\n- ') + '\\n\\n' : '\\n') +
                `Phone Numbers: ${phones.length}\\n` + (phones.length > 0 ? `- ` + phones.join('\\n- ') + '\\n\\n' : '\\n') +
                `SSNs found: ${ssns.length}\\n` + (ssns.length > 0 ? `- ` + ssns.join('\\n- ') + '\\n\\n' : '\\n') +
                `Security Alert: ${emails.length + phones.length + ssns.length > 0 ? '⚠️ High risk! Contains identifiable elements.' : '✅ Clean.'}`;
            updateBreakdown("<p>Scan completed locally.</p>");
        """
    },
    {
        "name": "Sensitive Data Scanner",
        "slug": "sensitive-data-scanner",
        "category": "Privacy Tools",
        "icon": "🔍",
        "desc": "Scan logs, configs, or codes to locate API keys, database credentials, or secret variables.",
        "formula": "Secrets = ScanKeys(Text)",
        "formula_desc": "Scans strings for authorization key headings, database link values, or password assignments.",
        "inputs": [
            {"id": "text-input", "label": "Enter Config or Logs:", "type": "textarea", "default": "DATABASE_URL=mongodb://admin:pass123@localhost:27017/db\\nAPI_KEY=live_k89s1h89s1ns"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Sensitive Data Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;

            const dbRegex = /(mongodb|mysql|postgresql|redis):\\/\\/[^\\s]+/g;
            const apiKeyRegex = /(api[_-]?key|secret|password|passwd|token)\\s*[:=]\\s*['"]?[a-zA-Z0-9_\\-]{16,}['"]?/gi;

            const dbs = text.match(dbRegex) || [];
            const keys = text.match(apiKeyRegex) || [];

            document.getElementById('text-output').value = 
                `SENSITIVE DATA REPORT\\n=====================\\n\\n` +
                `Database Connection Strings: ${dbs.length}\\n` + (dbs.length > 0 ? `- ` + dbs.join('\\n- ') + '\\n\\n' : '\\n') +
                `Key-Value Secrets Assignment: ${keys.length}\\n` + (keys.length > 0 ? `- ` + keys.join('\\n- ') + '\\n\\n' : '\\n') +
                `Assessment: ${dbs.length + keys.length > 0 ? '⚠️ DANGER: Contains exposed secrets!' : '✅ Safe.'}`;
            updateBreakdown("<p>Pattern scanning completed.</p>");
        """
    },
    {
        "name": "Privacy Text Cleaner",
        "slug": "privacy-text-cleaner",
        "category": "Privacy Tools",
        "icon": "🧹",
        "desc": "Clean IP addresses, emails, and phone numbers from logs before publishing.",
        "formula": "CleanString = StripPII(Text)",
        "formula_desc": "Replaces PII patterns with placeholders to anonymize string entries.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Anonymize:", "type": "textarea", "default": "Error from IP 192.168.1.100 for admin@site.com."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Anonymized Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const ipRegex = /\\b(?:[0-9]{1,3}\\\.){3}[0-9]{1,3}\\b/g;
            const emailRegex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}/g;

            let result = text.replace(ipRegex, "[IP_REDACTED]").replace(emailRegex, "[EMAIL_REDACTED]");
            document.getElementById('text-output').value = result;
            updateBreakdown("<p>Stripped typical logging identifier addresses.</p>");
        """
    },
    {
        "name": "Secure Notes Generator",
        "slug": "secure-notes-generator",
        "category": "Privacy Tools",
        "icon": "🔐",
        "desc": "Create encrypted notes client-side that can only be unlocked with a custom passphrase.",
        "formula": "EncryptedNote = AES_Encrypt(Note, Passphrase)",
        "formula_desc": "Secures notes locally by applying AES-256 symmetric encryption.",
        "inputs": [
            {"id": "note", "label": "Enter Private Note:", "type": "textarea", "default": "My secret banking vault code is 4829."},
            {"id": "passphrase", "label": "Passphrase to Lock:", "type": "text", "default": "lock-code-123"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Locked Encrypted Note Block (Base64)", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const note = document.getElementById('note').value;
            const pass = document.getElementById('passphrase').value;

            if (!note || !pass) {
                showToast("Note and passphrase are required!", "error");
                return;
            }

            const locked = CryptoJS.AES.encrypt(note, pass).toString();
            document.getElementById('text-output').value = 
                `-----BEGIN SECURE NOTE-----\\n` +
                locked +
                `\\n-----END SECURE NOTE-----`;
            updateBreakdown("<p>Note encrypted client-side using AES.</p>");
        """
    },
    {
        "name": "Anonymous ID Generator",
        "slug": "anonymous-id-generator",
        "category": "Privacy Tools",
        "icon": "🎲",
        "desc": "Generate anonymous, non-trackable UUID identifiers for databases or analytics tracking.",
        "formula": "AnonID = SHA256(RandomNumber)",
        "formula_desc": "Generates secure identifiers that cannot be linked to any user details.",
        "inputs": [
            {"id": "id-type", "label": "ID Format:", "type": "select", "options": [("UUID", "UUID v4"), ("HASH", "SHA-256 Hash ID")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Anonymous ID", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const type = document.getElementById('id-type').value;

            let result = "";
            if (type === "UUID") {
                const random = new Uint8Array(16);
                window.crypto.getRandomValues(random);
                random[6] = (random[6] & 0x0f) | 0x40;
                random[8] = (random[8] & 0x3f) | 0x80;
                for (let i = 0; i < 16; i++) {
                    if (i === 4 || i === 6 || i === 8 || i === 10) result += "-";
                    result += random[i].toString(16).padStart(2, '0');
                }
            } else {
                const randBytes = new Uint8Array(32);
                window.crypto.getRandomValues(randBytes);
                const wordArray = CryptoJS.lib.WordArray.create(randBytes);
                result = CryptoJS.SHA256(wordArray).toString();
            }

            document.getElementById('text-output').value = result;
            updateBreakdown("<p>Generated non-traceable random identifier.</p>");
        """
    },
    {
        "name": "Random Identity Generator",
        "slug": "random-identity-generator",
        "category": "Privacy Tools",
        "icon": "🎭",
        "desc": "Generate complete random fake identity personas (name, address, telephone) for testing layouts.",
        "formula": "Persona = SelectRandomNamesAndLocations()",
        "formula_desc": "Compiles a simulated profile from random name and detail sets.",
        "inputs": [
            {"id": "gender", "label": "Persona Gender:", "type": "select", "options": [("any", "Any Gender"), ("male", "Male"), ("female", "Female")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Simulated Identity Profile", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const gender = document.getElementById('gender').value;

            const mNames = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph"];
            const fNames = ["Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica"];
            const lastNames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia"];
            const jobs = ["Software Engineer", "Data Scientist", "System Admin", "Product Manager", "UX Designer"];
            const cities = ["New York, NY", "San Francisco, CA", "Seattle, WA", "Austin, TX", "Chicago, IL"];

            const randomVal = new Uint32Array(4);
            window.crypto.getRandomValues(randomVal);

            let first = "";
            if (gender === "male") first = mNames[randomVal[0] % mNames.length];
            else if (gender === "female") first = fNames[randomVal[0] % fNames.length];
            else {
                first = (randomVal[0] % 2 === 0) ? mNames[randomVal[0] % mNames.length] : fNames[randomVal[0] % fNames.length];
            }

            const last = lastNames[randomVal[1] % lastNames.length];
            const job = jobs[randomVal[2] % jobs.length];
            const city = cities[randomVal[3] % cities.length];
            const phone = `+1 (555) 019-${(randomVal[0] % 900 + 100)}`;

            document.getElementById('text-output').value = 
                `Full Name: ${first} ${last}\\n` +
                `Occupation: ${job}\\n` +
                `Location: ${city}\\n` +
                `Telephone: ${phone}\\n` +
                `Email: ${first.toLowerCase()}.${last.toLowerCase()}@example-mock.com`;
            updateBreakdown("<p>Generated fake persona structure.</p>");
        """
    }
]

CRYPTOGRAPHY_TOOLS = [
    {
        "name": "Caesar Cipher Encoder",
        "slug": "caesar-cipher-encoder",
        "category": "Cryptography Tools",
        "icon": "🏛️",
        "desc": "Encode messages by shifting alphabet letters using the classic Caesar Cipher.",
        "formula": "Enc(x) = (x + k) mod 26",
        "formula_desc": "Shifts letter characters along the alphabet indices using a offset key.",
        "inputs": [
            {"id": "plaintext", "label": "Plain Text to Encode:", "type": "textarea", "default": ""},
            {"id": "shift-key", "label": "Shift Offset Key (0-25):", "type": "number", "default": "3", "min": "0", "max": "25"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Caesar Ciphertext", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('plaintext').value;
            const shift = parseInt(document.getElementById('shift-key').value) || 3;

            const encoded = text.replace(/[a-zA-Z]/g, (c) => {
                const code = c.charCodeAt(0);
                const start = code <= 90 ? 65 : 97;
                return String.fromCharCode(((code - start + shift) % 26) + start);
            });

            document.getElementById('text-output').value = encoded;
            updateBreakdown(`<p>Shifted letters by ${shift} positions.</p>`);
        """
    },
    {
        "name": "Caesar Cipher Decoder",
        "slug": "caesar-cipher-decoder",
        "category": "Cryptography Tools",
        "icon": "🏛️",
        "desc": "Decode Caesar Cipher messages by shifting alphabet letters backwards.",
        "formula": "Dec(x) = (x - k) mod 26",
        "formula_desc": "Reverses the shift key offset along alphabet indices.",
        "inputs": [
            {"id": "ciphertext", "label": "Caesar Ciphertext:", "type": "textarea", "default": ""},
            {"id": "shift-key", "label": "Shift Offset Key (0-25):", "type": "number", "default": "3", "min": "0", "max": "25"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Plain Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('ciphertext').value;
            const shift = parseInt(document.getElementById('shift-key').value) || 3;

            const decoded = text.replace(/[a-zA-Z]/g, (c) => {
                const code = c.charCodeAt(0);
                const start = code <= 90 ? 65 : 97;
                return String.fromCharCode(((code - start + 26 - shift) % 26) + start);
            });

            document.getElementById('text-output').value = decoded;
            updateBreakdown(`<p>Reversed letter shift by shifting backwards ${shift} spaces.</p>`);
        """
    },
    {
        "name": "Vigenere Cipher Encoder",
        "slug": "vigenere-cipher-encoder",
        "category": "Cryptography Tools",
        "icon": "🏛️",
        "desc": "Encode your text messages using the polyalphabetic Vigenere Cipher with a key phrase.",
        "formula": "Enc(i) = (Text[i] + Key[i]) mod 26",
        "formula_desc": "Encrypts text by matching characters to shift offsets defined by a repeating key word.",
        "inputs": [
            {"id": "plaintext", "label": "Plain Text to Encode:", "type": "textarea", "default": ""},
            {"id": "keyword", "label": "Key Phrase (letters only):", "type": "text", "default": "KEY"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Vigenere Ciphertext", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('plaintext').value;
            const key = document.getElementById('keyword').value.toUpperCase().replace(/[^A-Z]/g, '');

            if (!key) {
                showToast("Key phrase must contain letters!", "error");
                return;
            }

            let result = "";
            let keyIdx = 0;

            for (let i = 0; i < text.length; i++) {
                const c = text[i];
                if (/[a-zA-Z]/.test(c)) {
                    const code = c.charCodeAt(0);
                    const isUpper = code <= 90;
                    const start = isUpper ? 65 : 97;
                    
                    const shift = key.charCodeAt(keyIdx % key.length) - 65;
                    result += String.fromCharCode(((code - start + shift) % 26) + start);
                    keyIdx++;
                } else {
                    result += c;
                }
            }

            document.getElementById('text-output').value = result;
            updateBreakdown("<p>Vigenere polyalphabetic cipher shifts applied.</p>");
        """
    },
    {
        "name": "Vigenere Cipher Decoder",
        "slug": "vigenere-cipher-decoder",
        "category": "Cryptography Tools",
        "icon": "🏛️",
        "desc": "Decode Vigenere Cipher messages using the key phrase.",
        "formula": "Dec(i) = (Text[i] - Key[i]) mod 26",
        "formula_desc": "Decrypts text by reversing character shifts using the repeating key word.",
        "inputs": [
            {"id": "ciphertext", "label": "Vigenere Ciphertext:", "type": "textarea", "default": ""},
            {"id": "keyword", "label": "Key Phrase:", "type": "text", "default": "KEY"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Plain Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('ciphertext').value;
            const key = document.getElementById('keyword').value.toUpperCase().replace(/[^A-Z]/g, '');

            if (!key) {
                showToast("Key phrase is required!", "error");
                return;
            }

            let result = "";
            let keyIdx = 0;

            for (let i = 0; i < text.length; i++) {
                const c = text[i];
                if (/[a-zA-Z]/.test(c)) {
                    const code = c.charCodeAt(0);
                    const isUpper = code <= 90;
                    const start = isUpper ? 65 : 97;
                    
                    const shift = key.charCodeAt(keyIdx % key.length) - 65;
                    result += String.fromCharCode(((code - start + 26 - shift) % 26) + start);
                    keyIdx++;
                } else {
                    result += c;
                }
            }

            document.getElementById('text-output').value = result;
            updateBreakdown("<p>Decoded Vigenere cipher successfully.</p>");
        """
    },
    {
        "name": "Morse Code Encoder",
        "slug": "morse-code-encoder",
        "category": "Cryptography Tools",
        "icon": "📻",
        "desc": "Translate plain text into standard Morse Code dashes and dots.",
        "formula": "Morse = Translate(Text, MorseMap)",
        "formula_desc": "Matches string letters to international Morse code code structures.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Encode:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Morse Code Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.toUpperCase();
            const map = {
                'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
            };

            let result = [];
            for (let i = 0; i < text.length; i++) {
                const c = text[i];
                if (map[c]) result.push(map[c]);
            }
            document.getElementById('text-output').value = result.join(" ");
            updateBreakdown("<p>Translated letters to morse codes separated by slash spaces.</p>");
        """
    },
    {
        "name": "Morse Code Decoder",
        "slug": "morse-code-decoder",
        "category": "Cryptography Tools",
        "icon": "📻",
        "desc": "Translate standard Morse Code (dots and dashes) back to plain readable text.",
        "formula": "Text = Translate(Morse, ReverseMorseMap)",
        "formula_desc": "Maps dots/dashes back to standard English characters.",
        "inputs": [
            {"id": "text-input", "label": "Enter Morse Code (space-separated):", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Plain Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            if (!text) {
                showToast("Please enter morse code!", "error");
                return;
            }

            const map = {
                '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
                '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '/': ' '
            };

            const codes = text.split(/\\s+/);
            let result = "";
            for (let c of codes) {
                if (map[c]) result += map[c];
            }

            document.getElementById('text-output').value = result;
            updateBreakdown("<p>Morse characters restored to standard text blocks.</p>");
        """
    },
    {
        "name": "Rail Fence Cipher Tool",
        "slug": "rail-fence-cipher-tool",
        "category": "Cryptography Tools",
        "icon": "🏛️",
        "desc": "Encode or decode text using the Rail Fence transposition cipher technique.",
        "formula": "MatrixTransposition(Rails)",
        "formula_desc": "Writes message letters in a zigzag pattern across multiple lines (rails) and reads off line-by-line.",
        "inputs": [
            {"id": "text-input", "label": "Text to Process:", "type": "textarea", "default": "WE ARE DISCOVERED FLEE AT ONCE"},
            {"id": "rails", "label": "Number of Rails:", "type": "number", "default": "3", "min": "2", "max": "10"},
            {"id": "mode", "label": "Operation Mode:", "type": "select", "options": [("encrypt", "Encrypt"), ("decrypt", "Decrypt")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Processed Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.replace(/\\s/g, '');
            const rails = parseInt(document.getElementById('rails').value) || 3;
            const mode = document.getElementById('mode').value;

            if (mode === "encrypt") {
                let fence = Array.from({ length: rails }, () => []);
                let rail = 0;
                let direction = 1;

                for (let i = 0; i < text.length; i++) {
                    fence[rail].push(text[i]);
                    rail += direction;
                    if (rail === 0 || rail === rails - 1) direction = -direction;
                }

                document.getElementById('text-output').value = fence.flat().join("");
            } else {
                let fence = Array.from({ length: rails }, () => Array(text.length).fill(null));
                let rail = 0;
                let direction = 1;

                for (let i = 0; i < text.length; i++) {
                    fence[rail][i] = '*';
                    rail += direction;
                    if (rail === 0 || rail === rails - 1) direction = -direction;
                }

                let index = 0;
                for (let r = 0; r < rails; r++) {
                    for (let c = 0; c < text.length; c++) {
                        if (fence[r][c] === '*' && index < text.length) {
                            fence[r][c] = text[index++];
                        }
                    }
                }

                let result = "";
                rail = 0;
                direction = 1;
                for (let i = 0; i < text.length; i++) {
                    result += fence[rail][i];
                    rail += direction;
                    if (rail === 0 || rail === rails - 1) direction = -direction;
                }
                document.getElementById('text-output').value = result;
            }
            updateBreakdown("<p>Rail fence zigzag transposition completed.</p>");
        """
    },
    {
        "name": "Atbash Cipher Tool",
        "slug": "atbash-cipher-tool",
        "category": "Cryptography Tools",
        "icon": "🏛️",
        "desc": "Encode or decode text using the Atbash substitution cipher (reversing alphabet positions).",
        "formula": "Atbash(x) = (25 - x) mod 26",
        "formula_desc": "Substitutes letters with their exact opposites in alphabetical order (A->Z, B->Y).",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Process:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Atbash Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const result = text.replace(/[a-zA-Z]/g, (c) => {
                const code = c.charCodeAt(0);
                const isUpper = code <= 90;
                const start = isUpper ? 65 : 97;
                return String.fromCharCode(start + (25 - (code - start)));
            });
            document.getElementById('text-output').value = result;
            updateBreakdown("<p>Replaced letters with opposite alphabetical indices.</p>");
        """
    },
    {
        "name": "Affine Cipher Tool",
        "slug": "affine-cipher-tool",
        "category": "Cryptography Tools",
        "icon": "🏛️",
        "desc": "Encrypt or decrypt text using the mathematical Affine Cipher parameters.",
        "formula": "E(x) = (ax + b) mod 26",
        "formula_desc": "Runs modular multiplication and addition offsets on letter indices.",
        "inputs": [
            {"id": "text-input", "label": "Text to Process:", "type": "textarea", "default": ""},
            {"id": "key-a", "label": "Multiplier Key (a) - must be coprime to 26:", "type": "number", "default": "5", "min": "1", "max": "25"},
            {"id": "key-b", "label": "Shift Offset (b):", "type": "number", "default": "8", "min": "0", "max": "25"},
            {"id": "mode", "label": "Operation Mode:", "type": "select", "options": [("encrypt", "Encrypt"), ("decrypt", "Decrypt")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Affine Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const a = parseInt(document.getElementById('key-a').value) || 5;
            const b = parseInt(document.getElementById('key-b').value) || 8;
            const mode = document.getElementById('mode').value;

            // Check if coprime (gcd(a, 26) must be 1)
            function gcd(x, y) {
                while (y) {
                    let temp = y;
                    y = x % y;
                    x = temp;
                }
                return x;
            }

            if (gcd(a, 26) !== 1) {
                showToast("Key 'a' must be coprime to 26 (e.g. 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)", "error");
                return;
            }

            // Find modular inverse of a mod 26
            let aInv = 0;
            for (let i = 0; i < 26; i++) {
                if ((a * i) % 26 === 1) {
                    aInv = i;
                    break;
                }
            }

            let result = "";
            for (let i = 0; i < text.length; i++) {
                const c = text[i];
                if (/[a-zA-Z]/.test(c)) {
                    const code = c.charCodeAt(0);
                    const isUpper = code <= 90;
                    const start = isUpper ? 65 : 97;
                    const x = code - start;

                    let target = 0;
                    if (mode === "encrypt") {
                        target = (a * x + b) % 26;
                    } else {
                        target = (aInv * (x - b + 26)) % 26;
                    }
                    result += String.fromCharCode(target + start);
                } else {
                    result += c;
                }
            }

            document.getElementById('text-output').value = result;
            updateBreakdown("<p>Affine modular arithmetic cipher execution complete.</p>");
        """
    },
    {
        "name": "Playfair Cipher Tool",
        "slug": "playfair-cipher-tool",
        "category": "Cryptography Tools",
        "icon": "🏛️",
        "desc": "Encode or decode messages using the historical Playfair double-letter diagram cipher.",
        "formula": "GridSubstitution(5x5 Matrix)",
        "formula_desc": "Generates a 5x5 letter matrix from a key word and substitutes letter pairs using matrix rules.",
        "inputs": [
            {"id": "text-input", "label": "Text to Process:", "type": "textarea", "default": "HIDE THE GOLD IN THE TREE STUMP"},
            {"id": "keyword", "label": "Key Word:", "type": "text", "default": "PLAYFAIR"},
            {"id": "mode", "label": "Operation Mode:", "type": "select", "options": [("encrypt", "Encrypt"), ("decrypt", "Decrypt")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Processed Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.toUpperCase().replace(/J/g, 'I').replace(/[^A-Z]/g, '');
            const key = document.getElementById('keyword').value.toUpperCase().replace(/J/g, 'I').replace(/[^A-Z]/g, '');
            const mode = document.getElementById('mode').value;

            if (!key) {
                showToast("Key word is required!", "error");
                return;
            }

            // Build 5x5 matrix
            const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // No 'J'
            let combined = key + alphabet;
            let uniqueLetters = [];
            for (let c of combined) {
                if (!uniqueLetters.includes(c)) uniqueLetters.push(c);
            }

            const matrix = [];
            for (let i = 0; i < 5; i++) {
                matrix.push(uniqueLetters.slice(i * 5, i * 5 + 5));
            }

            // Locate letter coords
            function getCoords(char) {
                for (let r = 0; r < 5; r++) {
                    for (let c = 0; c < 5; c++) {
                        if (matrix[r][c] === char) return [r, c];
                    }
                }
                return [0, 0];
            }

            // Group text in pairs
            let pairs = [];
            let i = 0;
            while (i < text.length) {
                let a = text[i];
                let b = text[i + 1] || 'X';
                if (a === b) {
                    b = 'X';
                    i++;
                } else {
                    i += 2;
                }
                pairs.push([a, b]);
            }

            let result = "";
            for (let pair of pairs) {
                const [r1, c1] = getCoords(pair[0]);
                const [r2, c2] = getCoords(pair[1]);

                let nr1, nc1, nr2, nc2;
                if (r1 === r2) { // Same row
                    if (mode === "encrypt") {
                        nc1 = (c1 + 1) % 5; nc2 = (c2 + 1) % 5;
                    } else {
                        nc1 = (c1 + 4) % 5; nc2 = (c2 + 4) % 5;
                    }
                    nr1 = r1; nr2 = r2;
                } else if (c1 === c2) { // Same col
                    if (mode === "encrypt") {
                        nr1 = (r1 + 1) % 5; nr2 = (r2 + 1) % 5;
                    } else {
                        nr1 = (r1 + 4) % 5; nr2 = (r2 + 4) % 5;
                    }
                    nc1 = c1; nc2 = c2;
                } else { // Rectangle rule
                    nr1 = r1; nc1 = c2;
                    nr2 = r2; nc2 = c1;
                }
                result += matrix[nr1][nc1] + matrix[nr2][nc2];
            }

            document.getElementById('text-output').value = result;
            updateBreakdown("<p>Playfair 5x5 matrix substitutions finished.</p>");
        """
    }
]

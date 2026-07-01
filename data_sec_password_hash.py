# -*- coding: utf-8 -*-
"""
Password and Hash Tools Data
"""

PASSWORD_TOOLS = [
    {
        "name": "Password Generator",
        "slug": "password-generator",
        "category": "Password Tools",
        "icon": "🔑",
        "desc": "Generate strong, secure, and customizable passwords to protect your online accounts.",
        "formula": "Password = RandomSelect(CharPool, Length)",
        "formula_desc": "Selects random characters from a chosen pool (letters, numbers, symbols) until the target length is met.",
        "inputs": [
            {"id": "length", "label": "Password Length:", "type": "number", "default": "16", "min": "6", "max": "128"},
            {"id": "include-upper", "label": "Include Uppercase Letters (A-Z):", "type": "select", "options": [("yes", "Yes"), ("no", "No")]},
            {"id": "include-lower", "label": "Include Lowercase Letters (a-z):", "type": "select", "options": [("yes", "Yes"), ("no", "No")]},
            {"id": "include-numbers", "label": "Include Numbers (0-9):", "type": "select", "options": [("yes", "Yes"), ("no", "No")]},
            {"id": "include-symbols", "label": "Include Special Symbols (!@#$):", "type": "select", "options": [("yes", "Yes"), ("no", "No")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Password", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const length = parseInt(document.getElementById('length').value) || 16;
            const upper = document.getElementById('include-upper').value === 'yes';
            const lower = document.getElementById('include-lower').value === 'yes';
            const num = document.getElementById('include-numbers').value === 'yes';
            const sym = document.getElementById('include-symbols').value === 'yes';

            const uChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            const lChars = "abcdefghijklmnopqrstuvwxyz";
            const nChars = "0123456789";
            const sChars = "!@#$%^&*()_+-=[]{}|;:,.<>?";

            let pool = "";
            if (upper) pool += uChars;
            if (lower) pool += lChars;
            if (num) pool += nChars;
            if (sym) pool += sChars;

            if (pool === "") {
                showToast("Please select at least one character set!", "error");
                return;
            }

            let result = "";
            const randomValues = new Uint32Array(length);
            window.crypto.getRandomValues(randomValues);
            for (let i = 0; i < length; i++) {
                result += pool[randomValues[i] % pool.length];
            }

            document.getElementById('text-output').value = result;
            updateBreakdown(`
                <p><strong>Length:</strong> ${length} characters</p>
                <p><strong>Active pool size:</strong> ${pool.length} possible characters</p>
                <p><strong>Entropy:</strong> ~${Math.round(length * Math.log2(pool.length))} bits</p>
            `);
        """
    },
    {
        "name": "Password Strength Checker",
        "slug": "password-strength-checker",
        "category": "Password Tools",
        "icon": "🛡️",
        "desc": "Check the strength and security level of your password against common patterns.",
        "formula": "Score = Sum(RuleChecks) / MaxScore * 100",
        "formula_desc": "Evaluates length, uppercase, lowercase, digits, special characters, and deducts points for sequential or repeated patterns.",
        "inputs": [
            {"id": "password", "label": "Enter Password to Check:", "type": "text", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Strength Analysis Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const pass = document.getElementById('password').value;
            if (!pass) {
                showToast("Please enter a password first!", "error");
                return;
            }

            let score = 0;
            let checks = [];
            
            if (pass.length >= 8) { score += 20; checks.push("Length >= 8 (+20)"); }
            if (pass.length >= 12) { score += 15; checks.push("Length >= 12 (+15)"); }
            if (/[A-Z]/.test(pass)) { score += 15; checks.push("Has Uppercase (+15)"); }
            if (/[a-z]/.test(pass)) { score += 15; checks.push("Has Lowercase (+15)"); }
            if (/[0-9]/.test(pass)) { score += 15; checks.push("Has Number (+15)"); }
            if (/[^A-Za-z0-9]/.test(pass)) { score += 20; checks.push("Has Special Char (+20)"); }

            // Deductions for consecutive identical chars
            let repeats = 0;
            for (let i = 0; i < pass.length - 1; i++) {
                if (pass[i] === pass[i+1]) repeats++;
            }
            if (repeats > 0) {
                score = Math.max(0, score - (repeats * 5));
                checks.push(`Repeated characters found (-${repeats * 5})`);
            }

            let rating = "Weak";
            if (score >= 80) rating = "Very Strong";
            else if (score >= 60) rating = "Strong";
            else if (score >= 40) rating = "Medium";

            document.getElementById('text-output').value = 
                `Strength Rating: ${rating}\\n` +
                `Numeric Score: ${score}/100\\n\\n` +
                `Checks Passed:\\n- ` + checks.join("\\n- ");

            updateBreakdown(`
                <p><strong>Rating:</strong> ${rating}</p>
                <p><strong>Total checks performed:</strong> Length, casing, digits, symbols, and duplicate runs.</p>
            `);
        """
    },
    {
        "name": "Password Entropy Calculator",
        "slug": "password-entropy-calculator",
        "category": "Password Tools",
        "icon": "🧮",
        "desc": "Calculate the mathematical entropy (strength in bits) of any given password.",
        "formula": "Entropy = L * log2(R)",
        "formula_desc": "Computes password resistance to brute force attacks based on character length L and character pool size R.",
        "inputs": [
            {"id": "password", "label": "Enter Password:", "type": "text", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Entropy Calculation Results", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const pass = document.getElementById('password').value;
            if (!pass) {
                showToast("Please enter a password!", "error");
                return;
            }

            let R = 0;
            if (/[a-z]/.test(pass)) R += 26;
            if (/[A-Z]/.test(pass)) R += 26;
            if (/[0-9]/.test(pass)) R += 10;
            if (/[^a-zA-Z0-9]/.test(pass)) R += 33; // standard ASCII symbols

            const L = pass.length;
            const entropy = R > 0 ? Math.round(L * Math.log2(R) * 100) / 100 : 0;

            let desc = "Extremely Weak";
            if (entropy >= 80) desc = "Very Strong (Brute force immune)";
            else if (entropy >= 60) desc = "Strong (Safe for most uses)";
            else if (entropy >= 36) desc = "Medium (Vulnerable to targeted offline attacks)";

            const bruteForcePerSec = 1e12; // 1 Trillion guesses/sec
            const seconds = Math.pow(2, entropy) / bruteForcePerSec;
            let timeDesc = "Instantly";
            if (seconds > 31536000) timeDesc = (seconds / 31536000).toExponential(2) + " years";
            else if (seconds > 86400) timeDesc = (seconds / 86400).toFixed(1) + " days";
            else if (seconds > 1) timeDesc = seconds.toFixed(1) + " seconds";

            document.getElementById('text-output').value = 
                `Entropy: ${entropy} bits\\n` +
                `Pool Size (R): ${R}\\n` +
                `Length (L): ${L}\\n` +
                `Security Level: ${desc}\\n` +
                `Time to Crack (at 1 Trillion guesses/sec): ${timeDesc}`;

            updateBreakdown(`<p>Formula used: E = L * log<sub>2</sub>(R). A higher pool size and length increases entropy exponentially.</p>`);
        """
    },
    {
        "name": "Random Password Generator",
        "slug": "random-password-generator",
        "category": "Password Tools",
        "icon": "🎲",
        "desc": "Quickly generate random high-strength passwords with customizable rules.",
        "formula": "Password = CryptoRandom(Length)",
        "formula_desc": "Uses browser cryptographically secure pseudorandom number generators (CSPRNG) to build a string.",
        "inputs": [
            {"id": "length", "label": "Desired Length:", "type": "number", "default": "12", "min": "4", "max": "64"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Password", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const length = parseInt(document.getElementById('length').value) || 12;
            const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+";
            let result = "";
            const randomValues = new Uint32Array(length);
            window.crypto.getRandomValues(randomValues);
            for (let i = 0; i < length; i++) {
                result += chars[randomValues[i] % chars.length];
            }
            document.getElementById('text-output').value = result;
            updateBreakdown("<p>Generated password using standard cryptographically secure random values.</p>");
        """
    },
    {
        "name": "Secure Passphrase Generator",
        "slug": "secure-passphrase-generator",
        "category": "Password Tools",
        "icon": "💬",
        "desc": "Generate memorable yet highly secure passphrases using Diceware-style random wordlists.",
        "formula": "Passphrase = Join(RandomWords(List, Count), Dash)",
        "formula_desc": "Generates a passphrase by selecting random English words and joining them with separators.",
        "inputs": [
            {"id": "words-count", "label": "Number of Words:", "type": "number", "default": "4", "min": "3", "max": "10"},
            {"id": "separator", "label": "Word Separator:", "type": "select", "options": [("-", "Hyphen (-)"), (".", "Period (.)"), ("_", "Underscore (_)"), (" ", "Space ( )")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Passphrase", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('words-count').value) || 4;
            const sep = document.getElementById('separator').value;
            const wordList = [
                "apple", "banana", "cherry", "orange", "grape", "melon", "lemon", "lime", "berry", "peach",
                "river", "forest", "mountain", "valley", "ocean", "desert", "cloud", "storm", "winter", "summer",
                "shadow", "silver", "golden", "crystal", "diamond", "bronze", "copper", "iron", "stone", "brick",
                "rocket", "engine", "wheels", "gears", "matrix", "vector", "binary", "system", "kernel", "daemon",
                "falcon", "eagle", "tiger", "lion", "leopard", "panther", "wolf", "fox", "bear", "bison"
            ];

            let result = [];
            const randomValues = new Uint32Array(count);
            window.crypto.getRandomValues(randomValues);
            for (let i = 0; i < count; i++) {
                result.push(wordList[randomValues[i] % wordList.length]);
            }

            const passphrase = result.join(sep);
            document.getElementById('text-output').value = passphrase;
            updateBreakdown(`
                <p><strong>Words:</strong> ${count} selected from a 50-word base pool.</p>
                <p><strong>Entropy:</strong> ~${Math.round(count * Math.log2(50))} bits.</p>
            `);
        """
    },
    {
        "name": "Password Hash Generator",
        "slug": "password-hash-generator",
        "category": "Password Tools",
        "icon": "🔑",
        "desc": "Securely hash your passwords client-side using MD5, SHA-1, SHA-256, or SHA-512 algorithms.",
        "formula": "Hash = HashFunction(Password)",
        "formula_desc": "Applies a one-way hashing function to encrypt password text.",
        "inputs": [
            {"id": "password", "label": "Enter Password:", "type": "text", "default": ""},
            {"id": "hash-algo", "label": "Hash Algorithm:", "type": "select", "options": [("SHA256", "SHA-256"), ("SHA1", "SHA-1"), ("SHA512", "SHA-512"), ("MD5", "MD5")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Password Hash", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const pass = document.getElementById('password').value;
            const algo = document.getElementById('hash-algo').value;
            if (!pass) {
                showToast("Please enter a password to hash!", "error");
                return;
            }

            let hash = "";
            if (algo === "MD5") {
                hash = CryptoJS.MD5(pass).toString();
            } else if (algo === "SHA1") {
                hash = CryptoJS.SHA1(pass).toString();
            } else if (algo === "SHA256") {
                hash = CryptoJS.SHA256(pass).toString();
            } else if (algo === "SHA512") {
                hash = CryptoJS.SHA512(pass).toString();
            }

            document.getElementById('text-output').value = hash;
            updateBreakdown(`<p>Generated <strong>${algo}</strong> hash locally using CryptoJS.</p>`);
        """
    },
    {
        "name": "Password Leak Checker",
        "slug": "password-leak-checker",
        "category": "Password Tools",
        "icon": "⚠️",
        "desc": "Check if your password has been exposed in a data breach safely using HIBP k-Anonymity.",
        "formula": "HIBP Range API Query",
        "formula_desc": "Checks the first 5 characters of SHA-1 hash of password against 'Have I Been Pwned' database client-side.",
        "inputs": [
            {"id": "password", "label": "Enter Password to Check:", "type": "text", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Breach Verification Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const pass = document.getElementById('password').value;
            if (!pass) {
                showToast("Please enter a password!", "error");
                return;
            }

            document.getElementById('text-output').value = "Checking database, please wait...";

            const sha1 = CryptoJS.SHA1(pass).toString().toUpperCase();
            const prefix = sha1.substring(0, 5);
            const suffix = sha1.substring(5);

            fetch(`https://api.pwnedpasswords.com/range/${prefix}`)
                .then(res => {
                    if (!res.ok) throw new Error("Could not contact the leak checker database");
                    return res.text();
                })
                .then(text => {
                    const lines = text.split('\\n');
                    let match = null;
                    for (let line of lines) {
                        const [hashSuffix, count] = line.split(':');
                        if (hashSuffix.trim() === suffix) {
                            match = parseInt(count);
                            break;
                        }
                    }

                    if (match) {
                        document.getElementById('text-output').value = 
                            `⚠️ ALERT: Password Exposed!\\n\\n` +
                            `This password was found in database leaks ${match.toLocaleString()} times!\\n` +
                            `DO NOT USE this password. Change it immediately if active.`;
                    } else {
                        document.getElementById('text-output').value = 
                            `✅ Good news!\\n\\n` +
                            `This password was not found in any exposed database leaks indexed by HaveIBeenPwned.\\n` +
                            `Note: This does not guarantee strength, but means it is not in known public wordlists.`;
                    }
                    updateBreakdown(`<p>Queried HIBP API using safe SHA-1 prefix k-anonymity protocol.</p>`);
                })
                .catch(err => {
                    document.getElementById('text-output').value = `Error checking leaks: ${err.message}`;
                    showToast("Failed to fetch breach data.", "error");
                });
        """
    },
    {
        "name": "Password Complexity Checker",
        "slug": "password-complexity-checker",
        "category": "Password Tools",
        "icon": "🔒",
        "desc": "Check the complexity requirements of your password, evaluating character variety, length, and repeats.",
        "formula": "Complexity = EvaluationRules(Password)",
        "formula_desc": "Verifies complexity metrics including unique characters, length, and presence of multiple letter casing and digits.",
        "inputs": [
            {"id": "password", "label": "Enter Password:", "type": "text", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Complexity Breakdown Results", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const pass = document.getElementById('password').value;
            if (!pass) {
                showToast("Please enter a password!", "error");
                return;
            }

            const uniqueChars = new Set(pass).size;
            const length = pass.length;
            const hasUpper = /[A-Z]/.test(pass);
            const hasLower = /[a-z]/.test(pass);
            const hasNumber = /[0-9]/.test(pass);
            const hasSymbol = /[^a-zA-Z0-9]/.test(pass);

            let score = 0;
            if (length >= 8) score++;
            if (length >= 14) score++;
            if (hasUpper && hasLower) score++;
            if (hasNumber) score++;
            if (hasSymbol) score++;
            if (uniqueChars >= length / 2) score++;

            let label = "Low Complexity";
            if (score >= 5) label = "Excellent Complexity";
            else if (score >= 3) label = "Moderate Complexity";

            document.getElementById('text-output').value = 
                `Complexity Rating: ${label}\\n` +
                `Total Length: ${length}\\n` +
                `Unique Characters: ${uniqueChars}\\n` +
                `Casing Mix: ${hasUpper && hasLower ? 'Yes' : 'No'}\\n` +
                `Includes Numbers: ${hasNumber ? 'Yes' : 'No'}\\n` +
                `Includes Symbols: ${hasSymbol ? 'Yes' : 'No'}`;

            updateBreakdown("<p>Password complexity evaluated using standard entropy rules.</p>");
        """
    },
    {
        "name": "Password Policy Generator",
        "slug": "password-policy-generator",
        "category": "Password Tools",
        "icon": "📋",
        "desc": "Create robust corporate or application password policies to ensure your users choose strong keys.",
        "formula": "PolicyDescription = RuleEngine(Settings)",
        "formula_desc": "Builds standard text definitions for security policies based on user constraints.",
        "inputs": [
            {"id": "min-len", "label": "Minimum Password Length:", "type": "number", "default": "8", "min": "4", "max": "32"},
            {"id": "req-mix", "label": "Require Casing Mix (A-Z and a-z):", "type": "select", "options": [("yes", "Yes"), ("no", "No")]},
            {"id": "req-num", "label": "Require Numbers:", "type": "select", "options": [("yes", "Yes"), ("no", "No")]},
            {"id": "req-sym", "label": "Require Special Characters:", "type": "select", "options": [("yes", "Yes"), ("no", "No")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Password Policy Documentation", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const minLen = document.getElementById('min-len').value;
            const mix = document.getElementById('req-mix').value === 'yes';
            const num = document.getElementById('req-num').value === 'yes';
            const sym = document.getElementById('req-sym').value === 'yes';

            let policy = `PASSWORD SECURITY POLICY\\n========================\\n`;
            policy += `1. Passwords must be a minimum of ${minLen} characters in length.\\n`;
            if (mix) policy += `2. Passwords must contain a mix of both uppercase and lowercase alphabetic characters.\\n`;
            if (num) policy += `3. Passwords must contain at least one numeric digit (0-9).\\n`;
            if (sym) policy += `4. Passwords must contain at least one special symbol character (e.g. !, @, #, $, etc.).\\n`;
            policy += `5. Passwords should not be reused within 5 change cycles.\\n`;
            policy += `6. Passwords should expire and be renewed every 90 days.`;

            document.getElementById('text-output').value = policy;
            updateBreakdown("<p>Generated compliance-standard password policy text.</p>");
        """
    },
    {
        "name": "Bulk Password Generator",
        "slug": "bulk-password-generator",
        "category": "Password Tools",
        "icon": "📦",
        "desc": "Generate multiple secure passwords at once for servers, user migrations, or bulk creation.",
        "formula": "BulkPasswords = Repeat(PasswordGenerator, Count)",
        "formula_desc": "Generates multiple passwords using random selection algorithms, outputting a list.",
        "inputs": [
            {"id": "bulk-count", "label": "Number of Passwords to Generate:", "type": "number", "default": "10", "min": "2", "max": "100"},
            {"id": "bulk-len", "label": "Password Length:", "type": "number", "default": "12", "min": "6", "max": "64"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Passwords List", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('bulk-count').value) || 10;
            const length = parseInt(document.getElementById('bulk-len').value) || 12;
            const pool = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^*()_+";

            let result = [];
            for (let c = 0; c < count; c++) {
                let pass = "";
                const randomValues = new Uint32Array(length);
                window.crypto.getRandomValues(randomValues);
                for (let i = 0; i < length; i++) {
                    pass += pool[randomValues[i] % pool.length];
                }
                result.push(pass);
            }

            document.getElementById('text-output').value = result.join("\\n");
            updateBreakdown(`<p>Generated ${count} random passwords using CSRNG.</p>`);
        """
    }
]

HASH_GENERATOR_TOOLS = [
    {
        "name": "MD5 Hash Generator",
        "slug": "md5-hash-generator",
        "category": "Hash Generators",
        "icon": "🔒",
        "desc": "Generate a 128-bit MD5 checksum of any text input for data integrity checks.",
        "formula": "MD5 = CryptoJS.MD5(Text)",
        "formula_desc": "Computes the MD5 message digest of the input string.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Hash:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "MD5 Hash Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const hash = CryptoJS.MD5(text).toString();
            document.getElementById('text-output').value = hash;
            updateBreakdown("<p>Generated standard 32-character hexadecimal MD5 hash locally.</p>");
        """
    },
    {
        "name": "SHA1 Hash Generator",
        "slug": "sha1-hash-generator",
        "category": "Hash Generators",
        "icon": "🔒",
        "desc": "Generate a 160-bit SHA-1 cryptographic hash of your text in your browser.",
        "formula": "SHA1 = CryptoJS.SHA1(Text)",
        "formula_desc": "Calculates the SHA-1 digest hash of input string.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Hash:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "SHA1 Hash Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const hash = CryptoJS.SHA1(text).toString();
            document.getElementById('text-output').value = hash;
            updateBreakdown("<p>Generated standard 40-character hexadecimal SHA-1 hash locally.</p>");
        """
    },
    {
        "name": "SHA224 Hash Generator",
        "slug": "sha224-hash-generator",
        "category": "Hash Generators",
        "icon": "🔒",
        "desc": "Generate a SHA-224 hash value of your text instantly.",
        "formula": "SHA224 = CryptoJS.SHA224(Text)",
        "formula_desc": "Calculates the 224-bit hash code belonging to the SHA-2 family.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "SHA224 Hash Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const hash = CryptoJS.SHA224(text).toString();
            document.getElementById('text-output').value = hash;
            updateBreakdown("<p>Generated standard 56-character hexadecimal SHA-224 hash locally.</p>");
        """
    },
    {
        "name": "SHA256 Hash Generator",
        "slug": "sha256-hash-generator",
        "category": "Hash Generators",
        "icon": "🔒",
        "desc": "Generate secure 256-bit SHA-256 hashes of your text strings client-side.",
        "formula": "SHA256 = CryptoJS.SHA256(Text)",
        "formula_desc": "Computes the cryptographic SHA-256 digest hash.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "SHA256 Hash Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const hash = CryptoJS.SHA256(text).toString();
            document.getElementById('text-output').value = hash;
            updateBreakdown("<p>Generated standard 64-character hexadecimal SHA-256 hash locally.</p>");
        """
    },
    {
        "name": "SHA384 Hash Generator",
        "slug": "sha384-hash-generator",
        "category": "Hash Generators",
        "icon": "🔒",
        "desc": "Generate secure 384-bit SHA-384 hashes of your text strings client-side.",
        "formula": "SHA384 = CryptoJS.SHA384(Text)",
        "formula_desc": "Computes the cryptographic SHA-384 digest hash.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "SHA384 Hash Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const hash = CryptoJS.SHA384(text).toString();
            document.getElementById('text-output').value = hash;
            updateBreakdown("<p>Generated standard 96-character hexadecimal SHA-384 hash locally.</p>");
        """
    },
    {
        "name": "SHA512 Hash Generator",
        "slug": "sha512-hash-generator",
        "category": "Hash Generators",
        "icon": "🔒",
        "desc": "Generate secure 512-bit SHA-512 hashes of your text strings client-side.",
        "formula": "SHA512 = CryptoJS.SHA512(Text)",
        "formula_desc": "Computes the cryptographic SHA-512 digest hash.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "SHA512 Hash Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const hash = CryptoJS.SHA512(text).toString();
            document.getElementById('text-output').value = hash;
            updateBreakdown("<p>Generated standard 128-character hexadecimal SHA-512 hash locally.</p>");
        """
    },
    {
        "name": "HMAC Generator",
        "slug": "hmac-generator",
        "category": "Hash Generators",
        "icon": "🔑",
        "desc": "Calculate Hash-based Message Authentication Codes (HMAC) using standard hash ciphers.",
        "formula": "HMAC = H(Key XOR opad, H(Key XOR ipad, Text))",
        "formula_desc": "Combines a secret key with a cryptographic hash function to verify data integrity.",
        "inputs": [
            {"id": "text-input", "label": "Enter Data String:", "type": "textarea", "default": ""},
            {"id": "hmac-key", "label": "Secret Key:", "type": "text", "default": ""},
            {"id": "hmac-algo", "label": "HMAC Algorithm:", "type": "select", "options": [("SHA256", "SHA-256"), ("SHA1", "SHA-1"), ("MD5", "MD5"), ("SHA512", "SHA-512")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "HMAC Output (HEX)", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const key = document.getElementById('hmac-key').value;
            const algo = document.getElementById('hmac-algo').value;

            if (!key) {
                showToast("Secret key is required for HMAC!", "error");
                return;
            }

            let hmac = "";
            if (algo === "MD5") {
                hmac = CryptoJS.HmacMD5(text, key).toString();
            } else if (algo === "SHA1") {
                hmac = CryptoJS.HmacSHA1(text, key).toString();
            } else if (algo === "SHA256") {
                hmac = CryptoJS.HmacSHA256(text, key).toString();
            } else if (algo === "SHA512") {
                hmac = CryptoJS.HmacSHA512(text, key).toString();
            }

            document.getElementById('text-output').value = hmac;
            updateBreakdown(`<p>Generated <strong>${algo}</strong> HMAC successfully.</p>`);
        """
    },
    {
        "name": "File Hash Generator",
        "slug": "file-hash-generator",
        "category": "Hash Generators",
        "icon": "📁",
        "desc": "Generate hashes and checksums of local files safely without uploading them to any servers.",
        "formula": "FileHash = Hash(FileArrayBuffer)",
        "formula_desc": "Reads file chunks locally and streams them into a cryptographic hash accumulator.",
        "inputs": [
            {"id": "file-input", "label": "Choose Local File to Hash:", "type": "file"},
            {"id": "hash-algo", "label": "Choose Hash Algorithm:", "type": "select", "options": [("SHA256", "SHA-256"), ("SHA1", "SHA-1"), ("MD5", "MD5"), ("SHA512", "SHA-512")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Checksum", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileElement = document.getElementById('file-input');
            const algo = document.getElementById('hash-algo').value;

            if (!fileElement || !fileElement.files || fileElement.files.length === 0) {
                showToast("Please select a file first!", "error");
                return;
            }

            const file = fileElement.files[0];
            const reader = new FileReader();

            document.getElementById('text-output').value = "Calculating hash, please wait...";

            reader.onload = function(e) {
                const arrayBuffer = e.target.result;
                const wordArray = CryptoJS.lib.WordArray.create(arrayBuffer);
                let hash = "";
                
                if (algo === "MD5") {
                    hash = CryptoJS.MD5(wordArray).toString();
                } else if (algo === "SHA1") {
                    hash = CryptoJS.SHA1(wordArray).toString();
                } else if (algo === "SHA256") {
                    hash = CryptoJS.SHA256(wordArray).toString();
                } else if (algo === "SHA512") {
                    hash = CryptoJS.SHA512(wordArray).toString();
                }
                
                document.getElementById('text-output').value = hash;
                updateBreakdown(`<p>File: <strong>${file.name}</strong> (${file.size} bytes)<br>Algorithm: <strong>${algo}</strong></p>`);
            };

            reader.onerror = function() {
                showToast("Error reading file", "error");
                document.getElementById('text-output').value = "Error reading file";
            };

            reader.readAsArrayBuffer(file);
        """
    },
    {
        "name": "Checksum Calculator",
        "slug": "checksum-calculator",
        "category": "Hash Generators",
        "icon": "🧮",
        "desc": "Calculate standard CRC-32 and Adler-32 checksums of any input text block.",
        "formula": "CRC32 = PolynomialDivision(Data)",
        "formula_desc": "Generates CRC-32 cyclic redundancy check values to identify stream alterations.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text for Checksum:", "type": "textarea", "default": ""},
            {"id": "checksum-type", "label": "Checksum Type:", "type": "select", "options": [("CRC32", "CRC-32"), ("ADLER32", "Adler-32")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Checksum Code", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const type = document.getElementById('checksum-type').value;

            // Simple CRC32 implementation
            function makeCRCTable() {
                let c;
                let crcTable = [];
                for(let n =0; n < 256; n++){
                    c = n;
                    for(let k =0; k < 8; k++){
                        c = ((c&1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1));
                    }
                    crcTable[n] = c;
                }
                return crcTable;
            }
            const crcTable = window.crcTable || makeCRCTable();
            window.crcTable = crcTable;

            function crc32(str) {
                let crc = 0 ^ (-1);
                for (let i = 0; i < str.length; i++ ) {
                    crc = (crc >>> 8) ^ crcTable[(crc ^ str.charCodeAt(i)) & 0xFF];
                }
                return (crc ^ (-1)) >>> 0;
            }

            function adler32(str) {
                let a = 1, b = 0;
                for (let i = 0; i < str.length; i++) {
                    a = (a + str.charCodeAt(i)) % 65521;
                    b = (b + a) % 65521;
                }
                return ((b << 16) | a) >>> 0;
            }

            let result = 0;
            if (type === "CRC32") {
                result = crc32(text);
            } else {
                result = adler32(text);
            }

            const hex = result.toString(16).toUpperCase().padStart(8, '0');
            document.getElementById('text-output').value = `HEX: ${hex}\\nDEC: ${result}`;
            updateBreakdown(`<p>Calculated <strong>${type}</strong> checksum value.</p>`);
        """
    },
    {
        "name": "Hash Comparison Tool",
        "slug": "hash-comparison-tool",
        "category": "Hash Generators",
        "icon": "⚖️",
        "desc": "Compare two cryptographic hashes to check if they match (integrity verification).",
        "formula": "Match = (HashA.trim().lower() === HashB.trim().lower())",
        "formula_desc": "Compares strings side-by-side, ignoring case and surrounding white spaces.",
        "inputs": [
            {"id": "hash-a", "label": "Hash Value A:", "type": "text", "default": ""},
            {"id": "hash-b", "label": "Hash Value B:", "type": "text", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Comparison Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const ha = document.getElementById('hash-a').value.trim().toLowerCase();
            const hb = document.getElementById('hash-b').value.trim().toLowerCase();

            if (!ha || !hb) {
                showToast("Please enter both hash values to compare!", "error");
                return;
            }

            const match = (ha === hb);
            document.getElementById('text-output').value = 
                `Result: ${match ? "✅ MATCH" : "❌ MISMATCH"}\\n\\n` +
                `Length A: ${ha.length} characters\\n` +
                `Length B: ${hb.length} characters`;

            updateBreakdown(`<p>Comparison completed. Case differences and padding spaces were ignored.</p>`);
        """
    }
]

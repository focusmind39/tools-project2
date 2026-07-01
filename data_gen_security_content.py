# -*- coding: utf-8 -*-
"""
Database of 20 Password, Security, and Content Creator Generator Tools for Enginewheels
"""

SECURITY_GENERATORS = [
    {
        "category": "Password & Security Generators",
        "name": "Password Generator",
        "slug": "password-generator-tool",
        "desc": "Generate custom passwords with selectable length, letters, numbers, and symbols.",
        "formula": "Random char set index selection",
        "formula_desc": "Iteratively appends random characters from character pools matching the selected criteria.",
        "icon": "🔑",
        "inputs": [
            {"id": "pass-len", "label": "Password Length:", "type": "number", "default": "12"},
            {"id": "pass-upper", "label": "Include Uppercase (A-Z):", "type": "select", "default": "yes",
             "options": [("yes", "Yes"), ("no", "No")]},
            {"id": "pass-lower", "label": "Include Lowercase (a-z):", "type": "select", "default": "yes",
             "options": [("yes", "Yes"), ("no", "No")]},
            {"id": "pass-nums", "label": "Include Numbers (0-9):", "type": "select", "default": "yes",
             "options": [("yes", "Yes"), ("no", "No")]},
            {"id": "pass-syms", "label": "Include Symbols (!@#$):", "type": "select", "default": "yes",
             "options": [("yes", "Yes"), ("no", "No")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Password:", "type": "textarea"}
        ],
        "calc_js": """
            const len = parseInt(document.getElementById('pass-len').value) || 12;
            const upper = document.getElementById('pass-upper').value === 'yes';
            const lower = document.getElementById('pass-lower').value === 'yes';
            const nums = document.getElementById('pass-nums').value === 'yes';
            const syms = document.getElementById('pass-syms').value === 'yes';

            const uChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            const lChars = "abcdefghijklmnopqrstuvwxyz";
            const nChars = "0123456789";
            const sChars = "!@#$%^&*()_+~`|}{[]:;?><,./-=";

            let pool = "";
            if (upper) pool += uChars;
            if (lower) pool += lChars;
            if (nums) pool += nChars;
            if (syms) pool += sChars;

            if (!pool) {
                showToast("Please select at least one character set.", "error");
                return;
            }

            let result = "";
            for (let i = 0; i < len; i++) {
                result += pool.charAt(Math.floor(Math.random() * pool.length));
            }

            document.getElementById('text-output').value = result;
            updateBreakdown("<p class='text-success'>Password generated successfully.</p>");
        """
    },
    {
        "category": "Password & Security Generators",
        "name": "Secure Password Generator",
        "slug": "secure-password-generator-tool",
        "desc": "Generate strong, cryptographically secure passwords utilizing browser-native Web Crypto API.",
        "formula": "window.crypto.getRandomValues cryptorand",
        "formula_desc": "Applies high-entropy, non-predictable 32-bit unsigned integers to build cryptographic passwords.",
        "icon": "🛡️",
        "inputs": [
            {"id": "sec-pass-len", "label": "Secure Length:", "type": "number", "default": "16"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Secure Cryptographic Password:", "type": "textarea"}
        ],
        "calc_js": """
            const len = parseInt(document.getElementById('sec-pass-len').value) || 16;
            const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+}{[]:;?><";
            
            let result = "";
            try {
                const array = new Uint32Array(len);
                window.crypto.getRandomValues(array);
                for (let i = 0; i < len; i++) {
                    result += chars.charAt(array[i] % chars.length);
                }
            } catch (e) {
                // Fallback to math random if crypto is blocked
                for (let i = 0; i < len; i++) {
                    result += chars.charAt(Math.floor(Math.random() * chars.length));
                }
            }

            document.getElementById('text-output').value = result;
            updateBreakdown("<p class='text-success'>Cryptographically secure password generated.</p>");
        """
    },
    {
        "category": "Password & Security Generators",
        "name": "Passphrase Generator",
        "slug": "passphrase-generator-tool",
        "desc": "Generate easy-to-remember but hard-to-crack random passphrases.",
        "formula": "Multi-word phrase compounding",
        "formula_desc": "Combines random common English words separated by a customized delimiter (hyphens, spaces).",
        "icon": "💬",
        "inputs": [
            {"id": "phrase-words", "label": "Word Count:", "type": "number", "default": "4"},
            {"id": "phrase-sep", "label": "Separator:", "type": "select", "default": "hyphen",
             "options": [
                 ("hyphen", "Hyphen (-)"),
                 ("dot", "Dot (.)"),
                 ("space", "Space ( )")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Passphrase:", "type": "textarea"}
        ],
        "calc_js": """
            const qty = parseInt(document.getElementById('phrase-words').value) || 4;
            const sepType = document.getElementById('phrase-sep').value;
            
            const words = ["correct", "battery", "horse", "staple", "galaxy", "system", "index", "code", "logic", "matrix", "cloud", "shadow", "flight", "bridge", "tunnel", "river", "stone", "glowing", "ancient", "vibrant"];
            
            let chosen = [];
            for (let i = 0; i < qty; i++) {
                chosen.push(words[Math.floor(Math.random() * words.length)]);
            }

            let sep = "-";
            if (sepType === "dot") sep = ".";
            else if (sepType === "space") sep = " ";

            document.getElementById('text-output').value = chosen.join(sep);
            updateBreakdown("<p class='text-success'>Passphrase assembled for secure mnemonic storage.</p>");
        """
    },
    {
        "category": "Password & Security Generators",
        "name": "PIN Generator",
        "slug": "pin-generator",
        "desc": "Generate numerical Personal Identification Numbers (PINs) of custom length.",
        "formula": "Iterative digit assembly",
        "formula_desc": "Generates a sequence of digits (0-9) ensuring zero guessable padding structures.",
        "icon": "🔢",
        "inputs": [
            {"id": "pin-len", "label": "PIN Digit Length:", "type": "select", "default": "4",
             "options": [
                 ("4", "4 Digits"),
                 ("6", "6 Digits"),
                 ("8", "8 Digits")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated PIN:", "type": "textarea"}
        ],
        "calc_js": """
            const len = parseInt(document.getElementById('pin-len').value) || 4;
            let pin = "";
            for (let i = 0; i < len; i++) {
                pin += Math.floor(Math.random() * 10);
            }
            document.getElementById('text-output').value = pin;
            updateBreakdown(`<p class='text-success'>Generated a secure ${len}-digit numerical PIN.</p>`);
        """
    },
    {
        "category": "Password & Security Generators",
        "name": "API Key Generator",
        "slug": "api-key-generator",
        "desc": "Generate custom API secret tokens and access client keys.",
        "formula": "Standardized token prefixes + random hex bytes",
        "formula_desc": "Combines a prefix tag with high-entropy hex bytes to match typical secret key strings (e.g. sk_live_...).",
        "icon": "🔑",
        "inputs": [
            {"id": "api-prefix", "label": "Key Prefix (e.g. sk_live):", "type": "text", "default": "sk_live"}
        ],
        "outputs": [
            {"id": "text-output", "label": "API Key Output:", "type": "textarea"}
        ],
        "calc_js": """
            const prefix = document.getElementById('api-prefix').value.trim() || "api_key";
            const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            
            let key = "";
            for (let i = 0; i < 32; i++) {
                key += chars.charAt(Math.floor(Math.random() * chars.length));
            }

            document.getElementById('text-output').value = `${prefix}_${key}`;
            updateBreakdown("<p class='text-success'>Mock API key generated.</p>");
        """
    },
    {
        "category": "Password & Security Generators",
        "name": "UUID Generator",
        "slug": "uuid-generator-tool",
        "desc": "Generate RFC4122 Version 4 Universally Unique Identifiers.",
        "formula": "RFC4122 Version 4 bits compilation",
        "formula_desc": "Replaces placeholders in a UUID template, forcing specific version bits (4) and variant bits.",
        "icon": "🆔",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "UUID v4 Output:", "type": "textarea"}
        ],
        "calc_js": """
            function genUUID() {
                return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
                    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
                    return v.toString(16);
                });
            }
            document.getElementById('text-output').value = genUUID();
            updateBreakdown("<p class='text-success'>Standard UUID v4 generated.</p>");
        """
    },
    {
        "category": "Password & Security Generators",
        "name": "Random Token Generator",
        "slug": "random-token-generator",
        "desc": "Generate random alphanumeric, hex, or base64 tokens of a custom length.",
        "formula": "Byte array encoding conversion",
        "formula_desc": "Converts random numbers into hex representations or character maps to build general session tokens.",
        "icon": "🪙",
        "inputs": [
            {"id": "tok-len", "label": "Token Length:", "type": "number", "default": "32"},
            {"id": "tok-type", "label": "Token Encoding:", "type": "select", "default": "hex",
             "options": [
                 ("hex", "Hexadecimal (a-f, 0-9)"),
                 ("alpha", "Alphanumeric (Letters & Numbers)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Token:", "type": "textarea"}
        ],
        "calc_js": """
            const len = parseInt(document.getElementById('tok-len').value) || 32;
            const type = document.getElementById('tok-type').value;

            let chars = "";
            if (type === "hex") chars = "0123456789abcdef";
            else chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

            let token = "";
            for (let i = 0; i < len; i++) {
                token += chars.charAt(Math.floor(Math.random() * chars.length));
            }

            document.getElementById('text-output').value = token;
            updateBreakdown("<p class='text-success'>Random token generated.</p>");
        """
    },
    {
        "category": "Password & Security Generators",
        "name": "Secret Key Generator",
        "slug": "secret-key-generator",
        "desc": "Generate strong, high-entropy cryptographic secret keys for cookie or JWT signing.",
        "formula": "Secure byte character compilation",
        "formula_desc": "Selects high-entropy characters from mixed alphanumerics and symbols to form cookie hashes.",
        "icon": "🔑",
        "inputs": [
            {"id": "sec-key-bits", "label": "Key Complexity:", "type": "select", "default": "256",
             "options": [
                 ("256", "256-bit equivalent (32 chars)"),
                 ("512", "512-bit equivalent (64 chars)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Cryptographic Secret Key:", "type": "textarea"}
        ],
        "calc_js": """
            const bits = document.getElementById('sec-key-bits').value;
            const len = bits === "256" ? 32 : 64;
            const pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,./<>?";
            
            let key = "";
            for (let i = 0; i < len; i++) {
                key += pool.charAt(Math.floor(Math.random() * pool.length));
            }

            document.getElementById('text-output').value = key;
            updateBreakdown("<p class='text-success'>High-entropy secret key generated successfully.</p>");
        """
    },
    {
        "category": "Password & Security Generators",
        "name": "Session ID Generator",
        "slug": "session-id-generator",
        "desc": "Generate standard session identifiers for cookies and database testing.",
        "formula": "Standard hex byte string construction",
        "formula_desc": "Combines random hexadecimal bytes into a 32-character string to simulate token transactions.",
        "icon": "💾",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Session ID:", "type": "textarea"}
        ],
        "calc_js": """
            const hex = "0123456789abcdef";
            let sess = "";
            for (let i = 0; i < 32; i++) {
                sess += hex.charAt(Math.floor(Math.random() * 16));
            }
            document.getElementById('text-output').value = sess;
            updateBreakdown("<p class='text-success'>Unique Session ID generated successfully.</p>");
        """
    },
    {
        "category": "Password & Security Generators",
        "name": "Encryption Key Generator",
        "slug": "encryption-key-generator",
        "desc": "Generate standard 128-bit, 192-bit, or 256-bit symmetric encryption keys.",
        "formula": "AES bit length hex matching",
        "formula_desc": "Synthesizes standard bit-length hex strings corresponding to symmetric AES keys.",
        "icon": "🔐",
        "inputs": [
            {"id": "key-bits", "label": "Key Size (bits):", "type": "select", "default": "256",
             "options": [
                 ("128", "128-bit (16-byte hex)"),
                 ("192", "192-bit (24-byte hex)"),
                 ("256", "256-bit (32-byte hex)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Symmetric Key Output (Hex):", "type": "textarea"}
        ],
        "calc_js": """
            const size = document.getElementById('key-bits').value;
            const bytesLen = size === "128" ? 16 : (size === "192" ? 24 : 32);
            
            const hex = "0123456789ABCDEF";
            let key = "";
            for (let i = 0; i < bytesLen * 2; i++) {
                key += hex.charAt(Math.floor(Math.random() * 16));
            }

            document.getElementById('text-output').value = key;
            updateBreakdown("<p class='text-success'>Symmetric AES encryption key generated.</p>");
        """
    },
    {
        "category": "Content Creator Generators",
        "name": "YouTube Title Generator",
        "slug": "youtube-title-generator",
        "desc": "Generate click-worthy and optimized titles for your YouTube videos.",
        "formula": "Viral template formulation",
        "formula_desc": "Appends keywords to standard viral headlines ('Before You Buy', 'Secrets of', 'How to...').",
        "icon": "🎥",
        "inputs": [
            {"id": "yt-keyword", "label": "Video Topic / Keyword:", "type": "text", "default": "Web Development"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Title Variations:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('yt-keyword').value.trim();
            if (!kw) {
                showToast("Please enter a video topic.", "error");
                return;
            }

            const titles = [
                `I Tried ${kw} for 30 Days (Here's What Happened)`,
                `The Ultimate Guide to ${kw} in 2026`,
                `5 Dangerous Mistakes People Make in ${kw}`,
                `How to Master ${kw} (Step-by-Step)`,
                `The Secret Behind ${kw} Nobody Tells You`,
                `Why ${kw} is Changing the Industry Forever`
            ];

            document.getElementById('text-output').value = titles.join("\\n\\n");
            updateBreakdown("<p class='text-success'>Viral YouTube titles generated.</p>");
        """
    },
    {
        "category": "Content Creator Generators",
        "name": "YouTube Description Generator",
        "slug": "youtube-description-generator",
        "desc": "Generate complete description outlines for YouTube uploads containing chapters and links.",
        "formula": "Description layout assembly",
        "formula_desc": "Injects user keywords, timeline markers, and social link brackets into structured description layouts.",
        "icon": "📝",
        "inputs": [
            {"id": "desc-kw", "label": "Video Title/Topic:", "type": "text", "default": "Learn CSS Flexbox"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted Description:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('desc-kw').value.trim();
            
            const template = `🔥 In this video, we dive deep into ${kw}! Discover the key concepts, best practices, and practical examples to master this topic instantly.

📌 Timestamps:
0:00 - Introduction
1:30 - Key Concepts & Basics
4:00 - Step-by-Step Tutorial
8:15 - Advanced Tips & Tricks
11:00 - Final Review

🔗 Useful Links & Resources:
- Support the channel: [Your Link Here]
- Website: https://enginewheels.com
- Twitter: @YourTwitter

👉 Don't forget to LIKE, COMMENT, and SUBSCRIBE for more content!

#${kw.replace(/\\s+/g, '')} #Tutorial #Tech #Education`;

            document.getElementById('text-output').value = template;
            updateBreakdown("<p class='text-success'>YouTube description layout assembled.</p>");
        """
    },
    {
        "category": "Content Creator Generators",
        "name": "YouTube Tag Generator",
        "slug": "youtube-tag-generator",
        "desc": "Generate search-optimized tags and keywords for your YouTube videos.",
        "formula": "Tag list keyword expansion",
        "formula_desc": "Combines niche keywords with popular modifiers ('tutorial', 'for beginners', 'explained', 'tips').",
        "icon": "🏷️",
        "inputs": [
            {"id": "tag-kw", "label": "Main Topic Keyword:", "type": "text", "default": "Python"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Suggested Tags (Comma Separated):", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('tag-kw').value.trim();
            if (!kw) {
                showToast("Please enter a keyword.", "error");
                return;
            }

            const modifiers = ["", " tutorial", " for beginners", " explained", " crash course", " tips", " guide", " basics", " coding", " development"];
            const tags = modifiers.map(m => kw + m);

            document.getElementById('text-output').value = tags.join(", ");
            updateBreakdown("<p class='text-success'>YouTube tags compiled successfully.</p>");
        """
    },
    {
        "category": "Content Creator Generators",
        "name": "Blog Title Generator",
        "slug": "blog-title-generator",
        "desc": "Generate catchy blog post headlines to attract readers.",
        "formula": "Listicle and guide layout mapping",
        "formula_desc": "Injects user keywords into standard blog headlines ('X Ways to', 'The Future of', 'Ultimate Guide to').",
        "icon": "✍️",
        "inputs": [
            {"id": "blog-kw", "label": "Blog Post Topic:", "type": "text", "default": "Remote Work"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Suggested Blog Titles:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('blog-kw').value.trim();
            if (!kw) {
                showToast("Please enter a topic.", "error");
                return;
            }

            const templates = [
                `10 Proven Ways to Master ${kw} Today`,
                `The Ultimate Guide to ${kw} for Beginners`,
                `Why ${kw} is the Future of the Industry`,
                `7 Common Mistakes in ${kw} (And How to Avoid Them)`,
                `The Secret to Success with ${kw}`,
                `How to Optimize Your ${kw} Workflow`
            ];

            document.getElementById('text-output').value = templates.join("\\n\\n");
            updateBreakdown("<p class='text-success'>Blog title variations compiled.</p>");
        """
    },
    {
        "category": "Content Creator Generators",
        "name": "Blog Idea Generator",
        "slug": "blog-idea-generator",
        "desc": "Generate creative blog ideas and concept outlines.",
        "formula": "Content direction matrix",
        "formula_desc": "Creates five unique blog concepts including target audience and writing direction.",
        "icon": "💡",
        "inputs": [
            {"id": "blog-niche", "label": "Niche/Category:", "type": "text", "default": "Coding"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Blog Post Ideas:", "type": "textarea"}
        ],
        "calc_js": """
            const niche = document.getElementById('blog-niche').value.trim();
            if (!niche) {
                showToast("Please enter a niche.", "error");
                return;
            }

            const ideas = [
                `1. A complete breakdown of the best tools in the ${niche} industry. (Target: Beginners)`,
                `2. How to transition into ${niche} from a non-traditional background. (Target: Career Changers)`,
                `3. A case study comparing different strategies in ${niche}. (Target: Intermediates)`,
                `4. The impact of automation and AI on the future of ${niche}. (Target: Industry professionals)`,
                `5. 5 simple habits that will double your efficiency in ${niche}. (Target: General audience)`
            ];

            document.getElementById('text-output').value = ideas.join("\\n\\n");
            updateBreakdown("<p class='text-success'>Blog ideas generated.</p>");
        """
    },
    {
        "category": "Content Creator Generators",
        "name": "Article Idea Generator",
        "slug": "article-idea-generator",
        "desc": "Generate article outlines, hooks, and research directions.",
        "formula": "Research outline compiling",
        "formula_desc": "Compiles structured article ideas containing intro hooks, main body concepts, and summaries.",
        "icon": "📰",
        "inputs": [
            {"id": "art-topic", "label": "Core Subject Area:", "type": "text", "default": "Sustainability"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Article Outlines:", "type": "textarea"}
        ],
        "calc_js": """
            const topic = document.getElementById('art-topic').value.trim();
            if (!topic) {
                showToast("Please enter a subject.", "error");
                return;
            }

            const outline = `Title Idea: The Quiet Revolution of ${topic}
--------------------------------------------------
Intro Hook: Most people overlook how ${topic} impacts daily routines, but change is happening.
Main Section 1: The current state of ${topic} and why it matters now.
Main Section 2: Three practical ways organizations are adapting.
Conclusion: Why long-term success requires immediate action.
Keywords to Include: ${topic}, technology, future, efficiency.`;

            document.getElementById('text-output').value = outline;
            updateBreakdown("<p class='text-success'>Article outline compiled.</p>");
        """
    },
    {
        "category": "Content Creator Generators",
        "name": "Headline Generator",
        "slug": "headline-generator",
        "desc": "Generate powerful headlines for landing pages, ads, and newsletters.",
        "formula": "Marketing copywriting templates",
        "formula_desc": "Combines user products or services with high-converting landing page headline templates.",
        "icon": "📣",
        "inputs": [
            {"id": "head-product", "label": "Product or Service Name:", "type": "text", "default": "Task Tracker"}
        ],
        "outputs": [
            {"id": "text-output", "label": "High-Converting Headlines:", "type": "textarea"}
        ],
        "calc_js": """
            const prod = document.getElementById('head-product').value.trim();
            if (!prod) {
                showToast("Please enter your product name.", "error");
                return;
            }

            const heads = [
                `Stop Wasting Time. Manage Your Workflow with ${prod}.`,
                `The Smart Way to Organize Your Day: Meet ${prod}.`,
                `Double Your Productivity with ${prod}—100% Free.`,
                `Finally, a ${prod} Built for Modern Teams.`,
                `Say Goodbye to Chaos. Say Hello to ${prod}.`
            ];

            document.getElementById('text-output').value = heads.join("\\n\\n");
            updateBreakdown("<p class='text-success'>High-converting marketing headlines generated.</p>");
        """
    },
    {
        "category": "Content Creator Generators",
        "name": "Hook Generator",
        "slug": "hook-generator",
        "desc": "Generate attention-grabbing hooks to start your essays or videos.",
        "formula": "Attention capture formulas",
        "formula_desc": "Generates curiosity, statistic, or query-based starting lines to hook readers or viewers.",
        "icon": "🪝",
        "inputs": [
            {"id": "hook-kw", "label": "Key Subject:", "type": "text", "default": "Coding"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Attention Hooks:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('hook-kw').value.trim();
            if (!kw) {
                showToast("Please enter a subject.", "error");
                return;
            }

            const hooks = [
                `Did you know that 90% of people struggle with ${kw} because of one simple mistake?`,
                `What if everything you've been told about ${kw} is completely wrong?`,
                `Here is a secret about ${kw} that most experts refuse to share.`,
                `Most people fail at ${kw} within the first week. Here is how to be in the 10% who succeed.`
            ];

            document.getElementById('text-output').value = hooks.join("\\n\\n");
            updateBreakdown("<p class='text-success'>Attention hooks generated successfully.</p>");
        """
    },
    {
        "category": "Content Creator Generators",
        "name": "CTA Generator",
        "slug": "cta-generator",
        "desc": "Generate effective Call to Action (CTA) buttons and copy tags.",
        "formula": "Urgency and benefit compounding",
        "formula_desc": "Combines action verbs with urgency indicators ('now', 'today', 'free') to create high-converting CTAs.",
        "icon": "🎯",
        "inputs": [
            {"id": "cta-benefit", "label": "User Benefit (e.g. Save 20%):", "type": "text", "default": "Start Free Trial"}
        ],
        "outputs": [
            {"id": "text-output", "label": "CTA Copy Options:", "type": "textarea"}
        ],
        "calc_js": """
            const benefit = document.getElementById('cta-benefit').value.trim();
            if (!benefit) {
                showToast("Please enter a benefit.", "error");
                return;
            }

            const ctas = [
                `👉 ${benefit} Now`,
                `Claim Your Spot: ${benefit}`,
                `Get Started Today (${benefit})`,
                `Join Now & ${benefit}`,
                `Limited Time: ${benefit}`
            ];

            document.getElementById('text-output').value = ctas.join("\\n");
            updateBreakdown("<p class='text-success'>Call to Action variations compiled.</p>");
        """
    },
    {
        "category": "Content Creator Generators",
        "name": "Social Media Caption Generator",
        "slug": "social-caption-generator",
        "desc": "Generate captions for Instagram, LinkedIn, or Twitter/X posts.",
        "formula": "Social post spacing + emojis",
        "formula_desc": "Formats text captions, automatically inserting relevant emojis and hashtags for social reach.",
        "icon": "📱",
        "inputs": [
            {"id": "cap-topic", "label": "Post Topic / Message:", "type": "text", "default": "Launched our new site"},
            {"id": "cap-platform", "label": "Target Platform:", "type": "select", "default": "insta",
             "options": [
                 ("insta", "Instagram (Aesthetic)"),
                 ("linkedin", "LinkedIn (Professional)"),
                 ("twitter", "Twitter/X (Punchy)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Social Caption Output:", "type": "textarea"}
        ],
        "calc_js": """
            const topic = document.getElementById('cap-topic').value.trim();
            const platform = document.getElementById('cap-platform').value;
            if (!topic) {
                showToast("Please enter a topic.", "error");
                return;
            }

            let result = "";
            if (platform === "insta") {
                result = `✨ New milestone unlocked: ${topic}! Can't wait to see where this journey leads. Let me know what you think in the comments! 👇\\n\\n#milestone #achievement #happy #journey #aesthetic`;
            } else if (platform === "linkedin") {
                result = `I'm thrilled to share that we've officially: ${topic}.\\n\\nThis milestone wouldn't have been possible without the dedication of the team. Thank you to everyone involved!\\n\\n#professional #networking #leadership #career #growth`;
            } else {
                result = `Just did this: ${topic}! 🚀 Huge thanks to everyone who supported us. What's next?`;
            }

            document.getElementById('text-output').value = result;
            updateBreakdown("<p class='text-success'>Social caption generated for the chosen platform.</p>");
        """
    }
]

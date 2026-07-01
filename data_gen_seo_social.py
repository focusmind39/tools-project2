# -*- coding: utf-8 -*-
"""
Database of 20 SEO and Social Media Generator Tools for Enginewheels
"""

SEO_GENERATORS = [
    {
        "category": "SEO Generators",
        "name": "Meta Title Generator",
        "slug": "meta-title-generator-tool",
        "desc": "Generate search-optimized page meta titles matching Google's character limit.",
        "formula": "Title = Keyword + Separator + Brand",
        "formula_desc": "Combines target keyword, page category modifiers, and brand names, restricting length to 60 characters.",
        "icon": "🏷️",
        "inputs": [
            {"id": "title-kw", "label": "Target Keyword:", "type": "text", "default": "Free PDF Tools"},
            {"id": "title-brand", "label": "Brand Name (Optional):", "type": "text", "default": "Enginewheels"},
            {"id": "title-sep", "label": "Separator:", "type": "select", "default": "pipe",
             "options": [
                 ("pipe", "Pipe (|)"),
                 ("dash", "Dash (-)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Optimized Title (Google Preview):", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('title-kw').value.trim();
            const brand = document.getElementById('title-brand').value.trim();
            const sepType = document.getElementById('title-sep').value;

            if (!kw) {
                showToast("Please enter a target keyword.", "error");
                return;
            }

            const sep = sepType === "pipe" ? "|" : "-";
            let title = kw;
            if (brand) {
                title = `${kw} ${sep} ${brand}`;
            }

            const len = title.length;
            let feedback = `<span class='text-success'>Good length: ${len} chars (Google limit is ~60).</span>`;
            if (len > 60) {
                feedback = `<span class='text-danger'>Too long: ${len} chars (Recommended <= 60). Title may be truncated in search results.</span>`;
            }

            document.getElementById('text-output').value = title;
            updateBreakdown(`<p>${feedback}</p>`);
        """
    },
    {
        "category": "SEO Generators",
        "name": "Meta Description Generator",
        "slug": "meta-description-generator-tool",
        "desc": "Generate click-worthy and search-optimized meta description tags.",
        "formula": "Description = Hook + Value Proposition + CTA",
        "formula_desc": "Integrates page keywords, benefit descriptions, and call-to-actions while tracking the 160 character limit.",
        "icon": "📝",
        "inputs": [
            {"id": "desc-kw", "label": "Target Keyword:", "type": "text", "default": "convert PDF to Word"},
            {"id": "desc-val", "label": "Value Proposition (e.g. fast, free, online):", "type": "text", "default": "convert document formats instantly offline"},
            {"id": "desc-brand", "label": "Brand Name:", "type": "text", "default": "Enginewheels"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Optimized Meta Description:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('desc-kw').value.trim();
            const val = document.getElementById('desc-val').value.trim();
            const brand = document.getElementById('desc-brand').value.trim();

            if (!kw || !val) {
                showToast("Please enter target keyword and value proposition.", "error");
                return;
            }

            const desc = `Looking to ${kw}? Use the free tool by ${brand} to ${val}. Fast, secure, and client-side processing!`;
            const len = desc.length;

            let feedback = `<span class='text-success'>Good length: ${len} chars (Google limit is ~160).</span>`;
            if (len > 160) {
                feedback = `<span class='text-danger'>Too long: ${len} chars (Recommended <= 160). Page description might be cut off.</span>`;
            }

            document.getElementById('text-output').value = desc;
            updateBreakdown(`<p>${feedback}</p>`);
        """
    },
    {
        "category": "SEO Generators",
        "name": "Schema Markup Generator",
        "slug": "schema-markup-generator-tool",
        "desc": "Generate website structured JSON-LD schema tags for search engines.",
        "formula": "JSON-LD WebSite schema compilation",
        "formula_desc": "Compiles structured organization metadata tags consumed by Google search crawlers.",
        "icon": "🛠️",
        "inputs": [
            {"id": "sch-name", "label": "Site / Brand Name:", "type": "text", "default": "Enginewheels"},
            {"id": "sch-url", "label": "Website URL:", "type": "text", "default": "https://enginewheels.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "JSON-LD Script Output:", "type": "textarea"}
        ],
        "calc_js": """
            const name = document.getElementById('sch-name').value.trim();
            const url = document.getElementById('sch-url').value.trim();
            if (!name || !url) {
                showToast("Please enter website name and URL.", "error");
                return;
            }

            const schema = {
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": name,
                "url": url
            };

            const script = '<script type="application/' + 'ld+json">\\n' + JSON.stringify(schema, null, 2) + '\\n</' + 'script>';
            document.getElementById('text-output').value = script;
            updateBreakdown("<p class='text-success'>JSON-LD website schema generated. Place inside HTML head or body.</p>");
        """
    },
    {
        "category": "SEO Generators",
        "name": "Sitemap Generator",
        "slug": "sitemap-generator-tool",
        "desc": "Generate standard XML sitemaps for search engine indexing submissions.",
        "formula": "XML Urlset schema matching",
        "formula_desc": "Constructs structured sitemap.xml files based on a list of input URLs.",
        "icon": "🗺️",
        "inputs": [
            {"id": "site-urls", "label": "URLs (One per line):", "type": "textarea", "default": "https://enginewheels.com\\nhttps://enginewheels.com/about.html"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Sitemap XML Output:", "type": "textarea"}
        ],
        "calc_js": """
            const text = document.getElementById('site-urls').value.trim();
            if (!text) {
                showToast("Please enter at least one URL.", "error");
                return;
            }

            const urls = text.split(/\\n+/).map(u => u.trim()).filter(u => u);
            const date = new Date().toISOString().split('T')[0];

            let xml = '<?xml version="1.0" encoding="UTF-8"?>\\n';
            xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n';
            urls.forEach(url => {
                xml += '  <url>\\n';
                xml += `    <loc>${url}</loc>\\n`;
                xml += `    <lastmod>${date}</lastmod>\\n`;
                xml += '    <priority>0.80</priority>\\n';
                xml += '  </url>\\n';
            });
            xml += '</urlset>';

            document.getElementById('text-output').value = xml;
            updateBreakdown("<p class='text-success'>Sitemap XML file compiled successfully.</p>");
        """
    },
    {
        "category": "SEO Generators",
        "name": "Robots.txt Generator",
        "slug": "robots-txt-generator-tool",
        "desc": "Generate custom robots.txt directives for search crawlers.",
        "formula": "User-agent Allow/Disallow rule compilations",
        "formula_desc": "Formats robots.txt direct rules to guide Googlebot, Bingbot, or general search agents.",
        "icon": "🤖",
        "inputs": [
            {"id": "rob-agent", "label": "Target User-Agent:", "type": "text", "default": "*"},
            {"id": "rob-disallow", "label": "Disallow Directories (Comma Separated):", "type": "text", "default": "/admin,/private"},
            {"id": "rob-sitemap", "label": "Sitemap URL:", "type": "text", "default": "https://enginewheels.com/sitemap.xml"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Robots.txt Content:", "type": "textarea"}
        ],
        "calc_js": """
            const agent = document.getElementById('rob-agent').value.trim() || "*";
            const disallow = document.getElementById('rob-disallow').value.trim();
            const sitemap = document.getElementById('rob-sitemap').value.trim();

            let rules = `User-agent: ${agent}\\n`;
            if (disallow) {
                const paths = disallow.split(',').map(p => p.trim()).filter(p => p);
                paths.forEach(p => {
                    rules += `Disallow: ${p}\\n`;
                });
            } else {
                rules += "Disallow:\\n";
            }

            if (sitemap) {
                rules += `Sitemap: ${sitemap}\\n`;
            }

            document.getElementById('text-output').value = rules;
            updateBreakdown("<p class='text-success'>Robots.txt directives configured.</p>");
        """
    },
    {
        "category": "SEO Generators",
        "name": "Canonical URL Generator",
        "slug": "canonical-url-generator-tool",
        "desc": "Generate canonical URL tag links to prevent duplicate page indexing issues.",
        "formula": "HTML link rel=canonical syntax construction",
        "formula_desc": "Wraps URLs in search-engine-readable relative or absolute HTML links.",
        "icon": "🔗",
        "inputs": [
            {"id": "can-url", "label": "Preferred Page URL:", "type": "text", "default": "https://enginewheels.com/category/generators.html"}
        ],
        "outputs": [
            {"id": "text-output", "label": "HTML Canonical Link Tag:", "type": "textarea"}
        ],
        "calc_js": """
            const url = document.getElementById('can-url').value.trim();
            if (!url) {
                showToast("Please enter page URL.", "error");
                return;
            }

            const tag = `<link rel="canonical" href="${url}">`;
            document.getElementById('text-output').value = tag;
            updateBreakdown("<p class='text-success'>Canonical HTML link tag generated.</p>");
        """
    },
    {
        "category": "SEO Generators",
        "name": "Open Graph Generator",
        "slug": "open-graph-generator",
        "desc": "Generate Facebook Open Graph meta tags for beautiful social sharing previews.",
        "formula": "og meta tag syntax formatting",
        "formula_desc": "Generates og:title, og:description, and og:image tags consumed by Facebook crawler bots.",
        "icon": "📊",
        "inputs": [
            {"id": "og-title", "label": "OG Title:", "type": "text", "default": "Amazing Free Online Tools"},
            {"id": "og-desc", "label": "OG Description:", "type": "text", "default": "Explore 100+ offline-first client-side web utility tools."},
            {"id": "og-url", "label": "OG Page URL:", "type": "text", "default": "https://enginewheels.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Open Graph HTML Meta Tags:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('og-title').value.trim();
            const desc = document.getElementById('og-desc').value.trim();
            const url = document.getElementById('og-url').value.trim();

            let og = `<meta property="og:title" content="${title}">\\n`;
            og += `<meta property="og:description" content="${desc}">\\n`;
            og += `<meta property="og:url" content="${url}">\\n`;
            og += `<meta property="og:type" content="website">`;

            document.getElementById('text-output').value = og;
            updateBreakdown("<p class='text-success'>Open Graph meta tags generated successfully.</p>");
        """
    },
    {
        "category": "SEO Generators",
        "name": "Twitter Card Generator",
        "slug": "twitter-card-generator",
        "desc": "Generate Twitter / X Card meta tags for rich social post attachments.",
        "formula": "twitter:card meta tag formatting",
        "formula_desc": "Prepares summary and large image Twitter cards for feed rendering algorithms.",
        "icon": "🐦",
        "inputs": [
            {"id": "tw-title", "label": "Twitter Title:", "type": "text", "default": "Amazing Free Online Tools"},
            {"id": "tw-desc", "label": "Twitter Description:", "type": "text", "default": "Explore 100+ offline-first client-side web utility tools."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Twitter Card HTML Meta Tags:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('tw-title').value.trim();
            const desc = document.getElementById('tw-desc').value.trim();

            let tw = `<meta name="twitter:card" content="summary">\\n`;
            tw += `<meta name="twitter:title" content="${title}">\\n`;
            tw += `<meta name="twitter:description" content="${desc}">`;

            document.getElementById('text-output').value = tw;
            updateBreakdown("<p class='text-success'>Twitter Card metadata tags generated.</p>");
        """
    },
    {
        "category": "SEO Generators",
        "name": "FAQ Schema Generator",
        "slug": "faq-schema-generator-tool",
        "desc": "Generate structured JSON-LD FAQPage schemas to qualify for Google search rich snippets.",
        "formula": "FAQPage JSON-LD schema matching",
        "formula_desc": "Combines questions and answers into Google-readable structured data scripts.",
        "icon": "❓",
        "inputs": [
            {"id": "faq-q1", "label": "Question 1:", "type": "text", "default": "What is Enginewheels?"},
            {"id": "faq-a1", "label": "Answer 1:", "type": "text", "default": "Enginewheels is a free directory of offline-first utility tools."}
        ],
        "outputs": [
            {"id": "text-output", "label": "JSON-LD FAQ Schema Output:", "type": "textarea"}
        ],
        "calc_js": """
            const q1 = document.getElementById('faq-q1').value.trim();
            const a1 = document.getElementById('faq-a1').value.trim();

            if (!q1 || !a1) {
                showToast("Please enter Question 1 and Answer 1.", "error");
                return;
            }

            const schema = {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": q1,
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": a1
                        }
                    }
                ]
            };

            const script = '<script type="application/' + 'ld+json">\\n' + JSON.stringify(schema, null, 2) + '\\n</' + 'script>';
            document.getElementById('text-output').value = script;
            updateBreakdown("<p class='text-success'>FAQ JSON-LD schema compiled.</p>");
        """
    },
    {
        "category": "SEO Generators",
        "name": "Hreflang Generator",
        "slug": "hreflang-generator-tool",
        "desc": "Generate localized hreflang link tags for international multi-language SEO sites.",
        "formula": "alternate link rel=hreflang format compilation",
        "formula_desc": "Generates localized alternates mapping languages (en, es, de, fr) to regional URLs.",
        "icon": "🌐",
        "inputs": [
            {"id": "href-url", "label": "Language Page URL:", "type": "text", "default": "https://enginewheels.com/es/"},
            {"id": "href-lang", "label": "Language Code (e.g. es):", "type": "text", "default": "es"}
        ],
        "outputs": [
            {"id": "text-output", "label": "HTML Hreflang Tag Output:", "type": "textarea"}
        ],
        "calc_js": """
            const url = document.getElementById('href-url').value.trim();
            const lang = document.getElementById('href-lang').value.trim().toLowerCase();

            if (!url || !lang) {
                showToast("Please fill in URL and language code.", "error");
                return;
            }

            const tag = `<link rel="alternate" hreflang="${lang}" href="${url}">`;
            document.getElementById('text-output').value = tag;
            updateBreakdown("<p class='text-success'>Hreflang localization alternate link generated.</p>");
        """
    },
    {
        "category": "Social Media Generators",
        "name": "Hashtag Generator",
        "slug": "hashtag-generator-tool",
        "desc": "Generate trending hashtags for Instagram, Twitter, and TikTok posts based on keywords.",
        "formula": "Social hashtag compiling",
        "formula_desc": "Combines base keywords with high-performing social hashtag suffixes.",
        "icon": "#️⃣",
        "inputs": [
            {"id": "hash-kw", "label": "Enter Base Keyword:", "type": "text", "default": "travel"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Hashtag Output:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('hash-kw').value.trim().replace(/#/g, '');
            if (!kw) {
                showToast("Please enter a keyword.", "error");
                return;
            }

            const suffixes = ["life", "photography", "vibes", "adventure", "daily", "community", "world", "goals", "love", "style"];
            const hashes = suffixes.map(s => `#${kw}${s}`);
            hashes.unshift(`#${kw}`);

            document.getElementById('text-output').value = hashes.join(" ");
            updateBreakdown("<p class='text-success'>Generated hashtags successfully.</p>");
        """
    },
    {
        "category": "Social Media Generators",
        "name": "Instagram Bio Generator",
        "slug": "instagram-bio-generator",
        "desc": "Generate attractive, structured bios with emojis for your Instagram profile.",
        "formula": "Emoji-styled bio outlines",
        "formula_desc": "Organizes job titles, personal values, and Call to Actions with aesthetic dividers.",
        "icon": "📸",
        "inputs": [
            {"id": "bio-niche", "label": "Your Profession / Niche:", "type": "text", "default": "Designer & Creator"},
            {"id": "bio-cta", "label": "Profile CTA / Link (e.g. Buy my art 👇):", "type": "text", "default": "Check my work 👇"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Aesthetic Instagram Bio Suggestions:", "type": "textarea"}
        ],
        "calc_js": """
            const niche = document.getElementById('bio-niche').value.trim();
            const cta = document.getElementById('bio-cta').value.trim();

            if (!niche) {
                showToast("Please enter your profession.", "error");
                return;
            }

            const bio1 = `✨ ${niche}\\n🎨 Creating magic daily\\n📍 Based in California\\n🔗 ${cta}`;
            const bio2 = `👋 Hey there! Welcome to my feed\\n🚀 Passionate about ${niche}\\n💌 Collabs: info@domain.com\\n👉 ${cta}`;

            document.getElementById('text-output').value = `${bio1}\\n\\n====================\\n\\n${bio2}`;
            updateBreakdown("<p class='text-success'>Generated bio suggestions with emojis.</p>");
        """
    },
    {
        "category": "Social Media Generators",
        "name": "TikTok Bio Generator",
        "slug": "tiktok-bio-generator",
        "desc": "Generate punchy and short bios matching TikTok's character limit.",
        "formula": "Short punchy hooks layout",
        "formula_desc": "Assembles short social bio tags designed to quickly capture attention under 80 characters.",
        "icon": "🎵",
        "inputs": [
            {"id": "tt-niche", "label": "TikTok Topic:", "type": "text", "default": "Coding Tips"}
        ],
        "outputs": [
            {"id": "text-output", "label": "TikTok Bios:", "type": "textarea"}
        ],
        "calc_js": """
            const niche = document.getElementById('tt-niche').value.trim();
            if (!niche) {
                showToast("Please enter a topic.", "error");
                return;
            }

            const bios = [
                `⚡ Daily ${niche} hacks | Follow for more!`,
                `Just a coder sharing ${niche} 🚀`,
                `Making ${niche} easy. New videos daily! 👇`,
                `Welcome to my ${niche} corner ✨`
            ];

            document.getElementById('text-output').value = bios.join("\\n\\n");
            updateBreakdown("<p class='text-success'>Punchy TikTok bios generated.</p>");
        """
    },
    {
        "category": "Social Media Generators",
        "name": "LinkedIn Headline Generator",
        "slug": "linkedin-headline-generator",
        "desc": "Generate professional headlines to attract recruiters and profile visits.",
        "formula": "Job Title + Benefit proposition compounding",
        "formula_desc": "Combines target job roles, key technical competencies, and value statements.",
        "icon": "💼",
        "inputs": [
            {"id": "li-role", "label": "Current Job Role:", "type": "text", "default": "Software Engineer"},
            {"id": "li-skill", "label": "Primary Skill (e.g. React):", "type": "text", "default": "Python & Cloud"}
        ],
        "outputs": [
            {"id": "text-output", "label": "LinkedIn Headline Suggestions:", "type": "textarea"}
        ],
        "calc_js": """
            const role = document.getElementById('li-role').value.trim();
            const skill = document.getElementById('li-skill').value.trim();

            if (!role || !skill) {
                showToast("Please fill in role and primary skill.", "error");
                return;
            }

            const heads = [
                `${role} | Specializing in ${skill} | Building scalable developer utilities`,
                `${role} @ Startup | Helping companies scale using ${skill}`,
                `Passionate ${role} | Expert in ${skill} | Let's connect!`
            ];

            document.getElementById('text-output').value = heads.join("\\n\\n");
            updateBreakdown("<p class='text-success'>Professional headlines compiled.</p>");
        """
    },
    {
        "category": "Social Media Generators",
        "name": "Facebook Post Generator",
        "slug": "facebook-post-generator",
        "desc": "Generate engaging Facebook posts with headlines and calls to action.",
        "formula": "Post body spacing with CTAs",
        "formula_desc": "Packs descriptions, questions, and link prompts with spacing for readability.",
        "icon": "👥",
        "inputs": [
            {"id": "fb-topic", "label": "What is the post about?", "type": "text", "default": "launching a new web tool"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Facebook Post:", "type": "textarea"}
        ],
        "calc_js": """
            const topic = document.getElementById('fb-topic').value.trim();
            if (!topic) {
                showToast("Please enter a topic.", "error");
                return;
            }

            const post = `🚀 BIG NEWS! 🚀\\n\\nWe are excited to announce that we are officially ${topic}! This has been in the works for a while, and we can't wait for you to try it.\\n\\nCheck it out here and let us know your thoughts: [Insert Link]\\n\\nHave questions? Comment below! 👇`;
            document.getElementById('text-output').value = post;
            updateBreakdown("<p class='text-success'>Facebook post drafted.</p>");
        """
    },
    {
        "category": "Social Media Generators",
        "name": "Twitter/X Post Generator",
        "slug": "twitter-post-generator",
        "desc": "Generate short, punchy tweets within Twitter's 280-character limit.",
        "formula": "280-character restricted formatting",
        "formula_desc": "Ensures generated social updates conform to the 280 character limit.",
        "icon": "🐦",
        "inputs": [
            {"id": "tw-message", "label": "Core Message:", "type": "text", "default": "Launched a free offline-first password generator tool."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Tweet Output:", "type": "textarea"}
        ],
        "calc_js": """
            const msg = document.getElementById('tw-message').value.trim();
            if (!msg) {
                showToast("Please enter a core message.", "error");
                return;
            }

            const tweet = `🚀 Just launched: ${msg}\\n\\n100% free, runs client-side in the browser, and requires no registration. Check it out! 👇\\n\\n#buildinpublic #dev`;
            const len = tweet.length;

            let feedback = `<span class='text-success'>Length: ${len} chars (OK, <= 280 limit).</span>`;
            if (len > 280) {
                feedback = `<span class='text-danger'>Tweet exceeds 280 characters (${len} chars). Please shorten message.</span>`;
            }

            document.getElementById('text-output').value = tweet;
            updateBreakdown(`<p>${feedback}</p>`);
        """
    },
    {
        "category": "Social Media Generators",
        "name": "YouTube Bio Generator",
        "slug": "youtube-bio-generator",
        "desc": "Generate description copy for your YouTube channel About page.",
        "formula": "About description template styling",
        "formula_desc": "Synthesizes YouTube channel introductions, target audience descriptions, and scheduling outlines.",
        "icon": "🎥",
        "inputs": [
            {"id": "yt-channel", "label": "Channel Name:", "type": "text", "default": "CodeLabs"},
            {"id": "yt-topic", "label": "Main Topic:", "type": "text", "default": "Web Dev Tutorials"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Channel About Description:", "type": "textarea"}
        ],
        "calc_js": """
            const name = document.getElementById('yt-channel').value.trim();
            const topic = document.getElementById('yt-topic').value.trim();

            if (!name || !topic) {
                showToast("Please fill in channel name and topic.", "error");
                return;
            }

            const desc = `Welcome to ${name}! 🎬\\n\\nOn this channel, we share simple and practical guides about ${topic}. Whether you are a beginner looking to get started or an expert brushing up on skills, there is something here for you.\\n\\n📅 New videos uploaded weekly!\\n\\n🔔 Subscribe to stay updated and join the community.`;
            document.getElementById('text-output').value = desc;
            updateBreakdown("<p class='text-success'>YouTube channel About copy compiled.</p>");
        """
    },
    {
        "category": "Social Media Generators",
        "name": "Pinterest Description Generator",
        "slug": "pinterest-description-generator",
        "desc": "Generate search-friendly Pinterest pin descriptions with target hashtags.",
        "formula": "Pinterest search meta tag compiler",
        "formula_desc": "Combines pin title keywords, helpful descriptions, and relevant Pinterest tags.",
        "icon": "📌",
        "inputs": [
            {"id": "pin-title", "label": "Pin Title / Subject:", "type": "text", "default": "DIY Room Decor"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Pin Description Output:", "type": "textarea"}
        ],
        "calc_js": """
            const title = document.getElementById('pin-title').value.trim();
            if (!title) {
                showToast("Please enter a title.", "error");
                return;
            }

            const desc = `Looking for inspiring ideas for ${title}? Here is a complete guide to help you get started. Check the full steps and tips inside! #diy #${title.toLowerCase().replace(/\\s+/g, '')} #homedecor #inspiration`;
            document.getElementById('text-output').value = desc;
            updateBreakdown("<p class='text-success'>Pinterest Pin description drafted.</p>");
        """
    },
    {
        "category": "Social Media Generators",
        "name": "Social Media Username Generator",
        "slug": "social-username-generator-tool",
        "desc": "Generate general social media handle suggestions checkable across networks.",
        "formula": "Multi-network username prefix mapping",
        "formula_desc": "Combines niche indicators and brand names to form compatible, readable user handles.",
        "icon": "👤",
        "inputs": [
            {"id": "handle-base", "label": "Enter Base Name:", "type": "text", "default": "alex"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Social Handles:", "type": "textarea"}
        ],
        "calc_js": """
            const base = document.getElementById('handle-base').value.trim().toLowerCase().replace(/[^a-z0-9]/g, '');
            if (!base) {
                showToast("Please enter a base name.", "error");
                return;
            }

            const handles = [
                base,
                `its${base}`,
                `the${base}`,
                `iam${base}`,
                `${base}_hq`,
                `${base}_design`
            ];

            document.getElementById('text-output').value = handles.join("\\n");
            updateBreakdown("<p class='text-success'>Compiled social media handles.</p>");
        """
    },
    {
        "category": "Social Media Generators",
        "name": "Influencer Name Generator",
        "slug": "influencer-name-generator",
        "desc": "Generate catchy personal brand and influencer names.",
        "formula": "Persona branding compound mapping",
        "formula_desc": "Assembles persona descriptors (Vibe, Glow, Chief) with personal name elements.",
        "icon": "🌟",
        "inputs": [
            {"id": "inf-style", "label": "Influencer Vibe:", "type": "select", "default": "lifestyle",
             "options": [
                 ("lifestyle", "Lifestyle & Vibe"),
                 ("tech", "Tech & Coding"),
                 ("gaming", "Gaming & Gaming")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Influencer Brand Names:", "type": "textarea"}
        ],
        "calc_js": """
            const style = document.getElementById('inf-style').value;

            let prefix = [];
            let suffix = [];
            if (style === "lifestyle") {
                prefix = ["Glow", "Urban", "Vibe", "Daily", "Aura", "Pure"];
                suffix = ["Life", "Chic", "Diaries", "Vibe", "Style", "Grace"];
            } else if (style === "tech") {
                prefix = ["Byte", "Code", "Pixel", "Tech", "Sync", "Cyber"];
                suffix = ["Master", "Guru", "Whip", "Dev", "Node", "Hustler"];
            } else {
                prefix = ["Apex", "Nova", "Steel", "Blaze", "Glitch", "Hyper"];
                suffix = ["Slayer", "Raider", "Fury", "Sniper", "Gamer", "Play"];
            }

            let names = [];
            for (let i = 0; i < 5; i++) {
                let p = prefix[Math.floor(Math.random() * prefix.length)];
                let s = suffix[Math.floor(Math.random() * suffix.length)];
                names.push(p + s);
            }

            document.getElementById('text-output').value = names.join("\\n");
            updateBreakdown("<p class='text-success'>Catchy influencer brand names compiled.</p>");
        """
    }
]

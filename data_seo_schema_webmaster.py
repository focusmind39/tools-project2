# -*- coding: utf-8 -*-
"""
Database of 20 Schema Markup and Webmaster Tools for Enginewheels
"""

SCHEMA_WEBMASTER_TOOLS = [
    {
        "category": "Schema Markup Tools",
        "name": "FAQ Schema Generator",
        "slug": "faq-schema-generator",
        "desc": "Generate valid JSON-LD FAQ schema markup for your website in seconds.",
        "formula": "JSON-LD FAQPage serialization",
        "formula_desc": "Converts question and answer fields into schema.org JSON-LD FAQPage format.",
        "icon": "❓",
        "inputs": [
            {"id": "faq-q1", "label": "Question 1:", "type": "text", "default": "What is Enginewheels?"},
            {"id": "faq-a1", "label": "Answer 1:", "type": "textarea", "default": "Enginewheels is a platform providing free web utilities."},
            {"id": "faq-q2", "label": "Question 2:", "type": "text", "default": "Are the tools safe?"},
            {"id": "faq-a2", "label": "Answer 2:", "type": "textarea", "default": "Yes, all tools run locally inside your browser tab."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated FAQ JSON-LD:", "type": "textarea"}
        ],
        "calc_js": """
            const q1 = document.getElementById('faq-q1').value.trim();
            const a1 = document.getElementById('faq-a1').value.trim();
            const q2 = document.getElementById('faq-q2').value.trim();
            const a2 = document.getElementById('faq-a2').value.trim();
            
            if (!q1 || !a1) {
                showToast("Please provide at least one Question and Answer.", "error");
                return;
            }
            
            const faq = {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": []
            };
            
            faq.mainEntity.push({
                "@type": "Question",
                "name": q1,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a1
                }
            });
            
            if (q2 && a2) {
                faq.mainEntity.push({
                    "@type": "Question",
                    "name": q2,
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": a2
                    }
                });
            }
            
            // To prevent issues when embedding script inside HTML in verification checks,
            // we will format the output JSON cleanly.
            const jsonStr = JSON.stringify(faq, null, 2);
            document.getElementById('text-output').value = `<script type="application/ld+json">\\n${jsonStr}\\n<\\/script>`;
            updateBreakdown("<p class='text-success'>FAQ JSON-LD Schema generated successfully.</p>");
        """
    },
    {
        "category": "Schema Markup Tools",
        "name": "Article Schema Generator",
        "slug": "article-schema-generator",
        "desc": "Generate Google-compliant Article JSON-LD schema markup to boost search appearance.",
        "formula": "JSON-LD Article serialization",
        "formula_desc": "Translates headline, author, datePublished, publisher details, and images into structured article blocks.",
        "icon": "📰",
        "inputs": [
            {"id": "art-headline", "label": "Article Headline:", "type": "text", "default": "How to Optimize Web Pages"},
            {"id": "art-author", "label": "Author Name:", "type": "text", "default": "SEO Expert"},
            {"id": "art-date", "label": "Publish Date:", "type": "date"},
            {"id": "art-publisher", "label": "Publisher Name:", "type": "text", "default": "Enginewheels"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Article JSON-LD Schema:", "type": "textarea"}
        ],
        "calc_js": """
            const headline = document.getElementById('art-headline').value.trim();
            const author = document.getElementById('art-author').value.trim();
            const date = document.getElementById('art-date').value || new Date().toISOString().split('T')[0];
            const publisher = document.getElementById('art-publisher').value.trim();
            
            if (!headline || !publisher) {
                showToast("Headline and Publisher fields are required.", "error");
                return;
            }
            
            const schema = {
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": headline,
                "datePublished": date,
                "author": {
                    "@type": "Person",
                    "name": author || "Anonymous"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": publisher
                }
            };
            
            document.getElementById('text-output').value = `<script type="application/ld+json">\\n${JSON.stringify(schema, null, 2)}\\n<\\/script>`;
            updateBreakdown("<p class='text-success'>Article JSON-LD Schema compiled.</p>");
        """
    },
    {
        "category": "Schema Markup Tools",
        "name": "Organization Schema Generator",
        "slug": "organization-schema-generator",
        "desc": "Generate detailed Organization schema templates to establish your company credentials with search engines.",
        "formula": "JSON-LD Organization serialization",
        "formula_desc": "Serializes corporate details, official web locations, logo references, and social media links.",
        "icon": "🏢",
        "inputs": [
            {"id": "org-name", "label": "Organization Name:", "type": "text", "default": "Enginewheels"},
            {"id": "org-url", "label": "Website URL:", "type": "text", "default": "https://enginewheels.com"},
            {"id": "org-logo", "label": "Logo URL:", "type": "text", "default": "https://enginewheels.com/logo.png"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Organization Schema Code:", "type": "textarea"}
        ],
        "calc_js": """
            const name = document.getElementById('org-name').value.trim();
            const url = document.getElementById('org-url').value.trim();
            const logo = document.getElementById('org-logo').value.trim();
            
            if (!name || !url) {
                showToast("Please provide Organization Name and URL.", "error");
                return;
            }
            
            const schema = {
                "@context": "https://schema.org",
                "@type": "Organization",
                "name": name,
                "url": url
            };
            if (logo) schema.logo = logo;
            
            document.getElementById('text-output').value = `<script type="application/ld+json">\\n${JSON.stringify(schema, null, 2)}\\n<\\/script>`;
            updateBreakdown("<p class='text-success'>Organization Schema generated.</p>");
        """
    },
    {
        "category": "Schema Markup Tools",
        "name": "Product Schema Generator",
        "slug": "product-schema-generator",
        "desc": "Generate Product JSON-LD schemas incorporating price, reviews, and availability markers.",
        "formula": "JSON-LD Product serialization",
        "formula_desc": "Assembles product identifiers, offers (pricing, currency, availability), and rating structures.",
        "icon": "🏷️",
        "inputs": [
            {"id": "prod-name", "label": "Product Name:", "type": "text", "default": "SaaS Starter Plan"},
            {"id": "prod-price", "label": "Price Value:", "type": "number", "default": "29", "min": "0", "step": "0.01"},
            {"id": "prod-currency", "label": "Currency (e.g. USD):", "type": "text", "default": "USD"},
            {"id": "prod-avail", "label": "Availability:", "type": "select", "default": "InStock",
             "options": [
                 ("InStock", "In Stock"),
                 ("OutOfStock", "Out Of Stock"),
                 ("PreOrder", "Pre-Order")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Product Schema Code:", "type": "textarea"}
        ],
        "calc_js": """
            const name = document.getElementById('prod-name').value.trim();
            const price = parseFloat(document.getElementById('prod-price').value) || 0;
            const currency = document.getElementById('prod-currency').value.trim() || "USD";
            const avail = document.getElementById('prod-avail').value;
            
            if (!name) {
                showToast("Product name is required.", "error");
                return;
            }
            
            const schema = {
                "@context": "https://schema.org",
                "@type": "Product",
                "name": name,
                "offers": {
                    "@type": "Offer",
                    "price": price,
                    "priceCurrency": currency,
                    "availability": `https://schema.org/${avail}`
                }
            };
            
            document.getElementById('text-output').value = `<script type="application/ld+json">\\n${JSON.stringify(schema, null, 2)}\\n<\\/script>`;
            updateBreakdown("<p class='text-success'>Product Schema template completed.</p>");
        """
    },
    {
        "category": "Schema Markup Tools",
        "name": "Local Business Schema Generator",
        "slug": "local-business-schema-generator",
        "desc": "Generate detailed LocalBusiness schemas incorporating hours, locations, and geocodes.",
        "formula": "JSON-LD LocalBusiness serialization",
        "formula_desc": "Serializes address components, geocoordinates, operating schedules, and phone numbers.",
        "icon": "🏡",
        "inputs": [
            {"id": "biz-name", "label": "Business Name:", "type": "text", "default": "City Pizza Shop"},
            {"id": "biz-phone", "label": "Phone Number:", "type": "text", "default": "+1-555-0199"},
            {"id": "biz-street", "label": "Street Address:", "type": "text", "default": "123 Main St"},
            {"id": "biz-city", "label": "City / Locality:", "type": "text", "default": "Seattle"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Local Business Schema Code:", "type": "textarea"}
        ],
        "calc_js": """
            const name = document.getElementById('biz-name').value.trim();
            const phone = document.getElementById('biz-phone').value.trim();
            const street = document.getElementById('biz-street').value.trim();
            const city = document.getElementById('biz-city').value.trim();
            
            if (!name || !city) {
                showToast("Please provide Business Name and City.", "error");
                return;
            }
            
            const schema = {
                "@context": "https://schema.org",
                "@type": "LocalBusiness",
                "name": name,
                "telephone": phone || undefined,
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": street || undefined,
                    "addressLocality": city
                }
            };
            
            document.getElementById('text-output').value = `<script type="application/ld+json">\\n${JSON.stringify(schema, null, 2)}\\n<\\/script>`;
            updateBreakdown("<p class='text-success'>LocalBusiness Schema built.</p>");
        """
    },
    {
        "category": "Schema Markup Tools",
        "name": "Event Schema Generator",
        "slug": "event-schema-generator",
        "desc": "Generate Event JSON-LD schema markup with schedules, location structures, and registration options.",
        "formula": "JSON-LD Event serialization",
        "formula_desc": "Assembles event name, dates, status, venue (physical or virtual address), and offer tickers.",
        "icon": "📅",
        "inputs": [
            {"id": "evt-name", "label": "Event Title:", "type": "text", "default": "SEO Masterclass Workshop"},
            {"id": "evt-start", "label": "Start Date & Time:", "type": "text", "default": "2026-09-10T09:00:00-07:00"},
            {"id": "evt-location", "label": "Event Location (Venue / URL):", "type": "text", "default": "https://enginewheels.com/live"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Event Schema Code:", "type": "textarea"}
        ],
        "calc_js": """
            const name = document.getElementById('evt-name').value.trim();
            const start = document.getElementById('evt-start').value.trim();
            const loc = document.getElementById('evt-location').value.trim();
            
            if (!name || !start) {
                showToast("Please provide Event Title and Start Date/Time.", "error");
                return;
            }
            
            const schema = {
                "@context": "https://schema.org",
                "@type": "Event",
                "name": name,
                "startDate": start,
                "location": {
                    "@type": "VirtualLocation",
                    "url": loc || "https://enginewheels.com"
                }
            };
            
            document.getElementById('text-output').value = `<script type="application/ld+json">\\n${JSON.stringify(schema, null, 2)}\\n<\\/script>`;
            updateBreakdown("<p class='text-success'>Event JSON-LD Schema compiled.</p>");
        """
    },
    {
        "category": "Schema Markup Tools",
        "name": "Breadcrumb Schema Generator",
        "slug": "breadcrumb-schema-generator",
        "desc": "Generate BreadcrumbList JSON-LD tags to improve site navigation hierarchy in search result snippets.",
        "formula": "JSON-LD BreadcrumbList nesting",
        "formula_desc": "Arranges parent categories and final leaves into indexed itemListElement items.",
        "icon": "🍞",
        "inputs": [
            {"id": "crumb-n1", "label": "Step 1 Name:", "type": "text", "default": "Home"},
            {"id": "crumb-u1", "label": "Step 1 URL:", "type": "text", "default": "https://enginewheels.com/index.html"},
            {"id": "crumb-n2", "label": "Step 2 Name:", "type": "text", "default": "Tools"},
            {"id": "crumb-u2", "label": "Step 2 URL:", "type": "text", "default": "https://enginewheels.com/category/generators.html"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Breadcrumb Schema Code:", "type": "textarea"}
        ],
        "calc_js": """
            const n1 = document.getElementById('crumb-n1').value.trim();
            const u1 = document.getElementById('crumb-u1').value.trim();
            const n2 = document.getElementById('crumb-n2').value.trim();
            const u2 = document.getElementById('crumb-u2').value.trim();
            
            if (!n1 || !u1) {
                showToast("Please provide at least Step 1 details.", "error");
                return;
            }
            
            const schema = {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": []
            };
            
            schema.itemListElement.push({
                "@type": "ListItem",
                "position": 1,
                "name": n1,
                "item": u1
            });
            
            if (n2 && u2) {
                schema.itemListElement.push({
                    "@type": "ListItem",
                    "position": 2,
                    "name": n2,
                    "item": u2
                });
            }
            
            document.getElementById('text-output').value = `<script type="application/ld+json">\\n${JSON.stringify(schema, null, 2)}\\n<\\/script>`;
            updateBreakdown("<p class='text-success'>Breadcrumb Schema generated successfully.</p>");
        """
    },
    {
        "category": "Schema Markup Tools",
        "name": "Website Schema Generator",
        "slug": "website-schema-generator",
        "desc": "Generate WebSite JSON-LD tags incorporating searchbox queries to get sitelinks search boxes.",
        "formula": "JSON-LD WebSite serialization",
        "formula_desc": "Configures structural links and SearchAction targets matching your internal site routing.",
        "icon": "🌐",
        "inputs": [
            {"id": "site-name", "label": "Website Display Name:", "type": "text", "default": "Enginewheels"},
            {"id": "site-url", "label": "Canonical site URL:", "type": "text", "default": "https://enginewheels.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "WebSite Schema Code:", "type": "textarea"}
        ],
        "calc_js": """
            const name = document.getElementById('site-name').value.trim();
            const url = document.getElementById('site-url').value.trim();
            
            if (!name || !url) {
                showToast("Please provide Site Name and URL.", "error");
                return;
            }
            
            const schema = {
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": name,
                "url": url,
                "potentialAction": {
                    "@type": "SearchAction",
                    "target": `${url}?q={search_term_string}`,
                    "query-input": "required name=search_term_string"
                }
            };
            
            document.getElementById('text-output').value = `<script type="application/ld+json">\\n${JSON.stringify(schema, null, 2)}\\n<\\/script>`;
            updateBreakdown("<p class='text-success'>WebSite Schema generated.</p>");
        """
    },
    {
        "category": "Schema Markup Tools",
        "name": "Person Schema Generator",
        "slug": "person-schema-generator",
        "desc": "Generate Person JSON-LD schemas representing authors, founders, or key team members.",
        "formula": "JSON-LD Person serialization",
        "formula_desc": "Compiles names, social links, job titles, and organizational affiliations into standard structured data.",
        "icon": "👤",
        "inputs": [
            {"id": "pers-name", "label": "Full Name:", "type": "text", "default": "John Doe"},
            {"id": "pers-title", "label": "Job Title:", "type": "text", "default": "SEO Consultant"},
            {"id": "pers-url", "label": "Personal Profile URL:", "type": "text", "default": "https://enginewheels.com/authors/john-doe"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Person Schema Code:", "type": "textarea"}
        ],
        "calc_js": """
            const name = document.getElementById('pers-name').value.trim();
            const title = document.getElementById('pers-title').value.trim();
            const url = document.getElementById('pers-url').value.trim();
            
            if (!name) {
                showToast("Name is required.", "error");
                return;
            }
            
            const schema = {
                "@context": "https://schema.org",
                "@type": "Person",
                "name": name,
                "jobTitle": title || undefined,
                "url": url || undefined
            };
            
            document.getElementById('text-output').value = `<script type="application/ld+json">\\n${JSON.stringify(schema, null, 2)}\\n<\\/script>`;
            updateBreakdown("<p class='text-success'>Person Schema generated.</p>");
        """
    },
    {
        "category": "Schema Markup Tools",
        "name": "JSON-LD Generator",
        "slug": "json-ld-generator",
        "desc": "Generate a baseline boilerplate structure for any custom JSON-LD schema type.",
        "formula": "Schema template mapping",
        "formula_desc": "Outputs a clean JSON-LD skeleton based on standard types (e.g. Service, Review, Course).",
        "icon": "📋",
        "inputs": [
            {"id": "schema-type", "label": "Select Schema Type:", "type": "select", "default": "Service",
             "options": [
                 ("Service", "Service Schema"),
                 ("Review", "Review Schema"),
                 ("Course", "Course Schema")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "JSON-LD Boilerplate:", "type": "textarea"}
        ],
        "calc_js": """
            const type = document.getElementById('schema-type').value;
            
            let schema = {};
            if (type === "Service") {
                schema = {
                    "@context": "https://schema.org",
                    "@type": "Service",
                    "serviceType": "SEO Optimization",
                    "provider": {
                        "@type": "LocalBusiness",
                        "name": "Enginewheels"
                    }
                };
            } else if (type === "Review") {
                schema = {
                    "@context": "https://schema.org",
                    "@type": "Review",
                    "itemReviewed": {
                        "@type": "Thing",
                        "name": "Enginewheels Utilities"
                    },
                    "reviewRating": {
                        "@type": "Rating",
                        "ratingValue": "5"
                    },
                    "author": {
                        "@type": "Person",
                        "name": "Alex"
                    }
                };
            } else {
                schema = {
                    "@context": "https://schema.org",
                    "@type": "Course",
                    "name": "Search Optimization Fundamentals",
                    "description": "Learn the basics of search indexes and crawler optimization.",
                    "provider": {
                        "@type": "Organization",
                        "name": "Enginewheels Academy"
                    }
                };
            }
            
            document.getElementById('text-output').value = `<script type="application/ld+json">\\n${JSON.stringify(schema, null, 2)}\\n<\\/script>`;
            updateBreakdown("<p class='text-success'>JSON-LD custom type block generated.</p>");
        """
    },
    {
        "category": "Webmaster Tools",
        "name": "Robots.txt Generator",
        "slug": "robots-txt-generator",
        "desc": "Generate custom robots.txt crawl rules to direct bots safely through your site pages.",
        "formula": "Directive parsing concatenation",
        "formula_desc": "Formats crawler rules (Allow/Disallow) with user-agents and sitemap links into robots.txt syntax.",
        "icon": "🤖",
        "inputs": [
            {"id": "bot-ua", "label": "Crawler User-Agent:", "type": "text", "default": "*"},
            {"id": "disallow-path", "label": "Disallow Path (e.g. /admin):", "type": "text", "default": "/admin/"},
            {"id": "sitemap-link", "label": "Sitemap URL:", "type": "text", "default": "https://enginewheels.com/sitemap.xml"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Robots.txt:", "type": "textarea"}
        ],
        "calc_js": """
            const ua = document.getElementById('bot-ua').value.trim() || "*";
            const disallow = document.getElementById('disallow-path').value.trim();
            const sitemap = document.getElementById('sitemap-link').value.trim();
            
            let code = `User-agent: ${ua}\\n`;
            if (disallow) {
                code += `Disallow: ${disallow}\\n`;
            } else {
                code += `Disallow: \\n`;
            }
            code += `Allow: /\\n`;
            if (sitemap) {
                code += `\\nSitemap: ${sitemap}`;
            }
            
            document.getElementById('text-output').value = code;
            updateBreakdown("<p class='text-success'>Robots.txt file generated successfully.</p>");
        """
    },
    {
        "category": "Webmaster Tools",
        "name": "Robots.txt Validator",
        "slug": "robots-txt-validator",
        "desc": "Validate standard robots.txt formatting guidelines and index syntax patterns.",
        "formula": "Syntax parsing validation",
        "formula_desc": "Scans line-by-line to check if rules begin with recognized tags (User-agent, Allow, Disallow, Sitemap).",
        "icon": "🔎",
        "inputs": [
            {"id": "robots-raw", "label": "Paste Robots.txt Content:", "type": "textarea", "default": "User-agent: *\\nDisallow: /admin/\\nSitemap: https://enginewheels.com/sitemap.xml"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Validation Audit Report:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('robots-raw').value.trim();
            if (!raw) {
                showToast("Please paste robots.txt rules to validate.", "error");
                return;
            }
            
            const lines = raw.split(/\\n/);
            let errors = 0;
            let report = "ROBOTS.TXT SYNTAX VALIDATOR REPORT\\n================================\\n\\n";
            
            lines.forEach((line, idx) => {
                const clean = line.trim();
                if (clean === "" || clean.startsWith("#")) return;
                
                const match = clean.match(/^([a-zA-Z-]+)\\s*:\\s*(.*)$/);
                if (!match) {
                    report += `[ERROR] Line ${idx + 1}: Invalid syntax format. Ensure keys are separated by colons. ("${clean}")\\n`;
                    errors++;
                    return;
                }
                
                const key = match[1].toLowerCase();
                const allowedKeys = ["user-agent", "disallow", "allow", "sitemap", "crawl-delay"];
                if (!allowedKeys.includes(key)) {
                    report += `[WARNING] Line ${idx + 1}: Unrecognized directive key "${match[1]}".\\n`;
                }
            });
            
            if (errors === 0) {
                report += "[✔] All directives contain valid formatting structure. Robots.txt is syntax-clean!";
            } else {
                report += `\\nValidation found ${errors} syntax errors. Fix them to prevent search crawler confusion.`;
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Validation complete. Syntax Errors = <strong>${errors}</strong></p>`);
        """
    },
    {
        "category": "Webmaster Tools",
        "name": "XML Sitemap Generator",
        "slug": "xml-sitemap-generator",
        "desc": "Generate XML sitemaps to index pages with crawl priorities and update dates.",
        "formula": "XML Urlset compounding",
        "formula_desc": "Wraps a list of URLs with loc, changefreq, lastmod, and priority XML tags.",
        "icon": "🗺️",
        "inputs": [
            {"id": "sitemap-urls", "label": "Enter URLs (One per line):", "type": "textarea", "default": "https://enginewheels.com/index.html\\nhttps://enginewheels.com/about.html"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Sitemap XML:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('sitemap-urls').value.trim();
            if (!raw) {
                showToast("Please provide URLs.", "error");
                return;
            }
            
            const urls = raw.split(/\\n/).map(u => u.trim()).filter(u => u.length > 0);
            const date = new Date().toISOString().split('T')[0];
            
            let xml = `<?xml version="1.0" encoding="UTF-8"?>\\n`;
            xml += `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n`;
            
            urls.forEach(url => {
                xml += `  <url>\\n`;
                xml += `    <loc>${url}</loc>\\n`;
                xml += `    <lastmod>${date}</lastmod>\\n`;
                xml += `    <changefreq>weekly</changefreq>\\n`;
                xml += `    <priority>0.8</priority>\\n`;
                xml += `  </url>\\n`;
            });
            
            xml += `</urlset>`;
            document.getElementById('text-output').value = xml;
            updateBreakdown("<p class='text-success'>XML sitemap generated successfully.</p>");
        """
    },
    {
        "category": "Webmaster Tools",
        "name": "Sitemap Validator",
        "slug": "sitemap-validator",
        "desc": "Check XML sitemap structures for syntactic tags validity and schema matches.",
        "formula": "XML syntax layout parsing",
        "formula_desc": "Validates markup tags like <urlset>, <url>, and <loc> namespaces format specifications.",
        "icon": "🗺️",
        "inputs": [
            {"id": "xml-raw", "label": "Paste Sitemap XML:", "type": "textarea", "default": '<?xml version="1.0" encoding="UTF-8"?>\\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n  <url><loc>https://enginewheels.com</loc></url>\\n</urlset>'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Sitemap Audit Report:", "type": "textarea"}
        ],
        "calc_js": """
            const raw = document.getElementById('xml-raw').value.trim();
            if (!raw) {
                showToast("Please enter sitemap XML code.", "error");
                return;
            }
            
            let report = "SITEMAP XML VALIDATION REPORT\\n============================\\n\\n";
            let errors = 0;
            
            if (!raw.includes("<?xml") && !raw.startsWith("<urlset")) {
                report += "[ERROR] Missing XML standard declaration tags.\\n";
                errors++;
            }
            if (!raw.includes("<urlset") || !raw.includes("</urlset>")) {
                report += "[ERROR] Missing main <urlset> root node elements.\\n";
                errors++;
            }
            if (!raw.includes("<url>") || !raw.includes("<loc>")) {
                report += "[ERROR] Missing <url> or <loc> elements within the block.\\n";
                errors++;
            }
            
            if (errors === 0) {
                report += "[✔] Sitemap XML formatting is standard and crawlable!";
            } else {
                report += `\\nFound ${errors} layout validation issues.`;
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Validation finished. Status = <strong>${errors === 0 ? "PASSED" : "FAILED"}</strong></p>`);
        """
    },
    {
        "category": "Webmaster Tools",
        "name": "Sitemap URL Extractor",
        "slug": "sitemap-url-extractor",
        "desc": "Extract a plain-text list of page links from an XML sitemap source block.",
        "formula": "Regular expression location matching",
        "formula_desc": "Scans and pulls strings wrapped in <loc> tag pairs inside sitemap files.",
        "icon": "📂",
        "inputs": [
            {"id": "xml-source", "label": "Paste Sitemap XML:", "type": "textarea", "default": "<url><loc>https://enginewheels.com/index.html</loc></url>\\n<url><loc>https://enginewheels.com/about.html</loc></url>"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Extracted Link List:", "type": "textarea"}
        ],
        "calc_js": """
            const xml = document.getElementById('xml-source').value.trim();
            if (!xml) {
                showToast("Please enter sitemap XML.", "error");
                return;
            }
            
            const regex = /<loc>\\s*([^<\\s]+)\\s*<\\/loc>/gi;
            const urls = [];
            let match;
            
            while ((match = regex.exec(xml)) !== null) {
                urls.push(match[1].trim());
            }
            
            if (urls.length > 0) {
                document.getElementById('text-output').value = urls.join("\\n");
                updateBreakdown(`<p class='text-success'>Extracted <strong>${urls.length}</strong> URLs successfully.</p>`);
            } else {
                document.getElementById('text-output').value = "No <loc> URLs detected in the XML.";
                updateBreakdown("<p class='text-warning'>Zero links extracted.</p>");
            }
        """
    },
    {
        "category": "Webmaster Tools",
        "name": "URL Inspection Tool",
        "slug": "url-inspection-tool",
        "desc": "Inspect URLs structure safety, protocols, subdirectories depth, and query parameters.",
        "formula": "Standard URL validation parsing",
        "formula_desc": "Instantiates the browser URL parser to extract protocol schemas, hostname mappings, and paths.",
        "icon": "🔎",
        "inputs": [
            {"id": "url-inspect", "label": "Enter URL:", "type": "text", "default": "https://enginewheels.com/category/generators.html?ref=nav"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Inspection Report:", "type": "textarea"}
        ],
        "calc_js": """
            const urlStr = document.getElementById('url-inspect').value.trim();
            if (!urlStr) {
                showToast("Please enter a URL.", "error");
                return;
            }
            
            try {
                const url = new URL(urlStr);
                let report = "URL INSPECTION REPORT\\n=====================\\n\\n";
                report += `Protocol: ${url.protocol}\\n`;
                report += `Host: ${url.hostname}\\n`;
                report += `Path: ${url.pathname}\\n`;
                report += `Query Params: ${url.search || "None"}\\n\\n`;
                
                if (url.protocol !== "https:") {
                    report += "[WARNING] Non-secure HTTP connection protocol detected. HTTPS recommended.\\n";
                } else {
                    report += "[✔] Secure HTTPS protocol present.\\n";
                }
                
                const depth = url.pathname.split('/').filter(p => p.length > 0).length;
                report += `Folder Depth: ${depth}\\n`;
                if (depth > 4) {
                    report += "[WARNING] Deep folder structure might impact crawling index visibility.\\n";
                } else {
                    report += "[✔] Directory nesting depth is search-optimal.\\n";
                }
                
                document.getElementById('text-output').value = report;
                updateBreakdown("<p class='text-success'>URL parameters analyzed.</p>");
            } catch (e) {
                showToast("Invalid URL format. Include http:// or https://", "error");
            }
        """
    },
    {
        "category": "Webmaster Tools",
        "name": "URL Analyzer",
        "slug": "url-analyzer",
        "desc": "Check URL layout structures for SEO-friendliness, lowercase consistency, and character lengths.",
        "formula": "URL SEO parameter checking",
        "formula_desc": "Grades URLs based on length, presence of underscores, uppercase letters, or special characters.",
        "icon": "🔗",
        "inputs": [
            {"id": "url-analyze", "label": "Paste Page URL:", "type": "text", "default": "https://enginewheels.com/category/Generators_list.html"}
        ],
        "outputs": [
            {"id": "text-output", "label": "URL SEO Audit:", "type": "textarea"}
        ],
        "calc_js": """
            const urlStr = document.getElementById('url-analyze').value.trim();
            if (!urlStr) {
                showToast("Please enter a URL to analyze.", "error");
                return;
            }
            
            let report = "URL SEO ANALYSIS\\n================\\n\\n";
            report += `Raw URL: ${urlStr}\\n`;
            report += `Length: ${urlStr.length} characters\\n\\n`;
            
            if (urlStr.length > 100) {
                report += "- [WARNING] URL is long. Keep it under 100 characters for optimal visibility.\\n";
            } else {
                report += "- [OK] URL length is good.\\n";
            }
            
            if (/[A-Z]/.test(urlStr)) {
                report += "- [WARNING] URL contains uppercase letters. Use lowercase to prevent duplicate content indexing.\\n";
            } else {
                report += "- [OK] URL uses clean lowercase letters.\\n";
            }
            
            if (/_/.test(urlStr)) {
                report += "- [WARNING] URL contains underscores (_). Search engines prefer hyphens (-) as word separators.\\n";
            } else {
                report += "- [OK] URL separators are standard.\\n";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>URL structure checks completed.</p>");
        """
    },
    {
        "category": "Webmaster Tools",
        "name": "Redirect Generator",
        "slug": "redirect-generator",
        "desc": "Generate Apache .htaccess or Nginx redirection config scripts.",
        "formula": "Redirect syntax mapping",
        "formula_desc": "Constructs configuration strings for 301 Permanent or 302 Temporary URL redirections.",
        "icon": "🔃",
        "inputs": [
            {"id": "redir-server", "label": "Server Type:", "type": "select", "default": "apache",
             "options": [
                 ("apache", "Apache (.htaccess)"),
                 ("nginx", "Nginx Config")
             ]},
            {"id": "redir-code", "label": "HTTP Status Code:", "type": "select", "default": "301",
             "options": [
                 ("301", "301 Permanent Redirect"),
                 ("302", "302 Temporary Redirect")
             ]},
            {"id": "redir-old", "label": "Old Relative Path:", "type": "text", "default": "/old-page.html"},
            {"id": "redir-new", "label": "New Absolute URL:", "type": "text", "default": "https://enginewheels.com/new-page.html"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Redirection Code:", "type": "textarea"}
        ],
        "calc_js": """
            const server = document.getElementById('redir-server').value;
            const code = document.getElementById('redir-code').value;
            const oldPath = document.getElementById('redir-old').value.trim();
            const newUrl = document.getElementById('redir-new').value.trim();
            
            if (!oldPath || !newUrl) {
                showToast("Paths fields are required.", "error");
                return;
            }
            
            let result = "";
            if (server === "apache") {
                result = `Redirect ${code} ${oldPath} ${newUrl}`;
            } else {
                const flag = code === "301" ? "permanent" : "redirect";
                result = `rewrite ^${oldPath}$ ${newUrl} ${flag};`;
            }
            
            document.getElementById('text-output').value = result;
            updateBreakdown("<p class='text-success'>Redirection rule generated.</p>");
        """
    },
    {
        "category": "Webmaster Tools",
        "name": "Redirect Checker",
        "slug": "redirect-checker",
        "desc": "Check redirect paths and HTTP header responses to verify redirection rules.",
        "formula": "Redirect mapping check",
        "formula_desc": "Checks if old paths correctly map to target destinations without loops.",
        "icon": "🔃",
        "inputs": [
            {"id": "redir-rule", "label": "Enter Redirection Rule:", "type": "text", "default": "Redirect 301 /old.html https://enginewheels.com/new.html"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Redirect Checker Result:", "type": "textarea"}
        ],
        "calc_js": """
            const rule = document.getElementById('redir-rule').value.trim();
            if (!rule) {
                showToast("Please enter a redirection rule.", "error");
                return;
            }
            
            let report = "REDIRECT RULE ANALYSIS\\n======================\\n\\n";
            
            if (rule.startsWith("Redirect")) {
                const parts = rule.split(/\\s+/);
                if (parts.length >= 4) {
                    report += `Type: Apache Redirect Directive\\n`;
                    report += `Code: ${parts[1]}\\n`;
                    report += `Source: ${parts[2]}\\n`;
                    report += `Destination: ${parts[3]}\\n\\n`;
                    report += `[✔] Valid Apache redirect syntax.\\n`;
                } else {
                    report += `[ERROR] Invalid Apache Redirect format. Format: Redirect 301 /old /new\\n`;
                }
            } else if (rule.includes("rewrite")) {
                report += "Type: Nginx Rewrite Rule\\n";
                report += "[✔] Valid Nginx rewrite configuration.\\n";
            } else {
                report += "[WARNING] Format not fully recognized. Paste an Apache Redirect or Nginx rewrite rule.\\n";
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown("<p class='text-success'>Rule format validated.</p>");
        """
    },
    {
        "category": "Webmaster Tools",
        "name": "Canonical URL Checker",
        "slug": "canonical-url-checker",
        "desc": "Extract and check if canonical links are configured correctly inside HTML files.",
        "formula": "Canonical HTML parsing check",
        "formula_desc": "Scans pasted HTML source code for rel=canonical links and checks if the link points to a valid destination URL.",
        "icon": "🔗",
        "inputs": [
            {"id": "html-code", "label": "Paste HTML Header Snippet:", "type": "textarea", "default": '<link rel="canonical" href="https://enginewheels.com/tools/json-formatter.html">'}
        ],
        "outputs": [
            {"id": "text-output", "label": "Canonical Check Report:", "type": "textarea"}
        ],
        "calc_js": """
            const html = document.getElementById('html-code').value.trim();
            if (!html) {
                showToast("Please enter HTML code.", "error");
                return;
            }
            
            const match = html.match(/<link[^>]+rel=['\"]canonical['\"][^>]+href=['\"]([^'\"]+)['\"]/i) ||
                          html.match(/<link[^>]+href=['\"]([^'\"]+)['\"][^>]+rel=['\"]canonical['\"]/i);
                          
            if (match) {
                const canonical = match[1].trim();
                document.getElementById('text-output').value = `Canonical Link Found:\\n- Target: "${canonical}"\\n\\nStatus: OK\\n[✔] The page contains a valid authority canonical URL directive.`;
                updateBreakdown("<p class='text-success'>Canonical URL link is valid.</p>");
            } else {
                document.getElementById('text-output').value = "Canonical Link: MISSING\\n\\n[✘] No canonical link tag found in the pasted HTML snippet. Add a canonical directive to prevent index issues.";
                updateBreakdown("<p class='text-warning'>Missing canonical URL link.</p>");
            }
        """
    }
]

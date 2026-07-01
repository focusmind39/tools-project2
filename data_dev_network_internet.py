# -*- coding: utf-8 -*-
"""
Database of 10 Network & Internet Tools for Enginewheels
"""

NETWORK_INTERNET_TOOLS = [
    {
        "category": "Network & Internet Tools",
        "name": "IP Address Lookup",
        "slug": "ip-address-lookup",
        "desc": "Retrieve geo-location, ISP, and connection metadata for your active public IP address.",
        "formula": "fetch('https://ipapi.co/json/')",
        "formula_desc": "Sends a client fetch request to a public geolocation API to retrieve location details without server-side storage.",
        "icon": "🔍",
        "inputs": [
            {"id": "ip-query", "label": "Enter IP (leave blank for your IP):", "type": "text", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "IP Metadata Output:", "type": "textarea"}
        ],
        "calc_js": """
            const ip = document.getElementById('ip-query').value.trim();
            const endpoint = ip ? `https://ipapi.co/${ip}/json/` : 'https://ipapi.co/json/';
            
            document.getElementById('text-output').value = "Locating IP details...";
            fetch(endpoint)
                .then(res => res.json())
                .then(data => {
                    if (data.error) {
                        throw new Error(data.reason || "IP lookup failed.");
                    }
                    let out = `IP Address: ${data.ip}\\n`;
                    out += `City: ${data.city}\\n`;
                    out += `Region: ${data.region}\\n`;
                    out += `Country: ${data.country_name}\\n`;
                    out += `ISP: ${data.org}\\n`;
                    out += `Latitude/Longitude: ${data.latitude}, ${data.longitude}`;
                    document.getElementById('text-output').value = out;
                    updateBreakdown("<p class='text-success'>IP details loaded from public geo-IP registry.</p>");
                })
                .catch(err => {
                    document.getElementById('text-output').value = "Lookup failed: " + err.message + "\\n\\n(Note: Public API limits or browser blocks might affect execution. Try entering a specific public IP.)";
                    showToast("IP Lookup failed!", "error");
                });
        """
    },
    {
        "category": "Network & Internet Tools",
        "name": "IP Address Validator",
        "slug": "ip-address-validator",
        "desc": "Check if an IP address is a valid IPv4 or IPv6 format.",
        "formula": "IPv4 Regex Check || IPv6 Regex Check",
        "formula_desc": "Applies standard regular expression pattern matching rules to verify IP structures.",
        "icon": "🛠️",
        "inputs": [
            {"id": "ip-val", "label": "Enter IP Address:", "type": "text", "default": "192.168.1.1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Validation Result:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('ip-val').value.trim();
            if (!val) {
                showToast("Please enter an IP address.", "error");
                return;
            }
            const ipv4Regex = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
            const ipv6Regex = /^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$/;
            
            if (ipv4Regex.test(val)) {
                document.getElementById('text-output').value = "✓ Valid IPv4 Address\\n\\nConforms to standard octet format.";
                updateBreakdown("<p class='text-success'>IPv4 check succeeded.</p>");
            } else if (ipv6Regex.test(val)) {
                document.getElementById('text-output').value = "✓ Valid IPv6 Address\\n\\nConforms to 128-bit hex formatting.";
                updateBreakdown("<p class='text-success'>IPv6 check succeeded.</p>");
            } else {
                document.getElementById('text-output').value = "✗ Invalid IP Address\\n\\nDoes not conform to IPv4 or IPv6 layouts.";
                updateBreakdown("<p class='text-danger'>Validation failed.</p>");
                showToast("Invalid IP format!", "error");
            }
        """
    },
    {
        "category": "Network & Internet Tools",
        "name": "DNS Lookup",
        "slug": "dns-lookup",
        "desc": "Query DNS A, AAAA, MX, and TXT records using public DNS over HTTPS interfaces.",
        "formula": "fetch('https://cloudflare-dns.com/dns-query')",
        "formula_desc": "Fires secure requests directly to Cloudflare DNS resolvers to pull domain record arrays.",
        "icon": "🌐",
        "inputs": [
            {"id": "dns-domain", "label": "Domain Name:", "type": "text", "default": "enginewheels.com"},
            {"id": "dns-type", "label": "Record Type:", "type": "select", "options": [("A", "A (IPv4)"), ("AAAA", "AAAA (IPv6)"), ("MX", "MX (Mail Exchange)"), ("TXT", "TXT (Text Record)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "DNS Records Output:", "type": "textarea"}
        ],
        "calc_js": """
            const domain = document.getElementById('dns-domain').value.trim();
            const type = document.getElementById('dns-type').value;
            
            if (!domain) {
                showToast("Please enter a domain.", "error");
                return;
            }
            
            document.getElementById('text-output').value = `Querying DNS record ${type} for ${domain}...`;
            fetch(`https://cloudflare-dns.com/dns-query?name=${domain}&type=${type}`, {
                headers: { 'accept': 'application/dns-json' }
            })
            .then(res => res.json())
            .then(data => {
                if (data.Answer) {
                    let out = `Results for ${domain} (${type}):\\n\\n`;
                    data.Answer.forEach(ans => {
                        out += `Name: ${ans.name}\\nTTL: ${ans.TTL} seconds\\nData: ${ans.data}\\n\\n`;
                    });
                    document.getElementById('text-output').value = out.trim();
                    updateBreakdown("<p class='text-success'>DNS records fetched successfully from Cloudflare DNS.</p>");
                } else {
                    document.getElementById('text-output').value = `No ${type} records found for ${domain}.`;
                }
            })
            .catch(err => {
                document.getElementById('text-output').value = "DNS query failed: " + err.message;
                showToast("DNS Lookup failed!", "error");
            });
        """
    },
    {
        "category": "Network & Internet Tools",
        "name": "Reverse DNS Lookup",
        "slug": "reverse-dns-lookup",
        "desc": "Simulate reverse PTR DNS lookups to find hostnames mapped to IP addresses.",
        "formula": "rDNS PTR Record Query",
        "formula_desc": "Queries reverse IP mappings using Cloudflare DNS over HTTPS API.",
        "icon": "🌐",
        "inputs": [
            {"id": "rdns-ip", "label": "Enter IP Address:", "type": "text", "default": "1.1.1.1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "PTR Records Output:", "type": "textarea"}
        ],
        "calc_js": """
            const ip = document.getElementById('rdns-ip').value.trim();
            if (!ip) {
                showToast("Please enter an IP address.", "error");
                return;
            }
            const parts = ip.split('.');
            if (parts.length !== 4) {
                showToast("Only IPv4 reverse lookup supported.", "error");
                return;
            }
            const ptrDomain = parts.reverse().join('.') + '.in-addr.arpa';
            document.getElementById('text-output').value = `Querying PTR record for ${ip}...`;
            
            fetch(`https://cloudflare-dns.com/dns-query?name=${ptrDomain}&type=PTR`, {
                headers: { 'accept': 'application/dns-json' }
            })
            .then(res => res.json())
            .then(data => {
                if (data.Answer) {
                    let out = "";
                    data.Answer.forEach(ans => {
                        out += `PTR Result: ${ans.data}\\n`;
                    });
                    document.getElementById('text-output').value = out.trim();
                    updateBreakdown("<p class='text-success'>Reverse DNS lookup succeeded.</p>");
                } else {
                    document.getElementById('text-output').value = `No PTR record found for ${ip}.`;
                }
            })
            .catch(err => {
                document.getElementById('text-output').value = "rDNS query failed: " + err.message;
                showToast("Reverse DNS lookup failed!", "error");
            });
        """
    },
    {
        "category": "Network & Internet Tools",
        "name": "HTTP Header Checker",
        "slug": "http-header-checker",
        "desc": "Simulate and check standard HTTP headers sent during page requests.",
        "formula": "fetch(url) -> Response Headers",
        "formula_desc": "Evaluates response header parameters using client-side JavaScript requests.",
        "icon": "🔒",
        "inputs": [
            {"id": "head-url", "label": "Enter URL:", "type": "text", "default": "https://jsonplaceholder.typicode.com/posts/1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Response Headers Log:", "type": "textarea"}
        ],
        "calc_js": """
            const url = document.getElementById('head-url').value.trim();
            if (!url) {
                showToast("Please enter URL.", "error");
                return;
            }
            document.getElementById('text-output').value = "Connecting to " + url + "...";
            fetch(url)
                .then(res => {
                    let out = `HTTP Status: ${res.status} ${res.statusText}\\n\\nHeaders:\\n`;
                    res.headers.forEach((val, key) => {
                        out += `${key}: ${val}\\n`;
                    });
                    document.getElementById('text-output').value = out;
                    updateBreakdown("<p class='text-success'>Headers loaded. (Note: Only headers permitted under CORS policies are displayed in browsers.)</p>");
                })
                .catch(err => {
                    document.getElementById('text-output').value = "CORS warning: Target server blocked client header inspection.\\n\\nMock Header Example:\\nContent-Type: text/html; charset=UTF-8\\nCache-Control: max-age=604800\\nServer: Enginewheels Mock Resolver";
                    showToast("CORS warning!", "error");
                });
        """
    },
    {
        "category": "Network & Internet Tools",
        "name": "User Agent Parser",
        "slug": "user-agent-parser",
        "desc": "Parse and identify OS, browser engine, and device brand metrics from active user-agents.",
        "formula": "navigator.userAgent Parser",
        "formula_desc": "Scans client browser info strings, filtering version numbers for display.",
        "icon": "🤖",
        "inputs": [
            {"id": "ua-input", "label": "User Agent String (leave blank for yours):", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Parsed Browser Specs:", "type": "textarea"}
        ],
        "calc_js": """
            let ua = document.getElementById('ua-input').value.trim();
            if (!ua) {
                ua = navigator.userAgent;
            }
            
            let browser = "Unknown";
            let os = "Unknown OS";
            
            if (ua.includes('Firefox')) browser = 'Mozilla Firefox';
            else if (ua.includes('Chrome')) browser = 'Google Chrome';
            else if (ua.includes('Safari')) browser = 'Apple Safari';
            else if (ua.includes('Edge')) browser = 'Microsoft Edge';
            
            if (ua.includes('Windows')) os = 'Microsoft Windows';
            else if (ua.includes('Macintosh')) os = 'macOS';
            else if (ua.includes('Android')) os = 'Android OS';
            else if (ua.includes('iPhone') || ua.includes('iPad')) os = 'Apple iOS';
            else if (ua.includes('Linux')) os = 'Linux';
            
            document.getElementById('text-output').value = `User Agent: ${ua}\\n\\nDetected OS: ${os}\\nDetected Browser: ${browser}`;
            updateBreakdown("<p class='text-success'>User Agent parsed locally in browser session.</p>");
        """
    },
    {
        "category": "Network & Internet Tools",
        "name": "MIME Type Lookup",
        "slug": "mime-type-lookup",
        "desc": "Check standard MIME types associated with file extensions.",
        "formula": "Extension to MIME Mapping Table",
        "formula_desc": "References standard content-type strings associated with common extension codes.",
        "icon": "📁",
        "inputs": [
            {"id": "mime-ext", "label": "Enter File Extension (e.g. png, json):", "type": "text", "default": "json"}
        ],
        "outputs": [
            {"id": "out-mime", "label": "MIME Content-Type:", "type": "text"}
        ],
        "calc_js": """
            const ext = document.getElementById('mime-ext').value.trim().toLowerCase().replace('.', '');
            const mimeMap = {
                'json': 'application/json',
                'html': 'text/html',
                'css': 'text/css',
                'js': 'application/javascript',
                'png': 'image/png',
                'jpg': 'image/jpeg',
                'jpeg': 'image/jpeg',
                'webp': 'image/webp',
                'svg': 'image/svg+xml',
                'xml': 'application/xml',
                'pdf': 'application/pdf',
                'zip': 'application/zip'
            };
            const type = mimeMap[ext] || 'application/octet-stream (Fallback)';
            document.getElementById('out-mime').textContent = type;
            updateBreakdown(`<p class='text-success'>MIME mapping resolved. Content-Type Header: <code>${type}</code></p>`);
        """
    },
    {
        "category": "Network & Internet Tools",
        "name": "Port Reference Tool",
        "slug": "port-reference-tool",
        "desc": "Check standard TCP/UDP networking port numbers and descriptions.",
        "formula": "Standard Port Numbers Directory",
        "formula_desc": "Returns port rules defined under IANA protocols records.",
        "icon": "🔌",
        "inputs": [
            {"id": "port-num", "label": "Enter Port Number (e.g. 80, 443, 22):", "type": "number", "default": "443"}
        ],
        "outputs": [
            {"id": "out-port-desc", "label": "Protocol/Description:", "type": "text"}
        ],
        "calc_js": """
            const port = parseInt(document.getElementById('port-num').value);
            const portMap = {
                21: 'FTP (File Transfer Protocol)',
                22: 'SSH (Secure Shell) / SFTP',
                23: 'Telnet (Unencrypted Text)',
                25: 'SMTP (Simple Mail Transfer Protocol)',
                53: 'DNS (Domain Name System)',
                80: 'HTTP (Hypertext Transfer Protocol)',
                110: 'POP3 (Post Office Protocol v3)',
                143: 'IMAP (Internet Message Access Protocol)',
                443: 'HTTPS (HTTP Secure)',
                3306: 'MySQL Database System',
                5432: 'PostgreSQL Database System'
            };
            const desc = portMap[port] || 'Custom / Private Port Definition';
            document.getElementById('out-port-desc').textContent = desc;
            updateBreakdown("<p class='text-success'>Port resolved.</p>");
        """
    },
    {
        "category": "Network & Internet Tools",
        "name": "HTTP Status Code Reference",
        "slug": "http-status-code-reference",
        "desc": "Check definitions for HTTP status response codes.",
        "formula": "HTTP Status Registry Map",
        "formula_desc": "References standard definitions for 2xx, 3xx, 4xx, and 5xx HTTP response categories.",
        "icon": "📶",
        "inputs": [
            {"id": "status-code", "label": "Enter HTTP Status Code:", "type": "number", "default": "404"}
        ],
        "outputs": [
            {"id": "out-status-desc", "label": "Status Code Category & Description:", "type": "text"}
        ],
        "calc_js": """
            const code = parseInt(document.getElementById('status-code').value);
            const statusMap = {
                200: 'OK - Request succeeded.',
                201: 'Created - Resource created.',
                301: 'Moved Permanently - URL updated.',
                302: 'Found - Temporary redirection.',
                400: 'Bad Request - Syntax issues.',
                401: 'Unauthorized - Credentials missing.',
                403: 'Forbidden - Access denied.',
                404: 'Not Found - Resource missing.',
                500: 'Internal Server Error - Server crash.',
                502: 'Bad Gateway - Upstream failure.',
                503: 'Service Unavailable - Load issues.'
            };
            const desc = statusMap[code] || 'Custom / Undefined HTTP Status';
            document.getElementById('out-status-desc').textContent = desc;
            updateBreakdown("<p class='text-success'>HTTP status code description resolved.</p>");
        """
    },
    {
        "category": "Network & Internet Tools",
        "name": "URL Parser",
        "slug": "url-parser",
        "desc": "Parse URL strings into separate hostname, protocol, search queries, and port properties.",
        "formula": "new URL(inputString) parser elements",
        "formula_desc": "Evaluates strings using browser URL parsers, dividing parameters into an attributes list.",
        "icon": "🌐",
        "inputs": [
            {"id": "text-input", "label": "Enter URL to Parse:", "type": "text", "default": "https://enginewheels.com:8080/tools/url-parser.html?q=dev#hash"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Parsed URL Parameters:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter a URL.", "error");
                return;
            }
            try {
                const url = new URL(val);
                let out = `Protocol: ${url.protocol}\\n`;
                out += `Hostname: ${url.hostname}\\n`;
                out += `Port: ${url.port || 'Default'}\\n`;
                out += `Pathname: ${url.pathname}\\n`;
                out += `Search Parameters: ${url.search}\\n`;
                out += `Hash Anchor: ${url.hash}`;
                document.getElementById('text-output').value = out;
                updateBreakdown("<p class='text-success'>URL parsed successfully.</p>");
            } catch(e) {
                document.getElementById('text-output').value = "Parsing failed: " + e.message;
                showToast("Invalid URL format!", "error");
            }
        """
    }
]

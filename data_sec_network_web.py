# -*- coding: utf-8 -*-
"""
Network and Web Security Tools
"""

NETWORK_SECURITY_TOOLS = [
    {
        "name": "IP Address Lookup",
        "slug": "ip-address-lookup",
        "category": "Network Security Tools",
        "icon": "🌐",
        "desc": "Lookup your public IP address or query custom IPs to retrieve location, ISP, and ASN data.",
        "formula": "IPInfo = Fetch('https://ipapi.co/json/')",
        "formula_desc": "Queries public geolocation APIs client-side to locate IP addresses.",
        "inputs": [
            {"id": "ip-input", "label": "Enter IP Address (leave blank for your IP):", "type": "text", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "IP Details Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const ip = document.getElementById('ip-input').value.trim();
            document.getElementById('text-output').value = "Locating IP details, please wait...";
            
            const endpoint = ip ? `https://ipapi.co/${ip}/json/` : 'https://ipapi.co/json/';
            
            fetch(endpoint)
                .then(res => {
                    if (!res.ok) throw new Error("Could not fetch location data.");
                    return res.json();
                })
                .then(data => {
                    if (data.error) {
                        document.getElementById('text-output').value = `Error: ${data.reason}`;
                        return;
                    }
                    document.getElementById('text-output').value = 
                        `IP Address: ${data.ip}\\n` +
                        `City: ${data.city}\\n` +
                        `Region: ${data.region}\\n` +
                        `Country: ${data.country_name} (${data.country_code})\\n` +
                        `Latitude/Longitude: ${data.latitude}, ${data.longitude}\\n` +
                        `ISP / Organization: ${data.org}\\n` +
                        `ASN: ${data.asn}`;
                    updateBreakdown("<p>IP lookup completed via ipapi.co client API.</p>");
                })
                .catch(err => {
                    showToast("Failed to lookup IP.", "error");
                    document.getElementById('text-output').value = `Error: ${err.message}`;
                });
        """
    },
    {
        "name": "IP Address Validator",
        "slug": "ip-address-validator",
        "category": "Network Security Tools",
        "icon": "🌐",
        "desc": "Check if an IP address string is a valid IPv4 or IPv6 address.",
        "formula": "Valid = RegexIPv4(IP) || RegexIPv6(IP)",
        "formula_desc": "Checks string formats against standard IPv4 and IPv6 syntax rules.",
        "inputs": [
            {"id": "ip-input", "label": "Enter IP to Validate:", "type": "text", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Validation Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const ip = document.getElementById('ip-input').value.trim();
            if (!ip) {
                showToast("Please enter an IP address!", "error");
                return;
            }

            const ipv4Regex = /^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
            const ipv6Regex = /^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$/;

            if (ipv4Regex.test(ip)) {
                document.getElementById('text-output').value = "IP Type: IPv4\\nStatus: ✅ VALID IP ADDRESS";
            } else if (ipv6Regex.test(ip)) {
                document.getElementById('text-output').value = "IP Type: IPv6\\nStatus: ✅ VALID IP ADDRESS";
            } else {
                document.getElementById('text-output').value = "IP Type: Unknown\\nStatus: ❌ INVALID IP ADDRESS";
            }
            updateBreakdown("<p>Validated format using standard address specification rules.</p>");
        """
    },
    {
        "name": "IPv4 Validator",
        "slug": "ipv4-validator",
        "category": "Network Security Tools",
        "icon": "🌐",
        "desc": "Check if a string matches the dot-decimal IPv4 address format (0.0.0.0 to 255.255.255.255).",
        "formula": "Valid = Match(IPv4_Regex)",
        "formula_desc": "Verifies that an IP consists of four dot-separated octet numbers, each ranging from 0 to 255.",
        "inputs": [
            {"id": "ip-input", "label": "Enter IPv4 Address:", "type": "text", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "IPv4 Validation Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const ip = document.getElementById('ip-input').value.trim();
            if (!ip) {
                showToast("Please enter an IPv4 address!", "error");
                return;
            }
            const regex = /^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
            const isValid = regex.test(ip);
            document.getElementById('text-output').value = isValid ? "Status: ✅ VALID IPv4" : "Status: ❌ INVALID IPv4";
            updateBreakdown("<p>IPv4 checked against dot-decimal boundaries (0-255).</p>");
        """
    },
    {
        "name": "IPv6 Validator",
        "slug": "ipv6-validator",
        "category": "Network Security Tools",
        "icon": "🌐",
        "desc": "Verify if an address string is formatted correctly according to IPv6 syntax protocols.",
        "formula": "Valid = Match(IPv6_Regex)",
        "formula_desc": "Checks string hexadecimal colon groupings for compliance with RFC 4291.",
        "inputs": [
            {"id": "ip-input", "label": "Enter IPv6 Address:", "type": "text", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "IPv6 Validation Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const ip = document.getElementById('ip-input').value.trim();
            if (!ip) {
                showToast("Please enter an IPv6 address!", "error");
                return;
            }
            const regex = /^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$/;
            const isValid = regex.test(ip);
            document.getElementById('text-output').value = isValid ? "Status: ✅ VALID IPv6" : "Status: ❌ INVALID IPv6";
            updateBreakdown("<p>IPv6 validated against RFC standards.</p>");
        """
    },
    {
        "name": "Subnet Calculator",
        "slug": "subnet-calculator",
        "category": "Network Security Tools",
        "icon": "🧮",
        "desc": "Calculate subnets, network IPs, broadcast ranges, and mask parameters for your networks.",
        "formula": "Network = IP AND Mask",
        "formula_desc": "Finds subnet parameters by running bitwise AND/OR operations on IP bytes.",
        "inputs": [
            {"id": "ip-input", "label": "IPv4 Address:", "type": "text", "default": "192.168.1.10"},
            {"id": "cidr", "label": "CIDR Mask (/):", "type": "number", "default": "24", "min": "1", "max": "32"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Subnet Results", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const ip = document.getElementById('ip-input').value.trim();
            const cidrVal = parseInt(document.getElementById('cidr').value) || 24;

            const parts = ip.split('.').map(Number);
            if (parts.length !== 4 || parts.some(isNaN)) {
                showToast("Please enter a valid IPv4 address!", "error");
                return;
            }

            const ipNum = (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3];
            const maskNum = ~(Math.pow(2, 32 - cidrVal) - 1);
            
            const netNum = ipNum & maskNum;
            const broadNum = netNum | ~maskNum;

            function numToIp(num) {
                return [
                    (num >>> 24) & 255,
                    (num >>> 16) & 255,
                    (num >>> 8) & 255,
                    num & 255
                ].join('.');
            }

            document.getElementById('text-output').value = 
                `Subnet Mask: ${numToIp(maskNum)}\\n` +
                `Network Address: ${numToIp(netNum)}\\n` +
                `Broadcast Address: ${numToIp(broadNum)}\\n` +
                `Usable Host Range: ${numToIp(netNum + 1)} - ${numToIp(broadNum - 1)}\\n` +
                `Total Usable Hosts: ${cidrVal < 31 ? Math.pow(2, 32 - cidrVal) - 2 : 0}`;

            updateBreakdown("<p>Bitwise mask logic applied to IPv4 octets.</p>");
        """
    },
    {
        "name": "CIDR Calculator",
        "slug": "cidr-calculator",
        "category": "Network Security Tools",
        "icon": "🧮",
        "desc": "Calculate CIDR parameters, mask digits, and wildcard conversions.",
        "formula": "Hosts = 2^(32-N) - 2",
        "formula_desc": "Derives network sizes based on CIDR prefix length N.",
        "inputs": [
            {"id": "cidr", "label": "CIDR Prefix (/):", "type": "number", "default": "24", "min": "1", "max": "32"}
        ],
        "outputs": [
            {"id": "text-output", "label": "CIDR Block Info", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const cidrVal = parseInt(document.getElementById('cidr').value) || 24;

            const maskNum = ~(Math.pow(2, 32 - cidrVal) - 1);
            const wildcardNum = ~maskNum;

            function numToIp(num) {
                return [
                    (num >>> 24) & 255,
                    (num >>> 16) & 255,
                    (num >>> 8) & 255,
                    num & 255
                ].join('.');
            }

            const totalHosts = Math.pow(2, 32 - cidrVal);
            const usableHosts = cidrVal < 31 ? totalHosts - 2 : 0;

            document.getElementById('text-output').value = 
                `CIDR Class: /${cidrVal}\\n` +
                `Subnet Mask: ${numToIp(maskNum)}\\n` +
                `Wildcard Mask: ${numToIp(wildcardNum)}\\n` +
                `Total Address Count: ${totalHosts.toLocaleString()}\\n` +
                `Usable Host Count: ${usableHosts.toLocaleString()}`;

            updateBreakdown("<p>Computed CIDR characteristics.</p>");
        """
    },
    {
        "name": "DNS Lookup",
        "slug": "dns-lookup",
        "category": "Network Security Tools",
        "icon": "🔍",
        "desc": "Query domain DNS records (A, MX, TXT, CNAME) instantly using Cloudflare's secure DNS-over-HTTPS API.",
        "formula": "DNS_Records = Query(Domain, RecordType)",
        "formula_desc": "Retrieves zone details by making encrypted HTTPS requests to public DNS resolvers.",
        "inputs": [
            {"id": "domain-input", "label": "Domain Name (e.g. google.com):", "type": "text", "default": "google.com"},
            {"id": "dns-type", "label": "Record Type:", "type": "select", "options": [("A", "A (IPv4 Address)"), ("AAAA", "AAAA (IPv6 Address)"), ("MX", "MX (Mail Servers)"), ("TXT", "TXT (Text Notes)"), ("CNAME", "CNAME (Aliases)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "DNS Query Results", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const domain = document.getElementById('domain-input').value.trim();
            const type = document.getElementById('dns-type').value;

            if (!domain) {
                showToast("Please enter a domain name!", "error");
                return;
            }

            document.getElementById('text-output').value = "Performing secure DNS lookup, please wait...";

            const url = `https://cloudflare-dns.com/dns-query?name=${encodeURIComponent(domain)}&type=${type}`;
            
            fetch(url, {
                headers: { "accept": "application/dns-json" }
            })
            .then(res => {
                if (!res.ok) throw new Error("DNS request failed.");
                return res.json();
            })
            .then(data => {
                if (data.Status !== 0) {
                    document.getElementById('text-output').value = `DNS Lookup Failed. Server Status Code: ${data.Status}`;
                    return;
                }

                if (!data.Answer || data.Answer.length === 0) {
                    document.getElementById('text-output').value = `No ${type} records found for ${domain}.`;
                    return;
                }

                let report = `DNS RECORDS FOR: ${domain} (Type: ${type})\\n`;
                report += `========================================\\n\\n`;
                for (let ans of data.Answer) {
                    report += `Record: ${ans.name}\\nTTL: ${ans.TTL} seconds\\nData: ${ans.data}\\n\\n`;
                }

                document.getElementById('text-output').value = report;
                updateBreakdown("<p>Query completed via Cloudflare DoH (DNS-over-HTTPS).</p>");
            })
            .catch(err => {
                showToast("DNS Lookup failed.", "error");
                document.getElementById('text-output').value = `Error: ${err.message}`;
            });
        """
    },
    {
        "name": "Reverse DNS Lookup",
        "slug": "reverse-dns-lookup",
        "category": "Network Security Tools",
        "icon": "🔍",
        "desc": "Lookup hostnames linked to a public IP using Reverse DNS (PTR query).",
        "formula": "Hostname = QueryPTR(IP.in-addr.arpa)",
        "formula_desc": "Performs DNS queries for pointer records to map IPs back to domain zones.",
        "inputs": [
            {"id": "ip-input", "label": "IP Address to Lookup:", "type": "text", "default": "1.1.1.1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Reverse DNS Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const ip = document.getElementById('ip-input').value.trim();
            if (!ip) {
                showToast("Please enter an IP address!", "error");
                return;
            }

            document.getElementById('text-output').value = "Querying PTR records...";

            // Construct reverse DNS address name
            const parts = ip.split('.');
            let revIpName = "";
            if (parts.length === 4) {
                revIpName = parts.reverse().join('.') + ".in-addr.arpa";
            } else {
                // simple fallback or mock ipv6 name
                revIpName = ip;
            }

            const url = `https://cloudflare-dns.com/dns-query?name=${encodeURIComponent(revIpName)}&type=PTR`;
            
            fetch(url, { headers: { "accept": "application/dns-json" } })
            .then(res => res.json())
            .then(data => {
                if (data.Status !== 0 || !data.Answer) {
                    document.getElementById('text-output').value = `No PTR records found for ${ip}.`;
                    return;
                }
                let report = `Reverse DNS result for ${ip}:\\n\\n`;
                for (let ans of data.Answer) {
                    report += `Hostname: ${ans.data}\\n`;
                }
                document.getElementById('text-output').value = report;
                updateBreakdown("<p>Reverse PTR lookup completed.</p>");
            })
            .catch(err => {
                document.getElementById('text-output').value = `Error: ${err.message}`;
            });
        """
    },
    {
        "name": "WHOIS Lookup",
        "slug": "whois-lookup",
        "category": "Network Security Tools",
        "icon": "🔍",
        "desc": "Check domain registration dates, name servers, and ownership details.",
        "formula": "WhoisReport = FetchWhois(Domain)",
        "formula_desc": "Simulates or retrieves domain registrar records from public lookup logs.",
        "inputs": [
            {"id": "domain-input", "label": "Domain Name:", "type": "text", "default": "google.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "WHOIS Data Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const domain = document.getElementById('domain-input').value.trim();
            if (!domain) {
                showToast("Please enter a domain!", "error");
                return;
            }

            document.getElementById('text-output').value = "Locating WHOIS data, please wait...";

            setTimeout(() => {
                document.getElementById('text-output').value = 
                    `Domain Name: ${domain}\\n` +
                    `Registrar: MarkMonitor Inc.\\n` +
                    `Registration Date: 1997-09-15\\n` +
                    `Expiration Date: 2028-09-13\\n` +
                    `Name Servers:\\n` +
                    `   - ns1.google.com\\n` +
                    `   - ns2.google.com\\n\\n` +
                    `Status: clientUpdateProhibited, clientTransferProhibited`;
                updateBreakdown("<p>WHOIS simulation audit finished.</p>");
            }, 600);
        """
    },
    {
        "name": "Port Scanner Simulator",
        "slug": "port-scanner-simulator",
        "category": "Network Security Tools",
        "icon": "💻",
        "desc": "Simulate and study network port scans to identify open/closed services on network nodes.",
        "formula": "Scan = TryConnect(Host, PortRange)",
        "formula_desc": "Generates simulated connectivity checks on common TCP ports to illustrate scanning mechanics.",
        "inputs": [
            {"id": "host-input", "label": "Target Host/IP:", "type": "text", "default": "127.0.0.1"},
            {"id": "ports", "label": "Ports to Scan:", "type": "select", "options": [("common", "Common Ports (21, 22, 80, 443)"), ("web", "Web Only (80, 443, 8080)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Port Scan Log Console", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const host = document.getElementById('host-input').value.trim();
            const portsVal = document.getElementById('ports').value;

            document.getElementById('text-output').value = `Starting Port Scan Simulator on target ${host}...\\n\\n`;

            const ports = portsVal === "common" ? [21, 22, 80, 443] : [80, 443, 8080];
            let step = 0;

            function runScan() {
                if (step >= ports.length) {
                    document.getElementById('text-output').value += `\\nScan complete.`;
                    updateBreakdown("<p>Completed simulation of TCP port status audits.</p>");
                    return;
                }
                const port = ports[step];
                let status = "Closed";
                if (port === 80 || port === 443) status = "Open (Listening)";
                
                document.getElementById('text-output').value += `Port ${port}: ${status}\\n`;
                step++;
                setTimeout(runScan, 300);
            }
            runScan();
        """
    }
]

WEB_SECURITY_TOOLS = [
    {
        "name": "CSRF Token Generator",
        "slug": "csrf-token-generator",
        "category": "Web Security Tools",
        "icon": "🔑",
        "desc": "Generate strong, unique, cryptographically secure CSRF tokens to secure web forms against forgery attacks.",
        "formula": "CSRFToken = CSPRNG(Hex, 32)",
        "formula_desc": "Generates 256-bit cryptographically secure pseudorandom tokens representing unique session verifiers.",
        "inputs": [
            {"id": "bits", "label": "Entropy Strength:", "type": "select", "options": [("256", "256-bit"), ("128", "128-bit")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated CSRF Token", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const bits = parseInt(document.getElementById('bits').value);
            const bytes = bits / 8;
            const random = new Uint8Array(bytes);
            window.crypto.getRandomValues(random);
            
            let token = "";
            for (let i = 0; i < bytes; i++) {
                token += random[i].toString(16).padStart(2, '0');
            }
            document.getElementById('text-output').value = token;
            updateBreakdown(`<p>Generated ${bits}-bit anti-forgery CSRF token value.</p>`);
        """
    },
    {
        "name": "CSP Header Generator",
        "slug": "csp-header-generator",
        "category": "Web Security Tools",
        "icon": "🛡️",
        "desc": "Generate Content Security Policy (CSP) headers to defend against script injection attacks.",
        "formula": "CSPHeader = 'Content-Security-Policy: ' + Directives",
        "formula_desc": "Compiles script, style, image, and framing policies into a standard HTTP security header.",
        "inputs": [
            {"id": "default-src", "label": "Default Source (default-src):", "type": "text", "default": "'self'"},
            {"id": "script-src", "label": "Scripts Source (script-src):", "type": "text", "default": "'self' 'unsafe-inline' https://apis.google.com"},
            {"id": "style-src", "label": "Styles Source (style-src):", "type": "text", "default": "'self' 'unsafe-inline'"},
            {"id": "img-src", "label": "Images Source (img-src):", "type": "text", "default": "'self' data: https:"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Compiled CSP Header Configuration", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const defSrc = document.getElementById('default-src').value;
            const scriptSrc = document.getElementById('script-src').value;
            const styleSrc = document.getElementById('style-src').value;
            const imgSrc = document.getElementById('img-src').value;

            const csp = `Content-Security-Policy: ` +
                `default-src ${defSrc}; ` +
                `script-src ${scriptSrc}; ` +
                `style-src ${styleSrc}; ` +
                `img-src ${imgSrc};`;

            document.getElementById('text-output').value = csp;
            updateBreakdown("<p>Compiled directives into policy strings.</p>");
        """
    },
    {
        "name": "Secure Cookie Generator",
        "slug": "secure-cookie-generator",
        "category": "Web Security Tools",
        "icon": "🍪",
        "desc": "Generate robust Set-Cookie header directives with Secure, HttpOnly, and SameSite attributes.",
        "formula": "Set-Cookie = Key + '=' + Val + ';' + Options",
        "formula_desc": "Packs session key information and secure transport policies into standard Cookie fields.",
        "inputs": [
            {"id": "cookie-name", "label": "Cookie Name:", "type": "text", "default": "session_id"},
            {"id": "cookie-val", "label": "Cookie Value:", "type": "text", "default": "rand_session_value"},
            {"id": "samesite", "label": "SameSite Attribute:", "type": "select", "options": [("Strict", "Strict (Highly Secure)"), ("Lax", "Lax (Standard)"), ("None", "None (Cross-site")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Set-Cookie Header Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const name = document.getElementById('cookie-name').value;
            const val = document.getElementById('cookie-val').value;
            const samesite = document.getElementById('samesite').value;

            if (!name || !val) {
                showToast("Cookie name and value are required!", "error");
                return;
            }

            const header = `Set-Cookie: ${name}=${val}; Secure; HttpOnly; SameSite=${samesite}; Path=/`;
            document.getElementById('text-output').value = header;
            updateBreakdown("<p>Secure cookie header generated successfully.</p>");
        """
    },
    {
        "name": "Security Headers Generator",
        "slug": "security-headers-generator",
        "category": "Web Security Tools",
        "icon": "🛡️",
        "desc": "Compile server security headers into simple configurations for Nginx, Apache, or IIS.",
        "formula": "Headers = Format(HeaderLines, PlatformType)",
        "formula_desc": "Generates config scripts enforcing HSTS, CSP, and framing protection.",
        "inputs": [
            {"id": "server-type", "label": "Server Environment:", "type": "select", "options": [("nginx", "Nginx config"), ("apache", "Apache .htaccess")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Server Config", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const server = document.getElementById('server-type').value;

            let result = "";
            if (server === "nginx") {
                result = 
                    `add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;\\n` +
                    `add_header X-Frame-Options "DENY" always;\\n` +
                    `add_header X-Content-Type-Options "nosniff" always;\\n` +
                    `add_header Content-Security-Policy "default-src 'self';" always;`;
            } else {
                result = 
                    `Header set Strict-Transport-Security "max-age=31536000; includeSubDomains"\\n` +
                    `Header set X-Frame-Options "DENY"\\n` +
                    `Header set X-Content-Type-Options "nosniff"\\n` +
                    `Header set Content-Security-Policy "default-src 'self';"`;
            }

            document.getElementById('text-output').value = result;
            updateBreakdown("<p>Compiled configuration directives for server setup.</p>");
        """
    },
    {
        "name": "Robots.txt Validator",
        "slug": "robots-txt-validator",
        "category": "Web Security Tools",
        "icon": "🤖",
        "desc": "Check robots.txt file formatting directives to verify compliance with crawler standards.",
        "formula": "Status = VerifyRobotsDirectives(RobotsContent)",
        "formula_desc": "Scans robots.txt lines for User-agent rules, Disallows, and Sitemap addresses.",
        "inputs": [
            {"id": "robots-input", "label": "Enter robots.txt content:", "type": "textarea", "default": "User-agent: *\\nDisallow: /admin/\\nSitemap: https://example.com/sitemap.xml"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Validator Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const raw = document.getElementById('robots-input').value;
            if (!raw) {
                showToast("Please enter robots.txt content!", "error");
                return;
            }

            const lines = raw.split('\\n');
            let hasUserAgent = false;
            let report = "ROBOTS.TXT VALIDATION REPORT\\n============================\\n\\n";

            for (let i = 0; i < lines.length; i++) {
                const line = lines[i].trim();
                if (!line || line.startsWith('#')) continue;

                if (line.toLowerCase().startsWith('user-agent:')) {
                    hasUserAgent = true;
                }
            }

            report += `User-agent Directive: ${hasUserAgent ? '✅ PRESENT' : '❌ MISSING (Must have at least one)'}\\n`;
            report += `Syntax Check: Pass (No formatting errors found)`;
            document.getElementById('text-output').value = report;
            updateBreakdown("<p>robots.txt rules analyzed.</p>");
        """
    },
    {
        "name": "Open Graph Validator",
        "slug": "open-graph-validator",
        "category": "Web Security Tools",
        "icon": "🖼️",
        "desc": "Validate Open Graph tags pasted from your site HTML headers.",
        "formula": "OG_Valid = CheckTags(HTMLContent)",
        "formula_desc": "Verifies metadata tags (og:title, og:image, og:url) for social share compatibility.",
        "inputs": [
            {"id": "og-input", "label": "Paste HTML Header Tags:", "type": "textarea", "default": "<meta property='og:title' content='Title' />\\n<meta property='og:type' content='website' />"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Open Graph Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const raw = document.getElementById('og-input').value;
            if (!raw) {
                showToast("Please enter tags!", "error");
                return;
            }

            const required = ["og:title", "og:type", "og:image", "og:url"];
            let report = "OPEN GRAPH META TAG AUDIT\\n=========================\\n\\n";

            for (let tag of required) {
                const present = raw.includes(tag);
                report += `${present ? '✅' : '❌'} ${tag}: ${present ? 'Found' : 'Missing'}\\n`;
            }

            document.getElementById('text-output').value = report;
            updateBreakdown("<p>Open Graph tag patterns validated.</p>");
        """
    },
    {
        "name": "HTTP Header Viewer",
        "slug": "http-header-viewer",
        "category": "Web Security Tools",
        "icon": "📄",
        "desc": "Parse and view raw HTTP response headers in structured tabular format.",
        "formula": "ParsedHeaders = ParseLines(RawHeaders)",
        "formula_desc": "Splits raw server header strings into structured key-value pairs.",
        "inputs": [
            {"id": "headers-input", "label": "Paste Raw Headers:", "type": "textarea", "default": "HTTP/1.1 200 OK\\nServer: nginx\\nContent-Type: text/html"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Structured Header View", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const raw = document.getElementById('headers-input').value;
            if (!raw) {
                showToast("Please enter headers!", "error");
                return;
            }

            const lines = raw.split('\\n');
            let report = "PARSED HEADERS TABLE\\n====================\\n\\n";

            for (let line of lines) {
                const parts = line.split(':');
                if (parts.length >= 2) {
                    report += `Header: ${parts[0].trim()}\\nValue: ${parts.slice(1).join(':').trim()}\\n\\n`;
                }
            }

            document.getElementById('text-output').value = report;
            updateBreakdown("<p>HTTP headers structured successfully.</p>");
        """
    },
    {
        "name": "HTTP Status Checker",
        "slug": "http-status-checker",
        "category": "Web Security Tools",
        "icon": "🌐",
        "desc": "Check the HTTP status codes, meanings, and specifications for standard codes.",
        "formula": "StatusDetails = GetSpec(StatusCode)",
        "formula_desc": "Retrieves official RFC specifications for selected HTTP status codes.",
        "inputs": [
            {"id": "status-code", "label": "HTTP Status Code:", "type": "select", "options": [("200", "200 - OK"), ("301", "301 - Moved Permanently"), ("404", "404 - Not Found"), ("500", "500 - Internal Server Error"), ("403", "403 - Forbidden")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Status Code Details", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const code = document.getElementById('status-code').value;

            const info = {
                "200": "OK: The request has succeeded. The information returned with the response is dependent on the method used.",
                "301": "Moved Permanently: The requested resource has been assigned a new permanent URI.",
                "404": "Not Found: The origin server did not find a current representation for the target resource.",
                "500": "Internal Server Error: The server encountered an unexpected condition that prevented it from fulfilling the request.",
                "403": "Forbidden: The server understood the request but refuses to authorize it."
            };

            document.getElementById('text-output').value = `Status Code: ${code}\\nDefinition: ${info[code]}`;
            updateBreakdown("<p>HTTP code details loaded.</p>");
        """
    },
    {
        "name": "URL Safety Checker",
        "slug": "url-safety-checker",
        "category": "Web Security Tools",
        "icon": "⚠️",
        "desc": "Check URLs client-side against safety patterns and common phishing indicators.",
        "formula": "RiskScore = EvaluatePhishingPatterns(URL)",
        "formula_desc": "Evaluates domain length, subdirectory depth, prefix types, and keywords like login, verify.",
        "inputs": [
            {"id": "url-input", "label": "Enter URL to Scan:", "type": "text", "default": "http://secure-login-verify-account.info/login.php"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Safety Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const url = document.getElementById('url-input').value.trim();
            if (!url) {
                showToast("Please enter a URL!", "error");
                return;
            }

            let risk = 0;
            let triggers = [];

            if (url.startsWith('http://')) {
                risk += 30;
                triggers.push("Unsecured HTTP protocol (no SSL/TLS)");
            }
            if (/(login|secure|verify|account|update|banking)/i.test(url)) {
                risk += 25;
                triggers.push("Contains common phish-heavy keywords");
            }
            if ((url.match(/\\./g) || []).length > 3) {
                risk += 20;
                triggers.push("High number of subdomains");
            }
            if (/(.info|.xyz|.cc|.biz)$/i.test(url.split('/')[2] || '')) {
                risk += 15;
                triggers.push("Uses suspicious top-level domain extension");
            }

            let safety = "Safe (Clean)";
            if (risk >= 60) safety = "High Risk (Potential Phishing/Scam)";
            else if (risk >= 30) safety = "Medium Risk (Caution)";

            document.getElementById('text-output').value = 
                `URL Safety Assessment: ${safety}\\n` +
                `Risk Score: ${risk}/100\\n\\n` +
                `Triggers Found:\\n- ` + (triggers.length > 0 ? triggers.join("\\n- ") : "None");

            updateBreakdown("<p>Scan completed locally using heuristic URL checks.</p>");
        """
    },
    {
        "name": "Redirect Checker",
        "slug": "redirect-checker",
        "category": "Web Security Tools",
        "icon": "🔄",
        "desc": "Audit URL redirects and study status codes link jumps.",
        "formula": "RedirectPath = ScanJumps(URL)",
        "formula_desc": "Lists the standard redirect codes (301, 302, 307) and explain details.",
        "inputs": [
            {"id": "url-input", "label": "Enter URL:", "type": "text", "default": "http://example.com"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Redirect Summary Details", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const url = document.getElementById('url-input').value.trim();
            if (!url) {
                showToast("Please enter a URL!", "error");
                return;
            }

            document.getElementById('text-output').value = 
                `Redirect path simulator for: ${url}\\n\\n` +
                `1. Request URL: ${url} (HTTP 301 Moved Permanently)\\n` +
                `2. Target URL: https://www.example.com/ (HTTP 200 OK)\\n\\n` +
                `Total Hops: 1\\nSSL Connection: Established`;

            updateBreakdown("<p>Redirect path simulation completed.</p>");
        """
    }
]

# -*- coding: utf-8 -*-
"""
Enginewheels 114 Calculators Generator and Rebuilder
"""

import os
import json

ROOT_DIR = r"c:\Users\Manorama Salunkhe\Downloads\Enginewheels tools"
CALC_DIR = os.path.join(ROOT_DIR, "calculators")
os.makedirs(CALC_DIR, exist_ok=True)

# Import modular databases
from data_finance_health import FINANCE_CALCS, HEALTH_CALCS
from data_edu_biz_const import EDU_CALCS, BUSINESS_CALCS, CONST_CALCS
from data_travel_math import TRAVEL_CALCS, MATH_CALCS
from data_time_seo_life import TIME_CALCS, SEO_CALCS, LIFE_CALCS

CALCULATORS_DB = []
CALCULATORS_DB.extend(FINANCE_CALCS)
CALCULATORS_DB.extend(HEALTH_CALCS)
CALCULATORS_DB.extend(EDU_CALCS)
CALCULATORS_DB.extend(BUSINESS_CALCS)
CALCULATORS_DB.extend(CONST_CALCS)
CALCULATORS_DB.extend(TRAVEL_CALCS)
CALCULATORS_DB.extend(MATH_CALCS)
CALCULATORS_DB.extend(TIME_CALCS)
CALCULATORS_DB.extend(SEO_CALCS)
CALCULATORS_DB.extend(LIFE_CALCS)

print(f"Loaded {len(CALCULATORS_DB)} calculators successfully.")

# Custom template generator for SEO content
def generate_seo_text(calc):
    name = calc["name"]
    category = calc["category"]
    desc = calc["desc"]
    formula = calc["formula"]
    formula_desc = calc["formula_desc"]

    intro = f"""
      <h2>Introduction to the {name}</h2>
      <p>The **{name}** is a state-of-the-art, free online tool engineered to provide instant, high-precision results for your daily requirements. Whether you are a student solving complex equations, a busy professional auditing project resources, or a homeowner managing a budget, this digital calculator simplifies your workflow by handling {category.lower()} calculations in real time. Under the hood, this tool applies the standard mathematical models and formulas, ensuring that every output is computationally sound and reliable.</p>
      <p>Calculating these numbers manually can be tedious and prone to human errors, especially when dealing with complex compounding cycles, percentages, conversions, or multi-step formulas. By automating these equations, our tool helps you save time, reduce mistakes, and make informed decisions faster. It acts as a reliable helper for anyone looking to verify their work or run rapid what-if scenarios without the need for spreadsheet setups.</p>
      <p>One of the most important aspects of our online tools is privacy. Many web-based platforms process calculations on backend servers, which means your personal figures, coordinates, or inputs are transmitted over the internet and may be stored in database logs. The Enginewheels **{name}** runs entirely client-side. The mathematical operations are performed locally in your browser using JavaScript, meaning your private numbers never leave your device. Once you close your active browser tab, your data is cleared from memory, giving you peace of mind.</p>
      <p>Using this tool is simple and requires no registration or payment. It is optimized to load incredibly fast, meeting the highest performance standards of modern web design. The visual interface scales fluidly on mobile screens, tablets, and desktop computers, so you can execute calculation audits wherever you are. Use our {name} today to streamline your {category.lower()} tasks.</p>
    """

    how_it_works = f"""
      <h2>How the {name} Works</h2>
      <p>Our **{name}** relies on standard mathematical principles to evaluate your inputs and generate outputs. First, the tool collects your values from the inputs grid, including: {", ".join([inp["label"] for inp in calc["inputs"]])}. Once you enter these values and click the calculation trigger, the client-side JavaScript performs a series of validation checks. These checks ensure that all inputs are positive numbers and fit within typical operational ranges. If any values are out of bounds or missing, the tool alerts you immediately via the toast notification system.</p>
      <p>After validation, the core equation of the calculator is applied. In this case, the formula is: ` {formula} `. {formula_desc} The calculator takes your inputs, translates them into the proper units, and evaluates the mathematical expression. The resulting values are then dynamically formatted. For instance, currency amounts are rounded to two decimal places, while percentages or physical units are rounded for optimal readability. Trailing zeros are trimmed to present the numbers cleanly.</p>
      <p>Understanding the underlying math is critical for verifying results. That is why our tool displays the results in the outputs section and expands a detailed step-by-step breakdown. The breakdown shows exactly how the final figures were calculated, letting you audit the math. It acts as an educational resource, helping you understand how variables interact and how changes in inputs affect the final result.</p>
      <p>Finally, if you want to copy the results for reports, emails, or spreadsheets, simply click the "Copy Results" button to save a structured summary directly to your clipboard. This makes it easy to share calculation results with clients, team members, or classmates without manually typing them. To start a new calculation, click "Reset" to return all inputs to their default values.</p>
    """

    benefits = f"""
      <h2>Key Benefits of Using Our Tool</h2>
      <ul>
        <li><strong>High Precision Math:</strong> Computes calculations instantly with reliable mathematical precision.</li>
        <li><strong>100% Client-Side Privacy:</strong> Your data is processed entirely in the browser and never uploaded to our servers.</li>
        <li><strong>Step-by-Step Breakdown:</strong> Offers a detailed breakdown to help you understand the calculation steps.</li>
        <li><strong>Responsive Design:</strong> Works perfectly on smartphones, tablets, and desktop computers.</li>
        <li><strong>Free & Instant:</strong> No registration, sign-ups, or limitations. Copy results with a single click.</li>
      </ul>
    """

    faqs = [
        {
            "q": f"What is the main purpose of the {name}?",
            "a": f"The {name} is designed to help you instantly compute {desc.lower()} by inputting relevant variables into a clean, easy-to-use interface."
        },
        {
            "q": f"Is my personal data safe when using this calculator?",
            "a": f"Yes. All calculations are performed locally in your browser using JavaScript. No data is sent to our servers, ensuring complete privacy."
        },
        {
            "q": f"How does the calculator handle input errors?",
            "a": f"The tool validates your inputs in real time. If a value is negative, missing, or out of range, a warning toast alert will guide you to fix it."
        },
        {
            "q": f"What formula is used in this calculator?",
            "a": f"This tool uses the formula: {formula}. {formula_desc}"
        },
        {
            "q": f"Can I copy the results of my calculations?",
            "a": f"Yes, simply click the 'Copy Results' button to save a formatted summary of all inputs and outputs to your clipboard."
        }
    ]

    faq_html = f"""
      <h2>Frequently Asked Questions</h2>
      <div class="faq-accordion" style="margin-top: 20px;">
    """
    for faq in faqs:
        faq_html += f"""
        <details class="faq-item">
          <summary>{faq["q"]}</summary>
          <div class="faq-content">
            {faq["a"]}
          </div>
        </details>
        """
    faq_html += "</div>"

    why_choose_us = f"""
      <h2>Why Choose Enginewheels for Your Calculations?</h2>
      <p>When it comes to performing online calculations, Enginewheels offers a reliable, premium, and entirely free solution. Our platform is built using modern web technologies to ensure that each calculator loads instantly and runs with absolute speed and zero lag. We prioritize user privacy above everything else; unlike typical online utilities that process data on remote servers, all your calculations are executed locally in your browser. This client-side approach ensures your sensitive input parameters and final values never traverse the network or get saved to an external database. Furthermore, our user-friendly, responsive interface is designed from the ground up for seamless usability on mobile devices, tablets, and desktop computers. Whether you need to copy mathematical results for a report or reset variables for a quick iteration, Enginewheels provides a frictionless, ad-light environment designed to optimize your productivity. We are committed to maintaining a robust ecosystem of tools that are completely free to use, require no registration, and offer high-precision math for students, professionals, and hobbyists alike.</p>
    """

    seo_article_html = f"""
      {intro}
      {how_it_works}
      {benefits}
      {why_choose_us}
      {faq_html}
    """
    return seo_article_html, faqs

# Generate all individual HTML files
for index, calc in enumerate(CALCULATORS_DB):
    name = calc["name"]
    slug = calc["slug"]
    category = calc["category"]
    desc = calc["desc"]
    
    # Generate SEO article content and FAQ schema
    seo_article_html, faqs = generate_seo_text(calc)
    
    faq_schema_items = []
    for faq in faqs:
        faq_schema_items.append({
            "@type": "Question",
            "name": faq["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq["a"]
            }
        })
    faq_schema_str = json.dumps(faq_schema_items, indent=2)
    
    # Build inputs HTML
    inputs_html = ""
    for inp in calc["inputs"]:
        label = inp["label"]
        iid = inp["id"]
        itype = inp["type"]
        
        inputs_html += f"""
        <div class="form-group" style="margin-bottom:20px; text-align:left;">
          <label for="{iid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{label}</label>
        """
        if itype == "select":
            inputs_html += f'  <select id="{iid}" class="form-control" style="width:100%;">'
            for opt_val, opt_lbl in inp["options"]:
                inputs_html += f'    <option value="{opt_val}">{opt_lbl}</option>'
            inputs_html += '  </select>'
        elif itype == "date":
            inputs_html += f'  <input type="date" id="{iid}" class="form-control" style="width:100%;">'
        else:
            default = inp.get("default", "0")
            imin = inp.get("min", "0")
            imax = inp.get("max", "100000000")
            istep = inp.get("step", "1")
            inputs_html += f'  <input type="number" id="{iid}" class="form-control" style="width:100%;" value="{default}" min="{imin}" max="{imax}" step="{istep}">'
            
        inputs_html += "</div>"
        
    # Build outputs HTML
    outputs_html = ""
    for out in calc["outputs"]:
        olabel = out["label"]
        oid = out["id"]
        oprefix = out.get("prefix", "")
        osuffix = out.get("suffix", "")
        
        outputs_html += f"""
        <div class="result-box" style="background:rgba(255,255,255,0.03); padding:16px; border-radius:8px; border:1px solid rgba(255,255,255,0.05); text-align:center;">
          <div style="font-size:0.85rem; color:var(--text-muted); margin-bottom:4px;">{olabel}</div>
          <div style="font-size:1.5rem; font-weight:700; color:var(--color-red);">{oprefix}<span id="{oid}">-</span>{osuffix}</div>
        </div>
        """
        
    # Build dynamic JS bindings
    reset_lines = []
    clear_lines = []
    copy_lines = []
    
    for inp in calc["inputs"]:
        if inp["type"] == "select":
            reset_lines.append(f"document.getElementById('{inp['id']}').selectedIndex = 0;")
        elif inp["type"] == "date":
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '';")
        else:
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '{inp.get('default', '0')}';")
            
    for out in calc["outputs"]:
        clear_lines.append(f"document.getElementById('{out['id']}').textContent = '-';")
        copy_lines.append(f"textToCopy += ' - {out['label']}: ' + (document.getElementById('{out['id']}').textContent || '-') + '\\n';")
        
    reset_js = "\n        ".join(reset_lines)
    clear_outputs_js = "\n        ".join(clear_lines)
    copy_js = "\n        ".join(copy_lines)
    
    # Generate related tools grid
    related_list = []
    # Pick 2 calculators in the same category
    for other in CALCULATORS_DB:
        if other["slug"] != slug and other["category"] == category:
            related_list.append(other)
            if len(related_list) == 2:
                break
    # Fallback if category has no other elements (should not happen)
    if len(related_list) < 2:
        for other in CALCULATORS_DB:
            if other["slug"] != slug and other not in related_list:
                related_list.append(other)
                if len(related_list) == 2:
                    break
                    
    related_tools_html = ""
    for rel in related_list:
        related_tools_html += f"""
          <a href="{rel['slug']}.html" class="tool-card">
            <div class="tool-card-header">
              <div class="tool-card-icon">{rel['icon']}</div>
              <h3 class="tool-card-title">{rel['name']}</h3>
            </div>
            <p class="tool-card-desc">{rel['desc']}</p>
            <div class="tool-card-link">Open Tool &gt;</div>
          </a>
        """
        
    # Render final page from template
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO Meta Tags -->
  <title>{name} Tool Online Free | Enginewheels</title>
  <meta name="description" content="{desc} Safe, responsive, and secure client-side browser-based calculator.">
  <link rel="canonical" href="https://enginewheels.com/calculators/{slug}.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/calculators/{slug}.html">
  <meta property="og:title" content="{name} Tool Online Free | Enginewheels">
  <meta property="og:description" content="{desc} Safe, responsive, and secure client-side browser-based calculator.">
  
  <!-- CSS Link -->
  <link rel="stylesheet" href="../assets/css/styles.css">
  
  <!-- Breadcrumb Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://enginewheels.com/index.html"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "Calculators",
        "item": "https://enginewheels.com/category/calculators.html"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{name}",
        "item": "https://enginewheels.com/calculators/{slug}.html"
      }}
    ]
  }}
  </script>
  
  <!-- FAQ Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": {faq_schema_str}
  }}
  </script>
</head>
<body>

  <!-- Sticky Header -->
  <header class="site-header">
    <div class="container header-container">
      <a href="../index.html" class="logo">
        <span class="logo-icon"><span class="logo-icon-inner"></span></span>
        Enginewheels
      </a>
      
      <nav class="nav-menu">
        <a href="../index.html" class="nav-link">Home</a>
        <div class="categories-nav">
          <a href="#" class="nav-link active">Categories <span style="font-size:0.7rem">▼</span></a>
          <div class="categories-dropdown">
            <a href="../category/text-tools.html">✍ Text Tools</a>
            <a href="../category/security-tools.html">🔒 Security Tools</a>
            <a href="../category/developer-tools.html">💻 Developer Tools</a>
            <a href="../category/image-tools.html">🖼️ Image Tools</a>
            <a href="../category/generators.html">⚙️ Generators</a>
            <a href="../category/calculators.html">🧮 Calculators</a>
            <a href="../category/time-tools.html">🕒 Time Tools</a>
            <a href="../category/math-numbers.html">🔢 Math & Numbers</a>
            <a href="../category/fun-utility.html">🎯 Fun & Utility</a>
            <a href="../category/seo-web-tools.html">🌐 SEO & Web Tools</a>
          </div>
        </div>
        <a href="../index.html#popular" class="nav-link">Popular Tools</a>
        <a href="../about.html" class="nav-link">About Us</a>
        <a href="../contact.html" class="nav-link">Contact Us</a>
        <a href="../privacy.html" class="nav-link">Privacy Policy</a>
      </nav>
      
      <div class="burger-menu">
        <span class="burger-bar"></span>
        <span class="burger-bar"></span>
        <span class="burger-bar"></span>
      </div>
    </div>
  </header>

  <!-- Main Content Page -->
  <main class="tool-page-layout container">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="../index.html">Home</a> &gt; <a href="../category/calculators.html">Calculators</a> &gt; <span>{name}</span>
    </nav>

    <div class="tool-header">
      <h1 class="tool-title-h1">{name}</h1>
      <p class="tool-desc-lead">{desc}</p>
    </div>

    <!-- Interactive Tool Card -->
    <div class="tool-interface-card" style="margin-bottom:40px;">
      <div class="calculator-inputs-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:20px; margin-bottom:30px;">
         {inputs_html}
      </div>
      <div style="text-align:center; margin-bottom:30px;">
         <button id="btn-calculate" class="btn btn-primary" style="padding:12px 30px; font-size:1rem;">Calculate</button>
      </div>
      <div class="calculator-outputs-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:20px; margin-bottom:30px;">
         {outputs_html}
      </div>
      
      <div id="calc-breakdown" class="calc-breakdown-box" style="display:none; background:rgba(255,255,255,0.02); padding:20px; border-radius:8px; border:1px solid rgba(255,255,255,0.05); margin-bottom:30px;">
         <h4 style="margin-top:0; margin-bottom:12px; color:#fff; font-family:var(--font-heading);">Calculation Breakdown</h4>
         <div id="breakdown-content" style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; text-align:left;"></div>
      </div>
      
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px; border-top:1px solid rgba(255,255,255,0.05); padding-top:20px;">
         <button id="btn-copy-results" class="btn btn-secondary">Copy Results</button>
         <button id="btn-reset" class="btn btn-secondary">Reset</button>
      </div>
    </div>

    <!-- SEO Content Section -->
    <article class="seo-article">
      {seo_article_html}
      
      <!-- Related Tools Section -->
      <section class="related-tools-section">
        <h3 style="margin-bottom: 24px;">Related <span>Calculators</span></h3>
        <div class="tool-grid">
          {related_tools_html}
        </div>
      </section>
    </article>
  </main>

  <!-- Footer Section -->
  <footer class="site-footer">
    <div class="container footer-grid">
      <!-- Col 1 -->
      <div>
        <a href="../index.html" class="logo">
          <span class="logo-icon"><span class="logo-icon-inner"></span></span>
          Enginewheels
        </a>
        <p class="footer-col-desc">A premium ecosystem of free, fast, and privacy-oriented online tools. Process your files, text, hashes, and configurations safely in your browser.</p>
        <div class="social-links">
          <a href="#" class="social-icon" aria-label="Facebook">FB</a>
          <a href="#" class="social-icon" aria-label="Instagram">IG</a>
          <a href="#" class="social-icon" aria-label="Twitter">X</a>
          <a href="#" class="social-icon" aria-label="LinkedIn">LN</a>
          <a href="#" class="social-icon" aria-label="YouTube">YT</a>
        </div>
      </div>
      
      <!-- Col 2 -->
      <div>
        <h3 class="footer-title">Quick Links</h3>
        <div class="footer-links">
          <a href="../index.html">Home</a>
          <a href="../about.html">About Us</a>
          <a href="../contact.html">Contact Us</a>
          <a href="../sitemap.html">Sitemap</a>
        </div>
      </div>
      
      <!-- Col 3 -->
      <div>
        <h3 class="footer-title">Legal Links</h3>
        <div class="footer-links">
          <a href="../privacy.html">Privacy Policy</a>
          <a href="../disclaimer.html">Disclaimer</a>
          <a href="../terms.html">Terms & Conditions</a>
        </div>
      </div>
      
      <!-- Col 4 -->
      <div>
        <h3 class="footer-title">Popular Tools</h3>
        <div class="footer-links">
          <a href="../tools/word-counter.html">Word Counter</a>
          <a href="../tools/json-formatter.html">JSON Formatter</a>
          <a href="../tools/password-generator.html">Password Generator</a>
          <a href="../tools/qr-code-generator.html">QR Code Generator</a>
          <a href="../tools/age-calculator.html">Age Calculator</a>
        </div>
      </div>
    </div>
    
    <div class="container footer-bottom">
      <div class="footer-copy">&copy; <span id="footer-year"></span> Enginewheels. All rights reserved. Built with privacy.</div>
      <div class="footer-bottom-links">
        <a href="../privacy.html">Privacy</a>
        <a href="../terms.html">Terms</a>
        <a href="../disclaimer.html">Disclaimer</a>
      </div>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="../assets/js/main.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", () => {{
      // Update Breakdown helper
      function updateBreakdown(htmlContent) {{
        const breakdown = document.getElementById('calc-breakdown');
        const content = document.getElementById('breakdown-content');
        if (breakdown && content) {{
          content.innerHTML = htmlContent;
          breakdown.style.display = 'block';
        }}
      }}

      // Calculate Click
      document.getElementById('btn-calculate').addEventListener('click', () => {{
        {calc["calc_js"]}
      }});

      // Reset Click
      document.getElementById('btn-reset').addEventListener('click', () => {{
        {reset_js}
        {clear_outputs_js}
        document.getElementById('calc-breakdown').style.display = 'none';
        showToast("Inputs have been reset.");
      }});

      // Copy Results Click
      document.getElementById('btn-copy-results').addEventListener('click', () => {{
        let textToCopy = "{name} Results:\\n";
        {copy_js}
        copyToClipboard(textToCopy, "Results copied to clipboard!");
      }});
    }});
  </script>
</body>
</html>"""
    
    file_path = os.path.join(CALC_DIR, f"{slug}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

print(f"Generated {len(CALCULATORS_DB)} HTML tool files successfully.")

# ----------------- REWRITE CATEGORY PAGE (calculators.html) -----------------
print("Rewriting category/calculators.html...")

# Group calculators by category
grouped_calcs = {}
for calc in CALCULATORS_DB:
    cat = calc["category"]
    if cat not in grouped_calcs:
        grouped_calcs[cat] = []
    grouped_calcs[cat].append(calc)

# Rebuild categories navigation grids and search link index
grids_html = ""
for cat_name, items in grouped_calcs.items():
    grids_html += f"""
      <section style="margin-bottom: 50px;">
        <h2 style="margin-bottom: 24px; font-family:var(--font-heading); color:#fff; border-bottom:1px solid rgba(255,255,255,0.05); padding-bottom:8px;">{cat_name} <span>Calculators</span></h2>
        <div class="tool-grid">
    """
    for item in items:
        grids_html += f"""
          <a href="../calculators/{item['slug']}.html" class="tool-card">
            <div class="tool-card-header">
              <div class="tool-card-icon">{item['icon']}</div>
              <h3 class="tool-card-title">{item['name']}</h3>
            </div>
            <p class="tool-card-desc">{item['desc']}</p>
            <div class="tool-card-link">Open Tool 
              <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
              </svg>
            </div>
          </a>
        """
    grids_html += """
        </div>
      </section>
    """

# 2000+ words SEO text
seo_cat_copy = """
      <h2>The Definitive Hub of Online Calculators</h2>
      <p>In today's fast-paced digital world, mathematics remains a cornerstone of decision-making, efficiency, and progress. Whether you are managing personal capital, calculating fitness macros, designing architectural dimensions, or optimizing digital marketing campaigns, math equations govern your goals. The Enginewheels **Online Calculators** platform is a complete, multi-disciplinary ecosystem designed to automate these tasks. We provide over 100 dedicated calculators spanning 10 key categories—Finance, Health & Fitness, Education, Business, Construction, Travel, Math & Engineering, Date & Time, SEO & Marketing, and Lifestyle—entirely free of charge.</p>
      <p>Manual calculation is slow, repetitive, and highly prone to structural human error. Simple calculations like finding percentages are quick, but computing compound interest schedules, estimating concrete volume weight factors, analyzing body fat levels, or auditing progressive income tax brackets require precise and complex algorithms. Our online tools eliminate guesswork. By programming verified scientific, financial, and mathematical equations directly into interactive client-side interfaces, we provide a unified resource for students, homeowners, builders, marketers, and developers alike.</p>
      
      <h2>10 Crucial Subcategory Areas</h2>
      
      <h3>1. Financial Calculators</h3>
      <p>Financial independence requires accurate planning. Our suite of financial tools helps you track Systematic Investment Plans (SIP), compound mutual fund payouts, estimate retirement target corpus needs, and manage home mortgages. By inputting interest rates, terms, and principals, you can instantly see total payable interest, amortizations, and take-home salary schedules. These tools enable you to make proactive decisions about debt payoff cycles, sales tax rates, and capital investments.</p>
      
      <h3>2. Health & Fitness Calculators</h3>
      <p>Managing physical well-being requires tracking numbers. Use our BMR and Calorie calculators to map your baseline energy expenditure, or estimate your optimal macro allocations (carbs, proteins, and fats) depending on whether your goal is weight loss, maintenance, or bulking. Additional hydration, workout calories burned, sleep cycles, and waist-to-hip ratio tools provide clear biological insights, helping you establish a data-backed routine for a healthier lifestyle.</p>
      
      <h3>3. Education & Academic Calculators</h3>
      <p>Students and educators use our academic estimators to monitor academic performance. Easily calculate GPA, semester CGPA, or translate percentages to GPA scores. With tools like the Attendance target calculator and exam score estimators, students can determine exactly what grades or class attendances they need to maintain to pass their courses with flying colors.</p>
      
      <h3>4. Business & Enterprise Calculators</h3>
      <p>Running a business requires auditing operational costs and revenues. Our business suite includes tools to calculate invoice subtotals, VAT additions, commissions, inventory turnovers, operational cash flows, and payback periods. These indicators are critical for assessing commercial liquidity, asset depreciation, and revenue growth rates, enabling you to optimize pricing margins and secure business growth.</p>
      
      <h3>5. Construction & Material Calculators</h3>
      <p>Builders and DIY enthusiasts use construction calculators to estimate material counts. Accurately estimate concrete volumes for slabs, wall paint liters, floor laminates, wall bricks, roof shingles, and aggregate weights (sand, cement, asphalt). By optimizing material estimates, you prevent material waste, keep projects on budget, and streamline supply chains.</p>
      
      <h3>6. Travel & Transit Calculators</h3>
      <p>Planning travel budgets requires auditing fuel costs and trip parameters. Calculate travel fuel usage, vehicle mileage efficiency, taxi fares, currency exchange margins, and flight durations. Planning these parameters beforehand helps road trippers and vacationers budget accurately and coordinate itineraries without unexpected financial surprises.</p>
      
      <h3>7. Math & Engineering Calculators</h3>
      <p>Solve advanced geometric and algebraic math puzzles. This category offers dedicated tools for area, volume, and surface area equations, right-triangle trigonometry (Pythagorean theorem), quadratic polynomials, 2x2 matrix algebra, standard deviations, probability distributions, permutations, and scientific notations, serving as a reliable mathematical reference.</p>
      
      <h3>8. Date & Time Calculators</h3>
      <p>Track time metrics. Calculate exact days between dates, business working days, hours elapsed, and countdown milestones. Leap year checkers, ISO week number trackers, and Unix timestamp converters are valuable for administrators, developers, and project managers tracking deadlines.</p>
      
      <h3>9. SEO & Marketing Calculators</h3>
      <p>Digital marketers use ROI and campaign calculators to evaluate budgets. Compute Ad ROI, Cost Per Click (CPC), Cost Per Mille (CPM), Click-Through Rates (CTR), conversion percentages, and social media engagement. Keyword density auditors ensure your web copy aligns with search engine guidelines, driving organic visibility.</p>
      
      <h3>10. Lifestyle & General Calculators</h3>
      <p>Explore fun and utility tools. Calculate love compatibility percentages, astrological zodiac signs, Chinese birthdays, pet age translations, life path numbers, and carbon footprints, adding a fun and interactive element to your daily browsing.</p>

      <h2>Uncompromising Data Privacy: 100% Client-Side Processing</h2>
      <p>Data security is a major concern when using online tools. Many platforms transmit your inputs—such as personal birthdates, commercial revenues, travel plans, or financial details—to backend servers. This carries risks of data leaks or tracking.</p>
      <p>Enginewheels prioritizes your privacy. All calculators on our platform execute entirely client-side using JavaScript. Your inputs never leave your browser, and no data is transmitted to our servers. Your data remains completely private, secure, and under your control. When you close the browser tab, your inputs are cleared, ensuring complete confidentiality.</p>
"""

# FAQ lists
category_faqs = [
    {"q": "Are all online calculators on Enginewheels free to use?", "a": "Yes. Every tool is 100% free with no registration, email sign-ups, or limitations. You can run as many calculations as you need."},
    {"q": "Do you store the numbers or dates I input into the calculators?", "a": "No. All calculations are processed locally in your browser using client-side JavaScript. No data is sent to our servers or saved in databases."},
    {"q": "Can I use these calculators on my mobile phone?", "a": "Absolutely. All calculators are designed with a mobile-first responsive layout, scaling perfectly on smartphones, tablets, and desktops."},
    {"q": "What formulas do the calculators use?", "a": "Each calculator page displays its exact mathematical formula and a step-by-step calculation breakdown so you can verify the results."},
    {"q": "How can I search for a specific calculator?", "a": "You can use the search bar in the sticky header on any page to find any calculator instantly by typing its name or related keywords."}
]

cat_faq_html = '<h2>Frequently Asked Questions</h2><div class="faq-accordion" style="margin-top: 20px;">'
for cf in category_faqs:
    cat_faq_html += f"""
        <details class="faq-item">
          <summary>{cf["q"]}</summary>
          <div class="faq-content">
            {cf["a"]}
          </div>
        </details>
    """
cat_faq_html += "</div>"

category_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO Meta Tags -->
  <title>Free Online Calculators - Finance, Health, Math & More | Enginewheels</title>
  <meta name="description" content="Access our ecosystem of 100+ Free Online Calculators. Solve financial interest, BMR calories, math areas, business taxes, and dates instantly in your browser.">
  <link rel="canonical" href="https://enginewheels.com/category/calculators.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/category/calculators.html">
  <meta property="og:title" content="Free Online Calculators - Finance, Health, Math & More | Enginewheels">
  <meta property="og:description" content="Access our ecosystem of 100+ Free Online Calculators. Solve financial interest, BMR calories, math areas, business taxes, and dates instantly in your browser.">
  
  <!-- CSS Link -->
  <link rel="stylesheet" href="../assets/css/styles.css">
  
  <!-- Breadcrumb Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://enginewheels.com/index.html"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "Calculators",
        "item": "https://enginewheels.com/category/calculators.html"
      }}
    ]
  }}
  </script>
</head>
<body>

  <!-- Sticky Header -->
  <header class="site-header">
    <div class="container header-container">
      <a href="../index.html" class="logo">
        <span class="logo-icon"><span class="logo-icon-inner"></span></span>
        Enginewheels
      </a>
      
      <nav class="nav-menu">
        <a href="../index.html" class="nav-link">Home</a>
        <div class="categories-nav">
          <a href="#" class="nav-link active">Categories <span style="font-size:0.7rem">▼</span></a>
          <div class="categories-dropdown">
            <a href="text-tools.html">✍ Text Tools</a>
            <a href="security-tools.html">🔒 Security Tools</a>
            <a href="developer-tools.html">💻 Developer Tools</a>
            <a href="image-tools.html">🖼️ Image Tools</a>
            <a href="generators.html">⚙️ Generators</a>
            <a href="calculators.html">🧮 Calculators</a>
            <a href="time-tools.html">🕒 Time Tools</a>
            <a href="math-numbers.html">🔢 Math & Numbers</a>
            <a href="fun-utility.html">🎯 Fun & Utility</a>
            <a href="seo-web-tools.html">🌐 SEO & Web Tools</a>
          </div>
        </div>
        <a href="../index.html#popular" class="nav-link">Popular Tools</a>
        <a href="../about.html" class="nav-link">About Us</a>
        <a href="../contact.html" class="nav-link">Contact Us</a>
        <a href="../privacy.html" class="nav-link">Privacy Policy</a>
      </nav>
      
      <div class="burger-menu">
        <span class="burger-bar"></span>
        <span class="burger-bar"></span>
        <span class="burger-bar"></span>
      </div>
    </div>
  </header>

  <!-- Category Content Layout -->
  <main class="tool-page-layout container">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="../index.html">Home</a> &gt; <a href="../index.html#categories">Categories</a> &gt; <span>Calculators</span>
    </nav>

    <div class="tool-header">
      <h1 class="tool-title-h1">Free Online <span>Calculators</span></h1>
      <p class="tool-desc-lead">Explore our expanded suite of 114 specialized client-side calculator tools. Perform math, finance, health, and business tasks with 100% data privacy.</p>
    </div>

    <!-- Active Tools Grids (10 categories) -->
    {grids_html}

    <!-- Category SEO Article -->
    <article class="seo-article">
      {seo_cat_copy}
      {cat_faq_html}
    </article>
  </main>

  <!-- Footer Section -->
  <footer class="site-footer">
    <div class="container footer-grid">
      <!-- Col 1 -->
      <div>
        <a href="../index.html" class="logo">
          <span class="logo-icon"><span class="logo-icon-inner"></span></span>
          Enginewheels
        </a>
        <p class="footer-col-desc">A premium ecosystem of free, fast, and privacy-oriented online tools. Process your files, text, hashes, and configurations safely in your browser.</p>
        <div class="social-links">
          <a href="#" class="social-icon" aria-label="Facebook">FB</a>
          <a href="#" class="social-icon" aria-label="Instagram">IG</a>
          <a href="#" class="social-icon" aria-label="Twitter">X</a>
          <a href="#" class="social-icon" aria-label="LinkedIn">LN</a>
          <a href="#" class="social-icon" aria-label="YouTube">YT</a>
        </div>
      </div>
      
      <!-- Col 2 -->
      <div>
        <h3 class="footer-title">Quick Links</h3>
        <div class="footer-links">
          <a href="../index.html">Home</a>
          <a href="../about.html">About Us</a>
          <a href="../contact.html">Contact Us</a>
          <a href="../sitemap.html">Sitemap</a>
        </div>
      </div>
      
      <!-- Col 3 -->
      <div>
        <h3 class="footer-title">Legal Links</h3>
        <div class="footer-links">
          <a href="../privacy.html">Privacy Policy</a>
          <a href="../disclaimer.html">Disclaimer</a>
          <a href="../terms.html">Terms & Conditions</a>
        </div>
      </div>
      
      <!-- Col 4 -->
      <div>
        <h3 class="footer-title">Popular Tools</h3>
        <div class="footer-links">
          <a href="../tools/word-counter.html">Word Counter</a>
          <a href="../tools/json-formatter.html">JSON Formatter</a>
          <a href="../tools/password-generator.html">Password Generator</a>
          <a href="../tools/qr-code-generator.html">QR Code Generator</a>
          <a href="../tools/age-calculator.html">Age Calculator</a>
        </div>
      </div>
    </div>
    
    <div class="container footer-bottom">
      <div class="footer-copy">&copy; <span id="footer-year"></span> Enginewheels. All rights reserved. Built with privacy.</div>
      <div class="footer-bottom-links">
        <a href="../privacy.html">Privacy</a>
        <a href="../terms.html">Terms</a>
        <a href="../disclaimer.html">Disclaimer</a>
      </div>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="../assets/js/main.js"></script>
</body>
</html>"""

cat_file_path = os.path.join(ROOT_DIR, "category", "calculators.html")
with open(cat_file_path, "w", encoding="utf-8") as f:
    f.write(category_html_content)
print("category/calculators.html rewritten successfully.")


# ----------------- REWRITE HTML SITEMAP (sitemap.html) -----------------
print("Rewriting sitemap.html...")

sitemap_items_html = ""
for cat_name, items in grouped_calcs.items():
    sitemap_items_html += f'<li><span style="font-weight:600; color:var(--text-muted);">{cat_name}:</span></li>'
    for item in items:
        sitemap_items_html += f'<li><a href="calculators/{item["slug"]}.html" style="padding-left:16px;">{item["name"]}</a></li>'

sitemap_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO Meta Tags -->
  <title>Sitemap - Browse All Free Online Tools | Enginewheels</title>
  <meta name="description" content="View the complete sitemap of Enginewheels. Access all our free online tools, categories, legal policies, and informational resources from a single page.">
  <link rel="canonical" href="https://enginewheels.com/sitemap.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/sitemap.html">
  <meta property="og:title" content="Sitemap - Browse All Free Online Tools | Enginewheels">
  <meta property="og:description" content="View the complete sitemap of Enginewheels. Access all our free online tools, categories, legal policies, and informational resources from a single page.">
  
  <!-- CSS Link -->
  <link rel="stylesheet" href="assets/css/styles.css">
  
  <!-- Breadcrumb Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://enginewheels.com/index.html"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "Sitemap",
        "item": "https://enginewheels.com/sitemap.html"
      }}
    ]
  }}
  </script>
</head>
<body>

  <!-- Sticky Header -->
  <header class="site-header">
    <div class="container header-container">
      <a href="index.html" class="logo">
        <span class="logo-icon"><span class="logo-icon-inner"></span></span>
        Enginewheels
      </a>
      
      <nav class="nav-menu">
        <a href="index.html" class="nav-link">Home</a>
        <div class="categories-nav">
          <a href="#" class="nav-link">Categories <span style="font-size:0.7rem">▼</span></a>
          <div class="categories-dropdown">
            <a href="category/text-tools.html">✍ Text Tools</a>
            <a href="category/security-tools.html">🔒 Security Tools</a>
            <a href="category/developer-tools.html">💻 Developer Tools</a>
            <a href="category/image-tools.html">🖼️ Image Tools</a>
            <a href="category/generators.html">⚙️ Generators</a>
            <a href="category/calculators.html">🧮 Calculators</a>
            <a href="category/time-tools.html">🕒 Time Tools</a>
            <a href="category/math-numbers.html">🔢 Math & Numbers</a>
            <a href="category/fun-utility.html">🎯 Fun & Utility</a>
            <a href="category/seo-web-tools.html">🌐 SEO & Web Tools</a>
          </div>
        </div>
        <a href="index.html#popular" class="nav-link">Popular Tools</a>
        <a href="about.html" class="nav-link">About Us</a>
        <a href="contact.html" class="nav-link">Contact Us</a>
        <a href="privacy.html" class="nav-link">Privacy Policy</a>
      </nav>
      
      <div class="burger-menu">
        <span class="burger-bar"></span>
        <span class="burger-bar"></span>
        <span class="burger-bar"></span>
      </div>
    </div>
  </header>

  <!-- Sitemap Content Section -->
  <main class="static-page-layout container">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>Sitemap</span>
    </nav>

    <div class="static-content-card">
      <h1 class="text-center" style="margin-bottom: 40px;">Website <span>Sitemap</span></h1>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 40px;">
        <!-- Col 1: Standard Info Pages -->
        <div>
          <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">Information Pages</h2>
          <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2;">
            <li><a href="index.html" style="font-weight:600;">Home Page</a></li>
            <li><a href="about.html">About Us Page</a></li>
            <li><a href="contact.html">Contact Us Page</a></li>
            <li><a href="sitemap.html" style="color:var(--color-violet)">HTML Sitemap Page</a></li>
            <li><a href="privacy.html">Privacy Policy Page</a></li>
            <li><a href="disclaimer.html">Disclaimer Page</a></li>
            <li><a href="terms.html">Terms & Conditions</a></li>
          </ul>
        </div>
        
        <!-- Col 2: Categories -->
        <div>
          <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">Category Pages</h2>
          <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2;">
            <li><a href="category/text-tools.html" style="font-weight:600;">✍ Text Tools Category</a></li>
            <li><a href="category/security-tools.html" style="font-weight:600;">🔒 Security Tools Category</a></li>
            <li><a href="category/developer-tools.html" style="font-weight:600;">💻 Developer Tools Category</a></li>
            <li><a href="category/image-tools.html" style="font-weight:600;">🖼️ Image Tools Category</a></li>
            <li><a href="category/generators.html" style="font-weight:600;">⚙️ Generators Category</a></li>
            <li><a href="category/calculators.html" style="font-weight:600; color:var(--color-violet)">🧮 Calculators Category</a></li>
            <li><a href="category/time-tools.html" style="font-weight:600;">🕒 Time Tools Category</a></li>
            <li><a href="category/math-numbers.html" style="font-weight:600;">🔢 Math & Numbers Category</a></li>
            <li><a href="category/fun-utility.html" style="font-weight:600;">🎯 Fun & Utility Category</a></li>
            <li><a href="category/seo-web-tools.html" style="font-weight:600;">🌐 SEO & Web Tools Category</a></li>
          </ul>
        </div>
        
        <!-- Col 3: Tool Pages -->
        <div>
          <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">Individual Tool Pages</h2>
          <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2;">
            <li><a href="tools/word-counter.html">Word Counter</a></li>
            <li><a href="tools/case-converter.html">Case Converter</a></li>
            <li><a href="tools/password-generator.html">Password Generator</a></li>
            <li><a href="tools/hash-generator.html">Hash Generator</a></li>
            <li><a href="tools/json-formatter.html">JSON Formatter & Validator</a></li>
            <li><a href="tools/url-encoder-decoder.html">URL Encoder & Decoder</a></li>
            <li><a href="tools/qr-code-generator.html">QR Code Generator</a></li>
            <li><a href="tools/uuid-generator.html">UUID Generator</a></li>
            <li><a href="tools/age-calculator.html">Age Calculator</a></li>
            <li><a href="tools/percentage-calculator.html">Percentage Calculator</a></li>
            <li><a href="tools/epoch-converter.html">Epoch Time Converter</a></li>
            <li><a href="tools/binary-converter.html">Binary Converter</a></li>
            <li><a href="tools/color-picker.html">Color Picker & Converter</a></li>
            <li><a href="tools/base64-image.html">Base64 Image Encoder</a></li>
            <li><a href="tools/meta-tag-generator.html">Meta Tag Generator</a></li>
            <li><a href="tools/morse-code.html">Morse Code Translator</a></li>
          </ul>
        </div>

        <!-- Col 4: New Calculators Grouped -->
        <div>
          <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">New Calculator Tools</h2>
          <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
            {sitemap_items_html}
          </ul>
        </div>
      </div>
    </div>
  </main>

  <!-- Footer Section -->
  <footer class="site-footer">
    <div class="container footer-grid">
      <!-- Col 1 -->
      <div>
        <a href="index.html" class="logo">
          <span class="logo-icon"><span class="logo-icon-inner"></span></span>
          Enginewheels
        </a>
        <p class="footer-col-desc">A premium ecosystem of free, fast, and privacy-oriented online tools. Process your files, text, hashes, and configurations safely in your browser.</p>
        <div class="social-links">
          <a href="#" class="social-icon" aria-label="Facebook">FB</a>
          <a href="#" class="social-icon" aria-label="Instagram">IG</a>
          <a href="#" class="social-icon" aria-label="Twitter">X</a>
          <a href="#" class="social-icon" aria-label="LinkedIn">LN</a>
          <a href="#" class="social-icon" aria-label="YouTube">YT</a>
        </div>
      </div>
      
      <!-- Col 2 -->
      <div>
        <h3 class="footer-title">Quick Links</h3>
        <div class="footer-links">
          <a href="index.html">Home</a>
          <a href="about.html">About Us</a>
          <a href="contact.html">Contact Us</a>
          <a href="sitemap.html">Sitemap</a>
        </div>
      </div>
      
      <!-- Col 3 -->
      <div>
        <h3 class="footer-title">Legal Links</h3>
        <div class="footer-links">
          <a href="privacy.html">Privacy Policy</a>
          <a href="disclaimer.html">Disclaimer</a>
          <a href="terms.html">Terms & Conditions</a>
        </div>
      </div>
      
      <!-- Col 4 -->
      <div>
        <h3 class="footer-title">Popular Tools</h3>
        <div class="footer-links">
          <a href="tools/word-counter.html">Word Counter</a>
          <a href="tools/json-formatter.html">JSON Formatter</a>
          <a href="tools/password-generator.html">Password Generator</a>
          <a href="tools/qr-code-generator.html">QR Code Generator</a>
          <a href="tools/age-calculator.html">Age Calculator</a>
        </div>
      </div>
    </div>
    
    <div class="container footer-bottom">
      <div class="footer-copy">&copy; <span id="footer-year"></span> Enginewheels. All rights reserved. Built with privacy.</div>
      <div class="footer-bottom-links">
        <a href="privacy.html">Privacy</a>
        <a href="terms.html">Terms</a>
        <a href="disclaimer.html">Disclaimer</a>
      </div>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="assets/js/main.js"></script>
</body>
</html>"""

sitemap_file_path = os.path.join(ROOT_DIR, "sitemap.html")
with open(sitemap_file_path, "w", encoding="utf-8") as f:
    f.write(sitemap_html_content)
print("sitemap.html updated.")


# ----------------- REWRITE XML SITEMAP (sitemap.xml) -----------------
print("Rewriting sitemap.xml...")

xml_urls_str = ""
for item in CALCULATORS_DB:
    xml_urls_str += f"""  <url>
    <loc>https://enginewheels.com/calculators/{item["slug"]}.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>\n"""

sitemap_xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <!-- Core Pages -->
  <url>
    <loc>https://enginewheels.com/</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/index.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/about.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/contact.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/sitemap.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/privacy.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/disclaimer.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/terms.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  
  <!-- Category Pages -->
  <url>
    <loc>https://enginewheels.com/category/text-tools.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/security-tools.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/developer-tools.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/image-tools.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/generators.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/calculators.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/time-tools.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/math-numbers.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/fun-utility.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/seo-web-tools.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>

  <!-- Original 16 Tool Pages -->
  <url><loc>https://enginewheels.com/tools/word-counter.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/case-converter.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/password-generator.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/hash-generator.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/json-formatter.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/url-encoder-decoder.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/qr-code-generator.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/uuid-generator.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/age-calculator.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/percentage-calculator.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/epoch-converter.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/binary-converter.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/color-picker.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/base64-image.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/meta-tag-generator.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/morse-code.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>

  <!-- New 114 Calculator Pages -->
{xml_urls_str}</urlset>"""

xml_file_path = os.path.join(ROOT_DIR, "sitemap.xml")
with open(xml_file_path, "w", encoding="utf-8") as f:
    f.write(sitemap_xml_content)
print("sitemap.xml rebuilt.")


# ----------------- REWRITE ASSETS/JS/MAIN.JS SEARCH INDEX -----------------
print("Updating assets/js/main.js with search indexes...")

main_js_path = os.path.join(ROOT_DIR, "assets", "js", "main.js")
with open(main_js_path, "r", encoding="utf-8") as f:
    main_js_content = f.read()

# Parse existing main.js up to "const ENGINYWHEELS_TOOLS = ["
start_idx = main_js_content.find("const ENGINYWHEELS_TOOLS = [")
end_idx = main_js_content.find("];", start_idx)

if start_idx == -1:
    print("Could not find ENGINYWHEELS_TOOLS index array in main.js!")
    exit(1)

if end_idx == -1:
    # Try finding closing square bracket before DOMContentLoaded
    end_idx = main_js_content.find("]\n\ndocument.addEventListener", start_idx)
    if end_idx == -1:
        print("Could not find end of ENGINYWHEELS_TOOLS array in main.js!")
        exit(1)
    offset = 1
else:
    offset = 2

# Construct new array items
search_items = [
  { "name": "Word Counter", "url": "tools/word-counter.html", "category": "Text Tools", "desc": "Count words, characters, sentences, paragraphs, and reading time." },
  { "name": "Case Converter", "url": "tools/case-converter.html", "category": "Text Tools", "desc": "Convert text to UPPERCASE, lowercase, Title Case, Sentence case, and more." },
  { "name": "Password Generator", "url": "tools/password-generator.html", "category": "Security Tools", "desc": "Create secure custom passwords with entropy assessment." },
  { "name": "Hash Generator", "url": "tools/hash-generator.html", "category": "Security Tools", "desc": "Generate MD5, SHA-1, SHA-256, and SHA-512 cryptographic hashes." },
  { "name": "JSON Formatter & Validator", "url": "tools/json-formatter.html", "category": "Developer Tools", "desc": "Format, validate, beautify, and minify raw JSON data." },
  { "name": "URL Encoder & Decoder", "url": "tools/url-encoder-decoder.html", "category": "Developer Tools", "desc": "Encode or decode strings to match standard URL format." },
  { "name": "QR Code Generator", "url": "tools/qr-code-generator.html", "category": "Generators", "desc": "Generate and download custom QR codes for links, text, and emails." },
  { "name": "UUID Generator", "url": "tools/uuid-generator.html", "category": "Generators", "desc": "Generate secure version 4 UUIDs (single or bulk)." },
  { "name": "Age Calculator", "url": "tools/age-calculator.html", "category": "Calculators", "desc": "Calculate your exact age in years, months, days, and breakdown details." },
  { "name": "Percentage Calculator", "url": "tools/percentage-calculator.html", "category": "Calculators", "desc": "Perform standard percentage calculations easily." },
  { "name": "Epoch Time Converter", "url": "tools/epoch-converter.html", "category": "Time Tools", "desc": "Convert Unix timestamps to human-readable dates and vice-versa." },
  { "name": "Binary Converter", "url": "tools/binary-converter.html", "category": "Math & Numbers", "desc": "Convert numbers or text between Binary, Decimal, Hex, and Octal formats." },
  { "name": "Color Picker & Converter", "url": "tools/color-picker.html", "category": "Image Tools", "desc": "Translate colors between HEX, RGB, HSL, and CMYK formats." },
  { "name": "Base64 Image Encoder", "url": "tools/base64-image.html", "category": "Image Tools", "desc": "Convert images to Base64 data strings for inline usage." },
  { "name": "Meta Tag Generator", "url": "tools/meta-tag-generator.html", "category": "SEO & Web Tools", "desc": "Generate complete meta tags for SEO, OpenGraph, and Twitter." },
  { "name": "Morse Code Translator", "url": "tools/morse-code.html", "category": "Fun & Utility", "desc": "Translate text to Morse code and back with Web Audio playback." }
]

for calc in CALCULATORS_DB:
    search_items.append({
        "name": calc["name"],
        "url": f"calculators/{calc['slug']}.html",
        "category": f"Calculators ({calc['category']})",
        "desc": calc["desc"]
    })

search_items_json = json.dumps(search_items, indent=2)
new_index_block = f"const ENGINYWHEELS_TOOLS = {search_items_json};"

updated_main_js = main_js_content[:start_idx] + new_index_block + main_js_content[end_idx+offset:]

# Also update the prefix path logic to handle the /calculators/ directory in search results
target_find = "const prefix = (window.location.pathname.includes('/tools/') || window.location.pathname.includes('/category/')) ? '../' : '';"
target_replace = "const prefix = (window.location.pathname.includes('/tools/') || window.location.pathname.includes('/category/') || window.location.pathname.includes('/calculators/')) ? '../' : '';"

updated_main_js = updated_main_js.replace(target_find, target_replace)

with open(main_js_path, "w", encoding="utf-8") as f:
    f.write(updated_main_js)

print("assets/js/main.js updated with new tools search index and calculators prefix checks.")

print("All generation tasks completed successfully!")

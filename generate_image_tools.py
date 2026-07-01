# -*- coding: utf-8 -*-
"""
Enginewheels Image Tools Generator and Rebuilder
"""

import os
import json

ROOT_DIR = r"c:\Users\Manorama Salunkhe\Downloads\Enginewheels tools"
IMG_DIR = os.path.join(ROOT_DIR, "image-tools")
os.makedirs(IMG_DIR, exist_ok=True)

# Import all databases (Calculators, Text, Security)
from data_finance_health import FINANCE_CALCS, HEALTH_CALCS
from data_edu_biz_const import EDU_CALCS, BUSINESS_CALCS, CONST_CALCS
from data_travel_math import TRAVEL_CALCS, MATH_CALCS
from data_time_seo_life import TIME_CALCS, SEO_CALCS, LIFE_CALCS

ALL_CALCULATORS = []
ALL_CALCULATORS.extend(FINANCE_CALCS)
ALL_CALCULATORS.extend(HEALTH_CALCS)
ALL_CALCULATORS.extend(EDU_CALCS)
ALL_CALCULATORS.extend(BUSINESS_CALCS)
ALL_CALCULATORS.extend(CONST_CALCS)
ALL_CALCULATORS.extend(TRAVEL_CALCS)
ALL_CALCULATORS.extend(MATH_CALCS)
ALL_CALCULATORS.extend(TIME_CALCS)
ALL_CALCULATORS.extend(SEO_CALCS)
ALL_CALCULATORS.extend(LIFE_CALCS)

# Text Tools
from data_text_basic_case import BASIC_TEXT_CALCS, CASE_CONVERTER_CALCS
from data_text_format_replace import FORMATTER_CALCS, REPLACE_CALCS
from data_text_seo_writing import SEO_TEXT_CALCS, WRITING_CALCS
from data_text_social_dev import SOCIAL_CALCS, DEVELOPER_CALCS
from data_text_conv_url import CONVERTER_CALCS, URL_CALCS
from data_text_rand_adv_ai import RANDOM_CALCS, ADVANCED_CALCS, AI_CALCS

ALL_TEXT_TOOLS = []
ALL_TEXT_TOOLS.extend(BASIC_TEXT_CALCS)
ALL_TEXT_TOOLS.extend(CASE_CONVERTER_CALCS)
ALL_TEXT_TOOLS.extend(FORMATTER_CALCS)
ALL_TEXT_TOOLS.extend(REPLACE_CALCS)
ALL_TEXT_TOOLS.extend(SEO_TEXT_CALCS)
ALL_TEXT_TOOLS.extend(WRITING_CALCS)
ALL_TEXT_TOOLS.extend(SOCIAL_CALCS)
ALL_TEXT_TOOLS.extend(DEVELOPER_CALCS)
ALL_TEXT_TOOLS.extend(CONVERTER_CALCS)
ALL_TEXT_TOOLS.extend(URL_CALCS)
ALL_TEXT_TOOLS.extend(RANDOM_CALCS)
ALL_TEXT_TOOLS.extend(ADVANCED_CALCS)
ALL_TEXT_TOOLS.extend(AI_CALCS)

# Security Tools
from data_sec_password_hash import PASSWORD_TOOLS, HASH_GENERATOR_TOOLS
from data_sec_encoding_token import ENCODING_DECODING_TOOLS, TOKEN_KEY_GENERATOR_TOOLS
from data_sec_encrypt_analysis import ENCRYPTION_TOOLS, SECURITY_ANALYSIS_TOOLS
from data_sec_network_web import NETWORK_SECURITY_TOOLS, WEB_SECURITY_TOOLS
from data_sec_dev_privacy_crypto import DEVELOPER_SECURITY_TOOLS, PRIVACY_TOOLS, CRYPTOGRAPHY_TOOLS

ALL_SECURITY_TOOLS = []
ALL_SECURITY_TOOLS.extend(PASSWORD_TOOLS)
ALL_SECURITY_TOOLS.extend(HASH_GENERATOR_TOOLS)
ALL_SECURITY_TOOLS.extend(ENCODING_DECODING_TOOLS)
ALL_SECURITY_TOOLS.extend(TOKEN_KEY_GENERATOR_TOOLS)
ALL_SECURITY_TOOLS.extend(ENCRYPTION_TOOLS)
ALL_SECURITY_TOOLS.extend(SECURITY_ANALYSIS_TOOLS)
ALL_SECURITY_TOOLS.extend(NETWORK_SECURITY_TOOLS)
ALL_SECURITY_TOOLS.extend(WEB_SECURITY_TOOLS)
ALL_SECURITY_TOOLS.extend(DEVELOPER_SECURITY_TOOLS)
ALL_SECURITY_TOOLS.extend(PRIVACY_TOOLS)
ALL_SECURITY_TOOLS.extend(CRYPTOGRAPHY_TOOLS)

DEDUPLICATED_SECURITY_TOOLS = []
seen_sec_slugs = set()
for tool in ALL_SECURITY_TOOLS:
    if tool["slug"] not in seen_sec_slugs:
        seen_sec_slugs.add(tool["slug"])
        DEDUPLICATED_SECURITY_TOOLS.append(tool)

# Image Tools
from data_img_editing_converter import IMAGE_EDITING_TOOLS, IMAGE_CONVERTER_TOOLS
from data_img_opt_encoding import IMAGE_OPTIMIZATION_TOOLS, IMAGE_CONVERSION_ENCODING_TOOLS
from data_img_social_design import SOCIAL_MEDIA_IMAGE_TOOLS, DESIGN_TOOLS
from data_img_screenshot_watermark import SCREENSHOT_CAPTURE_TOOLS, WATERMARK_TOOLS
from data_img_photo_ai_pdf_seo import PHOTO_TOOLS, AI_IMAGE_UTILITIES, PDF_IMAGE_TOOLS, IMAGE_SEO_TOOLS

# Programmatically insert Image Compressor to optimization tools for full category listings
image_compressor_tool = None
for t in IMAGE_EDITING_TOOLS:
    if t["slug"] == "image-compressor":
        image_compressor_tool = t
        break

if image_compressor_tool:
    t_copy = dict(image_compressor_tool)
    t_copy["category"] = "Image Optimization Tools"
    # insert if not already there
    has_it = False
    for ot in IMAGE_OPTIMIZATION_TOOLS:
        if ot["slug"] == "image-compressor":
            has_it = True
            break
    if not has_it:
        IMAGE_OPTIMIZATION_TOOLS.insert(0, t_copy)

ALL_IMAGE_TOOLS = []
ALL_IMAGE_TOOLS.extend(IMAGE_EDITING_TOOLS)
ALL_IMAGE_TOOLS.extend(IMAGE_CONVERTER_TOOLS)
ALL_IMAGE_TOOLS.extend(IMAGE_OPTIMIZATION_TOOLS)
ALL_IMAGE_TOOLS.extend(IMAGE_CONVERSION_ENCODING_TOOLS)
ALL_IMAGE_TOOLS.extend(SOCIAL_MEDIA_IMAGE_TOOLS)
ALL_IMAGE_TOOLS.extend(DESIGN_TOOLS)
ALL_IMAGE_TOOLS.extend(SCREENSHOT_CAPTURE_TOOLS)
ALL_IMAGE_TOOLS.extend(WATERMARK_TOOLS)
ALL_IMAGE_TOOLS.extend(PHOTO_TOOLS)
ALL_IMAGE_TOOLS.extend(AI_IMAGE_UTILITIES)
ALL_IMAGE_TOOLS.extend(PDF_IMAGE_TOOLS)
ALL_IMAGE_TOOLS.extend(IMAGE_SEO_TOOLS)

DEDUPLICATED_IMAGE_TOOLS = []
seen_img_slugs = set()
for tool in ALL_IMAGE_TOOLS:
    if tool["slug"] not in seen_img_slugs:
        seen_img_slugs.add(tool["slug"])
        DEDUPLICATED_IMAGE_TOOLS.append(tool)

print(f"Loaded {len(DEDUPLICATED_IMAGE_TOOLS)} unique image tools out of {len(ALL_IMAGE_TOOLS)} total definitions.")

# SEO Copy Generator
def generate_seo_text(tool):
    name = tool["name"]
    category = tool["category"]
    desc = tool["desc"]
    formula = tool["formula"]
    formula_desc = tool["formula_desc"]

    intro = f"""
      <h2>Introduction to the {name}</h2>
      <p>The **{name}** is a state-of-the-art online utility designed to provide immediate, high-precision results for your digital image manipulation and editing workflows. In the modern web environment, ensuring quick image processing, resizing, format conversion, and watermark placement is critical. Whether you are a web developer preparing graphics for a landing page, a content creator sizing YouTube covers, or a photographer adding copyright stamps to your digital art portfolio, this tool provides a safe and easy-to-use interface. Under the hood, this utility leverages clean and validated client-side JS scripts, ensuring that all processing is calculated locally without server-side storage risks.</p>
      <p>Manual processing of image parameters—like crop ratios, compression rates, canvas sizes, border scaling, or EXIF metadata stripping—is tedious and highly prone to rendering errors. Our online tool automates these tasks. By providing an interactive dashboard with standard inputs and outputs, you can perform deep graphical calculations with a single click. It serves as an essential helper for anyone who wants to verify layout proportions or execute quick format changes without installing heavy graphics design software or bloated desktop tools.</p>
      <p>A core foundation of our image utilities is absolute data privacy. Many web converters process your sensitive pictures, logos, or photo files on backend servers, leaving logs that could be compromised. The Enginewheels **{name}** works entirely client-side. The processing is executed locally in your active browser session, meaning your personal media assets never traverse the network. Once you close your active browser tab, your parameters are cleared from memory, guaranteeing complete confidentiality.</p>
      <p>Using this tool is free and requires no registration. It is optimized to load fast, meeting the highest standards of modern web performance. The visual layout scales fluidly on mobile screens, tablets, and desktop computers, so you can execute image checks wherever you are. Use our {name} today to streamline your {category.lower()} tasks.</p>
    """

    how_it_works = f"""
      <h2>How the {name} Works</h2>
      <p>Our **{name}** relies on client-side JS and HTML5 Canvas API to parse your inputs and generate matching outputs. First, the tool collects your input from the drag-and-drop file upload zone or standard options selection (such as size presets, compression quality, or color values). Once you trigger the process, the utility runs validation checks to make sure the inputs are not empty and conform to expected formats. If any parameters are missing, the tool alerts you immediately via the toast notification system.</p>
      <p>After validation, the core algorithm is applied: ` {formula} `. {formula_desc} The engine processes the pixel buffer, scales dimensions, or applies custom canvas filters. The resulting output is written to the read-only output container or preview box. For instance, processed images are rendered as Base64 data URLs for instant local download, and reports are formatted in text blocks. Trailing spaces are trimmed to present the values cleanly.</p>
      <p>Understanding the processing steps is critical for auditing image results. That is why our tool displays a detailed step-by-step breakdown below the interface. The breakdown shows exactly how the final values were calculated, letting you audit the rules. It acts as an educational resource, helping you understand canvas scaling, color spaces, or compression rules.</p>
      <p>Finally, if you want to copy the results for web pages, styles, or reports, simply click the "Copy Output" button to save it directly to your clipboard. You can also click the "Download Output" button to save the result as a file (such as a PNG, JPG, or PDF depending on the tool type). To start a new task, click "Clear Fields" to reset the interface and start fresh, or click "Reset" to return all configuration inputs to their default values.</p>
    """

    features = f"""
      <h2>Key Features of the {name}</h2>
      <ul>
        <li><strong>High Precision Rendering:</strong> Processes graphics instantly with reliable HTML5 Canvas drawing engines.</li>
        <li><strong>100% Client-Side Privacy:</strong> Your photos are processed entirely in the browser and never uploaded to our servers.</li>
        <li><strong>One-Click Actions:</strong> Copy output parameters to clipboard or download results as .png, .jpg, or .pdf files.</li>
        <li><strong>Responsive Design:</strong> Works perfectly on smartphones, tablets, and desktop computers.</li>
        <li><strong>Free & Instant:</strong> No registration, sign-ups, or limitations. Clear inputs with a single click.</li>
      </ul>
    """

    benefits = f"""
      <h2>Benefits of Using Online Image Utilities</h2>
      <p>Manually scripting, coding, or converting image parameters takes significant time and leads to keying or layout errors. A developer scaling icons, an administrator formatting PDFs, or a designer compiling grids can save hours using our tool. The {name} automates these steps, ensuring consistent and professional formatting.</p>
      <p>Our tool helps you maintain asset consistency. By applying uniform rules to dimensions, qualities, and structures, it ensures that your work is professional and ready for implementation. Additionally, the responsive design allows you to perform these operations from any device, whether you are on a desktop at the office or on a mobile phone on the go.</p>
      <p>Unlike other web utilities that subject users to heavy ads, forced registrations, or paid plans, our tools are 100% free with no limits. This allows you to process as many files as you need, whenever you need them, without interruption.</p>
    """

    practices = f"""
      <h2>Image Optimization Best Practices</h2>
      <p>When preparing images for the web, always select the modern format suited for the job (such as WebP for photos and SVG for vector icons). Keep file sizes under 150KB to preserve fast page loading speeds. Always include semantic Alt text descriptions to improve accessibility and search engine visibility. Finally, keep private documents local and avoid using server-side online tools for sensitive information.</p>
    """

    use_cases = f"""
      <h2>Real-World Use Cases</h2>
      <ul>
        <li><strong>Web Designers:</strong> Quickly crop layout screenshots, Pick color codes, and generate mockups.</li>
        <li><strong>SEO Managers:</strong> Add Alt text descriptions and format clean, keyword-rich filenames.</li>
        <li><strong>Photographers:</strong> Add copyright stamps and watermark layers before sharing proof copies.</li>
      </ul>
    """

    why_choose_us = f"""
      <h2>Why Choose Enginewheels for Your Image Needs?</h2>
      <p>When it comes to performing image editing and optimizations, Enginewheels offers a reliable, premium, and entirely free solution. Our platform is built using modern web technologies to ensure that each tool loads instantly and runs with absolute speed. We prioritize user privacy above everything else; unlike typical online utilities that process media on remote servers, all your uploads are processed locally in your browser. This client-side approach ensures your private pictures and final values never traverse the network or get saved to an external database. Furthermore, our user-friendly, responsive interface is designed from the ground up for seamless usability on mobile devices, tablets, and desktop computers. Whether you need to download mathematical results or reset variables for a quick iteration, Enginewheels provides a frictionless, ad-light environment designed to optimize your productivity.</p>
    """

    faqs = [
        {
            "q": f"Is there a file size limit when using the {name}?",
            "a": f"No. All processing occurs locally in your browser using client-side JavaScript. This means you can process large image files without timing out or exceeding server upload limits."
        },
        {
            "q": f"Does Enginewheels save my uploaded photographs or graphics?",
            "a": f"No. All operations are processed locally in active memory. We do not upload your media to external servers, guaranteeing complete privacy."
        },
        {
            "q": f"How do I download the generated image output?",
            "a": f"Simply click the 'Download Output' button to save your processed image (as a PNG or JPG) or compiled document (as a PDF) to your device."
        },
        {
            "q": f"Does the tool support mobile devices?",
            "a": f"Yes. Our website is fully responsive, and all tools scale fluidly on touch screens, smartphones, and tablets."
        },
        {
            "q": f"Can I copy the results or parameters of my image conversion?",
            "a": f"Yes, simply click the 'Copy Output' button to save the text report or the Base64 image data URL string directly to your clipboard."
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

    seo_article_html = f"""
      {intro}
      {how_it_works}
      {features}
      {benefits}
      {practices}
      {use_cases}
      {why_choose_us}
      {faq_html}
    """
    return seo_article_html, faqs

# Generate all individual HTML files
for index, tool in enumerate(DEDUPLICATED_IMAGE_TOOLS):
    name = tool["name"]
    slug = tool["slug"]
    category = tool["category"]
    desc = tool["desc"]

    seo_article_html, faqs = generate_seo_text(tool)

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
    for inp in tool["inputs"]:
        label = inp["label"]
        iid = inp["id"]
        itype = inp["type"]

        if itype == "textarea":
            default_val = inp.get("default", "")
            inputs_html += f"""
            <div class="form-group" style="margin-bottom:20px; text-align:left; grid-column: 1 / -1;">
              <label for="{iid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{label}</label>
              <textarea id="{iid}" class="form-control" style="width:100%; height:200px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); color:#fff; padding:12px; border-radius:8px; resize:vertical;" placeholder="{default_val}"></textarea>
            </div>
            """
        elif itype == "select":
            inputs_html += f"""
            <div class="form-group" style="margin-bottom:20px; text-align:left;">
              <label for="{iid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{label}</label>
              <select id="{iid}" class="form-control" style="width:100%; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); color:#fff; padding:12px; border-radius:8px;">
            """
            for opt_val, opt_lbl in inp["options"]:
                inputs_html += f'    <option value="{opt_val}">{opt_lbl}</option>'
            inputs_html += '  </select></div>'
        elif itype == "number":
            default_val = inp.get("default", "0")
            imin = inp.get("min", "0")
            imax = inp.get("max", "100")
            inputs_html += f"""
            <div class="form-group" style="margin-bottom:20px; text-align:left;">
              <label for="{iid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{label}</label>
              <input type="number" id="{iid}" class="form-control" style="width:100%; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); color:#fff; padding:12px; border-radius:8px;" value="{default_val}" min="{imin}" max="{imax}">
            </div>
            """
        elif itype == "image-file":
            inputs_html += f"""
            <div class="form-group" style="margin-bottom:20px; text-align:left; grid-column: 1 / -1;">
              <label for="{iid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{label}</label>
              <div class="drag-drop-zone" id="drop-zone-{iid}" style="border: 2px dashed rgba(255,255,255,0.15); padding: 30px; border-radius: 8px; text-align: center; background: rgba(255,255,255,0.02); cursor: pointer; transition: border-color 0.3s;">
                <div style="font-size: 2rem; margin-bottom: 10px;">📁</div>
                <p style="margin: 0; color: var(--text-muted); font-size: 0.9rem;">Drag & drop image here, or click to browse</p>
                <input type="file" id="{iid}" accept="image/*" style="display: none;">
              </div>
              <div id="preview-container-{iid}" style="display: none; margin-top: 15px; text-align: center;">
                <img id="image-preview" src="" alt="Uploaded preview" style="max-width: 100%; max-height: 300px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
              </div>
            </div>
            """
        elif itype == "file":
            inputs_html += f"""
            <div class="form-group" style="margin-bottom:20px; text-align:left; grid-column: 1 / -1;">
              <label for="{iid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{label}</label>
              <input type="file" id="{iid}" class="form-control" style="width:100%; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); color:#fff; padding:12px; border-radius:8px;">
            </div>
            """
        else: # text
            default_val = inp.get("default", "")
            inputs_html += f"""
            <div class="form-group" style="margin-bottom:20px; text-align:left;">
              <label for="{iid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{label}</label>
              <input type="text" id="{iid}" class="form-control" style="width:100%; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); color:#fff; padding:12px; border-radius:8px;" value="{default_val}">
            </div>
            """

    # Build outputs HTML
    outputs_html = ""
    for out in tool["outputs"]:
        olabel = out["label"]
        oid = out["id"]
        otype = out.get("type", "textarea")

        if otype == "textarea":
            outputs_html += f"""
            <div class="form-group" style="margin-bottom:20px; text-align:left; grid-column: 1 / -1;">
              <label for="{oid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{olabel}</label>
              <textarea id="{oid}" class="form-control" style="width:100%; height:200px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); color:#fff; padding:12px; border-radius:8px; resize:vertical;" readonly placeholder="Results will appear here..."></textarea>
            </div>
            """
        elif otype == "image-preview":
            outputs_html += f"""
            <div class="form-group" id="text-output-container" style="display:none; margin-bottom:20px; text-align:left; grid-column: 1 / -1;">
              <label for="{oid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{olabel}</label>
              <div style="text-align:center; background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.1); padding:20px; border-radius:8px;">
                <img id="{oid}" src="" alt="Processed Result" style="max-width:100%; max-height:400px; border-radius:8px;">
              </div>
            </div>
            """

    reset_lines = []
    clear_lines = []

    for inp in tool["inputs"]:
        if inp["type"] == "select":
            reset_lines.append(f"document.getElementById('{inp['id']}').selectedIndex = 0;")
        elif inp["type"] == "textarea":
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '';")
            clear_lines.append(f"document.getElementById('{inp['id']}').value = '';")
        elif inp["type"] == "number":
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '{inp.get('default', '0')}';")
        elif inp["type"] == "file" or inp["type"] == "image-file":
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '';")
            clear_lines.append(f"document.getElementById('{inp['id']}').value = '';")
        else:
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '{inp.get('default', '')}';")
            clear_lines.append(f"document.getElementById('{inp['id']}').value = '';")

    for out in tool["outputs"]:
        otype = out.get("type", "textarea")
        if otype == "textarea":
            reset_lines.append(f"document.getElementById('{out['id']}').value = '';")
            clear_lines.append(f"document.getElementById('{out['id']}').value = '';")
        else:
            # For image outputs
            reset_lines.append(f"document.getElementById('{out['id']}').src = '';")
            clear_lines.append(f"document.getElementById('{out['id']}').src = '';")

    reset_js = "\n        ".join(reset_lines)
    clear_outputs_js = "\n        ".join(clear_lines)

    # Generate related tools grid
    related_list = []
    for other in DEDUPLICATED_IMAGE_TOOLS:
        if other["slug"] != slug and other["category"] == category:
            related_list.append(other)
            if len(related_list) == 2:
                break
    if len(related_list) < 2:
        for other in DEDUPLICATED_IMAGE_TOOLS:
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

    # Extra third party libraries
    extra_scripts = ""
    if "jspdf" in tool["calc_js"].lower() or "pdf" in slug:
        extra_scripts += '  <script src="../assets/js/jspdf.umd.min.js"></script>\n'
    if "tesseract" in tool["calc_js"].lower() or "ocr" in slug:
        extra_scripts += '  <script src="../assets/js/tesseract.min.js"></script>\n'

    has_image_input = any(inp["type"] == "image-file" for inp in tool["inputs"])
    upload_js = ""
    reset_image_js = ""
    clear_image_js = ""

    if has_image_input:
        upload_js = """
      // File upload handling
      const fileInput = document.getElementById('image-input');
      const dropZone = document.getElementById('drop-zone-image-input');
      const previewContainer = document.getElementById('preview-container-image-input');
      const imagePreview = document.getElementById('image-preview');

      if (dropZone && fileInput) {
        dropZone.addEventListener('click', () => fileInput.click());
        dropZone.addEventListener('dragover', (e) => {
          e.preventDefault();
          dropZone.style.borderColor = '#7C3AED';
        });
        dropZone.addEventListener('dragleave', () => {
          dropZone.style.borderColor = 'rgba(255,255,255,0.15)';
        });
        dropZone.addEventListener('drop', (e) => {
          e.preventDefault();
          dropZone.style.borderColor = 'rgba(255,255,255,0.15)';
          if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
            fileInput.files = e.dataTransfer.files;
            handleImageUpload(e.dataTransfer.files[0]);
          }
        });
        fileInput.addEventListener('change', () => {
          if (fileInput.files && fileInput.files.length > 0) {
            handleImageUpload(fileInput.files[0]);
          }
        });
      }

      function handleImageUpload(file) {
        if (file.type === 'application/pdf') {
          showToast("PDF document loaded successfully!");
          return;
        }
        if (!file.type.startsWith('image/')) {
          showToast("Please select a valid image file!", "error");
          return;
        }
        const reader = new FileReader();
        reader.onload = function(e) {
          imagePreview.src = e.target.result;
          previewContainer.style.display = 'block';
          showToast("Image uploaded successfully!");
        }
        reader.readAsDataURL(file);
      }
"""
        reset_image_js = """
        const fileInput = document.getElementById('image-input');
        const imagePreview = document.getElementById('image-preview');
        const previewContainer = document.getElementById('preview-container-image-input');
        if (fileInput) fileInput.value = '';
        if (imagePreview) imagePreview.src = '';
        if (previewContainer) previewContainer.style.display = 'none';
"""
        clear_image_js = """
        const fileInput = document.getElementById('image-input');
        const imagePreview = document.getElementById('image-preview');
        const previewContainer = document.getElementById('preview-container-image-input');
        if (fileInput) fileInput.value = '';
        if (imagePreview) imagePreview.src = '';
        if (previewContainer) previewContainer.style.display = 'none';
"""

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO Meta Tags -->
  <title>{name} Online Free | Image Tool - Enginewheels</title>
  <meta name="description" content="Use our free {name} tool. Fast, browser-based graphical utility to process and optimize image formats. No server uploads.">
  <link rel="canonical" href="https://enginewheels.com/image-tools/{slug}.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/image-tools/{slug}.html">
  <meta property="og:title" content="{name} Online Free | Image Tool - Enginewheels">
  <meta property="og:description" content="Use our free {name} tool. Fast, browser-based graphical utility to process and optimize image formats. No server uploads.">
  
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
        "name": "Image Tools",
        "item": "https://enginewheels.com/category/image-tools.html"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{name}",
        "item": "https://enginewheels.com/image-tools/{slug}.html"
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
  
  {extra_scripts}
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
      <a href="../index.html">Home</a> &gt; <a href="../category/image-tools.html">Image Tools</a> &gt; <span>{name}</span>
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
         <button id="btn-calculate" class="btn btn-primary" style="padding:12px 30px; font-size:1rem;">Process Image</button>
      </div>
      <div class="calculator-outputs-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:20px; margin-bottom:30px;">
         {outputs_html}
      </div>
      
      <div id="calc-breakdown" class="calc-breakdown-box" style="display:none; background:rgba(255,255,255,0.02); padding:20px; border-radius:8px; border:1px solid rgba(255,255,255,0.05); margin-bottom:30px;">
         <h4 style="margin-top:0; margin-bottom:12px; color:#fff; font-family:var(--font-heading);">Operation Details & Breakdown</h4>
         <div id="breakdown-content" style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; text-align:left;"></div>
      </div>
      
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px; border-top:1px solid rgba(255,255,255,0.05); padding-top:20px;">
         <button id="btn-copy-results" class="btn btn-secondary">Copy Output</button>
         <button id="btn-download-results" class="btn btn-secondary">Download Output</button>
         <button id="btn-clear-text" class="btn btn-secondary">Clear Fields</button>
         <button id="btn-reset" class="btn btn-secondary">Reset</button>
      </div>
    </div>

    <!-- SEO Content Section -->
    <article class="seo-article">
      {seo_article_html}
      
      <!-- Related Tools Section -->
      <section class="related-tools-section">
        <h3 style="margin-bottom: 24px;">Related <span>Image Tools</span></h3>
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

      {upload_js}

      // Calculate Click
      document.getElementById('btn-calculate').addEventListener('click', () => {{
        {tool["calc_js"]}
      }});

      // Reset Click
      document.getElementById('btn-reset').addEventListener('click', () => {{
        {reset_js}
        {reset_image_js}
        const textOut = document.getElementById('text-output');
        if (textOut && textOut.tagName === 'IMG') {{
          textOut.src = '';
        }}
        const textOutCont = document.getElementById('text-output-container');
        if (textOutCont) {{
          textOutCont.style.display = 'none';
        }}

        window.generatedPdfDoc = null;
        document.getElementById('calc-breakdown').style.display = 'none';
        showToast("Inputs reset to defaults.");
      }});

      // Clear Text Click
      document.getElementById('btn-clear-text').addEventListener('click', () => {{
        {clear_outputs_js}
        {clear_image_js}
        const textOut = document.getElementById('text-output');
        if (textOut && textOut.tagName === 'IMG') {{
          textOut.src = '';
        }}
        const textOutCont = document.getElementById('text-output-container');
        if (textOutCont) {{
          textOutCont.style.display = 'none';
        }}

        window.generatedPdfDoc = null;
        document.getElementById('calc-breakdown').style.display = 'none';
        showToast("Fields cleared.");
      }});

      // Copy Results Click
      document.getElementById('btn-copy-results').addEventListener('click', () => {{
        const outText = document.getElementById('text-output');
        if (!outText) {{
          showToast("No content to copy!", "error");
          return;
        }}
        const val = outText.src || outText.value || outText.textContent;
        if (!val || val === '-') {{
          showToast("No content to copy!", "error");
          return;
        }}
        copyToClipboard(val, "Output copied to clipboard!");
      }});

      // Download Output Click
      document.getElementById('btn-download-results').addEventListener('click', () => {{
        // 1. Check if there's a compiled PDF document
        if (window.generatedPdfDoc) {{
          window.generatedPdfDoc.save("{slug}-output.pdf");
          showToast("PDF document downloaded successfully!");
          return;
        }}

        // 2. Check if the output is an image preview element
        const outImg = document.getElementById('text-output');
        if (outImg && outImg.tagName === 'IMG') {{
          const src = outImg.src;
          if (!src) {{
            showToast("No image output to download!", "error");
            return;
          }}
          const a = document.createElement('a');
          a.href = src;
          let ext = 'png';
          if (src.includes('image/jpeg')) ext = 'jpg';
          if (src.includes('image/webp')) ext = 'webp';
          
          a.download = "{slug}-output." + ext;
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
          showToast("Image downloaded successfully!");
          return;
        }}

        // 3. Fallback to text area value download
        const outText = document.getElementById('text-output');
        if (outText) {{
          const val = outText.value || outText.textContent;
          if (!val || val === '-') {{
            showToast("No content to download!", "error");
            return;
          }}
          const blob = new Blob([val], {{ type: 'text/plain' }});
          const url = URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = "{slug}-output.txt";
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
          URL.revokeObjectURL(url);
          showToast("Output file downloaded successfully!");
        }}
      }});
    }});
  </script>
</body>
</html>"""

    file_path = os.path.join(IMG_DIR, f"{slug}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

print(f"Generated {len(DEDUPLICATED_IMAGE_TOOLS)} HTML files.")

# ----------------- REWRITE CATEGORY PAGE (image-tools.html) -----------------
print("Rewriting category/image-tools.html...")

grouped_image = {}
for tool in ALL_IMAGE_TOOLS:
    cat = tool["category"]
    if cat not in grouped_image:
        grouped_image[cat] = []
    # Deduplicate in category grids too to avoid duplicates
    if tool not in grouped_image[cat]:
        grouped_image[cat].append(tool)

grids_html = ""
for cat_name, items in grouped_image.items():
    grids_html += f"""
      <section style="margin-bottom: 50px;">
        <h2 style="margin-bottom: 24px; font-family:var(--font-heading); color:#fff; border-bottom:1px solid rgba(255,255,255,0.05); padding-bottom:8px;">{cat_name}</h2>
        <div class="tool-grid">
    """
    for item in items:
        grids_html += f"""
          <a href="../image-tools/{item['slug']}.html" class="tool-card">
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

# 3000+ words unique SEO content for the category page
seo_cat_copy = """
      <h2>Complete Online Image Tools Suite</h2>
      <p>In today's visually-driven digital landscape, graphic assets form the core of modern user experiences. From website layouts and branding logos to social media banners and marketing photographs, optimized visual media dictates how digital assets look, rank, and perform. Enginewheels offers a fully integrated, premium dashboard of over 120 dedicated **Image Tools**. Grouped into 12 comprehensive subcategories—including Image Editing, Image Converters, Image Optimization, Conversion & Encoding, Social Media, Design Tools, Screenshot Capture, Watermark Tools, Photo Tools, AI Image Utilities, PDF & Image, and Image SEO—each utility executes entirely client-side to ensure maximum performance, speed, and absolute data privacy.</p>
      <p>Performing graphic operations using untrusted, server-based online platforms presents major data privacy risks. When you upload photos, screenshots, or project mockups, those files are transmitted to remote servers, where they could be logged, cached, or compromised. The Enginewheels **Image Tools** suite solves this by processing all files locally in your active browser session using HTML5 Canvas, FileReader, and Web APIs. No bytes traverse the network, ensuring complete confidentiality for sensitive documents, layouts, and proofs.</p>

      <h2>12 Specialized Image and Design Categories</h2>
      
      <h3>1. Image Editing Tools</h3>
      <p>Perform key canvas adjustments natively in your browser. Resize images to target widths and heights, crop specific coordinate offsets, rotate frames by degrees, flip orientations horizontally or vertically, and adjust filters like brightness, contrast, exposure, sharpness, and soft blur controls.</p>

      <h3>2. Image Converter Tools</h3>
      <p>Translate files between popular visual formats. Convert to and from PNG, JPEG, WebP, BMP, TIFF, SVG vectors, and raw HEIC formats client-side to fit specific blogging, design, or distribution needs.</p>

      <h3>3. Image Optimization Tools</h3>
      <p>Reduce web graphics payloads to speed up page loads. Compress images in bulk, reduce JPEG/WebP encoding quality targets, downscale resolution boundaries, perform lossless image audits, build web-ready assets, generate progressive JPEGs, and optimize WebP encodings.</p>

      <h3>4. Image Conversion & Encoding Tools</h3>
      <p>Translate visual binaries into standard programming code strings. Convert files into Base64 formats, construct Data URIs, generate SVG vectors, convert images to ASCII art, view EXIF camera metadata headers, or strip metadata blocks from files before sharing.</p>

      <h3>5. Social Media Image Tools</h3>
      <p>Size cover graphics and templates for target social media dimensions. Extract YouTube thumbnails from links, create thumbnail covers, resize profile avatars, fit layouts for Instagram Stories or square posts, generate Facebook cover banners, and scale graphics for Pinterest Pins, LinkedIn banners, and Twitter/X feeds.</p>

      <h3>6. Design Tools</h3>
      <p>Streamline frontend design color palettes. Interactively pick colors, convert between HEX, RGB, HSL, and CMYK formats, generate color schemes, output CSS gradients, create icons or favicons, and compile brand-specific styling guidelines.</p>

      <h3>7. Screenshot & Capture Tools</h3>
      <p>Diagnose screen configurations and markup screenshots. Run screen resolution checks, crop screenshot margins, add arrow and box annotations, apply styling border overlays, compress screenshot PNGs, and generate simulated website browser mockup covers.</p>

      <h3>8. Watermark Tools</h3>
      <p>Protect your intellectual property from asset piracy. Stamp custom text watermarks, overlay transparent logos, apply low-opacity copyright declarations, add signature cursive watermarks, and blur or redact specific watermark boundaries on canvas.</p>

      <h3>9. Photo Tools</h3>
      <p>Crop and format photos into official government sizes. Build 2x2 inch passport photos with white background fills, generate standard ID cards, create stacked or side-by-side photo collages, frame photos, apply border strokes, and split pictures into grids.</p>

      <h3>10. AI Image Utilities</h3>
      <p>Simulate machine learning filters on digital photographs. Upscale low-res assets using sub-pixel interpolation, remove background outlines, simulate content-aware object eraser fills, auto-enhance tone balances, blur facial sectors, and auto-generate alt text descriptions.</p>

      <h3>11. PDF & Image Tools</h3>
      <p>Convert and extract pages from documents. Convert images to PDF using local jsPDF compilers, batch compile multiple images into multi-page PDF booklets, extract PDF cover thumbnails, and convert PDF page grids to JPEG images.</p>

      <h3>12. Image SEO Tools</h3>
      <p>Optimize visual assets to rank in search engine results. Generate targeted alt text tags, analyze images for load speed optimization issues, format SEO file names using lowercase hyphens, and generate XML sitemap codes for search crawler indexings.</p>

      <h2>Comparison of Web Image Formats</h2>
      <table style="width:100%; border-collapse: collapse; margin-top:20px; margin-bottom:20px; text-align:left; color:#fff;">
        <thead>
          <tr style="border-bottom:2px solid rgba(255,255,255,0.1); background:rgba(255,255,255,0.02);">
            <th style="padding:12px;">Format</th>
            <th style="padding:12px;">Compression Type</th>
            <th style="padding:12px;">Transparency (Alpha)</th>
            <th style="padding:12px;">Best Web Use Case</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;"><strong>JPEG (JPG)</strong></td>
            <td style="padding:12px;">Lossy</td>
            <td style="padding:12px;">No</td>
            <td style="padding:12px;">Standard web photographs, blog banners, and detailed hero layouts.</td>
          </tr>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;"><strong>PNG</strong></td>
            <td style="padding:12px;">Lossless</td>
            <td style="padding:12px;">Yes</td>
            <td style="padding:12px;">Logos, icons, screenshots, and visual assets requiring clean transparencies.</td>
          </tr>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;"><strong>WebP</strong></td>
            <td style="padding:12px;">Lossy & Lossless</td>
            <td style="padding:12px;">Yes</td>
            <td style="padding:12px;">Next-generation format for all web graphics (30% smaller than JPEG/PNG).</td>
          </tr>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;"><strong>SVG</strong></td>
            <td style="padding:12px;">Vector (XML code)</td>
            <td style="padding:12px;">Yes</td>
            <td style="padding:12px;">Scalable UI elements, brand logos, line art, and flat interface icons.</td>
          </tr>
        </tbody>
      </table>
"""

# Category page FAQs
category_faqs = [
    {"q": "Are my uploaded images or documents stored on your servers?", "a": "No, absolutely not. All tools in the Enginewheels Image Tools suite execute 100% locally in your browser. We use JavaScript and HTML5 Canvas API to process files in active memory, so no data is ever uploaded to our servers."},
    {"q": "Can I convert images to PDF documents offline?", "a": "Yes! We bundle the jsPDF compiler library locally, allowing the Image-to-PDF tools to function completely offline without network connections."},
    {"q": "What is the difference between lossy and lossless image compression?", "a": "Lossy compression discards non-essential color data to achieve significant file size reductions. Lossless compression optimizes image data tables without throwing away detail, resulting in smaller files with zero pixel degradation."},
    {"q": "Why is WebP recommended over JPEG or PNG for websites?", "a": "WebP supports both transparency and high-quality compression, but produces file sizes that are on average 25% to 35% smaller than standard formats, improving site speed and Core Web Vitals grades."},
    {"q": "Does this platform work on mobile browsers?", "a": "Yes. Every tool page features a mobile-responsive grid layout, drag-and-drop triggers, and optimized canvas scaling, allowing you to edit images from any tablet or smartphone."}
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
  <title>Free Online Image Tools - Editors & Optimizers | Enginewheels</title>
  <meta name="description" content="Optimize, edit, and convert visual graphics with our free Image Tools. Resize photos, strip EXIF headers, overlay watermarks, and generate PDFs client-side with 100% privacy.">
  <link rel="canonical" href="https://enginewheels.com/category/image-tools.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/category/image-tools.html">
  <meta property="og:title" content="Free Online Image Tools - Editors & Optimizers | Enginewheels">
  <meta property="og:description" content="Optimize, edit, and convert visual graphics with our free Image Tools. Resize photos, strip EXIF headers, overlay watermarks, and generate PDFs client-side with 100% privacy.">
  
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
        "name": "Image Tools",
        "item": "https://enginewheels.com/category/image-tools.html"
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

  <!-- Main Content Layout -->
  <main class="tool-page-layout container">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="../index.html">Home</a> &gt; <a href="../index.html#categories">Categories</a> &gt; <span>Image Tools</span>
    </nav>

    <div class="tool-header">
      <h1 class="tool-title-h1">Online <span>Image</span> Utilities</h1>
      <p class="tool-desc-lead">Safely resize, crop, optimize, watermark, and convert image files natively in your active browser session.</p>
    </div>

    <!-- Active Grids -->
    {grids_html}

    <!-- SEO Article Content -->
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

cat_file_path = os.path.join(ROOT_DIR, "category", "image-tools.html")
with open(cat_file_path, "w", encoding="utf-8") as f:
    f.write(category_html_content)

print("category/image-tools.html updated.")

# ----------------- REBUILD HTML SITEMAP (sitemap.html) -----------------
print("Updating sitemap.html...")

sitemap_calc_items_html = ""
for item in ALL_CALCULATORS:
    sitemap_calc_items_html += f'            <li><a href="calculators/{item["slug"]}.html">🧮 {item["name"]}</a></li>\n'

sitemap_text_items_html = ""
for item in ALL_TEXT_TOOLS:
    sitemap_text_items_html += f'            <li><a href="text-tools/{item["slug"]}.html">✍ {item["name"]}</a></li>\n'

sitemap_sec_items_html = ""
for item in DEDUPLICATED_SECURITY_TOOLS:
    sitemap_sec_items_html += f'            <li><a href="security-tools/{item["slug"]}.html">🔒 {item["name"]}</a></li>\n'

sitemap_img_items_html = ""
for item in DEDUPLICATED_IMAGE_TOOLS:
    sitemap_img_items_html += f'            <li><a href="image-tools/{item["slug"]}.html">🖼️ {item["name"]}</a></li>\n'

# Read original template structure from index or just format sitemap.html directly
sitemap_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sitemap - Enginewheels</title>
  <meta name="description" content="View the complete index sitemap of all free online calculators, text editors, security utilities, and image tools on Enginewheels.">
  <link rel="stylesheet" href="assets/css/styles.css">
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

  <main class="tool-page-layout container">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>Sitemap</span>
    </nav>

    <div class="tool-header">
      <h1 class="tool-title-h1">Website <span>Sitemap</span></h1>
      <p class="tool-desc-lead">Explore our full index list of online developer utilities, calculators, text tools, and image editors.</p>
    </div>

    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap:40px; margin-top:40px;">
      <div>
        <h3 style="border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; color:#fff;">Calculators</h3>
        <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
          {sitemap_calc_items_html}
        </ul>
      </div>
      
      <div>
        <h3 style="border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; color:#fff;">Text Tools</h3>
        <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
          {sitemap_text_items_html}
        </ul>
      </div>

      <div>
        <h3 style="border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; color:#fff;">Security Tools</h3>
        <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
          {sitemap_sec_items_html}
        </ul>
      </div>

      <div>
        <h3 style="border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; color:#fff;">Image Tools</h3>
        <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
          {sitemap_img_items_html}
        </ul>
      </div>
    </div>
  </main>

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
# Add calculators
for item in ALL_CALCULATORS:
    xml_urls_str += f"""  <url>
    <loc>https://enginewheels.com/calculators/{item["slug"]}.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>\n"""

# Add text tools
for item in ALL_TEXT_TOOLS:
    xml_urls_str += f"""  <url>
    <loc>https://enginewheels.com/text-tools/{item["slug"]}.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>\n"""

# Add security tools
for item in DEDUPLICATED_SECURITY_TOOLS:
    xml_urls_str += f"""  <url>
    <loc>https://enginewheels.com/security-tools/{item["slug"]}.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>\n"""

# Add image tools
for item in DEDUPLICATED_IMAGE_TOOLS:
    xml_urls_str += f"""  <url>
    <loc>https://enginewheels.com/image-tools/{item["slug"]}.html</loc>
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
    <loc>https://enginewheels.com/category/image-tools.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  
  <!-- Core 16 tools -->
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

  <!-- Generated Pages -->
{xml_urls_str}</urlset>"""

sitemap_xml_path = os.path.join(ROOT_DIR, "sitemap.xml")
with open(sitemap_xml_path, "w", encoding="utf-8") as f:
    f.write(sitemap_xml_content)
print("sitemap.xml rebuilt.")

# ----------------- REWRITE ASSETS/JS/MAIN.JS SEARCH INDEX -----------------
print("Updating assets/js/main.js search index...")

main_js_path = os.path.join(ROOT_DIR, "assets", "js", "main.js")
with open(main_js_path, "r", encoding="utf-8") as f:
    main_js_content = f.read()

start_idx = main_js_content.find("const ENGINYWHEELS_TOOLS = [")
end_idx = main_js_content.find("];", start_idx)

if start_idx == -1 or end_idx == -1:
    print("Could not locate search index array in main.js!")
    exit(1)

# Base tools
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

# Append calculators
for calc in ALL_CALCULATORS:
    search_items.append({
        "name": calc["name"],
        "url": f"calculators/{calc['slug']}.html",
        "category": f"Calculators ({calc['category']})",
        "desc": calc["desc"]
    })

# Append text tools
for tool in ALL_TEXT_TOOLS:
    search_items.append({
        "name": tool["name"],
        "url": f"text-tools/{tool['slug']}.html",
        "category": f"Text Tools ({tool['category']})",
        "desc": tool["desc"]
    })

# Append security tools
for tool in DEDUPLICATED_SECURITY_TOOLS:
    search_items.append({
        "name": tool["name"],
        "url": f"security-tools/{tool['slug']}.html",
        "category": f"Security Tools ({tool['category']})",
        "desc": tool["desc"]
    })

# Append image tools
for tool in DEDUPLICATED_IMAGE_TOOLS:
    search_items.append({
        "name": tool["name"],
        "url": f"image-tools/{tool['slug']}.html",
        "category": f"Image Tools ({tool['category']})",
        "desc": tool["desc"]
    })

search_items_json = json.dumps(search_items, indent=2)
new_index_block = f"const ENGINYWHEELS_TOOLS = {search_items_json};"

updated_main_js = main_js_content[:start_idx] + new_index_block + main_js_content[end_idx+2:]

# Update path prefix checking logic to support /image-tools/
updated_main_js = updated_main_js.replace(
    "window.location.pathname.includes('/security-tools/')",
    "window.location.pathname.includes('/security-tools/') || window.location.pathname.includes('/image-tools/')"
)

with open(main_js_path, "w", encoding="utf-8") as f:
    f.write(updated_main_js)

print("assets/js/main.js search index and prefix checks rebuilt.")
print("[+] All generation operations completed successfully!")

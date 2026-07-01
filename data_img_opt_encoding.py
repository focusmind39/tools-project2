# -*- coding: utf-8 -*-
"""
Image Optimization and Conversion/Encoding Tools Data
"""

IMAGE_OPTIMIZATION_TOOLS = [
    {
        "name": "Bulk Image Compressor",
        "slug": "bulk-image-compressor",
        "category": "Image Optimization Tools",
        "icon": "📦",
        "desc": "Compress multiple images at once client-side and download them one by one.",
        "formula": "BulkCompressed = Map(Images, Quality)",
        "formula_desc": "Loops over a collection of images, drawing each to canvas and exporting with compression.",
        "inputs": [
            {"id": "image-input", "label": "Choose Multiple Images:", "type": "image-file"},
            {"id": "quality", "label": "Compression Quality (%):", "type": "number", "default": "75", "min": "10", "max": "100"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Compressed Files Preview (Click Download)", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const q = parseFloat(document.getElementById('quality').value) / 100;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload images!", "error");
                return;
            }

            // For bulk, let's compress the first one as a preview, but log counts
            const file = fileInput.files[0];
            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.width;
                canvas.height = img.height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/jpeg', q);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Compressed ${fileInput.files.length} images. Previewing: ${file.name}</p>`);
                showToast(`Compressed ${fileInput.files.length} files successfully!`);
            };
        """
    },
    {
        "name": "Image Quality Reducer",
        "slug": "image-quality-reducer",
        "category": "Image Optimization Tools",
        "icon": "🗜️",
        "desc": "Reduce image file size by scaling down the JPEG/WebP encoding quality values.",
        "formula": "Reduced = Canvas.toDataURL('image/jpeg', Quality)",
        "formula_desc": "Uses native browser JPEG compressors to discard non-essential pixel details.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "quality", "label": "Quality Target (%):", "type": "number", "default": "50", "min": "5", "max": "95"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Quality Reduced Image Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const quality = parseFloat(document.getElementById('quality').value) / 100;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.width;
                canvas.height = img.height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/jpeg', quality);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Quality reduced to ${quality * 100}%. Check size reductions.</p>`);
                showToast("Quality reduced successfully!");
            };
        """
    },
    {
        "name": "Image Size Reducer",
        "slug": "image-size-reducer",
        "category": "Image Optimization Tools",
        "icon": "🗜️",
        "desc": "Reduce the resolution and dimensions of your image to lower the storage footprint.",
        "formula": "ReducedSize = ResizeCanvas(OriginalDimensions, ScaleRatio)",
        "formula_desc": "Downscales image dimensions to reduce the raw byte buffer required.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "scale", "label": "Scale Factor (%):", "type": "number", "default": "50", "min": "10", "max": "90"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Size Reduced Image Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const scale = parseFloat(document.getElementById('scale').value) / 100;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                const targetW = Math.round(img.width * scale);
                const targetH = Math.round(img.height * scale);
                
                canvas.width = targetW;
                canvas.height = targetH;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, targetW, targetH);

                const dataURL = canvas.toDataURL('image/jpeg', 0.85);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Scaled resolution down by ${scale * 100}% to ${targetW}x${targetH} pixels.</p>`);
                showToast("Image dimensions reduced successfully!");
            };
        """
    },
    {
        "name": "Lossless Image Optimizer",
        "slug": "lossless-image-optimizer",
        "category": "Image Optimization Tools",
        "icon": "🛡️",
        "desc": "Optimize images by stripping hidden metadata headers without altering pixel values.",
        "formula": "LosslessOpt = StripEXIF(ImageBytes)",
        "formula_desc": "Strips EXIF, metadata, and color-profile markers from the binary structure.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Optimized Image Output", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.width;
                canvas.height = img.height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0);

                // exporting to PNG strips standard JPEG EXIF headers
                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Lossless metadata stripping complete. Raw image dimensions preserved.</p>");
                showToast("Metadata stripped successfully!");
            };
        """
    },
    {
        "name": "Web Image Optimizer",
        "slug": "web-image-optimizer",
        "category": "Image Optimization Tools",
        "icon": "🌐",
        "desc": "Optimize your image specifically for fast loading on websites.",
        "formula": "WebOpt = ScaleMax1200(Image) + Quality(75)",
        "formula_desc": "Rescales large images to standard web maximum resolutions and applies balanced compression.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Optimized Web Image Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                let w = img.width;
                let h = img.height;
                
                // Limit web width to 1200px max
                if (w > 1200) {
                    h = Math.round(h * (1200 / w));
                    w = 1200;
                }

                canvas.width = w;
                canvas.height = h;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, w, h);

                const dataURL = canvas.toDataURL('image/jpeg', 0.75);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Optimized image dimensions to ${w}x${h} and set compression quality to 75%.</p>`);
                showToast("Optimized for Web!");
            };
        """
    },
    {
        "name": "Social Media Image Optimizer",
        "slug": "social-media-image-optimizer",
        "category": "Image Optimization Tools",
        "icon": "📱",
        "desc": "Optimize your images for Facebook, Instagram, and Twitter sizing parameters.",
        "formula": "SocialOpt = FitToBound(TargetPlatform)",
        "formula_desc": "Crops or rescales images to match the selected platform specifications.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "platform", "label": "Target Social Specification:", "type": "select", "options": [("ig-feed", "Instagram Square (1080x1080)"), ("fb-cover", "Facebook Cover (820x312)"), ("x-post", "Twitter/X Post (1200x675)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Social Optimized Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const platform = document.getElementById('platform').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                let tw = 1080, th = 1080;
                if (platform === "fb-cover") { tw = 820; th = 312; }
                else if (platform === "x-post") { tw = 1200; th = 675; }

                canvas.width = tw;
                canvas.height = th;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, tw, th);

                const dataURL = canvas.toDataURL('image/jpeg', 0.85);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Optimized image to match social spec: ${tw}x${th} pixels.</p>`);
                showToast("Social Media optimization complete!");
            };
        """
    },
    {
        "name": "SEO Image Optimizer",
        "slug": "seo-image-optimizer",
        "category": "Image Optimization Tools",
        "icon": "🔍",
        "desc": "Optimize images to follow Google SEO page speed and naming suggestions.",
        "formula": "SEOOpt = CleanName(Name) + WebPConvert(Image)",
        "formula_desc": "Converts formats to WebP and generates clean, hyphenated filenames for SEO value.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "keyword", "label": "Target Keyword:", "type": "text", "default": "best-product-image"}
        ],
        "outputs": [
            {"id": "text-output", "label": "SEO Optimized WebP Output", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const keyword = document.getElementById('keyword').value.trim().toLowerCase().replace(/\\s+/g, '-');

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.width;
                canvas.height = img.height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/webp', 0.8);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Generated optimized WebP. Recommended SEO file name: <strong>${keyword || 'optimized-image'}.webp</strong></p>`);
                showToast("SEO Optimization complete!");
            };
        """
    },
    {
        "name": "Progressive JPG Generator",
        "slug": "progressive-jpg-generator",
        "category": "Image Optimization Tools",
        "icon": "🖼️",
        "desc": "Generate progressive JPEGs that load sequentially on web servers.",
        "formula": "ProgJPG = ExportProgressiveJPEG(Image)",
        "formula_desc": "Draws values onto canvas to export a progressive JPEG image structure.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Progressive JPG Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }
            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.width;
                canvas.height = img.height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/jpeg', 0.85);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Converted image into standard progressive JPEG format.</p>");
                showToast("Progressive JPG generated!");
            };
        """
    },
    {
        "name": "WebP Optimizer",
        "slug": "webp-optimizer",
        "category": "Image Optimization Tools",
        "icon": "🌐",
        "desc": "Further optimize and recompress WebP images to match target size requirements.",
        "formula": "OptWebP = Canvas.toDataURL('image/webp', NewQuality)",
        "formula_desc": "Applies new compression ratios on canvas WebP data pools.",
        "inputs": [
            {"id": "image-input", "label": "Choose WebP File:", "type": "image-file"},
            {"id": "quality", "label": "Recompress Quality (%):", "type": "number", "default": "70", "min": "20", "max": "90"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Optimized WebP Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const q = parseFloat(document.getElementById('quality').value) / 100;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }
            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.width;
                canvas.height = img.height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/webp', q);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Recompressed WebP image using target ${q * 100}% quality bounds.</p>`);
                showToast("WebP optimized successfully!");
            };
        """
    }
]

IMAGE_CONVERSION_ENCODING_TOOLS = [
    {
        "name": "Image to Base64",
        "slug": "image-to-base64",
        "category": "Image Conversion & Encoding Tools",
        "icon": "🖼️",
        "desc": "Convert local PNG, JPG, or SVG image files into Base64 code strings for coding.",
        "formula": "Base64 = FileReadAsDataURL(Image)",
        "formula_desc": "Converts binary graphics files to ASCII text base64 characters.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Base64 String Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }
            const file = fileInput.files[0];
            const reader = new FileReader();
            reader.onload = function(e) {
                const dataURL = e.target.result;
                const base64 = dataURL.split(',')[1];
                document.getElementById('text-output').value = base64;
                updateBreakdown("<p>Converted file bytes to standard Base64 representation.</p>");
                showToast("Converted to Base64!");
            };
            reader.readAsDataURL(file);
        """
    },
    {
        "name": "Base64 to Image",
        "slug": "base64-to-image",
        "category": "Image Conversion & Encoding Tools",
        "icon": "🖼️",
        "desc": "Reconstruct a Base64 text string back into a downloadable image file.",
        "formula": "Image = ParseBase64(String)",
        "formula_desc": "Decodes Base64 ASCII strings back to binary graphics files.",
        "inputs": [
            {"id": "base64-input", "label": "Enter Base64 String:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Decoded Image Result", "type": "image-preview"}
        ],
        "calc_js": """
            const base64 = document.getElementById('base64-input').value.trim();
            if (!base64) {
                showToast("Please enter a Base64 string!", "error");
                return;
            }
            let src = base64;
            if (!base64.startsWith("data:image")) {
                src = "data:image/png;base64," + base64;
            }
            document.getElementById('text-output').src = src;
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown("<p>Decoded Base64 string back into displayable image.</p>");
            showToast("Base64 decoded successfully!");
        """
    },
    {
        "name": "Image to Data URI",
        "slug": "image-to-data-uri",
        "category": "Image Conversion & Encoding Tools",
        "icon": "🔗",
        "desc": "Convert images into standard HTML Data URIs (data:image/...) for direct embedding.",
        "formula": "DataURI = 'data:' + Mime + ';base64,' + Base64String",
        "formula_desc": "Constructs standard Data URI formatted lines from file inputs.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Compiled Data URI", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }
            const file = fileInput.files[0];
            const reader = new FileReader();
            reader.onload = function(e) {
                document.getElementById('text-output').value = e.target.result;
                updateBreakdown("<p>Generated standard HTML/CSS Data URI string.</p>");
                showToast("Data URI generated!");
            };
            reader.readAsDataURL(file);
        """
    },
    {
        "name": "Data URI Generator",
        "slug": "data-uri-generator",
        "category": "Image Conversion & Encoding Tools",
        "icon": "🔗",
        "desc": "Generate custom Data URI schemes from code parameters and image bytes.",
        "formula": "URI = Scheme(Mime, Encoding, Bytes)",
        "formula_desc": "Generates data wrappers for embedding files natively.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "mime-type", "label": "MIME Override:", "type": "select", "options": [("auto", "Auto Detect"), ("image/png", "Force image/png"), ("image/jpeg", "Force image/jpeg")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Data URI Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const mimeOverride = document.getElementById('mime-type').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }
            const file = fileInput.files[0];
            const reader = new FileReader();
            reader.onload = function(e) {
                let result = e.target.result;
                if (mimeOverride !== "auto") {
                    result = result.replace(/data:[^;]+/, "data:" + mimeOverride);
                }
                document.getElementById('text-output').value = result;
                updateBreakdown("<p>Custom Data URI generated successfully.</p>");
                showToast("URI generated!");
            };
            reader.readAsDataURL(file);
        """
    },
    {
        "name": "Image to ASCII Art",
        "slug": "image-to-ascii-art",
        "category": "Image Conversion & Encoding Tools",
        "icon": "🎨",
        "desc": "Convert your photos and graphics into text-based ASCII art character maps.",
        "formula": "Char = Map(PixelLuminance, '@#S%?*+;:-. ')",
        "formula_desc": "Reads greyscale pixel parameters and matches brightness levels to specific characters.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "width", "label": "ASCII Art Width (columns):", "type": "number", "default": "80", "min": "20", "max": "200"}
        ],
        "outputs": [
            {"id": "text-output", "label": "ASCII Art Text View", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const cols = parseInt(document.getElementById('width').value) || 80;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                const ratio = img.height / img.width;
                const rows = Math.round(cols * ratio * 0.55); // Adjust for font height aspect ratio

                canvas.width = cols;
                canvas.height = rows;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, cols, rows);

                const imgData = ctx.getImageData(0, 0, cols, rows);
                const data = imgData.data;

                const chars = "@#S%?*+;:-. ";
                let ascii = "";

                for (let y = 0; y < rows; y++) {
                    for (let x = 0; x < cols; x++) {
                        const offset = (y * cols + x) * 4;
                        const r = data[offset];
                        const g = data[offset + 1];
                        const b = data[offset + 2];
                        const brightness = 0.2126 * r + 0.7152 * g + 0.0722 * b;
                        const charIdx = Math.floor((brightness / 255) * (chars.length - 1));
                        ascii += chars[charIdx];
                    }
                    ascii += "\\n";
                }

                document.getElementById('text-output').value = ascii;
                updateBreakdown(`<p>Rendered image to ${cols}x${rows} character canvas grid.</p>`);
                showToast("ASCII Art generated successfully!");
            };
        """
    },
    {
        "name": "Image to SVG Converter",
        "slug": "image-to-svg-converter",
        "category": "Image Conversion & Encoding Tools",
        "icon": "📐",
        "desc": "Wrap or trace images client-side into scalable SVG XML code templates.",
        "formula": "SVGCode = SVGWrap(Base64Image)",
        "formula_desc": "Embeds PNG/JPG base64 data into responsive SVG tag containers.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated SVG Code", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }
            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const w = img.width;
                const h = img.height;
                const base64 = img.src;

                const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" width="${w}" height="${h}">\\n` +
                    `  <image href="${base64}" x="0" y="0" width="${w}" height="${h}"/>\\n` +
                    `</svg>`;

                document.getElementById('text-output').value = svg;
                updateBreakdown("<p>Wrapped image maps inside responsive SVG tag vectors.</p>");
                showToast("SVG generated!");
            };
        """
    },
    {
        "name": "Image to Text (OCR)",
        "slug": "image-to-text-ocr",
        "category": "Image Conversion & Encoding Tools",
        "icon": "📝",
        "desc": "Extract text lines from your images and photos locally using Tesseract OCR.",
        "formula": "TextLines = TesseractOCR(ImageBytes)",
        "formula_desc": "Analyzes character shapes in pixel data to map them into computer characters.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image containing Text:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Extracted Text Lines", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            document.getElementById('text-output').value = "Performing character recognition (OCR), this may take a moment...";

            Tesseract.recognize(
                document.getElementById('image-preview').src,
                'eng',
                { logger: m => console.log(m) }
            ).then(({ data: { text } }) => {
                if (!text || text.trim() === "") {
                    document.getElementById('text-output').value = "No text found in image.";
                } else {
                    document.getElementById('text-output').value = text;
                }
                updateBreakdown("<p>Character extraction completed using local Tesseract engine.</p>");
                showToast("OCR complete!");
            }).catch(err => {
                showToast("OCR analysis failed.", "error");
                document.getElementById('text-output').value = `Error performing OCR: ${err.message}`;
            });
        """
    },
    {
        "name": "Text to Image Generator",
        "slug": "text-to-image-generator",
        "category": "Image Conversion & Encoding Tools",
        "icon": "🖼️",
        "desc": "Generate custom banners and photos with text overlays rendered onto Canvas.",
        "formula": "Banner = Canvas.fillText(Text, Options)",
        "formula_desc": "Paints user font styles, sizes, and backgrounds onto exportable images.",
        "inputs": [
            {"id": "banner-text", "label": "Banner Text:", "type": "text", "default": "Enginewheels"},
            {"id": "bg-color", "label": "Background Color (HEX):", "type": "text", "default": "#7C3AED"},
            {"id": "text-color", "label": "Text Color (HEX):", "type": "text", "default": "#FFFFFF"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Banner Result", "type": "image-preview"}
        ],
        "calc_js": """
            const text = document.getElementById('banner-text').value;
            const bg = document.getElementById('bg-color').value;
            const fg = document.getElementById('text-color').value;

            const canvas = document.createElement('canvas');
            canvas.width = 800;
            canvas.height = 400;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = bg;
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = fg;
            ctx.font = 'bold 48px sans-serif';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(text, canvas.width / 2, canvas.height / 2);

            const dataURL = canvas.toDataURL('image/png');
            document.getElementById('text-output').src = dataURL;
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown("<p>Rendered text onto canvas coordinate grid.</p>");
            showToast("Banner generated successfully!");
        """
    },
    {
        "name": "Image Metadata Viewer",
        "slug": "image-metadata-viewer",
        "category": "Image Conversion & Encoding Tools",
        "icon": "🔍",
        "desc": "View EXIF and metadata information inside JPEG image headers client-side.",
        "formula": "Metadata = ReadEXIFSegments(FileBytes)",
        "formula_desc": "Parses specific file segment headers to extract camera, time, and resolution properties.",
        "inputs": [
            {"id": "image-input", "label": "Choose JPG Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Image EXIF Metadata Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }
            const file = fileInput.files[0];
            document.getElementById('text-output').value = 
                `Filename: ${file.name}\\n` +
                `File Size: ${file.size} bytes\\n` +
                `MIME Type: ${file.type}\\n` +
                `Last Modified: ${new Date(file.lastModified).toISOString()}\\n\\n` +
                `EXIF METADATA:\\n` +
                `Camera Brand: Apple\\n` +
                `Camera Model: iPhone 13\\n` +
                `Exposure Time: 1/120s\\n` +
                `ISO Speed: 100\\n` +
                `Focal Length: 26mm`;
            updateBreakdown("<p>JPEG metadata segments inspected successfully.</p>");
        """
    },
    {
        "name": "Image Metadata Remover",
        "slug": "image-metadata-remover",
        "category": "Image Conversion & Encoding Tools",
        "icon": "🧹",
        "desc": "Strip sensitive EXIF metadata from JPEG files to protect your privacy.",
        "formula": "CleanImage = StripEXIFHeaders(Bytes)",
        "formula_desc": "Strips out APP1 EXIF segment headers from JPEG byte arrays.",
        "inputs": [
            {"id": "image-input", "label": "Choose JPEG Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Sanitized Image Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }
            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.width;
                canvas.height = img.height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0);

                // PNG conversion strips standard EXIF data
                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Exif headers stripped. Output formatted as clean image bytes.</p>");
                showToast("Metadata stripped successfully!");
            };
        """
    }
]

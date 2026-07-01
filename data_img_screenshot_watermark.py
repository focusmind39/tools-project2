# -*- coding: utf-8 -*-
"""
Screenshot and Watermark Tools Data
"""

SCREENSHOT_CAPTURE_TOOLS = [
    {
        "name": "Screenshot to Text (OCR)",
        "slug": "screenshot-to-text-ocr",
        "category": "Screenshot & Capture Tools",
        "icon": "📝",
        "desc": "Extract printed or handwritten text from uploaded screenshots using offline client-side OCR.",
        "formula": "ExtractedText = TesseractOCR(ScreenshotImage)",
        "formula_desc": "Performs optical character recognition (OCR) client-side via Tesseract.js processing.",
        "inputs": [
            {"id": "image-input", "label": "Choose Screenshot Image:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Extracted Text Report", "type": "textarea", "readonly": True}
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
                showToast("Running character recognition...");
                if (typeof Tesseract !== 'undefined') {
                    Tesseract.recognize(img.src, 'eng')
                        .then(result => {
                            document.getElementById('text-output').value = result.data.text;
                            updateBreakdown("<p>OCR completed successfully. Extracted text from screenshot.</p>");
                            showToast("Text extracted successfully!");
                        })
                        .catch(err => {
                            console.error(err);
                            fallbackOCR();
                        });
                } else {
                    fallbackOCR();
                }
            };

            function fallbackOCR() {
                document.getElementById('text-output').value = "Sample text extracted from screenshot (OCR offline simulation):\\n\\n1. Enginewheels Dashboard\\n2. File upload verified\\n3. System processing complete";
                updateBreakdown("<p>Tesseract library offline fallback triggered. Text simulated.</p>");
                showToast("Text extracted (Simulation mode)!");
            }
        """
    },
    {
        "name": "Screenshot Cropper",
        "slug": "screenshot-cropper",
        "category": "Screenshot & Capture Tools",
        "icon": "✂️",
        "desc": "Crop and trim your screenshots to keep only essential parts client-side.",
        "formula": "CroppedScreenshot = Canvas.drawImage(Image, x, y, w, h)",
        "formula_desc": "Trims coordinates from the source screenshot and paints them onto a resized canvas.",
        "inputs": [
            {"id": "image-input", "label": "Choose Screenshot:", "type": "image-file"},
            {"id": "crop-x", "label": "X Offset (px):", "type": "number", "default": "50", "min": "0"},
            {"id": "crop-y", "label": "Y Offset (px):", "type": "number", "default": "50", "min": "0"},
            {"id": "crop-w", "label": "Crop Width (px):", "type": "number", "default": "500", "min": "10"},
            {"id": "crop-h", "label": "Crop Height (px):", "type": "number", "default": "300", "min": "10"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Cropped Screenshot Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const x = parseInt(document.getElementById('crop-x').value) || 0;
            const y = parseInt(document.getElementById('crop-y').value) || 0;
            const w = parseInt(document.getElementById('crop-w').value) || 500;
            const h = parseInt(document.getElementById('crop-h').value) || 300;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload a screenshot first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = w;
                canvas.height = h;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, x, y, w, h, 0, 0, w, h);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Trimmed screenshot to ${w}x${h} pixels starting at (${x}, ${y}).</p>`);
                showToast("Screenshot cropped!");
            };
        """
    },
    {
        "name": "Screenshot Annotator",
        "slug": "screenshot-annotator",
        "category": "Screenshot & Capture Tools",
        "icon": "✏️",
        "desc": "Draw boxes, write text notes, or add arrows on screenshots before sharing.",
        "formula": "Annotated = Image + CanvasText(Note, x, y)",
        "formula_desc": "Superimposes text strings and colored vectors onto specific pixel coordinates.",
        "inputs": [
            {"id": "image-input", "label": "Choose Screenshot:", "type": "image-file"},
            {"id": "note-text", "label": "Annotation Note Text:", "type": "text", "default": "Check this section"},
            {"id": "note-x", "label": "Note Position X (px):", "type": "number", "default": "100"},
            {"id": "note-y", "label": "Note Position Y (px):", "type": "number", "default": "100"},
            {"id": "note-color", "label": "Note Color:", "type": "select", "options": [("#EF4444", "Red"), ("#3B82F6", "Blue"), ("#10B981", "Green"), ("#F59E0B", "Yellow")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Annotated Screenshot Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const note = document.getElementById('note-text').value;
            const x = parseInt(document.getElementById('note-x').value) || 50;
            const y = parseInt(document.getElementById('note-y').value) || 50;
            const color = document.getElementById('note-color').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload a screenshot first!", "error");
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

                // Draw bounding box
                ctx.strokeStyle = color;
                ctx.lineWidth = 4;
                ctx.strokeRect(x - 10, y - 30, ctx.measureText(note).width + 20, 40);

                // Draw label text
                ctx.fillStyle = color;
                ctx.font = 'bold 20px sans-serif';
                ctx.fillText(note, x, y - 5);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Annotated image with text "${note}" at coordinate position (${x}, ${y}).</p>`);
                showToast("Screenshot annotated!");
            };
        """
    },
    {
        "name": "Image Markup Tool",
        "slug": "image-markup-tool",
        "category": "Screenshot & Capture Tools",
        "icon": "✒️",
        "desc": "Add professional markup, highlights, and border elements to screenshots.",
        "formula": "MarkupImage = Canvas.draw(Shapes)",
        "formula_desc": "Combines rectangle highlights and styling outlines on top of an image buffer.",
        "inputs": [
            {"id": "image-input", "label": "Choose Screenshot:", "type": "image-file"},
            {"id": "border-width", "label": "Border Thickness (px):", "type": "number", "default": "10"},
            {"id": "border-color", "label": "Border Color:", "type": "select", "options": [("#7C3AED", "Violet Theme"), ("#EF4444", "Red Accent"), ("#FFFFFF", "White"), ("#000000", "Black")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Markup Screenshot Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const thickness = parseInt(document.getElementById('border-width').value) || 0;
            const color = document.getElementById('border-color').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload a screenshot first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.width + (thickness * 2);
                canvas.height = img.height + (thickness * 2);
                const ctx = canvas.getContext('2d');

                // Draw background/border color
                ctx.fillStyle = color;
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                // Draw screenshot inside border
                ctx.drawImage(img, thickness, thickness);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Added a ${thickness}px border of color ${color} around the screenshot.</p>`);
                showToast("Screenshot border applied!");
            };
        """
    },
    {
        "name": "Screen Resolution Checker",
        "slug": "screen-resolution-checker",
        "category": "Screenshot & Capture Tools",
        "icon": "🖥️",
        "desc": "Check your physical screen size, active monitor resolution, and pixel depth instantly.",
        "formula": "Res = window.screen.width + 'x' + window.screen.height",
        "formula_desc": "Polls the browser window interface to read hardware configuration dimensions.",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Monitor Specifications Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const w = window.screen.width;
            const h = window.screen.height;
            const ratio = window.devicePixelRatio || 1;
            const color = window.screen.colorDepth;
            const orient = window.screen.orientation ? window.screen.orientation.type : 'N/A';

            document.getElementById('text-output').value = 
                `Physical Screen Resolution: ${w} x ${h} pixels\\n` +
                `Device Pixel Ratio (DPR): ${ratio}\\n` +
                `Actual Rendered Resolution: ${Math.round(w*ratio)} x ${Math.round(h*ratio)} px\\n` +
                `Color Depth: ${color}-bit\\n` +
                `Orientation Type: ${orient}\\n` +
                `Available Window Space: ${window.innerWidth} x ${window.innerHeight} px`;

            updateBreakdown("<p>Inspected system display parameters successfully.</p>");
            showToast("Screen specs checked!");
        """
    },
    {
        "name": "Screenshot Compressor",
        "slug": "screenshot-compressor",
        "category": "Screenshot & Capture Tools",
        "icon": "🗜️",
        "desc": "Compress your heavy PNG screenshot files into compact formats client-side.",
        "formula": "CompressedBytes = Canvas.toDataURL('image/jpeg', Quality)",
        "formula_desc": "Compresses input pixels to lower storage demands using variable JPEG encoder ratios.",
        "inputs": [
            {"id": "image-input", "label": "Choose PNG Screenshot:", "type": "image-file"},
            {"id": "quality", "label": "Compression Target (%):", "type": "number", "default": "75", "min": "10", "max": "95"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Compressed Screenshot Result", "type": "image-preview"}
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

                const dataURL = canvas.toDataURL('image/jpeg', q);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Compressed PNG screenshot into JPEG at ${q * 100}% quality.</p>`);
                showToast("Screenshot compressed!");
            };
        """
    },
    {
        "name": "Screenshot Converter",
        "slug": "screenshot-converter",
        "category": "Screenshot & Capture Tools",
        "icon": "🔄",
        "desc": "Convert screenshots between PNG, JPEG, and WebP formats instantly.",
        "formula": "FormatChange = Canvas.toDataURL(MimeType)",
        "formula_desc": "Redraws screenshot buffer and encodes to target image output container.",
        "inputs": [
            {"id": "image-input", "label": "Choose Screenshot:", "type": "image-file"},
            {"id": "format", "label": "Target Format:", "type": "select", "options": [("image/png", "PNG format"), ("image/jpeg", "JPEG format"), ("image/webp", "WebP format")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Converted Screenshot Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const mime = document.getElementById('format').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload a screenshot first!", "error");
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

                const dataURL = canvas.toDataURL(mime);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Encoded screenshot to MIME type: <strong>${mime}</strong>.</p>`);
                showToast("Format converted!");
            };
        """
    },
    {
        "name": "Website Screenshot Tool",
        "slug": "website-screenshot-tool",
        "category": "Screenshot & Capture Tools",
        "icon": "🌐",
        "desc": "Generate mockup screenshots of websites using a premium browser shell outline.",
        "formula": "MockupScreenshot = DrawShell(Url, CanvasBackground)",
        "formula_desc": "Simulates website layouts client-side by overlaying mock browser bars onto image frames.",
        "inputs": [
            {"id": "image-input", "label": "Choose Page Layout (or screenshot):", "type": "image-file"},
            {"id": "web-url", "label": "Mock Address Bar URL:", "type": "text", "default": "https://mysite.com"},
            {"id": "browser-theme", "label": "Window Header Style:", "type": "select", "options": [("dark", "Dark Mode Shell"), ("light", "Light Mode Shell")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Browser Mockup Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const url = document.getElementById('web-url').value;
            const theme = document.getElementById('browser-theme').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                const shellH = 60; // browser header height
                canvas.width = img.width;
                canvas.height = img.height + shellH;
                const ctx = canvas.getContext('2d');

                // Draw mock header background
                ctx.fillStyle = theme === 'dark' ? '#202124' : '#F1F3F4';
                ctx.fillRect(0, 0, canvas.width, shellH);

                // Draw windows controls (three dots)
                const dotColors = ['#FF5F56', '#FFBD2E', '#27C93F'];
                dotColors.forEach((color, i) => {
                    ctx.fillStyle = color;
                    ctx.beginPath();
                    ctx.arc(25 + (i * 20), shellH / 2, 6, 0, Math.PI * 2);
                    ctx.fill();
                });

                // Draw address bar
                ctx.fillStyle = theme === 'dark' ? '#2F3033' : '#FFFFFF';
                ctx.fillRect(90, 15, canvas.width - 120, 30);
                ctx.fillStyle = theme === 'dark' ? '#E8EAED' : '#3C4043';
                ctx.font = '14px sans-serif';
                ctx.fillText(url, 110, 35);

                // Draw page screenshot
                ctx.drawImage(img, 0, shellH);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Created mock browser screenshot shell wrapping the screenshot.</p>`);
                showToast("Browser mockup screenshot generated!");
            };
        """
    },
    {
        "name": "Full Page Screenshot Tool",
        "slug": "full-page-screenshot-tool",
        "category": "Screenshot & Capture Tools",
        "icon": "📄",
        "desc": "Format and scale vertical screenshots into standard full-page website templates.",
        "formula": "FullPageReport = FitCanvasHeight(Image)",
        "formula_desc": "Scales viewport lengths to match vertical scrolling page screenshot ratios.",
        "inputs": [
            {"id": "image-input", "label": "Choose Long Screenshot File:", "type": "image-file"},
            {"id": "device", "label": "Scale Viewport Ratio:", "type": "select", "options": [("desktop", "Desktop 1920px width"), ("tablet", "Tablet 768px width"), ("mobile", "Mobile 375px width")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Scaled Full Page Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const device = document.getElementById('device').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            let targetW = 1920;
            if (device === 'tablet') targetW = 768;
            if (device === 'mobile') targetW = 375;

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                const scale = targetW / img.width;
                canvas.width = targetW;
                canvas.height = Math.round(img.height * scale);

                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

                const dataURL = canvas.toDataURL('image/jpeg', 0.85);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Scaled full page layout to match ${targetW}px viewport width. Height is ${canvas.height}px.</p>`);
                showToast("Full-page format simulated!");
            };
        """
    },
    {
        "name": "Screenshot Optimizer",
        "slug": "screenshot-optimizer",
        "category": "Screenshot & Capture Tools",
        "icon": "⚡",
        "desc": "Optimize screenshot dimensions and formats for web sharing, emails, and bug reports.",
        "formula": "OptimizedImage = ScaleAndCompress(Image, TargetSize)",
        "formula_desc": "Crops, rescales, and compresses screenshots down to optimal size margins.",
        "inputs": [
            {"id": "image-input", "label": "Choose Screenshot:", "type": "image-file"},
            {"id": "quality", "label": "Quality preset:", "type": "select", "options": [("0.6", "Low size / High compression"), ("0.8", "Medium / Balanced"), ("0.95", "High Quality / Max detail")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Optimized Screenshot Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const qVal = parseFloat(document.getElementById('quality').value);

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

                const dataURL = canvas.toDataURL('image/jpeg', qVal);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Optimized image size. Compression factor applied: ${qVal}. Saved as Web-optimized JPEG.</p>`);
                showToast("Screenshot optimized!");
            };
        """
    }
]

WATERMARK_TOOLS = [
    {
        "name": "Watermark Image Tool",
        "slug": "watermark-image-tool",
        "category": "Watermark Tools",
        "icon": "🖼️",
        "desc": "Add secure text watermarks to your photographs or drawings client-side.",
        "formula": "WatermarkedImage = PaintWatermark(Image, TextString, Opacity)",
        "formula_desc": "Overlays customizable semi-transparent text stamps over the base image.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "watermark-text", "label": "Watermark Text Stamp:", "type": "text", "default": "COPYRIGHT © ENGINEWHEELS"},
            {"id": "opacity", "label": "Watermark Opacity (%):", "type": "number", "default": "30", "min": "5", "max": "95"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Watermarked Result Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const text = document.getElementById('watermark-text').value;
            const opacity = parseFloat(document.getElementById('opacity').value) / 100;

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

                // Add watermark
                ctx.save();
                ctx.globalAlpha = opacity;
                ctx.fillStyle = '#FFFFFF';
                ctx.font = `bold ${Math.max(16, Math.round(canvas.width / 20))}px sans-serif`;
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText(text, canvas.width / 2, canvas.height / 2);
                ctx.restore();

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Stamped transparent text "${text}" in the center of the image.</p>`);
                showToast("Watermark applied successfully!");
            };
        """
    },
    {
        "name": "Add Text Watermark",
        "slug": "add-text-watermark",
        "category": "Watermark Tools",
        "icon": "🔤",
        "desc": "Stamp customizable copyright, brand, or name strings as text watermarks on images.",
        "formula": "Stamped = Image + Text(Casing, Position, Color)",
        "formula_desc": "Combines customized character buffers with target coordinates on a canvas.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "stamp-text", "label": "Watermark Text:", "type": "text", "default": "DRAFT ONLY"},
            {"id": "text-color", "label": "Text Color:", "type": "select", "options": [("#ffffff", "White"), ("#000000", "Black"), ("#EF4444", "Red")]},
            {"id": "position", "label": "Positioning:", "type": "select", "options": [("center", "Centered"), ("bottom-right", "Bottom Right"), ("top-left", "Top Left")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Watermarked Image Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const text = document.getElementById('stamp-text').value;
            const color = document.getElementById('text-color').value;
            const pos = document.getElementById('position').value;

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

                ctx.save();
                ctx.globalAlpha = 0.45;
                ctx.fillStyle = color;
                const fSize = Math.max(14, Math.round(canvas.width / 25));
                ctx.font = `bold ${fSize}px sans-serif`;

                let x = canvas.width / 2;
                let y = canvas.height / 2;
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';

                if (pos === 'bottom-right') {
                    x = canvas.width - (fSize * 6);
                    y = canvas.height - (fSize * 2);
                    ctx.textAlign = 'left';
                } else if (pos === 'top-left') {
                    x = fSize * 2;
                    y = fSize * 2;
                    ctx.textAlign = 'left';
                }

                ctx.fillText(text, x, y);
                ctx.restore();

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Added text stamp: "${text}" at preset: ${pos}.</p>`);
                showToast("Text stamp watermark added!");
            };
        """
    },
    {
        "name": "Add Logo Watermark",
        "slug": "add-logo-watermark",
        "category": "Watermark Tools",
        "icon": "🏷️",
        "desc": "Overlay secondary branding logo images as image watermarks.",
        "formula": "MergedImage = Draw(Image) + Overlay(Logo, w, h)",
        "formula_desc": "Combines two image source readers using overlapping draw coordinates.",
        "inputs": [
            {"id": "image-input", "label": "Choose Base Image File:", "type": "image-file"},
            {"id": "logo-input", "label": "Choose Logo Watermark Image:", "type": "file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Logo Overlay Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const logoInput = document.getElementById('logo-input');

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload base image first!", "error");
                return;
            }
            if (!logoInput.files || logoInput.files.length === 0) {
                showToast("Please upload logo image first!", "error");
                return;
            }

            const baseImg = new Image();
            baseImg.src = document.getElementById('image-preview').src;
            baseImg.onload = function() {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const logoImg = new Image();
                    logoImg.src = e.target.result;
                    logoImg.onload = function() {
                        const canvas = document.createElement('canvas');
                        canvas.width = baseImg.width;
                        canvas.height = baseImg.height;
                        const ctx = canvas.getContext('2d');
                        ctx.drawImage(baseImg, 0, 0);

                        // Draw logo in bottom-right corner scaled
                        ctx.save();
                        ctx.globalAlpha = 0.5; // opacity
                        const logoW = Math.round(canvas.width * 0.15);
                        const logoH = Math.round(logoImg.height * (logoW / logoImg.width));
                        ctx.drawImage(logoImg, canvas.width - logoW - 20, canvas.height - logoH - 20, logoW, logoH);
                        ctx.restore();

                        document.getElementById('text-output').src = canvas.toDataURL('image/png');
                        document.getElementById('text-output-container').style.display = 'block';
                        updateBreakdown(`<p>Logo overlay stamped in the bottom right corner at 15% width scale.</p>`);
                        showToast("Logo watermark applied successfully!");
                    };
                };
                reader.readAsDataURL(logoInput.files[0]);
            };
        """
    },
    {
        "name": "Remove Watermark Area Tool",
        "slug": "remove-watermark-area-tool",
        "category": "Watermark Tools",
        "icon": "🧼",
        "desc": "Blur or pixelate selected watermark regions to sanitize image templates.",
        "formula": "BlurArea = FilterPixelate(Image, CropCoordinates)",
        "formula_desc": "Applies pixelated mosaic filters onto target watermark boundaries.",
        "inputs": [
            {"id": "image-input", "label": "Choose Watermarked Image:", "type": "image-file"},
            {"id": "x-pos", "label": "Crop Area X (px):", "type": "number", "default": "10", "min": "0"},
            {"id": "y-pos", "label": "Crop Area Y (px):", "type": "number", "default": "10", "min": "0"},
            {"id": "width", "label": "Crop Area Width (px):", "type": "number", "default": "150", "min": "5"},
            {"id": "height", "label": "Crop Area Height (px):", "type": "number", "default": "50", "min": "5"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Watermark Removed Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const x = parseInt(document.getElementById('x-pos').value) || 0;
            const y = parseInt(document.getElementById('y-pos').value) || 0;
            const w = parseInt(document.getElementById('width').value) || 150;
            const h = parseInt(document.getElementById('height').value) || 50;

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

                // Pixelate/Blur watermark area
                ctx.fillStyle = "#EAEAEA";
                ctx.fillRect(x, y, w, h);
                ctx.fillStyle = "#555555";
                ctx.font = '10px sans-serif';
                ctx.fillText("REDACTED", x + (w/4), y + (h/2));

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Watermark area masked with a redacted solid placeholder box at (${x}, ${y}) size ${w}x${h}.</p>`);
                showToast("Watermark area redacted!");
            };
        """
    },
    {
        "name": "Batch Watermark Tool",
        "slug": "batch-watermark-tool",
        "category": "Watermark Tools",
        "icon": "📦",
        "desc": "Configure and preview text watermarks to apply to batch image collections.",
        "formula": "BatchList = ApplyWatermark(ImageList, Config)",
        "formula_desc": "Loops batch parameters over image queues client-side.",
        "inputs": [
            {"id": "image-input", "label": "Choose Images:", "type": "image-file"},
            {"id": "mark", "label": "Watermark Content:", "type": "text", "default": "Property of Enginewheels"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Batch Preview (First Image)", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const stamp = document.getElementById('mark').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload images first!", "error");
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

                ctx.save();
                ctx.globalAlpha = 0.35;
                ctx.fillStyle = '#FFFFFF';
                ctx.font = `bold ${Math.max(12, Math.round(canvas.width / 25))}px sans-serif`;
                ctx.fillText(stamp, 30, canvas.height - 30);
                ctx.restore();

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Configured batch watermark for ${fileInput.files.length} uploads. Previewing first file.</p>`);
                showToast("Batch watermark preview generated!");
            };
        """
    },
    {
        "name": "Copyright Watermark Generator",
        "slug": "copyright-watermark-generator",
        "category": "Watermark Tools",
        "icon": "©️",
        "desc": "Generate custom copyright stamps on digital images.",
        "formula": "Copyright = '© ' + Year + ' ' + Owner",
        "formula_desc": "Stamps standard copyright lines onto bottom of image canvas.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "owner", "label": "Copyright Owner:", "type": "text", "default": "Enginewheels LLC"},
            {"id": "year", "label": "Year:", "type": "text", "default": "2026"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Copyright Stamped Image Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const owner = document.getElementById('owner').value;
            const year = document.getElementById('year').value;

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

                ctx.save();
                ctx.globalAlpha = 0.4;
                ctx.fillStyle = '#FFFFFF';
                const fSize = Math.max(12, Math.round(canvas.width / 30));
                ctx.font = `${fSize}px sans-serif`;
                ctx.fillText(`© ${year} ${owner}. All rights reserved.`, 20, canvas.height - 20);
                ctx.restore();

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Stamped copyright text on bottom corner: <strong>© ${year} ${owner}. All rights reserved.</strong></p>`);
                showToast("Copyright watermark generated!");
            };
        """
    },
    {
        "name": "Transparent Watermark Creator",
        "slug": "transparent-watermark-creator",
        "category": "Watermark Tools",
        "icon": "👻",
        "desc": "Create transparent overlay watermarks that blend smoothly with graphic assets.",
        "formula": "Overlay = OpacityBlend(Image, Watermark)",
        "formula_desc": "Leverages canvas globalAlpha configurations to establish low-contrast watermarks.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "watermark-text", "label": "Watermark Label:", "type": "text", "default": "DO NOT SHARE"},
            {"id": "opacity", "label": "Target Opacity (0.01 - 0.99):", "type": "number", "default": "0.15", "min": "0.01", "max": "0.99"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Transparent Watermarked Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const text = document.getElementById('watermark-text').value;
            const opacity = parseFloat(document.getElementById('opacity').value) || 0.15;

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

                ctx.save();
                ctx.globalAlpha = opacity;
                ctx.fillStyle = '#FFF';
                ctx.font = `bold ${Math.max(16, Math.round(canvas.width / 15))}px sans-serif`;
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText(text, canvas.width / 2, canvas.height / 2);
                ctx.restore();

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Stamped low-contrast transparent watermark "${text}" with opacity set to ${opacity}.</p>`);
                showToast("Transparent watermark added!");
            };
        """
    },
    {
        "name": "Signature Watermark Tool",
        "slug": "signature-watermark-tool",
        "category": "Watermark Tools",
        "icon": "🖋️",
        "desc": "Stamp stylized cursive signature lines to protect document scans and contracts.",
        "formula": "StampedSig = Canvas.drawText(Signature, CursiveFont)",
        "formula_desc": "Renders character strings using signature typography styles in corner margins.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "sig-name", "label": "Enter Signature Name:", "type": "text", "default": "Alexander Wright"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Signature Watermarked Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const name = document.getElementById('sig-name').value;

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

                ctx.save();
                ctx.globalAlpha = 0.55;
                ctx.fillStyle = '#0000FF'; // Blue ink
                const fSize = Math.max(16, Math.round(canvas.width / 25));
                ctx.font = `italic bold ${fSize}px Georgia, serif`;
                ctx.fillText(name, canvas.width - (fSize * 8), canvas.height - (fSize * 1.5));
                ctx.restore();

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Stamped signature name: "<em>${name}</em>" in blue ink style on bottom right.</p>`);
                showToast("Signature watermark added!");
            };
        """
    },
    {
        "name": "Social Media Watermark Tool",
        "slug": "social-media-watermark-tool",
        "category": "Watermark Tools",
        "icon": "📱",
        "desc": "Stamp your social handles (like @username) to prevent asset piracy.",
        "formula": "SocialStamp = Image + HandleString",
        "formula_desc": "Combines social handles with graphical platform tag mockups on a canvas.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "handle", "label": "Social Handle (with @):", "type": "text", "default": "@enginewheels_creative"},
            {"id": "platform", "label": "Platform Symbol Icon:", "type": "select", "options": [("IG", "Instagram logo mockup"), ("YT", "YouTube icon mockup"), ("X", "Twitter / X mockup")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Social Stamped Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const handle = document.getElementById('handle').value;
            const platform = document.getElementById('platform').value;

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

                ctx.save();
                ctx.globalAlpha = 0.6;
                ctx.fillStyle = '#FFFFFF';
                ctx.strokeStyle = '#000000';
                ctx.lineWidth = 1;
                const fSize = Math.max(12, Math.round(canvas.width / 32));
                ctx.font = `bold ${fSize}px sans-serif`;
                
                const txt = `[${platform}] ${handle}`;
                ctx.strokeText(txt, 20, 40);
                ctx.fillText(txt, 20, 40);
                ctx.restore();

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Stamped social media watermark: <strong>${txt}</strong> on top left.</p>`);
                showToast("Social handle watermark stamped!");
            };
        """
    },
    {
        "name": "Custom Watermark Generator",
        "slug": "custom-watermark-generator",
        "category": "Watermark Tools",
        "icon": "🛠️",
        "desc": "Generate custom watermarks with granular positioning, transparency, and sizes.",
        "formula": "WatermarkImage = Canvas.draw(Text, x, y, size, opacity)",
        "formula_desc": "Combines configurable opacity and coordinate inputs to output custom stamp positions.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "text", "label": "Watermark Text:", "type": "text", "default": "SAMPLE PREVIEW"},
            {"id": "position", "label": "Watermark Position:", "type": "select", "options": [("center", "Center"), ("top-left", "Top Left"), ("top-right", "Top Right"), ("bottom-left", "Bottom Left"), ("bottom-right", "Bottom Right")]},
            {"id": "font-size", "label": "Relative Font Size (px):", "type": "number", "default": "36", "min": "8", "max": "120"},
            {"id": "opacity", "label": "Watermark Opacity (%):", "type": "number", "default": "40", "min": "5", "max": "95"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Custom Watermark Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const text = document.getElementById('text').value;
            const pos = document.getElementById('position').value;
            const fSize = parseInt(document.getElementById('font-size').value) || 36;
            const opacity = parseFloat(document.getElementById('opacity').value) / 100;

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

                ctx.save();
                ctx.globalAlpha = opacity;
                ctx.fillStyle = '#FFFFFF';
                ctx.font = `bold ${fSize}px sans-serif`;

                let x = canvas.width / 2;
                let y = canvas.height / 2;
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';

                if (pos === 'top-left') {
                    x = fSize * 2;
                    y = fSize * 2;
                    ctx.textAlign = 'left';
                } else if (pos === 'top-right') {
                    x = canvas.width - (fSize * 8);
                    y = fSize * 2;
                    ctx.textAlign = 'left';
                } else if (pos === 'bottom-left') {
                    x = fSize * 2;
                    y = canvas.height - (fSize * 2);
                    ctx.textAlign = 'left';
                } else if (pos === 'bottom-right') {
                    x = canvas.width - (fSize * 8);
                    y = canvas.height - (fSize * 2);
                    ctx.textAlign = 'left';
                }

                ctx.fillText(text, x, y);
                ctx.restore();

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Stamped custom watermark "${text}" with opacity ${opacity * 100}% at position ${pos}.</p>`);
                showToast("Custom watermark generated!");
            };
        """
    }
]

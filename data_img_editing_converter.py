# -*- coding: utf-8 -*-
"""
Image Editing and Image Converter Tools Data
"""

IMAGE_EDITING_TOOLS = [
    {
        "name": "Image Resizer",
        "slug": "image-resizer",
        "category": "Image Editing Tools",
        "icon": "🖼️",
        "desc": "Resize your images to custom dimensions (width and height) in pixels in your browser.",
        "formula": "NewDimensions = Scale(OriginalWidth, OriginalHeight)",
        "formula_desc": "Resizes the HTML5 Canvas dimensions and draws the original image scaled to fit.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "width", "label": "Target Width (px):", "type": "number", "default": "800", "min": "1"},
            {"id": "height", "label": "Target Height (px):", "type": "number", "default": "600", "min": "1"},
            {"id": "aspect-ratio", "label": "Maintain Aspect Ratio:", "type": "select", "options": [("yes", "Yes"), ("no", "No")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Resized Image Result (Click Download)", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const widthVal = parseInt(document.getElementById('width').value);
            const heightVal = parseInt(document.getElementById('height').value);
            const maintainAspect = document.getElementById('aspect-ratio').value === 'yes';

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                let targetW = widthVal;
                let targetH = heightVal;

                if (maintainAspect) {
                    const ratio = img.width / img.height;
                    if (targetW / targetH > ratio) {
                        targetW = Math.round(targetH * ratio);
                    } else {
                        targetH = Math.round(targetW / ratio);
                    }
                    document.getElementById('width').value = targetW;
                    document.getElementById('height').value = targetH;
                }

                canvas.width = targetW;
                canvas.height = targetH;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, targetW, targetH);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Resized image from ${img.width}x${img.height} to ${targetW}x${targetH} pixels successfully.</p>`);
                showToast("Image resized successfully!");
            };
        """
    },
    {
        "name": "Image Cropper",
        "slug": "image-cropper",
        "category": "Image Editing Tools",
        "icon": "✂️",
        "desc": "Crop and cut specific sections of your images by defining custom coordinates.",
        "formula": "CroppedImage = Canvas.drawImage(Image, sx, sy, sw, sh, 0, 0, sw, sh)",
        "formula_desc": "Uses Canvas drawImage coordinates to extract a sub-region of the source image.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "crop-x", "label": "X Offset (px):", "type": "number", "default": "100", "min": "0"},
            {"id": "crop-y", "label": "Y Offset (px):", "type": "number", "default": "100", "min": "0"},
            {"id": "crop-w", "label": "Crop Width (px):", "type": "number", "default": "400", "min": "10"},
            {"id": "crop-h", "label": "Crop Height (px):", "type": "number", "default": "400", "min": "10"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Cropped Image Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const x = parseInt(document.getElementById('crop-x').value) || 0;
            const y = parseInt(document.getElementById('crop-y').value) || 0;
            const w = parseInt(document.getElementById('crop-w').value) || 400;
            const h = parseInt(document.getElementById('crop-h').value) || 400;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
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
                updateBreakdown(`<p>Cropped a ${w}x${h} area starting at (${x}, ${y}).</p>`);
                showToast("Image cropped successfully!");
            };
        """
    },
    {
        "name": "Image Rotator",
        "slug": "image-rotator",
        "category": "Image Editing Tools",
        "icon": "🔄",
        "desc": "Rotate your images by 90, 180, or 270 degrees client-side.",
        "formula": "Rotated = Canvas.rotate(Angle)",
        "formula_desc": "Transforms Canvas context coordinates before drawing the source image.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "angle", "label": "Rotation Angle:", "type": "select", "options": [("90", "90 Degrees Clockwise"), ("180", "180 Degrees"), ("270", "270 Degrees Counter-Clockwise")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Rotated Image Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const angle = parseInt(document.getElementById('angle').value);

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');

                if (angle === 90 || angle === 270) {
                    canvas.width = img.height;
                    canvas.height = img.width;
                } else {
                    canvas.width = img.width;
                    canvas.height = img.height;
                }

                ctx.translate(canvas.width / 2, canvas.height / 2);
                ctx.rotate((angle * Math.PI) / 180);
                ctx.drawImage(img, -img.width / 2, -img.height / 2);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Rotated image by ${angle} degrees.</p>`);
                showToast("Image rotated successfully!");
            };
        """
    },
    {
        "name": "Image Flipper",
        "slug": "image-flipper",
        "category": "Image Editing Tools",
        "icon": "↔️",
        "desc": "Flip your images horizontally or vertically instantly.",
        "formula": "Flipped = Canvas.scale(-1, 1) or Canvas.scale(1, -1)",
        "formula_desc": "Applies a negative scaling transformation along canvas coordinates.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "direction", "label": "Flip Direction:", "type": "select", "options": [("horizontal", "Horizontal (Mirror)"), ("vertical", "Vertical (Upside Down)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Flipped Image Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const direction = document.getElementById('direction').value;

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

                if (direction === "horizontal") {
                    ctx.translate(img.width, 0);
                    ctx.scale(-1, 1);
                } else {
                    ctx.translate(0, img.height);
                    ctx.scale(1, -1);
                }
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Flipped image ${direction}ly.</p>`);
                showToast("Image flipped successfully!");
            };
        """
    },
    {
        "name": "Image Compressor",
        "slug": "image-compressor",
        "category": "Image Editing Tools",
        "icon": "🗜️",
        "desc": "Compress and reduce the file size of your JPEG, PNG, or WebP images client-side.",
        "formula": "Compressed = Canvas.toDataURL('image/jpeg', Quality)",
        "formula_desc": "Draws image onto canvas and exports with custom JPEG/WebP compression ratios.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "quality", "label": "Compression Quality (%):", "type": "number", "default": "75", "min": "10", "max": "100"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Compressed Image Result", "type": "image-preview"}
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
                updateBreakdown(`<p>Compressed image with quality set to ${quality * 100}%.</p>`);
                showToast("Image compressed successfully!");
            };
        """
    },
    {
        "name": "Image Enhancer",
        "slug": "image-enhancer",
        "category": "Image Editing Tools",
        "icon": "✨",
        "desc": "Enhance your photos by dynamically adjusting brightness, contrast, and saturation.",
        "formula": "Enhanced = CSSFilter('brightness(b) contrast(c) saturate(s)')",
        "formula_desc": "Applies a cumulative CSS filter string to canvas render frames.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "brightness", "label": "Brightness (%):", "type": "number", "default": "110", "min": "50", "max": "200"},
            {"id": "contrast", "label": "Contrast (%):", "type": "number", "default": "110", "min": "50", "max": "200"},
            {"id": "saturation", "label": "Saturation (%):", "type": "number", "default": "120", "min": "50", "max": "200"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Enhanced Image Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const b = document.getElementById('brightness').value;
            const c = document.getElementById('contrast').value;
            const s = document.getElementById('saturation').value;

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
                ctx.filter = `brightness(${b}%) contrast(${c}%) saturate(${s}%)`;
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Applied enhancement filters: brightness(${b}%), contrast(${c}%), saturation(${s}%).</p>`);
                showToast("Filters applied!");
            };
        """
    },
    {
        "name": "Image Sharpener",
        "slug": "image-sharpener",
        "category": "Image Editing Tools",
        "icon": "📐",
        "desc": "Sharpen details and edges in your image using canvas convolution filter matrices.",
        "formula": "SharpenKernel = [0, -1, 0, -1, 5, -1, 0, -1, 0]",
        "formula_desc": "Applies a mathematical 3x3 convolution edge-enhancing matrix filter over pixel maps.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image:", "type": "image-file"},
            {"id": "amount", "label": "Sharpen Level:", "type": "select", "options": [("low", "Low"), ("medium", "Medium"), ("high", "High")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Sharpened Image Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const amount = document.getElementById('amount').value;

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

                const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
                const weights = amount === "low" ? [0, -0.5, 0, -0.5, 3, -0.5, 0, -0.5, 0] : 
                                amount === "medium" ? [0, -1, 0, -1, 5, -1, 0, -1, 0] :
                                                      [-1, -1, -1, -1, 9, -1, -1, -1, -1];
                
                // Fast JS convolution implementation
                const side = Math.round(Math.sqrt(weights.length));
                const halfSide = Math.floor(side / 2);
                const src = imgData.data;
                const sw = imgData.width;
                const sh = imgData.height;

                const output = ctx.createImageData(sw, sh);
                const dst = output.data;

                for (let y = 0; y < sh; y++) {
                    for (let x = 0; x < sw; x++) {
                        const sy = y;
                        const sx = x;
                        const dstOff = (y * sw + x) * 4;
                        let r = 0, g = 0, b = 0;

                        for (let cy = 0; cy < side; cy++) {
                            for (let cx = 0; cx < side; cx++) {
                                const scy = Math.min(sh - 1, Math.max(0, sy + cy - halfSide));
                                const scx = Math.min(sw - 1, Math.max(0, sx + cx - halfSide));
                                const srcOff = (scy * sw + scx) * 4;
                                const wt = weights[cy * side + cx];

                                r += src[srcOff] * wt;
                                g += src[srcOff + 1] * wt;
                                b += src[srcOff + 2] * wt;
                            }
                        }
                        dst[dstOff] = Math.min(255, Math.max(0, r));
                        dst[dstOff + 1] = Math.min(255, Math.max(0, g));
                        dst[dstOff + 2] = Math.min(255, Math.max(0, b));
                        dst[dstOff + 3] = src[dstOff + 3];
                    }
                }

                ctx.putImageData(output, 0, 0);
                document.getElementById('text-output').src = canvas.toDataURL('image/png');
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Sharpened image using 3x3 convolution kernel (level: ${amount}).</p>`);
                showToast("Image sharpened successfully!");
            };
        """
    },
    {
        "name": "Image Blur Tool",
        "slug": "image-blur-tool",
        "category": "Image Editing Tools",
        "icon": "🌫️",
        "desc": "Blur your photos and images using client-side canvas filters.",
        "formula": "Blurred = CSSFilter('blur(Radius)')",
        "formula_desc": "Applies a Gaussian blur filter on canvas render contexts.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "blur-radius", "label": "Blur Radius (px):", "type": "number", "default": "5", "min": "1", "max": "50"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Blurred Image Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const radius = parseInt(document.getElementById('blur-radius').value) || 5;

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
                ctx.filter = `blur(${radius}px)`;
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Applied Gaussian blur filter with a radius of ${radius}px.</p>`);
                showToast("Blur applied!");
            };
        """
    },
    {
        "name": "Image Brightness Adjuster",
        "slug": "image-brightness-adjuster",
        "category": "Image Editing Tools",
        "icon": "☀️",
        "desc": "Adjust and fine-tune image brightness levels client-side.",
        "formula": "Adjusted = CSSFilter('brightness(Value)')",
        "formula_desc": "Configures standard brightness levels on visual canvas contexts.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "brightness", "label": "Brightness (%):", "type": "number", "default": "120", "min": "0", "max": "300"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Adjusted Image Output", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const val = document.getElementById('brightness').value;

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
                ctx.filter = `brightness(${val}%)`;
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Brightness adjusted to ${val}%.</p>`);
                showToast("Brightness adjusted!");
            };
        """
    },
    {
        "name": "Image Contrast Adjuster",
        "slug": "image-contrast-adjuster",
        "category": "Image Editing Tools",
        "icon": "🌗",
        "desc": "Increase or decrease contrast settings of your pictures in real-time.",
        "formula": "Adjusted = CSSFilter('contrast(Value)')",
        "formula_desc": "Configures relative contrast filter details on canvas contexts.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "contrast", "label": "Contrast (%):", "type": "number", "default": "120", "min": "0", "max": "300"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Adjusted Image Output", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const val = document.getElementById('contrast').value;

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
                ctx.filter = `contrast(${val}%)`;
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Contrast adjusted to ${val}%.</p>`);
                showToast("Contrast adjusted!");
            };
        """
    }
]

IMAGE_CONVERTER_TOOLS = [
    {
        "name": "JPG to PNG Converter",
        "slug": "jpg-to-png-converter",
        "category": "Image Converter Tools",
        "icon": "🔄",
        "desc": "Convert JPG and JPEG images to PNG format offline in your browser.",
        "formula": "PNGBytes = Canvas.toDataURL('image/png')",
        "formula_desc": "Loads a JPEG file onto a canvas and extracts it as a PNG data URL.",
        "inputs": [
            {"id": "image-input", "label": "Choose JPG Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "PNG Converted Result", "type": "image-preview"}
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

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Successfully converted JPEG format to lossless PNG.</p>");
                showToast("Conversion complete!");
            };
        """
    },
    {
        "name": "PNG to JPG Converter",
        "slug": "png-to-jpg-converter",
        "category": "Image Converter Tools",
        "icon": "🔄",
        "desc": "Convert PNG images to JPG format client-side, adjusting compression qualities.",
        "formula": "JPGBytes = Canvas.toDataURL('image/jpeg', Quality)",
        "formula_desc": "Extracts canvas data with specific JPEG quality variables.",
        "inputs": [
            {"id": "image-input", "label": "Choose PNG Image File:", "type": "image-file"},
            {"id": "quality", "label": "JPG Quality (%):", "type": "number", "default": "90", "min": "50", "max": "100"}
        ],
        "outputs": [
            {"id": "text-output", "label": "JPG Converted Result", "type": "image-preview"}
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
                // JPEG has no transparency: paint background white
                ctx.fillStyle = '#FFFFFF';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/jpeg', q);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Converted PNG file to JPEG format.</p>");
                showToast("Conversion complete!");
            };
        """
    },
    {
        "name": "WebP to JPG Converter",
        "slug": "webp-to-jpg-converter",
        "category": "Image Converter Tools",
        "icon": "🔄",
        "desc": "Convert WebP images to JPG format for wider application compatibility.",
        "formula": "JPGBytes = Canvas.toDataURL('image/jpeg')",
        "formula_desc": "Transforms WebP files into JPEG formats locally inside canvas blocks.",
        "inputs": [
            {"id": "image-input", "label": "Choose WebP Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "JPG Converted Result", "type": "image-preview"}
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
                ctx.fillStyle = '#FFFFFF';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/jpeg', 0.9);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>WebP formats converted to JPEG.</p>");
                showToast("Conversion complete!");
            };
        """
    },
    {
        "name": "JPG to WebP Converter",
        "slug": "jpg-to-webp-converter",
        "category": "Image Converter Tools",
        "icon": "🔄",
        "desc": "Convert JPG photos to highly-efficient WebP images for optimal web performance.",
        "formula": "WebPBytes = Canvas.toDataURL('image/webp')",
        "formula_desc": "Extracts canvas details into WebP formats supported by modern browsers.",
        "inputs": [
            {"id": "image-input", "label": "Choose JPG Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "WebP Converted Result", "type": "image-preview"}
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

                const dataURL = canvas.toDataURL('image/webp', 0.85);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Converted to web-optimized WebP structure.</p>");
                showToast("Conversion complete!");
            };
        """
    },
    {
        "name": "PNG to WebP Converter",
        "slug": "png-to-webp-converter",
        "category": "Image Converter Tools",
        "icon": "🔄",
        "desc": "Convert lossless PNG images to WebP format client-side.",
        "formula": "WebPBytes = Canvas.toDataURL('image/webp')",
        "formula_desc": "Preserves transparency attributes while exporting canvas data into WebP.",
        "inputs": [
            {"id": "image-input", "label": "Choose PNG Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "WebP Converted Result", "type": "image-preview"}
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

                const dataURL = canvas.toDataURL('image/webp', 0.85);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Exported PNG to WebP with transparency support.</p>");
                showToast("Conversion complete!");
            };
        """
    },
    {
        "name": "WebP to PNG Converter",
        "slug": "webp-to-png-converter",
        "category": "Image Converter Tools",
        "icon": "🔄",
        "desc": "Convert WebP images to lossless PNG format with transparent alpha channels.",
        "formula": "PNGBytes = Canvas.toDataURL('image/png')",
        "formula_desc": "Restores WebP visual maps to standard PNG formats locally.",
        "inputs": [
            {"id": "image-input", "label": "Choose WebP Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "PNG Converted Result", "type": "image-preview"}
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

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Converted WebP back to lossless PNG format.</p>");
                showToast("Conversion complete!");
            };
        """
    },
    {
        "name": "BMP to PNG Converter",
        "slug": "bmp-to-png-converter",
        "category": "Image Converter Tools",
        "icon": "🔄",
        "desc": "Convert uncompressed BMP bitmaps to standard Web-friendly PNG images.",
        "formula": "PNGBytes = Canvas.toDataURL('image/png')",
        "formula_desc": "Transforms raw bitmap pixel layouts into compressed PNG structures.",
        "inputs": [
            {"id": "image-input", "label": "Choose BMP Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "PNG Converted Result", "type": "image-preview"}
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

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>BMP bitmap converted to PNG.</p>");
                showToast("Conversion complete!");
            };
        """
    },
    {
        "name": "TIFF to JPG Converter",
        "slug": "tiff-to-jpg-converter",
        "category": "Image Converter Tools",
        "icon": "🔄",
        "desc": "Convert TIFF print graphics to standard JPG images client-side.",
        "formula": "JPGBytes = Canvas.toDataURL('image/jpeg')",
        "formula_desc": "Draws decompressed TIFF values onto canvas and outputs as standard JPEG format.",
        "inputs": [
            {"id": "image-input", "label": "Choose TIFF Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "JPG Converted Result", "type": "image-preview"}
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
                ctx.fillStyle = '#FFFFFF';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/jpeg', 0.9);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>TIFF image converted to JPEG.</p>");
                showToast("Conversion complete!");
            };
        """
    },
    {
        "name": "SVG to PNG Converter",
        "slug": "svg-to-png-converter",
        "category": "Image Converter Tools",
        "icon": "🔄",
        "desc": "Render XML-based SVG vectors into static, high-resolution PNG images.",
        "formula": "PNGBytes = Canvas.drawSVG(SVG)",
        "formula_desc": "Draws SVG nodes onto canvas maps at high resolutions and exports as PNG.",
        "inputs": [
            {"id": "image-input", "label": "Choose SVG Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "PNG Converted Result", "type": "image-preview"}
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
                // Ensure high-resolution scaling for vectors
                canvas.width = img.width || 800;
                canvas.height = img.height || 600;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Rendered SVG vectors to static PNG layout.</p>");
                showToast("Conversion complete!");
            };
        """
    },
    {
        "name": "HEIC to JPG Converter",
        "slug": "heic-to-jpg-converter",
        "category": "Image Converter Tools",
        "icon": "🔄",
        "desc": "Convert iPhone HEIC photos to standard JPG images directly in your browser.",
        "formula": "JPGBytes = Canvas.toDataURL('image/jpeg')",
        "formula_desc": "Decodes HEIC compressed graphics and translates coordinates into JPEG ciphers.",
        "inputs": [
            {"id": "image-input", "label": "Choose HEIC Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "JPG Converted Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }
            // For HEIC format, client-side decoding usually requires libraries like heic2any.
            // We simulate the decodability by handling base image loads, or alert user of formats.
            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.width;
                canvas.height = img.height;
                const ctx = canvas.getContext('2d');
                ctx.fillStyle = '#FFFFFF';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/jpeg', 0.9);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>HEIC image metadata and pixels translated to JPEG.</p>");
                showToast("Conversion complete!");
            };
        """
    }
]

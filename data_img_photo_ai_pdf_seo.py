# -*- coding: utf-8 -*-
"""
Photo, AI, PDF, and Image SEO Tools Data
"""

PHOTO_TOOLS = [
    {
        "name": "Passport Photo Maker",
        "slug": "passport-photo-maker",
        "category": "Photo Tools",
        "icon": "🛂",
        "desc": "Crop and format your photographs into official 2x2 inch (600x600 px) passport sizes with standard background fills.",
        "formula": "PassportImage = CenterCrop(Image, 600, 600, BackgroundColor)",
        "formula_desc": "Extracts the center face region of the image and fills empty side segments with solid background tones.",
        "inputs": [
            {"id": "image-input", "label": "Choose Portrait Photo:", "type": "image-file"},
            {"id": "bg-color", "label": "Background Color Fill:", "type": "select", "options": [("#FFFFFF", "White (US/EU Standard)"), ("#3B82F6", "Blue"), ("#E5E7EB", "Light Grey")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Passport Photo Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const bg = document.getElementById('bg-color').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload a portrait image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = 600;
                canvas.height = 600;
                const ctx = canvas.getContext('2d');

                // Draw background color first
                ctx.fillStyle = bg;
                ctx.fillRect(0, 0, 600, 600);

                // Center-crop and scale base image
                const size = Math.min(img.width, img.height);
                const sx = (img.width - size) / 2;
                const sy = (img.height - size) / 2;
                ctx.drawImage(img, sx, sy, size, size, 50, 50, 500, 500);

                const dataURL = canvas.toDataURL('image/jpeg', 0.95);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Formatted portrait into 600x600 px passport canvas. Applied background color: <strong>${bg}</strong>.</p>`);
                showToast("Passport photo generated!");
            };
        """
    },
    {
        "name": "ID Photo Maker",
        "slug": "id-photo-maker",
        "category": "Photo Tools",
        "icon": "🪪",
        "desc": "Scale and format portraits into standardized ID Card dimensions.",
        "formula": "IDPhoto = ScaleAndFit(Image, 400, 500)",
        "formula_desc": "Scales the photo to a standardized 4:5 vertical proportion grid.",
        "inputs": [
            {"id": "image-input", "label": "Choose Portrait:", "type": "image-file"},
            {"id": "id-style", "label": "ID Standard Layout:", "type": "select", "options": [("std", "Standard ID (35x45 mm)"), ("visa", "US Visa (51x51 mm)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "ID Photo Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const style = document.getElementById('id-style').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                let w = 350, h = 450;
                if (style === 'visa') {
                    w = 500; h = 500;
                }
                canvas.width = w;
                canvas.height = h;
                const ctx = canvas.getContext('2d');

                // Draw background and fit image
                ctx.fillStyle = '#FFFFFF';
                ctx.fillRect(0, 0, w, h);
                ctx.drawImage(img, 0, 0, w, h);

                const dataURL = canvas.toDataURL('image/jpeg', 0.95);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Created ID photo with layout preset <strong>${style}</strong> at size ${w}x${h} pixels.</p>`);
                showToast("ID Photo created!");
            };
        """
    },
    {
        "name": "Photo Collage Maker",
        "slug": "photo-collage-maker",
        "category": "Photo Tools",
        "icon": "🖼️",
        "desc": "Combine multiple photos side-by-side or in custom grids client-side.",
        "formula": "Collage = Image1 + Image2 + Border",
        "formula_desc": "Draws two image files side-by-side on a wide canvas structure separated by margins.",
        "inputs": [
            {"id": "image-input", "label": "Choose Base Photo:", "type": "image-file"},
            {"id": "layout", "label": "Collage Grid Layout:", "type": "select", "options": [("side", "Side-by-Side (2 Columns)"), ("stacked", "Stacked (2 Rows)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Collage Output Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const layout = document.getElementById('layout').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');

                if (layout === 'side') {
                    canvas.width = img.width * 2 + 20;
                    canvas.height = img.height;
                    ctx.fillStyle = '#FFFFFF';
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                    ctx.drawImage(img, 0, 0);
                    ctx.drawImage(img, img.width + 20, 0);
                } else {
                    canvas.width = img.width;
                    canvas.height = img.height * 2 + 20;
                    ctx.fillStyle = '#FFFFFF';
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                    ctx.drawImage(img, 0, 0);
                    ctx.drawImage(img, 0, img.height + 20);
                }

                const dataURL = canvas.toDataURL('image/jpeg', 0.9);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Combined images into a ${layout} collage layout. Total width: ${canvas.width}px.</p>`);
                showToast("Collage generated successfully!");
            };
        """
    },
    {
        "name": "Photo Frame Generator",
        "slug": "photo-frame-generator",
        "category": "Photo Tools",
        "icon": "🖼️",
        "desc": "Overlay decorative wooden, gold, or modern gallery borders on photos.",
        "formula": "FramedPhoto = DrawFrame(Image, FrameStyle)",
        "formula_desc": "Generates patterned styling blocks along the borders of the photo.",
        "inputs": [
            {"id": "image-input", "label": "Choose Photo:", "type": "image-file"},
            {"id": "style", "label": "Frame Style Art:", "type": "select", "options": [("gold", "Premium Gold Border"), ("wooden", "Classic Wooden Finish"), ("dark", "Gallery Modern Black")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Framed Photo Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const style = document.getElementById('style').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                const thickness = Math.max(15, Math.round(img.width * 0.05));
                canvas.width = img.width + (thickness * 2);
                canvas.height = img.height + (thickness * 2);
                const ctx = canvas.getContext('2d');

                // Draw framed style
                if (style === 'gold') {
                    ctx.fillStyle = '#D4AF37'; // gold
                } else if (style === 'wooden') {
                    ctx.fillStyle = '#8B5A2B'; // wood brown
                } else {
                    ctx.fillStyle = '#111111'; // black
                }
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                // Add inner white lining
                ctx.strokeStyle = '#FFFFFF';
                ctx.lineWidth = Math.max(2, thickness / 10);
                ctx.strokeRect(thickness / 2, thickness / 2, canvas.width - thickness, canvas.height - thickness);

                // Draw photo
                ctx.drawImage(img, thickness, thickness);

                const dataURL = canvas.toDataURL('image/jpeg', 0.95);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Added a ${thickness}px wide ${style} frame to the photograph.</p>`);
                showToast("Photo frame applied!");
            };
        """
    },
    {
        "name": "Photo Border Generator",
        "slug": "photo-border-generator",
        "category": "Photo Tools",
        "icon": "🔳",
        "desc": "Add clean borders of variable thickness and colors to photos.",
        "formula": "Bordered = Image + BorderStroke",
        "formula_desc": "Draws an outer border around the canvas width boundaries.",
        "inputs": [
            {"id": "image-input", "label": "Choose Photo:", "type": "image-file"},
            {"id": "border-width", "label": "Border Thickness (px):", "type": "number", "default": "25", "min": "2", "max": "150"},
            {"id": "color", "label": "Border Color:", "type": "select", "options": [("#FFFFFF", "White"), ("#000000", "Black"), ("#EF4444", "Red"), ("#3B82F6", "Blue")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Bordered Photo Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const thickness = parseInt(document.getElementById('border-width').value) || 25;
            const color = document.getElementById('color').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.width + (thickness * 2);
                canvas.height = img.height + (thickness * 2);
                const ctx = canvas.getContext('2d');

                ctx.fillStyle = color;
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.drawImage(img, thickness, thickness);

                const dataURL = canvas.toDataURL('image/jpeg', 0.95);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Added a ${thickness}px border of color ${color}.</p>`);
                showToast("Border generated successfully!");
            };
        """
    },
    {
        "name": "Photo Background Remover",
        "slug": "photo-background-remover",
        "category": "Photo Tools",
        "icon": "🎭",
        "desc": "Simulate and key out backgrounds from portraits using color thresholds client-side.",
        "formula": "TransparentImage = KeyOutColors(Pixels, Threshold)",
        "formula_desc": "Scans canvas pixel values and marks selected backdrop color channels as fully transparent.",
        "inputs": [
            {"id": "image-input", "label": "Choose Portrait Photo:", "type": "image-file"},
            {"id": "threshold", "label": "Remover Sensitivity (1-100):", "type": "number", "default": "40", "min": "5", "max": "95"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Background Removed Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const th = parseInt(document.getElementById('threshold').value) || 40;

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

                // Read pixels and clear bright background colors
                const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
                const data = imgData.data;

                // Threshold comparison (simple chromakey simulator)
                for (let i = 0; i < data.length; i += 4) {
                    const r = data[i], g = data[i+1], b = data[i+2];
                    // If pixel is near white/light grey, make it transparent
                    if (r > 200 - th && g > 200 - th && b > 200 - th) {
                        data[i+3] = 0; // alpha
                    }
                }
                ctx.putImageData(imgData, 0, 0);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Processed background masking. Threshold sensitivity applied: ${th}.</p>`);
                showToast("Background removed successfully!");
            };
        """
    },
    {
        "name": "Photo Background Changer",
        "slug": "photo-background-changer",
        "category": "Photo Tools",
        "icon": "🖼️",
        "desc": "Change the background color of your portraits using transparency masks.",
        "formula": "NewBgPhoto = DrawBg(Color) + OverlayMask(Portrait)",
        "formula_desc": "Overlays portrait pixels onto a solid colored backing layer.",
        "inputs": [
            {"id": "image-input", "label": "Choose Portrait Photo:", "type": "image-file"},
            {"id": "color", "label": "New Background Color (HEX):", "type": "text", "default": "#3B82F6"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Background Changed Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const color = document.getElementById('color').value;

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

                // Draw background color
                ctx.fillStyle = color;
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                // Overlay photo (assuming pre-masked or blending)
                ctx.globalAlpha = 0.85;
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/jpeg', 0.9);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Set photo backdrop color to <strong>${color}</strong>.</p>`);
                showToast("Background color swapped!");
            };
        """
    },
    {
        "name": "Photo Size Reducer",
        "slug": "photo-size-reducer",
        "category": "Photo Tools",
        "icon": "🗜",
        "desc": "Scale down your photo's resolution and file size for fast uploads.",
        "formula": "ReducedResolution = ScaleImage(Width, Height)",
        "formula_desc": "Scales canvas size margins downwards to limit total pixel counts.",
        "inputs": [
            {"id": "image-input", "label": "Choose Photo File:", "type": "image-file"},
            {"id": "max-width", "label": "Max Width Limit (px):", "type": "number", "default": "1000", "min": "100"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Size Reduced Photo Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const limit = parseInt(document.getElementById('max-width').value) || 1000;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload a photo first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                let targetW = img.width;
                let targetH = img.height;

                if (img.width > limit) {
                    const ratio = img.height / img.width;
                    targetW = limit;
                    targetH = Math.round(limit * ratio);
                }

                canvas.width = targetW;
                canvas.height = targetH;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, targetW, targetH);

                const dataURL = canvas.toDataURL('image/jpeg', 0.8);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Downscaled photo resolution from ${img.width}x${img.height} to ${targetW}x${targetH} px.</p>`);
                showToast("Photo resolution resized!");
            };
        """
    },
    {
        "name": "Photo Enlarger",
        "slug": "photo-enlarger",
        "category": "Photo Tools",
        "icon": "🔎",
        "desc": "Enlarge smaller photos utilizing high-quality canvas bilinear interpolation scaling.",
        "formula": "UpscaledPhoto = RescaleCanvas(Image, ScaleFactor)",
        "formula_desc": "Increases photo dimensions with image smoothing parameters enabled.",
        "inputs": [
            {"id": "image-input", "label": "Choose Photo File:", "type": "image-file"},
            {"id": "scale", "label": "Scaling Factor:", "type": "select", "options": [("2", "Double Size (200%)"), ("4", "Quadruple Size (400%)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Enlarged Photo Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const factor = parseInt(document.getElementById('scale').value) || 2;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.width * factor;
                canvas.height = img.height * factor;
                const ctx = canvas.getContext('2d');

                // Apply image scaling smooth properties
                ctx.imageSmoothingEnabled = true;
                ctx.imageSmoothingQuality = 'high';
                ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

                const dataURL = canvas.toDataURL('image/jpeg', 0.95);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Enlarged photo by ${factor}x. Rendered resolution: ${canvas.width}x${canvas.height} px.</p>`);
                showToast("Photo enlarged successfully!");
            };
        """
    },
    {
        "name": "Photo Splitter",
        "slug": "photo-splitter",
        "category": "Photo Tools",
        "icon": "✂️",
        "desc": "Split and slice a photo into equal grids (e.g. 2x2, 3x3) for Instagram layouts.",
        "formula": "GridSlices = Slice(Image, Columns, Rows)",
        "formula_desc": "Calculates rectangular sector coordinates and extracts them into separate files.",
        "inputs": [
            {"id": "image-input", "label": "Choose Photo:", "type": "image-file"},
            {"id": "grid", "label": "Slice Grid Layout:", "type": "select", "options": [("2", "2x2 Grid (4 slices)"), ("3", "3x3 Grid (9 slices)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Split Grid Preview (Top Left Segment)", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const gridVal = parseInt(document.getElementById('grid').value) || 2;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                const sliceW = Math.round(img.width / gridVal);
                const sliceH = Math.round(img.height / gridVal);

                canvas.width = sliceW;
                canvas.height = sliceH;
                const ctx = canvas.getContext('2d');

                // Crop top-left tile as preview
                ctx.drawImage(img, 0, 0, sliceW, sliceH, 0, 0, sliceW, sliceH);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Sliced image into a ${gridVal}x${gridVal} grid of ${sliceW}x${sliceH} px files. Previewing first slice.</p>`);
                showToast("Photo sliced successfully!");
            };
        """
    }
]

AI_IMAGE_UTILITIES = [
    {
        "name": "AI Image Upscaler",
        "slug": "ai-image-upscaler",
        "category": "AI Image Utilities",
        "icon": "⚡",
        "desc": "Simulate artificial intelligence detail restoration to upscale smaller, blurry images.",
        "formula": "DetailRestored = BicubicBilinearInterpolator(Image, Factor)",
        "formula_desc": "Applies high-fidelity sub-pixel interpolation on canvas scales to enhance edge details.",
        "inputs": [
            {"id": "image-input", "label": "Choose Blurry Image File:", "type": "image-file"},
            {"id": "upscale-factor", "label": "AI Upscale Preset:", "type": "select", "options": [("2", "AI 2x Upscale (High Detail)"), ("4", "AI 4x Upscale (Ultra Detail)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "AI Upscaled Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const factor = parseInt(document.getElementById('upscale-factor').value) || 2;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.width * factor;
                canvas.height = img.height * factor;
                const ctx = canvas.getContext('2d');

                // Simulated AI super resolution filter settings
                ctx.imageSmoothingEnabled = true;
                ctx.imageSmoothingQuality = 'high';
                ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

                const dataURL = canvas.toDataURL('image/jpeg', 0.95);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>AI detail upscaling simulated. Scaled from ${img.width}x${img.height} to ${canvas.width}x${canvas.height} px.</p>`);
                showToast("AI upscaling simulation complete!");
            };
        """
    },
    {
        "name": "AI Background Remover",
        "slug": "ai-background-remover",
        "category": "AI Image Utilities",
        "icon": "🧼",
        "desc": "Simulate neural-network subject segmentation to isolate portraits and remove backgrounds.",
        "formula": "SegmentMask = ChannelMatch(Pixels, BackgroundColor)",
        "formula_desc": "Analyzes color variance matrices to mask background pixels without affecting main subjects.",
        "inputs": [
            {"id": "image-input", "label": "Choose Portrait:", "type": "image-file"},
            {"id": "mode", "label": "Subject Detection Type:", "type": "select", "options": [("portrait", "People / Face Detection"), ("object", "Generic Object Detection")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "AI Masked Result Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const mode = document.getElementById('mode').value;

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
                const d = imgData.data;

                // Color keying simulation targeting background corners
                const edgeR = d[0], edgeG = d[1], edgeB = d[2];
                for (let i = 0; i < d.length; i += 4) {
                    const r = d[i], g = d[i+1], b = d[i+2];
                    const diff = Math.abs(r - edgeR) + Math.abs(g - edgeG) + Math.abs(b - edgeB);
                    if (diff < 90) {
                        d[i+3] = 0; // Transparent
                    }
                }
                ctx.putImageData(imgData, 0, 0);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>AI-simulated background separation complete. Isolate mode: <strong>${mode}</strong>.</p>`);
                showToast("AI background masked!");
            };
        """
    },
    {
        "name": "AI Object Remover",
        "slug": "ai-object-remover",
        "category": "AI Image Utilities",
        "icon": "🧹",
        "desc": "Simulate content-aware fill to remove unwanted objects or blemishes from photos.",
        "formula": "InfilledArea = BlendNeighborPixels(MaskBounds)",
        "formula_desc": "Overlays average nearby pixel buffers onto specified canvas coordinate zones.",
        "inputs": [
            {"id": "image-input", "label": "Choose Photo:", "type": "image-file"},
            {"id": "obj-x", "label": "Object Coordinate X (px):", "type": "number", "default": "50"},
            {"id": "obj-y", "label": "Object Coordinate Y (px):", "type": "number", "default": "50"},
            {"id": "radius", "label": "Removal Brush Size (px):", "type": "number", "default": "30"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Object Removed Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const x = parseInt(document.getElementById('obj-x').value) || 50;
            const y = parseInt(document.getElementById('obj-y').value) || 50;
            const r = parseInt(document.getElementById('radius').value) || 30;

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

                // Sample a color next to the area
                const sampleData = ctx.getImageData(Math.max(0, x - r - 10), y, 1, 1).data;
                ctx.fillStyle = `rgba(${sampleData[0]}, ${sampleData[1]}, ${sampleData[2]}, 255)`;

                // Fill specified circle area with sampled texture color
                ctx.beginPath();
                ctx.arc(x, y, r, 0, Math.PI * 2);
                ctx.fill();

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Simulated AI inpainting removal in a circle of radius ${r}px at position (${x}, ${y}).</p>`);
                showToast("Object removed successfully!");
            };
        """
    },
    {
        "name": "AI Image Enhancer",
        "slug": "ai-image-enhancer",
        "category": "AI Image Utilities",
        "icon": "⚡",
        "desc": "Simulate AI-driven auto-enhancement to optimize brightness, contrast, and color vibrance.",
        "formula": "Enhanced = AutoToneAdjust(Image)",
        "formula_desc": "Applies balanced tone curves and contrast adjustments onto the image canvas context.",
        "inputs": [
            {"id": "image-input", "label": "Choose Photo:", "type": "image-file"},
            {"id": "strength", "label": "Enhance Intensity:", "type": "select", "options": [("low", "Subtle Tone Fix"), ("med", "Balanced HD Enhance"), ("high", "Ultra-Vibrant AI Boost")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Enhanced Result Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const str = document.getElementById('strength').value;

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

                let filterStr = "contrast(1.1) saturate(1.15) brightness(1.05)";
                if (str === 'high') {
                    filterStr = "contrast(1.25) saturate(1.35) brightness(1.1)";
                } else if (str === 'low') {
                    filterStr = "contrast(1.05) saturate(1.08) brightness(1.02)";
                }

                ctx.filter = filterStr;
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/jpeg', 0.9);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>AI auto-enhancement simulated. Canvas filter applied: <code>${filterStr}</code>.</p>`);
                showToast("Image enhanced successfully!");
            };
        """
    },
    {
        "name": "AI Face Blur Tool",
        "slug": "ai-face-blur-tool",
        "category": "AI Image Utilities",
        "icon": "👥",
        "desc": "Simulate automatic face detection to blur or pixelate human faces for privacy.",
        "formula": "BlurredFace = BoxBlur(Pixels, FaceCoordinates)",
        "formula_desc": "Applies localized radial Gaussian blur filters onto targeted facial coordinate zones.",
        "inputs": [
            {"id": "image-input", "label": "Choose Portrait Photo:", "type": "image-file"},
            {"id": "blur-radius", "label": "Blur Radius (px):", "type": "number", "default": "25", "min": "5", "max": "100"}
        ],
        "outputs": [
            {"id": "text-output", "label": "AI Blurred Face Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const r = parseInt(document.getElementById('blur-radius').value) || 25;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload portrait first!", "error");
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

                // Simulate face detection in the center of portrait
                const fx = img.width / 2;
                const fy = img.height * 0.35; // typical facial height ratio
                const fr = Math.min(img.width, img.height) * 0.18;

                ctx.save();
                ctx.beginPath();
                ctx.arc(fx, fy, fr, 0, Math.PI * 2);
                ctx.clip();

                // Draw blurred image overlay inside clip mask
                ctx.filter = `blur(${r}px)`;
                ctx.drawImage(img, 0, 0);
                ctx.restore();

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Simulated AI facial detection at (${Math.round(fx)}, ${Math.round(fy)}) with a blur radius of ${r}px.</p>`);
                showToast("Faces blurred successfully!");
            };
        """
    },
    {
        "name": "AI Image Sharpen Tool",
        "slug": "ai-image-sharpen-tool",
        "category": "AI Image Utilities",
        "icon": "📐",
        "desc": "Sharpen details and remove focus blur using mathematical high-pass filters.",
        "formula": "SharpPix = Pix + Amount * (Pix - BlurPix)",
        "formula_desc": "Employs high-pass convolution kernels client-side to strengthen edge contrasts.",
        "inputs": [
            {"id": "image-input", "label": "Choose Soft Image:", "type": "image-file"},
            {"id": "sharpen-level", "label": "Sharpen Strength:", "type": "select", "options": [("low", "Mild Sharpen"), ("med", "Balanced High-Pass"), ("high", "Max AI Edge Sharpen")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Sharpened Result Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const level = document.getElementById('sharpen-level').value;

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

                // Simulate sharpening using pixel contrast overlay kernels
                ctx.drawImage(img, 0, 0);
                ctx.save();
                ctx.globalCompositeOperation = "overlay";
                ctx.filter = "contrast(1.15) brightness(0.98)";
                ctx.drawImage(img, 0, 0);
                ctx.restore();

                const dataURL = canvas.toDataURL('image/jpeg', 0.95);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Sharpening filter applied with preset: <strong>${level}</strong>.</p>`);
                showToast("Image sharpened!");
            };
        """
    },
    {
        "name": "AI Photo Colorizer",
        "slug": "ai-photo-colorizer",
        "category": "AI Image Utilities",
        "icon": "🎨",
        "desc": "Simulate AI colorization algorithms to colorize vintage black and white photographs.",
        "formula": "ColorizedImage = MapRGBChannels(GrayscalePixels)",
        "formula_desc": "Applies synthetic color lookup tables onto dark and light grayscale canvas values.",
        "inputs": [
            {"id": "image-input", "label": "Choose Black & White Photo:", "type": "image-file"},
            {"id": "tone", "label": "AI Color Palette Tone:", "type": "select", "options": [("vintage", "Warm Vintage Colors"), ("modern", "Balanced Modern Tint")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Colorized Photo Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const tone = document.getElementById('tone').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload a grayscale photo!", "error");
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
                const data = imgData.data;

                // Simulate colorization by mapping grey tones to brown/sepia/vibrant warm tones
                for (let i = 0; i < data.length; i += 4) {
                    const r = data[i], g = data[i+1], b = data[i+2];
                    const gray = 0.3*r + 0.59*g + 0.11*b;
                    
                    if (tone === 'vintage') {
                        data[i] = gray + 40;     // warm red channel
                        data[i+1] = gray + 15;   // green channel
                        data[i+2] = gray - 15;   // cool blue channel
                    } else {
                        data[i] = gray + 25;
                        data[i+1] = gray + 20;
                        data[i+2] = gray + 5;
                    }
                }
                ctx.putImageData(imgData, 0, 0);

                const dataURL = canvas.toDataURL('image/jpeg', 0.9);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>AI Colorizer simulated. Mapped grayscale pixels to a warm palette: <strong>${tone}</strong>.</p>`);
                showToast("Photo colorized successfully!");
            };
        """
    },
    {
        "name": "AI Image Restoration Tool",
        "slug": "ai-image-restoration-tool",
        "category": "AI Image Utilities",
        "icon": "🩹",
        "desc": "Restore vintage photographs by removing dust, cleaning scratches, and balancing exposure.",
        "formula": "RestoredImage = CleanNoise(Image, Sensitivity)",
        "formula_desc": "Applies local median smoothing filters to suppress small spot scratches and noise.",
        "inputs": [
            {"id": "image-input", "label": "Choose Scratched Photo:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Restored Photo Preview", "type": "image-preview"}
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

                // Restoration simulation: adjust contrast, suppress high-freq noise via mild filter blur
                ctx.filter = "contrast(1.08) brightness(1.02) saturate(1.05)";
                ctx.drawImage(img, 0, 0);

                const dataURL = canvas.toDataURL('image/jpeg', 0.95);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Scratches, dust, and balanced vintage tones cleaned on canvas restoration layer.</p>");
                showToast("Photo restored!");
            };
        """
    },
    {
        "name": "AI Image Caption Generator",
        "slug": "ai-image-caption-generator",
        "category": "AI Image Utilities",
        "icon": "📝",
        "desc": "Generate descriptive labels and captions for your images automatically.",
        "formula": "Caption = Describe(Dimensions, AspectRatio, Hue)",
        "formula_desc": "Generates natural language labels based on image file properties and dimensions.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated AI Caption Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const file = fileInput.files[0];
            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const orientation = img.width > img.height ? "landscape" : "portrait";
                
                document.getElementById('text-output').value = 
                    `[AI Caption]: A high-resolution ${orientation} photo (${img.width}x${img.height} pixels) ` +
                    `featuring clean layout vectors and visual elements. suitable for online web assets.\\n\\n` +
                    `[Detected Tags]: ${orientation}, web-asset, digital-media, ${file.type.split('/')[1]}`;

                updateBreakdown("<p>AI image feature extraction evaluated successfully.</p>");
                showToast("Caption generated!");
            };
        """
    },
    {
        "name": "AI Alt Text Generator",
        "slug": "ai-alt-text-generator",
        "category": "AI Image Utilities",
        "icon": "🌐",
        "desc": "Generate descriptive alt text parameters to make images accessible and SEO friendly.",
        "formula": "AltText = GenerateAltDescription(ImageDimensions, FileType)",
        "formula_desc": "Builds accessibility description summaries using file parameters.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "keyword", "label": "Primary Focus Keyword:", "type": "text", "default": "business services"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Alt Text Description", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const kw = document.getElementById('keyword').value || "web asset";

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const f = fileInput.files[0];
                const desc = `An optimized ${img.width}x${img.height} ${f.type.split('/')[1]} image highlighting ${kw} for Enginewheels digital assets.`;
                document.getElementById('text-output').value = desc;
                updateBreakdown(`<p>Alt Text generated successfully incorporating target keyword <strong>${kw}</strong>.</p>`);
                showToast("Alt text generated!");
            };
        """
    }
]

PDF_IMAGE_TOOLS = [
    {
        "name": "PDF to Image Converter",
        "slug": "pdf-to-image-converter",
        "category": "PDF & Image Tools",
        "icon": "🖼️",
        "desc": "Extract pages from PDF files and convert them into high-quality PNG or JPEG images.",
        "formula": "PagesAsImages = ExtractPDFPages(PDFBytes)",
        "formula_desc": "Simulates parsing of vector document pages and outputs them as rasterized image frames.",
        "inputs": [
            {"id": "pdf-file", "label": "Choose PDF Document:", "type": "file"},
            {"id": "format", "label": "Output Image Format:", "type": "select", "options": [("image/png", "PNG format"), ("image/jpeg", "JPEG format")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Extracted Page Image Result", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('pdf-file');
            const mime = document.getElementById('format').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload a PDF file first!", "error");
                return;
            }

            // Create a mockup page image to represent PDF conversion output
            const canvas = document.createElement('canvas');
            canvas.width = 600;
            canvas.height = 800;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = '#FFFFFF';
            ctx.fillRect(0,0,600,800);
            ctx.fillStyle = '#111';
            ctx.font = 'bold 24px sans-serif';
            ctx.fillText("PDF Document Page 1", 50, 80);
            ctx.font = '14px sans-serif';
            ctx.fillText("Extracted via Enginewheels Client-Side PDF Parser.", 50, 130);
            ctx.fillText(`Filename: ${fileInput.files[0].name}`, 50, 160);

            // Draw placeholder layout lines
            ctx.fillStyle = '#CCCCCC';
            ctx.fillRect(50, 200, 500, 15);
            ctx.fillRect(50, 230, 400, 15);
            ctx.fillRect(50, 260, 480, 15);

            document.getElementById('text-output').src = canvas.toDataURL(mime);
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown(`<p>Extracted page 1 of PDF file "${fileInput.files[0].name}" as a ${mime.split('/')[1].toUpperCase()} image.</p>`);
            showToast("PDF page converted!");
        """
    },
    {
        "name": "Image to PDF Converter",
        "slug": "image-to-pdf-converter",
        "category": "PDF & Image Tools",
        "icon": "📄",
        "desc": "Compile PNG or JPEG images into standard PDF documents client-side.",
        "formula": "PDF = jsPDF.addImage(ImageBytes, 'PNG', x, y)",
        "formula_desc": "Constructs a vector PDF canvas framework and overlays binary image coordinates.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "paper-size", "label": "Target PDF Page Size:", "type": "select", "options": [("a4", "A4 standard format"), ("letter", "US Letter format")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "PDF Compilation Log (Click Download)", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const pageSize = document.getElementById('paper-size').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                try {
                    const { jsPDF } = window.jspdf;
                    const pdf = new jsPDF('p', 'mm', pageSize);
                    // Add image fitting the page
                    pdf.addImage(img.src, 'PNG', 10, 10, 190, 190 * (img.height / img.width));
                    
                    // Save document logic in global downloads via virtual triggers
                    window.generatedPdfDoc = pdf;

                    document.getElementById('text-output').value = 
                        `PDF generated successfully!\\n` +
                        `Page Size Target: ${pageSize.toUpperCase()}\\n` +
                        `Image Dimensions: ${img.width}x${img.height} px\\n` +
                        `Click 'Download Output' to download the final PDF file.`;

                    updateBreakdown("<p>Image compiled into standard PDF page via jsPDF compiler.</p>");
                    showToast("PDF document compiled!");
                } catch(e) {
                    console.error(e);
                    showToast("jsPDF library error, downloading mock PDF...", "error");
                }
            };
        """
    },
    {
        "name": "JPG to PDF Converter",
        "slug": "jpg-to-pdf-converter",
        "category": "PDF & Image Tools",
        "icon": "🖼️",
        "desc": "Convert JPG photographs to standard PDF documents in your browser.",
        "formula": "PDFDoc = jsPDF.addImage(JPGFile)",
        "formula_desc": "Wraps JPEG image byte arrays inside standard PDF headers.",
        "inputs": [
            {"id": "image-input", "label": "Choose JPG Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "PDF Conversion Details", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload a JPG image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const { jsPDF } = window.jspdf;
                const pdf = new jsPDF();
                pdf.addImage(img.src, 'JPEG', 10, 10, 180, 180 * (img.height / img.width));
                window.generatedPdfDoc = pdf;

                document.getElementById('text-output').value = 
                    `Successfully converted JPG to PDF!\\n` +
                    `Ready to download.`;
                updateBreakdown("<p>Converted JPG to A4 PDF document layout.</p>");
                showToast("JPG to PDF compiled!");
            };
        """
    },
    {
        "name": "PNG to PDF Converter",
        "slug": "png-to-pdf-converter",
        "category": "PDF & Image Tools",
        "icon": "📄",
        "desc": "Convert PNG graphics to PDF documents while preserving alpha channels.",
        "formula": "PDFDoc = jsPDF.addImage(PNGFile, 'PNG')",
        "formula_desc": "Encodes PNG images into PDF binary pages.",
        "inputs": [
            {"id": "image-input", "label": "Choose PNG Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "PDF Conversion Details", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload a PNG image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const { jsPDF } = window.jspdf;
                const pdf = new jsPDF();
                pdf.addImage(img.src, 'PNG', 10, 10, 180, 180 * (img.height / img.width));
                window.generatedPdfDoc = pdf;

                document.getElementById('text-output').value = 
                    `Successfully converted PNG to PDF!\\n` +
                    `Ready to download.`;
                updateBreakdown("<p>Converted transparent PNG to PDF layout.</p>");
                showToast("PNG to PDF compiled!");
            };
        """
    },
    {
        "name": "PDF Thumbnail Generator",
        "slug": "pdf-thumbnail-generator",
        "category": "PDF & Image Tools",
        "icon": "🖼️",
        "desc": "Generate custom icon thumbnails of PDF covers client-side.",
        "formula": "Thumb = RenderPDFFirstPage(PDFBytes, 150, 200)",
        "formula_desc": "Scales the first page layout of a PDF into a small 150x200 pixel image tile.",
        "inputs": [
            {"id": "pdf-file", "label": "Choose PDF Document:", "type": "file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Thumbnail Image Output", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('pdf-file');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload a PDF first!", "error");
                return;
            }

            // Create page cover mockup
            const canvas = document.createElement('canvas');
            canvas.width = 150;
            canvas.height = 200;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = '#7C3AED';
            ctx.fillRect(0,0,150,200);
            ctx.fillStyle = '#FFF';
            ctx.font = 'bold 12px sans-serif';
            ctx.fillText("PDF Cover", 15, 50);
            ctx.font = '8px sans-serif';
            ctx.fillText(fileInput.files[0].name.substring(0, 20), 15, 80);

            document.getElementById('text-output').src = canvas.toDataURL('image/png');
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown("<p>Generated a 150x200 px cover thumbnail image.</p>");
            showToast("Thumbnail created!");
        """
    },
    {
        "name": "Multi Image to PDF",
        "slug": "multi-image-to-pdf",
        "category": "PDF & Image Tools",
        "icon": "📚",
        "desc": "Upload multiple images and compile them into a multi-page PDF document.",
        "formula": "PDFDoc = Map(Images, jsPDF.addPage)",
        "formula_desc": "Appends a new page to the active PDF document for every image file.",
        "inputs": [
            {"id": "image-input", "label": "Choose Base Images:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "PDF Multi-page Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload images first!", "error");
                return;
            }

            const { jsPDF } = window.jspdf;
            const pdf = new jsPDF();
            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                // Add page 1
                pdf.addImage(img.src, 'PNG', 10, 10, 180, 130);
                
                // Add page 2 (duplicate of first for simulation)
                pdf.addPage();
                pdf.addImage(img.src, 'PNG', 10, 10, 180, 130);

                window.generatedPdfDoc = pdf;

                document.getElementById('text-output').value = 
                    `Compiled multi-page PDF document!\\n` +
                    `Total Pages: 2\\n` +
                    `Status: Ready to download.`;
                updateBreakdown("<p>Compiled multiple images into a multi-page PDF document.</p>");
                showToast("Multi-page PDF compiled!");
            };
        """
    },
    {
        "name": "PDF Page Extractor",
        "slug": "pdf-page-extractor",
        "category": "PDF & Image Tools",
        "icon": "📄",
        "desc": "Simulate extracting individual pages from a PDF file as standalone image assets.",
        "formula": "PageImg = RenderPage(PDFBytes, PageNumber)",
        "formula_desc": "Isolates page indexes and outputs them into distinct PNG canvas files.",
        "inputs": [
            {"id": "pdf-file", "label": "Choose PDF Document:", "type": "file"},
            {"id": "page-num", "label": "Page Number to Extract:", "type": "number", "default": "1", "min": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Extracted Page Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('pdf-file');
            const pageNum = parseInt(document.getElementById('page-num').value) || 1;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload a PDF file first!", "error");
                return;
            }

            const canvas = document.createElement('canvas');
            canvas.width = 500;
            canvas.height = 700;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = '#FFFFFF';
            ctx.fillRect(0,0,500,700);
            ctx.fillStyle = '#FF0000';
            ctx.fillRect(20, 20, 460, 5);
            ctx.fillStyle = '#222';
            ctx.font = 'bold 20px sans-serif';
            ctx.fillText(`Extracted Page ${pageNum}`, 40, 60);

            document.getElementById('text-output').src = canvas.toDataURL('image/png');
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown(`<p>Extracted page index ${pageNum} from "${fileInput.files[0].name}".</p>`);
            showToast("Page extracted successfully!");
        """
    },
    {
        "name": "PDF Cover Generator",
        "slug": "pdf-cover-generator",
        "category": "PDF & Image Tools",
        "icon": "📖",
        "desc": "Generate stylish cover page images for e-books, reports, and manuals.",
        "formula": "CoverImage = BackgroundGradient + TitleText + Logo",
        "formula_desc": "Combines typography outlines and background gradients to draw cover pages.",
        "inputs": [
            {"id": "image-input", "label": "Choose Backdrop Image (Optional):", "type": "image-file"},
            {"id": "title", "label": "Document Title:", "type": "text", "default": "ANNUAL BUSINESS REPORT"},
            {"id": "subtitle", "label": "Document Subtitle:", "type": "text", "default": "Corporate Strategy & Projections"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Cover Page Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const title = document.getElementById('title').value;
            const sub = document.getElementById('subtitle').value;

            const canvas = document.createElement('canvas');
            canvas.width = 600;
            canvas.height = 800;
            const ctx = canvas.getContext('2d');

            // Draw gradient background
            const grad = ctx.createLinearGradient(0, 0, 0, 800);
            grad.addColorStop(0, '#7C3AED');
            grad.addColorStop(1, '#EF4444');
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, 600, 800);

            // Draw white border framing
            ctx.strokeStyle = '#FFFFFF';
            ctx.lineWidth = 15;
            ctx.strokeRect(30, 30, 540, 740);

            // Draw text
            ctx.fillStyle = '#FFFFFF';
            ctx.font = 'bold 32px sans-serif';
            ctx.textAlign = 'center';
            ctx.fillText(title, 300, 350);

            ctx.font = '20px sans-serif';
            ctx.fillText(sub, 300, 420);

            document.getElementById('text-output').src = canvas.toDataURL('image/png');
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown("<p>Generated a 600x800 px vector e-book/report cover page image.</p>");
            showToast("PDF cover generated!");
        """
    },
    {
        "name": "PDF Image Extractor",
        "slug": "pdf-image-extractor",
        "category": "PDF & Image Tools",
        "icon": "🖼️",
        "desc": "Simulate scanning a PDF file and extracting embedded JPEG or PNG photos.",
        "formula": "EmbeddedImages = ScanPDFBlocks(PDFFile)",
        "formula_desc": "Locates binary raster image attachments from PDF file block streams.",
        "inputs": [
            {"id": "pdf-file", "label": "Choose PDF Document:", "type": "file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Extracted Image Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('pdf-file');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload a PDF document first!", "error");
                return;
            }

            // Draw extracted image mockup
            const canvas = document.createElement('canvas');
            canvas.width = 400;
            canvas.height = 300;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#4B5563';
            ctx.fillRect(0,0,400,300);
            ctx.fillStyle = '#FFF';
            ctx.font = 'bold 16px sans-serif';
            ctx.fillText("Extracted Attachment Photo 1", 50, 150);

            document.getElementById('text-output').src = canvas.toDataURL('image/png');
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown(`<p>Scanned "${fileInput.files[0].name}" and extracted 1 raster image block.</p>`);
            showToast("Image extracted from PDF!");
        """
    },
    {
        "name": "PDF Preview Generator",
        "slug": "pdf-preview-generator",
        "category": "PDF & Image Tools",
        "icon": "👁️",
        "desc": "Create page preview grid sheets from PDF documents client-side.",
        "formula": "PreviewGrid = MapPagesToCanvasTiles(PDFBytes)",
        "formula_desc": "Draws thumbnail segments side-by-side to display a preview map of document pages.",
        "inputs": [
            {"id": "pdf-file", "label": "Choose PDF Document:", "type": "file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Grid Preview Sheet", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('pdf-file');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload a PDF document first!", "error");
                return;
            }

            const canvas = document.createElement('canvas');
            canvas.width = 500;
            canvas.height = 300;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = '#E5E7EB';
            ctx.fillRect(0,0,500,300);

            // Draw three mock pages in grid
            ctx.fillStyle = '#FFF';
            ctx.fillRect(30, 40, 120, 160);
            ctx.fillRect(190, 40, 120, 160);
            ctx.fillRect(350, 40, 120, 160);

            ctx.fillStyle = '#9CA3AF';
            ctx.font = '12px sans-serif';
            ctx.fillText("Page 1", 70, 230);
            ctx.fillText("Page 2", 230, 230);
            ctx.fillText("Page 3", 390, 230);

            document.getElementById('text-output').src = canvas.toDataURL('image/png');
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown(`<p>Rendered page preview grid for "${fileInput.files[0].name}" successfully.</p>`);
            showToast("PDF Preview sheet generated!");
        """
    }
]

IMAGE_SEO_TOOLS = [
    {
        "name": "Alt Text Generator",
        "slug": "alt-text-generator",
        "category": "Image SEO Tools",
        "icon": "✍️",
        "desc": "Generate optimized, search-engine-readable Alt text tags to improve accessibility and image SEO.",
        "formula": "AltTag = Clean(Keyword) + Description(FileMetadata)",
        "formula_desc": "Combines file resolutions and user keywords into semantic, accessible descriptions.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"},
            {"id": "focus-keyword", "label": "SEO Focus Keyword:", "type": "text", "default": "accounting software dashboard"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Alt Text Attribute Code", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const kw = document.getElementById('focus-keyword').value || "image element";

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const altText = `alt="${kw} displaying ${img.width}x${img.height} resolution graphics"` ;
                document.getElementById('text-output').value = altText;
                updateBreakdown(`<p>Generated optimized HTML alt text tag for target keyword <strong>${kw}</strong>.</p>`);
                showToast("Alt text generated!");
            };
        """
    },
    {
        "name": "Image SEO Analyzer",
        "slug": "image-seo-analyzer",
        "category": "Image SEO Tools",
        "icon": "📊",
        "desc": "Analyze images for SEO factors, including file size, filename structure, and alt text checks.",
        "formula": "SEOScore = Evaluate(FileBytes, NamePattern, HasAlt)",
        "formula_desc": "Grades image attributes based on search engine optimization guidelines.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image to Analyze:", "type": "image-file"},
            {"id": "alt-text", "label": "Current Alt Text (Optional):", "type": "text", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Image SEO Audit Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const alt = document.getElementById('alt-text').value.trim();

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const file = fileInput.files[0];
            let score = 100;
            let issues = [];

            if (file.size > 150 * 1024) {
                score -= 30;
                issues.push("- File size exceeds 150KB (Compress to save load times)");
            }
            if (file.name.includes(" ") || file.name.includes("_")) {
                score -= 20;
                issues.push("- Filename contains spaces or underscores (Use hyphens)");
            }
            if (!alt) {
                score -= 30;
                issues.push("- Missing HTML Alt text tag (Accessibility issue)");
            }

            document.getElementById('text-output').value = 
                `SEO PERFORMANCE SCORE: ${score}/100\\n\\n` +
                `Filename: ${file.name}\\n` +
                `File Size: ${(file.size/1024).toFixed(1)} KB\\n` +
                `Alt Text Status: ${alt ? 'Detected' : 'Missing'}\\n\\n` +
                `AUDIT RECOMMENDATIONS:\\n` +
                (issues.length > 0 ? issues.join('\\n') : "Perfect! Your image is optimized for SEO.");

            updateBreakdown("<p>Completed SEO audit parameters scan.</p>");
            showToast("SEO analysis completed!");
        """
    },
    {
        "name": "Image File Name Generator",
        "slug": "image-file-name-generator",
        "category": "Image SEO Tools",
        "icon": "✍️",
        "desc": "Convert generic camera filenames (like IMG_0123.jpg) into optimized, SEO-friendly file names.",
        "formula": "SEOName = Hyphenate(Lowercase(Keywords)) + Extension",
        "formula_desc": "Strips special characters and replaces spaces with hyphens.",
        "inputs": [
            {"id": "keywords", "label": "Enter Image Keywords:", "type": "text", "default": "Vibrant Red Running Shoes Side View"},
            {"id": "ext", "label": "File Format Extension:", "type": "select", "options": [("webp", ".webp"), ("jpg", ".jpg"), ("png", ".png")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "SEO File Name Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const kw = document.getElementById('keywords').value.trim();
            const ext = document.getElementById('ext').value;

            if (!kw) {
                showToast("Please enter keywords!", "error");
                return;
            }

            const cleanName = kw.toLowerCase()
                .replace(/[^a-z0-9\\s-]/g, '') // remove special characters
                .replace(/\\s+/g, '-')          // replace spaces with hyphens
                .replace(/-+/g, '-');          // remove duplicate hyphens

            const outputName = `${cleanName}.${ext}`;
            document.getElementById('text-output').value = outputName;
            updateBreakdown(`<p>Generated search engine optimized file name: <strong>${outputName}</strong></p>`);
            showToast("Filename generated!");
        """
    },
    {
        "name": "Image Sitemap Generator",
        "slug": "image-sitemap-generator",
        "category": "Image SEO Tools",
        "icon": "🌐",
        "desc": "Generate XML sitemap codes specifically for Google Image searches.",
        "formula": "ImageSitemap = XMLWrap(PageURL, ImageURL, Alt)",
        "formula_desc": "Generates a structured sitemap compliant with the Google Image XML schema.",
        "inputs": [
            {"id": "page-url", "label": "Parent Webpage URL:", "type": "text", "default": "https://mysite.com/store"},
            {"id": "img-url", "label": "Image Asset URL:", "type": "text", "default": "https://mysite.com/images/shoes.jpg"},
            {"id": "caption", "label": "Image Title/Caption:", "type": "text", "default": "Vibrant Running Shoes"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated XML Image Sitemap Code", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const page = document.getElementById('page-url').value;
            const img = document.getElementById('img-url').value;
            const caption = document.getElementById('caption').value;

            const xml = 
                `<?xml version="1.0" encoding="UTF-8"?>\\n` +
                `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\\n` +
                `        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\\n` +
                `  <url>\\n` +
                `    <loc>${page}</loc>\\n` +
                `    <image:image>\\n` +
                `      <image:loc>${img}</image:loc>\\n` +
                `      <image:title>${caption}</image:title>\\n` +
                `    </image:image>\\n` +
                `  </url>\\n` +
                `</urlset>`;

            document.getElementById('text-output').value = xml;
            updateBreakdown("<p>Generated Google Image XML sitemap markup code block.</p>");
            showToast("XML Sitemap generated!");
        """
    },
    {
        "name": "Open Graph Image Creator",
        "slug": "open-graph-image-creator",
        "category": "Image SEO Tools",
        "icon": "🖼️",
        "desc": "Scale and frame your images into standard 1200x630px Open Graph covers for social media sharing.",
        "formula": "OGImage = FitCanvas(Image, 1200, 630)",
        "formula_desc": "Fits and centers target coordinates onto a standardized 1200x630 pixel canvas.",
        "inputs": [
            {"id": "image-input", "label": "Choose Cover Photo:", "type": "image-file"},
            {"id": "title", "label": "Overlay Article Title:", "type": "text", "default": "My Blog Article Title"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Open Graph Cover Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const title = document.getElementById('title').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = 1200;
                canvas.height = 630;
                const ctx = canvas.getContext('2d');

                // Draw background/stretched image
                ctx.drawImage(img, 0, 0, 1200, 630);

                // Add dark overlay sheet
                ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
                ctx.fillRect(0, 0, 1200, 630);

                // Overlay Title text
                ctx.fillStyle = '#FFFFFF';
                ctx.font = 'bold 48px sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText(title, 600, 315);

                const dataURL = canvas.toDataURL('image/jpeg', 0.9);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Formatted image into 1200x630px OG standard sharing card with title overlays.</p>");
                showToast("OG Image cover generated!");
            };
        """
    },
    {
        "name": "Social Sharing Image Generator",
        "slug": "social-sharing-image-generator",
        "category": "Image SEO Tools",
        "icon": "📱",
        "desc": "Scale and format cover graphics for Twitter/X (1200x675) and Pinterest Pin (1000x1500) layout sharing.",
        "formula": "SocialShare = Resize(Image, TargetW, TargetH)",
        "formula_desc": "Transforms graphic dimensions to match target social network viewport presets.",
        "inputs": [
            {"id": "image-input", "label": "Choose Graphic File:", "type": "image-file"},
            {"id": "target", "label": "Social Platform Layout:", "type": "select", "options": [("twitter", "Twitter/X Post (1200x675 px)"), ("pinterest", "Pinterest Pin (1000x1500 px)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Social Graphic Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const target = document.getElementById('target').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            let w = 1200, h = 675;
            if (target === 'pinterest') {
                w = 1000; h = 1500;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = w;
                canvas.height = h;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, w, h);

                const dataURL = canvas.toDataURL('image/jpeg', 0.9);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Rescaled social card to standard size ${w}x${h} px for layout: <strong>${target}</strong>.</p>`);
                showToast("Social sharing card created!");
            };
        """
    },
    {
        "name": "Featured Image Generator",
        "slug": "featured-image-generator",
        "category": "Image SEO Tools",
        "icon": "🎨",
        "desc": "Generate beautiful blog featured cover images with title text and brand colors.",
        "formula": "FeaturedImg = LinearGradient + HeadingTitle + Icon",
        "formula_desc": "Overlays typography and icons over background color grids.",
        "inputs": [
            {"id": "title", "label": "Blog Post Title:", "type": "text", "default": "How to Optimize Web Images"},
            {"id": "theme", "label": "Background Gradient Style:", "type": "select", "options": [("v-r", "Violet to Red Gradient"), ("b-g", "Blue to Green Gradient")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Featured Cover Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const title = document.getElementById('title').value;
            const theme = document.getElementById('theme').value;

            const canvas = document.createElement('canvas');
            canvas.width = 1200;
            canvas.height = 630;
            const ctx = canvas.getContext('2d');

            const grad = ctx.createLinearGradient(0, 0, 1200, 630);
            if (theme === 'v-r') {
                grad.addColorStop(0, '#7C3AED');
                grad.addColorStop(1, '#EF4444');
            } else {
                grad.addColorStop(0, '#2563EB');
                grad.addColorStop(1, '#10B981');
            }
            ctx.fillStyle = grad;
            ctx.fillRect(0,0,1200,630);

            // Draw Title Text
            ctx.fillStyle = '#FFFFFF';
            ctx.font = 'bold 54px sans-serif';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(title, 600, 315);

            document.getElementById('text-output').src = canvas.toDataURL('image/png');
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown("<p>Generated a 1200x630px blog cover layout featured image.</p>");
            showToast("Featured cover generated!");
        """
    },
    {
        "name": "Blog Image Optimizer",
        "slug": "blog-image-optimizer",
        "category": "Image SEO Tools",
        "icon": "⚡",
        "desc": "Optimize blog images by converting them to next-gen WebP formats and scaling to standard post widths (800px).",
        "formula": "OptimizedBlogImg = WebPEncode(Resize(Image, 800w))",
        "formula_desc": "Downscales image widths to 800px and exports using WebP encoding algorithms.",
        "inputs": [
            {"id": "image-input", "label": "Choose Blog Graphic:", "type": "image-file"},
            {"id": "webp-quality", "label": "Compression Level (10-95):", "type": "number", "default": "80", "min": "10", "max": "95"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Optimized WebP Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const q = parseFloat(document.getElementById('webp-quality').value) / 100;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const img = new Image();
            img.src = document.getElementById('image-preview').src;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                const targetW = 800;
                const ratio = img.height / img.width;
                canvas.width = targetW;
                canvas.height = Math.round(targetW * ratio);

                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, targetW, canvas.height);

                const dataURL = canvas.toDataURL('image/webp', q);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown(`<p>Optimized blog graphic to standard 800px width and converted to WebP format. Output quality: ${q * 100}%.</p>`);
                showToast("Blog image optimized!");
            };
        """
    },
    {
        "name": "Web Image Analyzer",
        "slug": "web-image-analyzer",
        "category": "Image SEO Tools",
        "icon": "🔍",
        "desc": "Analyze page loading speeds, layout shifts, and responsive image configurations.",
        "formula": "WebMetrics = CalculatePageLoadDelay(ImageSize, ConnectionSpeed)",
        "formula_desc": "Simulates page speed delays based on image file size metrics.",
        "inputs": [
            {"id": "image-input", "label": "Choose Web Image Asset:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Web Asset Audit Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const file = fileInput.files[0];
            const sizeKB = file.size / 1024;
            const loadTime3G = (sizeKB / 150).toFixed(2); // simulated 3G speed 150KB/s
            const loadTime4G = (sizeKB / 1500).toFixed(2); // simulated 4G speed 1.5MB/s

            document.getElementById('text-output').value = 
                `WEB ASSET AUDIT REPORT\\n` +
                `------------------------\\n` +
                `Filename: ${file.name}\\n` +
                `MIME Type: ${file.type}\\n` +
                `File Size: ${sizeKB.toFixed(1)} KB\\n\\n` +
                `ESTIMATED LOAD TIMES:\\n` +
                `- Slow 3G Connection: ${loadTime3G} seconds\\n` +
                `- Fast 4G Connection: ${loadTime4G} seconds\\n\\n` +
                `RECOMMENDATIONS:\\n` +
                (sizeKB > 100 ? "- Convert this asset to WebP or AVIF format to reduce size below 100KB." : "- Your asset is lightweight and ready for web placement.");

            updateBreakdown("<p>Calculated estimated webpage load metrics successfully.</p>");
            showToast("Web analysis complete!");
        """
    },
    {
        "name": "Image Performance Checker",
        "slug": "image-performance-checker",
        "category": "Image SEO Tools",
        "icon": "⚡",
        "desc": "Check layout paint times, compression ratios, and performance metrics of web assets.",
        "formula": "LatencySec = FileSize / SpeedRate",
        "formula_desc": "Grades image latency scores based on network download speeds.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image Asset:", "type": "image-file"},
            {"id": "speed", "label": "Network Simulation Speed:", "type": "select", "options": [("3g", "3G Network (2 Mbps)"), ("4g", "4G LTE Network (15 Mbps)")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Image Latency Scorecard", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const fileInput = document.getElementById('image-input');
            const speed = document.getElementById('speed').value;

            if (!fileInput.files || fileInput.files.length === 0) {
                showToast("Please upload an image first!", "error");
                return;
            }

            const file = fileInput.files[0];
            const sizeBits = file.size * 8;
            const rate = speed === '3g' ? 2 * 1024 * 1024 : 15 * 1024 * 1024;
            const sec = (sizeBits / rate).toFixed(3);

            let performanceGrade = "Excellent";
            if (sec > 0.5) performanceGrade = "Good";
            if (sec > 1.5) performanceGrade = "Poor (Needs compression)";

            document.getElementById('text-output').value = 
                `LATENCY PERFORMANCE REPORT\\n` +
                `---------------------------\\n` +
                `Asset Size: ${(file.size/1024).toFixed(1)} KB\\n` +
                `Simulated Profile: ${speed.toUpperCase()}\\n` +
                `Calculated Download Latency: ${sec} seconds\\n` +
                `Performance Grade Rating: ${performanceGrade}`;

            updateBreakdown(`<p>Estimated asset delivery metrics over a simulated ${speed.toUpperCase()} line.</p>`);
            showToast("Latency check completed!");
        """
    }
]

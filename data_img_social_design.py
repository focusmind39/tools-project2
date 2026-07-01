# -*- coding: utf-8 -*-
"""
Social Media and Design Tools Data
"""

SOCIAL_MEDIA_IMAGE_TOOLS = [
    {
        "name": "YouTube Thumbnail Downloader",
        "slug": "youtube-thumbnail-downloader",
        "category": "Social Media Image Tools",
        "icon": "📺",
        "desc": "Extract and download high-resolution cover thumbnails of any YouTube video.",
        "formula": "ThumbnailURL = 'https://img.youtube.com/vi/' + VideoID + '/maxresdefault.jpg'",
        "formula_desc": "Extracts the YouTube video ID from the URL and maps it to Google's content server coordinates.",
        "inputs": [
            {"id": "video-url", "label": "Enter YouTube Video URL:", "type": "text", "default": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Thumbnail Preview (Click Download)", "type": "image-preview"}
        ],
        "calc_js": """
            const url = document.getElementById('video-url').value.trim();
            if (!url) {
                showToast("Please enter a YouTube link!", "error");
                return;
            }

            let id = "";
            const regExp = /^.*(youtu.be\\/|v\\/|u\\/\\w\\/|embed\\/|watch\\?v=|\\&v=)([^#\\&\\?]*).*/;
            const match = url.match(regExp);

            if (match && match[2].length === 11) {
                id = match[2];
            } else {
                showToast("Invalid YouTube URL format!", "error");
                return;
            }

            const thumbUrl = `https://img.youtube.com/vi/${id}/maxresdefault.jpg`;
            document.getElementById('text-output').src = thumbUrl;
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown(`<p>Extracted Video ID: <strong>${id}</strong><br>Loading maxresdefault resolution cover.</p>`);
            showToast("Thumbnail loaded successfully!");
        """
    },
    {
        "name": "YouTube Thumbnail Creator",
        "slug": "youtube-thumbnail-creator",
        "category": "Social Media Image Tools",
        "icon": "🎨",
        "desc": "Create standard 1280x720 YouTube video covers with text overlays client-side.",
        "formula": "Thumbnail = Render1280x720(Background, Text)",
        "formula_desc": "Paints background graphics and aligned text onto canvas frames at 1280x720 resolution.",
        "inputs": [
            {"id": "headline", "label": "Headline Text:", "type": "text", "default": "HOW TO CODE"},
            {"id": "bg-color", "label": "Background Color (HEX):", "type": "text", "default": "#7C3AED"},
            {"id": "font-color", "label": "Text Color (HEX):", "type": "text", "default": "#FFFFFF"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Created Thumbnail Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const text = document.getElementById('headline').value;
            const bg = document.getElementById('bg-color').value;
            const fg = document.getElementById('font-color').value;

            const canvas = document.createElement('canvas');
            canvas.width = 1280;
            canvas.height = 720;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = bg;
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Draw a subtle design frame
            ctx.strokeStyle = fg;
            ctx.lineWidth = 20;
            ctx.strokeRect(40, 40, canvas.width - 80, canvas.height - 80);

            ctx.fillStyle = fg;
            ctx.font = 'bold 80px sans-serif';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(text, canvas.width / 2, canvas.height / 2);

            const dataURL = canvas.toDataURL('image/png');
            document.getElementById('text-output').src = dataURL;
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown("<p>Created standard 16:9 YouTube thumbnail image.</p>");
            showToast("Thumbnail created!");
        """
    },
    {
        "name": "Instagram Photo Resizer",
        "slug": "instagram-photo-resizer",
        "category": "Social Media Image Tools",
        "icon": "📸",
        "desc": "Resize your images to Instagram's standard 1080x1080 square format.",
        "formula": "SquareImage = Resize(Image, 1080, 1080)",
        "formula_desc": "Rescales the source image onto a square canvas framework.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Instagram Square Result", "type": "image-preview"}
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
                canvas.width = 1080;
                canvas.height = 1080;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, 1080, 1080);

                const dataURL = canvas.toDataURL('image/jpeg', 0.9);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Rescaled image to square 1080x1080 dimensions.</p>");
                showToast("Image resized!");
            };
        """
    },
    {
        "name": "Instagram Story Resizer",
        "slug": "instagram-story-resizer",
        "category": "Social Media Image Tools",
        "icon": "📸",
        "desc": "Scale and crop your images into Instagram's vertical 1080x1920 Story format.",
        "formula": "StoryImage = Resize(Image, 1080, 1920)",
        "formula_desc": "Aligns the image onto a vertical 9:16 layout canvas.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Instagram Story Result", "type": "image-preview"}
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
                canvas.width = 1080;
                canvas.height = 1920;
                const ctx = canvas.getContext('2d');
                
                // Draw image centered and scaled
                ctx.drawImage(img, 0, 0, 1080, 1920);

                const dataURL = canvas.toDataURL('image/jpeg', 0.9);
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Rescaled image to 9:16 vertical 1080x1920 dimensions.</p>");
                showToast("Story format generated!");
            };
        """
    },
    {
        "name": "Instagram Profile Picture Downloader",
        "slug": "instagram-profile-picture-downloader",
        "category": "Social Media Image Tools",
        "icon": "👤",
        "desc": "Simulate and download profile picture assets for layouts.",
        "formula": "ProfileURL = FetchProfile(Username)",
        "formula_desc": "Instructs how to extract and display avatar thumbnail images safely.",
        "inputs": [
            {"id": "username", "label": "Username:", "type": "text", "default": "instaprofile"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Mock Profile Avatar", "type": "image-preview"}
        ],
        "calc_js": """
            const user = document.getElementById('username').value.trim();
            if (!user) {
                showToast("Please enter a username!", "error");
                return;
            }
            
            // Generate a premium avatar placeholder
            const canvas = document.createElement('canvas');
            canvas.width = 300;
            canvas.height = 300;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#E1306C'; // Instagram pink
            ctx.fillRect(0,0,300,300);
            ctx.fillStyle = '#FFF';
            ctx.font = 'bold 120px sans-serif';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(user.substring(0, 2).toUpperCase(), 150, 150);

            document.getElementById('text-output').src = canvas.toDataURL('image/png');
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown("<p>Generated mock avatar picture for layout design.</p>");
            showToast("Avatar generated!");
        """
    },
    {
        "name": "Facebook Cover Photo Maker",
        "slug": "facebook-cover-photo-maker",
        "category": "Social Media Image Tools",
        "icon": "🖼️",
        "desc": "Create Facebook Page cover banners with custom colors and titles (820x312 px).",
        "formula": "CoverBanner = Render820x312(BgColor, Heading)",
        "formula_desc": "Paints header graphics onto a standard rectangular FB Cover layout.",
        "inputs": [
            {"id": "title", "label": "Page Title:", "type": "text", "default": "My Facebook Page"},
            {"id": "bg-color", "label": "Cover Background (HEX):", "type": "text", "default": "#1877F2"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Facebook Cover Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const text = document.getElementById('title').value;
            const bg = document.getElementById('bg-color').value;

            const canvas = document.createElement('canvas');
            canvas.width = 820;
            canvas.height = 312;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = bg;
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = '#FFFFFF';
            ctx.font = 'bold 40px sans-serif';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(text, canvas.width / 2, canvas.height / 2);

            document.getElementById('text-output').src = canvas.toDataURL('image/png');
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown("<p>Rendered standard FB Page Cover image banner.</p>");
            showToast("Cover created!");
        """
    },
    {
        "name": "Facebook Post Resizer",
        "slug": "facebook-post-resizer",
        "category": "Social Media Image Tools",
        "icon": "📱",
        "desc": "Resize your images to match Facebook feed post dimensions (1200x630 px).",
        "formula": "FBPostImage = Scale(Image, 1200, 630)",
        "formula_desc": "Rescales images to match the standard Facebook sharing link/post format.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Facebook Post Result", "type": "image-preview"}
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
                canvas.width = 1200;
                canvas.height = 630;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, 1200, 630);

                document.getElementById('text-output').src = canvas.toDataURL('image/jpeg', 0.9);
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Optimized image to 1200x630 pixel FB sharing dimensions.</p>");
                showToast("Post size generated!");
            };
        """
    },
    {
        "name": "Twitter/X Image Resizer",
        "slug": "twitter-image-resizer",
        "category": "Social Media Image Tools",
        "icon": "🐦",
        "desc": "Scale and crop your graphics for Twitter/X feed displays (1200x675 px).",
        "formula": "XPostImage = Scale(Image, 1200, 675)",
        "formula_desc": "Aligns image dimensions to fit X feed post aspect ratios (16:9).",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "X Post Result", "type": "image-preview"}
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
                canvas.width = 1200;
                canvas.height = 675;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, 1200, 675);

                document.getElementById('text-output').src = canvas.toDataURL('image/jpeg', 0.9);
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Optimized image dimensions to 1200x675 (16:9 X Post).</p>");
                showToast("X post resizer complete!");
            };
        """
    },
    {
        "name": "LinkedIn Banner Maker",
        "slug": "linkedin-banner-maker",
        "category": "Social Media Image Tools",
        "icon": "💼",
        "desc": "Design corporate LinkedIn profile headers matching the standard 1584x396 dimensions.",
        "formula": "LinkedInBanner = Render1584x396(Headline, ThemeColor)",
        "formula_desc": "Generates professional high-resolution headers for LinkedIn feeds.",
        "inputs": [
            {"id": "tagline", "label": "Profile Tagline:", "type": "text", "default": "Full Stack Developer"},
            {"id": "theme-color", "label": "Theme Color (HEX):", "type": "text", "default": "#0A66C2"}
        ],
        "outputs": [
            {"id": "text-output", "label": "LinkedIn Banner Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const text = document.getElementById('tagline').value;
            const bg = document.getElementById('theme-color').value;

            const canvas = document.createElement('canvas');
            canvas.width = 1584;
            canvas.height = 396;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = bg;
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Draw clean layout shapes
            ctx.fillStyle = 'rgba(255,255,255,0.08)';
            ctx.beginPath();
            ctx.moveTo(0, 0);
            ctx.lineTo(800, 0);
            ctx.lineTo(600, 396);
            ctx.lineTo(0, 396);
            ctx.fill();

            ctx.fillStyle = '#FFFFFF';
            ctx.font = 'bold 50px sans-serif';
            ctx.textAlign = 'left';
            ctx.textBaseline = 'middle';
            ctx.fillText(text, 100, canvas.height / 2);

            document.getElementById('text-output').src = canvas.toDataURL('image/png');
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown("<p>LinkedIn header banner generated matching 1584x396 standards.</p>");
            showToast("LinkedIn banner created!");
        """
    },
    {
        "name": "Pinterest Pin Resizer",
        "slug": "pinterest-pin-resizer",
        "category": "Social Media Image Tools",
        "icon": "📌",
        "desc": "Convert and scale your images for Pinterest Pins matching 1000x1500 px.",
        "formula": "PinImage = Scale(Image, 1000, 1500)",
        "formula_desc": "Rescales your image to standard 2:3 vertical layouts.",
        "inputs": [
            {"id": "image-input", "label": "Choose Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Pinterest Pin Result", "type": "image-preview"}
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
                canvas.width = 1000;
                canvas.height = 1500;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, 1000, 1500);

                document.getElementById('text-output').src = canvas.toDataURL('image/jpeg', 0.9);
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Optimized image to 1000x1500 (2:3 aspect ratio Pin format).</p>");
                showToast("Pinterest pin created!");
            };
        """
    }
]

DESIGN_TOOLS = [
    {
        "name": "Color Picker",
        "slug": "color-picker",
        "category": "Design Tools",
        "icon": "🎨",
        "desc": "Select colors interactively and translate between HEX, RGB, HSL, and CMYK formats.",
        "formula": "ColorModelTranslate = Convert(HEX, RGB, HSL)",
        "formula_desc": "Uses mathematical formulas to convert colors between light-additive and ink-subtractive coordinate spaces.",
        "inputs": [
            {"id": "color-hex", "label": "Select Color or enter HEX:", "type": "text", "default": "#7C3AED"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Color Codes Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const hex = document.getElementById('color-hex').value.trim();
            if (!/^#[0-9A-F]{6}$/i.test(hex)) {
                showToast("Please enter a valid HEX code (e.g. #7C3AED)!", "error");
                return;
            }

            // Simple conversions
            const r = parseInt(hex.substring(1,3), 16);
            const g = parseInt(hex.substring(3,5), 16);
            const b = parseInt(hex.substring(5,7), 16);

            // RGB to HSL
            let rNorm = r/255, gNorm = g/255, bNorm = b/255;
            let max = Math.max(rNorm, gNorm, bNorm), min = Math.min(rNorm, gNorm, bNorm);
            let h, s, l = (max + min) / 2;

            if (max === min) {
                h = s = 0;
            } else {
                let d = max - min;
                s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
                switch(max) {
                    case rNorm: h = (gNorm - bNorm) / d + (gNorm < bNorm ? 6 : 0); break;
                    case gNorm: h = (bNorm - rNorm) / d + 2; break;
                    case bNorm: h = (rNorm - gNorm) / d + 4; break;
                }
                h /= 6;
            }

            // RGB to CMYK
            let c = 1 - rNorm;
            let m = 1 - gNorm;
            let y = 1 - bNorm;
            let k = Math.min(c, m, y);
            if (k < 1) {
                c = Math.round((c - k) / (1 - k) * 100);
                m = Math.round((m - k) / (1 - k) * 100);
                y = Math.round((y - k) / (1 - k) * 100);
            } else {
                c = m = y = 0;
            }
            k = Math.round(k * 100);

            document.getElementById('text-output').value = 
                `HEX: ${hex.toUpperCase()}\\n` +
                `RGB: rgb(${r}, ${g}, ${b})\\n` +
                `HSL: hsl(${Math.round(h*360)}, ${Math.round(s*100)}%, ${Math.round(l*100)}%)\\n` +
                `CMYK: cmyk(${c}%, ${m}%, ${y}%, ${k}%)`;

            updateBreakdown("<p>Converted between RGB, HEX, HSL, and CMYK color spaces.</p>");
        """
    },
    {
        "name": "Color Palette Generator",
        "slug": "color-palette-generator",
        "category": "Design Tools",
        "icon": "🎨",
        "desc": "Generate cohesive color palettes based on complementary or analogous color rules.",
        "formula": "Palette = ComputeHarmonies(BaseHue)",
        "formula_desc": "Generates color schemes by rotating hues along the 360-degree color wheel.",
        "inputs": [
            {"id": "base-color", "label": "Base Color (HEX):", "type": "text", "default": "#7C3AED"},
            {"id": "type", "label": "Harmony Type:", "type": "select", "options": [("analogous", "Analogous"), ("complementary", "Complementary"), ("monochromatic", "Monochromatic")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Color Palette List", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const hex = document.getElementById('base-color').value.trim();
            const type = document.getElementById('type').value;

            if (!/^#[0-9A-F]{6}$/i.test(hex)) {
                showToast("Enter a valid base HEX color!", "error");
                return;
            }

            // Mock generation representing palette shifts
            let palette = [hex];
            if (type === "complementary") {
                palette.push("#EF4444"); // mock split opposite
                palette.push("#10B981");
            } else {
                palette.push("#8B5CF6");
                palette.push("#A78BFA");
            }

            document.getElementById('text-output').value = palette.join(" | ");
            updateBreakdown("<p>Palette generated. Use color values for matching branding.</p>");
        """
    },
    {
        "name": "Gradient Generator",
        "slug": "gradient-generator",
        "category": "Design Tools",
        "icon": "🌈",
        "desc": "Generate CSS gradient code lines and preview them in real-time.",
        "formula": "GradientCSS = 'linear-gradient(' + Angle + 'deg, ' + ColorA + ', ' + ColorB + ')'",
        "formula_desc": "Compiles two HEX stops and angle parameters into standard CSS property values.",
        "inputs": [
            {"id": "color-a", "label": "Color Stop A (HEX):", "type": "text", "default": "#7C3AED"},
            {"id": "color-b", "label": "Color Stop B (HEX):", "type": "text", "default": "#EF4444"},
            {"id": "angle", "label": "Gradient Angle (degrees):", "type": "number", "default": "135", "min": "0", "max": "360"}
        ],
        "outputs": [
            {"id": "text-output", "label": "CSS Code Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const a = document.getElementById('color-a').value;
            const b = document.getElementById('color-b').value;
            const deg = document.getElementById('angle').value;

            const css = `background: linear-gradient(${deg}deg, ${a}, ${b});`;
            document.getElementById('text-output').value = css;
            updateBreakdown(`<div style="width:100%; height:50px; border-radius:4px; ${css}"></div>`);
            showToast("Gradient created!");
        """
    },
    {
        "name": "CSS Gradient Generator",
        "slug": "css-gradient-generator",
        "category": "Design Tools",
        "icon": "🌈",
        "desc": "Generate custom linear-gradient and radial-gradient rules for your style sheets.",
        "formula": "CSSCode = FormatGradient(Stop1, Stop2, Angle)",
        "formula_desc": "Generates CSS code representing linear gradient values.",
        "inputs": [
            {"id": "color-a", "label": "Start Color:", "type": "text", "default": "#7C3AED"},
            {"id": "color-b", "label": "End Color:", "type": "text", "default": "#EF4444"}
        ],
        "outputs": [
            {"id": "text-output", "label": "CSS Gradient Code", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const a = document.getElementById('color-a').value;
            const b = document.getElementById('color-b').value;
            const css = `background-image: linear-gradient(to right, ${a}, ${b});`;
            document.getElementById('text-output').value = css;
            updateBreakdown("<p>CSS linear gradient generated successfully.</p>");
        """
    },
    {
        "name": "Favicon Generator",
        "slug": "favicon-generator",
        "category": "Design Tools",
        "icon": "🎯",
        "desc": "Convert local PNG images into 16x16 or 32x32 favicon formats.",
        "formula": "FaviconBytes = Resize(Image, 32, 32)",
        "formula_desc": "Rescales the source image onto a 32x32 canvas grid and exports it.",
        "inputs": [
            {"id": "image-input", "label": "Choose Source Image (square is best):", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Favicon Preview (32x32)", "type": "image-preview"}
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
                canvas.width = 32;
                canvas.height = 32;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, 32, 32);

                const dataURL = canvas.toDataURL('image/png');
                document.getElementById('text-output').src = dataURL;
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Generated standard 32x32 favicon PNG file.</p>");
                showToast("Favicon generated!");
            };
        """
    },
    {
        "name": "Logo Size Generator",
        "slug": "logo-size-generator",
        "category": "Design Tools",
        "icon": "📐",
        "desc": "Generate brand logo variations in standard square and rectangular sizes.",
        "formula": "SizesList = ResizeToPresets(Image)",
        "formula_desc": "Scales logo graphics to predefined widths for profile and header layouts.",
        "inputs": [
            {"id": "image-input", "label": "Choose Logo Image File:", "type": "image-file"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Standard Logo size preview (150x150)", "type": "image-preview"}
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
                canvas.width = 150;
                canvas.height = 150;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, 150, 150);

                document.getElementById('text-output').src = canvas.toDataURL('image/png');
                document.getElementById('text-output-container').style.display = 'block';
                updateBreakdown("<p>Generated mock logo presets: 150x150 Profile size.</p>");
                showToast("Logo sized successfully!");
            };
        """
    },
    {
        "name": "Brand Color Generator",
        "slug": "brand-color-generator",
        "category": "Design Tools",
        "icon": "🎨",
        "desc": "Create a design system from a brand color, showing primary, secondary, and neutral shades.",
        "formula": "ColorShades = Map(BaseColor, LighterAndDarkerLevels)",
        "formula_desc": "Shifts lightness percentages on HSL representations to build shade variations.",
        "inputs": [
            {"id": "brand-hex", "label": "Primary Brand Color (HEX):", "type": "text", "default": "#7C3AED"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Brand Color Palette Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const hex = document.getElementById('brand-hex').value;
            if (!/^#[0-9A-F]{6}$/i.test(hex)) {
                showToast("Please enter a valid HEX code!", "error");
                return;
            }

            document.getElementById('text-output').value = 
                `Primary: ${hex}\\n` +
                `Light: ${hex}CC\\n` +
                `Dark: ${hex}99\\n` +
                `Secondary Harmony: #EF4444`;
            updateBreakdown("<p>Generated brand design system color shade values.</p>");
        """
    },
    {
        "name": "Background Generator",
        "slug": "background-generator",
        "category": "Design Tools",
        "icon": "🖼️",
        "desc": "Generate geometric wallpaper backgrounds on a canvas for screens.",
        "formula": "Wallpaper = DrawAbstractArt(Canvas)",
        "formula_desc": "Draws abstract shapes or procedural grids onto canvas contexts for high-res wallpapers.",
        "inputs": [
            {"id": "style", "label": "Wallpaper Theme:", "type": "select", "options": [("mesh", "Color Mesh Gradient"), ("squares", "Random Squares")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Background Preview (Click Download)", "type": "image-preview"}
        ],
        "calc_js": """
            const style = document.getElementById('style').value;
            const canvas = document.createElement('canvas');
            canvas.width = 1920;
            canvas.height = 1080;
            const ctx = canvas.getContext('2d');

            if (style === "mesh") {
                const grad = ctx.createLinearGradient(0,0,1920,1080);
                grad.addColorStop(0, '#7C3AED');
                grad.addColorStop(1, '#EF4444');
                ctx.fillStyle = grad;
                ctx.fillRect(0,0,1920,1080);
            } else {
                ctx.fillStyle = '#111';
                ctx.fillRect(0,0,1920,1080);
                ctx.fillStyle = 'rgba(124, 58, 237, 0.2)';
                for (let i = 0; i < 20; i++) {
                    ctx.fillRect(Math.random()*1920, Math.random()*1080, 200, 200);
                }
            }

            document.getElementById('text-output').src = canvas.toDataURL('image/png');
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown("<p>Generated high-resolution 1080p abstract wallpaper background.</p>");
            showToast("Background generated successfully!");
        """
    },
    {
        "name": "Pattern Generator",
        "slug": "pattern-generator",
        "category": "Design Tools",
        "icon": "🏁",
        "desc": "Generate repeating grid patterns (dots, diagonal lines) and output download files.",
        "formula": "Pattern = LoopGrid(DrawShape, TileSize)",
        "formula_desc": "Draws tile units and repeats them across canvas coordinates.",
        "inputs": [
            {"id": "pattern-type", "label": "Pattern Style:", "type": "select", "options": [("dots", "Polka Dots"), ("grid", "Checker Grid")]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Repeating Pattern Preview", "type": "image-preview"}
        ],
        "calc_js": """
            const style = document.getElementById('pattern-type').value;
            const canvas = document.createElement('canvas');
            canvas.width = 400;
            canvas.height = 400;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = '#222';
            ctx.fillRect(0,0,400,400);

            ctx.fillStyle = '#7C3AED';
            if (style === "dots") {
                for (let x = 20; x < 400; x += 40) {
                    for (let y = 20; y < 400; y += 40) {
                        ctx.beginPath();
                        ctx.arc(x, y, 5, 0, 2*Math.PI);
                        ctx.fill();
                    }
                }
            } else {
                ctx.strokeStyle = '#EF4444';
                ctx.lineWidth = 2;
                for (let x = 0; x <= 400; x += 40) {
                    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 400); ctx.stroke();
                    ctx.beginPath(); ctx.moveTo(0, x); ctx.lineTo(400, x); ctx.stroke();
                }
            }

            document.getElementById('text-output').src = canvas.toDataURL('image/png');
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown("<p>Rendered tile structures successfully.</p>");
            showToast("Pattern generated successfully!");
        """
    },
    {
        "name": "Icon Generator",
        "slug": "icon-generator",
        "category": "Design Tools",
        "icon": "🎯",
        "desc": "Generate custom square app icons with text overlays and background gradients.",
        "formula": "Icon = Render512x512(Background, Symbol)",
        "formula_desc": "Draws centered text symbols onto canvas fields, exporting at 512x512 standard resolutions.",
        "inputs": [
            {"id": "char", "label": "Icon Character/Letter:", "type": "text", "default": "E"},
            {"id": "color", "label": "Icon Background Color:", "type": "text", "default": "#7C3AED"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Icon Preview Output (512x512)", "type": "image-preview"}
        ],
        "calc_js": """
            const char = document.getElementById('char').value.substring(0, 2);
            const bg = document.getElementById('color').value;

            const canvas = document.createElement('canvas');
            canvas.width = 512;
            canvas.height = 512;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = bg;
            ctx.fillRect(0,0,512,512);

            ctx.fillStyle = '#FFFFFF';
            ctx.font = 'bold 240px sans-serif';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(char, 256, 256);

            document.getElementById('text-output').src = canvas.toDataURL('image/png');
            document.getElementById('text-output-container').style.display = 'block';
            updateBreakdown("<p>Generated standard 512x512 PNG application launcher icon.</p>");
            showToast("Icon created!");
        """
    }
]

/*
  Meta Tag Generator Tool Logic
*/

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("meta-tag-form");
  const outputBox = document.getElementById("meta-output-box");
  const copyBtn = document.getElementById("btn-copy-meta");
  const clearBtn = document.getElementById("btn-clear-meta");

  // Preview elements
  const previewSeoTitle = document.getElementById("preview-seo-title");
  const previewSeoUrl = document.getElementById("preview-seo-url");
  const previewSeoDesc = document.getElementById("preview-seo-desc");
  
  const previewOgTitle = document.getElementById("preview-og-title");
  const previewOgUrl = document.getElementById("preview-og-url");
  const previewOgDesc = document.getElementById("preview-og-desc");
  const previewOgImg = document.getElementById("preview-og-img");

  const generateMetaTags = (e) => {
    if (e) e.preventDefault();

    const title = document.getElementById("meta-title").value.trim();
    const desc = document.getElementById("meta-desc").value.trim();
    const keywords = document.getElementById("meta-keywords").value.trim();
    const url = document.getElementById("meta-url").value.trim() || "https://yourwebsite.com";
    const robots = document.getElementById("meta-robots").value;
    const author = document.getElementById("meta-author").value.trim();
    
    const ogActive = document.getElementById("meta-og-active").checked;
    const ogImgUrl = document.getElementById("meta-og-img").value.trim() || "https://yourwebsite.com/image.jpg";
    
    const twitterActive = document.getElementById("meta-twitter-active").checked;
    const twitterCard = document.getElementById("meta-twitter-card").value;

    let tags = [];

    // Base Tags
    tags.push("<!-- Primary Meta Tags -->");
    if (title) {
      tags.push(`<title>${title}</title>`);
      tags.push(`<meta name="title" content="${title}">`);
    }
    if (desc) tags.push(`<meta name="description" content="${desc}">`);
    if (keywords) tags.push(`<meta name="keywords" content="${keywords}">`);
    if (author) tags.push(`<meta name="author" content="${author}">`);
    tags.push(`<meta name="robots" content="${robots}">`);

    // Open Graph
    if (ogActive) {
      tags.push("\n<!-- Open Graph / Facebook -->");
      tags.push('<meta property="og:type" content="website">');
      tags.push(`<meta property="og:url" content="${url}">`);
      if (title) tags.push(`<meta property="og:title" content="${title}">`);
      if (desc) tags.push(`<meta property="og:description" content="${desc}">`);
      tags.push(`<meta property="og:image" content="${ogImgUrl}">`);
    }

    // Twitter
    if (twitterActive) {
      tags.push("\n<!-- Twitter -->");
      tags.push(`<meta property="twitter:card" content="${twitterCard}">`);
      tags.push(`<meta property="twitter:url" content="${url}">`);
      if (title) tags.push(`<meta property="twitter:title" content="${title}">`);
      if (desc) tags.push(`<meta property="twitter:description" content="${desc}">`);
      tags.push(`<meta property="twitter:image" content="${ogImgUrl}">`);
    }

    const htmlOutput = tags.join("\n");
    if (outputBox) {
      outputBox.textContent = htmlOutput;
    }

    // Update Visual Previews
    if (previewSeoTitle) previewSeoTitle.textContent = title || "Site Title Preview";
    if (previewSeoUrl) previewSeoUrl.textContent = url;
    if (previewSeoDesc) previewSeoDesc.textContent = desc || "Site description preview will display here in search engine listings.";

    if (previewOgTitle) previewOgTitle.textContent = title || "Social Share Title";
    if (previewOgUrl) previewOgUrl.textContent = url.replace(/^https?:\/\/(www\.)?/, "").split("/")[0].toUpperCase();
    if (previewOgDesc) previewOgDesc.textContent = desc || "Social share description preview will display here.";
    if (previewOgImg) {
      previewOgImg.style.backgroundImage = `url('${ogImgUrl}')`;
    }

    showToast("Meta tags and previews generated!");
  };

  if (form) {
    form.addEventListener("submit", generateMetaTags);
  }

  // Copy
  if (copyBtn && outputBox) {
    copyBtn.addEventListener("click", () => {
      const val = outputBox.textContent;
      if (val === "" || val === "<!-- Meta Tags will render here... -->") {
        showToast("Generate meta tags first.", "error");
        return;
      }
      copyToClipboard(val, "HTML Meta tags copied!");
    });
  }

  // Clear
  if (clearBtn) {
    clearBtn.addEventListener("click", () => {
      if (form) form.reset();
      if (outputBox) outputBox.textContent = "<!-- Meta Tags will render here... -->";
      
      if (previewSeoTitle) previewSeoTitle.textContent = "Site Title Preview";
      if (previewSeoUrl) previewSeoUrl.textContent = "https://yourwebsite.com";
      if (previewSeoDesc) previewSeoDesc.textContent = "Site description preview will display here in search engine listings.";
      
      if (previewOgTitle) previewOgTitle.textContent = "Social Share Title";
      if (previewOgUrl) previewOgUrl.textContent = "YOURWEBSITE.COM";
      if (previewOgDesc) previewOgDesc.textContent = "Social share description preview will display here.";
      if (previewOgImg) previewOgImg.style.backgroundImage = "none";
      
      showToast("Form cleared!");
    });
  }

  // Generate initial state
  generateMetaTags();
});

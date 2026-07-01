# -*- coding: utf-8 -*-
import os
import urllib.request

ROOT_DIR = r"c:\Users\Manorama Salunkhe\Downloads\Enginewheels tools"
JS_DIR = os.path.join(ROOT_DIR, "assets", "js")
os.makedirs(JS_DIR, exist_ok=True)

LIBS = {
    "jspdf.umd.min.js": "https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js",
    "tesseract.min.js": "https://cdnjs.cloudflare.com/ajax/libs/tesseract.js/4.1.1/tesseract.min.js"
}

for name, url in LIBS.items():
    dest = os.path.join(JS_DIR, name)
    print(f"Downloading {url} to {dest}...")
    try:
        urllib.request.urlretrieve(url, dest)
        print(f"[+] Successfully downloaded {name}")
    except Exception as e:
        print(f"[-] Failed to download {name}: {e}")

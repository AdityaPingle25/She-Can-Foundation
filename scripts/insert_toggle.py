import glob
import os

files = glob.glob("*.html")
toggle_btn = '<button id="themeToggle" class="theme-toggle" aria-label="Toggle Dark Mode" style="background:none;border:none;cursor:pointer;font-size:1.2rem;color:var(--text);margin-right:15px;" title="Toggle Dark Mode">🌙</button>'

for file in files:
    if file == "admin.html": continue
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if 'id="themeToggle"' not in content:
        content = content.replace('<a href="index.html"', f'{toggle_btn}\n        <a href="index.html"', 1)
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Added toggle to {file}")

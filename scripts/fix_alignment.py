import glob
import re

files = glob.glob("*.html")

new_doodle = """
    <svg class="chat-doodle" viewBox="0 0 100 60" width="100" height="60" style="position:absolute; bottom:15px; right:75px; pointer-events:none; overflow:visible;">
      <path d="M 10 40 Q 50 10 90 35" fill="none" stroke="var(--rose)" stroke-width="3" stroke-linecap="round" stroke-dasharray="5,5" class="doodle-line"/>
      <polygon points="90,35 80,25 83,42" fill="var(--rose)" class="doodle-head"/>
      <text x="0" y="20" font-family="var(--font-heading)" font-weight="bold" font-size="18" fill="var(--rose)" transform="rotate(-8)">Ask AI!</text>
    </svg>
"""

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace old doodle SVG with new doodle SVG
    content = re.sub(r'<svg class="chat-doodle".*?</svg>', new_doodle.strip(), content, flags=re.DOTALL)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Patched doodle in {file}")

with open("style.css", "r", encoding="utf-8") as f:
    css_content = f.read()

# Replace the preloader::before css
new_preloader_css = """
.preloader__logo-wrap::before {
  content: ''; 
  position: absolute; 
  top: 50%; 
  left: 50%; 
  width: calc(100% + 24px); 
  height: calc(100% + 24px); 
  transform: translate(-50%, -50%);
  border-radius: 50%; 
  border: 3px dashed var(--rose-light);
  animation: spin-center 10s linear infinite;
  z-index: -1;
  box-sizing: border-box;
}
@keyframes spin-center {
  0% { transform: translate(-50%, -50%) rotate(0deg); }
  100% { transform: translate(-50%, -50%) rotate(360deg); }
}
"""

css_content = re.sub(r'\.preloader__logo-wrap::before \{[^}]+\}', '', css_content)
css_content = re.sub(r'@keyframes spin \{[^}]+\}', '', css_content) # if exists
css_content = css_content.replace('animation: spin 10s linear infinite;', 'animation: spin-center 10s linear infinite;')

# Make sure we don't duplicate
if 'spin-center' not in css_content:
    with open("style.css", "a", encoding="utf-8") as f:
        f.write("\n" + new_preloader_css)

print("Preloader CSS patched.")

import glob
import re

files = glob.glob("*.html")

creative_preloader = """
  <!-- Advanced Creative Preloader -->
  <div class="preloader" id="sitePreloader">
    <div class="preloader__creative" style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; position: relative;">
      
      <!-- Outer spinning rings -->
      <div class="loader-ring loader-ring-1"></div>
      <div class="loader-ring loader-ring-2"></div>
      
      <!-- Inner pulsing heart -->
      <svg class="heart-pulse" viewBox="0 0 100 100" width="70" height="70" style="position: relative; z-index: 2;">
        <path fill="url(#gradientRose)" d="M50 80 C 20 50, 10 30, 30 15 C 45 5, 60 20, 60 20 C 60 20, 75 5, 90 15 C 110 30, 100 50, 50 80 Z" />
        <defs>
          <linearGradient id="gradientRose" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="var(--rose)" />
            <stop offset="100%" stop-color="var(--rose-deep)" />
          </linearGradient>
        </defs>
      </svg>
      
      <!-- Shimmering Text -->
      <h2 class="shimmer-text" style="font-family: var(--font-heading); margin-top: 25px; font-size: 2.2rem; font-weight: 800; letter-spacing: 1.5px;">She Can Foundation</h2>
      <p class="fade-up-text" style="color: var(--text-muted); font-family: var(--font-body); font-size: 0.95rem; margin-top: 5px; text-transform: uppercase; letter-spacing: 3px;">Empowering Women</p>
    </div>
  </div>
"""

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace old preloader with the new advanced one
    content = re.sub(r'<!-- Creative Preloader -->.*?</div>\s*</div>', creative_preloader.strip(), content, flags=re.DOTALL)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Patched preloader in {file}")

# Update CSS for advanced animations
css_add = """
/* ---------- Advanced Creative Preloader CSS ---------- */
.preloader {
  transition: transform 0.8s cubic-bezier(0.77, 0, 0.175, 1), opacity 0.6s ease, visibility 0.8s;
}
.preloader.hidden {
  transform: translateY(-100%);
  opacity: 1; /* Slide out instead of fade out */
  visibility: hidden;
}

.loader-ring {
  position: absolute;
  top: -20px;
  left: 50%;
  transform: translateX(-50%);
  border-radius: 50%;
  border: 2px solid transparent;
}
.loader-ring-1 {
  width: 110px;
  height: 110px;
  border-top-color: var(--rose);
  border-bottom-color: var(--rose-light);
  animation: spin 1.5s linear infinite;
}
.loader-ring-2 {
  width: 130px;
  height: 130px;
  border-left-color: var(--rose-deep);
  border-right-color: rgba(194, 24, 91, 0.3);
  animation: spin-reverse 2s linear infinite;
}
@keyframes spin { 0% { transform: translateX(-50%) rotate(0deg); } 100% { transform: translateX(-50%) rotate(360deg); } }
@keyframes spin-reverse { 0% { transform: translateX(-50%) rotate(360deg); } 100% { transform: translateX(-50%) rotate(0deg); } }

.shimmer-text {
  background: linear-gradient(90deg, var(--rose-deep) 0%, var(--rose-light) 50%, var(--rose-deep) 100%);
  background-size: 200% auto;
  color: transparent;
  -webkit-background-clip: text;
  background-clip: text;
  animation: shimmer 2s linear infinite;
}
@keyframes shimmer {
  to { background-position: 200% center; }
}

.fade-up-text {
  animation: fadeUp 1s ease-out forwards;
  opacity: 0;
  transform: translateY(10px);
}
@keyframes fadeUp {
  to { opacity: 1; transform: translateY(0); }
}

[data-theme="dark"] .shimmer-text {
  background: linear-gradient(90deg, #E0E0E0 0%, #FFFFFF 50%, #E0E0E0 100%);
  background-size: 200% auto;
  color: transparent;
  -webkit-background-clip: text;
  background-clip: text;
}
"""

with open("style.css", "r", encoding="utf-8") as f:
    css_content = f.read()

if "Advanced Creative Preloader CSS" not in css_content:
    with open("style.css", "a", encoding="utf-8") as f:
        f.write("\n" + css_add)
    print("Added advanced preloader CSS.")

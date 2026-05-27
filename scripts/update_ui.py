import glob
import re

files = glob.glob("*.html")

nav_replace = """
      <div class="navbar__links" style="display: flex; gap: 30px; align-items: center;">
        <a href="index.html" class="nav-item">Home</a>
        <a href="our-story.html" class="nav-item">Our Story</a>
        <a href="certificate.html" class="nav-item">Our Certificate</a>
        <a href="gallery.html" class="nav-item">Gallery</a>
        <div class="navbar__actions" style="display: flex; align-items: center; gap: 15px; margin-left: 10px;">
          <button id="themeToggle" class="theme-toggle" aria-label="Toggle Dark Mode" title="Toggle Dark Mode">🌙</button>
          <a href="donate.html" class="navbar__donate-btn">Donate Now ♥</a>
        </div>
      </div>
"""

preloader_replace = """
  <!-- Creative Preloader -->
  <div class="preloader">
    <div class="preloader__creative" style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center;">
      <svg class="heart-pulse" viewBox="0 0 100 100" width="80" height="80">
        <path fill="var(--rose)" d="M50 80 C 20 50, 10 30, 30 15 C 45 5, 60 20, 60 20 C 60 20, 75 5, 90 15 C 110 30, 100 50, 50 80 Z" />
      </svg>
      <h2 style="font-family: var(--font-heading); color: var(--rose); margin-top: 20px; font-size: 2rem; font-weight: 700; letter-spacing: 1px;">She Can Foundation</h2>
      <p style="color: var(--text-muted); font-family: var(--font-body); font-size: 0.9rem; margin-top: 8px;">Empowering Women Daily</p>
    </div>
  </div>
"""

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Fix Navbar (remove the border-left inline style block and replace with cleaner flex)
    content = re.sub(r'<div class="navbar__links.*?</div>\s*<button class="hamburger"', nav_replace.strip() + '\n      <button class="hamburger"', content, flags=re.DOTALL)
    
    # Fix Preloader
    content = re.sub(r'<!-- Creative Preloader -->.*?</div>\s*</div>', preloader_replace.strip(), content, flags=re.DOTALL)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Patched {file}")

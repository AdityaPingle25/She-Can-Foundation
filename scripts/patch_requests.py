import glob
import re
import os

files = glob.glob("*.html")

logo_preloader = """
  <!-- Logo Creative Preloader -->
  <div class="preloader" id="sitePreloader">
    <div class="preloader__creative" style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; position: relative;">
      
      <div class="preloader__logo-wrap">
        <img src="img/she-YlenJon1O7ieeEoa.avif" alt="She Can Foundation Logo" class="preloader-logo-img">
      </div>
      
      <!-- Shimmering Text -->
      <h2 class="shimmer-text" style="font-family: var(--font-heading); margin-top: 35px; font-size: 2.2rem; font-weight: 800; letter-spacing: 1.5px;">She Can Foundation</h2>
      <p class="fade-up-text" style="color: var(--text-muted); font-family: var(--font-body); font-size: 0.95rem; margin-top: 5px; text-transform: uppercase; letter-spacing: 3px;">Empowering Women</p>
    </div>
  </div>
"""

chatbot_doodle_and_placeholder = """
    <form class="chatbot-input" id="chatForm">
      <input type="text" id="chatInput" placeholder="Ask about our impact, volunteering..." required autocomplete="off">
      <button type="submit" aria-label="Send Message" class="chat-send-btn">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
      </button>
    </form>
  </div>
  
  <div style="position:fixed; bottom:30px; right:30px; z-index:1000; display:flex; flex-direction:column; align-items:flex-end;">
    <!-- Cute Doodle Arrow -->
    <svg class="chat-doodle" viewBox="0 0 100 80" width="80" height="60" style="position:absolute; bottom:65px; right:25px; pointer-events:none; overflow:visible;">
      <path d="M 20 20 Q 60 -10 80 50" fill="none" stroke="var(--rose)" stroke-width="3" stroke-linecap="round" stroke-dasharray="6,6" class="doodle-line"/>
      <polygon points="80,50 72,40 88,40" fill="var(--rose)" class="doodle-head"/>
      <text x="-15" y="25" font-family="var(--font-heading)" font-weight="bold" font-size="16" fill="var(--rose)" transform="rotate(-15)">Ask AI!</text>
    </svg>
    
    <button class="chatbot-toggle" id="chatbotToggle" aria-label="Open Chat">
      <svg viewBox="0 0 24 24" width="28" height="28" fill="white" style="margin-top:2px;"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z"/></svg>
      <span class="chatbot-badge"></span>
    </button>
  </div>
"""

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace Preloader
    content = re.sub(r'<!-- Advanced Creative Preloader v2 -->.*?</div>\s*</div>', logo_preloader.strip(), content, flags=re.DOTALL)
    
    # Replace Chatbot placeholder and toggle to include doodle
    content = re.sub(r'<form class="chatbot-input".*?</button>', chatbot_doodle_and_placeholder.strip(), content, flags=re.DOTALL)

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Patched {file}")

# Advanced Gallery HTML Replacement
gallery_html = """
    <div class="gallery-grid" id="galleryGrid">
      <!-- Lightbox Container -->
      <div id="lightbox" class="lightbox">
        <span class="lightbox-close">&times;</span>
        <img class="lightbox-img" id="lightboxImg">
        <div class="lightbox-caption" id="lightboxCaption"></div>
      </div>
"""

images = [
    ("img/1682903598969-A3QBebgnl5iDPebP.avif", "Community Outreach & Education", "wide"),
    ("img/1682903599444-m5KPBaLG4LiW4P7B.avif", "Empowering the Next Generation", "tall"),
    ("img/1682903599995-mp8MQljne9CxjEvZ.avif", "Skill Development Workshops", "normal"),
    ("img/184070293_828968751391244_7235892078703811277_n_1622920242-dJolyz1XOzhegjPK.avif", "Grassroots Distribution Drive", "normal"),
    ("img/1__4__1620906612-AR0eoXKMlXF3kDQ5.avif", "Sanitary Kits Distribution", "wide"),
    ("img/untitled-design-6-YKbP4nXvKOuzqRbO.avif", "Advocacy and Awareness", "tall"),
    ("img/she-YlenJon1O7ieeEoa.avif", "She Can Foundation Identity", "normal")
]

for img, title, size_class in images:
    gallery_html += f"""
      <div class="gallery-item {size_class}">
        <img src="{img}" alt="{title}">
        <div class="gallery-overlay">
          <h3>{title}</h3>
          <span class="view-btn">View Photo</span>
        </div>
      </div>
"""
gallery_html += "    </div>"

with open("gallery.html", "r", encoding="utf-8") as f:
    g_content = f.read()

# Replace masonry with new grid
g_content = re.sub(r'<div class="gallery-masonry">.*?</div>\s*</div>\s*</section>', gallery_html + '\n  </div>\n</section>', g_content, flags=re.DOTALL)
with open("gallery.html", "w", encoding="utf-8") as f:
    f.write(g_content)


css_append = """
/* ---------- Logo Preloader CSS ---------- */
.preloader__logo-wrap {
  width: 130px; height: 130px; border-radius: 50%; padding: 8px; background: white;
  box-shadow: 0 10px 40px rgba(194, 24, 91, 0.3);
  animation: logoFloat 3s ease-in-out infinite;
  position: relative;
  z-index: 2;
}
.preloader__logo-wrap::before {
  content: ''; position: absolute; top: -12px; left: -12px; right: -12px; bottom: -12px;
  border-radius: 50%; border: 3px dashed var(--rose-light);
  animation: spin 10s linear infinite;
  z-index: -1;
}
.preloader-logo-img {
  width: 100%; height: 100%; object-fit: contain; border-radius: 50%;
  animation: logoPulse 2s infinite alternate;
}
@keyframes logoFloat { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-15px); } }
@keyframes logoPulse { 0% { transform: scale(0.95); } 100% { transform: scale(1.05); } }

/* ---------- Chat Doodle ---------- */
.chat-doodle {
  animation: doodleWiggle 3s infinite ease-in-out;
}
.doodle-line { stroke-dashoffset: 100; animation: drawDoodle 2s forwards ease-out; }
@keyframes drawDoodle { to { stroke-dashoffset: 0; } }
@keyframes doodleWiggle {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-8px) rotate(-5deg); filter: drop-shadow(0 4px 6px rgba(194,24,91,0.2)); }
}

/* ---------- Advanced Gallery Grid ---------- */
.gallery-grid {
  max-width: 1300px; margin: 0 auto; padding: 40px 20px 100px;
  display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  grid-auto-rows: 250px; grid-gap: 20px; grid-auto-flow: dense;
}
.gallery-item {
  position: relative; border-radius: 20px; overflow: hidden;
  box-shadow: 0 10px 30px rgba(0,0,0,0.08); cursor: pointer;
  transition: transform 0.4s ease, box-shadow 0.4s ease;
}
.gallery-item.wide { grid-column: span 2; }
.gallery-item.tall { grid-row: span 2; }
.gallery-item img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s ease; }
.gallery-overlay {
  position: absolute; inset: 0; background: linear-gradient(to top, rgba(194,24,91,0.9) 0%, rgba(0,0,0,0.2) 100%);
  display: flex; flex-direction: column; justify-content: flex-end; padding: 30px;
  opacity: 0; transition: opacity 0.4s ease; color: white;
}
.gallery-item:hover { transform: translateY(-5px); box-shadow: 0 20px 40px rgba(194,24,91,0.2); z-index: 2; }
.gallery-item:hover img { transform: scale(1.1); filter: blur(2px); }
.gallery-item:hover .gallery-overlay { opacity: 1; }
.gallery-overlay h3 { font-family: var(--font-heading); font-size: 1.5rem; transform: translateY(20px); transition: transform 0.4s ease; }
.view-btn { margin-top: 10px; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 2px; transform: translateY(20px); transition: transform 0.4s ease 0.1s; opacity: 0.8; }
.gallery-item:hover h3, .gallery-item:hover .view-btn { transform: translateY(0); }

@media(max-width: 768px) {
  .gallery-item.wide, .gallery-item.tall { grid-column: span 1; grid-row: span 1; }
}

/* Lightbox */
.lightbox {
  position: fixed; inset: 0; background: rgba(0,0,0,0.9); z-index: 10000;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  opacity: 0; pointer-events: none; transition: opacity 0.3s ease;
}
.lightbox.active { opacity: 1; pointer-events: auto; }
.lightbox-img { max-width: 90%; max-height: 80%; border-radius: 12px; box-shadow: 0 0 50px rgba(0,0,0,0.5); transform: scale(0.9); transition: transform 0.3s ease; }
.lightbox.active .lightbox-img { transform: scale(1); }
.lightbox-close { position: absolute; top: 30px; right: 40px; color: white; font-size: 3rem; cursor: pointer; transition: 0.2s; }
.lightbox-close:hover { color: var(--rose-light); transform: rotate(90deg); }
.lightbox-caption { color: white; font-family: var(--font-heading); font-size: 1.5rem; margin-top: 20px; }
"""

with open("style.css", "a", encoding="utf-8") as f:
    f.write("\n" + css_append)

print("UI enhancements written.")

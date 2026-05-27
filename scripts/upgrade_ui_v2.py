import glob
import re

files = glob.glob("*.html")

advanced_preloader = """
  <!-- Advanced Creative Preloader v2 -->
  <div class="preloader" id="sitePreloader">
    <div class="preloader__creative" style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; position: relative;">
      
      <!-- Blooming Lotus SVG -->
      <svg viewBox="0 0 100 100" width="120" height="120" class="blooming-lotus">
        <defs>
          <linearGradient id="lotusGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="var(--rose)" />
            <stop offset="100%" stop-color="#FF6B6B" />
          </linearGradient>
          <linearGradient id="lotusGradDark" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="var(--rose-deep)" />
            <stop offset="100%" stop-color="var(--rose)" />
          </linearGradient>
        </defs>
        
        <path class="petal petal-1" fill="url(#lotusGradDark)" d="M50 50 C 20 10, 80 10, 50 50 Z" />
        <path class="petal petal-2" fill="url(#lotusGradDark)" d="M50 50 C 90 20, 90 80, 50 50 Z" />
        <path class="petal petal-3" fill="url(#lotusGradDark)" d="M50 50 C 80 90, 20 90, 50 50 Z" />
        <path class="petal petal-4" fill="url(#lotusGradDark)" d="M50 50 C 10 80, 10 20, 50 50 Z" />
        
        <path class="petal petal-5" fill="url(#lotusGrad)" d="M50 50 C 35 15, 65 15, 50 50 Z" />
        <path class="petal petal-6" fill="url(#lotusGrad)" d="M50 50 C 85 35, 85 65, 50 50 Z" />
        <path class="petal petal-7" fill="url(#lotusGrad)" d="M50 50 C 65 85, 35 85, 50 50 Z" />
        <path class="petal petal-8" fill="url(#lotusGrad)" d="M50 50 C 15 65, 15 35, 50 50 Z" />
        
        <circle cx="50" cy="50" r="6" fill="#fff" class="lotus-center" />
      </svg>
      
      <!-- Shimmering Text -->
      <h2 class="shimmer-text" style="font-family: var(--font-heading); margin-top: 30px; font-size: 2.2rem; font-weight: 800; letter-spacing: 1.5px;">She Can Foundation</h2>
      <p class="fade-up-text" style="color: var(--text-muted); font-family: var(--font-body); font-size: 0.95rem; margin-top: 5px; text-transform: uppercase; letter-spacing: 3px;">Empowering Women</p>
    </div>
  </div>
"""

advanced_chatbot = """
  <!-- Premium AI Chatbot Widget -->
  <div class="chatbot-widget" id="chatbotWidget">
    <div class="chatbot-header">
      <div style="display:flex; align-items:center; gap:12px;">
        <div class="bot-avatar">✨</div>
        <div>
          <h4>She Can AI</h4>
          <span style="font-size: 0.75rem; opacity: 0.9; font-weight: 500;">🟢 Always Online</span>
        </div>
      </div>
      <button id="closeChat" aria-label="Close Chat" style="background:rgba(255,255,255,0.2); border-radius:50%; width:30px; height:30px; display:flex; align-items:center; justify-content:center; transition:0.3s; padding-bottom:2px;">&times;</button>
    </div>
    
    <div class="chatbot-messages" id="chatMessages">
      <div class="chat-msg bot-msg">
        <span class="msg-avatar">✨</span>
        <div class="msg-bubble">Hello! I'm the She Can AI Assistant. How can I help you today?</div>
      </div>
      <div class="chat-quick-replies">
        <button type="button" class="quick-reply-btn" onclick="document.getElementById('chatInput').value='How can I donate?'; document.getElementById('chatForm').dispatchEvent(new Event('submit', {cancelable: true, bubbles: true}))">How can I donate?</button>
        <button type="button" class="quick-reply-btn" onclick="document.getElementById('chatInput').value='Where are you located?'; document.getElementById('chatForm').dispatchEvent(new Event('submit', {cancelable: true, bubbles: true}))">Where are you located?</button>
        <button type="button" class="quick-reply-btn" onclick="document.getElementById('chatInput').value='How to volunteer?'; document.getElementById('chatForm').dispatchEvent(new Event('submit', {cancelable: true, bubbles: true}))">How to volunteer?</button>
      </div>
    </div>
    
    <form class="chatbot-input" id="chatForm">
      <input type="text" id="chatInput" placeholder="Type your message here..." required autocomplete="off">
      <button type="submit" aria-label="Send Message" class="chat-send-btn">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
      </button>
    </form>
  </div>
  <button class="chatbot-toggle" id="chatbotToggle" aria-label="Open Chat">
    <svg viewBox="0 0 24 24" width="28" height="28" fill="white" style="margin-top:2px;"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z"/></svg>
    <span class="chatbot-badge"></span>
  </button>
"""

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace Preloader
    content = re.sub(r'<!-- Advanced Creative Preloader -->.*?</div>\s*</div>', advanced_preloader.strip(), content, flags=re.DOTALL)
    content = re.sub(r'<!-- Creative Preloader -->.*?</div>\s*</div>', advanced_preloader.strip(), content, flags=re.DOTALL)
    
    # Replace Chatbot
    content = re.sub(r'<!-- AI Chatbot Widget -->.*?<span class="chatbot-badge"></span>\s*</button>', advanced_chatbot.strip(), content, flags=re.DOTALL)
    content = re.sub(r'<!-- AI Chatbot Widget -->.*?<button class="chatbot-toggle".*?</button>', advanced_chatbot.strip(), content, flags=re.DOTALL)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Patched {file}")

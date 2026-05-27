import glob
import re

chatbot_html = """
  <!-- AI Chatbot Widget -->
  <div class="chatbot-widget" id="chatbotWidget">
    <div class="chatbot-header">
      <h4>Ask She Can AI ✨</h4>
      <button id="closeChat" aria-label="Close Chat">&times;</button>
    </div>
    <div class="chatbot-messages" id="chatMessages">
      <div class="chat-msg bot-msg">Hello! I'm the She Can AI Assistant. How can I help you today?</div>
    </div>
    <form class="chatbot-input" id="chatForm">
      <input type="text" id="chatInput" placeholder="Type your message..." required autocomplete="off">
      <button type="submit" aria-label="Send Message">➤</button>
    </form>
  </div>
  <button class="chatbot-toggle" id="chatbotToggle" aria-label="Open Chat">💬</button>
"""

new_toggle = '<button id="themeToggle" class="theme-toggle" aria-label="Toggle Dark Mode" title="Toggle Dark Mode">🌙</button>'
donate_btn = '<a href="donate.html" class="navbar__donate-btn">'

files = glob.glob("*.html")
for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Clean up old ugly toggle button (it might be the first item in navbar__links)
    ugly_toggle_pattern = r'<button id="themeToggle".*?>🌙</button>'
    content = re.sub(ugly_toggle_pattern, '', content, flags=re.DOTALL)
    
    # Wait, what if there's an old one that has ☀️ instead of 🌙? Or maybe it's just exactly the one I inserted.
    content = re.sub(r'<button id="themeToggle" class="theme-toggle" aria-label="Toggle Dark Mode" style=".*?">.*?</button>', '', content, flags=re.DOTALL)

    # Insert new clean toggle right before the donate button
    if 'id="themeToggle"' not in content:
        content = content.replace(donate_btn, f'{new_toggle}\n        {donate_btn}')
    
    # Add chatbot if missing
    if 'id="chatbotWidget"' not in content:
        content = content.replace('</body>', f'{chatbot_html}\n</body>')

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Processed {file}")

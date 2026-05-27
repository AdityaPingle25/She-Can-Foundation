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

files = glob.glob("*.html")
for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Completely remove any existing chatbot HTML to be safe
    content = re.sub(r'<!-- AI Chatbot Widget -->.*?aria-label="Open Chat">.*?</button>', '', content, flags=re.DOTALL)
    
    # Clean up trailing whitespace after </html>
    content = content.strip()

    # Now inject exactly before </body>
    if '</body>' in content:
        content = content.replace('</body>', f'{chatbot_html}\n</body>')

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed chatbot in {file}")

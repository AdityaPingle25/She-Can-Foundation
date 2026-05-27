import glob
import re

files = glob.glob("*.html")

quick_replies_html = """
    <div class="chatbot-messages" id="chatMessages">
      <div class="chat-msg bot-msg">Hello! I'm the She Can AI Assistant. How can I help you today?</div>
      <div class="chat-quick-replies" style="display:flex; gap:8px; margin-top:10px; flex-wrap:wrap;">
        <button type="button" style="background:var(--rose-pale); color:var(--rose-deep); border:1px solid var(--rose); border-radius:15px; padding:5px 10px; font-size:0.8rem; cursor:pointer;" onclick="document.getElementById('chatInput').value='How can I donate?'; document.getElementById('chatForm').dispatchEvent(new Event('submit', {cancelable: true, bubbles: true}))">How can I donate?</button>
        <button type="button" style="background:var(--rose-pale); color:var(--rose-deep); border:1px solid var(--rose); border-radius:15px; padding:5px 10px; font-size:0.8rem; cursor:pointer;" onclick="document.getElementById('chatInput').value='Where are you located?'; document.getElementById('chatForm').dispatchEvent(new Event('submit', {cancelable: true, bubbles: true}))">Where are you located?</button>
        <button type="button" style="background:var(--rose-pale); color:var(--rose-deep); border:1px solid var(--rose); border-radius:15px; padding:5px 10px; font-size:0.8rem; cursor:pointer;" onclick="document.getElementById('chatInput').value='How to volunteer?'; document.getElementById('chatForm').dispatchEvent(new Event('submit', {cancelable: true, bubbles: true}))">How to volunteer?</button>
      </div>
    </div>
"""

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace old chat messages container with new one containing quick replies
    content = re.sub(r'<div class="chatbot-messages" id="chatMessages">.*?</div>\s*</div>\s*<form class="chatbot-input"', quick_replies_html.strip() + '\n    <form class="chatbot-input"', content, flags=re.DOTALL)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Patched Chatbot UI in {file}")

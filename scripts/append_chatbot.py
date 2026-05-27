with open("index.html", "a", encoding="utf-8") as f:
    f.write("""
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
""")

with open("style.css", "a", encoding="utf-8") as f:
    f.write("""
/* ---------- AI Chatbot Widget ---------- */
.chatbot-toggle {
  position: fixed; bottom: 30px; right: 30px; width: 60px; height: 60px; border-radius: 50%;
  background: var(--rose); color: white; font-size: 1.5rem; border: none;
  box-shadow: 0 10px 20px rgba(194,24,91,0.3); cursor: pointer; z-index: 1000;
  transition: transform 0.3s ease;
}
.chatbot-toggle:hover { transform: scale(1.1); }
.chatbot-widget {
  position: fixed; bottom: 100px; right: 30px; width: 350px; height: 450px;
  background: var(--white); border-radius: 16px; box-shadow: 0 15px 40px rgba(0,0,0,0.15);
  display: flex; flex-direction: column; z-index: 1000; overflow: hidden;
  transform: translateY(20px); opacity: 0; pointer-events: none; transition: all 0.3s ease;
}
.chatbot-widget.open { transform: translateY(0); opacity: 1; pointer-events: auto; }
.chatbot-header {
  background: var(--rose); color: white; padding: 15px 20px; display: flex;
  justify-content: space-between; align-items: center; font-family: var(--font-heading);
}
.chatbot-header h4 { margin: 0; font-size: 1.1rem; }
.chatbot-header button { background: none; border: none; color: white; font-size: 1.5rem; cursor: pointer; }
.chatbot-messages { flex: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 10px; background: #fafafa; }
[data-theme="dark"] .chatbot-messages { background: #1a1a1a; }
.chat-msg { padding: 10px 15px; border-radius: 15px; max-width: 85%; font-size: 0.95rem; line-height: 1.4; }
.bot-msg { background: var(--rose-pale); color: var(--rose-deep); align-self: flex-start; border-bottom-left-radius: 5px; }
.user-msg { background: var(--rose); color: white; align-self: flex-end; border-bottom-right-radius: 5px; }
.chatbot-input { display: flex; border-top: 1px solid rgba(0,0,0,0.05); }
.chatbot-input input { flex: 1; border: none; padding: 15px; outline: none; background: transparent; color: var(--text); }
.chatbot-input button { background: transparent; border: none; color: var(--rose); padding: 0 20px; cursor: pointer; font-size: 1.2rem; }
""")

with open("main.js", "a", encoding="utf-8") as f:
    f.write("""
// AI Chatbot Logic
document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('chatbotToggle');
  const widget = document.getElementById('chatbotWidget');
  const closeBtn = document.getElementById('closeChat');
  const chatForm = document.getElementById('chatForm');
  const chatInput = document.getElementById('chatInput');
  const chatMessages = document.getElementById('chatMessages');

  if(toggleBtn && widget) {
    toggleBtn.addEventListener('click', () => widget.classList.add('open'));
    closeBtn.addEventListener('click', () => widget.classList.remove('open'));

    chatForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const text = chatInput.value.trim();
      if(!text) return;

      // Add user message
      chatMessages.innerHTML += `<div class="chat-msg user-msg">${text}</div>`;
      chatInput.value = '';
      chatMessages.scrollTop = chatMessages.scrollHeight;

      // Add typing indicator
      const typingId = 'typing-' + Date.now();
      chatMessages.innerHTML += `<div id="${typingId}" class="chat-msg bot-msg">...</div>`;
      chatMessages.scrollTop = chatMessages.scrollHeight;

      try {
        const response = await fetch('/api/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message: text })
        });
        const data = await response.json();
        document.getElementById(typingId).remove();
        chatMessages.innerHTML += `<div class="chat-msg bot-msg">${data.reply}</div>`;
      } catch(err) {
        document.getElementById(typingId).remove();
        chatMessages.innerHTML += `<div class="chat-msg bot-msg">Oops! I am offline right now. (Server not running)</div>`;
      }
      chatMessages.scrollTop = chatMessages.scrollHeight;
    });
  }
});
""")

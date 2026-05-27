import re

with open("main.js", "r", encoding="utf-8") as f:
    content = f.read()

# The file currently has a broken block starting from line 416 to the end.
# Let's cleanly replace all AI Chatbot logic.
clean_content = re.sub(r'// AI Chatbot Logic\s*document\.addEventListener.*', '', content, flags=re.DOTALL)

# And if there's any broken trailing text from the botched replace:
clean_content = re.sub(r'\s*// Add user message.*?chatMessages\.scrollHeight;\s*$', '', clean_content, flags=re.DOTALL)

# Now append the correct full logic
correct_logic = """
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
        if (!response.ok) throw new Error("API Offline");
        const data = await response.json();
        document.getElementById(typingId).remove();
        chatMessages.innerHTML += `<div class="chat-msg bot-msg">${data.reply}</div>`;
      } catch(err) {
        document.getElementById(typingId).remove();
        let fallback = "Thank you for reaching out to She Can Foundation! How else can I assist you today?";
        const lower = text.toLowerCase();
        if (lower.includes('donate') || lower.includes('money')) {
          fallback = "Every contribution counts! 100% of your donation goes directly towards our ground operations. You can donate securely via our Donate page.";
        } else if (lower.includes('volunteer') || lower.includes('join')) {
          fallback = "We're thrilled you want to join us! Please click the 'Volunteer With Us' button on our homepage.";
        }
        chatMessages.innerHTML += `<div class="chat-msg bot-msg">${fallback}</div>`;
      }
      chatMessages.scrollTop = chatMessages.scrollHeight;
    });
  }
});
"""

with open("main.js", "w", encoding="utf-8") as f:
    f.write(clean_content.strip() + '\n\n' + correct_logic.strip())

print("main.js fixed")

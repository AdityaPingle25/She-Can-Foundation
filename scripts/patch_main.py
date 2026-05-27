with open("main.js", "r", encoding="utf-8") as f:
    js_content = f.read()

# Replace user message format
js_content = js_content.replace(
    '`<div class="chat-msg user-msg">${text}</div>`',
    '`<div class="chat-msg user-msg"><div class="msg-bubble">${text}</div></div>`'
)

# Replace typing indicator format
js_content = js_content.replace(
    '`<div id="${typingId}" class="chat-msg bot-msg">...</div>`',
    '`<div id="${typingId}" class="chat-msg bot-msg"><span class="msg-avatar">✨</span><div class="msg-bubble">...</div></div>`'
)

# Replace bot message format
js_content = js_content.replace(
    '`<div class="chat-msg bot-msg">${data.reply}</div>`',
    '`<div class="chat-msg bot-msg"><span class="msg-avatar">✨</span><div class="msg-bubble">${data.reply}</div></div>`'
)

# Replace fallback format
js_content = js_content.replace(
    '`<div class="chat-msg bot-msg">${fallback}</div>`',
    '`<div class="chat-msg bot-msg"><span class="msg-avatar">✨</span><div class="msg-bubble">${fallback}</div></div>`'
)

with open("main.js", "w", encoding="utf-8") as f:
    f.write(js_content)
print("main.js patched for premium chatbot UI.")

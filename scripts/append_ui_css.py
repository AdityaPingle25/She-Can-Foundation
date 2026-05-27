css_append = """
/* ---------- Blooming Lotus Preloader ---------- */
.blooming-lotus { animation: lotusRotate 15s linear infinite; }
@keyframes lotusRotate { to { transform: rotate(360deg); } }
.petal { transform-origin: 50px 50px; animation: bloom 3s ease-in-out infinite alternate; opacity: 0.9; }
.petal-1 { animation-delay: 0s; }
.petal-2 { animation-delay: 0.3s; }
.petal-3 { animation-delay: 0.6s; }
.petal-4 { animation-delay: 0.9s; }
.petal-5 { animation-delay: 1.2s; }
.petal-6 { animation-delay: 1.5s; }
.petal-7 { animation-delay: 1.8s; }
.petal-8 { animation-delay: 2.1s; }
@keyframes bloom {
  0% { transform: scale(0.4); opacity: 0.5; }
  100% { transform: scale(1.1); opacity: 1; filter: drop-shadow(0 0 10px rgba(194, 24, 91, 0.5)); }
}
.lotus-center { animation: pulseCenter 1.5s infinite alternate; }
@keyframes pulseCenter { to { r: 9; opacity: 0.8; filter: drop-shadow(0 0 5px #fff); } }

/* ---------- Premium AI Chatbot UI ---------- */
.chatbot-widget {
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0,0,0,0.2) !important;
  border: 1px solid rgba(0,0,0,0.05);
}
.chatbot-header {
  background: linear-gradient(135deg, var(--rose) 0%, var(--rose-deep) 100%) !important;
  padding: 16px 20px !important;
  box-shadow: 0 4px 15px rgba(194,24,91,0.2);
}
.bot-avatar {
  background: rgba(255,255,255,0.2);
  width: 38px; height: 38px;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.2rem;
  border: 1px solid rgba(255,255,255,0.4);
}
.msg-avatar {
  background: var(--rose-pale);
  width: 28px; height: 28px;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 0.9rem;
  flex-shrink: 0;
  margin-right: 8px;
}
.chat-msg {
  display: flex;
  align-items: flex-end;
  max-width: 90% !important;
  padding: 0 !important;
  background: transparent !important;
}
.msg-bubble {
  padding: 12px 16px;
  border-radius: 18px;
  font-size: 0.95rem;
  line-height: 1.4;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.bot-msg .msg-bubble {
  background: #ffffff;
  color: var(--charcoal);
  border-bottom-left-radius: 4px;
}
.user-msg {
  justify-content: flex-end;
  align-self: flex-end;
}
.user-msg .msg-bubble {
  background: linear-gradient(135deg, var(--rose) 0%, var(--rose-deep) 100%);
  color: white;
  border-bottom-right-radius: 4px;
}
.chat-quick-replies {
  display: flex; flex-wrap: wrap; gap: 8px; margin-top: 15px; margin-left: 36px;
}
.quick-reply-btn {
  background: var(--white);
  color: var(--rose-deep);
  border: 1px solid rgba(194,24,91,0.2);
  border-radius: 20px;
  padding: 8px 14px;
  font-size: 0.8rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 5px rgba(0,0,0,0.02);
}
.quick-reply-btn:hover {
  background: var(--rose-pale);
  border-color: var(--rose);
  transform: translateY(-2px);
}
.chatbot-input {
  padding: 10px !important;
  background: var(--white);
  border-top: 1px solid rgba(0,0,0,0.05) !important;
}
.chatbot-input input {
  background: #f5f5f5 !important;
  border-radius: 20px !important;
  padding: 12px 20px !important;
  margin-right: 10px;
}
.chat-send-btn {
  background: var(--rose-pale) !important;
  width: 44px; height: 44px;
  border-radius: 50%;
  display: flex !important;
  align-items: center; justify-content: center;
  padding: 0 !important;
  transition: 0.3s;
}
.chat-send-btn:hover {
  background: var(--rose) !important;
  color: white !important;
  transform: scale(1.05);
}
.chatbot-toggle {
  display: flex; align-items: center; justify-content: center;
}
.chatbot-badge {
  position: absolute; top: 0; right: 0; width: 14px; height: 14px;
  background: #00E676; border: 2px solid var(--rose); border-radius: 50%;
  animation: badgePulse 2s infinite;
}
@keyframes badgePulse {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 230, 118, 0.7); }
  70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(0, 230, 118, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 230, 118, 0); }
}

[data-theme="dark"] .bot-msg .msg-bubble { background: #2A2A2A; color: #E0E0E0; border: 1px solid rgba(255,255,255,0.05); }
[data-theme="dark"] .quick-reply-btn { background: #2A2A2A; color: var(--rose-light); border-color: rgba(255,255,255,0.1); }
[data-theme="dark"] .chatbot-input input { background: #2A2A2A !important; color: #E0E0E0 !important; }
"""

with open("style.css", "a", encoding="utf-8") as f:
    f.write("\n" + css_append)
print("CSS injected.")

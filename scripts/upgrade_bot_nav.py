import re

# 1. Update style.css for Floating Pill Navbar
with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

pill_navbar_css = """
/* ---------- Floating Pill Navbar Upgrade ---------- */
.navbar {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  width: 92%;
  max-width: 1200px;
  border-radius: 50px;
  padding: 12px 24px;
  background: rgba(255, 248, 240, 0.85);
  box-shadow: 0 8px 32px rgba(194, 24, 91, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.4);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.navbar.scrolled {
  top: 10px;
  padding: 10px 24px;
  background: rgba(255, 248, 240, 0.95);
  box-shadow: 0 10px 40px rgba(194, 24, 91, 0.12);
}
[data-theme="dark"] .navbar {
  background: rgba(18, 18, 18, 0.85) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  box-shadow: 0 10px 40px rgba(0,0,0,0.4) !important;
}
[data-theme="dark"] .navbar.scrolled {
  background: rgba(18, 18, 18, 0.98) !important;
}
.navbar__inner { padding: 0; }
"""

if "Floating Pill Navbar Upgrade" not in css:
    with open("style.css", "a", encoding="utf-8") as f:
        f.write("\n" + pill_navbar_css)

# 2. Update server.js to train AI Bot with more features
with open("server.js", "r", encoding="utf-8") as f:
    server_js = f.read()

new_bot_logic = """
// Mock Chatbot API Endpoint
app.post('/api/chat', (req, res) => {
  const { message } = req.body;
  const lower = message.toLowerCase();
  
  let reply = "I'm still learning! But I can help you with donations, volunteering, our mission, or contact info. What would you like to know?";
  
  // Advanced Training Rules
  if (lower.includes('donate') || lower.includes('money') || lower.includes('fund')) {
    reply = "Every contribution empowers a girl. ₹500 provides pads for 5 girls for a month, while ₹5000 keeps 25 girls in school with dignity. You can donate via UPI, Card, or Bank Transfer securely on our <a href='donate.html' style='color:var(--rose); text-decoration:underline;'>Donate page</a>.";
  } else if (lower.includes('volunteer') || lower.includes('join') || lower.includes('intern')) {
    reply = "We're thrilled you want to join the She Can family! We offer both field volunteering and remote internships. Click the 'Volunteer' button on our homepage to fill out our application form.";
  } else if (lower.includes('location') || lower.includes('located') || lower.includes('where') || lower.includes('address')) {
    reply = "Our main registered office is in New Delhi, but our on-ground operations run across 250+ rural villages throughout India.";
  } else if (lower.includes('certificate') || lower.includes('registered') || lower.includes('legal') || lower.includes('fake')) {
    reply = "We operate with 100% transparency. She Can Foundation is fully registered under the Indian Society Act, 1860. You can view our official legal registration on the 'Our Certificate' page.";
  } else if (lower.includes('hello') || lower.includes('hi') || lower.includes('hey')) {
    reply = "Hello there! ✨ I'm the She Can AI Assistant. How can I help you make an impact today?";
  } else if (lower.includes('founder') || lower.includes('who created') || lower.includes('reeta')) {
    reply = "She Can Foundation was founded by Reeta Mishra, our visionary President who dedicated her life to ensuring no girl misses school due to period poverty.";
  } else if (lower.includes('contact') || lower.includes('email') || lower.includes('phone') || lower.includes('reach')) {
    reply = "You can reach our team directly via email at <b>president@shecanfoundation.org</b> or call us at <b>+91 8283841830</b>.";
  } else if (lower.includes('why') || lower.includes('mission') || lower.includes('vision') || lower.includes('what do you do')) {
    reply = "Our mission is simple: End period poverty. 1 in 5 girls in India drop out of school because of periods. We provide free sanitary pads, dignity kits, and awareness workshops to keep them educated and empowered.";
  } else if (lower.includes('impact') || lower.includes('how many')) {
    reply = "Thanks to our amazing donors, we have already helped over 1,20,000+ girls across India receive free sanitary pads and menstrual hygiene education!";
  } else if (lower.includes('thank')) {
    reply = "You're very welcome! Let me know if you need anything else. ♥";
  }

  // Simulate network delay for realism
  setTimeout(() => {
    res.json({ reply });
  }, 800);
});
"""

# Replace the old endpoint
server_js = re.sub(r"// Mock Chatbot API Endpoint.*?\}\);\s*\}\);", new_bot_logic.strip(), server_js, flags=re.DOTALL)

with open("server.js", "w", encoding="utf-8") as f:
    f.write(server_js)

print("Navbar and Bot updated successfully.")

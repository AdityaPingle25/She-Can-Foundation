with open("style.css", "a") as f:
    f.write("""
/* ---------- Dark Theme Overrides ---------- */
[data-theme="dark"] {
  --cream: #121212;
  --charcoal: #E0E0E0;
  --text: #D0D0D0;
  --text-muted: #A0A0A0;
  --white: #1E1E1E;
  --rose-pale: #301018;
  --rose-glow: rgba(194, 24, 91, 0.4);
}
[data-theme="dark"] .polaroid, [data-theme="dark"] .about__img-accent, [data-theme="dark"] .hero__badge {
  background: var(--white) !important;
  box-shadow: 0 10px 25px rgba(0,0,0,0.5) !important;
}
[data-theme="dark"] .tape {
  background: rgba(30, 30, 30, 0.7) !important;
  border-color: rgba(255,255,255,0.1) !important;
}
[data-theme="dark"] .sim-displays { background: #1a1a1a !important; }
[data-theme="dark"] .metric-item__icon { background: #2a2a2a !important; }
[data-theme="dark"] .simulator-box { background: rgba(30, 30, 30, 0.9) !important; border-color: rgba(255,255,255,0.1) !important; }
""")

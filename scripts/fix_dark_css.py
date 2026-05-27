with open("style.css", "a") as f:
    f.write("""
/* ---------- Dark Theme Advanced Overrides ---------- */
[data-theme="dark"] .navbar {
  background: rgba(18, 18, 18, 0.94) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
}
[data-theme="dark"] .mobile-menu {
  background: rgba(18, 18, 18, 0.98) !important;
}
[data-theme="dark"] .mobile-menu a {
  color: var(--charcoal) !important;
}
[data-theme="dark"] .section, [data-theme="dark"] body {
  background: var(--cream) !important;
  color: var(--charcoal) !important;
}
[data-theme="dark"] h1, [data-theme="dark"] h2, [data-theme="dark"] h3, [data-theme="dark"] h4, [data-theme="dark"] h5, [data-theme="dark"] h6 {
  color: var(--charcoal) !important;
}
[data-theme="dark"] .theme-toggle {
  color: var(--charcoal) !important;
  text-shadow: 0 0 5px rgba(255,255,255,0.2);
}
[data-theme="dark"] .preloader { background: #121212 !important; }
""")

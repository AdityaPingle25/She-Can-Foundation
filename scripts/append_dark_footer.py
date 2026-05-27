with open("style.css", "a") as f:
    f.write("""
/* ---------- Dark Theme Overrides for Footer and Letter ---------- */
[data-theme="dark"] .footer {
  background: #0a0a0a !important;
  color: #a0a0a0 !important;
}
[data-theme="dark"] .footer-col h4, [data-theme="dark"] .footer-brand p {
  color: #e0e0e0 !important;
}
[data-theme="dark"] .footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
}
[data-theme="dark"] .journal-diary__page {
  background: #1a1a1a !important;
  color: #d0d0d0 !important;
  box-shadow: 0 10px 40px rgba(0,0,0,0.5) !important;
  border-left: 2px solid var(--rose-deep) !important;
}
[data-theme="dark"] .journal-diary__handwritten {
  color: var(--rose-light) !important;
}
""")

with open("style.css", "a", encoding="utf-8") as f:
    f.write("""
/* ---------- Updated Theme Toggle & Navbar Actions ---------- */
.theme-toggle {
  background: var(--white) !important;
  border: 1px solid rgba(194, 24, 91, 0.1) !important;
  box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
  border-radius: 20px !important;
  cursor: pointer !important;
  font-size: 1.1rem !important;
  color: var(--text) !important;
  padding: 6px 14px !important;
  transition: all 0.3s ease !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin-left: 15px !important;
  margin-right: 5px !important;
}
.theme-toggle:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 15px rgba(194, 24, 91, 0.15) !important;
}
[data-theme="dark"] .theme-toggle {
  background: #1a1a1a !important;
  border-color: rgba(255,255,255,0.1) !important;
  color: #fff !important;
}
""")

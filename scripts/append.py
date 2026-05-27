with open("style.css", "a") as f:
    f.write("""
/* ---------- Volunteer Modal ---------- */
.volunteer-modal { position: fixed; inset: 0; z-index: 10000; display: flex; align-items: center; justify-content: center; opacity: 0; visibility: hidden; transition: all var(--transition); }
.volunteer-modal.open { opacity: 1; visibility: visible; }
.volunteer-modal__overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.6); backdrop-filter: blur(4px); }
.volunteer-modal__content { position: relative; background: var(--cream); width: 90%; max-width: 500px; border-radius: 20px; padding: 40px; box-shadow: 0 20px 60px rgba(0,0,0,0.15); transform: translateY(40px); transition: transform var(--transition); z-index: 2; overflow: hidden; }
.volunteer-modal.open .volunteer-modal__content { transform: translateY(0); }
.volunteer-modal__close { position: absolute; top: 16px; right: 16px; background: none; border: none; font-size: 2rem; color: var(--text-muted); cursor: pointer; line-height: 1; transition: color var(--transition); }
.volunteer-modal__close:hover { color: var(--rose); }
.volunteer-modal__quote { font-family: var(--font-heading); font-size: 1.1rem; font-style: italic; color: var(--rose-deep); text-align: center; margin-bottom: 24px; padding-bottom: 20px; border-bottom: 1px dashed rgba(194,24,91,0.2); }
.volunteer-modal__quote span { display: block; font-family: var(--font-body); font-style: normal; font-size: 0.85rem; color: var(--text-muted); margin-top: 8px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.05em; }
""")

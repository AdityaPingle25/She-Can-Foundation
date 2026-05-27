with open("style.css", "a", encoding="utf-8") as f:
    f.write("""
/* ---------- Creative Preloader ---------- */
.preloader__creative {
  display: flex;
  align-items: center;
  justify-content: center;
  animation: pulseHeart 1.5s infinite;
}
@keyframes pulseHeart {
  0% { transform: scale(0.9); opacity: 0.8; }
  50% { transform: scale(1.1); opacity: 1; filter: drop-shadow(0 0 15px var(--rose-light)); }
  100% { transform: scale(0.9); opacity: 0.8; }
}
""")

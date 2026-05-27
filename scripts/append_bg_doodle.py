with open("style.css", "a") as f:
    f.write("""
/* ---------- Floating Doodles ---------- */
.bg-doodle {
  position: absolute;
  pointer-events: none;
  z-index: 0;
  animation: floatDoodle 8s ease-in-out infinite alternate;
}
@keyframes floatDoodle {
  from { transform: translateY(0) rotate(0deg); }
  to { transform: translateY(-40px) rotate(15deg); }
}
""")

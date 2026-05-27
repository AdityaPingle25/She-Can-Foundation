with open("style.css", "a") as f:
    f.write("""
/* ---------- Donate Oval Animation ---------- */
.donate-oval-path { stroke-dasharray: 600; stroke-dashoffset: 600; animation: drawOval 2s ease-out forwards; animation-delay: 0.5s; stroke: var(--rose) !important; stroke-width: 3px !important; }
@keyframes drawOval { to { stroke-dashoffset: 0; } }
""")

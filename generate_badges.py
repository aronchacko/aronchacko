import os

BADGES = [
    ("badge-portfolio.svg", "PORTFOLIO", "ARON.OS"),
    ("badge-linkedin.svg", "LINKEDIN", "NETWORK"),
    ("badge-github.svg", "GITHUB", "SOURCE")
]

TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="240" height="36">
  <defs>
    <style>
      .bg {{ fill: #0D1117; stroke: #00F0FF; stroke-width: 1.5; }}
      .lbl {{ font-family: 'Courier New', Courier, monospace; font-size: 14px; font-weight: bold; fill: #00F0FF; }}
      .msg {{ font-family: 'Courier New', Courier, monospace; font-size: 14px; font-weight: bold; fill: #ffffff; }}
    </style>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="1.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect x="2" y="2" width="236" height="32" rx="4" class="bg" filter="url(#glow)"/>
  <line x1="120" y1="2" x2="120" y2="34" stroke="#00F0FF" stroke-width="1.5" filter="url(#glow)"/>
  <text x="60" y="22" class="lbl" text-anchor="middle" filter="url(#glow)">{lbl}</text>
  <text x="180" y="22" class="msg" text-anchor="middle">{msg}</text>
</svg>"""

for filename, lbl, msg in BADGES:
    filepath = os.path.join(os.getcwd(), filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(lbl=lbl, msg=msg))

print("Badges generated successfully.")

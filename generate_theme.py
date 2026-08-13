import os
import re

HEADER_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 60" width="100%" height="60">
    <defs>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="3" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <style>
            .header-text {
                font-family: 'Courier New', Courier, monospace;
                font-size: 22px;
                font-weight: bold;
                fill: #ffffff;
            }
            .accent {
                fill: #00F0FF;
            }
        </style>
    </defs>

    <text x="20" y="40" class="header-text" filter="url(#glow)"><tspan class="accent">░ </tspan>{title}</text>
    <line x1="20" y1="55" x2="300" y2="55" stroke="#00F0FF" stroke-width="1.5" stroke-opacity="0.6" filter="url(#glow)"/>
</svg>"""

DIVIDER_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 40" width="100%" height="40">
    <defs>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="3" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
    </defs>
    <line x1="50" y1="20" x2="750" y2="20" stroke="#00F0FF" stroke-width="1" stroke-opacity="0.2" stroke-dasharray="8 4" filter="url(#glow)"/>
    <circle cx="400" cy="20" r="3" fill="#00F0FF" opacity="0.6" filter="url(#glow)"/>
</svg>"""

sections = {
    "TECH STACK": "header-tech-stack.svg",
    "GITHUB LIVE METRICS": "header-metrics.svg",
    "CONTRIBUTION MATRIX": "header-contribution.svg",
    "WHAT I BUILD": "header-what-i-build.svg",
    "CURRENT MISSION": "header-mission.svg",
    "PROJECT CARDS": "header-projects.svg",
    "SYSTEM ARCHITECTURE": "header-architecture.svg",
    "ENGINEERING PRINCIPLES": "header-principles.svg",
    "CONNECT TO ARON.OS": "header-connect.svg"
}

def main():
    base_dir = os.getcwd()
    
    # 1. Generate SVGs
    for title, filename in sections.items():
        filepath = os.path.join(base_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(HEADER_TEMPLATE.format(title=title))
            
    divider_path = os.path.join(base_dir, "divider.svg")
    with open(divider_path, "w", encoding="utf-8") as f:
        f.write(DIVIDER_TEMPLATE)
        
    # 2. Update README.md
    readme_path = os.path.join(base_dir, "README.md")
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    for title, filename in sections.items():
        pattern = r"### ░ " + re.escape(title)
        replacement = f'<div align="center">\n  <img src="{filename}" alt="{title}" width="100%">\n</div>'
        # To add a divider before each section except maybe the first, but let's just replace the header.
        content = re.sub(pattern, replacement, content)
        
    # Let's insert dividers before the replacements to make it look cool?
    # Actually, replacing the headers might be enough. If we want a divider, we could add it before the div.
    # We will add divider above each new header except the ones that already follow something clear.
    # To be safe, we'll just add the divider above each header image tag block.
    # But wait, regex replace already happened. 
    # Let's re-read and replace `<div align="center">\n  <img src="header-` with `<div align="center">\n  <img src="divider.svg" width="100%">\n  <br>\n  <img src="header-`
    # We'll skip adding a divider before TECH STACK as it is right under IDENTITY. Wait, maybe add divider there too.
    content = content.replace('<img src="header-', '<img src="divider.svg" alt="Divider" width="100%">\n  <br>\n  <img src="header-')
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Done generating SVGs and updating README.md")

if __name__ == "__main__":
    main()

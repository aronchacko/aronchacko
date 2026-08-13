import os
import re

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
    readme_path = os.path.join(base_dir, "README.md")
    
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    for title, filename in sections.items():
        pattern = r"### ░ " + re.escape(title)
        replacement = f'<div align="center">\n  <img src="divider.svg" alt="Divider" width="100%">\n  <br><br>\n  <img src="{filename}" alt="{title}" width="100%">\n</div>'
        content = re.sub(pattern, replacement, content)
        
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Updated README.md")

if __name__ == "__main__":
    main()

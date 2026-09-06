import os
import glob
import re

def fix_typo():
    path = r"c:\Users\anton\Desktop\MKT\Brota Marketing\public\blog\marketing-influencers-pymes.html"
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace("Error a evitar: No cumplas la ley.", "Error a evitar: Incumplir la ley.")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Typo fixed.")

def fix_navbar():
    base_dir = r"c:\Users\anton\Desktop\MKT\Brota Marketing\public"
    files = []
    
    # Recoger todos los HTMLs en public y en public/blog
    files.extend(glob.glob(os.path.join(base_dir, "*.html")))
    files.extend(glob.glob(os.path.join(base_dir, "blog", "*.html")))
    
    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Reemplazar la clase glass por clases nativas de tailwind
        # glass = bg-white/70 backdrop-blur-md border border-white/50
        # Buscamos class="... glass ..." y reemplazamos
        new_content = re.sub(
            r'<nav class="([^"]*?)\bglass\b([^"]*?)"',
            r'<nav class="\1bg-white/70 backdrop-blur-md border-b border-white/50\2"',
            content
        )
        
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Fixed navbar in {os.path.basename(f)}")

if __name__ == "__main__":
    fix_typo()
    fix_navbar()

import os

def fix_image_urls():
    img_url = "/blog/images/marketing-influencers-pymes_ai.jpg"
    old_img_url = "https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=1200&h=600&fit=crop"
    
    path_art = r"c:\Users\anton\Desktop\MKT\Brota Marketing\public\blog\marketing-influencers-pymes.html"
    path_idx = r"c:\Users\anton\Desktop\MKT\Brota Marketing\public\blog\index.html"
    
    for path in [path_art, path_idx]:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace(old_img_url, img_url)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")

if __name__ == "__main__":
    fix_image_urls()

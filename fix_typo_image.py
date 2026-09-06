import os

def fix_typo():
    path = r"c:\Users\anton\Desktop\MKT\Brota Marketing\public\blog\marketing-influencers-pymes.html"
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace("Error a evitar:</strong> No cumplas la ley.", "Error a evitar:</strong> Incumplir la ley.")
    
    # Also replace loremflickr with unsplash
    content = content.replace("https://loremflickr.com/1200/600/marketing,influencer", "https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=1200&h=600&fit=crop")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Article fixed.")

def fix_index():
    path = r"c:\Users\anton\Desktop\MKT\Brota Marketing\public\blog\index.html"
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace("https://loremflickr.com/1200/600/marketing,influencer", "https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=1200&h=600&fit=crop")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Index fixed.")

if __name__ == "__main__":
    fix_typo()
    fix_index()

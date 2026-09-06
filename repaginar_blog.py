import os
import re
import math
import json

def main():
    blog_dir = r"c:\Users\anton\Desktop\MKT\Brota Marketing\public\blog"
    # Find all index files
    files = [f for f in os.listdir(blog_dir) if f.startswith("index") and f.endswith(".html")]
    
    def get_num(f):
        if f == "index.html": return 1
        m = re.search(r'\d+', f)
        return int(m.group()) if m else 999
    
    files.sort(key=get_num)
    
    all_articles = []
    content_template = None
    
    for idx_file in files:
        path = os.path.join(blog_dir, idx_file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        grid_match = re.search(r'(<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">)(.*?)(</div>\s*<div class="flex justify-center items-center space-x-2 mt-12">|</div>\s*</main>|</div>\s*<!--\s*Paginación)', content, re.DOTALL)
        if grid_match:
            articles_html = grid_match.group(2)
            arts = re.findall(r'<article.*?</article>', articles_html, re.DOTALL)
            all_articles.extend(arts)
            
            if content_template is None:
                before = content[:grid_match.start(2)]
                after_match = re.search(r'</div>\s*(<div class="flex justify-center items-center space-x-2 mt-12">.*?</main>|</main>)', content[grid_match.end(2):], re.DOTALL)
                if after_match:
                    after = "\n</div>\n" + "{PAGINATION}" + "\n</main>" + content[grid_match.end(2) + after_match.end():]
                else:
                    after = "\n</div>\n" + "{PAGINATION}" + "\n</main>"
                content_template = (before, after)

    # 1. Generar search_index.json a partir de all_articles
    search_data = []
    for art in all_articles:
        # Extraer URL
        url_match = re.search(r'<a href="([^"]+)"', art)
        url = url_match.group(1) if url_match else ""
        
        # Extraer título
        title_match = re.search(r'<h2[^>]*>(.*?)</h2>', art, re.DOTALL)
        title = title_match.group(1).strip() if title_match else ""
        title = re.sub(r'<[^>]+>', '', title)
        
        # Extraer descripción (line-clamp-3)
        desc_match = re.search(r'<p[^>]*line-clamp-3[^>]*>(.*?)</p>', art, re.DOTALL)
        desc = desc_match.group(1).strip() if desc_match else ""
        desc = re.sub(r'<[^>]+>', '', desc)
        
        # Extraer categoría
        cat_match = re.search(r'<span[^>]*uppercase[^>]*>(.*?)</span>', art)
        category = cat_match.group(1).strip() if cat_match else ""
        category = re.sub(r'<[^>]+>', '', category)
        
        search_data.append({
            "title": title,
            "url": url,
            "description": desc,
            "category": category
        })
        
    with open(os.path.join(blog_dir, 'search_index.json'), 'w', encoding='utf-8') as f:
        json.dump(search_data, f, ensure_ascii=False, indent=2)
    print("Generado search_index.json")

    # Re-calculate files needed
    items_per_page = 9
    total_pages = math.ceil(len(all_articles) / items_per_page)

    for page in range(1, total_pages + 1):
        start_idx = (page - 1) * items_per_page
        end_idx = start_idx + items_per_page
        page_articles = all_articles[start_idx:end_idx]

        pagination_html = '<div class="flex justify-center items-center space-x-2 mt-12">\n'
        for p in range(1, total_pages + 1):
            page_url = "index.html" if p == 1 else f"index-{p}.html"
            active_class = "bg-brota-green text-white" if p == page else "bg-white text-brota-dark hover:bg-brota-light"
            pagination_html += f'<a href="{page_url}" class="px-4 py-2 rounded-lg font-bold shadow-sm {active_class} transition-colors">{p}</a>\n'
        pagination_html += '</div>'

        before, after = content_template
        page_content = before + "\n".join(page_articles) + after.replace("{PAGINATION}", pagination_html)
        
        file_name = "index.html" if page == 1 else f"index-{page}.html"
        with open(os.path.join(blog_dir, file_name), 'w', encoding='utf-8') as f:
            f.write(page_content)
        print(f"Generado {file_name} con {len(page_articles)} artículos.")

    # Clean up any leftover index files (e.g. if we deleted articles)
    for idx_file in files:
        num = get_num(idx_file)
        if num > total_pages:
            os.remove(os.path.join(blog_dir, idx_file))
            print(f"Eliminado archivo obsoleto {idx_file}")

if __name__ == "__main__":
    main()

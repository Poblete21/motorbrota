import os
import re
import math
from datetime import datetime, timedelta

def get_dates():
    dates = []
    current_date = datetime(2026, 7, 28)
    for i in range(100):
        dates.append(current_date.strftime("%d %b, %Y").replace("Jan", "Ene").replace("Apr", "Abr").replace("Aug", "Ago").replace("Dec", "Dic"))
        if current_date.weekday() == 1:
            current_date -= timedelta(days=5)
        else:
            current_date -= timedelta(days=2)
    return dates

def main():
    blog_dir = r"c:\Users\anton\Desktop\MKT\Brota Marketing\public\blog"
    
    # We use a backed up version or we just parse all files in blog_dir and re-generate indexes.
    # Actually, all <article> in index.html, index-2.html, etc. should be collected!
    # Let's collect from all index*.html files
    index_files = [f for f in os.listdir(blog_dir) if f.startswith("index") and f.endswith(".html")]
    index_files.sort()
    
    all_articles = []
    nav_bar = None
    content_template = None
    
    for idx_file in index_files:
        path = os.path.join(blog_dir, idx_file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if nav_bar is None:
            nav_match = re.search(r'(<nav\b[^>]*>.*?</nav>)', content, re.DOTALL)
            if nav_match:
                nav_bar = nav_match.group(1)
                
        grid_match = re.search(r'(<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">)(.*?)(</div>\s*<div class="flex justify-center items-center space-x-2 mt-12">|</div>\s*</main>|</div>\s*<!--\s*Paginación)', content, re.DOTALL)
        if grid_match:
            articles_html = grid_match.group(2)
            arts = re.findall(r'<article.*?</article>', articles_html, re.DOTALL)
            all_articles.extend(arts)
            if content_template is None:
                # Store the before and after template from the first index
                before = content[:grid_match.start(2)]
                
                # capture everything after the grid
                after_match = re.search(r'</div>\s*(<div class="flex justify-center items-center space-x-2 mt-12">.*?</main>|</main>)', content[grid_match.end(2):], re.DOTALL)
                if after_match:
                    # we will rebuild the pagination so we just need </main> onwards
                    after = "\n</div>\n" + "{PAGINATION}" + "\n</main>" + content[grid_match.end(2) + after_match.end():]
                else:
                    after = "\n</div>\n" + "{PAGINATION}" + "\n</main>"
                
                content_template = (before, after)

    print(f"Total articles found: {len(all_articles)}")
    
    dates = get_dates()
    
    # Update dates for first 9
    for idx, article in enumerate(all_articles):
        if idx >= 9:
            break
            
        date_str = dates[idx]
        
        # Check if card already has date
        if '<i data-lucide="calendar" class="w-3 h-3"></i>' not in article:
            cat_match = re.search(r'<span class="text-xs font-bold uppercase text-brota-green bg-brota-green/10 px-3 py-1 rounded-full w-fit mb-4">(.*?)</span>', article)
            if cat_match:
                cat_text = cat_match.group(1)
                new_html = f'''<div class="flex items-center gap-3 mb-4">
                        <span class="text-xs font-bold uppercase text-brota-green bg-brota-green/10 px-3 py-1 rounded-full w-fit">{cat_text}</span>
                        <span class="text-xs text-gray-500 font-semibold flex items-center gap-1"><i data-lucide="calendar" class="w-3 h-3"></i> {date_str}</span>
                    </div>'''
                article = article.replace(cat_match.group(0), new_html)
                all_articles[idx] = article

        # Update file
        url_match = re.search(r'<a href="/blog/([^"]+\.html)"', article)
        if url_match:
            art_file = url_match.group(1)
            art_path = os.path.join(blog_dir, art_file)
            if os.path.exists(art_path):
                with open(art_path, 'r', encoding='utf-8') as f:
                    art_content = f.read()
                
                # Use a specific check to avoid CTA calendar icons
                date_html = f'<span class="text-gray-300 mx-1">•</span>\n                    <span class="text-gray-400 text-sm font-semibold flex items-center gap-1"><i data-lucide="calendar" class="w-4 h-4"></i> {date_str}</span>'
                
                if 'mx-1">•</span>' not in art_content:
                    read_time_pattern = r'(<span class="text-gray-400 text-sm font-semibold">[^<]*min de lectura</span>)'
                    art_content = re.sub(read_time_pattern, r'\1\n                    ' + date_html, art_content)
                    with open(art_path, 'w', encoding='utf-8') as f:
                        f.write(art_content)
                    print(f"Añadida fecha {date_str} a {art_file}")
                
    # Paginate and write
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

if __name__ == "__main__":
    main()

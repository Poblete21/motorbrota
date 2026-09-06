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

def strip_article_card_date(article):
    pattern = r'<div class="flex items-center gap-3 mb-4">\s*(<span class="text-xs font-bold uppercase text-brota-green bg-brota-green/10 px-3 py-1 rounded-full w-fit">.*?</span>)\s*<span class="text-xs text-gray-500 font-semibold flex items-center gap-1"><i data-lucide="calendar" class="w-3 h-3"></i>.*?</span>\s*</div>'
    def repl(m):
        span = m.group(1)
        return span.replace('rounded-full w-fit"', 'rounded-full w-fit mb-4"')
    return re.sub(pattern, repl, article)

def strip_article_file_date(content):
    pattern = r'(<span class="text-gray-400 text-sm font-semibold">[^<]*min de lectura</span>)\s*<span class="text-gray-300 mx-1">•</span>\s*<span class="text-gray-400 text-sm font-semibold flex items-center gap-1"><i data-lucide="calendar" class="w-4 h-4"></i>.*?</span>'
    return re.sub(pattern, r'\1', content)

def get_filename(article):
    url_match = re.search(r'<a href="/blog/([^"]+\.html)"', article)
    return url_match.group(1) if url_match else ""

def main():
    blog_dir = r"c:\Users\anton\Desktop\MKT\Brota Marketing\public\blog"
    
    index_files = ["index.html", "index-2.html", "index-3.html"]
    
    all_articles = []
    content_template = None
    
    for idx_file in index_files:
        path = os.path.join(blog_dir, idx_file)
        if not os.path.exists(path):
            continue
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

    print(f"Total articles found: {len(all_articles)}")
    
    # Strip dates from all individual files first
    for filename in os.listdir(blog_dir):
        if filename.endswith(".html") and not filename.startswith("index"):
            art_path = os.path.join(blog_dir, filename)
            with open(art_path, 'r', encoding='utf-8') as f:
                art_content = f.read()
            cleaned = strip_article_file_date(art_content)
            if cleaned != art_content:
                with open(art_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned)

    # Reorder articles explicitly
    order = [
        "diseno-flyer-publicitario-clinicas.html",
        "email-marketing-para-pymes-2026.html",
        "linkedin-para-empresas-b2b-2026.html",
        "eeat-seo-medico-ymyl.html",
        "marketing-pymes-lecciones-mundial-2026.html",
        "fidelizacion-pacientes-reducir-citas-perdidas.html",
        "pagina-web-para-clinicas.html",
        "reels-para-clinicas.html",
        "gestionar-opiniones-google.html",
        "seo-vs-geo-marketing-inteligencia-artificial.html",
        "calcular-roi-marketing-digital.html",
        "whatsapp-business-captar-clientes.html",
        "analisis-competencia-digital-seo.html",
        "web-pierde-ventas-3-segundos.html",
        "neuromarketing-ventas-digitales.html",
        "plan-marketing-paso-a-paso.html",
        "elegir-agencia-marketing-2026.html",
        "plan-marketing-pymes.html",
        "seo-local-google-maps.html",
        "necesito-pagina-web.html",
        "agencia-sem-campanas-ads.html",
        "web-no-aparece-google.html",
        "calendario-contenidos-redes.html",
        "email-marketing-para-pymes.html",
        "google-ads-vs-facebook-ads.html",
        "redes-sociales-sectores.html",
        "tiktok-reels-negocio-local.html"
    ]
    
    art_dict = {get_filename(art): strip_article_card_date(art) for art in all_articles}
    sorted_articles = []
    
    for f in order:
        if f in art_dict:
            sorted_articles.append(art_dict[f])
            del art_dict[f]
            
    # Add any remaining ones
    for f in art_dict:
        sorted_articles.append(art_dict[f])

    dates = get_dates()
    
    # Inject new ones for first 9
    for idx, article in enumerate(sorted_articles):
        if idx < 9:
            date_str = dates[idx]
            cat_match = re.search(r'<span class="text-xs font-bold uppercase text-brota-green bg-brota-green/10 px-3 py-1 rounded-full w-fit mb-4">(.*?)</span>', article)
            if cat_match:
                cat_text = cat_match.group(1)
                new_html = f'''<div class="flex items-center gap-3 mb-4">
                        <span class="text-xs font-bold uppercase text-brota-green bg-brota-green/10 px-3 py-1 rounded-full w-fit">{cat_text}</span>
                        <span class="text-xs text-gray-500 font-semibold flex items-center gap-1"><i data-lucide="calendar" class="w-3 h-3"></i> {date_str}</span>
                    </div>'''
                article = article.replace(cat_match.group(0), new_html)
            
            # Inject into file
            art_file = get_filename(article)
            art_path = os.path.join(blog_dir, art_file)
            if os.path.exists(art_path):
                with open(art_path, 'r', encoding='utf-8') as f:
                    art_content = f.read()
                
                date_html = f'<span class="text-gray-300 mx-1">•</span>\n                    <span class="text-gray-400 text-sm font-semibold flex items-center gap-1"><i data-lucide="calendar" class="w-4 h-4"></i> {date_str}</span>'
                read_time_pattern = r'(<span class="text-gray-400 text-sm font-semibold">[^<]*min de lectura</span>)'
                art_content = re.sub(read_time_pattern, r'\1\n                    ' + date_html, art_content)
                with open(art_path, 'w', encoding='utf-8') as f:
                    f.write(art_content)
                print(f"Re-añadida fecha {date_str} a {art_file}")
                    
        sorted_articles[idx] = article

    # Paginate and write
    items_per_page = 9
    total_pages = math.ceil(len(sorted_articles) / items_per_page)

    for page in range(1, total_pages + 1):
        start_idx = (page - 1) * items_per_page
        end_idx = start_idx + items_per_page
        page_articles = sorted_articles[start_idx:end_idx]

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

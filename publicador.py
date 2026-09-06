import os
import json
import datetime
import shutil
import re
import subprocess

# Configuración de las rutas de tus carpetas
PROGRAMADOS_DIR = "public/blog/programados"
BLOG_DIR = "public/blog"
INDEX_FILE = "public/blog/index.html"
SITEMAP_FILE = "public/sitemap.xml"

# Obtener la fecha de hoy
hoy_str = datetime.date.today().strftime("%Y-%m-%d")

# Verificar si existe la carpeta de programados (si no, la crea para evitar errores)
if not os.path.exists(PROGRAMADOS_DIR):
    os.makedirs(PROGRAMADOS_DIR)
    print("Carpeta de programados creada. No hay artículos para publicar.")
    exit()

archivos = os.listdir(PROGRAMADOS_DIR)
archivos_publicados = 0

for archivo in archivos:
    if not archivo.endswith(".html"): 
        continue
    
    # El formato es YYYY-MM-DD_slug.html, así que extraemos los 10 primeros caracteres
    fecha_str = archivo[:10]
    
    # Si la fecha del archivo es igual o anterior a hoy, toca publicarlo
    if fecha_str <= hoy_str:
        print(f"Publicando artículo: {archivo}...")
        
        ruta_origen = os.path.join(PROGRAMADOS_DIR, archivo)
        # El archivo final irá a /public/blog/ quitando la fecha del nombre
        slug_con_html = archivo[11:] 
        slug = slug_con_html.replace('.html', '')
        ruta_destino = os.path.join(BLOG_DIR, slug_con_html)
        
        with open(ruta_origen, "r", encoding="utf-8") as f:
            contenido = f.read()
        
        # Extraer los metadatos generados por la IA
        match = re.search(r'<!-- BROTA-META:\s*({.*?})\s*-->', contenido)
        if not match:
            print(f"Error: No se encontraron metadatos en {archivo}. Saltando...")
            continue
        
        meta = json.loads(match.group(1))
        
        # 1. Mover el archivo HTML a la carpeta pública de blog
        shutil.move(ruta_origen, ruta_destino)
        
        # 2. Preparar la fecha en formato texto (Ej: 8 Sep, 2026)
        fecha_obj = datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
        meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
        fecha_formateada = f"{fecha_obj.day} {meses[fecha_obj.month-1]}, {fecha_obj.year}"
        
        # 3. Crear el código HTML de la tarjeta para la portada
        tarjeta_html = f"""
        <article class="flex flex-col bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-lg transition-shadow duration-300">
            <a href="/blog/{slug_con_html}" class="block aspect-video overflow-hidden">
                <img src="{meta['image']}" alt="{meta['title']}" class="w-full h-full object-cover transition-transform duration-300 hover:scale-105">
            </a>
            <div class="p-6 flex flex-col flex-grow">
                <div class="flex items-center gap-3 mb-3">
                    <span class="text-xs font-bold px-3 py-1 bg-green-100 text-green-800 rounded-full">Marketing</span>
                    <span class="text-xs text-gray-500 font-semibold flex items-center gap-1"><i data-lucide="calendar" class="w-3 h-3"></i> {fecha_formateada}</span>
                </div>
                <a href="/blog/{slug_con_html}" class="block group">
                    <h3 class="text-xl font-bold text-gray-900 mb-2 group-hover:text-green-600 transition-colors line-clamp-2">{meta['title']}</h3>
                    <p class="text-gray-600 line-clamp-3 text-sm">{meta['description']}</p>
                </a>
                <div class="mt-auto pt-4">
                    <a href="/blog/{slug_con_html}" class="text-green-600 font-bold text-sm hover:underline inline-flex items-center gap-1">Leer artículo <i data-lucide="arrow-right" class="w-4 h-4"></i></a>
                </div>
            </div>
        </article>"""
        
        # 4. Inyectar la tarjeta en index.html (busca la primera etiqueta <article y la pone justo antes)
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            index_html = f.read()
        
        index_html = index_html.replace("<article", tarjeta_html + "\n<article", 1)
        
        with open(INDEX_FILE, "w", encoding="utf-8") as f:
            f.write(index_html)
            
        # 5. Inyectar la URL en el sitemap.xml
        sitemap_entry = f"""
    <url>
        <loc>https://brotamarketing.es/blog/{slug_con_html}</loc>
        <lastmod>{fecha_str}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>"""
        with open(SITEMAP_FILE, "r", encoding="utf-8") as f:
            sitemap_xml = f.read()
        
        sitemap_xml = sitemap_xml.replace("</urlset>", sitemap_entry + "\n</urlset>")
        
        with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
            f.write(sitemap_xml)
            
        archivos_publicados += 1

if archivos_publicados > 0:
    print("Cuadrando el grid con repaginar_blog.py...")
    subprocess.run(["python", "repaginar_blog.py"])
    print(f"¡Listo! Se han publicado {archivos_publicados} artículos nuevos.")
else:
    print("Todo al día. No hay artículos programados para hoy.")
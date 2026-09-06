import os
import re
import subprocess

def main():
    blog_dir = r"c:\Users\anton\Desktop\MKT\Brota Marketing\public\blog"
    slug = "marketing-influencers-pymes"
    article_path = os.path.join(blog_dir, f"{slug}.html")
    index_path = os.path.join(blog_dir, "index.html")
    
    # 1. Obtener el Navbar del template
    template_path = os.path.join(blog_dir, "agencia-sem-campanas-ads.html")
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    nav_match = re.search(r'(<nav\b[^>]*>.*?</nav>)', template_content, re.DOTALL)
    navbar = nav_match.group(1) if nav_match else ""
    
    # 2. Generar el contenido del nuevo artículo
    html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marketing de Influencers para Pymes: Cómo Colaborar sin Presupuesto | Brota Marketing</title>
    <meta name="description" content="Descubre cómo usar el marketing de influencers en tu pyme colaborando con micro y nanoinfluencers locales sin un gran presupuesto.">
    <meta name="author" content="Brota Marketing">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="Marketing de Influencers para Pymes: Guía 2026">
    <meta property="og:description" content="Aprende a colaborar con nanoinfluencers sin gastar como una gran empresa.">
    <meta property="og:type" content="article">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Outfit:wght@500;700;900&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        brota: {{
                            green: '#76bc21', dark: '#101820', light: '#f4f9f1', gray: '#f9fafb'
                        }}
                    }},
                    fontFamily: {{
                        sans: ['Nunito', 'sans-serif'], heading: ['Outfit', 'sans-serif']
                    }}
                }}
            }}
        }}
    </script>
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="font-sans text-brota-dark bg-brota-gray antialiased selection:bg-brota-green selection:text-white">
{navbar}

    <main>
        <article class="max-w-3xl mx-auto px-4 py-16 sm:py-24">
            
            <header class="mb-10">
                <div class="flex items-center gap-2 mb-6">
                    <span class="bg-brota-light text-brota-green font-bold px-3 py-1 rounded-full text-sm tracking-wide uppercase">Estrategia Digital</span>
                    <span class="text-gray-400 text-sm font-semibold">5 min de lectura</span>
                    <span class="text-gray-300 mx-1">•</span>
                    <span class="text-gray-400 text-sm font-semibold flex items-center gap-1"><i data-lucide="calendar" class="w-4 h-4"></i> 30 Jul, 2026</span>
                </div>
                
                <h1 class="font-heading font-black text-4xl lg:text-5xl text-brota-dark mb-8 leading-tight">
                    Marketing de Influencers para Pymes: Cómo Colaborar <span class="text-transparent bg-clip-text bg-gradient-to-r from-brota-green to-teal-500">sin Presupuesto de Gran Empresa</span>
                </h1>

                <figure class="mb-10">
                    <img src="https://loremflickr.com/1200/600/marketing,influencer" 
                         alt="Marketing de Influencers" 
                         class="w-full h-auto object-cover aspect-video rounded-3xl shadow-xl border border-gray-100 mb-2">
                </figure>
            </header>

            <section class="mb-12">
                <p class="text-lg text-gray-600 leading-relaxed mb-6">
                    Cuando escuchas "marketing de influencers", probablemente piensas en marcas grandes pagando decenas de miles de euros a celebrities con millones de seguidores. Y te parece algo completamente fuera de tu alcance si tienes una pyme.
                </p>
                <p class="text-lg text-gray-600 leading-relaxed mb-6">
                    Error. Y un error caro, porque estás dejando escapar uno de los canales con mayor capacidad de generar confianza y ventas a nivel local.
                </p>
                <blockquote class="italic text-xl text-brota-dark bg-brota-green/10 border-l-4 border-brota-green p-6 rounded-r-xl my-8 shadow-sm">
                    La realidad es que el marketing de influencers más efectivo en 2026 no lo hacen los famosos con millones de seguidores. Lo hacen los <strong>microinfluencers y nanoinfluencers</strong>: perfiles locales y comprometidos, accesibles para cualquier presupuesto.
                </blockquote>
            </section>
            
            <section class="mb-12">
                <h2 class="font-heading font-bold text-2xl lg:text-3xl text-brota-dark mt-10 mb-6 flex items-center gap-3">
                    <span class="bg-brota-green text-white w-10 h-10 rounded-full flex items-center justify-center text-xl shadow-md">1</span>
                    La diferencia entre Macro, Micro y Nanoinfluencer
                </h2>
                <div class="grid gap-4 mt-8 mb-8">
                    <div class="bg-white p-5 rounded-2xl shadow-sm border border-gray-100 flex flex-col gap-4">
                        <strong class="text-xl text-brota-dark font-heading">Macroinfluencers (+500k)</strong>
                        <p class="text-gray-700">Precios muy altos (desde 3.000€). Solo tienen sentido para marcas nacionales con presupuestos masivos.</p>
                    </div>
                    <div class="bg-white p-5 rounded-2xl shadow-sm border border-gray-100 flex flex-col gap-4">
                        <strong class="text-xl text-brota-green font-heading">Microinfluencers (10k a 100k)</strong>
                        <p class="text-gray-700">El punto dulce para las pymes. Alta credibilidad y tasas de engagement superiores. Suelen cobrar entre 100€ y 800€, a veces incluso aceptan producto.</p>
                    </div>
                    <div class="bg-white p-5 rounded-2xl shadow-sm border border-gray-100 flex flex-col gap-4">
                        <strong class="text-xl text-brota-green font-heading">Nanoinfluencers (1k a 10k)</strong>
                        <p class="text-gray-700">Perfiles hiperlocales. Engagement altísimo. Muchas colaboraciones son a cambio de producto o experiencias (invitaciones a restaurantes, tratamientos, etc).</p>
                    </div>
                </div>
            </section>
            
            <section class="mb-12">
                <h2 class="font-heading font-bold text-2xl lg:text-3xl text-brota-dark mt-10 mb-6 flex items-center gap-3">
                    <span class="bg-brota-green text-white w-10 h-10 rounded-full flex items-center justify-center text-xl shadow-md">2</span>
                    Cómo medir los resultados (Evita los errores)
                </h2>
                <p class="text-lg text-gray-600 leading-relaxed mb-6">
                    Sin métricas, no sabes si has ganado dinero. Utiliza estas 3 tácticas:
                </p>
                <ul class="space-y-4 mb-8">
                    <li class="flex items-start">
                        <i data-lucide="check" class="text-brota-green mr-3 mt-1 flex-shrink-0"></i>
                        <span class="text-lg text-gray-600 leading-relaxed"><strong>Código descuento único:</strong> Un cupón personalizado te dirá exactamente de dónde viene cada venta.</span>
                    </li>
                    <li class="flex items-start">
                        <i data-lucide="check" class="text-brota-green mr-3 mt-1 flex-shrink-0"></i>
                        <span class="text-lg text-gray-600 leading-relaxed"><strong>Enlaces con UTM:</strong> Crea links rastreables para medir en Google Analytics todo el tráfico real.</span>
                    </li>
                    <li class="flex items-start">
                        <i data-lucide="check" class="text-brota-green mr-3 mt-1 flex-shrink-0"></i>
                        <span class="text-lg text-gray-600 leading-relaxed"><strong>Medición directa:</strong> En negocios físicos, pregunta siempre a los nuevos clientes cómo os han conocido.</span>
                    </li>
                </ul>
                <div class="bg-red-50 border-l-4 border-red-500 p-5 rounded-r-xl flex items-start gap-3 mt-6">
                        <i data-lucide="alert-triangle" class="text-red-500 mt-1 flex-shrink-0"></i>
                        <p class="text-lg text-gray-700 leading-relaxed">
                            <strong class="text-red-700">Error a evitar:</strong> No cumplas la ley. En España la CNMC exige etiquetar el contenido como #publicidad, de lo contrario ambos os enfrentáis a multas.
                        </p>
                </div>
            </section>

            <section class="bg-brota-light p-8 md:p-12 rounded-3xl mt-16 border border-brota-green/20 text-center shadow-sm relative overflow-hidden">
                <div class="absolute top-0 right-0 -mr-8 -mt-8 w-32 h-32 rounded-full bg-brota-green opacity-10"></div>
                <h3 class="font-heading font-bold text-3xl text-brota-dark mb-4 relative z-10">¿Quieres una estrategia para tu negocio?</h3>
                <p class="text-lg text-gray-700 leading-relaxed mb-8 max-w-2xl mx-auto relative z-10">
                    En Brota Marketing identificamos los perfiles adecuados para tu sector y zona, diseñamos la colaboración y medimos los resultados. Sin humo, sin seguidores comprados, sin dinero tirado.
                </p>
                <a href="https://brotamarketing.es/#contacto" class="bg-brota-green text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-brota-dark hover:-translate-y-1 transition-all duration-300 shadow-lg inline-flex items-center gap-2 relative z-10">
                    Pide tu consultoría gratuita
                    <i data-lucide="arrow-right" class="w-5 h-5"></i>
                </a>
            </section>
        </article>
    </main>
    <script>lucide.createIcons();</script>
    <script src="/cookie-banner.js"></script>
</body>
</html>'''

    with open(article_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Creado articulo: {article_path}")

    # 3. Actualizar index.html
    new_card = f'''
                <!-- Artículo Influencers -->
                <article class="bg-white rounded-3xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-xl hover:-translate-y-2 transition-all duration-300 flex flex-col group reveal">
                    <a href="/blog/{slug}.html" class="block h-52 overflow-hidden relative bg-brota-light">
                        <img src="https://loremflickr.com/1200/600/marketing,influencer" alt="Marketing de Influencers Pymes" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    </a>
                    <div class="p-8 flex-grow flex flex-col">
                        <div class="flex items-center gap-3 mb-4">
                            <span class="text-xs font-bold uppercase text-brota-green bg-brota-green/10 px-3 py-1 rounded-full w-fit">Estrategia Digital</span>
                            <span class="text-xs text-gray-500 font-semibold flex items-center gap-1"><i data-lucide="calendar" class="w-3 h-3"></i> 30 Jul, 2026</span>
                        </div>
                        <a href="/blog/{slug}.html">
                            <h2 class="font-heading text-xl font-bold text-brota-dark mb-3 leading-tight group-hover:text-brota-green transition-colors">Marketing de Influencers para Pymes: Cómo Colaborar sin Presupuesto</h2>
                        </a>
                        <p class="text-gray-500 text-sm mb-6 line-clamp-3">Descubre cómo usar el marketing de influencers en tu pyme colaborando con micro y nanoinfluencers locales sin un gran presupuesto.</p>
                        <a href="/blog/{slug}.html" class="mt-auto inline-flex items-center text-brota-dark font-bold group-hover:text-brota-green transition-colors w-fit">
                            Leer artículo <i data-lucide="arrow-right" class="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform"></i>
                        </a>
                    </div>
                </article>'''

    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()

    grid_pattern = r'(<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">)'
    if re.search(grid_pattern, index_content):
        updated_index = re.sub(grid_pattern, r'\1\n' + new_card, index_content, count=1)
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(updated_index)
        print("index.html actualizado")

    # 4. Repaginar
    print("Ejecutando repaginación...")
    subprocess.run(["python", r"c:\Users\anton\Desktop\MKT\Brota Marketing\repaginar_blog.py"], check=True)
    
    # 5. Limpieza
    pdf_path = r"c:\Users\anton\Desktop\MKT\Brota Marketing\public\blog\pdf\16.blog_ Marketing de Influencerspdf.pdf"
    if os.path.exists(pdf_path):
        os.remove(pdf_path)
        print("PDF eliminado")

if __name__ == "__main__":
    main()

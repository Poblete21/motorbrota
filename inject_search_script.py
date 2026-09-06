import os

path = r"c:\Users\anton\Desktop\MKT\Brota Marketing\public\blog\index.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

script = """<script>
    document.addEventListener("DOMContentLoaded", () => {
        const searchInput = document.getElementById('blog-search-input');
        const resultsContainer = document.getElementById('search-results-container');
        let articlesData = [];
        if(searchInput && resultsContainer) {
            fetch('/blog/search_index.json')
                .then(res => res.json())
                .then(data => { articlesData = data; })
                .catch(err => console.error("Error cargando buscador:", err));
            searchInput.addEventListener('input', (e) => {
                const query = e.target.value.toLowerCase().trim();
                resultsContainer.innerHTML = '';
                if (query.length < 2) {
                    resultsContainer.classList.add('hidden');
                    resultsContainer.classList.remove('flex');
                    return;
                }
                const filtered = articlesData.filter(art => 
                    art.title.toLowerCase().includes(query) || 
                    art.description.toLowerCase().includes(query) || 
                    art.category.toLowerCase().includes(query)
                );
                if (filtered.length === 0) {
                    resultsContainer.innerHTML = '<div class="p-4 text-center text-gray-500">No se encontraron artículos.</div>';
                } else {
                    filtered.forEach(art => {
                        const resultEl = document.createElement('a');
                        resultEl.href = art.url;
                        resultEl.className = "block p-4 hover:bg-brota-light transition-colors border-b border-gray-50 last:border-0";
                        resultEl.innerHTML = `
                            <div class="text-xs text-brota-green font-bold uppercase mb-1">${art.category}</div>
                            <div class="font-bold text-brota-dark">${art.title}</div>
                            <div class="text-sm text-gray-500 line-clamp-1">${art.description}</div>
                        `;
                        resultsContainer.appendChild(resultEl);
                    });
                }
                resultsContainer.classList.remove('hidden');
                resultsContainer.classList.add('flex');
                if(typeof lucide !== 'undefined') lucide.createIcons();
            });
            document.addEventListener('click', (e) => {
                if (!searchInput.contains(e.target) && !resultsContainer.contains(e.target)) {
                    resultsContainer.classList.add('hidden');
                    resultsContainer.classList.remove('flex');
                }
            });
        }
    });
</script>
</body>"""

if "search_index.json" not in content:
    content = content.replace("</body>", script)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Injected script properly!")

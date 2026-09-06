document.addEventListener('DOMContentLoaded', () => {
    // Si ya aceptó las cookies, no mostramos nada
    if (localStorage.getItem('cookiesAccepted')) {
        return;
    }

    // Si ya se le mostró el banner en esta sesión y no lo aceptó, tampoco lo volvemos a mostrar al cambiar de página
    if (sessionStorage.getItem('cookieBannerShown')) {
        return;
    }

    const bannerHTML = `
    <div id="cookie-banner" class="fixed bottom-0 left-0 right-0 bg-brota-dark/95 backdrop-blur-md text-white p-4 sm:p-6 shadow-[0_-10px_40px_rgba(0,0,0,0.3)] z-[100] transform translate-y-full transition-transform duration-500 ease-in-out border-t border-white/10">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
            <div class="text-sm sm:text-base text-gray-300 flex-1">
                Utilizamos cookies propias y de terceros para analizar nuestros servicios y mostrarte publicidad relacionada con tus preferencias. 
                Puedes obtener más información en nuestra <a href="/cookies/" class="text-brota-green font-bold hover:underline">Política de Cookies</a>.
            </div>
            <div class="flex gap-4 w-full sm:w-auto">
                <button id="accept-cookies-btn" class="w-full sm:w-auto bg-brota-green text-white px-8 py-2.5 rounded-xl font-bold hover:bg-white hover:text-brota-dark transition-all duration-300 shadow-lg shadow-brota-green/20">
                    Aceptar
                </button>
            </div>
        </div>
    </div>
    `;

    document.body.insertAdjacentHTML('beforeend', bannerHTML);

    const banner = document.getElementById('cookie-banner');
    const acceptBtn = document.getElementById('accept-cookies-btn');

    // Desplegamos el banner
    setTimeout(() => {
        banner.classList.remove('translate-y-full');
        // Registramos que ya se mostró en esta sesión
        sessionStorage.setItem('cookieBannerShown', 'true');
    }, 1000);

    // Acción de aceptar
    acceptBtn.addEventListener('click', () => {
        localStorage.setItem('cookiesAccepted', 'true');
        banner.classList.add('translate-y-full');
        setTimeout(() => {
            if (banner.parentNode) {
                banner.parentNode.removeChild(banner);
            }
        }, 500);
    });
});

@echo off
echo ==============================================
echo 1. Descargando publicaciones automaticas de la nube...
echo ==============================================
git pull origin main
echo.
echo ==============================================
echo 2. Subiendo nuevos articulos programados...
echo ==============================================
git add .
git commit -m "Nuevos articulos programados subidos"
git push
echo.
echo ==============================================
echo ¡Listo! Tu ordenador y la nube estan 100% sincronizados.
echo ==============================================
pause
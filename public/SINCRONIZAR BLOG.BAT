@echo off
cd %~dp0
echo ==============================================
echo 1. Descargando publicaciones automaticas de la nube...
echo ==============================================
git pull origin main
echo.
echo ==============================================
echo 2. Subiendo nuevos articulos y configuraciones...
echo ==============================================
git add -A
git commit -m "Sincronizacion de articulos y configuracion"
git push
echo.
echo ==============================================
echo ¡Listo! Tu ordenador y la nube estan 100%% sincronizados.
echo ==============================================
pause
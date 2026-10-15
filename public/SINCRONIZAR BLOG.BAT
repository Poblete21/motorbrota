@echo off
cd %~dp0
echo ==============================================
echo 1. Guardando cambios locales...
echo ==============================================
git add -A
git commit -m "Sincronizacion de articulos y configuracion" 2>nul
echo.
echo ==============================================
echo 2. Descargando publicaciones automaticas de la nube...
echo ==============================================
git pull --rebase origin main
echo.
echo ==============================================
echo 3. Subiendo nuevos articulos y configuraciones...
echo ==============================================
git push origin main
echo.
echo ==============================================
echo ¡Listo! Tu ordenador y la nube estan 100%% sincronizados.
echo ==============================================
pause
@echo off
echo ==============================================
echo Sincronizando nuevos articulos con GitHub...
echo ==============================================
git add .
git commit -m "Nuevos articulos programados subidos"
git push
echo.
echo ==============================================
echo ¡Listo! Los articulos ya estan en el taller en la nube.
echo ==============================================
pause
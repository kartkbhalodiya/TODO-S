@echo off
echo ============================================
echo   NOVA AI — Backend Server
echo ============================================
echo.

REM Navigate to backend directory
cd /d "%~dp0"

REM Apply migrations
echo [1/3] Applying migrations...
python manage.py migrate
if %errorlevel% neq 0 (
    echo ERROR: Migrations failed!
    pause
    exit /b 1
)

REM Create superuser if not exists
echo [2/3] Checking superuser...
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@nova.ai', 'admin123'); print('Superuser ready: admin / admin123')" 2>nul

REM Start server
echo [3/3] Starting development server...
echo.
echo Backend running at: http://127.0.0.1:8000
echo API base:           http://127.0.0.1:8000/api
echo Admin panel:        http://127.0.0.1:8000/admin/
echo.
python manage.py runserver 0.0.0.0:8000

pause

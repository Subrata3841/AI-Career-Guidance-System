@echo off
echo Starting AI Career Compass application...

echo 0. Running the model to ensure it's up to date...
"D:\SIH-2024-1781-main\.venv\Scripts\python.exe" "d:\SIH-2024-1781-main\SIH-2024-1781-main\simple_model_runner.py"

echo 1. Starting the API server...
start cmd /k ""D:\SIH-2024-1781-main\.venv\Scripts\python.exe" "d:\SIH-2024-1781-main\SIH-2024-1781-main\simple_api_server.py""

echo 2. Opening the frontend in your browser...
timeout /t 3
start "" "d:\SIH-2024-1781-main\SIH-2024-1781-main\simple_frontend.html"

echo.
echo =======================================================
echo AI Career Guidance is now running!
echo =======================================================
echo API Server: http://localhost:5000
echo Frontend: Open in your default browser
echo.
echo Press any key to stop the application...
pause > nul
taskkill /f /im python.exe
echo Application stopped.
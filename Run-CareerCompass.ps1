# PowerShell script to run AI Career Compass
Write-Host "Starting AI Career Compass application..." -ForegroundColor Green

# Get the current script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Step 1: Run the model
Write-Host "Step 1: Running the model..." -ForegroundColor Cyan
& python "$scriptDir\simple_model_runner.py"

# Step 2: Start the API server in a new PowerShell window
Write-Host "Step 2: Starting the API server..." -ForegroundColor Cyan
$apiProcess = Start-Process -FilePath "powershell.exe" -ArgumentList "-Command & python '$scriptDir\simple_api_server.py'" -PassThru

# Step 3: Wait a moment for the server to start
Write-Host "Waiting for API server to start..." -ForegroundColor Yellow
Start-Sleep -Seconds 3

# Step 4: Open the frontend in the default browser
Write-Host "Step 3: Opening the frontend..." -ForegroundColor Cyan
Start-Process "$scriptDir\simple_frontend.html"

Write-Host ""
Write-Host "=======================================================" -ForegroundColor Green
Write-Host "AI Career Guidance System is now running!" -ForegroundColor Green
Write-Host "=======================================================" -ForegroundColor Green
Write-Host "API Server: http://localhost:5000"
Write-Host "Frontend: Opened in your default browser"
Write-Host ""
Write-Host "Press Enter to stop the application..." -ForegroundColor Yellow
Read-Host

# Stop the API server process
if ($apiProcess) {
    Stop-Process -Id $apiProcess.Id -Force
    Write-Host "API server stopped." -ForegroundColor Cyan
}

Write-Host "Application stopped." -ForegroundColor Green
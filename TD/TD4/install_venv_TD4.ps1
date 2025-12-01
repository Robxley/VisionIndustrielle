# ===========================================================
#   Vision Industrielle Python environment setup (Windows)
#   Virtual environment name : opencv_env
#   Auto-create requirements.txt if missing
# ===========================================================

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Write-Host "=== Starting VisionIndustrielle setup ==="

# -------- Determine current script location --------
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# -------- Determine target folder (VisionIndustrielle) --------
$desktop = [Environment]::GetFolderPath("Desktop")
$targetDir = Join-Path $desktop "VisionIndustrielle"
Write-Host "Target directory: $targetDir"

# -------- Create target directory if missing --------
if (!(Test-Path $targetDir)) {
    Write-Host "Creating VisionIndustrielle directory..."
    New-Item -ItemType Directory -Path $targetDir | Out-Null
} else {
    Write-Host "VisionIndustrielle directory already exists. Updating..."
}

# -------- Move script execution into target folder --------
Set-Location $targetDir

# -------- Check Python presence --------
Write-Host "Checking Python availability..."
$pythonCheck = python --version 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Python not installed or not in PATH." -ForegroundColor Red
    exit 1
}

# -------- Create requirements.txt if missing --------
$srcReq = Join-Path $scriptDir "requirements.txt"
$dstReq = Join-Path $targetDir "requirements.txt"

if (Test-Path $srcReq) {
    Write-Host "Found requirements.txt next to script. Copying..."
    Copy-Item $srcReq -Destination $dstReq -Force
}
else {
    if (!(Test-Path $dstReq)) {
        Write-Host "Creating new requirements.txt..."
        @(
            "numpy"
            "opencv-python"
            "matplotlib"
            "notebook"
            "jupyterlab"
            "ipykernel"
        ) | Set-Content -Path $dstReq -Encoding UTF8
    }
    else {
        Write-Host "requirements.txt already exists in target directory."
    }
}

# -------- Check venv existence --------
$venvPath = ".\opencv_env"
$venvExists = Test-Path $venvPath

if ($venvExists) {
    Write-Host "opencv_env detected. Updating existing environment..."
} else {
    Write-Host "opencv_env missing. Creating new environment..."
    python -m venv opencv_env

    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERROR: Could not create virtual environment." -ForegroundColor Red
        exit 1
    }
}

# -------- Activate venv --------
Write-Host "Activating virtual environment..."
$activate = ".\opencv_env\Scripts\Activate.ps1"
if (Test-Path $activate) {
    & $activate
} else {
    Write-Host "ERROR: Activation script missing." -ForegroundColor Red
    exit 1
}

# -------- Update pip --------
Write-Host "Updating pip..."
.\opencv_env\Scripts\python.exe -m pip install --upgrade pip

# -------- Install required modules from requirements.txt --------
Write-Host "Installing modules from requirements.txt..."
.\opencv_env\Scripts\python.exe -m pip install --upgrade -r requirements.txt

# -------- Register kernel --------
Write-Host "Registering Jupyter kernel..."
$kernelName = "opencv_env"
.\opencv_env\Scripts\python.exe -m ipykernel install --user --name $kernelName --display-name "Python ($kernelName)" --force

# -------- Copy TD4 files if present next to script --------
Write-Host "Checking for TD4 files to copy..."
$filesToCopy = @(
    "TD4-Traitement_image.ipynb",
    "TD4-Traitement_image.py"
)

foreach ($file in $filesToCopy) {
    $source = Join-Path $scriptDir $file
    if (Test-Path $source) {
        Write-Host "Copying $file..."
        Copy-Item $source -Destination $targetDir -Force
    }
}

# -------- Configure VS Code --------
Write-Host "Configuring VS Code..."
$settingsDir = ".vscode"
if (!(Test-Path $settingsDir)) {
    New-Item -ItemType Directory -Path $settingsDir | Out-Null
}

$settingsObj = @{
    "python.defaultInterpreterPath" = ".\opencv_env\Scripts\python.exe"
    "jupyter.jupyterServerType" = "local"
}

$settingsJson = $settingsObj | ConvertTo-Json -Depth 5
Set-Content -Path ".vscode\settings.json" -Value $settingsJson -Encoding UTF8

Write-Host "=== Setup complete ===" -ForegroundColor Green
Write-Host "Location: $targetDir"
Write-Host "Open VS Code and select: Python (opencv_env)"

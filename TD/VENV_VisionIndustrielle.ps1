$venv_path = [System.IO.Path]::Combine($env:UserProfile, "Desktop\VisionIndustrielle\env_opencv")

Set-Location $env:UserProfile\Desktop

Write-Host "Dossier d'installation de l'environnement python:"
Write-Host $venv_path

# Assurez-vous que le chemin vers l'exécutable Python est correct.
$python_executable = "C:\python38-64\python.exe"

& $python_executable --version

Write-Host "Creation de l'environnement virtuel en cours..."

# Vérifiez si l'environnement virtuel existe déjà.
if (Test-Path (Join-Path $venv_path "Scripts\activate.bat")) {
    Write-Host "L'environnement virtuel existe déjà à l'emplacement spécifié."
} else {
    # Créez l'environnement virtuel s'il n'existe pas.
    & $python_executable -m venv $venv_path
    Write-Host "L'environnement virtuel a été créé avec succès à l'emplacement : $venv_path"
}

if (Test-Path (Join-Path $venv_path "Scripts\activate.bat")) {
    Write-Host "Activation de l'environnement : $($venv_path)\Scripts\activate.bat"
    Set-Location $venv_path
    .\Scripts\activate.bat
    pip --version
    python -m pip install --upgrade pip
    python -m pip install opencv-python matplotlib ipykernel
    Write-Host "Creation de l'environnement virtuel terminee"
} else {
    Write-Host "L'environnement virtuel n'est pas activable : $($venv_path)\Scripts\activate.bat"
}

Pause

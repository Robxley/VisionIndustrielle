@echo off

set "venv_path=%UserProfile%\Desktop\VisionIndustrielle\env_opencv"
echo Dossier d'installation de l'environnement python:
echo %venv_path%

set "python_executable=%~1"
REM Assurez-vous que le chemin vers l'exécutable Python est correct.
if exist "%python_executable%" (
    echo Localisation de python : %python_executable%
) else (
    echo "Commande python par defaut"
    set "python_executable=python"
)

if not exist %python_executable% (
    echo python not found
    pause
    Exit /b
)

%python_executable% --version

echo Creation de l'environnement virtuel en cours...

REM Vérifiez si l'environnement virtuel existe déjà.
if exist "%venv_path%\Scripts\activate.bat" (
    echo L'environnement virtuel existe deja a l'emplacement specifie.
) else (
    REM Créez l'environnement virtuel s'il n'existe pas.
    %python_executable% -m venv "%venv_path%"
    echo L'environnement virtuel a ete cree avec succes a l'emplacement : %venv_path%
)

if exist "%venv_path%\Scripts\activate.bat" (
    echo Activation de l'environnement : %venv_path%\Scripts\activate.bat
    cd %venv_path%
    .\Scripts\activate.bat
    pip --version
    python -m pip install --upgrade pip
    python -m pip install opencv-python matplotlib
    python -m pip install ipykernel
)
else (
    echo L'environnement virtuel n'est pas activable : %venv_path%\Scripts\activate.bat
)

pause
@echo off
set "venv_path=%UserProfile%\Desktop\VisionIndustrielle\env_opencv"

cd %UserProfile%\Desktop

echo Dossier d'installation de l'environnement python:
echo %venv_path%

REM Assurez-vous que le chemin vers l'exécutable Python est correct.
set "python_executable=python"

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
)
else (
    echo L'environnement virtuel n'est pas activable : %venv_path%\Scripts\activate.bat
)

pause
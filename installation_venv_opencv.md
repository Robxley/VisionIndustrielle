### Prérequis

Préparation d’un environnement Python et installation du paquet OpenCV :  
[Documentation officielle](https://docs.python.org/fr/3/tutorial/venv.html)

1. Créez un dossier 📂 **VisionIndustrielle** (par exemple sur le bureau) et ouvrez-le.
2. Faites `Shift + clic droit` dans ce dossier.
3. Choisissez `Ouvrir la fenêtre PowerShell ici`.
4. Exécutez les commandes suivantes pour préparer l’environnement Python :

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install jupyter opencv-python matplotlib ipykernel
```
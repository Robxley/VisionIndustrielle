# TD4 – Prérequis: traitement d’image

## Préparation d’un environnement virtuel pour le traitement d’image avec ```Python``` et la librairie ```OpenCV```.

Documentation : https://opencv.org/  
Documentation : https://docs.python.org/fr/3/tutorial/venv.html  

1.	Lancer l’invite de commande cmd.exe.
3.	Exécuter les commandes suivantes pour l’installation d’un environnement python et des librairies (packages) ```OpenCV``` et ```matplotlib``` :

    - Création de l'environnement (sur votre bureau dans le dossier VisionIndustrielle/env_opencv) :
        > ```python -m venv "%UserProfile%/Desktop/VisionIndustrielle/env_opencv"```

    - Aller dans le dossier d’environnement « env_opencv » en tapant la commande suivante :  
        > ```cd "%UserProfile%/Desktop/VisionIndustrielle/env_opencv"```

    - Activer l’environnement :  
        > ```.\Scripts\activate.bat```  

        Lorsque l’environnement est activé suite à cette commande, vous devez avoir (env_opencv) au niveau de votre invite de commande quelque chose comme ceci : 
        > ```(env_opencv) C:\Users\ac268552\Desktop\VisionIndustrielle> ```
    
    - Mise à jour de l'installeur de packages ```pip``` : 
        > ```python -m pip install --upgrade pip``` 

    - Installer les librairies/packages ```opencv```, ```matplotlib``` et ```ipykernel``` (avec cmd.exe)
        > ```pip install opencv-python ipykernel matplotlib```  

4.	Ouvrer le dossier VisionIndustrielle dans VSCode.
5.	Créer un Jupyter notebook « TD4-Traitement_image.ipynb »
6.	Ajouter une cellule de code et importer les librairies OpenCV et numpy en copiant le code suivant :
    > ```import cv2```  
    > ```import numpy as np```

7.	Exécuter la cellule et vérifier l’absence de message d’erreur pour valider la bonne configuration de l’environnement de travail.

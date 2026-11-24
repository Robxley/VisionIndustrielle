# TD 4 : Vision par ordinateur — Traitement d'image

## Prérequis

Préparation d'un environnement Python et installation du paquet OpenCV :

1. Créez un dossier **VisionIndustrielle** (par exemple sur le bureau) et ouvrez-le.
2. Faites `Shift + clic droit` dans ce dossier.
3. Choisissez `Ouvrir la fenêtre PowerShell ici`.
4. Exécutez les commandes suivantes pour préparer l'environnement Python :

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install jupyter opencv-python matplotlib ipykernel
```

> Documentation officielle : [https://docs.python.org/fr/3/tutorial/venv.html](https://docs.python.org/fr/3/tutorial/venv.html)

---

## Manipulations

### 1. Lecture d'une image en niveaux de gris

1. Consultez la documentation de la fonction `cv2.imread` dans la documentation d'OpenCV.
2. Utilisez `cv2.imread` pour lire l'image `../images/fruits.jpg` en mode niveaux de gris (`cv2.IMREAD_GRAYSCALE`).
3. Affichez les dimensions de l'image avec `.shape` et identifiez les indices correspondant aux lignes et colonnes.

### 2. Affichage d'une image avec Matplotlib

1. Consultez la documentation de `imshow` (paramètre `cmap="gray"`).
2. Expérimentez en modifiant `cmap="gray"` pour observer les effets.
3. Créez une fonction `implot` pour simplifier l'affichage des images.

### 3. Image en couleur

1. Lisez `../images/fruits.jpg` avec `cv2.IMREAD_UNCHANGED`.
2. Affichez les dimensions (lignes, colonnes, canaux de couleur).
3. Affichez l'image en couleur avec `implot`.
4. Recherchez les différents encodages couleur (RGB, BGR, LAB, HSV, etc.).
5. Documentez-vous sur le filtre de Bayer et son rôle dans les capteurs.

### 4. Affichage de l'image en couleur avec OpenCV

1. Utilisez `cv2.imshow` et `cv2.waitKey` pour afficher une image en couleur.
2. Créez une fonction `imshow_cv` pour simplifier les affichages futurs.

### 5. Convertir l'image en RGB pour Matplotlib

1. Convertissez en RGB en inversant les canaux via les indices du tableau NumPy.
2. Alternative : utilisez `cv2.cvtColor`.

### 6. Canaux de couleur (R, V, B)

1. Affichez les canaux rouge, vert et bleu séparément.
2. Concaténez-les avec `np.vstack` ou `cv2.hconcat`.
3. Affichez les canaux pour les encodages LAB et HSV (`cv2.cvtColor`).

### 7. Opérations élémentaires entre images en niveaux de gris

1. Sélectionnez les canaux R, V et/ou B.
2. Testez addition, soustraction, multiplication entre canaux (opérateurs NumPy ou `cv2.add`, `cv2.subtract`, etc.).
3. Vérifiez la cohérence des résultats et la profondeur (`dtype`) de l'image.
4. Passez en flottant 32 bits avec `.astype(np.float32)` pour les calculs.

### 8. Opérations élémentaires entre images couleur

1. Chargez deux images couleur. Créez une fonction de lecture BGR → RGB automatique.
2. Testez addition, soustraction, multiplication, division (`cv2.addWeighted`, etc.).
3. Testez les opérateurs binaires : `np.bitwise_and`, `np.bitwise_or`, `np.bitwise_xor` (ou équivalents OpenCV).

### 9. Filtrage

1. Appliquez `cv2.boxFilter` ou `cv2.GaussianBlur` pour lisser une image.
2. Répétez avec `cv2.medianBlur` (filtre médian).

### 10. Génération de bruit gaussien

Utilisez la fonction fournie `add_noise(img, mean, stddev, threshold)` pour bruiter artificiellement une image.

### 11. Filtrage du bruit

1. Bruitez une image avec `add_noise`.
2. Testez plusieurs filtres (`cv2.boxFilter`, `cv2.GaussianBlur`, `cv2.medianBlur`) avec différents paramètres.

### 12. Détection de contours (gradients)

1. Appliquez `cv2.Sobel` sur une image couleur (directions X et Y).
2. Modifiez les paramètres du filtre.
3. Combinez les gradients avec `cv2.magnitude` ou `cv2.convertScaleAbs` + `cv2.addWeighted`.
4. Normalisez avec `cv2.normalize` (`norm_type=cv2.NORM_MINMAX`).
5. Expérimentez `cv2.Laplacian`.

### 13. Seuillage / Segmentation

1. Additionnez les canaux R, G, B du gradient.
2. Appliquez un seuillage avec :
   - `cv2.threshold`
   - `cv2.adaptiveThreshold`
   - `cv2.inRange`

### 14. Morphologie mathématique

1. Sur une image segmentée, testez :
   - `cv2.erode`
   - `cv2.dilate`
   - `cv2.morphologyEx`
2. Expliquez ce qu'est une ouverture et une dilatation.

### 15. Détection de contours : Canny

1. Utilisez `cv2.Canny`.
2. Comptez les pixels de contour avec `cv2.countNonZero`.

### 16. Manipulation des images

1. `cv2.resize`
2. `cv2.pyrDown`
3. `cv2.flip` (différents paramètres)
4. Sélection d'une région d'intérêt (ROI)

### 17. Dessin dans une image

1. Texte : `cv2.putText`
2. Ligne : `cv2.line`
3. Rectangle : `cv2.rectangle`
4. Cercle : `cv2.circle`
5. Ellipse : `cv2.ellipse`

### 18. Histogramme

1. Sélectionnez le canal rouge d'une image.
2. Calculez son histogramme avec `cv2.calcHist` ou `np.histogram`.
3. Affichez-le avec `plt.hist`.

### 19. Application : détection de défaut — Contrôle d'ébréchure

1. Chargez `../images/controle-ébrechure.jpg` et `../images/controle-ébrechure_2.jpg`.
2. Effectuez la différence entre ces deux images.
3. Appliquez un seuillage sur la différence.
4. Comptez les pixels différents avec `cv2.countNonZero`.
5. Répétez l'opération en ajoutant du bruit avec `add_noise`.

---

## Ressources

- [OpenCV Tutorial — Introduction](https://docs.opencv.org/4.8.0/d6/d00/tutorial_py_root.html)
- [OpenCV Tutorial — Image Processing](https://docs.opencv.org/4.8.0/d2/d96/tutorial_py_table_of_contents_imgproc.html)

## Fichiers associés

- Notebook Jupyter : [TD4-Traitement_image.ipynb](TD4-Traitement_image.ipynb)
- Script Python : [TD4-Traitement_image.py](TD4-Traitement_image.py)
- Images de test : [images/](images/)

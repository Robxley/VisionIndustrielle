# TD 5 : Analyse vidéo — Détection de mouvement par soustraction de fond

## Contexte

Ce TD porte sur l'analyse d'une **séquence vidéo** (flux d'images) afin de détecter les objets en mouvement. La technique utilisée est la **soustraction de la médiane** : on calcule l'image médiane de toute la vidéo (le « fond »), puis on soustrait cette image de fond à chaque image de la vidéo pour ne garder que les objets en mouvement.

## Objectifs

1. Charger une vidéo image par image avec OpenCV (`cv2.VideoCapture`).
2. Réduire la résolution des images (`cv2.pyrDown`) pour accélérer les traitements.
3. Calculer l'image médiane de la vidéo (`np.median` sur l'axe des images).
4. Soustraire le fond à chaque image pour obtenir une vidéo des différences.
5. Sauvegarder le résultat dans un nouveau fichier vidéo.

## Étapes guidées

### 1. Chargement et décimation de la vidéo

Utilisez `cv2.VideoCapture` pour lire la vidéo image par image. La fonction `load_video` / `decim_video` fournie permet de :
- lire chaque frame,
- convertir éventuellement en niveaux de gris (`cv2.COLOR_BGR2GRAY`),
- réduire la taille de moitié avec `cv2.pyrDown` (paramètre `decim`).

### 2. Calcul du fond (image médiane)

Calculez la médiane de toutes les images de la vidéo sur l'axe 0 :

```python
median_image = np.median(video, axis=0)
```

Affichez cette image de fond avec `implot` (pensez à convertir en RGB pour Matplotlib).

### 3. Soustraction du fond

Pour chaque image, calculez la valeur absolue de la différence avec l'image médiane :

```python
new_video = np.absolute(np.asarray(video, dtype=np.int32) - median_image.astype(np.int32)).astype(np.uint8)
```

> Attention au type des données : faites le calcul en `int32` avant de revenir en `uint8` pour éviter les dépassements.

### 4. Sauvegarde du résultat

Écrivez la vidéo des différences dans un fichier `.avi` avec `write_video`.

---

## Fichiers associés

- Notebook Jupyter : [TD5-AnalyseVideo.ipynb](TD5-AnalyseVideo.ipynb)

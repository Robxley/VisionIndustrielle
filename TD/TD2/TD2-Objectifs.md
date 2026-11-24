# TD 2 : Les objectifs des caméras

> Correction des questions du cours sur les objectifs des caméras.

---

## Problème 1 : Il est loin mon sapin ?

- Mon sapin mesure **18 m** de hauteur.
- Le sapin a une hauteur de **90 pixels** dans l'image.
- La focale **F** est de **8 mm**.
- La taille d'un pixel du capteur est de **5,5 µm** (0,0055 mm).

**Question a** : Calculer la précision (la résolution spatiale) d'un pixel.

**Question b** : Calculer le grandissement γ.

**Question c** : Calculer la distance du sapin par rapport à la caméra.

---

## Problème 2 : Boîte avec QR Code

- Une boîte de dimension **40 cm × 30 cm** est scannée sur sa largeur de **30 cm**.
- Il faut au moins **750 pixels** pour respecter la précision nécessaire à la lecture du QR Code.
- La hauteur maximale disponible au-dessus du carton est de **120 cm**.
- La documentation du capteur renseigne que la taille d'un pixel est de **3,40 µm** (0,0034 mm).

**Question a** : Calculer la taille image (A'B') de la boîte projetée sur le capteur.

**Question b** : Calculer le grandissement γ.

**Question c** : Calculer la focale f' nécessaire pour disposer la caméra à moins de 120 cm.

**Question d** : Choisissez la meilleure focale dans la liste suivante : **8, 12, 16, 25, 35, 50 mm** (focales classiquement proposées chez les constructeurs).

---

## Formules utiles

- **Grandissement** : γ = A'B' / AB = (taille image capteur) / (taille objet)
- **Formule de conjugaison de Descartes** : 1/OA' − 1/OA = 1/f'
- **Distance de travail** : OA = f × (1/γ + 1)

## Fichiers associés

- Notebook Jupyter : [TD2-Objectifs.ipynb](TD2-Objectifs.ipynb)
- Script Python : [TD2-Objectifs.py](TD2-Objectifs.py)

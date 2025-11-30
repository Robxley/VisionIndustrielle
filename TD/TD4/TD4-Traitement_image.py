# %% [markdown]
# TD-3 : Application au contrôle qualité d'une gourde décorée
#
# Vous devez proposer un système de vision permettant d’inspecter une gourde décorée en rotation à l’aide d’une caméra linéaire.
# La cadence de production est de 5 gourdes en 3 secondes.
# La gourde fait 25 cm et a un diamètre maximal de φ = 45 mm.
# Le plus petit élément à détecter est de 0,15 mm.

# %%
# variables en mm et en sec
cadence_nb = 5
cadence_sec = 3
dim_gourde_mm = 250
diameter_mm = 45
dim_min_element_mm = 0.15

# %% [markdown]
# Question 1 : Quel est le périmètre maximal de la gourde ?

# %%
import math
perimeter_mm = diameter_mm * math.pi
print("Périmètre max (mm):", perimeter_mm)

# %% [markdown]
# Question 2 : Quelle est la vitesse de déplacement d’un élément du motif de la gourde ?

# %%
temps_de_scan = cadence_sec / cadence_nb
print("Le temps de scan pour une gourde est de (sec):", temps_de_scan)
vitesse_mms = perimeter_mm / temps_de_scan
print("La vitesse de déplacement des éléments de surface est de (mm/s):", vitesse_mms)
coef_mms_en_kmh = 0.0036
print("La vitesse de déplacement des éléments de surface est de (km/h):", vitesse_mms * coef_mms_en_kmh)

# %% [markdown]
# Question 3 : Nombre de pixels

# %%
coef_sec = 2
nb_pixels = dim_gourde_mm / dim_min_element_mm
nb_pixels *= coef_sec
print("Le capteur doit avoir au moins", math.ceil(nb_pixels), "pixels")

# %% [markdown]
# Question 4 : Nombre minimal de lignes pour le scan

# %%
nb_de_lignes = perimeter_mm / dim_min_element_mm
nb_de_lignes *= coef_sec
print("Nombre de lignes :", math.ceil(nb_de_lignes))

# %% [markdown]
# Question 5 : Calculer la fréquence minimale d’acquisition pour la caméra (images/s).

# %%
temps_pour_1_ligne = temps_de_scan / nb_de_lignes
print("Le temps pour scanner une ligne doit être de (sec):", temps_pour_1_ligne)
fps = math.ceil(1 / temps_pour_1_ligne)
print("Fréquence nécessaire (fps):", fps)

# %% [markdown]
# Question 6 : Temps d’exposition max

# %%
temps_de_transfert = 15e-5
temps_expo_max = temps_pour_1_ligne - temps_de_transfert
print("Temps d'exposition maximal :", temps_expo_max)

# %% [markdown]
# Question 7 : Trouver une caméra répondant au besoin.

# %%
# Le capteur doit avoir au moins 3334 pixels (résultat de la question 3).
# Exemple : la caméra Basler Racer 4k répond au besoin.

# %% [markdown]
# Question 8 : Calculer le grandissement pour le capteur sélectionné

# %%
dim_pixel_mm = 7 / 1000
print("Taille des pixels (mm):", dim_pixel_mm)

capteur_pixels = 4000
grandissement = (dim_pixel_mm * capteur_pixels) / dim_gourde_mm
print("Grandissement pour {} pixels : {}".format(capteur_pixels, grandissement))

# %% [markdown]
# Question 9 : Calculer la distance de travail pour des focales de 6 mm, 8 mm et 12 mm.

# %%
def distance_de_travail(focale, grandissement):
    return focale * (1 / grandissement + 1)

def print_distance_de_travail(focale, grandissement):
    dist = distance_de_travail(focale, grandissement)
    print("Focale {} mm : distance de travail (mm) = {}".format(focale, dist))

for focale in [6, 8, 12]:
    print_distance_de_travail(focale, grandissement)

# %% [markdown]
# Question 10 : Test avec un temps d’exposition Ti = 3·10⁻⁴.
# La valeur max de l’image est 45.
# De combien augmenter Ti pour exploiter la dynamique 8 bits ?

# %%
ti = 1.5e-4
ti_valeur = 45
max_8bit = 255

ti_max_dynamique = ti * max_8bit / ti_valeur
print("Temps d'exposition pour utiliser toute la dynamique :", ti_max_dynamique)
print("Temps d'exposition maximal permis :", temps_expo_max)

# %% [markdown]
# Question 11 : Est-il possible d’exploiter complètement la dynamique du capteur tout en respectant la cadence ?

# %%
if ti_max_dynamique > temps_expo_max:
    print("Impossible de respecter la cadence en utilisant toute la dynamique.")
    print("Solution : augmenter le gain.")
else:
    print("Cadence respectée.")

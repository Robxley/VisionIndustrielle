# %% [markdown]
# ### TD-3 : Application au contrôle qualité d'une gourde décorée  
# 
# Vous devez proposer un système de vision permettant d’inspecter une gourde décorée en rotation à l’aide d’une caméra linéaire. La cadence de production est de 5 gourdes en 3 secondes. La gourde fait 25 cm et a un diamètre maximal de φ = 45mm. Le plus petit élément à détecter est de 0.15mm.

# %%
# variable en mm et en sec
cadence_nb = 5              # nombre de gourdes (scannées sur 3 secondes)
cadence_sec = 3             # 3 secondes
dim_gourde_mm = 250         # hauteur de la gourde (25 cm)
diameter_mm = 45            # diamètre de la gourde
dim_min_element_mm = 0.15   # dimension du plus petit élément à inspecter sur la gourde

# %% [markdown]
# **Question 1** : Quel est le périmètre maximal de la gourde

# %%
import math
perimeter_mm = diameter_mm * math.pi        # le périmètre = 2 * rayon * pi = diametre * pi
print("Périmètre max (mm):", perimeter_mm)

# %% [markdown]
# **Question 2** : Quelle est la vitesse de déplacement d’un élément du motif de la gourde ?

# %%
# vitesse = distance / temps
temps_de_scan =  cadence_sec / cadence_nb                                   # temps de scan d'une bouteille
print("Le temps de scan pour une gourde est de (sec):", temps_de_scan)
vitesse_mms = perimeter_mm / temps_de_scan
print("La vitesse de déplacement des éléments de surface est de (mm/s):", vitesse_mms)
coef_mms_en_kmh = 0.0036
print("La vitesse de déplacement des éléments de surface est de (km/h):", vitesse_mms * coef_mms_en_kmh)

# %% [markdown]
# **Question 3** : Nombre de pixels

# %%
coef_sec = 2
nb_pixels = dim_gourde_mm / dim_min_element_mm      # calcul du nombre de pixels nécessaires pour scanner la bouteille en fonction du plus petit élément
nb_pixels *= coef_sec                               # on multiplie ce nombre de pixels par le facteur de sécurité
print("Le capteur doit avoir au moins", math.ceil(nb_pixels), "pixels")

# %% [markdown]
# **Question 4** : Nombre minimal de lignes pour le scan

# %%
nb_de_lignes = perimeter_mm / dim_min_element_mm    # calcul du nombre de lignes nécessaires pour scanner la bouteille en fonction du plus petit élément
nb_de_lignes *= coef_sec                            # on multiplie ce nombre de pixels par le facteur de sécurité
print("Nombre de lignes :", math.ceil(nb_de_lignes))

# %% [markdown]
# **Question 5** : Calculer la fréquence F minimale d’acquisition pour la caméra (ou nombre d'images par second).

# %%
temps_pour_1_ligne =  temps_de_scan / nb_de_lignes
print("Le temps pour scanner une ligne doit être de (en sec):", temps_pour_1_ligne)
fps = math.ceil(1/temps_pour_1_ligne)       # frame per second : calcul du nombre d'images qu'il est possible de prendre en 1 sec.
print("Le nombre d'image par seconde (ou fréquence) nécessaire pour maintenir la cadence est de :", fps)

# %% [markdown]
# **Question 6** : Temps d'exposition max ?

# %%
temps_de_transfert = 15e-5
temps_expo_max = temps_pour_1_ligne - temps_de_transfert
print("Temps d'expo max",  temps_expo_max)

# %% [markdown]
# **Question 7** : Trouver une caméra répondant au besoin. (Quelques noms de distributeurs : Basler, Thorlabs, ids-imaging, Keyence, etc.)

# %%
# Pour rappel le capteur doit avoir au moins 3334 pixels (réponse question 3)
# la caméra https://www.baslerweb.fr/fr/cameras-lineaires/24-529-basler-racer.html en 4k répond au besoin.

# %% [markdown]
# **Question 8** : Calculer le grandissement pour le capteur sélectionné

# %%
# pour rappel le nombre minimal de pixels calculé était de 3334 pixels, mais rien ne nous empèche de prendre plus si le capteur le permet.

dim_pixel_mm =  7 / 1000    # par exemple pour une caméra 4k dont la taille des pixels est de 7µm -> en millimètre 7 / 1000
print("Taille des pixels (mm): ", dim_pixel_mm)

capteur_pixels = 4000   # en 4k le capteur à 4096 pixels. On peut prend 4000 pour se laisser une marge d'erreur (en cas de vibrations, positionnement de la caméra etc...).
grandissement =  (dim_pixel_mm*capteur_pixels) / dim_gourde_mm
print("Le grandissement pour {} pixels est de : {}".format(capteur_pixels, grandissement))

# %% [markdown]
# **Question 9** : Calculer la distance de travail de la caméra pour les focales 6mm, 8mm et 12mm
# 
# 

# %%
#OA = f * (1/grandissement + 1)
def distance_de_travail(focale, grandissement):
    return focale * (1/grandissement + 1)

def print_distance_de_travail(focale, grandissement):
    dist = distance_de_travail(focale, grandissement)
    print("Pour la focale {}, la distance de travail est de (mm) : {}".format(focale, dist))

for focale in [6, 8, 12]:
    print_distance_de_travail(focale, grandissement)

# %% [markdown]
# **Question 10** : Vous faite un premier test avec un temps d’exposition de valeur Ti = 3.10-4. La valeur maximale de l’image est alors de 45. En supposant que la réponse de la caméra est linéaire de combien vous devait augmenter le temps d’exposition pour exploiter la dynamique complète du capteur 8bits.

# %%
ti = 1.5e-4    
ti_valeur = 45
max_8bit = 255

ti_max_dynamique = ti * max_8bit / ti_valeur
print("Pour exploiter complètement la dynamique le temps d'exposition doit être de : ", ti_max_dynamique)
print("Temps d'exposition max :", temps_expo_max)


# %% [markdown]
# **Question 11** : Est-ce  qu’il  est  possible  d’exploiter  complétement  la  dynamique  du  capteur  tout  en 
# respectant les cadences de production ? Si non, proposer une solution.

# %%
if ti_max_dynamique > temps_expo_max:
    print("Le temps d'exposition pour exploiter la dynamique du capteur ne respecte pas les conditions de cadence : 😭")
    print("L'utilisation d'un gain > 1 peut permettre d'atteindre")
else:
    print("Ok cadence respectée : 😁")



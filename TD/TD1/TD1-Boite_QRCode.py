# %% [markdown]
# # TD 1 : Caméra linéaire pour la détection de QR Codes sur des boîtes.
# 
# Énoncé du TD : [TD1-Boite_QRCODE.pdf](TD1-Boite_QRCODE.pdf)
# 
# Résumé :  
# Un industriel fait appel à vos talents en vision industrielle pour moderniser son entreprise. Il vous invite à venir visiter sa chaîne de production. Il vous présente un poste de travail où des boîtes en carton équipées de QR code sont scannées manuellement par un opérateur. L'industriel vous demande s'il est possible d'utiliser une caméra linéaire sur le tapis roulant convoyant les cartons pour automatiser le scan des QR Codes. 
# 
# Après discussion avec l'ingénieur de production, voici les informations obtenues pour identifier les éléments nécessaires à l'identification d'une caméra linéaire répondant au besoin :
# (Les informations obtenues sur le système sont les réponses de la question B de [TD1-Boite_QRCODE.pdf](TD1-Boite_QRCODE.pdf))
# 
# 1. Informations sur les boîtes à scanner :
#     - boîte de dimensions : 40x30 cm².
#     - les boîtes avancent sur le tapis roulant suivant la longueur de 40 cm.
#     - la distance entre deux boîtes sur le tapis est de 5 cm.
# 2. Informations sur le QR CODE :
#     - le QR CODE V2 a une dimension de 2x2 cm².  
#     - la grille d'encodage du QR CODE est de 25x25 éléments.  
# 3. Informations de production :
#     - la cadence de production est de 35 boîtes pour une minute.
#     - La caméra linéaire scanne ligne par ligne la boîte dans sa largeur de 30 cm.
#     - la boîte se déplace dans le sens de sa longueur (40 cm) sous la caméra.
# 

# %%
#Informations sur les boîtes :
dim1_box_cm = 40        # longueur 40 cm
dim2_box_cm = 30        # largeur 30 cm
box_gap_cm = 5          # distance entre les boîtes 5 cm

#Informations sur le QR code
dim_qr_code_cm = 2      # taille du QR code 4x4 cm²
qr_code_grid = 25       # grille 25x25

#Cadence
cadence_box = 35        # unité
cadence_sec = 60        # en secondes


# %% [markdown]
# **Question 1** : Calculer la taille du plus petit élément à observer.
# 

# %%
min_size_to_detect  = dim_qr_code_cm / qr_code_grid 
print("Taille du plus petit objet (cm):", min_size_to_detect)

# %% [markdown]
# **Question 2** : Calculer la vitesse nécessaire (en cm/s puis km/h) de défilement des boîtes pour respecter la cadence.

# %%
box_speed = (dim1_box_cm + box_gap_cm) * cadence_box / cadence_sec     
print("Vitesse de la boîte (cm/s)", box_speed)

# Facteur de conversion cm/s en km/h 
cms_to_kmh_factor = 3600/100000     # 3600 secondes dans 1 heure, 100000 cm dans 1 km (attention de ne pas se tromper, calcul parfois compliqué !😉)
print("Facteur de conversion cm/s vers km/h : ", cms_to_kmh_factor)
print("Vitesse de la boîte (km/h)", box_speed * cms_to_kmh_factor)


# %% [markdown]
# **Question 3** : Quel est le nombre minimal de pixels N que doit contenir le capteur linéaire quand le coefficient C de sécurité est fixé à 2 (pour respecter le théorème de Shannon) ?
# 

# %%
coef_C = 2 # coefficient C de sécurité

# Première façon de voir les choses en suivant la formule du cours sur la précision :
precision = min_size_to_detect / coef_C     # on calcule la précision souhaitée => la plus petite distance divisée par le coefficient de sécurité.
pixels = int(dim2_box_cm / precision)       # nombre de pixels (résolution du capteur) = dimension de l'objet à inspecter divisée par la précision
print("Nombre de pixels pour le capteur (v1): ", pixels)

# Deuxième façon de voir les choses (et donnant le même résultat) :           
pixels_v2 = int(dim2_box_cm / min_size_to_detect)  # le nombre de pixels = dimension de l'objet à inspecter divisée par la dimension du plus petit objet à observer
pixels_v2 = pixels_v2 * coef_C                     # on multiplie ce nombre de pixels par le coefficient de sécurité.
print("Nombre de pixels pour le capteur (v2): ", pixels_v2)

# %% [markdown]
# **Question 4** : Combien de lignes (ou images) sont nécessaires pour scanner une boite.

# %%
# calcul similaire à la question 3 sur la longueur de la boîte.
line_scan_count = (dim1_box_cm / min_size_to_detect)  # largeur divisée par le plus petit élément
line_scan_count = int(line_scan_count * coef_C)  # on multiplie ce nombre par le facteur de sécurité
print("Nombre de lignes nécessaires au scan d'une boîte (en tenant compte du facteur de sécurité) :", line_scan_count)


# %% [markdown]
# **Question 5** : Combien de temps faut-il pour scanner une boite complète ?

# %%
# formule: vitesse = distance / temps -> temps = distance / vitesse
time_to_scan_one_box = dim1_box_cm / box_speed
print("Temps pour scanner une boîte (sec) :", time_to_scan_one_box)


# %% [markdown]
# **Question 6** : Quelle est la fréquence F d’acquisition des images lignes (le FPS – Frames per second) ?
# 

# %%
from math import ceil
fps = line_scan_count / time_to_scan_one_box
print("Images par seconde :", fps)   
print("Images par seconde (valeur arrondie au supérieur) :", ceil(fps))   # fonction ceil pour arrondir la valeur au supérieur


# %% [markdown]
# **Question 7** : Sachant que le transfert de l’image d’une ligne vers le système de calcul prend 0,0005 s, quel est le temps maximal d’intégration possible pour la caméra ?
# 

# %%
time_to_scan_one_line = time_to_scan_one_box / line_scan_count # ou 1 / fps
print("Le temps pour scanner une ligne (sec) :", time_to_scan_one_line, "(ou 1/fps :", 1/fps,")")
image_transfert_time_sec = 0.0005               
max_integration_time = time_to_scan_one_line - image_transfert_time_sec
print("Le temps d'intégration ne doit pas dépasser (seconde) :", max_integration_time)
print("Le temps d'intégration ne doit pas dépasser (millisecondes) :", max_integration_time * 1000)


# %% [markdown]
# **Question 8** : Une fois la boîte entièrement scannée, le traitement d’image pour détecter et lire le QR Code prend 0.20 s. Vérifiez si ce temps de calcul est suffisant pour suivre la cadence de production.

# %%
 # Le calcul doit être plus rapide que le temps écoulé entre deux boîtes
time_between_box = box_gap_cm / box_speed          
print("Temps écoulé entre deux boîtes :", time_between_box)
if time_between_box > 0.20:
    print("Le temps écoulé entre deux boîtes est plus long que le temps de calcul. Tout est OK ! 😊👍")
else:
    print("Le temps écoulé entre deux boîtes est trop court pour faire le calcul - 😒❌")

# %% [markdown]
# 
# **Question 9** : Proposer des solutions. Réviser les calculs si nécessaire en fonction des solutions proposées.
# 

# %% [markdown]
# Solutions envisageables :
# 1. On peut tourner les boîtes de 90° pour gagner du temps en ne scannant dans le temps que 30 cm au lieu de 40 cm.
# Il faudra néanmoins un capteur linéaire avec plus de pixels pour l'acquisition d'une ligne de 40 cm.
# Pour vérifier facilement les résultats dans cette configuration, inverser les valeurs des variables ```dim1_box_cm``` et ```dim2_box_cm``` dans la première cellule de code.  
# 
# ```dim1_box_cm = 30```        
# ```dim2_box_cm = 40```  
# 
# Puis, ré-executer l'ensemble des cellules de codes en cliquant sur ```>> Exécuter Tout``` (en haut de votre Notebook).
# Vous devez obtenir à la question 8:  
# 
# ```Le temps écoulé entre deux boites est plus long que le temps de calcul. Tout est OK ! 😊👍```
# 
# 
# 2. On peut poser le QR Code toujours au même endroit sur la boîte.  
# Le temps restant pour le calcul est alors le temps écoulé entre 2 QR Code.  
# Soit le temps pour parcourir la distance suivante :  
# 
# ```l'espace entre 2 boites (5cm) + la longueur d'une boite (40cm) - la taille du QR Code (2cm)```.
# 
# 3. Utiliser une caméra matricielle qui se déclenche (à l'aide d'un capteur/trigger) lorsque la caméra est positionnée au milieu de la boîte.
# Soit le temps pour parcourir la distance suivante :  
# 
# ```l'espace entre 2 boites (5cm) + la longueur d'une boite (40cm)```.
# 
# Un schéma peut aider à visualiser ces différentes solutions.
# 
# 
# 
# 
# 



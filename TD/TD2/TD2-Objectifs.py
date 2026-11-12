# %% [markdown]
# ## TD2 - Les objectifs des caméras 
# ***(correction des questions du cours sur les objectifs des caméras)***
# 
# 
# ### Problème 1 : Il est loin mon sapin ?
# 
# Mon sapin mesure 18m de hauteur.  
# Le sapin a une hauteur de 90 pixels dans l'image.  
# La focale F est de 8mm.  
# La taille d’un pixel du capteur est de  5,5µm (0.0055mm).  

# %%
sapin_mm = 18000            # hauteur du sapin en mm
image_sapin_px = 90         # hauteur du sapin en pixel
focale_mm = 25              # focale de l'objectif en mm
dim_pixel_mm = 0.0055       # dimension d'un pixel en mm

# %% [markdown]
# **Question a** : Calculer la précision (la résolution spatiale) d’un pixel.

# %%
precision = sapin_mm / image_sapin_px
print("La résolution spatiale de l'image (ou précision) est (mm/pixel):", precision)
print("La résolution spatiale de l'image (ou précision) est (m/pixel):", precision /1000)

# %% [markdown]
# **Question b** : Calculer le grandissement 𝛾.

# %%
grandissement = (image_sapin_px * dim_pixel_mm) / sapin_mm  # G = A'B' / AB
print("Le grandissement est de : ", grandissement)

# %% [markdown]
# **Question c** : Calculer la distance du sapin par rapport à la caméra.

# %%
distance_OA = focale_mm * ( (1/grandissement) + 1)
print("Le sapin est situé à en (mm): ", distance_OA)
print("Le sapin est situé à en (m): ", distance_OA / 1000)

# %% [markdown]
# ### Problème 2 : Boîte avec QR CODE
# 
# Une boite de dimension 40cm x 30cm est scannée sur sa largeur de 30cm. 
# Il faut au moins 750 pixels pour respecter la précision nécessaire à la lecture du QRCode.  
# La hauteur maximale disponible au dessus du carton est de 120cm.  
# La documentation du capteur renseigne que la taille d'un pixel est de 3,40µm (0.0034mm).  
# 
# a. Calculer la taille image (A’B’) de la boîte projetée sur le capteur  
# b. Calculer le grandissement 𝛾  
# c. Calculer la focale f’ nécessaire pour disposer la caméra à moins de 60cm.  
# 

# %%
dim_boite_mm = 300
pixels = 750
hauteur_max_mm = 1200
dim_pixel_mm = 0.0034

# %% [markdown]
# **Question a** : Calculer la taille de l'image de la boîte projetée sur le capteur.

# %%
dim_image_mm = pixels * dim_pixel_mm
print("L'image projetée sur le capteur fait (mm):", dim_image_mm)

# %% [markdown]
# **Question b** : Calculer le grandissement 𝛾
# 

# %%
grandissement = dim_image_mm / dim_boite_mm
print("Le grandissement vaut :", grandissement)

# %% [markdown]
# **Question c** : Calculer la focale f’ nécessaire pour disposer la caméra à moins de 120cm.

# %%
inv_grandissement = 1 / grandissement
focale = 1200 / ( inv_grandissement + 1)
print("La focale maximale ne doit pas dépasser (mm):", focale)

# %% [markdown]
# **Question d** : Choisissez la meilleure focale dans la liste suivante : 8, 12, 16, 25, 35, 50 (focales classiquement proposées chez les constructeurs).

# %%
focale = 8
position_camera_mm = (inv_grandissement + 1) * focale
print("Pour une focale de {}mm, il faut positionner la caméra à {:.2f}mm de hauteur".format(focale, position_camera_mm))
print("Pour une focale de {}mm, il faut positionner la caméra à {:.2f}cm de hauteur".format(focale, position_camera_mm/10))



import os

# Chemin complet du fichier
chemin_du_fichier = "/C:/Users/yokos/Terre01.py"

# Récupérer le nom du fichier à partir du chemin complet
nom_du_fichier = os.path.basename(chemin_du_fichier)

# Afficher le nom du fichier
print("Nom du fichier :", nom_du_fichier)

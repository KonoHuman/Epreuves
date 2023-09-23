# Ouvrir le fichier contenant le plateau en mode lecture
with open('board.txt', 'r') as plateau_file:
    plateau = plateau_file.readlines()

# Ouvrir le fichier contenant le modèle à rechercher (to_find.txt)
with open('to.find.txt', 'r') as modele_file:
    modele_a_rechercher = modele_file.readlines()

# Supprimer les espaces inutiles et les caractères de nouvelle ligne
modele_a_rechercher = [ligne.strip() for ligne in modele_a_rechercher]

# Parcourir le plateau pour trouver le modèle
for row_index, row in enumerate(plateau):
    for col_index, caractere in enumerate(row):
        if caractere == modele_a_rechercher[0][0]:
            # Si le premier caractère correspond, vérifiez le modèle complet
            correspondance = True
            for i in range(len(modele_a_rechercher)):
                for j in range(len(modele_a_rechercher[i])):
                    if (
                        row_index + i >= len(plateau) or
                        col_index + j >= len(plateau[0]) or
                        plateau[row_index + i][col_index + j] != modele_a_rechercher[i][j]
                    ):
                        correspondance = False
                        break
                if not correspondance:
                    break
            if correspondance:
                print("Trouvé !")
                print(f"Coordonnées : {row_index},{col_index}")
                for line in modele_a_rechercher:
                    print(line)
                break

if not correspondance:
    print("Introuvable")

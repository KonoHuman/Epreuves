

try:
    nom_fichier = input("Entrez le nom du fichier à afficher : ")

    with open(nom_fichier, 'r') as fichier:
        contenu = fichier.read()
        print("Contenu du fichier {} :".format(nom_fichier))
        print(contenu)
except FileNotFoundError:
    print("Le fichier {} n'a pas été trouvé.".format(nom_fichier))
except Exception as e:
    print("Une erreur s'est produite :", str(e))

def indice():
    # Exemple de tableau contenant des mots
    phrase = input("Veuillez entrer une suite de mots : ")
    
    tableau = phrase.split()

    # Obtenez l'élément recherché (dernier élément)
    mot_a_rechercher = tableau[-1]

    # Parcourez le tableau pour trouver le premier index de l'élément recherché
    indice_trouve = None
    for index, mot in enumerate(tableau):
        if mot == mot_a_rechercher:
            indice_trouve = index
            break  # Sortez de la boucle dès que vous trouvez le premier indice

    # Vérifiez si l'élément a été trouvé
    if indice_trouve is not None:
        print(f"Le premier indice de '{mot_a_rechercher}' est : {indice_trouve}")
    else:
        print("-1")  # Affiche -1 si l'élément n'est pas trouvé

indice()

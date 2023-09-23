def fusion():
    try:
        premier_chiffre = int(input('Veuillez entrer un premier nombre : '))
        second_chiffre = int(input('Veuillez entrer un second nombre : '))
        troisième_chiffre = int(input('Veuillez entrer un troisième nombre : '))
        quatrième_chiffre = int(input('Veuillez entrer un quatrième nombre : '))
        cinquième_chiffre = int(input('Veuillez entrer un cinquième nombre : '))
        sixieme_chiffre = int(input('Veuillez entrer un sixième chiffre : '))

        nombres1 = [premier_chiffre, second_chiffre, troisième_chiffre]
        nombres2 = [quatrième_chiffre, cinquième_chiffre, sixieme_chiffre]

        nombres1.sort()  # Tri en ordre croissant
        nombres2.sort()  # Tri en ordre croissant

        resultat = " ".join(map(str, nombres1)) + " fusion " + " ".join(map(str, nombres2))

        print(resultat)

        question = input("Voulez-vous fusionner les deux listes ? ").lower()

        if question == "oui":
            new_list = nombres1 + nombres2
            new_list.sort()  # Tri de la liste en ordre croissant
            print(new_list)
        elif question == "non":
            print("Très bien, Au revoir")
        else:
            print("Veuillez répondre avec 'oui' ou 'non'.")

    except ValueError:
        print("Veuillez n'insérer que des chiffres.")

fusion()

def inside():
    phrase = input("Veuillez entrer une suite de caractères : ")
    bout_de_phrase = input("Veuillez entrer une seconde suite de caractères : ")

    # Vérifie si bout_de_phrase contient des chiffres
    if any(char.isdigit() for char in bout_de_phrase):
        raise ValueError("La sous-chaîne ne doit pas contenir de chiffres.")

    if bout_de_phrase in phrase:
        print("La sous-chaîne est présente dans le texte.")
    else:
        print("La sous-chaine n'est pas présente dans le texte.")

    print('Programme terminé')

inside()
6
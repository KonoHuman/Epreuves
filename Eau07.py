def maj():
    
    phrase = input("Veuillez entrer une suite de characteres : ")
    
    if any(char.isdigit() for char in phrase):
        raise ValueError("La sous-chaîne ne doit pas contenir de chiffres.")

    liste_de_caracteres = list(phrase)

    for i in range(0, len(liste_de_caracteres), 2):
        # Modifiez les caractères à des indices pairs, par exemple, en les mettant en majuscules.
        liste_de_caracteres[i] = liste_de_caracteres[i].upper()

    # Reconvertir la liste de caractères en une chaîne.
    resultat = ''.join(liste_de_caracteres)

    print(resultat)  # Cela affichera "AbCdEfG"

maj()
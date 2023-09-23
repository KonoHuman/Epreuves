def firstmaj():
    phrase = input("Veuillez entrer une suite de caractères : ")

    if any(char.isdigit() for char in phrase):
        raise ValueError("La sous-chaîne ne doit pas contenir de chiffres.")

    liste_de_mots = phrase.split()

    for i in range(len(liste_de_mots)):
        mot = liste_de_mots[i]
        if len(mot) > 0:
            liste_de_mots[i] = mot[0].upper() + mot[1:]

    # Rejoindre les mots modifiés en une seule chaîne.
    resultat = ' '.join(liste_de_mots)

    print(resultat)

firstmaj()

def solution():
    suite_de_char = input('Veuillez entrer une suite de caractères : ')
    nombre_de_char = len(suite_de_char)
    liste_de_doublon = []

    if nombre_de_char % 2 == 0:
        for char in range(0, nombre_de_char - 1, 2):
            caractere_actuel = suite_de_char[char]
            caractere_suivant = suite_de_char[char + 1]
            doublon = caractere_actuel + caractere_suivant
            liste_de_doublon.append(doublon)
    elif nombre_de_char % 2 != 0:
        for char in range(0, nombre_de_char - 1, 2):
            caractere_actuel = suite_de_char[char]
            caractere_suivant = suite_de_char[char + 1]
            doublon = caractere_actuel + caractere_suivant
            liste_de_doublon.append(doublon)
        trait_du_8 = "_"
        dernier_caractere = suite_de_char[-1]
        liste_de_doublon.append(dernier_caractere + trait_du_8)

    print(liste_de_doublon)

solution()

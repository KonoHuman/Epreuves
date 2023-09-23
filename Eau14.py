def tri_selection():
    try:
        premier_chiffre = int(input('Veuillez entrer un nombre : '))
        second_chiffre = int(input('Veuillez entrer un second nombre : '))
        troisième_chiffre = int(input('Veuillez entrer un troisième nombre : '))
        quatrième_chiffre = int(input('Veuillez entrer un quatrième nombre : '))
        cinquième_chiffre = int(input('Veuillez entrer un cinquième nombre : '))

        nombres = [premier_chiffre, second_chiffre, troisième_chiffre, quatrième_chiffre, cinquième_chiffre]

        for i in range(len(nombres)):
            min_index = i
            for j in range(i + 1, len(nombres)):  # Commencer à i + 1
                if nombres[j] < nombres[min_index]:
                    min_index = j

            # Échanger l'élément minimum avec l'élément actuel
            nombres[i], nombres[min_index] = nombres[min_index], nombres[i]

        print(nombres)

    except ValueError:
        print("Erreur : Veuillez n'entrer que des chiffres")

tri_selection()

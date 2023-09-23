def triabulle():
    try:
        premier_chiffre = int(input('Veuillez entrer un nombre : '))
        second_chiffre = int(input('Veuillez entrer un second nombre : '))
        troisième_chiffre = int(input('Veuillez entrer un troisième nombre : '))
        quatrième_chiffre = int(input('Veuillez entrer un quatrième nombre : '))
        cinquième_chiffre = int(input('Veuillez entrer un cinquième nombre : '))

        nombres = [premier_chiffre, second_chiffre, troisième_chiffre, quatrième_chiffre, cinquième_chiffre]

        for i in range(len(nombres)):
            for j in range(len(nombres) - 1):
                if nombres[j] > nombres[j + 1]:
                    nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]

        print(nombres)

    except ValueError:
        print("Erreur : Veuillez n'entrer que des chiffres")

triabulle()

def addition_ou_soustraction():
    try:
        premier_chiffre = int(input('Veuillez entrer un premier nombre : '))
        second_chiffre = int(input('Veuillez entrer un second nombre : '))
        troisième_chiffre = int(input('Veuillez entrer un troisième nombre : '))
        quatrième_chiffre = int(input('Veuillez entrer un quatrième nombre : '))
        cinquième_chiffre = int(input('Veuillez entrer un cinquième nombre : '))

        nombres = [premier_chiffre, second_chiffre, troisième_chiffre, quatrième_chiffre, cinquième_chiffre]
        
        print(nombres)
        
        calculateur = nombres[-1]
        
        print("Votre nombre calculateur est : " + str(calculateur))
         
        
        addition_ou_soustraction = str(input('Voulez-vous effectuer une addition ou soustraction ? '))
        
        option_invalide = True  # Variable pour suivre si l'option est invalide
        
        for chiffre in nombres:
            if "addition".lower() in addition_ou_soustraction:
                tous_additionnée = chiffre + nombres[-1]
                print(tous_additionnée)
                option_invalide = False  # L'option est valide, pas besoin de message d'erreur
            elif "soustraction".lower() in addition_ou_soustraction:
                tous_soustrait = chiffre - nombres[-1]
                print(tous_soustrait)
                option_invalide = False  # L'option est valide, pas besoin de message d'erreur
        
        if option_invalide:
            print("Veuillez répondre à la question")

    except ValueError:
        print("Veuillez n'insérer que des chiffres")

addition_ou_soustraction()

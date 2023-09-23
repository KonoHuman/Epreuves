def minimum():
    
    try:
        premier_chiffre = input('Veuillez entrer un nombre : ')
        premier_chiffre = int(premier_chiffre)
            
        second_chiffre = input('Veuillez entrer un second nombre : ')
        second_chiffre = int(second_chiffre)
        
        troisième_chiffre = input('Veuillez entrer un troisième nombre : ')
        troisième_chiffre = int(troisième_chiffre)
        
        quatrième_chiffre = input('Veuillez entrer un quatrième nombre : ')
        quatrième_chiffre = int(quatrième_chiffre)
        
        cinquieme_chiffre = input('Veuillez entrer un cinquième nombre : ')
        cinquieme_chiffre = int(cinquieme_chiffre)
        
        # Initialisez la liste "nombres" avec les valeurs entrées
        nombres = [premier_chiffre, second_chiffre, troisième_chiffre, quatrième_chiffre, cinquieme_chiffre]
        
        nombres_tries = sorted(nombres)  # Triez la liste de nombres

        differences = [nombres_tries[i + 1] - nombres_tries[i] for i in range(len(nombres_tries) - 1)]

        difference_minimale = min(differences)  # Trouvez la différence minimale

        print("La différence minimale entre les nombres est :", difference_minimale)
        
    except ValueError:
        print("Erreur : Veuillez n'entrer que des chiffres")
    
minimum()

def ajout_et_trie():
    
    try:
        premier_chiffre = int(input('Veuillez entrer un premier nombre : '))
        second_chiffre = int(input('Veuillez entrer un second nombre : '))
        troisième_chiffre = int(input('Veuillez entrer un troisième nombre : '))
        quatrième_chiffre = int(input('Veuillez entrer un quatrième nombre : '))
        cinquième_chiffre = int(input('Veuillez entrer un cinquième nombre : '))

        nombres = [premier_chiffre, second_chiffre, troisième_chiffre, quatrième_chiffre, cinquième_chiffre]
        
        nombres.sort()
        
        print(nombres)
        
        chiffre_a_ajouter = int(input('Veuillez rajouter un autre nombre'))
        
        nombres.append(chiffre_a_ajouter)
        
        print("Votre nombre ajouté est : " + str(chiffre_a_ajouter))
        
        nombres.sort()
        
        print(nombres)
        
        
    except ValueError:
        print("Veuillez n'insérer que des chiffres")
        
ajout_et_trie()
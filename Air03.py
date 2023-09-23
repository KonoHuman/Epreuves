def paire_manquante():
    try:
        premier_chiffre = int(input('Veuillez entrer un nombre : '))
        second_chiffre = int(input('Veuillez entrer un second nombre : '))
        troisième_chiffre = int(input('Veuillez entrer un troisième nombre : '))
        quatrième_chiffre = int(input('Veuillez entrer un quatrième nombre : '))
        cinquième_chiffre = int(input('Veuillez entrer un cinquième nombre : '))

        
        nombres = [premier_chiffre, second_chiffre, troisième_chiffre, quatrième_chiffre, cinquième_chiffre]
        
        for chiffre in nombres:
            if nombres.count(chiffre) == 1:
                print(f"Le chiffre {chiffre} n'a pas de paire.")
                return
                
        print("Tous les chiffres ont une paire.")
            
    except ValueError:
        print("Erreur, veuillez n'entrer que des chiffres")

paire_manquante()

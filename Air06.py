def pass_sanitaire():
    try:
        premier_mot = str(input('Veuillez entrer un premier mot : '))
        second_mot = str(input('Veuillez entrer un second mot : '))
        troisième_mot = str(input('Veuillez entrer un troisième mot : '))
        quatrième_mot = str(input('Veuillez entrer un quatrième mot : '))
        cinquième_mot = str(input('Veuillez entrer un cinquième mot : '))

        liste = [premier_mot, second_mot, troisième_mot, quatrième_mot, cinquième_mot]
        
        print(liste)
        
        chaine_clé = str(input('Veuillez insérer un pass ? '))
        
        # Convertir chaine_clé en minuscules
        chaine_clé = chaine_clé.lower()
        
        new_liste = []
        
        for word in liste:
            # Convertir word en minuscules pour la comparaison
            word = word.lower()
            
            if chaine_clé not in word:
                new_liste.append(word)
                
        print(new_liste)

    except ValueError:
        print("Veuillez n'insérer que des lettres")

pass_sanitaire()

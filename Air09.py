def decalage():

        premier_mot = input('Veuillez entrer un premier mot : ')
        deuxième_mot = input('Veuillez entrer un second mot : ')
        troisième_mot = input('Veuillez entrer un troisième mot : ')
        quatrième_mot = input('Veuillez entrer un quatrième mot : ')
        cinquième_mot = input('Veuillez entrer un cinquième mot : ')
        
        liste = [premier_mot, deuxième_mot, troisième_mot, quatrième_mot, cinquième_mot]
        
        print(liste)


        question = input("Voulez-vous décaller la liste ? ").lower()
        
        if question == "oui":
            
            for mot in range(1, len(liste)):
                
                liste[mot], liste[mot - 1] = liste[mot -1], liste[mot]
                print(liste)
                 
        elif question == "non":
            
            print("Très bien, Au revoir")
            
        else:
            
            print("Veuillez répondre avec 'oui' ou 'non'.")
            
decalage()
            

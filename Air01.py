def separation_fonction():
    
    phrase = input("Veuillez entrer une suite de characteres : ")
    
    bout_de_phrase = input("Veuillez entrer une suite de characteres : ")
    
    if bout_de_phrase in phrase:
        tableau = phrase.split(bout_de_phrase)
        
        print(tableau[0] + " \n" + tableau[1])
        
    else:
        print("Impossible de séparer la phrase")


    
separation_fonction()
def ascii():
    
    # Exemple de tableau contenant des mots
    phrase = input("Veuillez entrer une suite de mots : ")
    
    tableau = phrase.split()
    
    new_tableau = tableau.sort()
        
    print(tableau)
    
ascii()
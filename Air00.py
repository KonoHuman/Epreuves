def separation():
    
    phrase = input("Veuillez entrer une suite de characteres : ")
    
    tableau = phrase.split()
    
    for mot in tableau:
        print(mot + "\n")

    
separation()
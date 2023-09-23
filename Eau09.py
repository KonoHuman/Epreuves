def chiffres():
    
    suite = input('Veuillez entrer une suite de chiffres : ')
    
    if any(not char.isdigit() for char in suite):
        raise ValueError("La sous-chaîne ne doit pas contenir de lettres.")

    else:
        print ("Votre suite est legit : " + suite)
        
chiffres()
    
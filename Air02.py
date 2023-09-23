def concat():
    phrase = input("Veuillez entrer une suite de caractères : ")
    tableau = phrase.split()
    print(tableau)
    
    question = input("Voulez-vous rassembler les fragments de votre phrase ? (Oui/Non) : ")
    
    if question.lower() == "oui":
        separateur = input("Veuillez entrer le séparateur : ")
        rassemblement = separateur.join(tableau)
        print(rassemblement)
    elif question.lower() == "non":
        print("Dommage, Au revoir")
    else:
        print("Réponse invalide. Veuillez répondre avec 'Oui' ou 'Non'.")

concat()

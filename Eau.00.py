def combinaisons():

    liste_de_combinaisons = []
    for i in range(10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                if i != j and j != k and i != k:  # Vérification des chiffres différents
                    combinaison = str(i) + str(j) + str(k)
                    liste_de_combinaisons.append(combinaison)
                    
    result = ", ".join(liste_de_combinaisons)
    print(result)
    
combinaisons()
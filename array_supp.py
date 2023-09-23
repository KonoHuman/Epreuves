def array_diff(a, b):
    # Créez une nouvelle liste vide pour stocker le résultat
    result = []
    
    # Parcourez chaque élément de la liste 'a'
    for item in a:
        # Si l'élément n'est pas dans la liste 'b', ajoutez-le à 'result'
        if item not in b:
            result.append(item)
    
    return result

# Exemple 1
a = [1, 2, 2, 2, 3]
b = [2]
resultat = array_diff(a, b)
print(resultat)  # Cela devrait afficher [1, 3]

# Exemple 2
a = [1, 2]
b = [1]
resultat = array_diff(a, b)
print(resultat)  # Cela devrait afficher [2]

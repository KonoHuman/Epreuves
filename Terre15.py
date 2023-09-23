def verifier_combinaisons_uniques():
    combinaisons_repetees = []
    for nombre in range(1000):
        chiffres = str(nombre).zfill(3)
        if len(set(chiffres)) != len(chiffres):
            combinaisons_repetees.append(chiffres)
    return combinaisons_repetees

# Exemple d'utilisation
combinaisons_repetees = verifier_combinaisons_uniques()
if combinaisons_repetees:
    print("Les combinaisons suivantes apparaissent plus d'une fois :", combinaisons_repetees)
else:
    print("Aucune combinaison ne réapparaît dans la liste.")

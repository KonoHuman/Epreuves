def empiler_barres(b):
    resultat = ""
    for _ in range(b):
        resultat += "|\n"
    return resultat

b = 3  # Remplacez 3 par le nombre de barres que vous souhaitez empiler
resultat = empiler_barres(b)
print(resultat)

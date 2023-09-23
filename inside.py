def inside(suite, indice):
    
    last_char = suite[-1]
    return indice == last_char

suite = "abcdefghij"
indice = "m"
resultat = inside(suite, indice)
print(resultat)

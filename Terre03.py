def alphabet_a_partir_de(lettre):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if lettre in alphabet:
        index = alphabet.index(lettre)
        sous_alphabet = alphabet[index:]
        return sous_alphabet
    else:
        return []

lettre = 'j'
resultat = alphabet_a_partir_de(lettre)
print(resultat)

def unseulàlafois():
    phrase = input("Veuillez entrer une suite de caractères : ")
    mots = phrase.split()
    
    for i, mot in enumerate(mots):
        unique_chars = []
        for char in mot:
            if mot.count(char) == 1:
                unique_chars.append(char)
        mots[i] = ''.join(unique_chars)
    
    new_phrase = ' '.join(mots)
    print(new_phrase)

unseulàlafois()

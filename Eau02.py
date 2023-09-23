def reverse():
    
    phrase = input('Entrez une suite de charactères : ')
    
    new_phrase = phrase.split()
    
    reverse_phrase = reverse(new_phrase)
    
    print(reverse_phrase)
    
reverse()
def disemvowel(string):
    

    vowel = ('AEIOUaeiou')
    new_string = ''
    
    for i in string:
        if i not in vowel:
            new_string += i
            
    return(new_string)


entrée_de_string = "This website is for losers LOL!"
sortie_de_string = disemvowel(entrée_de_string)
print(sortie_de_string)

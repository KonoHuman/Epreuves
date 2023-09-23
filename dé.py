import random

try:
    nombres_de_face = [1, 2, 3, 4, 5, 6]
        
    lancer = str(input('Voulez-vous lancer le dé ? :')).lower()
        
        
    if lancer == 'oui':
            
        face = random.choice(nombres_de_face)
        
        print('Le dé a attéri sur la face ' + str(face))
                
    elif lancer == 'non':
        
        print('Ah bon, dommage.')
        
    else:
        print('Veuillez répondre par oui ou par non.')
   
except ValueError:
    print('Veuillez ne répondre que par oui ou par non.') 

    
                       
                       
    
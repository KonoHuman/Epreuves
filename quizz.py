def quiz():
    
    réponses = []
    
    question1 = input('Quel est votre destination de reve ? : (A) La mer / (B) La Campagne (C) La ville : ').lower()
    question2 = input('Quel est votre temps préféré ? : (A) Pluvieux / (B) Ensolléillé / (C) Caniculeux : ').lower()
    question3 = input('Quel est votre caractère ? : (A) Flexible / (B) Calme / (C) Téméraire : ').lower()
    question4 = input('Quel est votre légendaire préférée ? : (A) Suicune / (B) Viridium / (C) Entei : ').lower()
    question5 = input('Quel est votre boissson préférée ? : (A) Eau / (B) Thé / (C) Soda : ').lower()
    
    if question1 == 'a':
    
        réponses.append(question1)
    
    elif question1 == 'b':
        
        réponses.append(question1)
        
    elif question1 == 'c':
        
        réponses.append(question1)
        
    if question2 == 'a':
        
        réponses.append(question2)
        
    elif question2 == 'b':
        
        réponses.append(question2)
        
    elif question2 == 'c':
        
        réponses.append(question2)
        
    if question3 == 'a':
        
        réponses.append(question3)
        
    elif question3 == 'b':
        
        réponses.append(question3)
        
    elif question3 == 'c':
        
        réponses.append(question3)
        
    if question4 == 'a':
        
        réponses.append(question4)
        
    elif question4 == 'b':
        
        réponses.append(question4)
        
    elif question4 == 'c':
        
        réponses.append(question4)
        
    if question5 == 'a':
        
        réponses.append(question5)
        
    elif question5 == 'b':
        
        réponses.append(question5)
        
    elif question5 == 'c':
        
        réponses.append(question5)
        
    
        
        
    nombre_de_a = réponses.count('a')
    nombre_de_b = réponses.count('b')
    nombre_de_c = réponses.count('c')

        
    if nombre_de_a > nombre_de_b and nombre_de_a > nombre_de_c:
        print('Vous devriez choisir un starter de type EAU')
            
    elif nombre_de_b > nombre_de_a and nombre_de_b > nombre_de_c:
        print('Vous devriez choisir un starter de type HERBE')
            
    elif nombre_de_c > nombre_de_a and nombre_de_c > nombre_de_b:
        print('Vous devriez choisir un starter de FEU')
        
    else:
        print('Il semblerait que vous ne soyez aucun de ces types là...')

quiz()
        
    
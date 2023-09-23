import random

try:
    
    liste_de_nombres = list(range(1, 1000))

    nombre_a_trouver = random.choice(liste_de_nombres)


    nombre_choisis = ()

        
    while nombre_choisis != nombre_a_trouver:
        nombre_choisis = int(input('Veuillez choisir un nombre :'))
        
        
        if nombre_choisis < nombre_a_trouver:
            print('Trop petit')
        elif nombre_choisis > nombre_a_trouver:
            print('Trop grand')

    resultat = 'Parfait, vous avez trouvé le nombre mystère qui était : ' + str(nombre_a_trouver )
    print(resultat)

except ValueError:
    print('Veuillez ne rentrer que des nombres')


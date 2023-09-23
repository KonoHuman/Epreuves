import nltk

from nltk.corpus import words

liste_de_mots = words.words()

import random
liste_de_mots_aleatoires = random.sample(liste_de_mots, 50)

mot_a_trouver = random.choice(liste_de_mots_aleatoires)


try:
        chance_du_joueur = 10

        mot_trouvé = []

        print("Bienvenue au jeu du pendu : ")

        while len(mot_trouvé) != len(mot_a_trouver):
            
            question = str(input("Donnez moi une lettre : ")).lower()

            if len(question) > 0 and len(question) < 2 and question in mot_a_trouver:
                
                mot_trouvé.append(question)
                
                print("Bravo : ",mot_trouvé)
                
            elif len(question) > 0 and len(question) < 2 and question not in mot_a_trouver:
                
                chance_du_joueur -= 1
                
                
                print("Mauvaise lettre, veuillez réssayez. Encore ", chance_du_joueur, " vies")
                
                print(mot_trouvé)
                
                if chance_du_joueur <= 0:
                        
                        print("Vous n'avez plus de vies, Partie terminée. Le mot à trouver était : ", mot_a_trouver)
                        
                        break
            elif len(question) > 1:
                print("Veillez n'entrer que des lettres")
                
                    

        if len(mot_trouvé) == len(mot_a_trouver):
            print("Félicitations, voici le mot trouvé : ", mot_a_trouver)

except ValueError:
    print("Veuillez n'entrer que des letttres : ")
    


                
                
                    

#Créez un programme qui affiche toutes les différentes combinaisons de deux nombre entre 00 et 99 dans l’ordre croissant.
#Exemples d’utilisation :
#$> python exo.py
#00 01, 00 02, 00 03, 00 04, ... , 00 99, 01 02, ... , 97 99, 98 99
#$>

def combinaisons():
    
    for i in range(100):
        for j in range(i, 100):
            if i != j:
                combinaison = f"{i:02} {j:02}"
                print(combinaison)  
                 
combinaisons()
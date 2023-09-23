import random

mot_de_passe = []

lettres_maj = [chr(x) for x in range(ord('A'), ord('Z') + 1)]

lettres_min = [chr(x) for x in range(ord('a'), ord('z') + 1)]

chiffres = list(range(10))

chiffres2 = [str(x) for x in chiffres]

caracteres_speciaux = ['!', '@', '#', '$', '%', '&']

liste_de_char = "".join(lettres_maj + lettres_min + chiffres2 + caracteres_speciaux)

nombre_de_charactères = int(input('Combien de charactères veux-tu ? '))

while len(mot_de_passe) != nombre_de_charactères:

   element_pioché = random.choice(liste_de_char)
   
   mot_de_passe.append(element_pioché)
   


if len(mot_de_passe) == nombre_de_charactères:
   
   mdp = "".join(mot_de_passe)
   
   print('Voici votre nouveau mot de passe : ' + str(mdp))





def row_sum_odd_numbers(n):
    with open("triangle.txt", "r") as fichier:
        triangle = fichier.readlines()
        
        # Vérifiez si l'indice n est valide
        if n < 0 or n >= len(triangle):
            print("Indice de ligne invalide.")
            return
        
        # Sélectionnez la ligne correspondante
        ligne = triangle[n].strip()  # .strip() pour supprimer les espaces inutiles
        
        # Initialisez la somme des chiffres à zéro
        somme_des_chiffres = 0
        
        # Parcourez les caractères de la ligne
        for caractere in ligne:
            if caractere.isdigit():
                somme_des_chiffres += int(caractere)
        
        print(f"Somme des chiffres dans la ligne {n} : {somme_des_chiffres}")

n = 3  # Remplacez 1 par l'indice de ligne que vous souhaitez traiter
row_sum_odd_numbers(n)

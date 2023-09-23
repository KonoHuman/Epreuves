def entredeux():

    try:
        premier_chiffre = input('Veuillez entrer un nombre : ')
        premier_chiffre = int(premier_chiffre)
        
        second_chiffre = input('Veuillez entrer un second nombre : ')
        second_chiffre = int(second_chiffre)

        if premier_chiffre < second_chiffre:
            for numbers in range(premier_chiffre, second_chiffre):
                print(numbers)
        elif second_chiffre < premier_chiffre:
            for numbers in range(second_chiffre, premier_chiffre):
                print(numbers)
                
    except ValueError:
        print('Error : Veuillez entrer un nombre')
                
entredeux()
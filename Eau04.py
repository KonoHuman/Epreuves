def suite_de_fibonacci():
    fibonacci = [0, 1]
    
    arg = int(input('Quel élément de la suite voulez-vous générer : '))
    
    if arg < 0:
        print('Erreur : Veuillez prendre un nombre positif.')
        return
    elif arg < len(fibonacci):
        index_donné = fibonacci[arg]
        print(index_donné)
    else:
        for _ in range(arg - len(fibonacci) + 1):
            calcul = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(calcul)
        
        index_donné = fibonacci[arg]
        print(index_donné)
        
suite_de_fibonacci()

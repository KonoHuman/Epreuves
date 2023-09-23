def suisse():
    try:
        a = input("Insérez un nombre : ")
        a = int(a)
        b = input("Insérez un second nombre : ")
        b = int(b)
        c = input("Insérez un troisième nombre : ")
        c = int(c)
        
        if b < a < c:
            print(a)
        elif c < a < b:
            print(a)
        elif a < b < c:
            print(b)
        elif c < b < a:
            print(b)
        elif a < c < b:
            print(c)
        elif b < c < a:
            print(c)
        else:
            print("Veuillez prendre des nombres différents : ")
    except ValueError:
        print("Veuillez prendre uniquement des nombres")
            
suisse()
    

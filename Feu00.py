def rectangle(a, b):
    
    return "o" + "-" * (a - 2) + "o\n" + ("|" + " " * (a - 2) + "|\n") * (b - 2) + "o" + "-" * (a - 2) + "o\n"

a = int(input("Entrez la longueur du rectangle : "))
b = int(input("Entrez la largeur du rectangle : "))
print(rectangle(a, b))

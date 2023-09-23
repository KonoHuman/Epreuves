def my_quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = int(input("Choisissez un pivot parmi les valeurs suivantes : "
                      "premier_nombre, second_nombre, troisieme_nombre, quatrieme_nombre, "
                      "cinquieme_nombre, sixieme_nombre, septieme_nombre, huitieme_nombre, "
                      "neuvieme_nombre, dixieme_nombre : "))
    
    # Vérifiez si le pivot choisi est l'une des dix variables
    if pivot not in [premier_nombre, second_nombre, troisieme_nombre, quatrieme_nombre,
                     cinquieme_nombre, sixieme_nombre, septieme_nombre, huitieme_nombre,
                     neuvieme_nombre, dixieme_nombre]:
        print("Le pivot choisi ne correspond à aucune des variables.")
        return None
    
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    
    return my_quick_sort(left) + middle + my_quick_sort(right)

if __name__ == "__main__":
    # Demandez à l'utilisateur de saisir dix variables
    premier_nombre = int(input("Entrez le premier nombre : "))
    second_nombre = int(input("Entrez le second nombre : "))
    troisieme_nombre = int(input("Entrez le troisième nombre : "))
    quatrieme_nombre = int(input("Entrez le quatrième nombre : "))
    cinquieme_nombre = int(input("Entrez le cinquième nombre : "))
    sixieme_nombre = int(input("Entrez le sixième nombre : "))
    septieme_nombre = int(input("Entrez le septième nombre : "))
    huitieme_nombre = int(input("Entrez le huitième nombre : "))
    neuvieme_nombre = int(input("Entrez le neuvième nombre : "))
    dixieme_nombre = int(input("Entrez le dixième nombre : "))
    
    # Récupérez les arguments en tant que liste de nombres
    numbers = [premier_nombre, second_nombre, troisieme_nombre, quatrieme_nombre,
               cinquieme_nombre, sixieme_nombre, septieme_nombre, huitieme_nombre,
               neuvieme_nombre, dixieme_nombre]
    
    # Triez la liste de nombres en utilisant my_quick_sort
    sorted_numbers = my_quick_sort(numbers)
    
    # Affichez la liste triée si elle n'est pas None (c'est-à-dire si le pivot est valide)
    if sorted_numbers is not None:
        print("Liste triée :", sorted_numbers)

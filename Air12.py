import sys

def my_quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    left = []
    right = []
    
    for num in array[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    
    return my_quick_sort(left) + [pivot] + my_quick_sort(right)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Erreur : Veuillez fournir une liste de nombres à trier.")
        sys.exit(1)

    try:
        numbers = [int(arg) for arg in sys.argv[1:]]
        sorted_numbers = my_quick_sort(numbers)
        print(" ".join(map(str, sorted_numbers)))
    except ValueError:
        print("Erreur : Les arguments doivent être des nombres entiers.")
        sys.exit(1)

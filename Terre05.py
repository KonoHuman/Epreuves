def division(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print("You can't divide by zero")
        
    except ValueError:
        print("Please enter a number")
        
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print(division(a, b))
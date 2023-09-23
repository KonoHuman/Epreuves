def pairs(number):
   try:     
        if number % 2 == 0:
            return True
        if number % 2 == 1:
            return False
    
   except ValueError:
       print("Please enter a number")
       
number = int(input("Enter a number: "))
print(pairs(number))
    

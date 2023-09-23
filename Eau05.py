def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_list(limit):
    prime_list = []
    for num in range(2, limit + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

limit = int(input("Entrez une limite pour générer des nombres premiers jusqu'à : "))
prime_numbers = generate_prime_list(limit)
print("Nombres premiers jusqu'à", limit, ":", prime_numbers)

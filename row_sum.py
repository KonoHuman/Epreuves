def row_sum_odd_numbers(n):
    if n == 1:
        return 1  
    else:
        start_number = (n - 1) ** 2 + 1  
        sum_of_row = sum(range(start_number, start_number + 2 * (n - 1), 2))
        return sum_of_row

n = 6  
result = row_sum_odd_numbers(n)
print(f"Sum of row {n} is {result}")

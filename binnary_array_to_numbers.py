def binary_array_to_number(arr):
    return int(''.join(str(i) for i in arr), 2)

binnary_input = [1, 1, 1, 1]
print(binary_array_to_number(binnary_input))
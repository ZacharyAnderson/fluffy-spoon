

def binary_array_to_number(arr):
    sum = 0
    for c, numbers in enumerate(reversed(arr),0):
        if numbers == 1:
            sum += 2 ** c
            print (sum)
    return sum
        
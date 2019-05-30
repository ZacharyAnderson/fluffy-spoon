def fibonacci_recursive(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)


def fibonacci(number):
    # Base case
    if number == 0:
        return 0

    a = 0
    b = 1
    # starting after base case and iteratively
    # adding all fibonacci sequences
    for _ in range(2, number):
        c = a + b
        a = b
        b = c
    return a + b


if __name__ == "__main__":
    print(fibonacci_recursive(10))

    print(fibonacci(10))

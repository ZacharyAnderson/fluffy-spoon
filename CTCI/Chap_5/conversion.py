def conversion(integer1, integer2):
    """
        determines the number of bits you would need to flip
        to convert integer1 into integer2
    """
    bit_difference = integer1 ^ integer2
    count = 0
    while bit_difference:
        count += 1
        bit_difference &= bit_difference - 1
    return count


if __name__ == "__main__":
    integer1 = 29
    integer2 = 15
    print(conversion(integer1, integer2))

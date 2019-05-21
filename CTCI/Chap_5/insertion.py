def insertion(n, m, i, j):
    """
        first, we must clear n to allow m to be inserted onto
        n.  Then we shift m to the left by i elements.
        Finally, we or the cleared n and shifted n
    """

    mask_n = n & ~((1 << (j+1)) - (1 << i))
    shifted_m = m << i
    return mask_n | shifted_m


if __name__ == "__main__":
    test = insertion(0b10000000000, 0b10011, 2, 6)
    print(bin(test))

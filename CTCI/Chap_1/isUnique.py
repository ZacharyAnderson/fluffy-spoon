def isUnique(string):
    """
        will check to see if string has all unique
        characters.
    """

    char_dict = dict()
    for ch in string:
        if ch in char_dict.keys():
            return False
        else:
            char_dict[ch] = 1
    return True

if __name__ == "__main__":
    print(isUnique("test"))
    print(isUnique("tes"))

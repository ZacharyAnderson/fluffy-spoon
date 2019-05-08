def checkPermutation(string1, string2):
    if len(string1) == len(string2):
        sorted_string1 = sorted(string1)
        sorted_string2 = sorted(string2)
        for i in range(len(string1)):
            if sorted_string1[i] != sorted_string2[i]:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    print(checkPermutation("testing", "testini"))

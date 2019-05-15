def is_one_away(string1, string2):
    if len(string1) == len(string2):
        count = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                count += 1
        return count <= 1
    else:
        if len(string1) > len(string2):
            return one_away_uneven_strings(string1, string2)
        else:
            return one_away_uneven_strings(string2, string1)


def one_away_uneven_strings(big, little):
    count = 1
    for i in range(len(little)):
        if little[i] == big[i] or (little[i] == big[i+1]):
            continue
        else:
            count += 1
    return count <= 1


if __name__ == "__main__":
    print(is_one_away("pale", "pad"))

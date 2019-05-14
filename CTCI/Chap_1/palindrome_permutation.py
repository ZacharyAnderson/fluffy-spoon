def is_palindrome_permutation(input_string):
    ch_pair_set = set()
    valid_chars = "abcdefghijklmnopqrstuvwxyz"

    for ch in input_string:
        if ch.lower() in ch_pair_set and valid_chars.find(ch.lower()) != -1:
            ch_pair_set.remove(ch.lower())
        elif valid_chars.find(ch.lower()) != -1:
            ch_pair_set.add(ch.lower())
    return len(ch_pair_set) <= 1


if __name__ == "__main__":
    print(is_palindrome_permutation("tact coa"))

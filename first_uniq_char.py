def firstUniqChar(s: str) -> int:

    if len(s) == 0:
        return -1
    char_set = dict()
    non_repeat_stack = list()

    for i in range(len(s)-1, -1, -1):
        if s[i] not in char_set:
            non_repeat_stack.append(i)
            char_set[s[i]] = 1
        else:
            char_set[s[i]] += 1

    while len(non_repeat_stack) > 0:
        top = non_repeat_stack.pop()
        if char_set[s[top]] < 2:
            return top

    return -1


if __name__ == "__main__":
    print(firstUniqChar("leetcode"))

def isValid(s: str) -> bool:
    paren_stack = list()
    paren_dict = {"}": "{", "]": "[", ")": "("}
    for ch in s:
        if ch in paren_dict.values():
            paren_stack.append(ch)
        if ch in paren_dict.keys():
            if len(paren_stack) == 0 or paren_stack.pop() != paren_dict[ch]:
                return False
    return len(paren_stack) == 0


if __name__ == "__main__":
    print(isValid("()"))

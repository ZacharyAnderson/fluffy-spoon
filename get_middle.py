def get_middle(s):
    length = len(s)
    if len(s) % 2 == 0:
        return (s[(length/2)-1]+s[(length/2)])
    else:
        return (s[(length/2)])
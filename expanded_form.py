def expanded_form(num):
    sum = []
    for c, number in enumerate(str(num)[::-1]):
        if int(number) != 0:
            sum.append(number + ('0' * c))
    return ' + '.join(sum[::-1])
    
    
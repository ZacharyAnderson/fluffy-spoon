def power_set(initial_set, index):
    sub_sets = []
    if len(initial_set) == index:
        sub_sets.append({})
    else:
        sub_sets = power_set(initial_set, index+1)
        item = initial_set[index]
        more_sets = []
        for subset in sub_sets:
            new_sub = []
            for val in subset:
                if val not in new_sub:
                    new_sub.append(val)
            new_sub.append(item)
            more_sets.append(new_sub)
            for value in more_sets:
                if value not in new_sub:
                    sub_sets.append(value)
    return sub_sets


if __name__ == "__main__":
    new_set = [1, 2, 3, 4, 5, 6]
    power_set(new_set, 0)

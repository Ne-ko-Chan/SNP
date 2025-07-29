def sort_list(list: list[int|float]) -> list[int|float]:
    if len(list) == 0:
        return []

    min = list[0]
    max = list[0]
    for v in list:
        if v > max:
            max = v
        if v < min:
            min = v

    for i in range(len(list)):
        if list[i] == min:
            list[i] = max
        elif list[i] == max:
            list[i] = min

    list.append(min)
    return list

print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))

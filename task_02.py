def coincidence(list: list = [], range: range = range(0,0)) -> list[int|float]:
    coincident = []
    for v in list:
        if not isinstance(v,(int, float)):
            continue
        if v < range.stop and v >= range.start:
            coincident.append(v)
    return coincident

# print(coincidence([1, 2, 3, 4, 5], range(3,6)))
# print(coincidence())
# print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1,4)))

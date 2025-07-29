from typing import Any


def max_odd(array: list[Any]) -> int | None:
    max = None
    for v in array:
        if not isinstance(v, (int, float)):
            continue
        if not v.is_integer():
            continue
        if v % 2 != 1:
            continue
        if max is None:
            max = v
            continue

        if v > max:
            max = v

    return int(max) if max != None else None


print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1,2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))

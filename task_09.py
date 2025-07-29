from typing import Any


def connect_dicts(dict1: dict[Any, int], dict2: dict[Any, int]) -> dict[Any, int]:
    # Count sum of values
    sum1: int = 0
    sum2: int = 0
    for _, v in dict1.items():
        sum1 += v
    for _, v in dict2.items():
        sum2 += v
    priority1 = True if sum1 > sum2 else False

    # Filter out bad entries
    dict1_filtered = {k: v for k, v in dict1.items() if v >= 10}
    dict2_filtered = {k: v for k, v in dict2.items() if v >= 10}

    # Start from low-priority dict(so you don't care if
    # something gets overwriten later)
    res = dict2_filtered if priority1 else dict1_filtered

    # Copy all the crap that's left :)
    for k, v in (dict1_filtered if priority1 else dict2_filtered).items():
        res[k] = v

    return dict(sorted(res.items(), reverse=True))


print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))

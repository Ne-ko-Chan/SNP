def multiply_numbers(inputs=None):
    if inputs is None:
        return None
    str_inputs = str(inputs)
    return str_mult(str_inputs)


def str_mult(string: str) -> None | int:
    res = None
    for c in string:
        if "0" <= c <= "9":
            res = res * int(c) if res != None else int(c)
    return res


print(multiply_numbers())
print(multiply_numbers("ss"))
print(multiply_numbers("1234"))
print(multiply_numbers("sssdd34"))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))

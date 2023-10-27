def new_format(string) -> str:
    length = len(string)
    new_string = ""
    if length > 3:
        for i in range(length - 1, -1, -1):
            new_string += string[i]
            if i > 0 and ((length - i) % 3) == 0:
                new_string += "."
    else:
        return string
    return new_string[::-1]


def new_format2(string) -> str:
    length = len(string)
    if length > 3:
        new_string = f"{int(string):,}"
    else:
        return string
    return new_string


assert new_format("1000000") == "1.000.000"
assert new_format("100") == "100"
assert new_format("1000") == "1.000"
assert new_format("100000") == "100.000"
assert new_format("10000") == "10.000"
assert new_format("0") == "0"


assert new_format2("1000000") == "1,000,000"
assert new_format2("100") == "100"
assert new_format2("1000") == "1,000"
assert new_format2("100000") == "100,000"
assert new_format2("10000") == "10,000"
assert new_format2("0") == "0"

# 1. custom map (iterator), приймає dict і приймає 2 функції.
#    першу фунцію застосовуємо до ключів а другу до значень.
#    map(dict, func1, funct2)
#   (func1(key), func2(value))


class CustomMap:
    def __init__(self, input_dict, func1, func2):
        self.input_dict = input_dict
        self.func1 = func1
        self.func2 = func2
        self.index = 0

    def __iter__(self):
        self.iter_keys = iter(input_dict.keys())
        return self

    def __next__(self):
        try:
            key = next(self.iter_keys)
            value = self.input_dict[key]
            return self.func1(key), self.func2(value)
        except StopIteration:
            raise StopIteration


def func1(key):
    return key.upper()


def func2(value):
    return value * 2


input_dict = {'a': 1, 'b': 2, 'c': 3}
custom_map_iterator = CustomMap(input_dict, func1, func2)
for result in custom_map_iterator:
    print(result)

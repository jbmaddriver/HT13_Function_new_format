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
        return self

    def __next__(self):
        if self.index < len(self.input_dict):
            key = list(self.input_dict.keys())[self.index]
            value = self.input_dict[key]
            transformed_key = self.func1(key)
            transformed_value = self.func2(value)
            self.index += 1
            return transformed_key, transformed_value
        else:
            raise StopIteration


def func1(key):
    return key.upper()


def func2(value):
    return value * 2


input_dict = {'a': 1, 'b': 2, 'c': 3}
custom_map_iterator = CustomMap(input_dict, func1, func2)
for result in custom_map_iterator:
    print(result)

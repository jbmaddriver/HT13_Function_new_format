# 1. custom map (iterator), приймає dict і приймає 2 функції.
#    першу фунцію застосовуємо до ключів а другу до значень.
#    map(dict, func1, funct2)
#   (func1(key), func2(value))


class CustomMap:
    def __init__(self, input_dict, func1, func2, iter_func=iter, next_func=next):
        self.input_dict = input_dict
        self.func1 = func1
        self.func2 = func2
        self.index = 0
        self.iter_func = iter_func
        self.next_func = next_func

    def iterate(self):
        return self.iter_func(self.input_dict)

    def get_next(self):
        key = list(self.input_dict.keys())[self.index]
        value = self.input_dict[key]
        transformed_key = self.func1(key)
        transformed_value = self.func2(value)
        self.index += 1
        return transformed_key, transformed_value


def func1(key):
    return key.upper()


def func2(value):
    return value * 2


input_dict = {'a': 1, 'b': 2, 'c': 3}
custom_map_iterator = CustomMap(input_dict, func1, func2)
iter_custom_map = custom_map_iterator.iterate()
for _ in input_dict:
    result = custom_map_iterator.get_next()
    print(result)

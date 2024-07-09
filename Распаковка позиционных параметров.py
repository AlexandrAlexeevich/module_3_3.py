def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызов функции с разными аргументами
print_params()
print_params(10)
print_params(10, 'другая строка')
print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка параметров
values_list = [42, 'привет', False]
values_dict = {'a': 99, 'b': 'словарь', 'c': [4, 5, 6]}

# Распаковка списка
print_params(*values_list)

# Распаковка словаря
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']

# Распаковка списка и передача отдельного параметра
print_params(*values_list_2, 42)

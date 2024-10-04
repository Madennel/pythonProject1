# Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# Вызовы функции с разным количеством аргументов
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка параметров из списка и словаря
values_list = [10, 'новая строка', False]
values_dict = {'a': 123.45, 'b': 'ещё одна строка', 'c': [4, 5, 6]}
print_params(*values_list, **values_dict)

# Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

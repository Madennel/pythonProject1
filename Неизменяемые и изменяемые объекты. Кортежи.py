# module_1_5.py

# Задаём переменные разных типов данных
immutable_var = (1, 2, 'a', 'b')
mutable_list = [1, 2, 'a', 'b']

# Выводим неизменяемый кортеж на экран
print("Immutable tuple:", immutable_var)

# Попытка изменить кортеж
try:
    immutable_var[0] = 10
except TypeError:
    print("Ошибка: кортежи неизменяемы")

# Изменяем список
mutable_list[4] = "Modified"

# Выводим изменённый список на экран
print("Mutable list:", mutable_list)
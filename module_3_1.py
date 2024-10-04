calls = 0  # Создадим глобальную переменную вне функций


def count_calls():
    global calls  # Используем оператор global внутри функции
    calls += 1


def string_info(string):
    count_calls()  # Увеличиваем счётчик вызовов
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счётчик вызовов
    return string.lower() in [item.lower() for item in list_to_search]


# Вызываем функции
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

# Выводим значение переменной calls
print(calls)
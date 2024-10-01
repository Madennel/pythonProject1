# Исходный список
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустые списки для простых и непростых чисел
primes = []
not_primes = []

# Перебираем список numbers
for num in numbers:
    # Пропускаем число 1, так как оно не является ни простым, ни составным
    if num == 1:
        continue

    # Предполагаем, что число простое
    is_prime = True

    # Проверяем делители от 2 до num (не включая num)
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False  # Если нашли делитель, число не простое
            break  # Прерываем цикл, так как уже знаем, что число не простое

    # В зависимости от значения is_prime добавляем число в соответствующий список
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим списки на экран
print("Primes:", primes)
print("Not Primes:", not_primes)

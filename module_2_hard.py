def generate_password(n):
    password = ""

    # Генерируем уникальные пары чисел от 1 до 20
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j

            # Проверяем кратность
            if n % pair_sum == 0:
                # Формируем строку из чисел пары
                password += f"{i}{j}"

    return password


# Примеры использования функции для чисел от 3 до 20
for number in range(3, 21):
    result = generate_password(number)
    print(f"{number} - {result}")
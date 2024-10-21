import numpy as np
from PIL import Image, ImageFilter

# NumPy
# 1. Создание массива
array = np.array([1, 2, 3, 4, 5])
print("Исходный массив:", array)

# 2. Операция: сложение с другим массивом
array2 = np.array([5, 4, 3, 2, 1])
sum_array = array + array2
print("Сумма массивов:", sum_array)

# 3. Операция: умножение на скаляр
multiplied_array = array * 2
print("Массив после умножения на 2:", multiplied_array)

# 4. Статистическая операция: среднее значение
mean_value = np.mean(array)
print("Среднее значение массива:", mean_value)

# 5. Операция: создание двумерного массива
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Двумерный массив:\n", matrix)

# 6. Транспонирование матрицы
transposed_matrix = np.transpose(matrix)
print("Транспонированная матрица:\n", transposed_matrix)

# Pillow
# 1. Открытие изображения
image = Image.open("example.jpeg")  # Убедитесь, что файл существует в вашей директории
print("Размер изображения:", image.size)

# 2. Изменение размера
resized_image = image.resize((100, 100))
resized_image.save("resized_image.jpeg")
print("Изображение изменено и сохранено как 'resized_image.jpeg'.")

# 3. Применение фильтра
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save("blurred_image.jpeg")
print("Изображение размазано и сохранено как 'blurred_image.jpeg'.")

# 4. Конвертация в другой формат (например, PNG)
image.convert("RGB").save("converted_image.png")
print("Изображение конвертировано и сохранено как 'converted_image.png'.")

# 5. Поворот изображения
rotated_image = image.rotate(90)
rotated_image.save("rotated_image.jpeg")
print("Изображение повернуто на 90 градусов и сохранено как 'rotated_image.jpeg'.")

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество students в список и сортируем его
students = sorted(students)

# Создаем пустой словарь для среднего балла
student_averages = {}

# Цикл по именам учеников в правильном порядке
for student in students:

    # Получаем список оценок ученика из списка grades
    grades_list = grades[list(students).index(student)]

    # Вычисляем средний балл как сумму всех оценок, деленную на их количество
    average = sum(grades_list) / len(grades_list)

    # Добавляем имя ученика и его средний балл в словарь
    student_averages[student] = average

# Выводим словарь с результатами в консоль
print(student_averages)
import sqlite3

# Подключаемся к базе данных (создается файл not_telegram.db, если его нет)
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Создаем таблицу Users, если она еще не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Очищаем таблицу перед добавлением новых записей (чтобы не было дублирования)
cursor.execute('DELETE FROM Users')
conn.commit()

# Заполняем таблицу 10 записями
users = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]
cursor.executemany('''
INSERT INTO Users (username, email, age, balance)
VALUES (?, ?, ?, ?)
''', users)
conn.commit()

# Обновляем balance для каждой записи с нечетным порядковым номером
cursor.execute('''
UPDATE Users
SET balance = 500
WHERE (id - 1) % 2 = 0
''')
conn.commit()

# Удаляем каждую третью запись, начиная с первой
cursor.execute('''
DELETE FROM Users
WHERE (id - 1) % 3 = 0
''')
conn.commit()

# Выбираем записи, где возраст не равен 60
cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
''')
records = cursor.fetchall()

# Выводим записи в заданном формате
for record in records:
    print(f"Имя: {record[0]} | Почта: {record[1]} | Возраст: {record[2]} | Баланс: {record[3]}")

# Закрываем подключение
conn.close()

import sqlite3

# Подключаемся к базе данных
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

# Удаляем пользователя с id=6
cursor.execute('DELETE FROM Users WHERE id = 6')
conn.commit()

# Подсчёт количества всех пользователей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Вычисление среднего баланса и вывод результата
if total_users > 0:
    print(all_balances / total_users)
else:
    print("Нет данных о пользователях.")

# Закрываем подключение
conn.close()

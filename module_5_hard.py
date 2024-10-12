class MessageCollection:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def __str__(self):
        return str(self.messages)

    def __repr__(self):
        return f"MessageCollection({self.messages})"

    def __contains__(self, message):
        return message in self.messages

    def __eq__(self, other):
        if isinstance(other, MessageCollection):
            return self.messages == other.messages
        return False

    def __len__(self):
        return len(self.messages)

# Пример использования класса
collection = MessageCollection()

# Добавление сообщений
collection.add_message('Лучший язык программирования 2024 года')
print(collection)  # ['Лучший язык программирования 2024 года']

collection.add_message('Для чего девушкам парень программист?')
print(collection)  # ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']

# Проверка наличия сообщения
print('Лучший язык программирования 2024 года' in collection)  # True
print('Не существующее сообщение' in collection)  # False

# Проверка длины коллекции
print(len(collection))  # 2

# Создание другой коллекции для сравнения
another_collection = MessageCollection()
another_collection.add_message('Лучший язык программирования 2024 года')
another_collection.add_message('Для чего девушкам парень программист?')

# Сравнение коллекций
print(collection == another_collection)  # True

# Вывод представления коллекции
print(repr(collection))  # MessageCollection(['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?'])
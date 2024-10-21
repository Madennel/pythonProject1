import inspect


def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получаем модуль объекта
    module = obj.__module__

    # Собираем информацию в словарь
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return info


# Пример использования
class SampleClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        return f"Value: {self.value}"


# Создаем объект класса
sample_object = SampleClass(42)

# Получаем информацию об объекте
object_info = introspection_info(sample_object)
print(object_info)

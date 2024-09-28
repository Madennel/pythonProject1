# module_1_6.py

# Работа со словарями
my_dict = {"Maxim": 2001, "Nikita": 1997, "Alina": 2000}
print("Dict:", my_dict)
print("Existing value:", my_dict["Alina"])
print("Not existing value:", my_dict.get("Alex", None))
my_dict["Kamila"] = 1981
my_dict["Artem"] = 1915
print("Deleted value:", my_dict.pop("Nikita"))
print("Modified dictionary:", my_dict)

# Работа с множествами
my_set = {1, "Яблоко", 42.314, 1.0, 1, (5, 6, 1.6)}
print("Set:", my_set)
my_set.add("Груша")
my_set.add(13)
my_set.remove((5, 6, 1.6))
print("Modified set:", my_set)

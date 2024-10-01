first = int(input("123"))
second = int(input("456"))
third = int(input("789"))

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)

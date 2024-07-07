first = int(input("Введите первое число:"))
second = int(input("Введите второе число:"))
third = int(input("Введите третье число:"))
if first == second and second == third:
    print(f"Вы ввели {3} одинаковых числа")
elif first == second or second == third or third == first:
    print(f"Вы ввели {2} одинаковых числа")
elif first != second or second != third:
    print(f"Вы ввели {0} одинаковых чисел")
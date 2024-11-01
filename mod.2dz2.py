first = int(input("введите первое значение: "))
second = int(input("введите второе значение: "))
third = int(input("введите третье значение: "))
if first == second == third:
    print("вывести три")
elif  second == first  or first == third or second==third:
    print("вывести два")
else:
    print("вывести ноль")
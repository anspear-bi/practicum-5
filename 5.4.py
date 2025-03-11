# -*- coding: utf-8 -*-
"""
5.4
"""
def parrot_declension(n):
    if 11 <= n % 100 <= 14:
        return "попугаев"
    elif n % 10 == 1:
        return "попугай"
    elif n % 10 in [2, 3, 4]:
        return "попугая"
    else:
        return "попугаев"

number = int(input("Введите число (1-100): "))
if 1 <= number <= 100:
    print(f"{number} {parrot_declension(number)}")
else:
    print("Число не в пределах от 1 до 100.")


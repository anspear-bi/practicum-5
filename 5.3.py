# -*- coding: utf-8 -*-
"""
5.3
"""
def is_criminal(n):
    d1 = n // 1000
    d2 = (n // 100) % 10
    d3 = (n // 10) % 10
    d4 = n % 10
    return (d1 == d4) and (d2 == d3)

number = int(input("Введите четырехзначное число: "))
if is_criminal(number):
    print("Число настоящее.")
else:
    print("Число кривое.")


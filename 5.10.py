# -*- coding: utf-8 -*-
"""
5.10
"""
def is_valid_pin(pin):
    if len(pin) != 4:
        return False
    if len(set(pin)) != len(pin):  # проверка на повторяющиеся цифры
        return False
    year = int(pin)
    if 1900 <= year <= 2050:
        return False
    return True

pin = input("Введите PIN-код: ")
if is_valid_pin(pin):
    print("ОК")
else:
    print("ERROR")


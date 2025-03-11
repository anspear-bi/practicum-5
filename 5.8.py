# -*- coding: utf-8 -*-
"""
5.8
"""
N = int(input("Введите количество кнатов: "))
galleons = N // (17 * 29)
N %= (17 * 29)
sickles = N // 29
knuts = N % 29

if galleons > 0:
    print(f"{galleons} галлеонов")
if sickles > 0:
    print(f"{sickles} сиклей")
if knuts > 0:
    print(f"{knuts} кнатов")


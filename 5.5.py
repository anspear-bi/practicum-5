# -*- coding: utf-8 -*-
"""
5.5
"""
def bmi_category(bmi):
    if bmi < 16:
        return 'Выраженный дефицит массы тела'
    elif 16 <= bmi < 18.5:
        return 'Недостаточная масса тела'
    elif 18.5 <= bmi < 25:
        return 'Нормальная масса тела'
    elif 25 <= bmi < 30:
        return 'Избыточная масса тела'
    elif 30 <= bmi < 35:
        return 'Ожирение 1 степени'
    elif 35 <= bmi < 40:
        return 'Ожирение 2 степени'
    else:
        return 'Ожирение 3 степени'

weight = float(input("Введите вес в кг: "))
height = float(input("Введите рост в метрах: "))

bmi = weight / (height * 2)
print(f"Ваш ИМТ: {bmi:.2f}. Категория: {bmi_category(bmi)}")


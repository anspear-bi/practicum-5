# -*- coding: utf-8 -*-
"""
5.2
"""
import math

def circle_position(xc, yc, r, x, y):
    distance = math.sqrt((x - xc) * 2 + (y - yc) * 2)
    if distance < r:
        return "Точка внутри окружности"
    elif distance == r:
        return "Точка на окружности"
    else:
        return "Точка вне окружности"

xc = int(input("Введите координату x центра окружности: "))
yc = int(input("Введите координату y центра окружности: "))
r = int(input("Введите радиус окружности: "))
x = int(input("Введите координату x точки: "))
y = int(input("Введите координату y точки: "))

print(circle_position(xc, yc, r, x, y))


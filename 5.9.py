# -*- coding: utf-8 -*-
"""
5.9
"""
heights = [int(x) for x in input("Введите высоты трех башен через пробел: ").split()]

for i in range(len(heights)):
    for j in range(len(heights) - 1):
        if heights[j] < heights[j + 1]:
            heights[j], heights[j + 1] = heights[j + 1], heights[j]
print("Высоты от наибольшей к наименьшей:", heights)



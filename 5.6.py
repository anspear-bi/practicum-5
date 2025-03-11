# -*- coding: utf-8 -*-
"""
5.6
"""
days = [int(input(f"Введите количество подданных, которые видели улыбку в день {i+1}: ")) for i in range(3)]
repeat_count = {}

for count in days:
    if count in repeat_count:
        repeat_count[count] += 1
    else:
        repeat_count[count] = 1

print("Количество повторений:")
for key, value in repeat_count.items():
    print(f"{key}: {value} раз(а)")


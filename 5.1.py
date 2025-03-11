# -*- coding: utf-8 -*-
"""
5.1
"""
def days_in_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 366  # високосный год
    else:
        return 365  # невисокосный год

year_input = int(input("Введите год: "))
print(f"В {year_input} году {days_in_year(year_input)} дней.")


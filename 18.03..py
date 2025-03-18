# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 15:12:20 2025

@author: aasta
"""


#Квадрат
a="*"
length = int(input("Введите длину стороны квадрата: "))
for i in range (length):
    print(a * length)
    
#Окно    
a='*'
b=' '
length = int(input('Введиите число: '))
print(a * length)
for i in range (length - 2):
    print (a, end = '')
    print (b*(length - 2), end='')
    print (a)
print (a * length)

#Обратный отсчёт
number = int(input('Введите число начала отсчёта: '))
meaning = number - 1
if meaning == 0:
    print ('pusk')
else:
    print (meaning)
    

#Максимум из двух.1
a,b=map(int,input('Введите два целых числа: ').split())
s = max(a,b)
print (s)


#Максимум из двух.2
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a > b:
    print (a)
else:
    print (b)


#Cумма двух
a = int(input('Введите а: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
if a == b + c or b == a + c or c == a + b:
    print('Yes') 
else:
    print('No') 
    
    


    

    


    
    
    
    

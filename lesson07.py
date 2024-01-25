# Знакомство с языком Python (семинары)
# Урок 7. Функции высшего порядка
# https://gb.ru/lessons/391158


# 01:13:30
"""
(разбор ДЗ-06, Александр Верзун)

Задача 30: 
Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: 
an = a1 + (n - 1) * d

Каждое число вводится с новой строки.
"""
# Ввод: 7 2 5 # 7 - число, 2 - шаг, 5 - количество
# Вывод: 7 9 11 13 15

"""
Решение

Вариант 1
"""

num = int(input('Input number: ')) 
step = int(input('Input step: '))
count = int(input('Input count: '))

my_list = [num]
for i in range(step, count + 1): 
	my_list.append(num + (i - 1) * step)

print(num, step, count)
print(*my_list)

'''
Вариант 2 (генератор списков)
'''
my_list = [num + i * step for i in range(count)]
print(my_list)

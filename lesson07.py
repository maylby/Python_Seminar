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

# num = int(input('Input number: ')) 
# step = int(input('Input step: '))
# count = int(input('Input count: '))

# my_list = [num]
# for i in range(step, count + 1): 
# 	my_list.append(num + (i - 1) * step)

# print(num, step, count)
# print(*my_list)

'''
Вариант 2 (генератор списков)
'''
# my_list = [num + i * step for i in range(count)]
# print(my_list)


"""
Задача 32:

Задать произвольные границы диапазона значений (min, max) и  
определить индексы элементов массива (списка),
значения которых лежат в заданном диапазоне (?),
т.е. не меньше заданного минимума 
и не больше заданного максимума.
"""

# Ввод: 
# [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 
# 10, -9, 0, -5, -5, 7]

# Вывод: [1, 9, 13, 14, 19]


#	         1                          9            13  14                19
list1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#	      0  1  2  3   4   5  6  7   8  9  10  11 12  13 14  15  16 17  18  19

min = int(input('min: '))
max = int(input('max: '))

def search(arr): # 'arr' - пустой список для передачи значений 'list1'
	result = []
	for i in range(len(arr)): 
		if min <= list1[i] <= max: # допустимая форма записи
			result.append(i) # добавление индексов элементов
	return result 

print('Ввод: ', list1)
print('Вывод:', search(list1)) 

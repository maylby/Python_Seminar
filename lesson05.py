# Знакомство с языком Python (семинары)
# Урок 5. Рекурсия и алгоритмы
# https://gb.ru/lessons/391156


# (01:03:50 - чат семинара 4)

# Задача для самостоятельного решения 
# (см. разбор задачи обещан на сминаре № 5)

"""		
Сергей Сердюк 
Вводятся номера телефонов в одну строчку через пробел 
с разными кодами стран: +7, +6, +2, +4 и т.д. 
Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п., 
а значения - список номеров, следующих в том же порядке, что и во входной строке, 
с соответствующими кодами. Полученный словарь вывести командой:
"""
# print(*sorted(d.items()))

# Sample Input:
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
# Sample Output:
# ('+2', ['+21235777890', '+21234567110']) 
# ('+5', ['+52134567890']) 
# ('+6', ['+61234576890']) 
# ('+7', ['+71234567890', '+71234567854', '+71232267890'])
"""
Решение (???)
"""
# dict_t = '+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890'

# d = {} # создан пустой словарь
# d = dict()

# for i in d:
# 	for j in tel: 
# 		if item != tel[:2]: tel += j
# 		else: d[item] = [tel, ' ']
# 	d += i
# 	print('{}: {}'.format(item, d[item]), end = " ")
# print(d.items()) # dict_items([('up', '↑'), ('down', '↓'), ('right', '→')])
# 		 # выдача "словаря" в виде "списка" "кортежей", 
# 		 # где указаны "ключ" и его "значение"
# print(*sorted(d.items())) # Как именно сортирует словари '*sorted'?


"""
Задача 22: 
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, 
которые встречаются в обоих наборах.

Пользователь вводит 2 числа. 
n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
"""
# # 11 6
# # 2 4 6 8 10 12 10 8 6 4 2
# # 3 6 9 12 15 18
# # 6 12


# list_n = '2 4 6 8 10 12 10 8 6 4 2'
# list_m = '3 6 9 12 15 18 2'
# # print(arr_n.split())
# n = print(len(list_n.split()), end = " ")
# m = print(len(list_m.split()))
# print(list_n)
# print(list_m)

# set_n = set(list_n.split())
# set_m = set(list_m.split())
# # print(set_n)
# # print(set_m)

# if set_n != set_m:
#     # result = sorted(set_n.intersection(set_m))  # 'intersection' - поиск 
#                                                 # пересечения множеств
#     result = sorted(set_n & set_m)  # '&' - амперсент, другой способ 
#                                     # поиска пересечения множеств
#     print(*result) # Как вывести значения в порядке возрастания?



"""
Задача 24: 

В фермерском хозяйстве в Карелии выращивают чернику. 
Она растет на круглой грядке, причем кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растет N кустов. 
Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
на них выросло различное число ягод – на i-ом кусте выросло ai ягод.

В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
"""
# # 4 -> 1 2 3 4
# # 9

# n = int(input('Input quantity numbers: '))
# arr = []

# from random import randint 
# for i in range(n):
#     arr.append(randint(1, 10)) 
# print(f'{n} -> {arr}')

# count = list()
# for i in range(len(arr)):
#     count.append(arr[i-2] + arr[i-1] + arr[i])
# print('max =', max(count))



# 00:34:00
''' 
Вариант 2 (цикл 'while')
(Генадий Ионов)
'''
# n = int(input('Input quantity numbers: '))
# arr = [] 

# from random import randint # вставил рандомный ввод
# for i in range(n):
#     arr.append(randint(1, 10)) 
# print(f'{n} -> {arr}')

# temp = 0
# count = 0
# maxNum = 0

# while count < len(arr):
#     temp = arr.pop(-1)  # <- объединил в одну строку 
#                         # temp = arr[-1] и arr.pop(-1)
#     arr.insert(0, temp)
#     count += 1
#     a = arr[i-2] + arr[i-1] + arr[i] # заменил цифры (1,2,3) на индекс (i)
#     if a > maxNum: maxNum = a
# print(maxNum)
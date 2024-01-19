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

# n = print(len(list_n.split()), end = " ")
# m = print(len(list_m.split()))
# print(list_n)
# print(list_m)

# set_n = set(list_n.split())
# set_m = set(list_m.split())
# # print(set_n) # проверочный вывод на экран
# # print(set_m) # проверочный вывод на экран

# if set_n != set_m: # print(*sorted(set_n & set_m)) # запись в одну строку
#     result = sorted(set_n.intersection(set_m))  # 'intersection' - поиск 
#                                                 # пересечения множеств
#     result = sorted(set_n & set_m)  # '&' - амперсент, другой способ 
#                                     # поиска пересечения множеств
#     print(*result)  # (???) Не выводит значения в порядке возрастания!
#                     # Вывод: '12 2 6' <- неупорядоченный результат



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

"""
Вариант 1
"""
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
#                         # temp = arr[-1] и arr.pop(-1), т.к.
#                         # метод pop() не только удаляет элемент, но
#                         # и возвращает, т.е. записывает его значение
#     arr.insert(0, temp)
#     count += 1
#     a = arr[i-2] + arr[i-1] + arr[i] # трёх ближайших значений
#                                      # заменил цифры (1,2,3) на индекс (i)
#     if a > maxNum: maxNum = a # определение максимальной суммы
# print(maxNum)


# 00:35:55
"""
Вариант 2 (Задача 22)
(Генадий Ионов) 
"""
# print()
# var1 = '5 4' # количество элементов двух списков (var2 и var3)
#              # количество элементов вводится вручную заранее,
#              # в "Варианте 1" решения, число элементов вычислялось 
#              # автоматически по заданным спискам (var2 и var3),
#              # автоматизация позволяет избежать ошибок при вводе данных
# print(var1)

# var2 = '1 3 5 7 9'
# var3 = '2 3 4 5'
# print(f'{var2}\n{var3}')

# a = set(var2.split())
# b = set(var3.split())
# i = a.intersection(b)
# print(*sorted(i))


# 00:41:00

'''
Сергей Сердюк 
Задача 31. Решение в группах
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). 
Требуется найти N-е число Фибоначчи

Input: 7 
Output: 21
Задание необходимо решать через рекурсию
'''

# a = int(input('Input number A: '))
# def fib(a):
#     if a == 0: return 0 
#     if a in [1, 2]: return 1
#     return fib(a-1) + fib(a-2)
# list_a = []
# for i in range(0, a): 
#     list_a.append(fib(i)) # "append" - добавление каждого полученного значения 
#                           # в конец текущего списка (слева направо)
# print(list_a)
# print()


""" 
Найти факториал числа 'x'

Вариант 1
"""
x = int(input('Input number X: '))
res = 1
for i in range(res, x + 1): res *= i # запись цикла и результата в одну строку
                                     # 'range' - диапазон от 'res' до 'x',
                                     # 'x' обозначаем, как 'x + 1', т.к. 
                                     # последнее число (x) цикл (for) не захватывает
print(f'{x}! = {res}')
print()


'''
Вариант 2
'''
n = int(input('Input number N: '))
def factorial(n):
    res = 1
    for i in range(res, n + 1): res *= i # запись цикла и результата в одну строку
    return res
f = factorial(n)
print(f'{n}! = {f}')

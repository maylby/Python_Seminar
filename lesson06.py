# Знакомство с языком Python (семинары)
# Урок 6. Повторение списков
# https://gb.ru/lessons/391157


# 00:12:35
"""
Разбор решения задач ДЗ-05

Задача 1 (26): 
Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
"""
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
""""
Решение
"""
a = int(input('Input base: '))
b = int(input('Input exp: '))

def power(a, b):
    if b == 0: return 1
    return (a * power(a, b - 1))

print(f'{a} ** {b} = {power(a, b)}')


"""
Задача 28: 
Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
"""
# 2 2
# 4

"""
Решение
""" 
a = int(input('Input A: '))
b = int(input('Input B: '))

def sum(a, b):
    if a < b: a, b = b, a # аналог записи "temp" (передача значений)
	# temp = a 
	# a = b
	# b = temp 
    if b == 0: return a
    return sum(a + 1, b - 1) # вариант записи

print(f'sum: {sum(a, b)}')


# 00:26:40
"""
Задача про холодильники 
(чат семинара)

Программа должна вывести номера зараженных холодильников через пробел. 
Если таких холодильников нет, ничего выводить не нужно.

Формат входных данных
В первой строке подаётся число 'n'.
'n' – количество холодильников. 
В последующих n-строках вводятся строки, 
содержащие латинские строчные буквы и цифры, 
в каждой строке от 5 до 100 символов.

два способа решения через списки и через условие (?)
"""


# 00:52:00
"""
Определить рекурсией является слово (ряд чисел) палиндромом. 
Палиндром, не палиндром, рекурсия
"""
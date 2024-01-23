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
# a = int(input('Input base: '))
# b = int(input('Input exp: '))

# def power(a, b):
#     if b == 0: return 1
#     return (a * power(a, b - 1))

# print(f'{a} ** {b} = {power(a, b)}')


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
# a = int(input('Input A: '))
# b = int(input('Input B: '))

# def sum(a, b):
#     if a < b: a, b = b, a # аналог записи "temp" (передача значений)
# 	# temp = a 
# 	# a = b
# 	# b = temp 
#     if b == 0: return a
#     return sum(a + 1, b - 1) # вариант записи

# print(f'sum: {sum(a, b)}')


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

# 00:27:30

''' Определить дружественная рекурсия или нет '''
"""
Дружественные функции - это функции, которые не являются членами класса, 
однако имеют доступ к его закрытым членам - переменным и функциям,
"""

# Sample Input 1: 6

# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n

# Sample Output 1:
# 1 2 3


# Sample Input 2: 9

# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton

# Sample Output 2: 
# 1 2 7 8


# 00:28:10
"""
Сергей Сердюк 1. 
Напишите функцию, которая принимает одно число и проверяет, 
является ли оно простым

*Напоминание: Простое число - это число, 
которое имеет два делителя: 1  и n(само число)*

Три вывода:
    - Простое число
    - Составное число
    - Рекурсия 
"""
# 00:52:00 - разбор решений
"""

Решение
"""
n = int(input('Input N: '))

def function(n, d = 2): # 'd = 2' - именованный аргумент, применён,
                         # чтобы постоянно не вводить занчение 2, которое
                         # будет использоваться постоянно для определения 
                         # простого и составного числа
                         # 'd' - не именованный аргумент
    if n == 2 or d * d > n: return True # квадрат делителя (d*d) больше делимого (n)
                                        # если выполняется 1-е условие или не выпоняется 2-е, 
                                        # то возврат 'True'
                                        # если не выполняется 1-е условие или выполняется 2-е, 
                                        # то 'function(n, d + 1)' и вывод: 'False'
    elif n % d == 0: return False
    return function(n, d + 1)

print(function(n, d = 2))


# 1:09:25 - прервал сессию
# 00:28:30
"""
Определить рекурсией является слово (ряд чисел) палиндромом. 

Три вывода:
    - Палиндром
    - Не палиндром
    - Рекурсия

Не обязательно брать слова-палиндромы (шалаш, колок, тот, оно),
можно использовать набор чисел (1 2 3 3 2 1)

Решение
"""
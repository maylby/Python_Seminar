# Знакомство с языком Python (семинары)
# Урок 2. Циклы (for, while)
# https://gb.ru/lessons/391153


# 00:45:30

''' Задача 9. 
Решение в группах

По данному целому неотрицательному n вычислите значение n!. 
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
Решить задачу используя цикл while '''

# Input: 5
# Output: 120


'''Решение 1 в обратном порядке, от N до 1'''

# n = int(input('Input number N: ', ))
# res = 1
# while n > 0:
#     res *= n
#     n -= 1
# print(f'result = {res}')


'''Решение 2 в соответствии с условием, от 1 до N'''

# num = int(input('Input number N: ', ))
# result = 1
# x = 1
# i = 0
# while i < num:
#     result *= x
#     x += 1
#     i += 1
#     print(f'result = {result}')


# 00:54:00

# Задача на применение цикла While
# Найти сумму пяти чисел, 
# каждое следующее из которых меньше предыдущего на единицу

# x = int(input('Input number: ', ))
# sum = 0
# # x = 5
# while x > 0:
#     print(sum)
#     sum += x
#     x -= 1
#     result = int(sum)
# print(sum, 'result =', result) # 1+2+3+4+5


# 00:57:00

''' Задача 11. 
Решение в группах
Дано натуральное число A > 1. 
Определить, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)= A. 
Если А не является числом Фибоначчи, выведите число -1.'''

# # Input: 5
# # Output: 6

# n = int(input('Input number: ', ))
# f1 = 0
# f2 = 1
# f3 = 0
# i = 1
# while f3 < n:
#     f3 = f1 + f2
#     f1 = f2
#     f2 = f3
#     i += 1
#     print(f'f3 = {f3}; i = {i}')
#     if f3 > n: print(f'n = {n} -> not a fibonacci number')
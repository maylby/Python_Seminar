# Знакомство с языком Python (семинары)
# Урок 8. Работа с файлами
# https://gb.ru/lessons/391159


# 00:09:00
''' 
Разбор ДЗ-07

Задача 1 

print_operation_table
'''
# https://autotest.gb.ru/problems/83?lesson_id=391158&_ga=2.55648939.1223630724.1705653773-1736153193.1704617193
'''

Напишите функцию 
'''
# print_operation_table(operation, num_rows, num_columns), 
'''
которая принимает в качестве аргумента функцию, 
вычисляющую элемент по номеру строки и столбца. 
По умолчанию номер столбца и строки = 9.

Аргументы num_rows и num_columns указывают 
число строк и столбцов таблицы, 
которые должны быть распечатаны.

Нумерация строк и столбцов идет с единицы 
(подумайте, почему не с нуля).

Если строк меньше двух, выдайте текст ОШИБКА! 
Размерности таблицы должны быть больше 2!.

Примечание: 
бинарной операцией называется любая операция, у которой 
ровно два аргумента, как, например, у операции умножения.

Между элементами должен быть 1 пробел, 
в конце строки пробел не нужен.

Пример
'''
# На входе:
# print_operation_table(lambda x, y: x * y)

# На выходе:
# 1 2 3
# 2 4 6 
# 3 6 9

""" 
Решение


Вариант 1 
(Марина Вершинина)
"""
num_rows = int(input('Number rows: '))
num_columns = int(input('Number columns: '))

def print_operation_table(operation, num_rows, num_columns):
    res = []
    if num_rows < 2:
        print('Error!')
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                res.append(operation(i, j))

            print(*res) # вариант вывода 1
            res = []
        
        # for i in range(0, len(res), num_columns):
        #     print(*res[0 + i: num_columns + i]) # вариант вывода 2

print_operation_table(lambda x, y: x * y, num_rows, num_columns)

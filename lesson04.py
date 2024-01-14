''' 
Знакомство с языком Python (семинары)
Урок 4. Словари, множества и профилирование 
'''
# https://gb.ru/lessons/391155



""" Задача 3 (20) """ 

"""
В настольной игре Скрабл (Scrabble) 
каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
"""
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.

"""
А русские буквы оцениваются так:
"""
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.

"""
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, 
которое содержит либо только английские, либо только русские буквы.

ПРИМЕР 

(презентация): 
"""
# Ввод: ноутбук
# Вывод: 12

""" 
(autotest): 
"""
# k = 'ноутбук'
# 12

""" 
Вариант 1 
(Андрей Лопатько) 
"""
# w = input('Input word: ')
# word = w.upper() 

# dict_rus = {'АВЕИНОРСТ' : 1,
# 	        'ДКЛМПУ' : 2,
# 	        'БГЁЬЯ' : 3,
# 	        'ЙЫ' : 4,
# 	        'ЖЗХЦЧ' : 5,
# 	        'ШЭЮ' : 8,
# 	        'ФЩЪ' : 10}
# dict_en = {'AEIOULNSTR' : 1,
# 		   'DG' : 2,
# 		   'BCMP' : 3,
# 		   'FHVWY' : 4,
# 		   'K' : 5,
# 		   'JX' : 8,
# 		   'QZ' : 10}
# result = 0
# for i in word:
# 	for simbols, count in dict_rus.items() | dict_en.items():
# 		if i in simbols: result += count
# print(result)


""" Задача 1 (16) """
# https://autotest.gb.ru/problems/21?lesson_id=391154&_ga=2.8891701.1648384661.1703691758-1734585693.1703049693

""" 
Требуется вычислить, сколько раз встречается 
некоторое число k в массиве list_1.
Найдите количество и выведите его. 
"""

# # Пример:

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# # 1

''' Решение:

Вариант 1 
(решение с применением метода 'count')
'''

# list_1 = [1, 2, 3, 4, 5, 3]
# k = 3

# print('list_1 =', list_1)
# print('k =', k)
# print(list_1.count(k)) # метод 'count', встроен в функционал Pyhton 


'''
Вариант 2 (алгоритмическое решение)
'''

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# print('list_1 =', list_1)
# print('k =', k)

# count = 0
# for i in list_1:
# 	if i == k: count += 1
# print(count)



""" Задача 2 (18) """
"""
Требуется найти в массиве list_1 
самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. 
Если значение k совпадает с этим элементом - выведите его.
"""
# Пример:

# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5

''' Решение 
(С-04; 00:17:40 - Андрей Лопатько)
'''
# n = int(input('Input quantity number: '))
# list_1 = [] # для сохранения созданного списка (массива)
# from random import randint # без "импорта" 'randint' функция не работает 
# for i in range(n):
#     list_1.append(randint(-10, 10)) # Если в промежутке (-10, 10) 
#                                     # заменить '-10' на другое число, то результат поиска 
#                                     # ближайшего числа к заданному числу 'k' 
#                                     # выдаёт ошибочные значения
# print(f'list_1 = {list_1}')

# k = int(input('k = '))

# min1 = abs(k - list_1[0]) # Функция 'abs()' возвращает абсолютное значение заданного числа: 
#                           # - Целые числа — целочисленное абсолютное значение; 
#                           # - Числа с плавающей точкой — абсолютное значение с плавающей точкой; 
#                           # - Комплексные числа — величина числа.
# result = list_1[0]
# for i in range(1, len(list_1)):
#     if (k - list_1[i]) < min1: 
#         min1 = abs(k - list_1[i])
#         result = list_1[i]
# print(result) # Как вернуть два числа, если минимумы совпадают? 
#               # Пример:
#               # list_1 = [10, 9, 2, -10, 4]
#               # k = 3
#               # 4 <- выдача || реальный результат -> 2 и 4
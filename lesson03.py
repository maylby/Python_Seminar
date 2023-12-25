# Знакомство с языком Python (семинары)
# Урок 3. Списки и словари
# https://gb.ru/lessons/391154


# 00:39:35

""" Задача №17. Общее обсуждение 
Дан список чисел. Определите, сколько в нем встречается различных чисел. """

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

""" Примечание: Пользователь может вводить значения
списка или список задан изначально. """


""" Моё решение (while) """

# # n = int(input())
# n = [1, 1, 2, 0, -1, 3, 4, 4]
# count = int(len(n))
# temp = 0
# i = 0

# while n > 0:
#     if n[i] != n[i+1]: temp += 1
#     if n[i] == n[i+1]: n += 1
# print(temp)


''' Решение 1 (множество ('set') - Сергей Пономарёв) '''

# my_dict = [1, 1, 2, 0, -1, 3, 4, 4]
# print('Input: ', my_dict)
# print('Output: ', len(set(my_dict)))
# new_set = set() # пустое множество (см. урок)


# 01:10:30

""" Решение (чат - Андрей Лапотько) """

# nums = [1, 1, 2, 0, -1, 3, 4, 4]
# result = []
# for i in nums:
#     if i not in result:
#         result.append(i) # 'append' добавляет элемент вправо
#                          # 'insert' добавляет элемент влево
#                          # здесь 'insert' не работает
# print(nums)
# print(result)
# print(len(result))



""" Задача №19. Решение в группах """

""" Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, 
K – положительное число. """

# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

""" Примечание: Пользователь может вводить значения
списка или список задан изначально. """

# В 2-х решениях, при разных сдвигах ('k = 3' и 'k = 2'), 
# ответ один и тот же (???)

""" Решение срезами (Сергей Пономарёв(?))"""

# my_dict = [1, 2, 3, 4, 5]
# k = 3 # сдвиг на 3 позиции
# print(my_dict[k:] + my_dict[:k])

# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


# 01:22:00

""" Решение (Андрей Верзун) """

# my_list = [1, 2, 3, 4, 5]
# k = 32 # сдвиг на 2 позиции
# k = k % len(my_list) # сокращение количества итераций при 'k' кратном длине списка 
#                      # если 'k = 31', то понадобиться, только одна итерация,  
#                      # до 30-й итерации, включительно, список будет оставаться прежним, 
#                      # т.к., в данном случае, 30 кратно 5,
#                      # только 31-я итерация измененит список
# while k > 0:
#     temp = my_list.pop() # 'pop' удаляет последний элемент и записывает его в 'temp'
#                          # 'remove(x)' удаляет из списка указанный элемент
#     my_list.insert(0, temp) # 'insert' добавляет элемент влево
#     k -= 1
# print(my_list)

# # Input: [1, 2, 3, 4, 5] k = 2
# # Output: [4, 5, 1, 2, 3] 


# 01:25:50

""" Решение срезами (исправленный вариант)"""

# k = 3
# lst1 = [1, 2, 3, 4, 5]
# print('Input:', lst1, ' k =', k)
# print('Output:', lst1[-k:] + lst1[:-k]) # используя '-k', когда k = 3,
#                                         # '-k:' перемещает каждый элемент, 
#                                         # начиная с последнего, на 3 позиции, при этом
#                                         # ':-k' перемещает элементы из начала списка,
#                                         # 1-й и 2-й без 3-го, до которого не доходит, 
#                                         # на 3 позиции каждый


# 01:27:50

""" Теория """

""" Сергей Сердюк """ 
# # 01:27:50

# d1 = {'ddg':22, (1,5,6): "dfd", 2:2}
# print(d1)

# for i in d1:
#     print(d1[i]) 

# for i in d1.values():
#     print(i) 

# for i,j in d1.items():
#     print(j) 
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
# num_rows = int(input('Number rows: '))
# num_columns = int(input('Number columns: '))

# def print_operation_table(operation, num_rows, num_columns):
#     res = []
#     if num_rows < 2:
#         print('Error!')
#     else:
#         for i in range(1, num_rows + 1):
#             for j in range(1, num_columns + 1):
#                 res.append(operation(i, j))

#             print(*res) # вариант вывода 1
#             res = [] # обнуление списка для каждой новой строки таблицы,
#                      # т.е. каждая строка таблицы - это новый список,
#                      # передаваемый после заполнения в первый "res" (стр.62),
#                      # где и записывается вся таблица до завершения цикла 

#         # for i in range(0, len(res), num_columns):
#         #     print(*res[0 + i: num_columns + i]) # вариант вывода 2

# print_operation_table(lambda x, y: x * y, num_rows, num_columns)


# 00:18:25
''' 
Решение можно было сделать в одну строку (Сердюков):
Пустая строка, куда мы добавляем значения со занком плюс
'''


# 00:19:30
''' 
Задача 2 
'''
# https://autotest.gb.ru/problems/82?lesson_id=391158&_ga=2.55648939.1223630724.1705653773-1736153193.1704617193
'''
Винни Пух

Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, 
насколько легко он их придумывает, Вам стоит написать программу.

Винни-Пух считает, что ритм есть, если число слогов (число гласных букв) 
в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, 
если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.

Стихотворение  Винни-Пух передаст вам автоматически 
в переменную stroka в виде строки. В ответе напишите 
Парам пам-пам, если с ритмом все в порядке и 
Пам парам, если с ритмом не все в порядке.
'''
# P.S. 
# Правильность ритма определяется 
# равным количеством гласных в каждой строке.
# Количество согласных в строке на ритм не влияет.
'''
Если фраза только одна, то ритм определить не получится 
и необходимо вывести: 
"Количество фраз должно быть больше одной!".

Пример
'''
# На входе:
# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

# На выходе:
# Парам пам-пам


'''
Решение

Вариант 1 (Марина Вешинина)
'''

stroka = 'пара-ра-рам тарам-пам-пам па-ра-па-дам'
list_1 = stroka.split(" ")
glasny = ['а','я','о','ё','у','ю','ы','и','э','е']
res = list()

def puh():
    if len(list_1) == 1: return "Фраз должно быть больше одной"
    else:
        for i in list_1: # проход по всему списку list_1
            count = 0 	 # подсчёт, начиная с нуля,
            for j in i:  # для 'j' из множества 'i',
                if j in glasny: # если 'j' - гласный, то 
                    count += 1  # прибавляем в счётчик единицу
            res.append(count) # добавляем 'count' в результат (res)
            
        if len(res) == res.count(res[0]): # 1-й вариант сравнения (уточнить пояснение)
					  # 'res.count' - считаем элементы списка 'res',
					  # начиная с первого элемента 'res[0]',
					  # сравниваем с длиной 'len()' исходника 'res'.
					  # счёт можно начать с любого (?) элемента -
					  # 'res[-1]' или 'res[2]', так как 
					  # в строке определённое число элементов, которые
					  # будут посчитаны полностью, начиная с любого, но
					  # т.к. 1-й элемент есть всегда, начинаем с него
        # if len(set(res)) == 1: # 2-й вариант сравнения
				 # список 'res' переводим в множество 'set'
				 # множество - неупорядоченный тип данных, 
				 # хранящий только уникальные значения
				 # если количество (?) гласных в списках 'res' совпадает,
				 # то множество равно 1, если не совпадает, 0 (нулю)
        # if min == max # 3-й вариант (???)
			          # сравнение минимума и максимума
			          # выяснить, как это можно записать?
            return 'Парам пам-пам'
        return 'Пам парам'
  
print(puh())



# 00:30:00
'''
Решение с помощью генератора списков

Вариант 2
(Сергей Сердюк - Марина Вешинина)
'''

stroka = 'пара-ра-рам тарам-пам-пам па-ра-па-дам'
list_1 = stroka.split(" ")
glasny = ['а','я','о','ё','у','ю','ы','и','э','е']
res = list()

def puh():
    if len(list_1) == 1: return "Фраз должно быть больше одной"
    else:
        for i in list_1:
            res.append(len([j for j in i if j in glasny]))  # генератор списка
								                            # выбор j из i, с условием,
			 					                            # что j - это гласные
            # for j in i: # строка изъята и помещена в генератор списка
            #     if j in glasny: # эта строка тоже в генераторе списка

            # print([j for j in i if j in glasny])     # 'glasny' - вывод гласных
            # print([j for j in i if j not in glasny]) # 'not' - вывод согласных
            # print([j for j in i if j in ""])         # кавычки - вывод: [], при пустом списке
	
        # print(res)  # выводит числом количество гласных в строке -> 4 (четыре гласных), 
		            # при использовании 'len()' в генераторе списка
		            # вывод: [4, 4, 4], т.к. количество гласных в трёх строках одинаковое 
	
    if len(res) == res.count(res[0]):
        return 'Парам пам-пам'
    return 'Пам парам'
    
print(puh())



# 00:50:50

'''
Задача с семинара (см. чат)

Выводится список целых чисел в одну строку через пробел.
Необходимо оставить в нём только двузначные числа.
Реализовать программу с использованием функуции filter (см. 01_(С-07)).
Результат отобразить на экране в виде последовательности
оставшихся чисел в одну строку через пробел.
Задаётся строка цифр '2 4 -23 5 13 897'

Решение с помощью функции высшего порядка
'''

num = '2 9 4 -23 5 13 897 11'

print(*list(filter(lambda x: len(str(abs(int(x)))) == 2, num.split()))) # -23 13 11
							        # str(abs(int(x))) вместо replace()
							        # abs(int(x)) - перевод х в цифру
							        # str() - возврат в строку

print(*list(filter(lambda x: 9 < abs(int(x)) < 100, num.split())))  # решение через диапазон чисел
                                                                    # диапазон от 9 до 100 включает
                                                                    # в себя все двузначные числа

print(*list(filter(lambda x: len(x) == 2, num.split()))) # 13 11 
					 		                             # не выводит отрицательных чисел, т.к.
						                                 # числа вопринимаются, как строки

print(*list(filter(lambda x: len(x.replace('-', '')) == 2, num.split())))
					                                     # filter() - применить оператор
					                                     # lambda x: - функция высшего порядка 
					                                     # split() - разбить 'num' на элементы
					                                     # (x == 2) - выбрать двузначные
					                                     # len(num) - по всей длине строки
					                                     # replace('-', '') - минус заменить пробелом
					                                     # list() - записать в одну строку
					                                     # * (звёздочка) - оставить только пробелы
					                                     # print() - вывод: -23 13 11



# 01:02:30

'''
Работа с файлами

Задача №49. 
Решение в группах

Создать телефонный справочник с
возможностью импорта и экспорта данных в формате .txt. 
Данные, которые должны находиться в файле:
Фамилия, имя, отчество, номер телефона. 

1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик 
для поиска определенной записи (Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной.
'''

# Иванов, Иван, 111, описание Иванова
# Петров,	Петр,	222,	описание Петрова
# Васичкина, Василиса, 333, описание Васичкиной
# Питонов, Антон, 777, умеет в Питон

"""
ДЗ по залдаче

Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, 
и Вы должны реализовать функционал для изменения и удаления данных.
"""


# 01:14:39
'''
Функция записи, хранения и поиска данных телефоных номеров
'''

''' Функция work_with_phonebook '''

def work_with_phonebook():

    choice = show_menu() # обращение к функции show_menu() /см. ниже/
                         # получение данных (выбора (?) /Сердюк/)
    phone_book = read_txt('phonebook.txt')

    while (choice != 7):

        if choice == 1:
            print_result(phone_book) # tkinter - библиотека (скачать)
                                     # Доп. инфа для любопытных от Сердюка
                                     # визуальная часть программы
        elif choice == 2:
            last_name = input('lastname ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('lastname ')
            new_number = input('new number ')
            print(change_number(phone_book, last_name, new_number))

        elif choice == 4:
           last_name = input('lastname ') 
           print(delete_by_lastname(phone_book, last_name))
        elif choice == 5:
            new_number = input('new number ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('new data ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        
        choice = show_menu()


# 01:14:45
''' Функция show_menu '''

def show_menu():
    print("\nВыберите наобходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти обонента по фамилии\n"
          "3. найти обонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить данные\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Закончить работу")
    choice = int(input()) # 'choice' - переменная, принимающая 
                          # значение введённое пользователем и
                          # переводящая его в цифру
    return choice


""" 
Таблица данных (пример)

Таблица в программе (?) должна представлять из себя список кортежей:
[(фамилия, Иванов), (имя, Иван), (телефон, 111), (описание, друг)]
"""

# Иванов, Иван, 111, описание Иванова

# Петров,	Петр,	222,	описание Петрова

# Васичкина, Василиса, 333, описание Васичкиной

# Питонов, Антон, 777, умеет в Питон


# 01:19:15
''' Функция read_txt'''

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', "Имя", "Телефон", "Описание"] # шапка таблицы данных

    with open(filename, 'r', encoding = 'utf-8') as phb: # 'with' - контекстное меню
            # 'filename' - это 'phonebook.txt'           # 'open' можно прописать без 'with', но
            # где запись filename = 'phonebook.txt'???   # тогда оператор закрывают командой.
            # 'r' - режим чтения                         # контестное меню закрытия не требует
            # 'encoding' - кодировка                     # 'open' закрывается при выходе из цикла 
            # 'utf-8' - указание кодировки               # в Pyhton цикл определяют отступы,
            # при использовании кирилицы,                # пока мы внутри отступа, мы в цикле
            # обязательно указывать кодировку            # выход левее его границы - выход из цикла
            # 'as phb' - открываем переменную,           
            # где записан наш файл .txt
            # имя переменной произвольное 
            # (phb, x, file_1 и пр.)

        for line in phb: # 'line' - строка таблицы, где записаны данные, которые мы перебираем

            record = dict(zip(fields, line.split(','))) # создаём словари, которые составят
                    # 'zip()' - функция высшего порядка # список для телефонной книги, т.е.
                    # 'split' делит 'fields' (таблицу)  # телефонная книга - список из словарей
                    # на отдельные строки (line)
                    # строк любое количество
            
            dict(( (фамилия, Иванов), (имя, Точка), (номер, 8928) )) # <- словари: (ключ, значение)
                                                                     # одна строка - 1 человек
                                                                     # в строке несколько словарей

        phone_book.append(record) # запись данных отдельного человека (строки, словаря) в список
    return phone_book # возврат списка


# 01:31:45
''' Функция write_txt '''

def write_txt(filename, phone_book): # функция имеет два значения (имя файла и данные)

    with open(filename, 'w', encoding = 'utf-8') as phout:  # filename, на семинаре, обозначен, как
                                                            # 'phonebook.txt', но в коде переменная
                                                            # filename нигде не принимает строку
                                                            # в виде: filename = 'phonebook.txt'
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values(): # 'v' - значение, которое ищем в наших словарях
                                             # Что такое 'values' код не понимает (не подсвечивает)
                s += v + ','
            phout.write(f'{s[:-1]}\n')  # phout.write - построчная запись
                                        # s[] - срез строки, найденой в результате перебора
                                        # [:-1] - строка без последнего элемента, без запятой
                                        # '\n' - переход на другую строку



work_with_phonebook()

''' 
(см. решение в 'home08.py' (01_ДЗ-08))
'''
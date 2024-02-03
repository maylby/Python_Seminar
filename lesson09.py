# Знакомство с языком Python (семинары)
# Урок 9. Работа с табличными данными
# https://gb.ru/lessons/391160


# 00:20:00
"""
Разбор задачи ДЗ-08 (Телефонный справочник)

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
"""

# Иванов, Иван, 111, описание Иванова
# Петров,	Петр,	222,	описание Петрова
# Васичкина, Василиса, 333, описание Васичкиной
# Питонов, Антон, 777, умеет в Питон

"""
ДЗ по задаче из 01(С-08)

Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, 
и Вы должны реализовать функционал для изменения и удаления данных.

Решение

Вариант 1 (Геннадий Ионов)
"""

"""
Начало кода Геннадия Ионова
"""
from seminar007 import * # импорт функций из файла "seminar007",
			             # где эти функции размещены
			             # посмотреть семинар 7, что на нём было?
			             # прописаны функции(?): 
			             # - защита от ввода в програмный код кирилицы
			             # - перевод в верхний регистр, вводимых пользователем символов

def readFunction(): # функция просмотра и перезаписи
		           # выделил авторский код в отдельный модуль
	# printing = []
	lens = 0
	data = open('Phonebook.txt', 'r+', encoding = 'utf-8') 
	for line in data:
		lens += 1
	data.close()


def actionRequest(Start):
	request = input(
		'What do you what to do''\n1-''Search''\n2-''add''\n3-''delete''\n4-'
		'directory display''\n5-''replacing value''\n6-''???''\n7-''???')

	if request == '1':
		Search = input(
			'plees enter one of the required values:'
			'name, phone-number, surname''\n')

		printing = []
		readFunction()  # Как вызвать функцию, вместо кода ниже, 
				        # Внутри файла и из хранилища функций???
		lens = 0
		data = open('Phonebook.txt', 'r+', encoding = 'utf-8') 	
		for line in data:
			lens += 1
		data.close()
		namePhoneNumberSurname(data, Search, printing, lens) 
		return printing

	elif request == '2':
		Add_value()
	elif request == '3':
		Search = input(
			'enter one of the values,:' 
			'first name, first name, phone-number''\n')
						# тут у автора после 'values' - запятая,
						# а в других местах двоеточие
		printing = []
		lens = 0
		data = open('Phonebook.txt', 'r+', encoding = 'utf-8')
		for line in data:
			lens += 1
		data.close()
		Delete(data, Search, printing, lens) # 'res =' - моя вставка
		return printing

	elif request == '4':
		with open('Phonebook.txt', 'r+', encoding = 'utf-8') as data:
			directory_display(data)
	elif request == '5':
		Search = input(
			'plees enter one of the required values:'
			'name, phone-number, surname''\n') # Как можно переносить часть строки?

		printing = [] # часть кода, отсюда и до "data.close()", 
			      # оформить в отдельную функцию
		lens = 0
		data = open('Phonebook.txt', 'r+', encoding = 'utf-8')
		for line in data:
			lens += 1
		data.close()

		replacement(data, Search, printing, lens) # 'res =' - моя вставка
		return printing

	elif request != 1 and request != 2 and request != 3 and request != 4 and request != 5
			# Почему числа без кавычек? Это же строки?
			# Как записать короче?
	# elif request != '1','2','3','4','5' # <- Так нельзя записать?
	# elif request != '1, 2, 3, 4, 5' # <- Или так?
		question = input('do you wath to try adain?''\n''yes: Y''\n''no: N''\n')
		if question.upper() == 'Y':		
			actionRequest(Start)
		elif question.upper() == 'Y':
			print('Gootbye')
			exit()
		

def Hello(): # точка входа в Телефонную книгу
	hello = input(
		'Welcome to Phone Book''\n''version 0.397(beta)''\n'
		'Woult you like to start working?''\n''yes: Y''\n''no: N''\n') # вывод строки
									       # в консоль
	if hello.upper() == 'Y': 
		Start = False
		actionRequest(Start) 

	elif hello.upper() == 'N':
		print('Gootbye')
		exit()
	else: Restart() # написать 


if '__main__' == __main__:
	Hello() # точка входа - функция "Hello" (см. выше) 
		# из файла приветствия VSCode (?)
		# "Экранирует" повторный вывод приветствия "Hello",
                # который запускается при обращении к программе,
                # одновременно открывая доступ к функциям,
                # размещённым в том же файле хранения, где и 
                # стартовая страница приветствия.
                # При вторичном обращении к файлу хранения,
                # приветствие "Hello" выводится не будет.


'''
Форма и порядок обращения к определённым функциям кода 
в консоле, при реализации запроса на изменение данных
'''
# "Want to replace values?" ("Хотите заменить значения?")

input('yes: Y', ) # yes: Y
input('no: N', ) # no: N


# "Select what you want to replace" ("Выберите, что хотите заменить")
'''
1 - имя (name)
2 - номер телефона (phone number)
3 - фамилия (surname)
'''
# 1 - name
# 2 - phone number
# 3 - surname

input('Number:', ) 


# Ввод в консоль

# surname: Чехов
# name: Антон
# phone number: 8(000)000 00 00 # предусмотреть полуавтоматический 
			      # ввод номера телефона:
			      # - код страны, код оператора (перечни)
			      # - блокироввка ввода любых символов, кроме цифр	

save(...) # запрос на сохранение
	if save == 'Y': 
		write(f()) # (???)
	elif: save == 'N':
		print('Gootbye')
		exit()
	Restart() # (?) функция, вывести отдельным модулем
		
return result # сохранение введённых данных в файле "Phonebook.txt"

# 00:29:00

# Пояснения Сердюка об использовании 

# 'return' - возврат заначения
# 'remove' - метод удаляет конкретный элемента
# 'replace' - заменяет элемент по индексу (размер - срез 64 символа)
# написать методы 'remove', 'replace'
# наверняка, есть вшитые в Pyhton

# 00:31:30

# Вывод в консоль:

# What do you what to do (перевести вопрос)
# 1-Search (поиск)
# 2-add (добавить)
# 3-delete (удалить)
# 4-directory display (отображение каталога)
# 5-replasing value (замена значения)

# 5 # выбор действия (№ - пункт меню)
# поиск по имени
# Антон
# was found Антон | Чехов | 8(000)000 00 00

# Если будет несколько Антонов,
# прога выведет все и попросит,
# ввести уникальный идентификатор (фамилию, телефон)

# Реализация поиска совпадений, путём перебора значений?



# 00:38:00
"""
Запрос на продолжение работы с программой
"""
# "Will you continue to work?" ("Вы продолжите работать?")

input('yes: Y', ) # yes: Y
input('no: N', ) # no: N
# n
# Goodbye



# 00:44:00
"""
Ссылка на сервис google-colab для решения задачи (?)
"""
# https://colab.research.google.com/drive/11udiVDM85HFjqLqDqfz0ef9NLBgHUWn-?pli=1#scrollTo=h0kTGcMNHRnW

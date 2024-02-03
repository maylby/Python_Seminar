# Знакомство с языком Python (семинары)
# Урок 10. Построение графиков
# https://gb.ru/lessons/391161

# 00:17:50

"""
Телфонный справочник (ДЗ-08)

Вариант 2 (Марина Вершинина)
"""
# 00:17:50 (файл lesson10.py)

# list_1 = [('Вершинина','Марина','777'),
# 		  ('Бурков','Евгений','666'),
# 		  ('tttttt','','22222')]
# for i in list_1:
# 	print(*i)


'''
Вход / Выход
'''
def outlog():
	picachu = input('\nПродолжить?\n1-да,\n2-нет\n: ')
	if picachu == '1': 
		start() # функция меню выбора действий (см. внизу)
	elif picachu == '2':
		print('Пока!\n')
		exit() # это вшитая фукция Pyhton?
	else: 
		print('Введена не верная команда')
		outlog()

'''
Поиск
'''
def find_name():
	list_1 = reade() # вывод найденных данных
	name = input('Введите ФИ: ')
	filde = list(filter(lambda x: name in x[0], list_1))
	if len(filde):# != 0:
		for i in filde:
			print(i)
			outlog()
	else:
		nike = input('ФИ нет в списке контактов. Добавить?\n1-да\n2-нет\n: ')
		if nike == '1':
			add_name() # запуск функции "Добавить новый контакт"
		if nike == '2':
			outlog() # возврат на страницу "Входа"
		else:
			print('Введена не верная команда')
			outlog()
# find_name()



'''
Удаление данных
'''
def delete():
	list_1 = reade()
	name = input('Введите ФИ: ')
	len_list_1 = len(list_1)
	rem = []
	for i in list_1:
		if name in i[0]:
			rem.append(i)
	if len(rem) != 0: print(*rem, sep ='\n')		
	if len(rem) == 1:
		list_1.remove(rem[0])
		create(list_1)
		outlog()
	elif len(rem) > 1:
		num = input('Введите номер телефона: ')
		for j in rem:
			if num == j[1]:
				list_1.remove(j)
				create(list_1)
				outlog()
		if len_list_1 == len(list_1):
			print('Нет номера') # Номер удалён?
			outlog()
	else: 
		print('Контакта нет') # Контакт удалён?
		outlog()
		


'''
Редактирование
'''
def redact(): 
	list_1 = reade()
	red = input('Кого редактировать?\n: ')
	find = list(filter(lambda x: red in x[0], list_1))
	if len(find) != 0:
		for i in find: 
			print(i)
	else: 
		print('ФИ нет в контактах')
		outlog()
	if len(find) == 1:
		for i in find: 
			uno = input('Изменить ФИ-1, телефон-2\n: ')
			if uno == '1':
				list_1[list_1.index(i)][0] = input('ФИ: ') 	# Разделить имя и фамилию (?)
			elif uno == '2':
				list_1[list_1.index(j)][1] = input('Телефон: ')
			else: 
				print('Введена неверная команда')
				redact()
# 00:30:29				
	bum = 0
	if len(find) > 1: 
		num = input('Введите номер телефона: ') 
		for j in find: 	
			# print(num, j[1])
			if num == j[1]:
				uno = input('Изменить: ФИ - 1, телефон - 2 ')
				if uno == '1':
					list_1[list_1.index(j)][0] = input('ФИ: ')
				elif uno == '2':
					list_1[list_1.index(j)][1] = input('Телефон: ')
				else:
					print('Введена неверная команда')
					redact()
			else: bum += 1
		if len(find) == bum: 
			print('Такого номера нет')
	create(list_1)
	outlog()	



'''
Добавить новый контакт
'''
def add_name():
    list_1 = reade()
    saves = input('Создать контакт?\nда-1\nнет-2\n ')
    list_2 =[]
    if saves == '1':
        name = input('Введите новое ФИ: ')
        list_2.append(name)
        num = input('Введите номер телефона: ')
        list_2.append(num)
        if len(list(filter(lambda x: list_2 == x, list_1))) > 0:
            print('Такой номер и ФИ уже есть')
        else:
            list_1.append(list_2)
            create(list_1)
            print('Контакт добавлен')
            outlog()
    elif saves == '2':
        outlog()
    else:
        print('Введена неверная команда')
        outlog()
	# print(list_1)


'''
Функция ввода (w), 
(создание новой записи)
'''
def create(list_1):
	listes = list_1
	with open('phonebook.txt','w+', encoding='utf-8') as Phone:
		for i in listes:
			Phone.write(f'{i[0]},{i[1]}\n') # 'i[0]' - ФИ, 'i[1]' - номер
		list_1 += listes
	return list_1 # добавил возврат 'return list_1'
create()


'''
Функция чтения (r)
'''
def reade(): 
	spros = []
	with open('phonebook.txt','r', encoding='utf-8') as Phone:
		for i in Phone.readlines():
			spros.append(i.strip().split(',')) 	# split - разбивает на символы (?)
							   					# strip - обрезает пробелы и '\n',
							   					# т.е. удаляет лишнюю строку 
												# в конце списка и пустые строки
												# не накапливаются при работе кода
												# lsrtip - обрезка пробелов слева
												# rsrtip - обрезка пробелов справа		
	return (spros)
# spros = reade()
print(reade())


'''
Функция начала Start
'''	
def start(): # Код, одновременно со списком пунктов, 
			 # при запуске, выдаёт список контактов
			 # Как исправить?
	
	# data = show_menu() # Вызов функции меню команд кода Сердюка

	data = input("\nКак продолжить?\n1-Показать список контактов\n"
				"2-Hайти контакт\n3-Добавить контакт\n"
				"4-Редактировать контакт\n5-Удалить\n") 
	if data == '1': 
		# reade() 	# прямая ссылка на функцию не работает,
					# список контактов выдаёт, только запись ниже
		spros = reade()
		print(*spros, sep ='\n')
		outlog()
	elif data == '2': 
		find_name()
	elif data == '3': 
		add_name()
	elif data == '4': 
		redact()
	elif data == '5': 
		delete()

	

# def show_menu():
# 	print("\nВыберите наобходимое действие:\n"
#           "1. Отобразить весь справочник\n"
#           "2. Найти обонента по фамилии\n"
#           "3. найти обонента по номеру телефона\n"
#           "4. Добавить абонента в справочник\n"
#           "5. Изменить данные\n"
#           "6. Сохранить справочник в текстовом формате\n"
#           "7. Закончить работу")
# 	data = int(input())
# 	return data


start()


# 00:33:20


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

Вариант 1 (Геннадий ...?)
"""

''' 
Файл размещён в коде автором решения
'''

# if '__main__' == __main__:  # "Экранирует" повторный вывод приветствия "Hello",
#     Hello()                 # который запускается при обращении к программе,
#                             # одновременно открывая доступ к функциям,
#                             # размещённым в том же файле хранения, где и 
#                             # стартовая страница приветствия.
#                             # При вторичном обращении к файлу хранения,
#                             # приветствие "Hello" выводится не будет.


'''
Форма и порядок обращения к определённым функциям программы в консоле
В данном случае, при реализации запроса на изменение данных
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

input('Number:', )  # или реализуется как-то иначе? 
                    # например, кликом о надписи?


# 00:38:00
"""
Запрос на продолжение работы с программой
"""
# "Will you continue to work?" ("Вы продолжите работать?")

input('yes: Y', ) # yes: Y
input('no: N', ) # no: N
# n
# Goodbye


# 00:44:20
"""
Ссылка на сервис google-colab для решения задачи
"""
# https://colab.research.google.com/drive/11udiVDM85HFjqLqDqfz0ef9NLBgHUWn-?pli=1#scrollTo=h0kTGcMNHRnW
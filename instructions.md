# Инструкция по работе со скриптом Python в VSCode и GitHub
https://git-scm.com/doc - документция по git (есть на русском)

_Принципиальных отдичий по работе с Git для скрипта Python нет,
команды стандартные_

## Пуш и коммит скриптом пайтон?

* __git init__ - активация репозитория
* __git add .__ - команда на отслеживание фыайла при первом запуске
* __git commit -m "first commit"__ - сохранение изменений

* __git remote add origin git@github.com:username/name_project.git__ - адрес удаленного сервера, где будет храниться "главная копия" нашего репозитория

### Бибилиотека **os** позволяет использовать следующий синтаксис:

* import os

* os.system("git add .")
* os.system(f'git commit -m "{commit_name}"')
* os.system("git push") 

* __git push -u origin master__ - отправка файла на внешний репозиторий

### Сценарий №2
_Клонирование удалённого репозитория на локальный ПК_

* __git clone git@github.com:username/name_project.git__
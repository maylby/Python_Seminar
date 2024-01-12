# Файл хранения функций


""" Функция создания случайного списка """
# Взято здесь:
# https://ru.stackoverflow.com/questions/565846

''' Вариант 1.1 '''

from random import randint

numbers = []
for i in range(20):
    numbers.append(randint(-10, 10))


''' Вариант 1.2 '''

from random import randint
lst = [randint(-10, 10) for i in range(20)]


''' Вариант 2 '''

import timeit, random, itertools, operator, functools, numpy # 'numpy' - что это?

a, b, s = -10, 10, 1000
v1=lambda: list(numpy.random.randint(a, b, s)) # (???) "random.randint" Pyhton не определяет
v2=lambda: [random.randint(a, b) for _ in range(s)]
v3=lambda: list(map(lambda _: random.randint(a, b), range(s)))
v4=lambda: list(itertools.starmap(lambda: random.randint(a, b), [()]*s))
v5=lambda: list(r(a, b) for r in [random.randint]*s)
v6=lambda: [r() for r in [functools.partial(random.randint, a, b)]*s]
v7=lambda: list(operator.methodcaller('__call__', a, b)(r) for r in [random.randint]*s)
v8=lambda: list(map(operator.methodcaller('__call__', a, b), [random.randint]*s))
v9=lambda: list(map(operator.methodcaller('__call__'), [functools.partial(random.randint, a, b)]*s))
v10=lambda: numpy.random.randint(a, b, s).tolist()

def execTime(target_: list, repeat=1):
    for n, fn in target_: print(n, timeit.Timer(fn).timeit(1), fn())
    target_[:] = [(n, timeit.Timer(fn).timeit(repeat)) for n, fn in target_]
    for e, (n, tmt) in enumerate(sorted(target_, key=lambda r: r[1]), start=1):
        print("{}'time {} {}".format(e, n, tmt))

if __name__ == '__main__':
    target = [(n, fn) for n, fn in sorted(globals().items()) if n.startswith('v')]
    execTime(target, repeat=100)

# out:

#     v1 0.00013895335493526386 [8, 6, 8,..]
#     ...
#     v9 0.0034144395633564986 [-8, 3, -3,..]
#     1'time v10 0.005898359039140072
#     2'time v1 0.014917592744244368
#     3'time v5 0.32350102439781625
#     4'time v2 0.33059889747340865
#     5'time v4 0.3355538953844154
#     6'time v8 0.34316236373969566
#     7'time v3 0.3506998448115352
#     8'time v6 0.3632192647513499
#     9'time v9 0.3795784125105248
#     10'time v7 0.4123779585340184
    
''' 
P.S. 
'''
map() # не возвращает список в Питоне 3. 
      # Для переносимости лучше использовать: 
[randint(-10, 10) for _ in range(20)] # Замена 'i' на '_' (подчёркивание)                                    
                                      # - принятое соглашение в Питоне. 

# у NumPy есть встроенный метод для конвертирования 
# 'array' в 'list' - 'array.tolist()'. 
# Заменить: 
list(numpy.random.randint(a, b, s)) # (?)'random.randint' опять не определяется, как оператор
# ->
numpy.random.randint(a, b, s).tolist()  # должно быть в 1.5-2 раза быстрее 
                                        # для такого к-ва элементов...

''' Вариант 3 '''


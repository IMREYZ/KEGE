# Шаблон для 2 задания (1)

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ... # Выражение
                if f == ...: # 0 или 1
                    print(x, y, z, w)




# Шаблон для 2 задания (2)

from itertools import *

def f(x, y, z, w):
    return ... # Выражение

# Сколько пропусков, столько и букв
for a, b, c, d, e in product([0, 1], repeat=5):
    table = [(a, 0, 1, 0), (0, b, c, 0), (d, 1, 1, e)]

    if len(table) == len(set(table)): # Если строки не повтояются
        for p in permutations('xyzw'): # Все перестановки x y z w
            result = [f(**dict(zip(p, row))) for row in table] 
            if result == [0, 0, 0]: # Результаты столбцов
                print(''.join(p))

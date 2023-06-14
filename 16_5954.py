# 1) Пробуем запустить
# 2) sys.setrec(10000000)
# 3) functools, @lru_cache(None), и потом цикл в +1 прогрессия, если не работает, то -1

from sys import *
setrecursionlimit(1000000)

def f(n):
    return 1 if n == 1 else n * f(n - 1)

print((f(2023) - f(2022)) / f(2020))



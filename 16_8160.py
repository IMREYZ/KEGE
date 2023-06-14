# 1) Пробуем запустить
# 2) sys.setrec(10000000)
# 3) @lru_cache(None), и потом цикл в нужном порядке

from sys import *
setrecursionlimit(10000000)

def f(n):
    if n > 3000: return n
    if n % 2 == 0: return n + f(n + 1) + 1
    return f(n + 2) + 2

print(f(40) - f(43))
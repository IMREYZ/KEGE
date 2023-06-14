# 1) Пробуем запустить
# 2) sys.setrec(10000000)
# 3) @lru_cache(None), и потом цикл в +1 прогрессия, если не работает, то -1


from functools import *

@lru_cache(None)
def f(n):
    if n == 1: return 3
    if n % 2 == 0: return f(n - 1) + 5*(n-1)
    return f(n-1) + 7

for i in range(1, 9000):
    f(i)

print(f(8765))
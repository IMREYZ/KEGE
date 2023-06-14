def f(x, y, a):
    return x + y <= 32 or y <= x + 4 or y >= a

for A in range(100_000):
    if all(f(x, y, A) == 1 for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
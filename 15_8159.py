def f(x, y, a):
    return (2*x + y != 150) or (not(50 <= x <= 70)) or (a > y)

for A in range(100_000):
    if all(f(x, y, A) == 1 for x in range(10000) for y in range(10000)):
        print(A)
        break
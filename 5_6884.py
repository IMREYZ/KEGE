m = 10 ** 20

for N in range(1, 1000):
    b = bin(N)[2:]

    if N % 2 == 0:
        b = '1' + b + '0'
    else:
        b = '11' + b + '11'

    R = int(b, 2)
    if R > 225:
        m = min(R, m)

print(m)



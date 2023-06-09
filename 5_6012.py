for N in range(1, 10000):
    b = bin(N)[2:]

    su = b.count('1')
    if su % 2 == 0:
        b = '1' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'

    R = int(b, 2)
    if 49 < R < 52:
        print(N, R)











for N in range(1, 10000):
    b = bin(N)[2:]

    su = b.count('1')
    if su % 2 == 0:
        b = '101' + b[3:] + '0'
    else:
        b = '10' + b[2:] + '11'

    R = int(b, 2)
    if R > 68:
        print(N)
        break
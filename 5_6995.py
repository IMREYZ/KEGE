for N in range(1, 10000):
    b = bin(N)[2:]

    last = b[-1]
    if last == '1':
        b = b[:-1] + '0'
    else:
        b = b[:-1] + '1'


    su2 = str(b.count('1') % 2)
    b += su2

    R = int(b, 2)
    if 85 > R > 78:
        print(N, R)










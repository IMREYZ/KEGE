for N in range(1, 10000):
    b = bin(N)[2:]

    if N % 2 == 0:
        b = '10' + b + '10'
    else:
        b = '1' + b + '00'

    R = int(b, 2)
    if 120 > R > 100:
        print(R)






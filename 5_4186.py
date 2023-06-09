for N in range(1, 10000):
    b = bin(N)[2:]

    if N % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'

    R = int(b, 2)
    if R > 441:
        print(N)
        break



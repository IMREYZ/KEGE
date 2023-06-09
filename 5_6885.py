for N in range(1, 10000):
    b = bin(N)[2:]

    if N % 2 == 0:
        b = '1' + b + '00'
    else:
        # su = sum(int(x) for x in b) Сумма всех цифр для 10 СС
        su = b.count('1')
        b += bin(su)[2:]

    R = int(b, 2)
    if 190 < R < 200:
        print(N, R)



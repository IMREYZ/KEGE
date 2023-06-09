for N in range(1, 10000):
    b = bin(N)[2:]

    b = b.replace('0', '2').replace('1', '0').replace('2', '1')

    b = '1' + b

    su = b.count('1')
    if su % 2 == 1:
        b += '1'
    else:
        b += '0'

    #b += str(b.count('1') % 2)
    R = int(b, 2)
    if R > 180:
        print(N)
        break










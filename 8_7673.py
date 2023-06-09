from itertools import *

count = 1

for s in product('ГЕЭ023', repeat=7):
    s = ''.join(s)

    if s == 'ЕГЭ2023':
        first = count

    if s == '2023ЕГЭ':
        second = count

    count += 1

print(abs(first - second) - 1)

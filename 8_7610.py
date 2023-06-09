from itertools import *

count = 1

for s in product('АКЛМНЯ', repeat=5):
    s = ''.join(s)

    if s[:2] == 'КМ':
        print(count)
        break

    count += 1

print(int('13000', 6) + 1)
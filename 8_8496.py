from itertools import *

count = 1

for s in product('АВОРТ', repeat=6):
    s = ''.join(s)

    if s == 'ВОРОТА':
        print(count)

    count += 1

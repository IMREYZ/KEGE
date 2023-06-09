from itertools import *

count = 1

for s in product('АВЛОР', repeat=4):
    s = ''.join(s)

    if s[0] == 'Л':
        print(count)
        break

    count += 1


print(int('2000', 5) + 1)
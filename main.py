from itertools import *

count = 0

for s in product('012345', repeat=6):
    s = ''.join(s)

    ban = ['12', '21', '32', '23', '52', '25']
    if s[0] != '0' and s.count('2') == 1:
        if all((x not in s) for x in ban):
            count += 1

print(count)



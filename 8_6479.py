from itertools import *

count = 0

for s in permutations('КАРПЫ', 5):
    s = ''.join(s)
    ban = ['АА', 'ЫА', 'АЫ', 'ЫЫ']

    if all(x not in s for x in ban):
        if s[0] != 'Р' and s[-1] != 'Р':
            count += 1

print(count)

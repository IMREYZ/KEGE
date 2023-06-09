from itertools import *

count = 1

for s in product('АЙКОС', repeat=5):
    s = ''.join(s)

    if s.count('О') <= 1 and 'CC' not in s:
        ans = count


    count += 1

print(ans)
print(int('43424', 5) + 1)

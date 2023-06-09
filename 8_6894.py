from itertools import *

count = 1

for s in product('АЛПЦЯ', repeat=5):
    s = ''.join(s)

    if s.count('А') <= 1 and s.count('Ц') == 2 and s.count('Л') == 0:
        print(count)
        break

    count += 1

print(int('02233', 5) + 1)
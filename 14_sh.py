#СС <= 16
for x in '0123456789ABC':
    a = int(f'753{x}2', 13) + int(f'2{x}173', 13)
    if a % 12 == 0:
        print(a // 12)
        break


#17 <= СС <= 36
from string import *
for x in (digits + ascii_uppercase)[:17]:
    a = int(f'9759{x}', 17) + int(f'3{x}108', 17)
    if a % 11 == 0:
        print(a // 11)
        break


#36 > (1 Способ)
for x in range(67):
    a1 = 1 * 81**0 + 2 * 81**1 + x * 81**2 + 3 * 81**3
    a2 = 4 * 67**0 + x * 67**1 + 7 * 67**2 + 1 * 67**3
    a = a1 + a2
    if a % 35 == 0:
        print(a // 35)

# 36 > (2 Способ)
def f(a, cc): # fromCCto10([1, 1, 1, 0], 2) -> 14
    return sum(a[i] * cc ** (len(a) - 1 - i) for i in range(len(a)))

for x in range(111):
    a = f([x, 3, 2, 1], 111) + f([1, 7, x, 4], 211)
    if a % 111 == 0:
        print(a // 111)

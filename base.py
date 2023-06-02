# Функция, которая проверяет число на простоту
def isProst(a):
    return all(a % i != 0 for i in range(2, int(a**0.5) + 1))


# Считывание строк чисел (17 задание)
#a = [int(x) for x in open('name.txt')]


# Считывание строк нескольких чисел (9 задание)
# a = [[int(s) for s in x.split()] for x in open('name.txt')]

# Считывание строк нескольких чисел (22 задание)
def f(i):
    if a[i][1] == 0: return a[i][0]
    else: return a[i][0] + max(f(x) for x in a[i][1:])

a = {}
array = [[int(x) for x in line.replace(';', ' ').split()] for line in open('q.txt')]

for line in array:
    a[line[0]] = line[1:]

print(max(f(i) for i in a.keys()))

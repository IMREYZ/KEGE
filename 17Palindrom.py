a = [int(x) for x in open('17.txt')]
ans = []

def isPalindom(n):
    n = str(abs(n))
    return n == n[::-1]

def is3(n):
    return 100 <= abs(n) <= 999

m = len([x for x in a if is3(x) and isPalindom(x)])



for i in range(len(a) - 1):
    if (a[i] % 2 == 0 and is3(a[i])) + (a[i + 1] % 2 == 0 and is3(a[i + 1])) == 1:
        if a[i] + a[i + 1] >= m:
            ans += [a[i] * a[i + 1]]

print(len(ans), max(x for x in ans if x % 7 == 0))
def isProst(a):
    return all(a % i != 0 for i in range(2, int(a**0.5) + 1))

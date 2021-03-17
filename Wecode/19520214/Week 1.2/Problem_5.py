from math import gcd

n = int(input())

for i in range(n):
    a, b = [int(x) for x in input().split()]
    ucln = gcd(a, b)
    if (b // ucln == 1):
        print(a // ucln)
    else:
        print(a // ucln, b // ucln)
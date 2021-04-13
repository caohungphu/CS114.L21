import math
t = int(input())
for i in range(t):
    n = int(input())
    res = 0
    if n==2:
        res = 2
    elif n%2==0:
        res = 0
    else:
        res = 1
    print(res)
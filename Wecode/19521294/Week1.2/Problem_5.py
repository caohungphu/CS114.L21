import math
n = int(input())

for i in range(n):
    x = input()
    x = x.split()
    a = int(x[0])
    b = int(x[1])
    uc = math.gcd(a,b)
    a = (a//uc)
    b = (b//uc)
    if(b==1):
        print(a)
    else:
        print(a,b)
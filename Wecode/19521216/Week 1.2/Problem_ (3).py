import math
n = int(input())
resultTu = []
resultMau = []
for i in range (0,n):
    tu,mau = [int(x) for x in input().split()]
    ucln = math.gcd(tu,mau)
    if(ucln==1):
        resultTu.append(tu)
        resultMau.append(mau)
    else:
        resultTu.append(tu//ucln)
        resultMau.append(mau//ucln)
for i in range (0,n):
    if(resultMau[i]>1):
        print(int(resultTu[i]),int(resultMau[i]))
    else:
        print(int(resultTu[i]))
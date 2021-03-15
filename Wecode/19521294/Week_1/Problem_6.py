from decimal import *
getcontext().prec = 6
f = float(input())
c = Decimal((f-32)/1.8)
k = Decimal((f-32)/1.8 + 273.15)
print(c.normalize(), k.normalize())
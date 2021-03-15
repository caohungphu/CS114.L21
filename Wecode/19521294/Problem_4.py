from decimal import *
getcontext().prec = 6
a = float(input())
res = Decimal((a*0.453592)/(2.54*2.54))
print(res.normalize())
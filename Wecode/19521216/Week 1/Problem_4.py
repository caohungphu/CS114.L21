from decimal import *
getcontext().prec = 6
f = float(input())
c = (f-32)*(5/9)
k = (f + 459.67)*(5/9)
print(Decimal(c).normalize(),Decimal(k).normalize())
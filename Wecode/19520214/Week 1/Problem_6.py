from decimal import *

f = Decimal(input())
c = (f - Decimal(32)) / Decimal(1.8)
k = c + Decimal(273.15)

getcontext().prec = 6

print(c.normalize(), k.normalize())
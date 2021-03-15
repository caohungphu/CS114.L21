from decimal import *

psi = float(input())
kgscm = (psi * 0.453592)/(2.54*2.54)
getcontext().prec = 6

print(Decimal(kgscm).normalize())
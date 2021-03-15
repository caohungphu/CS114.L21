from decimal import *
getcontext().prec=6
psi = float(input())
kgcm2=0.453592/(2.54**2)
print(Decimal(psi*kgcm2).normalize())
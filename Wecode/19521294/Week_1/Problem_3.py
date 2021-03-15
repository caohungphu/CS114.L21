import math
from decimal import *
getcontext().prec = 3
a = float(input()) 
b = float(input()) 
c = float(input()) 
if (a>=b+c) or (b>=a+c) or (c>=a+b):
    print ("Khong phai tam giac")
else:
    p = (a+b+c)/2
    s = Decimal(math.sqrt(p*(p-a)*(p-b)*(p-c)))
    if (a*a==b*b+c*c) or(b*b==a*a+c*c) or (c*c==a*a+b*b):
        print('Tam giac vuong, dien tich =', s.normalize())
    elif (a==b) and (b==c):
        print('Tam giac deu, dien tich =', s.normalize())
    elif (a==b) or (a==c) or(b==c):
        print('Tam giac can, dien tich =', s.normalize())
    else: 
        print('Tam giac thuong, dien tich =', s.normalize())
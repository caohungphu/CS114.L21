from decimal import *

a = int(input())
b = int(input())
c = int(input())
def TriangleArea(x,y,z):
    p = (x + y +z )/2
    return (p*(p-x)*(p-y)*(p-z))**0.5
getcontext().prec = 3
area = Decimal(TriangleArea(a,b,c))/Decimal(1)
if ((a+b) > c and (b+c)>a and (a+c)>b) and (a*b*c>0) :
    if ((a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b)):     
        print ("Tam giac vuong",end="")
    elif a==b and a==c:
        print ("Tam giac deu",end="")
    elif (a==b or b==c or a==c):
        print ("Tam giac can",end="")
    else:
        print ("Tam giac thuong",end="")
    print(", dien tich = ",area.normalize())
else:
    print("Khong phai tam giac",end="")
from  math import sqrt

a = int(input())
b = int(input())
c = int(input())

if a<b+c and b<a+c and c<a+b:
    p = (a+b+c)/2
    s = round(sqrt(p*(p-a)*(p-b)*(p-c)), 2)
    if s == int(s):
        s = int(s)
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c== a*a+b*b:
        print("Tam giac vuong, dien tich = {}".format(s))
    elif a==b==c:
        print("Tam giac deu, dien tich = {}".format(s))
    elif a==b or b==c or a==c:
        print("Tam giac can, dien tich = {}".format(s))
    else:
        print("Tam giac thuong, dien tich = {}".format(s))
else:
    print("Khong phai tam giac")
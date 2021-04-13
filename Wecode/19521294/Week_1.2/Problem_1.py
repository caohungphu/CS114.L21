t = int(input())
z=t
scs = 0
while t/10>0:
    scs += 1
    t = int(t/10)
x = pow(10,scs-1)
t = z
res = 0
while (t/x)>=1:
    y = int(t/x)
    res += pow(y,scs)
    t = t%x
    x = x/10
if res==z:
    print("True")
else:
    print("False")

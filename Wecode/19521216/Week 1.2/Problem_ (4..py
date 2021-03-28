x,y,z = [int(x) for x in input().split()]
S = x * y
Sz = z*z
x1,y1 = 0,0
gach = 0
if x% z == 0 and y %z==0:
    print(int(S/Sz))
else:
    if x%z ==0 and y % z!=0:
        x1 = x
        y1 = (y//z)*z + z
    elif y%z==0 and x%z!=0:
        x1 = (x//z)*z + z
        y1 = y
    else:
        x1=(x//z)*z + z
        y1=(y//z)*z + z
    gach = int((x1*y1)/(Sz))
    print(gach)
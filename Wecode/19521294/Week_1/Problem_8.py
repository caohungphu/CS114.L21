n = int(input())
k = int(input())
p = int(input())
q = int(input())
if (p*2+q-2-k)>0:
    if(k%2==0):
        u = round(p-k/2)
        v = q
    elif q==1:
        u = round(p-k/2)
        v = 2
    else:
        u = round(p-k/2+0.5)
        v = 1 
    print(u,v)
elif (p*2+q-2+k)<=n:  
    if(k%2==0):
        u = round(p+k/2)
        v = q
    elif q==1:
        u = round(p+k/2-0.5)
        v = 2
    else:
        u = round(p+k/2+0.5)
        v = 1 
    print(u,v)
else:
    print(-1)
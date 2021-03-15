k,t = [int(x) for x in input().split()]
if t%(2*k)==0 :
    print(0)
elif t%k==0:
    print(k)
elif t%k!=0 and (t//k)%2 ==0   :
    print(t%k)
else:
    print(k-t%k)
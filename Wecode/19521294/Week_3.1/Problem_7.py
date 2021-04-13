import sys
input = sys.stdin.readline
def countk(k,n):
    lenk = len(k)
    lenn = len(n)
    intk = int(k)
    intn = int(n)
    count = 0
    if lenn == lenk:
        if intn-intk>=0:
            count =1
    else:
        x = intn - int(n[-lenk:])
        y = pow(10,len(k))
        if intn // x > 0:
            count = (x // y) 
        y = int(n[-lenk:])
        if y-intk >= 0:
            count += 1
    print(count)
nk = sys.stdin.readline().strip().split(" ")

countk(nk[0],nk[1])
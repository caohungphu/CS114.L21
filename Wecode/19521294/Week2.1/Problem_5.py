import sys
input = sys.stdin.readline
mn=sys.stdin.readline().strip().split(" ")
m = int(mn[0])
n = int(mn[1])
rc=sys.stdin.readline().strip().split(" ")
row = int(rc[0])
column = int(rc[1])
arr = []
res = []
if m*n==row*column:
    tmp = column
    for i in range(m):
        arr.extend(sys.stdin.readline().strip().split(" "))
        if column > n:
            if tmp > n:
                res += arr
                tmp -= n
            elif tmp < n:
                res += arr[0:n-tmp]
                ttt = n-tmp
                sys.stdout.write(' '.join(map(str, res))+"\n")
                res = arr[n-tmp:n]
                tmp = column - ttt
            else:
                res += arr
                tmp = column
                sys.stdout.write(' '.join(map(str, res))+"\n")
                res = []   
        elif column < n:
            while tmp <= n:
                if res == []:
                    sys.stdout.write(' '.join(map(str, arr[tmp-column:tmp]))+"\n")
                    tmp += column
                    res = []
                else:
                    res += arr[0:tmp]
                    sys.stdout.write(' '.join(map(str, res))+"\n")
                    res =[]
                    tmp += column
            if tmp - column < n:
                res = arr[tmp-column:n]
                tmp = n-(tmp-column)
        else:
            sys.stdout.write(' '.join(map(str, arr))+"\n")   
        arr = []     
else:
    for i in range(m):
        arr.extend(sys.stdin.readline().strip().split(" "))
        sys.stdout.write(' '.join(map(str, arr))+"\n")
        arr = []
import sys
input = sys.stdin.readline
row,column=map(int,input().split())
arr = []
for i in range(row):
    arr.append([int(j) for j in input().split()])
top,left,bot,right=map(int,input().split())
tmp = []
for i in range(column):
    tmp.append(0)
for i in range(row):
    if i<top or i>bot:
        arr[i] = tmp
    else:
        for j in range(column):
            if j<left or j>right:
                arr[i][j] = 0
for i in range(row):
    sys.stdout.write(' '.join(map(str, arr[i]))+"\n")
from sys import stdin,stdout
input = stdin.readline
def printMatrix(matrix,n,m,tren,trai,phai,duoi):
    for i in range (0,n):
        if i < tren or i > duoi:
            matrix[i] = arr_tmp
        for j in range(0,m):
            if j<trai or j>phai:
                matrix[i][j] = 0    
    for i in range(0,n):
        print(' '.join(map(str,matrix[i]))+"\n")   
n,m = map(int,input().split())
l_ = []
arr_tmp = []
for i in range(0,n):
    l_.append([int(j) for j in input().split()])
for i in range(0,m):
    arr_tmp.append(0)
t,l,b,r= map(int,input().split())
printMatrix(l_,n, m,t, l, r, b)
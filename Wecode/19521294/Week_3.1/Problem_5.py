from sys import *
n,m = [int(x) for x in stdin.readline().split()]
a = []
maxlen = [0]*m
for i in range(n):
    s = [int(x) for x in stdin.readline().split()]
    a.append(s)
for i in range(n):
    for j in range(m):
        a[i][j] = str(a[i][j])
        maxlen[j] = max(len(a[i][j]),maxlen[j])
for i in range(n):
    for j in range(m):
        stdout.write(str(a[i][j]).rjust(maxlen[j]," "))
        if j < m-1:
            stdout.write(" ")
        else:
            stdout.write("\n")
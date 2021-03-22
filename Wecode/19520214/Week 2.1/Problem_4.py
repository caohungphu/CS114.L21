n, m = [int(x) for x in input().split()]

f = []

for row in range(n):
    f.append(list(input().split()))
     
a, b, x, y = [int(x) for x in input().split()]

f2 = [[0 for i in range(m)] for j in range(n)] 

for i in range(a, x + 1):
    for j in range(b, y + 1):
        f2[i][j] = f[i][j]

for i in range(n):
    print(*f2[i], end="\n")

from sys import stdin, stdout

n, m = [int(x) for x in stdin.readline().split()]

a = []
max_length = [0] * m

for i in range(n):
    s = [int(x) for x in input().split()]  
    for j in range(m):
        str_i = str(s[j])
        max_length[j] = max(len(str_i), max_length[j])
    a.append(s)

for i in range(n):
    for j in range(m):
        stdout.write(str(a[i][j]).rjust(max_length[j], " "))
        if j < m - 1:
            stdout.write(" ")
        else:
            if i < n - 1:
                stdout.write("\n")
        
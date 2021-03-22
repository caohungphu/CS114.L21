from sys import stdin, stdout

n, m = [int(x) for x in stdin.readline().split()]
n2, m2 = [int(x) for x in stdin.readline().split()]

if ((n * m) != (n2 * m2)):
    for i in range(n):
        print(input())
else:
    s = []
    for i in range(n):
        s = s + input().split()
        while len(s) >= m2:
            stdout.write(" ".join(s[:m2]))
            stdout.write("\n")
            s = s[m2:]
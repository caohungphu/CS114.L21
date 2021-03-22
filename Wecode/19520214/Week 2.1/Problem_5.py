from sys import stdin, stdout

n, m = [int(x) for x in stdin.readline().split()]
n2, m2 = [int(x) for x in stdin.readline().split()]

def printString(s, k):
    while s.count(' ') >= k - 1:
        f = s.split(' ', k)
        new_list = f[:k]
        stdout.write(" ".join(new_list))
        stdout.write("\n")
        if s.count(' ') < k - 1:
            s = f[k - 1]
        elif s.count(' ') > k - 1:
            s = f[k]
        else:
            s = ""
    return s

if ((n * m) != (n2 * m2)):
    for i in range(n):
        print(input())
else:
    tmp = ""
    for i in range(n):
        s = input()
        if len(tmp) != 0:
            s = tmp + " " + s
        tmp = printString(s, m2)
    if len(tmp) != 0:
        printString(tmp, m2)
            
        
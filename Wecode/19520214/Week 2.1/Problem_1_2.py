from sys import stdin, stdout

n = int(stdin.readline())
a = list([int(x) for x in stdin.readline().split()])
k, x = [int(x) for x in stdin.readline().split()]

def findNums(a, k, x):
    i, j = 0, len(a) - k
    while i < j:
        mid = (i + j) // 2
        if x - a[mid] > a[mid + k] - x:
            i = mid + 1
        else:
            j = mid
    return a[i:i+k]

stdout.write(" ".join(str(x) for x in findNums(a, k, x)))

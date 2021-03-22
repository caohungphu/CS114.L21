from sys import stdin, stdout
import bisect

n = int(stdin.readline())
a = list([int(x) for x in stdin.readline().split()])
k, x = [int(x) for x in stdin.readline().split()]

def findNums(a, k, x):
    i = bisect.bisect_left(a, x)
    left, right = i-1, i
    while k:
        if right >= len(a) or (left >= 0 and x-a[left] <= a[right]-x):
            left -= 1
        else:
            right += 1
        k -= 1
    return a[left+1:right]

result = findNums(a, k, x)

stdout.write(" ".join(str(x) for x in result))

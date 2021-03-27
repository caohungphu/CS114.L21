from sys import stdin, stdout
from bisect import bisect_left

n = int(stdin.readline())
a = [int(x) for x in stdin.readline().split()]

def findNums(a, k, x):
    i = bisect_left(a, x, 0, len(a) - 1)
    left = max(0, i - k + 1)
    right = left + k - 1
    while (right + 1) < len(a) and a[right + 1] - x < x - a[left]:
        left += 1
        right += 1
    print(a[left], a[right])

try:
    while True:
        k, x = [int(x) for x in stdin.readline().split()]
        findNums(a, k, x)

except:
    exit() 
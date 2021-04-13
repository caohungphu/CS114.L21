import math
q = int(input())
for i in range(q):
    n = int(input())
    arr = input()
    arr = arr.split()
    res = 0
    for i in range(n):
        res += int(arr[i])
    print(math.ceil(res/n))
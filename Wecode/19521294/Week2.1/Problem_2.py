import sys
input = sys.stdin.readline
res = []
while 1:
    arr = list(map(int, input().split()))
    if arr[0] == 6:
        break
    elif arr[0] == 0:
        res.insert(0, arr[1])
    elif arr[0] == 1:
        res.append(arr[1])
    elif arr[0] == 2:
        if arr[1] not in res:
            res.insert(0,arr[2])
        else:
            ind = res.index(arr[1]) + 1
            res.insert(ind, arr[2])
    elif arr[0] == 3:
        if arr[1] in res:
            res.remove(arr[1])
    elif arr[0] == 4:
        if arr[1] in res:
            res = list(filter(lambda a: a != arr[1], res))
    elif arr[0] == 5:
        if res != []:
            del res[0]
sys.stdout.write(' '.join(map(str, res))+"\n")
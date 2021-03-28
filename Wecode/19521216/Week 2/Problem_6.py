from sys import stdin
input = stdin.readline
arr =[]   
while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        arr.insert(0,s[1])
    elif s[0] == 1:
        arr.append(s[1])
    elif s[0] == 2:
        if s[1] not in arr:
            arr.insert(0,s[2])
        else:
            x = arr.index(s[1])
            arr.insert(x+1,s[2])
    elif s[0]== 3:
        if s[1] in arr:
            arr.remove(s[1])
    elif s[0] == 4:
        arr = [x for x in arr if x != s[1]]
    elif s[0] == 5:
        if len(arr)!=0:
            del arr[0]
    elif s[0] == 6:
        break
if len(arr) == 0:
    print("blank")
else:
    print(*arr,end=' ')
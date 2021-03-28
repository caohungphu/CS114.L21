from bisect import bisect_left 
n = int(input())
arr = []
arr.extend([int(x) for x in input().split()])
k,x = [int(x) for x in input().split()]
lenght= len(arr) -1
i =1
if x > arr[lenght]:
    print(*arr[lenght-k+1:lenght+1], sep=" ")
elif x < arr[0]:
    print(*arr[0:k], sep=" ")
else:
    vt = bisect_left(arr, x)
    trai = vt - 1
    phai = vt + 1
    while i<k :
        if trai <0:
            print(*arr[0:k],sep=' ')
            i=k
        elif phai > lenght:
            print(*arr[-lenght:],sep=' ')
            i=k
        else:
            if arr[phai] - x >= x - arr[trai]:
                trai -= 1
            else:
                phai += 1
            i+=1
            if i==k:
                print(*arr[trai+1:phai],sep=' ')
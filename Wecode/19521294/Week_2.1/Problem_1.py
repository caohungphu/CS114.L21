from bisect import bisect_left
def fivenumber(array, number, mid, k):
    bigger = mid + 1
    a = k
    while k > 0:
        if mid < 0:
            res = array[0:a]
            return res
        elif bigger > len(array)-1:
            res = array[-a:]
            return res
        else:
            if array[bigger] - number >= number - array[mid]:
                k -= 1
                mid -= 1          
            else:
                if k == 1:
                    mid += 1
                k -= 1           
                bigger +=1

    res = array[mid:bigger]
    return res
length = int(input())
arr = list(map(int, input().split()))
k,number=map(int,input().split())
if number > arr[length-1]:
    res = []
    t = k
    while t > 0:
        res.append(arr[length-t])
        t -= 1
    print(*res, sep=" ")
elif number < arr[0]:
    res = []
    for i in range(k):
        res.append(arr[i])
    print(*res, sep=" ")
else:
    mid = bisect_left(arr,number) - 1
    res = fivenumber(arr,number,mid,k)
    print(*res, sep=" ")

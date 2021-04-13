from bisect import bisect_left
import sys
input = sys.stdin.readline
def fivenumber(array, number, mid, k):
    bigger = mid + 1
    a = k-1
    while k > 0:
        if mid < 0:
            print(array[0],array[a])
            return 
        elif bigger > len(array)-1:
            print(array[-(a+1)],array[-1])
            return 
        else:
            if (array[bigger] - number) >= (number - array[mid]):
                if k!= 1:
                    mid -= 1
                k -= 1          
            else:
                if k == 1:
                    mid += 1
                k -= 1           
                bigger +=1

    print(array[mid],array[bigger-1])
length = int(input())
arr = list(map(int, input().split()))
knumber = []
while 1:
    knumber = list(map(int, input().split()))
    if knumber == []:
        break
    else:
        k = (knumber[0])
        number = (knumber[1])
        mid = bisect_left(arr,number) 
        fivenumber(arr,number,mid,k)

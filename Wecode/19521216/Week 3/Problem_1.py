from bisect import bisect_left
from sys import stdin
input = stdin.readline
n = int(input())
arr = []
arr= list([int(x) for x in input().split()])
length= len(arr)
list_input =[] 
try:
    while True:    
        k,x = [int(x) for x in input().split()]
        vt = bisect_left(arr,x) 
        trai = vt
        phai = vt + 1
        so = k -1
        while k>0 :
            if  trai <0:
                trai = 0
                phai = so +1
                break
            elif phai > length -1:
                trai = -(so+1)
                phai = 0
                break
            else:
                if   (arr[phai] - x >= x - arr[trai]):
                    if k!= 1:
                       trai -= 1
                    k -= 1
                else:
                    if k ==1:
                       trai += 1
                       
                    phai+=1
                    k-=1
                
        print(arr[trai],arr[phai-1]) 
except:
    exit()
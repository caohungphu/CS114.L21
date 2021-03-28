n,m = [int(x) for x in input().split()]
r,c = [int(x) for x in input().split()]
arr = []
arr_ = []
a = 0 
b = c
if n*m != r*c:
    for i in range (0,n):
        arr = (input().strip().split(" "))
        print(' '.join(arr),end='\n')
else:
     if (m>c): 
         for i in range (0,n):
            arr = arr_+ ((input().split(" ")))
            print(' '.join(arr[a:b]),end='\n') 
            arr_ = arr[b:len(arr)]
            # print(arr,a,b)
            if n == 1:
                a+=c
                b+=c
            else:
                if (i>1 and n!=2):
                    a+=c
                    b+=c
                elif (i>=1 and n==2):
                    a+=c
                    b+=c
         for i in range (0,r-n):
            print(' '.join(arr[a:b]),end='\n')
            a+=c
            b+=c
     else:
         for i in range (0,n):
            arr = (input().strip().split(" "))
            arr_ += arr
            if (len(arr_) >= c):
                print(' '.join(arr_[0:c]),end='\n') 
                arr_ = arr_[c:len(arr_)]
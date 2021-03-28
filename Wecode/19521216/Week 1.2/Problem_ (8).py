q = int(input())
gia = []
sum_ = 0
for i in range (0,q):
    n = int(input())
    x = []
    x.extend([int(x) for x in input().split()]) 
    sum_ = sum(x) // n
    if (sum(x) %n !=0):
        sum_ += 1
    gia.append(sum_)
for i in gia:
    print(i)
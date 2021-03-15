a = input()
x = a.split()
t = int(x[1])
k = int(x[0])
if ((int(t/k))%2 ==0):
    print(t%k)
else:
    print(k-t%k)
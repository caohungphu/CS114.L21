a = int(input())

if a < 1 or a > 30:
    print("So",a,"khong nam trong khoang [1,30].")
else:
    f = []
    f.append(0)
    f.append(1)
    for i in range(2, a+1):
       x = int(f[i-1]) + int(f[i-2])
       f.append(x)
    print(f[a])
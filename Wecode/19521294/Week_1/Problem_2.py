n=int(input())
def fibon(n):
    f1, f2 = 1, 1
    if n == 1:
        return f1
    if n == 2:
        return f2
    for _ in range (1,n):
        f1, f2 = f2, f1 + f2
    return f1
if (n < 1) or (n > 30):
    print('So', n ,'khong nam trong khoang [1,30].')
else:
    print(fibon(n))
f = {}

while True:
    a = list(input().split())
    if a[0] == '1':
        f[a[1]] = True
    elif a[0] == '2':
        if f.get(a[1]) == True:
            print(1)
        else:
            print(0)
    else:
        exit()
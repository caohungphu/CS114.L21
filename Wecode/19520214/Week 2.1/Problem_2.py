from sys import stdin

f = []

while True:
    a = list(map(int, stdin.readline().split()))
    if a[0] == 0:
        if len(f) == 0:
            f.append(a[1])
        else:
            f.insert(0,(a[1]))
    elif a[0] == 1:
        f.append(a[1])
    elif a[0] == 2:
        if len(f) > 0:
            try:
                i = f.index(a[1])
                f.insert(i + 1,(a[2]))
            except ValueError:
                f.insert(0,(a[2]))
    elif a[0] == 3:
        if len(f) > 0:
            try:
                f.remove(a[1])
            except ValueError:
                continue
    elif a[0] == 4:
        if len(f) > 0:
            try:
                while a[1] in f:
                    f.remove(a[1])
            except ValueError:
                continue
    elif a[0] == 5:
        if len(f) > 0:
            del f[0]
    else:
        if len(f) == 0:
            print("blank")
        else:
            print(*f, end="\n")
        exit()
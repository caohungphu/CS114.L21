for i in range(int(input())):
    s1 = input()
    s2 = input()
    check = False

    for c in s2:
        if (s1.find(c) != -1):
            check = True
            break

    if check:
        print("YES")
    else:
        print("NO")
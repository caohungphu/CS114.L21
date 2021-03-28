online = {}
s =0
while True:
    s = list([int(x) for x in input().split()])
    if s[0] == 1:
        online[s[1]] = 1
    elif s[0] == 2:
        if s[1]  not in online:
            print(0)
        else:
            print(1)
    elif s[0] == 0 :
        break
from sys import stdin,stdout
input = stdin.readline
online = {}
s =0
try :
    while True:
        s = list([int(x) for x in stdin.readline().split()])
        if s[0] == 1:
            online[s[1]] = 1
        elif s[0] == 2:
            if online.get(s[1])!=1:
                stdout.write("0\n")
            else:
                stdout.write("1\n")
        elif s[0] == 3:
            try:
                online.pop(s[1])
            except KeyError:
                pass
        else:
            exit()
except :
    exit()
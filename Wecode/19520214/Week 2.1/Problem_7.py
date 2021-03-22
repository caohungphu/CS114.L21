from sys import stdin, stdout

f = dict()

try:
    while True:
        a = [int(x) for x in stdin.readline().split()]
        if a[0] == 0:
            break
        else:
            if a[0] == 1:
                f[a[1]] = 1
            elif a[0] == 3:
                if f.get(a[1]) == 1:
                    f.pop(a[1], None)
            elif a[0] == 2:
                if f.get(a[1]) == 1:
                    stdout.write('1\n')
                else:
                    stdout.write('0\n')
            else:
                break
except:
    exit()
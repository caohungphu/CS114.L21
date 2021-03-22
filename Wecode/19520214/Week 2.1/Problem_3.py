n, m = [int(x) for x in input().split()]
a = list([int(x) for x in input().split()])
b = list([int(x) for x in input().split()])
c = a + b
c.sort()

for x in c:
    print(x, end=" ")
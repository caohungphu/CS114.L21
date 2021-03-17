q = int(input())

for i in range(q):
    n = int(input())
    a = list([int(x) for x in input().split()])
    cost = sum(a) // n
    if n * cost != sum(a):
        cost += 1

    print(cost)
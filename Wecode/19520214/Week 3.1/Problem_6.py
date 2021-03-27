q = int(input())

while q:
    n, k = input().split()
    a = list(input().split())
    print(a.count(k))
    q -= 1
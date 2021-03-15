k, t = [int(x) for x in input().split()]

if (t // k) % 2 == 0:
    print(t % k)
else:
    print(k - t % k)
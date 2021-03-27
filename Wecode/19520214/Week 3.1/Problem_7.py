n, m = [int(x) for x in input().split()]

tg, t10 = n, 1

while tg > 0:
    tg //= 10
    t10 *= 10

print(m // t10 + (m % t10 >= n))
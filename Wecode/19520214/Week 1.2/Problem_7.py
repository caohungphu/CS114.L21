n, m, a = [int(x) for x in input().split()]

result = (n // a) * (m // a)

if n % a != 0:
    result += m // a

if m % a != 0:
    result += n // a

if n % a != 0 and m % a != 0:
    result += 1

print(result) 
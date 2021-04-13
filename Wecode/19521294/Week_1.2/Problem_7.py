import math
t = input()
t = t.split()
n = int(t[0])
m = int(t[1])
a = int(t[2])
res = math.ceil(n/a) * math.ceil(m/a)
print(res)
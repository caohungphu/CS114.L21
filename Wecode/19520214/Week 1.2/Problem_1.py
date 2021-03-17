n = input()

s = 0

for i in n:
    s += int(i) ** len(n)

print('True' if int(n) == s else 'False')
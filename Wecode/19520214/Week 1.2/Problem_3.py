s = input().lower()

k = ['a', 'o', 'y', 'e', 'u', 'i']

for i in k:
    s = s.replace(i, '')

for i in s:
    print("." + i, end="")
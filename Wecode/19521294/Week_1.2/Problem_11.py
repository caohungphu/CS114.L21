a = input()
b = input()
s =[]
for i in a:
    s.append(i)
if b == "".join(reversed(s)):
    print("YES")
else:
    print("NO")
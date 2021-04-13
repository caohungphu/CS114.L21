arr = input()
arr = arr.lower()
s = []
for i in arr:
    if i not in {'u','e','o','a','i','y'}:
        s.append(i)
print("."+".".join(s))
s = str(input())
nguyenam= ["a","o","y","e","u","i"]
phuam=[]
s = s.lower()
vt = 0
for i in range (0,len(s)):
    if s[i] not in nguyenam:
        phuam.extend(s[i])
for i in range (0,len(phuam)):
        phuam.insert(vt,'.')
        vt += 2
for i in phuam:
    print(i, end='')
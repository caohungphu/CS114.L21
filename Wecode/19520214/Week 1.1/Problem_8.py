n = int(input())
k = int(input())
p = int(input())
q = int(input())

chiso = (p-1) * 2 + (q-1)
truoc = chiso - k
sau = chiso + k

if truoc >= 0:
    print(truoc // 2 + 1, truoc % 2 + 1)
elif sau <= n-1:
    print(sau // 2 + 1, sau % 2 + 1)
else:
    print(-1)
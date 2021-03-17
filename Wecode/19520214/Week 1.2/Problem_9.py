n = int(input())

def soLuong(k):
    if k == 2:
        return 2
    elif (k % 2 != 0):
        return 1
    return 0

for i in range(n):
    k = int(input())
    print(soLuong(k))
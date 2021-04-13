import math
def check(a,b):
    for i in a:
        if i in b:
            return True
    return False
t = int(input())
for i in range(t):
    a = (input())
    b = (input())
    if check(a,b):
        print("YES")
    else:
        print("NO")
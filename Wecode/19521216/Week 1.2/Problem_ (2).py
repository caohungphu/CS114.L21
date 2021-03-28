n = int(input())
result =[]
def check_(s1,s2):
    for i in s1:
        if s2.find(i) != -1:
            return True
            break
    return False
for i in range (0,n):
    s1 = str(input())
    s2 = str(input())
    if check_(s1, s2) == True:
        print("YES")
    else:
        print("NO")
a,b = [int(x) for x in input().split()]
arr_a =[]
arr_b = []
arr_a.extend([int(a) for a in input().split()])
arr_b.extend([int(b) for b in input().split()])
arr_c = arr_a + arr_b
arr_c.sort()
print(*arr_c,sep=' ')
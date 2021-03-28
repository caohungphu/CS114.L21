n,m = [int(x) for x in input().split()]
arr = []
max_length = []
for i in range(0,m):
   max_length.append(0)
for i in range (0,n):
   arr.append(list(int(x) for x in input().split()))
   for j in range (0,m):
      length = len(str(arr[i][j]))
      max_length[j] = max(length,max_length[j])
for i in range (0,n):
   for j in range (0,m):
      print(str(arr[i][j]).rjust(max_length[j],' '),end=' ')
   print()
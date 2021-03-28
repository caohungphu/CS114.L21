n,k = [int(x) for x in input().split()]
def socohau(a,b):
   length = len(str(a))
   dem = 0
   tmp =pow(10,length)
   dem = int(b/tmp)
   if b%tmp >= a:
       dem+=1
   return dem
print(socohau(n,k))
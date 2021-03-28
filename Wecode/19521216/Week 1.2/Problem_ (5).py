n = int(input())
result=[]
for i in range (0,n):
   x = int(input())
   if(x<=4):
      result.append(4-x)
   else:
      if x%2 ==0:
         result.append(0)
      else:
         result.append(1)
print(*result,sep='\n')
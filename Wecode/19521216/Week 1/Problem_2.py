def Fibonacci_x(n):
    if n <= 1:
        return n
    else:
        return (Fibonacci_x(n-1)+Fibonacci_x(n-2))
    
x = int(input())

if x < 1 or x >30:
    print("So",x,"khong nam trong khoang [1,30].")
else:
    print(Fibonacci_x(x))
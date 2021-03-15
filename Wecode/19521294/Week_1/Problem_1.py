a = int(input())
UC = 1
for i in range(2,a):
    if (a%i==0):
        UC = UC+i
print(UC)

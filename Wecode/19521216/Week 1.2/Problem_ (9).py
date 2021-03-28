s = str(input())
somu = len(s)
amstrong = 0
for i in s:
    amstrong += pow(int(i),somu)   
if amstrong == int(s):
    print("True")
else:
    print("False")
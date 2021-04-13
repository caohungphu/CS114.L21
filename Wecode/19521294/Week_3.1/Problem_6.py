import sys
input = sys.stdin.readline
SL = int(input())
for i in range(SL):
    nk=sys.stdin.readline().strip().split(" ")
    arr = sys.stdin.readline().strip().split(" ")
    print(arr.count(nk[1]))
import sys
input = sys.stdin.readline
n = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a += b
a.sort()
sys.stdout.write(' '.join(map(str, a))+"\n")
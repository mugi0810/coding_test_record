import sys
input=sys.stdin.readline

a,b = map(int,input().split())

a1= set(map(int,input().split()))
b1= set(map(int,input().split()))

print(len(a1-b1)+len(b1-a1))


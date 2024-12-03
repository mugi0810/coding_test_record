import sys
from collections import deque
a=deque([])
for i in range(int(sys.stdin.readline())):
    command=list(sys.stdin.readline().split())
    if command[0] == "push":
        a.append(command[1])
    elif command[0] == "pop":
        if len(a)>0:
            print(a.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(a))
    elif command[0] == "empty":
        if len(a)==0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(a)>0:
            print(a[0])
        else:
            print(-1)
    elif command[0] == "back":
        if len(a)>0:
            print(a[-1])
        else:
            print(-1)
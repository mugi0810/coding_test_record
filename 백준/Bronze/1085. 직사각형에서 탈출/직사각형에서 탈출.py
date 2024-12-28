# 현수는 지금 x, y에 있다
# 왼쪽 아래 꼭지점은 0, 0
# 오른 쪽 위는 w, h

x, y, w, h = map(int,input().split())

print(min(x,y,w-x,h-y))

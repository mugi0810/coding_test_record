data = list(map(int,input().split()))
data.sort(reverse=True)

if data[0]>=data[1]+data[2]:
    data[0]=data[1]+data[2]-1
    print(sum(data))

else:
    print(sum(data))
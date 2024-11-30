n = int(input())

for i in range(n):
    a = list(input())
    sum = 0
    for i in a:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
        if sum < 0:  # 여기서 if로 변경
            print("NO")
            break
            
    if sum == 0:
        print("YES")
    elif sum > 0:
        print("NO")  # 대소문자 수정
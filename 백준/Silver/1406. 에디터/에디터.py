import sys
input = sys.stdin.readline

# 초기 문자열과 명령 개수 입력
string = list(input().strip())
n = int(input())

# 스택 초기화
left_stack = string  # 초기 문자열은 왼쪽 스택에 저장
right_stack = []     # 오른쪽 스택은 비어 있음

# 명령어 처리
for _ in range(n):
    command = input().split()

    if command[0] == 'L':  # 커서를 왼쪽으로 이동
        if left_stack:
            right_stack.append(left_stack.pop())

    elif command[0] == 'D':  # 커서를 오른쪽으로 이동
        if right_stack:
            left_stack.append(right_stack.pop())

    elif command[0] == 'B':  # 커서 왼쪽 문자 삭제
        if left_stack:
            left_stack.pop()

    elif command[0] == 'P':  # 커서 위치에 문자 삽입
        left_stack.append(command[1])

# 결과 출력 (왼쪽 스택 + 오른쪽 스택 뒤집기)
print(''.join(left_stack + right_stack[::-1]))
# N개의 수 입력받기
N = int(input())
num_list = []

# N개의 수를 리스트에 추가
for _ in range(N):
    num = int(input())
    num_list.append(num)

# 리스트를 오름차순으로 정렬
num_list.sort()

# 정렬된 수를 출력
for num in num_list:
    print(num)
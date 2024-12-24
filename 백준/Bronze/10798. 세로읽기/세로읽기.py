# 입력 받기
words = [input() for _ in range(5)]

# 가장 긴 단어의 길이 찾기
max_length = max(len(word) for word in words)

# 각 단어를 가로로 변환하여 출력
for i in range(max_length):
    for word in words:
        if i < len(word):
            print(word[i], end='')
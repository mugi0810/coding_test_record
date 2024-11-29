import sys
input = sys.stdin.readline

n = int(input())  # 사용할 문장 개수

for i in range(n):
    words = list(input().split())  # 리스트에 단어들 입력
    reversed_words = [''.join(reversed(word)) for word in words]  # 각 단어를 뒤집기
    print(' '.join(reversed_words))  # 뒤집힌 단어들을 다시 문자열로 출력
# 분류: 9주차 자유주제
# 문제: 백준 14720 우유축제
# 문제 주소: https://www.acmicpc.net/problem/14720
# 푼 사람: 진홍엽
# 설명: 수학
# 평점: 3/5

# 복잡해보이지만 의외로 쉬운 문제
i_n = int(input())
cnt = 0
for i in map(int, input().split()):
    if i == cnt % 3:
        cnt += 1
print(cnt)
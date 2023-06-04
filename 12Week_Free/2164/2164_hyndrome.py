# 분류: 12주차 자유주제
# 문제: 백준 2164 카드2
# 문제 주소: https://www.acmicpc.net/problem/2164
# 푼 사람: 진홍엽
# 설명: 큐  
# 평점: 1.5/5
from collections import deque


i_n = int(input())
que = deque([i + 1 for i in range(i_n)])
while len(que) != 1:
    que.popleft()
    que.rotate(-1)
print(*que)
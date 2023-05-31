# 분류: 12주차 자유주제
# 문제: 백준 2583 영역구하기
# 문제 주소: https://www.acmicpc.net/problem/2583
# 푼 사람: 진홍엽
# 설명: BFS 델타탐색
# 평점: 3/5
from collections import deque


i_n = int(input())
que = deque([i + 1 for i in range(i_n)])
while len(que) != 1:
    que.popleft()
    que.rotate(-1)
print(*que)
import sys
from collections import deque


i_m, i_n, i_k = map(int, sys.stdin.readline().split())
graph = [[0] * i_n for _ in range(i_m)]
for i in range(i_k):
    x_1, y_1, x_2, y_2 = map(int, sys.stdin.readline().split())
    for y in range(y_1, y_2, 1):
        for x in range(x_1, x_2, 1):
            graph[y][x] = 1
delta_x = [0, 1, 0, -1]
delta_y = [1, 0, -1, 0]
cnt = 0
ls_area = []

def bfs (x, y):
    area = 0
    if graph[y][x] == 0:
        graph[y][x] = 1
        global cnt
        cnt += 1
        area = 1
        que = deque()
        que.append((x, y))
        while que:
            x, y = que.popleft()
            for delta in range(4):
                nx = x + delta_x[delta]
                ny = y + delta_y[delta]
                if (0 <= nx < i_n) and (0 <= ny < i_m):
                    if graph[ny][nx] == 0:
                        graph[ny][nx] = 1
                        que.append((nx, ny))
                        area += 1
    if area != 0:
        ls_area.append(area)
    return

for y in range(i_m):
    for x in range(i_n):
        bfs(x, y)
ls_area.sort()
print(cnt)
print(*ls_area)    
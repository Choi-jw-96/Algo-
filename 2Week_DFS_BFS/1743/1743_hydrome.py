# 분류: 2주차 BFS / DFS
# 문제: 백준 1743 음식물피하기
# 문제 주소: https://www.acmicpc.net/problem/1743
# 푼 사람: 진홍엽
# 설명: bfs
import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]

i_n, i_m, i_k = map(int, sys.stdin.readline().split())
graph = [[0] * i_m for i_1 in range(i_n)]
for i_2 in range(i_k):
    y_trash, x_trash = map(int, sys.stdin.readline().split())
    graph[y_trash - 1][x_trash - 1] = 1

ls_trash = []

for i_3 in range(i_n):
    for i_4 in range(i_m):
        if graph[i_3][i_4] == 1:
            graph[i_3][i_4] = 0
            que = deque()
            que.append((i_4, i_3))
            cnt = 1
            while que:
                x, y = que.popleft()
                for i_5 in range(4):
                    nx = x + dx[i_5]
                    ny = y + dy[i_5]
                    if (0 <= nx < i_m) * (0 <= ny < i_n):
                        if (graph[ny][nx] == 1):
                            graph[ny][nx] = 0
                            que.append((nx, ny))
                            cnt += 1
            ls_trash.append(cnt)
print(max(ls_trash))
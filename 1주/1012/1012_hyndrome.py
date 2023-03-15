# 분류: 1주차 BFS / DFS
# 문제: 백준 1012 유기농 배추
# 푼 사람: 진홍엽
# 설명: BFS, 델타 탐색 사용

import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt_worm = 0

i_t = int(sys.stdin.readline())
for i_1 in range(i_t):
    cnt_worm = 0
    i_m, i_n, i_k = map(int, sys.stdin.readline().split())
    graph = [[0] * i_m for i_2 in range(i_n)]
    for i_3 in range(i_k):
        x_cabbage, y_cabbage = map(int, sys.stdin.readline().split())
        graph[y_cabbage][x_cabbage] = 1

    for i_4 in range(i_n):
        for i_5 in range(i_m):
            if graph[i_4][i_5] == 0:
                continue
            else:
                graph[i_4][i_5] = 0
                que = deque()
                que.append((i_5, i_4))
                while que:
                    x, y = que.popleft()
                    for i_6 in range(4):
                        nx = x + dx[i_6]
                        ny = y + dy[i_6]
                        if (nx <  0) + (nx >= i_m) + (ny < 0) + (ny >= i_n):
                            continue
                        else:
                            if graph[ny][nx] == 1:
                                que.append((nx, ny))
                                graph[ny][nx] = 0
                cnt_worm += 1
    print(cnt_worm)                
                
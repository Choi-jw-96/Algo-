# 분류: 1주차 BFS / DFS
# 문제: 백준 2468 안전영역 
# 문제 주소: https://www.acmicpc.net/problem/2468
# 푼 사람: 진홍엽
# 설명: BFS, 델타 탐색 사용

import sys
from collections import deque
import pprint

i_n = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for i_1 in range(i_n)]

result = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

i_max = 1
i_min = 100
for ls_1 in graph:
    if max(ls_1) > i_max:
        i_max = max(ls_1)
    if min(ls_1) < i_min:
        i_min = min(ls_1) - 1

for i_2 in range(i_min, i_max):
    visited = [[False] * i_n for i_6 in range(i_n)]
    cnt_island = 0
    for i_3 in range(i_n):
        for i_4 in range(i_n):
            if graph[i_3][i_4] > i_2 and visited[i_3][i_4] == False:
                cnt_island += 1
                visited[i_3][i_4] = True
                que = deque()
                que.append((i_4, i_3))
                while que:
                    x, y = que.popleft()
                    for i_5 in range(4):
                        nx = x + dx[i_5]
                        ny = y + dy[i_5]
                        if nx < 0 or nx >= i_n or ny < 0 or ny >= i_n:
                            continue
                        if graph[ny][nx] > i_2 and visited[ny][nx] == False:
                            que.append((nx, ny))
                            visited[ny][nx] = True
            else:
                visited[i_3][i_4] = True
    result.append(cnt_island)
print(max(result))
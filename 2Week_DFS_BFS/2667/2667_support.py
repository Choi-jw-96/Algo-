# DFS
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
big = 0

def dfs(graph, x, y, visited):
    global c
    c += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == "1" and not visited[nx][ny]:
                visited[nx][ny] = c
                dfs(graph, nx, ny, visited)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000000)

n = int(input())

graph = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

cnt = 0
c_li = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == "1" and visited[i][j] == 0:
            # c가 마지막에 돌다가 그대로 나오기 때문에 0부터 시작
            c = 0
            visited[i][j] = 1
            dfs(graph, i, j, visited)
            cnt += 1
            c_li.append(c)

print(cnt)
for _ in sorted(c_li):
    print(_)


# BFS
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

from collections import deque
def bfs(graph, x, y, visited):
    global c
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == "1" and not visited[nx][ny]:
                    q.append((nx, ny))
                    c += 1
                    visited[nx][ny] = c


import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000000)

n = int(input())

graph = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

cnt = 0
c_li = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == "1" and visited[i][j] == 0:
            c = 1
            bfs(graph, i, j, visited)
            cnt += 1
            c_li.append(c)

print(cnt)
for _ in sorted(c_li):
    print(_)
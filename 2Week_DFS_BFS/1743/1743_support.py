# BFS
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def BFS(graph, visitied, x, y):
    global cnt

    queue = deque([(x, y)])
    cnt += 1
    visitied[x][y] = cnt

    while queue:
        n, m = queue.popleft()

        for _ in range(4):
            nx = n + dx[_]
            ny = m + dy[_]

            if 0 <= nx < N and 0 <= ny < M and not visitied[nx][ny] and graph[nx][ny]:
                queue.append((nx, ny))
                cnt += 1
                visitied[nx][ny] = cnt
    
    return

N, M, k = map(int, input().split())

graph = [[0] * (M) for _ in range(N)]
visited = [[0] * (M) for _ in range(N)]

for i in range(k):
    n, m = map(int, input().split())
    graph[n - 1][m - 1] = 1

big = 0
for x in range(N):
    for y in range(M):
        if graph[x][y] and not visited[x][y]:
            cnt = 0
            BFS(graph, visited, x, y)
            big = max(cnt, big)
print(big)


# DFS
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def DFS(graph, visitied, x, y):
    global cnt
    visited[x][y] = cnt

    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]

        if 0 <= nx < N and 0 <= ny < M and not visitied[nx][ny] and graph[nx][ny]:
            cnt += 1
            DFS(graph, visited, nx, ny)



N, M, k = map(int, input().split())

graph = [[0] * (M) for _ in range(N)]
visited = [[0] * (M) for _ in range(N)]

for i in range(k):
    n, m = map(int, input().split())
    graph[n - 1][m - 1] = 1

big = 0
for x in range(N):
    for y in range(M):
        if graph[x][y] and not visited[x][y]:
            cnt = 1
            DFS(graph, visited, x, y)
            big = max(cnt, big)
print(big)
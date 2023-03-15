# DFS
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(graph, x, y, visited, I):
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]

        if  0 <= nx < N and 0 <= ny < N and graph[nx][ny] > I and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(graph, nx, ny, visited, I)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())

graph = []
big = 0

for _ in range(N):
    n = list(map(int, input().split()))
    graph.append(n)
    m = max(n)
    big = max(m, big)

maxi = 0
for I in range(0, big + 1):
    visited =[[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > I:
                visited[i][j] = True
                dfs(graph, i, j, visited, I)
                cnt += 1
                maxi = max(maxi, cnt)

print(maxi)
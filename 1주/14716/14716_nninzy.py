import sys
sys.setrecursionlimit(1000000)

def dfs(y, x):
    graph[y][x] = 0
    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [-1, 0, 1, -1, 1, 1, 0, -1]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= ny < m) and (0 <= nx < n) and graph[ny][nx] == 1:
            dfs(ny, nx)
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            cnt += 1
print(cnt)
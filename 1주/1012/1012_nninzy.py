import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = -1
                dfs(nx, ny)
T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    matrix = [[0]*m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    for a in range(n):
        for b in range(m):
            if matrix[a][b] > 0:
                dfs(a, b)
                cnt += 1
    print(cnt)
# 2583번 영역 구하기
'''
각 좌표마다 빵구를 뚫는다. 나머지 0으로 채워진 곳의 그룹을 센다.
영역의 넓이(좌표 0의 개수(len))
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(x, y):
    global cnt
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0<= ny < n and visited[nx][ny] == 0:
            cnt += 1
            dfs(nx, ny)

m, n, k = map(int, input().split())
visited = [[0] * n for _ in range(m)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = 1
area = 0
res = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            visited[i][j] = 1

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            area += 1
            dfs(i, j)
            res.append(cnt)
            cnt = 1
res.sort()
print(area)
print(*res)

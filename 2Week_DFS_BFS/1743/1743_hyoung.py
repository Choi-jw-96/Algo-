# 1743 음식물 피하기
import sys
sys.setrecursionlimit(10**7)

n, m, k = map(int, sys.stdin.readline().split())
graph = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    graph[r-1][c-1] = 1

ls = []
cnt = 0

def dfs(x,y):
    if x >= 0 and x < n and y >= 0 and y < m and graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dfs(i,j)
            ls.append(cnt)
            cnt = 0
print(max(ls))
        
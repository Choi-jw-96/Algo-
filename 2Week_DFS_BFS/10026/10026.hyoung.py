# 10026
import sys
sys.setrecursionlimit(10**7)

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
cnt1 = 0
cnt2 = 0

def dfs(x,y):
    if x >= 0 and x < n and y >= 0 and y < n and graph[x][y] == color and visited[x][y] == False:
        visited[x][y] = True
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            color = graph[i][j]
            dfs(i,j)
            cnt1 += 1

# 적록색약
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
visited = [[False] * n for _ in range(n)]

def dfs(x,y):
    if x >= 0 and x < n and y >= 0 and y < n and graph[x][y] == color and visited[x][y] == False:
        visited[x][y] = True
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            color = graph[i][j]
            dfs(i,j)
            cnt2 += 1
print(cnt1, cnt2)
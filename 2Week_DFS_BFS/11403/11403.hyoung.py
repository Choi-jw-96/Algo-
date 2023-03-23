import sys
from collections import deque
sys.setrecursionlimit(10**7)

n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def bfs(x):
    queue = deque()
    queue.append(x)
    row = [0 for _ in range(n)]
    while queue:
        q = queue.popleft()
        for i in range(n):
            if row[i] == 0 and graph[q][i] == 1:
                queue.append(i)
                visited[x][i] = 1
                row[i] = 1
for i in range(n):
    bfs(i)
    
for i in visited:
    print(*i)


# n = int(input())
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# visited = [0] * n
# def dfs(v):
#     for k in range(n):
#         if graph[v][k] == 1:
#             visited[k] = 1
#             dfs(k)

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             dfs(j)
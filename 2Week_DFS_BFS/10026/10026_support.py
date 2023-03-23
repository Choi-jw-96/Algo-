dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

def DFS(graph, visited, i, j):
  visited[i][j] = 1

  for _ in range(4):
    nx = i + dx[_]
    ny = j + dy[_]

    if 0 <= nx < N and 0 <= ny < N and graph[i][j] == graph[nx][ny] and not visited[nx][ny]:
      DFS(graph, visited, nx, ny)

N = int(input())

graph = [list(input().strip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited_2 = [[0] * N for _ in range(N)]

cnt = 0
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      DFS(graph, visited, i, j)
      cnt += 1

for i in range(N):
  for j in range(N):
    if graph[i][j] == "G":
      graph[i][j] = "R"

cnt_2 = 0
for i in range(N):
  for j in range(N):
    if not visited_2[i][j]:
      DFS(graph, visited_2, i, j)
      cnt_2 += 1
print(cnt, cnt_2)
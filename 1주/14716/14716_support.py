import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 1, 1, 0, -1]

def DFS(graph, visited, i, j):
    visited[i][j] = True

    for _ in range(8):
        X = i + dx[_]
        Y = j + dy[_]
        if 0 <= X < M and 0 <= Y < N and visited[X][Y] == False and graph[X][Y] == "1":
            visited[X][Y] = True
            DFS(graph, visited, X, Y)

M, N =  map(int, input().split())
graph = []
visited = [[False] * N  for _ in range(M)]

for _ in range(M):
    graph.append(list(input().strip().split()))

cnt = 0

for i in range(M):
    for j in range(N):
        if graph[i][j] == "1" and visited[i][j] == False:
            DFS(graph, visited, i, j)
            cnt += 1

print(cnt)
# D
import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10**6

def dfs(graph, visited, i, j):
    global Y, X
    for _ in range(4):
        I = i + dx[_]
        J = j + dy[_]

        if 0 <= I < X and 0 <= J < Y and graph[I][J] == 1 and visited[I][J] == False:
            visited[I][J] = True
            dfs(graph, visited, I, J)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())

for _ in range(n):
    Y, X, K = map(int, input().split())

    graph = [[0] * Y for _ in range(X)]
    visited = [[False] * Y for _ in range(X)]

    for k in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1

    cnt = 0
    for i in range(X):
        for j in range(Y):
            if graph[i][j] == 1 and visited[i][j] == False:
                visited[i][j] = True
                dfs(graph, visited, i, j)
                cnt += 1
    
    print(cnt)

# B
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10**6

def bfs(graph, visited, i, j):
    global Y, X
    q = deque([(i, j)])
    visited[i][j] = True

    while q:
        i, j = q.popleft()
    
        for _ in range(4):
            I = i + dx[_]
            J = j + dy[_]

            if 0 <= I < X and 0 <= J < Y and graph[I][J] == 1 and visited[I][J] == False:
                q.append((I, J))
                visited[I][J] = True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())

for _ in range(n):
    Y, X, K = map(int, input().split())

    graph = [[0] * Y for _ in range(X)]
    visited = [[False] * Y for _ in range(X)]

    for k in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1

    cnt = 0
    for i in range(X):
        for j in range(Y):
            if graph[i][j] == 1 and visited[i][j] == False:
                bfs(graph, visited, i, j)
                cnt += 1
     
print(cnt)
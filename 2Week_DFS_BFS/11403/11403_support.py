import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline

def BFS(i):
    queue = deque([i])
    check = [0] * N

    while queue:
        q = queue.popleft()
        for j in range(N):
            if not check[j] and graph[q][j] == 1:
                queue.append(j)
                check[j] = 1
                visited[i][j] = 1

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for i in range(N):
    BFS(i)
    print(*visited[i])

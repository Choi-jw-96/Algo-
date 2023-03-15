import sys
from collections import deque

def dfs(current):
    for i in graph[current]:
        if visited[i] == -1:
            visited[i] = visited[current] + 1
            dfs(i)

N = int(input())
start, end = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)]
for _ in range(int(input())):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[start] = 0
dfs(start)
print(visited[end])
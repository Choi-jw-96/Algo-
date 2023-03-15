# DSF
def dsf(graph, n, visited):
    global cnt

    for j in graph[n]:
        if visited[j] == 0:
            visited[j] = visited[n] + 1
            dsf(graph, j, visited)


import sys
input = sys.stdin.readline

people = int(input())

graph = [[] for _ in range(people + 1)]
visited = [0] * (people + 1)

who_1, who_2 = map(int, input().split())

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited[who_1] = 1
dsf(graph, who_1, visited)


if visited[who_2] > 0:
    print(visited[who_2] - 1)
else:
    print(-1)

    
# BFS
from collections import deque
def bsf(graph, n, visited):
    q = deque([n])
    visited[n] = 1

    while q:
        p = q.popleft()
        for j in graph[p]:
            if visited[j] == 0:
                visited[j] = visited[p] + 1
                q.append(j)

import sys
input = sys.stdin.readline

people = int(input())

graph = [[] for _ in range(people + 1)]
visited = [0] * (people + 1)
who_1, who_2 = map(int, input().split())
m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
bsf(graph, who_1, visited)

if visited[who_2] > 0:
    print(visited[who_2] - 1)
else:
    print(-1)
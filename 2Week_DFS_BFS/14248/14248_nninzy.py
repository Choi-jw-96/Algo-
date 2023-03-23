from collections import deque

# BFS 메서드
def bfS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 1
    while queue:
        v = queue.popleft()
        for j in graph[v]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True
                cnt += 1
    return print(cnt)

# input 받기
n = int(input())
stones = [*map(int, input().split())]
s = int(input()) - 1

# 이중리스트 만들기
graph = []
for i in range(n):
    lines = []
    line1 = i - stones[i]
    line2 = i + stones[i]
    if 0 <= line1 < n: lines.append(line1)
    if 0 <= line2 < n: lines.append(line2)
    graph.append(lines)

visited = [False] * n

bfS(graph, s, visited)
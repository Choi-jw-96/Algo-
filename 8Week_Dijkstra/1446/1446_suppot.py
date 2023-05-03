import heapq, sys
input = sys.stdin.readline

def short(start):
    queue = []
    heapq.heappush(queue, (0, start))
    visited[start] = 0

    while queue:
        far, now = heapq.heappop(queue)

        for i in graph[now]:
            if visited[i[0]] > far + i[1]:
                visited[i[0]] = far + i[1]
                heapq.heappush(queue, (far + i[1], i[0]))


n, M = map(int, input().split())
graph = [[] for i in range(M + 1)]
visited = [float('inf')] * (M + 1)

for i in range(M):
    graph[i].append((i+1, 1))

for _ in range(n):
    start, end, m = map(int, input().split())
    if end > M:
        continue
    graph[start].append((end, m))

short(0)
print(visited[M])
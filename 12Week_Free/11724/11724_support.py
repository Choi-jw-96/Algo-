import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline 

def dsf(grap, num, visit):
    visit[num] = True
    for i in grap[num]:
        if not visit[i]:
            dsf(grap, i, visit)

N, M = map(int, input().split())
graph = [[]for _ in range(N + 1)]
visited = [False] * (N + 1)


for _ in range(M):
    u, v =  map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0

for j in range(1, N + 1):
    if not visited[j]:
        dsf(graph, j, visited)
        cnt += 1

print(cnt)

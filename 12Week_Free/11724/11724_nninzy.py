n, m = map(int, input().split())
graph = list([] for _ in range(n+1))

visited = [False] * (n+1)
cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(x):
    visited[x] = True
    for a in graph[x]:
        if not visited[a]:
            dfs(a)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
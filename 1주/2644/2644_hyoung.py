import sys

n = int(input())
a, b = map(int, sys.stdin.readline().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

cnt_ls = []
cnt = 0

def dfs(v,cnt):
    cnt += 1
    visited[v] = True
    if v == b:
        cnt_ls.append(cnt)
    for i in graph[v]:
        if not visited[i]:
            dfs(i,cnt)
dfs(a, 0)

if len(cnt_ls) == 0:
    print(-1)
else:
    print(cnt_ls[0]-1)

  
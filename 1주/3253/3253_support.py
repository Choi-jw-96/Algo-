
import sys
input = sys.stdin.readline

def DFS(graph, visited, a, b):
    global cnt
    visited[a] = True  

    for i in graph[a]:
        if i != b :
            if visited[i] == False:
                cnt += 1
                DFS(graph, visited, i, b) 
                cnt -= 1
        else:
            cnt += 1
            short.append(cnt)

N, A, B = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
    n = list(map(int, input().strip().split()))
    for j in range(1, n[0]+1):
        graph[i].append(n[j])

short = []

for i in graph[A]:
    if i != B:
        visited = [False] * (N + 1)
        visited[A] = True
        cnt = 0    
        DFS(graph, visited, i, B)
    else:
        short.append(0)

if not short:
    print(-1)
else:
    print(min(short))

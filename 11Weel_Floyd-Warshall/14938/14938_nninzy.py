INF = int(1e9)

n, m, r = map(int, input().split())
t_list = list(map(int, input().split()))
graph = [[INF] * n for _ in range(n)]
answer = 0

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = min(graph[a-1][b-1], l)
    graph[b][a] = min(graph[b][a], l)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    temp = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            temp += t_list[j - 1]

    answer = max(answer, temp)

print(answer)
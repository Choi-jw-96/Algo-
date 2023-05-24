import sys


n = int(input())
m = int(input())
INF = 1e9
# 최소비용을 구하기 위한 문제 INF로 초기화 해주고 갱신
graph = [[INF] *n for i in range(n)]

for _ in range(m):
    start,end,dis = map(int,input().split())
    # 작은걸로 갱신해서 값 넣어주기
    if graph[start-1][end-1] > dis:
        graph[start-1][end-1] = dis

for i in range(n):
    for j in range(n):
        for k in range(n):
                if graph[j][k] > graph[j][i]  + graph[i][k] and  j != k:
                    graph[j][k]  = graph[j][i]  + graph[i][k]
         
# 만약 INF가 담겨있다면 방문을 하지 않은 것이기 때문에 0으로 바꿔준다.
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(n):
    print(*graph[i])
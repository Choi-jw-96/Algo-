# 1389번 케빈 베이컨의 6단게 법칙
'''
케빈 베이컨 게임은 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산하는 게임
각 index별 총합을 구해 최소합을 찾아내는 것
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = 1e9
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
# print(graph)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
# print(graph)

# 각 index별로 총합을 구해서 최솟값을 구하되, 값이 동일하면 작은 index를 출력한다.
min = 1e9
min_index = n
for a in range(n, 0, -1):
    sum_friend = 0
    for b in range(n, 0, -1):
        sum_friend += graph[a][b]
    if min >= sum_friend:
        min = sum_friend
        min_index = a

print(min_index)
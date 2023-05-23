# 분류: 11주차 플로이드-마셜
# 문제: 백준 14938 서강그라운드
# 문제 주소: https://www.acmicpc.net/problem/14938
# 푼 사람: 진홍엽
# 설명: 플로이드-마셜 
# 평점: 3.5/5
import sys

# 입력 및 플로이드 마셜 적용
i_n, i_m, i_r = map(int, sys.stdin.readline().split())
ls_items = [0] + list(map(int, sys.stdin.readline().split()))
INF = int(1e9)
graph = [[INF] * (i_n + 1) for _ in range(i_n + 1)]
for i in range(i_r):
    start, end, distance = map(int, sys.stdin.readline().split())
    graph[start][end] = distance
    graph[end][start] = distance
for y in range(1, i_n + 1):
    for x in range(1, i_n + 1):
        if x == y:
            graph[y][x] = 0

for k in range(1, i_n + 1):
    for y in range(1, i_n + 1):
        for x in range(1, i_n + 1):
            graph[y][x] = min(graph[y][x], graph[y][k] + graph[k][x])

# 수색 범위 내 아이템 개수 확인 및 최대 개수 갱신
items_max = 0
for y in range(1, i_n + 1):
    items_n = 0
    for x in range(1, i_n + 1):
        if graph[y][x] <= i_m:
            items_n += ls_items[x]
    if items_n > items_max:
        items_max = items_n

print(items_max)
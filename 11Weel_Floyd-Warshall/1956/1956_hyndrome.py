# 분류: 11주차 플로이드-마셜
# 문제: 백준 1956 운동
# 문제 주소: https://www.acmicpc.net/problem/1956
# 푼 사람: 진홍엽
# 설명: 플로이드-마셜 다익스트라 
# 평점: 3/5
# 이전과 비교했을 때 채점 샘플이 바뀐 것 같음
# 플로이드 마셜에서 자기자신을 0으로 두는 대신에 무한으로 두고 그대로 계산하면 될듯?
# 플로이드 마셜 - 시간 초과; 노드 개수가 400개일 때 조금 쌔했음
# PyPy3으로 제출 시 876ms / 시간복잡도 O(V^3)
import sys


i_v, i_e = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (i_v + 1) for _ in range(i_v + 1)]

# 기존 플로이드-마셜 알고리즘에서 자기 자신을 0으로 두는 부분 삭제
for i in range(i_e):
    start, end, distance = map(int, sys.stdin.readline().split())
    graph[start][end] = distance

for k in range(1, i_v + 1):
    for y in range(1, i_v + 1):
        for x in range(1, i_v + 1):
            graph[y][x] = min(graph[y][x], graph[y][k] + graph[k][x])

cycle_min = INF
for i in range(1, i_v):
    cycle_v = graph[i][i]
    if cycle_v < cycle_min:
        cycle_min = cycle_v

if cycle_min == INF:
    print(-1)
else:
    print(cycle_min)

# 폴로이드 마셜의 시간 복잡도보다 다익스트라가 시간복잡도가 작을 것이라고 생각해서 다익스트라 적용해봄
# 보기 좋게 실패
# PyPy3으로 제출 시 1616ms / 시간복잡도 O(V*V(V-1)logV = ElogV를 V번 적용)
import sys, heapq


INF = int(1e9)
i_v, i_e = map(int, input().split())
graph = [[] for _ in range(i_v + 1)]
distance = [INF] * (i_v + 1)
for i in range(i_e):
    start, end, distance_input = map(int, sys.stdin.readline().split())
    graph[start].append((end, distance_input))

def dijkstra(start):
    que = []
    # 다익스트라의 시작지점의 거리를 0이 아닌 INF로 두고 시작 (heapq 내에서는 알고리즘 작동을 위해서 0으로 둠)
    heapq.heappush(que, (0, start))
    distance[start] = INF
    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for path in graph[now]:
            cost = dist + path[1]
            if cost < distance[path[0]]:
                distance[path[0]] = cost
                heapq.heappush(que, (cost, path[0]))

cycle_min = INF
for i in range(1, i_v + 1):
    dijkstra(i)
    cycle_v = distance[i]
    if cycle_v < cycle_min:
        cycle_min = cycle_v
    distance = [INF] * (i_v + 1)
if cycle_min == INF:
    print(-1)
else:
    print(cycle_min)

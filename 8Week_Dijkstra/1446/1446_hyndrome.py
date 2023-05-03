# 분류: 8주차 이분탐색
# 문제: 백준 1446 지름길
# 문제 주소: https://www.acmicpc.net/problem/1446
# 푼 사람: 진홍엽
# 설명: 데이크스트라 DP
# 평점: 5/5
import sys
import heapq

INF = int(1e9)

# i_n, i_d = map(int, sys.stdin.readline().split())
# graph = [[(i+1, 1)] for i in range(i_d)]
# distance = [INF] * (i_d + 1)

# for i in range(i_n):
#     start, end, cost = map(int, input().split())
#     if ((end - start) - cost > 0) and (end <= i_d):
#         graph[start].append((end, cost))

n , d = map(int,input().split())
graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

#일단 거리 1로 초기화.
for i in range(d):
    graph[i].append((i+1, 1))

#지름길 있는 경우에 업데이트
for _ in range(n):
    s, e, l = map(int,input().split())
    if e > d:# 고려 안해도 됨.
        continue
    graph[s].append((e,l))

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for path in graph[now]:
            cost = dist + path[1]
            if cost < distance[path[0]]:
                distance[path[0]] = cost
                heapq.heappush(que, (cost, path[0]))

dijkstra(0)
print(distance[d])

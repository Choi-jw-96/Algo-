# 분류: 8주차 이분탐색
# 문제: 백준 1916 최소비용구하기
# 문제 주소: https://www.acmicpc.net/problem/1916
# 푼 사람: 진홍엽
# 설명: 데이크스트라
# 평점: 4/5 [기본]
import sys
import heapq

INF = int(1e9)

i_n = int(input())
i_m = int(input())
# 인덱스가 1부터 시작하기 때문에 i_n + 1
graph = [[] for _ in range(i_n + 1)]
distance = [INF] * (i_n + 1)
for i in range(i_m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end, cost))
i_start, i_end = map(int, input().split())

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

dijkstra(i_start)

print(distance[i_end])
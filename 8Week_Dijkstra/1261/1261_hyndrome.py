# 분류: 8주차 이분탐색
# 문제: 백준 1261 알고스팟
# 문제 주소: https://www.acmicpc.net/problem/1261
# 푼 사람: 진홍엽
# 설명: 데이크스트라
# 평점: 3/5
import sys
import heapq

INF = int(1e9)
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

i_m, i_n = map(int, input().split())
graph = []
for i in range(i_n):
    graph.append([int(s) for s in sys.stdin.readline().rstrip()])
distance = [[INF] * i_m for _ in range(i_n)]

def dijkstra(start):
    que = []
    heapq.heappush(que, (graph[0][0], start))
    distance[start[1]][start[0]] = graph[0][0]
    while que:
        dist, now = heapq.heappop(que)
        if distance[now[1]][now[0]] < dist:
            continue
        for dx, dy in move:
            nx = now[0] + dx
            ny = now[1] + dy
            if (0 <= nx < i_m) and (0 <= ny < i_n):
                cost = dist + graph[ny][nx]
                if cost < distance[ny][nx]:
                    distance[ny][nx] = cost
                    heapq.heappush(que, (cost, (nx, ny)))
                    
dijkstra((0, 0))

print(distance[i_n - 1][i_m - 1])
# 1916번 최소비용 구하기
## 문제
'''
N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다
우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라.

도시의 번호는 1부터 N까지이다.
'''
import heapq
import sys
input = sys.stdin.readline

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수
INF = int(1e9)
# print(type(INF)) -> class 'float'

route = [[] for _ in range(n + 1)] # 노선 정보
for _ in range(m):
    s, e, c = map(int, input().split())
    route[s].append((e, c))
distance = [INF] * (n + 1)
target_s, target_e = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        c, now = heapq.heappop(q)
        if distance[now] < c:
            continue
        for destination, weight in route[now]:
            cost = distance[now] + weight
            if distance[destination] > cost:
                distance[destination] = cost
                heapq.heappush(q, (cost, destination))

dijkstra(target_s)
print(distance[target_e])




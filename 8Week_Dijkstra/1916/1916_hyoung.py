# 최소비용 구하기

import heapq 
import sys
input = sys.stdin.readline

# 입력
N = int(input())  
M = int(input())  
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split()) 


def dijkstra(graph, start):
    distances = [int(1e9)] * (N+1)  # 처음 초기값은 무한대
    distances[start] = 0  
    queue = []
    heapq.heappush(queue, [distances[start], start])  

    while queue: 
        dist, node = heapq.heappop(queue)  

        if distances[node] < dist:
            continue

        # 노드와 연결된 인접노드 탐색
        for next_node, next_dist in graph[node]:
            distance = dist + next_dist  # 인접노드까지의 거리
            if distance < distances[next_node]:  
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node]) 
    return distances

dist_start = dijkstra(graph, start)
print(dist_start[end])
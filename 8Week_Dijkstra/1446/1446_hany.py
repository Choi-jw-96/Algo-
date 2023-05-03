# 1446번 지름길
## 문제
'''
D킬로미터 길이의 고속도로를 지난다.
모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.
세준이가 운전해야 하는 거리의 최솟값을 출력하시오.

첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다(0<=n<= 12, d<= 10,000)
다음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다.
지름길의 시작 위치는 도착 위치보다 작다.
'''
## 접근방법
'''
- 0 -> d 까지 가야함
- d <= 10000 (거리 1마다 노드로 본다면, heapq를 쓰는 게 합당)
- 고속도로 d보다 지름길이 끝나는 지점이 큰 경우, 정보를 추가하지 않는다.
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) 

n, d = map(int, input().split()) # n: 지름길의 개수, d: 고속도로의 길이
graph = [[] for _ in range(d + 1)] # 고속도로 d만큼 그래프 추가
distance = [INF] * (d + 1) # 최소거리 테이블 또한 마찬가지

def dijkstra(start):
    q = []
    # 초기값 넣기
    heapq.heappush(q, (0, start)) 
    distance[start] = 0
    while q: # q에 남아 있는 노드가 없으면 끝남.
        # 가장 최단 거리인 노드에 대한 정보 꺼내끼
        dist, now = heapq.heappop(q) # dist:탐색할 노드, now: 현재

        # 기존 거리보다 길다면, 의미 x
        # 즉, 현재 노드가 이미 처리되었다면 스킵하라
        if dist > distance[now]:
            continue
        # 기존 거리보다 짧은 경우, 현 노드와 연결된 다른 인접 노드 확인
        for i in graph[now]:
            # 해당 노드를 거쳐 갈 때의 거리
            cost = dist + i[1]
            # 그 거리가 알고 있는 기존 거리보다 자작으면 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 다음 인접 거리를 계산하기 위해 큐에 삽입
                heapq.heappush(q, (cost, i[0]))

# 그래프의 모든 거리를 1로 초기화
for i in range(d):
    graph[i].append((i + 1, 1))
# print(graph)

for _ in range(n):
    s, e, shortcut = map(int, input().split())
    # 지름길의 끝이 고속도로 길이를 넘어선다면 고려 x
    if e > d:
        continue
    # 시작 노드에서 도착 노드까지의 거리
    # 그래프의 해당 인덱스(시작위치)에 도착 위치, 거리(지름길)을 튜플로 넣는다.
    graph[s].append((e, shortcut))

dijkstra(0)
print(distance[d])
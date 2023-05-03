import sys, heapq
input = sys.stdin.readline

def go(s):
    visited[s] = 0
    queue = []
    # 힙을 사용하여 최대한 적은 cost를먼져 나오게 한다
    # 시작점을 넣어준다, cost는 0으로 시작
    heapq.heappush(queue, (0, s))

    # queue가 필때까지
    while queue:
        cost, station = heapq.heappop(queue)
        # 이문장은 없어도 정답은 나오지만, 문제 풀때 시간 초과가 나온다. 막기위해 필수!
        if visited[station] < cost:
            continue
        for c, d in graph[station]:
            # 범위 안에서 visited에 등록 된것 보다 적에 움직인 것만 넣어줘라
            if  visited[d] > c + cost:
                visited[d] = c + cost
                heapq.heappush(queue, (c + cost, d))

city = int(input())
bus = int(input())

graph = [[] for _ in range(city + 1)]
for i in range(bus):
    s, e, c = map(int, input().split())
    # heapq이니 cost가 먼저오게 설정
    graph[s].append((c, e))

visited = [float('inf')] * (city + 1)
start, end = map(int, input().split()) 
go(start)
print(visited[end])
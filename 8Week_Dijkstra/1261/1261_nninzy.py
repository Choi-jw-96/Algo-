import heapq
INF = int(1e9)

# 다익스트라 관련 함수
# 1을 가중치로 생각.
def dijkstra():
    dist[0][0] = 0 
    heap = [[0, 0]] # 출발점인 (0, 0)을 우선순위 큐에 넣음

    while heap:
        y, x = heapq.heappop(heap)

        for i in range(4): #상하좌우 인접 노트 확인
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m: #범위 내부
                if maze[ny][nx] == 1: #벽인 경우 노드까지 거리는 이전 노드까지 거리에서 1을 더한 값. 가중치
                    if dist[ny][nx] > dist[y][x] + 1:
                        dist[ny][nx] = dist[y][x] + 1
                        heapq.heappush(heap, [ny, nx])
                else: #0인 경우 해당 노드까지 거리는 이전 노드까지 거리와 같음
                    if dist[ny][nx] > dist[y][x]:
                        dist[ny][nx] = dist[y][x]
                        heapq.heappush(heap, [ny, nx])
# 기본세팅
m, n = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)] #미로저장
dist = [[INF] * m for _ in range(n)] #2차월 배열로 각 미로의 칸마다 해당칸까지의 거리를 저장하는 공간

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

dijkstra()

print(dist[n - 1][m - 1]) #목적지인 노드까지의 거리 출력. (4.2)의 경우 실제로는 (3,2)에 존재하기에 1씩 빼줌
# 가중치가 0과 1로만 이뤄진 경우 BFS가 다익스트라보다 빠르다고 함. BFS가 풀이 시간 더 짧음
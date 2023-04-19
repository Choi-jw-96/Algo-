# dfs로 노력해봤으나 시간 관계상 전체탐색 방향을 시간초과로 통과를 하지 못함
# visited는 따로 필요 없는 문제라 사용 X
# from collections import deque가 그냥 import deque 보다 빠름
from collections import deque
import sys
input = sys.stdin.readline

# 3차원이니 z를 사용
dz = [0, 0, 0, 0, 1, -1]
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]

def bfs():
    global day
    while queue:
        # 먼저 들어온 순서대로 빼준다
        z, x, y = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and graph[nz][nx][ny] == 0:
                queue.append((nz, nx, ny))
                # 날짜를 뽑기위해 지정 날짜로 부터 하루씩 더해준다
                graph[nz][nx][ny] = graph[z][x][y] + 1
                if day < graph[nz][nx][ny]:
                    # day를 0으로 지정했기때문에 -1, day를 1로 지정한다면 없어도 된다
                    day = graph[nz][nx][ny]-1


m, n, h = map(int, input().split())
graph = []
queue = deque([])

# 3차원리스트로 받아주면서 queue에 익은 토마토의 장소를 저장해준다
# 똑같은 문장을 쓰지 않으려고 여기서 받음으로써 시간 단축
for z in range(h):
    graph1 = []
    for x in range(n):
        graph1.append(list(map(int, input().split())))
        for y in range(m):
            if graph1[x][y] == 1:
                queue.append((z, x, y))
    graph.append(graph1)

# bfs 이후 모두 돌면서 max를 사용하는 것보다 빠를 것 같아 day 사용
day = 0      
bfs()

# 안익읕 토마토가 있는지 확인하고 결과 값을 출력
for z in range(h):
    for x in range(n):
        if 0 in graph[z][x]:
            print(-1)
            # 모든 것을 종료(2중 for문 전체 종료) ↔ break는 for문 하나만 종료
            exit()
        if z == h-1 and x == n-1:
            print(day)

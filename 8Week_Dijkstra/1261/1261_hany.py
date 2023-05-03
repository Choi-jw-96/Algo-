# 1261번 알고스팟
## 문제
'''
미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다.
미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.

알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 즉, 여러 명이 다른 방에 있을 수는 없다.

어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다.
즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다.
단, 미로의 밖으로 이동 할 수는 없다.

벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다.
벽을 부수면, 빈 방과 동일한 방으로 변한다.

현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성
'''

## 접근방법
'''
0은 빈 방, 1은 벽
최대한 0으로 가되, 갈 곳이 없으면 1을 0으로 바꾸고 카운팅한다.
많이 걸어도 상관 없되, 벽은 최소로 부수라는 뜻
그니까 0부터 가게 만들고, 0이 없으면 그제서야 1인 곳을 0으로 바꾸고 움직이기.
결국, 최솟값을 찾아서 움직이는과 동일하므로 다익스트라로 풀 수 있다.
'''
import heapq
m, n = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]
distance = [[1e9] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0
    while q:
        cost, x, y = heapq.heappop(q)
        if cost > distance[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < m:
                c = cost + miro[nx][ny]
                if c < distance[nx][ny]:
                    distance[nx][ny] = c
                    heapq.heappush(q, (distance[nx][ny], nx, ny))
dijkstra()
print(distance[n - 1][m - 1])
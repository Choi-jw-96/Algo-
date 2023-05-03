# 4485번 녹색 옷 입은 애가 젤다지?
## 문제
'''
소지한 루피가 감소하게 된다!
도둑루피만 가득한 N x N 크기의 동굴의 제일 왼쪽 위에 있다. [0][0]번 칸이기도 하다. 
이 동굴의 반대편 출구, 제일 오른쪽 아래 칸인 [N-1][N-1]까지 이동해야 한다. 

동굴의 각 칸마다 도둑루피가 있는데, 이 칸을 지나면 해당 도둑루피의 크기만큼 소지금을 잃게 된다.
링크는 잃는 금액을 최소로 하여 동굴 건너편까지 이동해야 하며,
한 번에 상하좌우 인접한 곳으로 1칸씩 이동할 수 있다.
링크가 잃을 수밖에 없는 최소 금액은 얼마일까?
'''
## 접근방법
'''
최소금액만 잃도록 움직여야한다.
델타검색 활용
'''
import heapq
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    q = []
    heapq.heappush(q, (cave[0][0], 0, 0))
    dist[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        # 끝에 도달하면
        if x == n - 1 and y == n - 1:
            print(f'Problem {cnt}: {dist[x][y]}')
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                nc = cost + cave[nx][ny]

                if nc < dist[nx][ny]:
                    dist[nx][ny] = nc
                    heapq.heappush(q, (nc, nx, ny))

cnt = 1
INF = int(1e9)

while True:
    n = int(input())
    # n값이 0으로 주어지면 바로 종료
    if n == 0:
        exit()
    cave = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]

    dijkstra()
    cnt += 1









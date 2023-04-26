# 우선순위 큐 구현
import sys, heapq
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1,]


def coin():
    # 시작값은 0
    move[0][0] = 0
    queue = []
    # 시작 노드부터 탐색을 시작하기 위해
    heapq.heappush(queue, [cave[0][0], 0, 0])

    # queue안에 남아있는 노드가 없으면 끝 
    while queue:
        have_coin, x, y = heapq.heappop(queue)
        if x == n - 1 and y == n - 1:
            print(f'Problem {cnt}: {move[x][y]}')
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 해당 코인보다 덜 먹는 경로라면 저장
            if 0 <= nx < n and 0 <= ny < n and move[nx][ny] > have_coin + cave[nx][ny]:
                move[nx][ny] =  have_coin + cave[nx][ny]
                heapq.heappush(queue, [move[nx][ny], nx, ny])

cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(n)]
    move = [[int(10e9)] * n for _ in range(n)]

    coin()
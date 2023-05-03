import sys, heapq
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def go(i, j):
    visited[i][j] = 0
    queue = []
    # 힙을 사용하여 최대한 적은 벽으로 움직이는것 먼져 나오게 한다
    # 시작점을 넣어준다
    heapq.heappush(queue, [int(miro[i][j]), i, j])

    # queue가 필때까지
    while queue:
        wall, x, y = heapq.heappop(queue)
        # 원하는 위치에 오면 멈춰라
        if x == X - 1 and y == Y - 1:
            print(wall)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 안에서 visited에 등록 된것 보다 적에 움직인 것만 넣어줘라
            if 0 <= nx < X and 0 <= ny < Y and visited[nx][ny] > wall + int(miro[nx][ny]):
                visited[nx][ny] = wall + int(miro[nx][ny])
                heapq.heappush(queue, [visited[nx][ny], nx, ny])


Y, X = map(int, input().split())

miro = [list(input()) for _ in range(X)]
visited = [[int(10e9)] * Y for _ in range(X)]

go(0, 0)
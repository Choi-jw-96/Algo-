from collections import deque

# BFS 메서드
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    cnt = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    return cnt

# input 값 받아서 이차원리스트 만들기
n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
for i in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

# max_food의 크기
max_food = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            # 리스트를 돌다가 한 지점에서의 bfs return값(쓰레기 크기)가 max_food보다 크면 max_food값 대체
            max_food = max(max_food, bfs(i, j))
print(max_food)
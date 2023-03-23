from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx,ny))

n = int(input())
graph = [list(input()) for _ in range(n)]
queue = deque()

# 적록색약 아닌 경우
visited = [[False] * n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt1 += 1

# 적록색약인 경우 - G를 R로 모두 대체
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
visited = [[False] * n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt2 += 1

print(cnt1, cnt2)
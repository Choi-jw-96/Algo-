# 예시 코드는 맞으나 정답은 아님
# 다시 풀어봐야 함

from collections import deque

# BFS 메서드
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    cnt = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    if cnt != 0: cnt += 1
    return cnt

# input 값 받아서 이차원리스트 만들기
# grpah input이 공백 구분이 아니기에 추가 작업 진행
n = int(input())
visited = [[False] * n for _ in range(n)]
graph = []
for _ in range(n):
    str = input()
    line = []
    for a in range(n):
        line.append(int(str[a]))
    graph.append(line)

# 총 단지수와 단지내 집수 cnt_list에 담아서 출력
cnt_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result = bfs(i,j)
            if result > 0:
                cnt_list.append(result)
cnt_list.sort()
print(len(cnt_list))
print(*cnt_list, sep='\n')
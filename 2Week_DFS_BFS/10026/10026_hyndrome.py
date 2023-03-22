# 분류: 2주차 BFS / DFS
# 문제: 백준 10026 적록색맹
# 문제 주소: https://www.acmicpc.net/problem/10026
# 푼 사람: 진홍엽
# 설명: bfs 델타탐색
import sys
from collections import deque
# 델타 탐색
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 문자열 여러개가 있는 리스트로 input 받기
i_n = int(sys.stdin.readline())
graph = [sys.stdin.readline().rstrip() for i_1 in range(i_n)]

# 사람(적록색약 x)의 경우
# 각 색깔별 확인을 위한 리스트 (사실 int 하나로 묶어도 되는데 확인을 위해 각 색을 리스트로 받음)
ls_human = [0, 0, 0] #[R, G, B]
# 방문을 확인하기 위한 별도의 빈 리스트 형성
ls_visited = [[False] * i_n for i_2 in range(i_n)]

for i_3 in range(i_n):
    for i_4 in range(i_n):
        # 방문하지 않은 곳을 방문한 경우
        if ls_visited[i_3][i_4] == False:
            # 방문하지 않은 곳을 방문한 경우 - 빨간색
            if graph[i_3][i_4] == 'R':
                # 해당 색 방문 카운트
                ls_human[0] += 1
                ls_visited[i_3][i_4] = True
                # BFS 탐색
                que = deque()
                que.append((i_4, i_3))
                while que:
                    x, y = que.popleft()
                    for i_5 in range(4):
                        nx = x + dx[i_5]
                        ny = y + dy[i_5]
                        if (0 <= nx < i_n) * (0 <= ny < i_n):
                            if (graph[ny][nx] == 'R') * (ls_visited[ny][nx] == False):
                                ls_visited[ny][nx] = True
                                que.append((nx, ny))
            elif graph[i_3][i_4] == 'G':
                # 해당 색 방문 카운트
                ls_human[1] += 1
                ls_visited[i_3][i_4] = True
                # BFS 탐색
                que = deque()
                que.append((i_4, i_3))
                while que:
                    x, y = que.popleft()
                    for i_5 in range(4):
                        nx = x + dx[i_5]
                        ny = y + dy[i_5]
                        if (0 <= nx < i_n) * (0 <= ny < i_n):
                            if (graph[ny][nx] == 'G') * (ls_visited[ny][nx] == False):
                                ls_visited[ny][nx] = True
                                que.append((nx, ny))
            else:
                # 해당 색 방문 카운트
                ls_human[2] += 1
                ls_visited[i_3][i_4] = True
                # BFS 탐색
                que = deque()
                que.append((i_4, i_3))
                while que:
                    x, y = que.popleft()
                    for i_5 in range(4):
                        nx = x + dx[i_5]
                        ny = y + dy[i_5]
                        if (0 <= nx < i_n) * (0 <= ny < i_n):
                            if (graph[ny][nx] == 'B') * (ls_visited[ny][nx] == False):
                                ls_visited[ny][nx] = True
                                que.append((nx, ny))
# print(ls_human)

# 소(적록색약 O)의 경우
# 각 색깔별 확인을 위한 리스트 (사실 int 하나로 묶어도 되는데 확인을 위해 각 색을 리스트로 받음)
ls_cow = [0, 0] #[R or G, B]
# 방문을 확인하기 위한 별도의 빈 리스트 형성
ls_visited = [[False] * i_n for i_2 in range(i_n)]

for i_3 in range(i_n):
    for i_4 in range(i_n):
        # 방문하지 않은 곳을 방문한 경우
        if ls_visited[i_3][i_4] == False:
            # 방문하지 않은 곳을 방문한 경우 - 빨간색 or 초록색
            if (graph[i_3][i_4] == 'R') + (graph[i_3][i_4] == 'G'):
                # 해당 색 방문 카운트
                ls_cow[0] += 1
                ls_visited[i_3][i_4] = True
                # BFS 탐색
                que = deque()
                que.append((i_4, i_3))
                while que:
                    x, y = que.popleft()
                    for i_5 in range(4):
                        nx = x + dx[i_5]
                        ny = y + dy[i_5]
                        if (0 <= nx < i_n) * (0 <= ny < i_n):
                            if ((graph[ny][nx] == 'R') + (graph[ny][nx] == 'G')) * (ls_visited[ny][nx] == False):
                                ls_visited[ny][nx] = True
                                que.append((nx, ny))
            
            else:
                # 해당 색 방문 카운트
                ls_cow[1] += 1
                ls_visited[i_3][i_4] = True
                # BFS 탐색
                que = deque()
                que.append((i_4, i_3))
                while que:
                    x, y = que.popleft()
                    for i_5 in range(4):
                        nx = x + dx[i_5]
                        ny = y + dy[i_5]
                        if (0 <= nx < i_n) * (0 <= ny < i_n):
                            if (graph[ny][nx] == 'B') * (ls_visited[ny][nx] == False):
                                ls_visited[ny][nx] = True
                                que.append((nx, ny))
# print(ls_cow)

print(sum(ls_human), sum(ls_cow))
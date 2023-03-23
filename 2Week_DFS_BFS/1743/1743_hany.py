# 1743번 음식물 피하기
'''
떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다.
선생님을 도와 제일 큰 음식물의 크기를 구해
'''
import sys
from pprint import pprint
sys.setrecursionlimit(10**6)

# 1. dfs 설정
# 델타검색을 위한 기준 리스트 설정
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 함수 설정
def dfs(x, y):
    global cnt # 전역 변수 설정
    visited[x][y] = True # 방문 기록 체크
    if hallway[x][y] == 1:
        cnt += 1

    # 네 방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if hallway[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)

        
# 2. 입력 및 초기값 설정
N, M, K = map(int, input().split()) # 세로길이 N, 가로길이 M, 음식물 쓰레기의 개수 K
visited = [[False for _ in range(M)] for _ in range(N)]

hallway = [[0 for _ in range(M)] for _ in range(N)]
# pprint(hallway)
for _ in range(K):
    r, c = map(int, input().split()) # r은 행, c는 열
    hallway[r - 1][c - 1] = 1
# pprint(hallway)


# 3. 결과 값 내기
result = 0
for x in range(N):
    for y in range(M):
        if hallway[x][y] == 1 and visited[x][y] == False:
            cnt = 0
            dfs(x, y)
            result = max(result, cnt)
print(result)


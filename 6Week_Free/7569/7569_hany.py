# 7569번 토마토
'''
토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩 넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관한다.
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.

철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
'''
# 1(익은 토마토)인 값들을 담아준다.
# 탐색 후 0인 곳에 1을 더해준다.
# 가장 큰 값 - 1 출력
# 모든 토마토가 1일 경우 0 출력
# 0이 단 하나라도 있을 시, -1 출력
# 스택 구조를 취할 것인가?
# 큐 구조를 취할 것인가?
import sys
from collections import deque
input = sys.stdin.readline


M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for i in range(H)]
ans = 0
q = deque([])

# 0. 탐색 좌표 설정(상하좌우위아래)
dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    while q:  
        # 1. 추출
        z, x, y = q.popleft()
        # 2. 범위 설정
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<= nx < N and 0<= ny < M and 0<= nz < H and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                q.append([nz, nx, ny])

# 익은 토마토 큐 쌓기
for z in range(H):
    for x in range(N):
        for y in range(M):
            if box[z][x][y] == 1:
                q.append([z, x, y])
bfs()

for z in range(H):
    for x in range(N):
        for y in range(M):
            # 익지 않은 토마토가 있으면
            if box[z][x][y] == 0:
                print(-1)
                exit()
            else:
                ans = max(ans, box[z][x][y])
                
print(ans - 1)
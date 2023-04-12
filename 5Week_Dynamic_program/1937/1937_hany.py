# 1937번 욕심쟁이 판다
'''
n * n의 크기의 대나무 숲이 있다. 
1. 욕심쟁이 판다는 어떤 지역에서 대나무를 먹기 시작한다.
2. 대나무를 다 먹어 치우면 상, 하, 좌, 우 중 한 곳으로 이동을 한다.
3. 또 그곳에서 대나무를 먹는다. 
단, 매우 욕심이 많아서 대나무를 먹고 자리를 옮기면 그 옮긴 지역에 그 전 지역보다 대나무가 많이 있어야 한다.

사육사는 어떤 지점에 처음에 풀어 놓아야 하고, 어떤 곳으로 이동을 시켜야
판다가 최대한 많은 칸을 방문할 수 있는지 고민에 빠져 있다. 

n * n 크기의 대나무 숲이 주어져 있을 때,
이 판다가 최대한 많은 칸을 이동하려면 어떤 경로를 통하여 움직여야 하는지 구하여라.
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 델타 탐색, dfs, dp

# 1. dfs 정의(dp 활용)
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 건넌적이 없는 경우만
    if dp[x][y] == 0:
        dp[x][y] = 1
        # 상하 좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 조건
            if 0<= nx < n and 0<= ny <n:
                # 문제 조건(많은 쪽으로만)
                if matrix[x][y] < matrix[nx][ny]:
                    # 기존대로 둘것인가, 먹게 할 것인가?
                    dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
        return dp[x][y]
    # 건넜다면 그대로 산출
    else:
        return dp[x][y]

# 2. 입력 및 설정
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
dp = [[0] * n for _ in range(n)]
cnt = 0

# 3. 결과 산출
for x in range(n):
    for y in range(n):
        cnt = max(cnt, dfs(x, y))
print(cnt)
    
# 1012번 유기농 배추
'''
어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다. 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.

 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.
'''
import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

from pprint import pprint
def dfs(y, x):
    # 범위 설정
    if y < 0 or y >= N or x < 0 or x >= M:
        return False
    
    # 방문하지 않았다면
    if matrix[y][x] == 1:
        # 방문하고
        matrix[y][x] = 0
        # 상하좌우도 탐색
        dfs(y + 1, x)
        dfs(y - 1, x)
        dfs(y, x - 1)
        dfs(y , x + 1)
        return True
    return False


# 행렬로 해야 하는가?
# 그렇다면 상하좌우가 연결되어 있다는 게 키포인트
# 상하좌우를 스캔하고, 인접 지점에 값이 1이면서, 아직 방문하지 않은 접점이 있으면 방문
# 방문 접점에서 다시 반복


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().rstrip().split()) # 가로길이, 세로길이, 배추 심어져 있는 위치의 개수
    
    visited = [False] * N
    matrix = [[0] * M for _ in range(N)]
    # pprint(matrix)
    for _ in range(K):
        x, y = map(int, input().rstrip().split())
        matrix[y][x] = 1
    # pprint(matrix)

    result = 0

    for j in range(N):
        for i in range(M):
            if dfs(j, i) == True:
                result += 1
    print(result)



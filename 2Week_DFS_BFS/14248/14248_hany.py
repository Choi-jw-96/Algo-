# 14248번 점프 점프
'''
영우는 지금 n개의 돌이 일렬로 놓여있는 돌다리에 있다. 그리고 돌다리의 돌에는 숫자가 하나씩 적혀있다. 영우는 이 숫자가 적혀있는 만큼 왼쪽이나 오른쪽으로 점프할 수 있는데, 이때 돌다리 밖으로 나갈 수는 없다.

영우는 이 돌다리에서 자기가 방문 가능한 돌들의 개수를 알고 싶어한다. 방문 가능하다는 것은 현재위치에서 다른 돌을 적절히 밟아 해당하는 위치로 이동이 가능하다는 뜻이다.

현재 위치가 주어졌을 때, 영우가 방문 가능한 돌들의 개수를 출력하시오.
'''

# 밟은 돌 체크 리스트, 인덱스
# 왼쪽 혹은 오른쪽으로 점프 가능 (이떄 돌다리 밖으로 나갈 수 없으므로 범위를 넘어서면 안 된다.)
# 돌의 범위 중요

# <DFS>
# 0. 입력 및 초기값 설정
import sys
sys.setrecursionlimit(10**6)

n = int(input()) # 돌다리의 돌 개수
check = [False] * n # 체크 리스트
jumps = list(map(int, input().split())) # 점프할 수 있는 거리
start = int(input()) - 1 # 출발점
cnt = 1 # 방문한 돌의 개수(초기값 1, 처음 밟은 위치)

# 1. dfs 함수 정의
def dfs(x):
    global cnt # 전역 변수 cnt 설정

    # 현재 정점에서 갈 수 있는 가용 범위는 +, - 오직 두 가지 위치
    for new_x in (x + jumps[x], x - jumps[x]): # new_x 새로운 정점
        if 0 <= new_x < n and check[new_x] == False: # 가능 범위 설정
            cnt += 1
            check[new_x] = True
            dfs(new_x)

dfs(start)
print(cnt)


# <BFS>
# 1. bfs 함수 정의
from collections import deque
def bfs(start):
    global cnt # 전역 변수
    q = deque([start])
    while q:
        cur = q.popleft() # 현재 돌의 위치
        for adj in (cur + jumps[cur], cur - jumps[cur]):
            if 0<= adj < n and check[adj] == False:
                cnt += 1
                q.append(adj)
                check[adj] = True

bfs(start)
print(cnt)
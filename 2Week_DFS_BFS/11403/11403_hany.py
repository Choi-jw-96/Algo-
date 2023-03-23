# 11403번 경로찾기
'''
가중치 없는 방향 그래프 G가 주어졌을 때, 
모든 정점 (i, j)에 대해서,
i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성

i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻
i번째 줄의 i번쨰 숫자는 항상 0

'''
# i번쨰 줄의 j번쨰 숫자가 1이라면, i에서 j로 가는 간선이 존재한다는 뜻
# 그리고 출력은 i에서 j로 가는 경로가 있냐 없냐 여부로 결정한다.
# 그게 바로 둘의 차이

#0. 입력 및 초기 설정
from pprint import pprint
import sys
input = sys.stdin.readline
N = int(input()) # 정점의 개수
matrix = []
lst = [[] for _ in range(N)]
for _ in range(N):
    nums = list(map(int, input().rstrip().split()))
    matrix.append(nums)
# print(lst)
# pprint(matrix)
# pprint(result)

# 1. 이중 포문으로 스캔하여, 값이 1인 (i, j) 값을 기록한다(인접 리스트 만들기)
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            lst[i].append(j)
# print(lst)

# 2. bfs 함수를 만든다.

from collections import deque

def bfs(start):
    visited = [0 for _ in range(N)]
    q = deque([])
    q.append(start)

    while q:
        cur = q.popleft()
        # print(cur, end = " ")
        for adj in lst[cur]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = 1
    print(*visited)

# 3. i와 j 사이에 인접접점이 있는가?(가중치 없으므로 bfs도 괜찮) -> 결국 그래프로 연결되어있는가
for n in range(N):
    bfs(n)
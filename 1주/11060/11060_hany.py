# 11060번 점프점프
'''
재환이가 1*N 크기의 미로에 갇혀있다. 미로는 1*1 크기의 칸으로 이루어져 있고, 각 칸에는 정수가 하나 쓰여 있다. i번째 칸에 쓰여 있는 수를 Ai라고 했을 때, 재환이는 Ai이하만큼 오른쪽으로 떨어진 칸으로 한 번에 점프할 수 있다. 예를 들어, 3번째 칸에 쓰여 있는 수가 3이면, 재환이는 4, 5, 6번 칸 중 하나로 점프할 수 있다.

재환이는 지금 미로의 가장 왼쪽 끝에 있고, 가장 오른쪽 끝으로 가려고 한다. 이때, 최소 몇 번 점프를 해야 갈 수 있는지 구하는 프로그램을 작성하시오. 만약, 가장 오른쪽 끝으로 갈 수 없는 경우에는 -1을 출력한다.
'''
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
jumps = list(map(int, input().split()))

# 끝끝내 n번째에 가지 못하면 -1 출력
# 완전탐색(모든 경우의 수)으로 n번째로 가는 최소값을 구하라.
# dfs냐, bfs냐?
# 그래프를 그려봤을 떄, 같은 층을 탐색하며 가는 게 더 적합하므로 bfs

# 1. 방문 지점을 체크하는 방법 + 몇 번의 점프로 해당 지점까지 갈 수있는지 기록

## 현재 위치 인덱스와 가용 점프 횟수
cur, jump = 0, 0

## 자료구조 '큐'를 활용하기 위한 셋팅
queue = deque()
queue.append((cur, jump))
# print(queue)

## 방문 기록지 셋팅
visited = []

## bfs 시전

while queue: # 큐가 빌 때까지
    cur, jump = queue.popleft() # 현 위치와 가용 점프 횟수
	
    # jumps[cur]가 마지막이라면 jump를 프린트하고 while을 끝내라.
    # 근데 만약 exit()가 발휘되지 않는다면 while문 바깥에 print(-1)
    if cur == N - 1:
       print(jump)
       sys.exit()

    # 해당 위치의 점프 경우의 수를 모두 돌린다.
    for i in range(1, jumps[cur] + 1):

        # 다음 위치로 셋팅해주고
        new_cur = cur + i
        # print(new_cur)

        # 그 위치가 visited에 포함되어 있지 않다면
        if new_cur not in visited:
            # 해당 위치의 점프 경우의 수를 합한 값과, 점프 횟수 + 1
            queue.append((new_cur, jump + 1))
            # print(queue)
            visited.append(new_cur)
            # print(visited)


# 2. 끝끝내 방문하지 못하면 -1
print(-1)


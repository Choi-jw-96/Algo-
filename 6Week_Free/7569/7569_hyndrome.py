# 분류: 6주차 자유주제
# 문제: 백준 7569 토마토
# 문제 주소: https://www.acmicpc.net/problem/7569
# 푼 사람: 진홍엽
# 설명: 3차원그래프 델타탐색 DFS

# dfs 활용을 위한 deque import
import sys
from collections import deque

# input 받기
# 현재 토마토의 배열을 3차원 리스트로 받음
# 배열이 1일 때(익은 토마토일 때), queue에 추가
i_m, i_n, i_h = map(int, sys.stdin.readline().split())
ls_tomato = []
que_tomato = deque()
for z in range(i_h):
    ls_tomato_xy = []
    for y in range(i_n):
        ls_tomato_x = []
        ls_input = list(map(int, sys.stdin.readline().split()))
        for x in range(i_m):
            ls_tomato_x.append(ls_input[x])
            if ls_input[x] == 1:
                que_tomato.append((x,y,z))
        ls_tomato_xy.append(ls_tomato_x)
    ls_tomato.append(ls_tomato_xy)

# 델타 탐색
delta = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

# DFS, 다음 토마토로 익을 때마다 1씩 추가
while que_tomato:
    tomato = que_tomato.popleft()
    for i in range(6):
        nx = tomato[0] + delta[i][0]
        ny = tomato[1] + delta[i][1]
        nz = tomato[2] + delta[i][2]
        if (0 <= nx < i_m) and (0 <= ny < i_n) and (0 <= nz < i_h):
            if ls_tomato[nz][ny][nx] == 0:
                ls_tomato[nz][ny][nx] = ls_tomato[tomato[2]][tomato[1]][tomato[0]] + 1
                que_tomato.append((nx, ny, nz))

# DFS 이후 결과 탐색
# 0이 있는지 여부 (안익은 토마토의 여부)와 최대로 걸린 시점을 확인
tomato_max = 1
bool_break = False
for z in range(i_h):
    for y in range(i_n):
        for x in range(i_m):
            if ls_tomato[z][y][x] == 0:
                bool_break = True
            elif ls_tomato[z][y][x] > tomato_max:
                tomato_max = ls_tomato[z][y][x]
# 위의 탐색 결과에 따라 결과 출력
if bool_break == True:
    print(-1)
else:
    print(tomato_max - 1)
# print(ls_tomato)
# print(ls_record)
# print(que_tomato)
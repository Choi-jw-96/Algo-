# 분류: 2주차 BFS / DFS
# 문제: 백준 2667 단지번호붙이
# 문제 주소: https://www.acmicpc.net/problem/2667
# 푼 사람: 진홍엽
# 설명: dfs 로컬변수 델타탐색
from collections import deque
import sys

sys.setrecursionlimit(100000)

i_n = int(sys.stdin.readline())
graph = [[int(s_1) for s_1 in sys.stdin.readline().rstrip()] for i_1 in range(i_n)]
i_cnt = 0
ls_cnt = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs_cnt(x, y):
    i_dfs_cnt = 0
    def dfs (x, y):
        if graph[y][x] == 1:
            graph[y][x] = 0
            nonlocal i_dfs_cnt 
            i_dfs_cnt += 1
            for i_3 in range(4):
                nx = x + dx[i_3]
                ny = y + dy[i_3]
                if (0 <= nx < i_n) * (0 <= ny < i_n):
                    dfs(nx, ny)
    dfs(x, y)
    return i_dfs_cnt

for i_4 in range(i_n):
    for i_5 in range(i_n):
        if graph[i_4][i_5] == 1:
            i_cnt += 1
            ls_cnt.append(dfs_cnt(i_5, i_4))

ls_cnt.sort()
print(len(ls_cnt))
for i_6 in ls_cnt:
    print(i_6)
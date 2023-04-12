# 분류: 5주차 DP
# 문제: 백준 1937 욕심쟁이팬더
# 문제 주소: https://www.acmicpc.net/problem/1937
# 푼 사람: 진홍엽
# 설명: DFS 델타탐색 DP 재귀 

# https://my-coding-notes.tistory.com/315

import sys
sys.setrecursionlimit(10**6)

i_n = int(sys.stdin.readline())
ls_bamboo = [list(map(int, sys.stdin.readline().split())) for i in range(i_n)]

# DP에 해당 지점에 DFS를 진행했을 때, 최대로 움직일 수 있는 칸 기록
dp = [[0]*i_n for i in range(i_n)]
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(x, y):
    if dp[y][x] == 0:
        dp[y][x] = 1
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if (0 <= nx < i_n) and (0 <= ny < i_n):
                if ls_bamboo[ny][nx] > ls_bamboo[y][x]:
                    dp[y][x]  = max(dp[y][x], dfs(nx, ny) + 1)
    return dp[y][x]

ans = 0
for y in range(i_n):
    for x in range(i_n):
        ans = max(ans, dfs(x, y))

print(dp)
print(ans)      
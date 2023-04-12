# 분류: 5주차 DP
# 문제: 백준 2579  계단오르기
# 문제 주소: https://www.acmicpc.net/problem/2579
# 푼 사람: 진홍엽
# 설명: DP

# https://great-park.tistory.com/49
# bottomup
import sys

i_n = int(sys.stdin.readline())
# 밑에서 dp[i-3] 인덱싱 때문에 편의로 [0]을 하나 더 추가
ls_stair = [0] + [int(sys.stdin.readline()) for i in range(i_n)]

dp = [0] * (i_n + 1)
dp[1] = ls_stair[1]
dp[2] = dp[1] + ls_stair[2]

for i in range(3, i_n+1):
    # i번째 계단을 1칸 건너서 올라온 경우 vs 바로 올라온 경우
    dp[i] = max(dp[i-2], dp[i-3] + ls_stair[i-1]) + ls_stair[i]

print(dp[i_n])
print(dp)
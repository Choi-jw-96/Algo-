# 분류: 5주차 DP
# 문제: 백준 14501 퇴사
# 문제 주소: https://www.acmicpc.net/problem/14501
# 푼 사람: 진홍엽
# 설명: DP

# https://great-park.tistory.com/48#recentComments
# bottomup
i_n = int(input())

consulting = [tuple(map(int, input().split())) for _ in range(i_n)]

dp = [0] * (i_n + 1)

for i in range(i_n):
    for j in range(i + consulting[i][0], i_n+1):
        if dp[j] < dp[i] + consulting[i][1]:
            dp[j] = dp[i] + consulting[i][1]
            # print(dp)
print(dp[-1])


# topdown
i_n = int(input())

consulting = [tuple(map(int, input().split())) for _ in range(i_n)]

dp = [0] * (i_n + 1)

for i in range(i_n-1, -1, -1):
    if i + consulting[i][0] > i_n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], consulting[i][1] + dp[i + consulting[i][0]])
    # print(dp)
print(dp[0])

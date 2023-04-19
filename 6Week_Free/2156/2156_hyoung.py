# 2156

n = int(input())
wines = [0] + [int(input()) for _ in range(n)] + [0]
dp = [0] * (n+2)
# n이 1일 때 wines[2] 인덱스에러
dp[1] = wines[1]
dp[2] = dp[1] + wines[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-3]+wines[i-1]+wines[i], dp[i-2]+wines[i], dp[i-1])
print(dp[n])
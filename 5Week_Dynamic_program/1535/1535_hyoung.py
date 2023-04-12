# 1535 안녕

n = int(input())
hp = [0] + list(map(int, input().split()))
happy = [0] + list(map(int, input().split()))

dp = [[0] * 101 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 101):
        if hp[i] <= j: # i번째 사람에게 인사를 하고 소모량보다 체력j가 클 때 기쁨 계산
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - hp[i]] + happy[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])
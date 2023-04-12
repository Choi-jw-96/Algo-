n = int(input())
lose_HP = [0] + list(map(int, input().split()))
be_happy = [0] + list(map(int, input().split()))

dp = [[0] * 101 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 101):
        if lose_HP[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - lose_HP[i]] + be_happy[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])
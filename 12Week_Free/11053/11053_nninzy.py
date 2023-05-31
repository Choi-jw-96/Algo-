n = int(input())
list_a = list(map(int, input().split()))

dp = list(0 for _ in range(n))

for i in range(n):
    for j in range(i):
        if list_a[i] > list_a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))

n = int(input())

t_list = []
p_list = []
dp = [0] * (n+1)

for i in range(n):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

for i in range(n - 1, -1, -1):
    if t_list[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(p_list[i] + dp[i+t_list[i]], dp[i+1])
        
print(dp[0])
# 2579 계단 오르기

n = int(input())
height = [int(input()) for _ in range(n)]
dp = [0]*(n)
if len(height)<=2: 
    print(sum(height))
else: 
    dp[0]=height[0] 
    dp[1]=height[0]+height[1] 
    for i in range(2,n): 
        dp[i]=max(dp[i-3]+height[i-1]+height[i], dp[i-2]+height[i])
    print(dp[-1])
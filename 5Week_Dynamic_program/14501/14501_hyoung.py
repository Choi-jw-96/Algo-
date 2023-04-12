# 14501 퇴사

N = int(input())

T = []
P = []
dp = [0 for _ in range(N+1)]

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N-1, -1, -1): 
    if T[i] + i > N: # 퇴사일을 넘어가면
        dp[i] = dp[i+1] 
    
    else:
        dp[i] = max(dp[i+1], dp[T[i] + i] + P[i]) 
print(dp[0])

n = int(input())
a = list(map(int, input().split()))
# 입력
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        # 숫자가 크다면
        if a[i] > a[j]:
            # 큰수를 저장한다
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
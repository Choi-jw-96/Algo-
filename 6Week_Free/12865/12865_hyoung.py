# 12865 평범한 배낭

n, k = map(int, input().split()) 
dp = [[0] * (k+1) for _ in range(n+1)]
bag = [[0, 0]]
for i in range(n):
    w, v = map(int, input().split())  
    bag.append([w, v])

for i in range(1, n+1):
    w = bag[i][0]
    v = bag[i][1]
    for j in range(1, k+1):
        if j < w:  # 현재 물건을 넣을 수 없으므로 최적값은 이전 물건까지만 고려했을 때의 값
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
print(dp[n][k])



# 재귀예시
def knapsack2(i, W, w, p):
  if (i <= 0 or W <= 0):
    return 0
  if (w[i] > W):
    return knapsack2(i - 1, W, w, p)
  else: # w[i] <= W
    left = knapsack2(i - 1, W, w, p)
    right = knapsack2(i - 1, W - w[i], w, p)
    return max(left, p[i] + right)

W = 30
w = [0, 5, 10, 20]
p = [0, 50, 60, 140]
profit = knapsack2(len(w)-1, W, w, p)
print(profit)

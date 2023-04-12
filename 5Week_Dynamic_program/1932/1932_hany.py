# 1932번 정수 삼각형
'''
맨 위층부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때,
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.
'''

n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))
# print(dp)
# dp[0] = dp[0][0]
# dp[1] = dp[0][0] + dp[1][0] or dp[0][0] + dp[1][1]
# dp[2] = max(dp[1][0] + dp[2][1], dp[1][1] + dp[2][1])
# 양 끝은 쭉 내려가면 되고, 가운데들은 max로 선별해야함

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] += dp[i - 1][j]
        elif j == i:
            dp[i][j] += dp[i - 1][j - 1]
        else:
            dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1])
print(max(dp[n - 1]))
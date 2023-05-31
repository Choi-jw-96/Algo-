# 분류: 12주차 자유주제
# 문제: 백준 11053 가장긴증가하는부분수열
# 문제 주소: https://www.acmicpc.net/problem 11053
# 푼 사람: 진홍엽
# 설명: dp
# 평점: 3.5/5
i_n = int(input())
ls_a = list(map(int, input().split()))
dp = [(0, 0) for _ in range(i_n)]
dp[0] = (ls_a[0], 1)

for i in range(1, i_n):
    cnt = 0
    for j in range(0, i):
        if ls_a[i] > dp[j][0]:
            if cnt < dp[j][1]:
                cnt = dp[j][1]
    dp[i] = (ls_a[i], cnt + 1)

v_max = max(dp, key= lambda x: x[1])
print(max(dp, key= lambda x: x[1])[1])
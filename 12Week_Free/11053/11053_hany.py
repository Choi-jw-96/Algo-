# 11053번 가장 긴 증가하는 부분 수열
'''
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
'''
n = int(input())
lst = list(map(int, input().split()))

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        # print(i, j)
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
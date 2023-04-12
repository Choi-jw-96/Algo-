# 분류: 5주차 DP
# 문제: 백준 1535 안녕
# 문제 주소: https://www.acmicpc.net/problem/1535
# 푼 사람: 진홍엽
# 설명: 백팩 DP

# https://gsmesie692.tistory.com/113?category=523232

i_n = int(input())
ls_damage = [0] + list(map(int, input().split()))
ls_pleasure = [0] + list(map(int, input().split()))

dp = [[0] * 100 for i_1 in range(i_n + 1)]

for person in range(1, i_n + 1):
    for stamina in range(1, 100):
        if ls_damage[person] <= stamina:
            dp[person][stamina] = max(dp[person - 1][stamina], dp[person - 1][stamina - ls_damage[person]] + ls_pleasure[person])
        else:
            dp[person][stamina] = dp[person - 1][stamina]

print(dp[i_n][99])
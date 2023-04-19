# 12865번 평범한 배낭
'''
가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.
준서가 여행에 필요하다고 생각하는 N개의 물건이 있다.
각 물건은 무게 W와 가치 V를 가지는데,
해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 

아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = [(0, 0)]
for _ in range(n):
    w, v = map(int, input().split())
    bag.append((w, v))
# 무게: bag[i][0], 가치: bag[i][1]
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = bag[i][0]
        value = bag[i][1]

        # 들 수 있는 경우보다 물건의 무게가 무거울 경우
        if j < weight:
            # 이전 가방의 최적값 그대로 대입
            dp[i][j] = dp[i - 1][j]
        # 아니라면
        else:
            # 이전 가방의 최적 값 vs 현 물건 가치 + 이전 물건에서 무게 - 물건 무게를 했을 때의 최적 값
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])
print(dp[n][k])
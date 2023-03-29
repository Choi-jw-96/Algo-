# 기초세팅
N, K = map(int, input().split())
result = 0
coins = []

# 동전가치 input 받기 + 내림차순 정렬
for _ in range(N):
    coin = int(input())
    coins.append(coin)
coins.sort(reverse=True)

for c in coins:
    if K == 0: break
    result += K // c
    K %= c
print(result)
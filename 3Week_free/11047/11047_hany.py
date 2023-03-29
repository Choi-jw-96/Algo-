# 11047번 동전 0
'''
준규가 가지고 있는 동전은 총 N종류
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성
'''
import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())

coins = []
for _ in range(N):
    coins.append(int(input().rstrip()))
# print(coins)
result = 0
remainder = K
for coin in coins[::-1]:
    if coin <= K:
        result += remainder // coin
        remainder = remainder % coin
print(result)
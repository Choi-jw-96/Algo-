# 13305 주유소

import sys

n = int(input())
length_ls = list(map(int, sys.stdin.readline().split()))
price_ls = list(map(int, sys.stdin.readline().split()))

# 각 주유소에서의 기름값을 최적의 기름값으로 바꿈
for i in range(n-1):
    if price_ls[i] <= price_ls[i+1]:
        price_ls[i+1] = price_ls[i]

total = 0
for i in range(n-1):
    total += length_ls[i] * price_ls[i]
print(total)

# 2512 예산

import sys

N = int(input())
costs = list(map(int, sys.stdin.readline().split()))
budgets = int(input()) 
start, end = 0, max(costs) 

while start <= end:
    mid = (start+end) // 2
    total = 0 
    for cost in costs:
        if cost > mid:
            total += mid
        else:
            total += cost
    if total <= budgets: # 지출 양이 예산 보다 작으면 키워야됨
        start = mid + 1
    else: 
        end = mid - 1
print(end)
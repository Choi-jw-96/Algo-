# 1654 랜선 자르기

import sys
 
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)] 

start, end = 1, max(lan)
 
while start <= end: 
    mid = (start + end) // 2 
    cnt = 0 
    for i in lan:
        cnt += i // mid # 랜선을 자른 수
    if cnt >= N: # 랜선을 자른 수가 만들어야될 랜선의 수보다 클 경우 
        start = mid + 1 
    else: 
        end = mid - 1 
print(end)
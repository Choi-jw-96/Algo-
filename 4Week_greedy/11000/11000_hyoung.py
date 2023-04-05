# 11000 강의실 배정

import sys
import heapq

n =  int(input())
ls = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ls.sort()

end = []
heapq.heappush(end, ls[0][1]) 

for i in range(1, n):
  if ls[i][0] < end[0]:
    heapq.heappush(end, ls[i][1])
  else: 
    heapq.heappop(end)
    heapq.heappush(end, ls[i][1])

print(len(end))

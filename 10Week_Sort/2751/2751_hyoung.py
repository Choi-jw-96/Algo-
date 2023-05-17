import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for n in range(N):
    num = int(sys.stdin.readline())
    heapq.heappush(heap, num)

while True:
    print(heapq.heappop(heap))
    if heap == []:
        break
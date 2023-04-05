import sys, heapq
input = sys.stdin.readline

n = int(input())
li = []

for _ in range(n):
    start, end = map(int, input().split())
    li.append([start, end])

li.sort()

li_queue = []
heapq.heappush(li_queue, li[0][1])

for i in range(1, n):
    if li[i][0] < li_queue[0]:
        heapq.heappush(li_queue, li[i][1])
    else:
        heapq.heappop(li_queue)
        heapq.heappush(li_queue, li[i][1])
print(len(li_queue))
# ㄴㅇ0ㅇㄱ!!!!
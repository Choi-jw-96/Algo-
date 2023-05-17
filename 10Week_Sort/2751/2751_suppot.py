import heapq
nums = []

for _ in range(int(input())):
    nums.append(int(input()))

heapq.heapify(nums)

for _ in range(len(nums)):

    print(heapq.heappop(nums))
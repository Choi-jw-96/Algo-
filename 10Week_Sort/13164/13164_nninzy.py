n, k = map(int, input().split())
heights = list(map(int, input().split()))

costs = []
for i in range(1, n):
    costs.append(heights[i] - heights[i-1])

costs.sort(reverse=True)
print(sum(costs[k-1:]))
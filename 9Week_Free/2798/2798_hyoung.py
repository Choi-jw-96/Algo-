# 2798 블랙잭

N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
total_list = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            total = nums[i] + nums[j] + nums[k]
            if total <= M:
                total_list.append(total)
print(max(total_list))
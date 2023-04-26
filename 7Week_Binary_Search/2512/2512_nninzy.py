n = int(input())
n_list = [*map(int, input().split())]
m = int(input())
start, end = 0, max(n_list)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in n_list:
        if i >= mid: total += mid
        else: total += i
    if total <= m: start = mid + 1
    else: end = mid - 1
print(end)
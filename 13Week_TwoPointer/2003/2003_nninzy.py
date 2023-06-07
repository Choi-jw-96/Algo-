n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 1

cnt = 0

while (start <= end and end <= n):
    total = sum(arr[start:end])
    if (total < m):
        end += 1
    elif (total > m):
        start += 1
    else:
        cnt += 1
        end += 1

print(cnt)
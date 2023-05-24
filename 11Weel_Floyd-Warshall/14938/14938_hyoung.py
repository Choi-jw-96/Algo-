INF = int(1e9)

N, M, R = map(int, input().split())
area = list(map(int, input().split()))
arr = [[INF] * N for _ in range(N)]

for _ in range(R):
    start, end, dist = map(int, input().split())
    arr[start-1][end-1] = min(arr[start-1][end-1], dist)
    arr[end-1][start-1] = min(arr[end-1][start-1], dist)

for k in range(N):
    for a in range(N):
        for b in range(N):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])
            if a == b:
                arr[a][b] = 0
max_value = 0
for i in range(N):
    temp = 0
    for j in range(N):
        if arr[i][j] <= M:
            temp += area[j]

    max_value = max(max_value, temp)
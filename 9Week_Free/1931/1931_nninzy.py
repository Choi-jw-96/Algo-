n = int(input())
time = []

last_time = 0
cnt = 0

for _ in range(n):
    meeting = list(map(int, input().split()))
    time.append(meeting)

time = sorted(time, key=lambda a: a[0])
time = sorted(time, key=lambda a: a[1])

for start, end in time:
    if start >= last_time:
        cnt += 1
        last_time = end

print(cnt)
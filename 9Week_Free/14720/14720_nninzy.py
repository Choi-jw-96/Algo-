n = int(input())
info = list(map(int, input().split()))

cnt = 0
last = -1

for i in range(n):
    if info[i] == last + 1:
        cnt += 1
        last = info[i]
        if last == 2:
            last = -1

print(cnt)
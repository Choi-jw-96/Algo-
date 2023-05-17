t = int(input())
for _ in range(t):
    n = int(input())
    n_list = []
    for _ in range(n):
        a,b = map(int, input().split())
        n_list.append([a,b])
    n_list.sort(key = lambda x: x[1])
    mini = n_list[0][0]

    cnt = 1
    for i in range(1, n):
        if n_list[i][0] < mini:
            mini = n_list[i][0]
            cnt += 1
    print(cnt)
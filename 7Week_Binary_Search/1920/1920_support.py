n = int(input())
n_li = sorted(list(map(int, input().split())))
m = int(input())
m_li = list(map(int, input().split()))

for i in m_li:
    start, end = 0, n-1
    while True:
        mid = (start + end) // 2
        if n_li[mid] == i:
            print(1)
            break
        if start >= end:
            print(0)
            break
        if n_li[mid] < i:
            start = mid + 1
        else:
            end = mid - 1

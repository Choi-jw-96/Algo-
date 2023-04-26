k, n = map(int, input().split())
k_list = []

for i in range(k):
    k_list.append(int(input()))

start = 1
end = max(k_list)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(k):
        cnt += k_list[i] // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)

# 틀린풀이
# 반례 5 10 / 1 / 100 / 100 / 100 / 100 (정답은 33인데 1이 나옴)
# k, n = map(int, input().split())
# k_list = [int(input()) for _ in range(k)]

# cut = min(k_list)
# cnt = 0
# while (cnt < n):
#     for i in k_list:
#         cnt += i // cut
#     if cnt >= n:
#         break
#     else:
#         cut -= 1
#         cnt = 0
# print(cut)
# 분류: 7주차 이분탐색
# 문제: 백준 2776 암기왕
# 문제 주소: https://www.acmicpc.net/problem/2776
# 푼 사람: 진홍엽
# 설명: 이분탐색 hashset


# hash_set을 이용한 풀이 1512 ms
# import sys


# i_t = int(sys.stdin.readline())

# for case in range(i_t):
#     i_n = int(sys.stdin.readline())
#     set_n = set(map(int, sys.stdin.readline().split()))
#     i_m = int(sys.stdin.readline())
#     ls_m = list(map(int, sys.stdin.readline().split()))
#     for i in ls_m:
#         if i in set_n:
#             print(1)
#         else:
#             print(0)


# 이분탐색을 이용한 풀이 7104ms (최적화는 잘 안된듯)
import sys


i_t = int(sys.stdin.readline())

for case in range(i_t):
    i_n = int(sys.stdin.readline())
    ls_n = list(map(int, sys.stdin.readline().split()))
    ls_n.sort()
    i_m = int(sys.stdin.readline())
    ls_m = list(map(int, sys.stdin.readline().split()))

    for i in ls_m:
        bool_in = False
        def bi_search(start, end, target):
            global bool_in
            mid = (start + end) // 2
            if start <= end:
                if ls_n[mid] == target:
                    bool_in = True
                elif ls_n[mid] > target:
                    bi_search(start, mid - 1, target)
                else:
                    bi_search(mid + 1, end, target)
        bi_search(0, len(ls_n) - 1, i)
        if bool_in:
            print(1)
        else:
            print(0)
# 분류: 7주차 이분탐색
# 문제: 백준 1920 수찾기
# 문제 주소: https://www.acmicpc.net/problem/1920
# 푼 사람: 진홍엽
# 설명: 이분탐색 hashset


i_n = int(input())
ls_input = list(map(int, input().split()))
i_m = int(input())
ls_check = list(map(int, input().split()))


#  슈퍼 컴퓨터는 가능한 풀이
# ls_total = [0] * (2**32 + 1)
# for i in ls_input():
#     ls_total[i + 2**31] = 1

# for i in ls_check:
#     if ls_total[i + 2**31]:
#         print(1)
#     else:
#         print(0)

# 얌전하게 이분탐색
# 이분 탐색을 위한 리스트의 정렬
ls_input.sort()

for i in ls_check:
    start = 0
    end = i_n - 1

    while start <= end:
        mid = (start + end) // 2
        if ls_input[mid] == i:
            print(1)
            break
        elif i < ls_input[mid]:
            end = mid - 1
        elif i > ls_input[mid]:
            start = mid + 1
    else:
        print(0)

# set의 in 시간복잡도는 list의 O(n)과 다르게 O(1)이라서 해당 연산을 빠르게 할 수 있다 hashset
i_n = int(input())
set_n = set(map(int, input().split()))
i_m = int(input())
ls_m = list(map(int, input().split()))

for i in list(ls_m):
    if i in set_n:
        print(1)
    else:
        print(0)
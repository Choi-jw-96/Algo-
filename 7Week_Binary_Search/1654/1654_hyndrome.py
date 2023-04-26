# 분류: 7주차 이분탐색
# 문제: 백준 1654 랜선자르기
# 문제 주소: https://www.acmicpc.net/problem/1654
# 푼 사람: 진홍엽
# 설명: 이분탐색


import sys
i_k , i_n = map(int, input().split())
lst_lan = [int(sys.stdin.readline()) for i_1 in range(i_k)]

# 이진탐색
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     # 원하는 값 찾은 경우 인덱스 반환
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     elif array[mid] < target:
#         return binary_search(array, target, mid + 1, end)
# 결과 값 저장용 리스
ls_result = []

# 케이블을 자르고 개수 세는 함수
def cablecutter(list, objective):
    cnt_cable = 0
    for i_1 in list:
        cnt_cable += i_1 // objective
    return cnt_cable

# 이진탐색 함수
def search_bi(list, target, start, end):
    # 종료 조건 
    if start > end:
        return None
    mid = (start + end) // 2

    if cablecutter(list, mid) == target:
        ls_result.append(mid)
        search_bi(list, target, mid + 1, end)
    elif cablecutter(list, mid) < target:
        search_bi(list, target, start, mid - 1)
    elif cablecutter(list, mid) > target:
        ls_result.append(mid)
        search_bi(list, target, mid + 1, end)

search_bi(lst_lan, i_n, 1, 2**31 - 1)

print(max(ls_result))
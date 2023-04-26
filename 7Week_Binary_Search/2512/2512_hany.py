# 2512번 예산
'''
정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.

1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
2. 모든 요청이 배정될 수 없는 경우에는
특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다.
상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.

여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성
'''

# 첫번쨰 방법: 시간 초과
# import sys
# from heapq import heappush
# input = sys.stdin.readline

# n = int(input()) # 지방의 수
# # 각 지방의 예산 요청액
# req = list(map(int, input().split()))
# req_budget = []
# for i in req:
#     heappush(req_budget, i)
# # print(req_budget)

# total_budget = int(input()) # 총 예산액
# total = 0
# def bs(arr, start, end):
#     global total
#     avg = (start + end) // 2
#     while True:
#     # 2번째 규칙으로 합친 예산이 총 예산액과 같아지면 멈추게 작동시켜라.
#         if total == total_budget:
#             break
#         total = 0 # 초기화
#         for budget in arr:
#             # 요청 예산이 중간값보다 작거나 같은 경우
#             if budget <= avg:
#                 # 그대로 배정한다.
#                 total += budget
#             # 그렇지 않다면
#             else:
#                 # 상한액으로 더하라
#                 total += avg
#             # 중간점을 내려라
#             avg -= 1
#     return avg + 1


# # 모든 요청이 배정 될 수 있는 경우
# if sum(req_budget) <= total_budget:
#     # 요청한 금액 그대로 배정 -> 따라서 요청 예산 중 가장 큰 금액 출력
#     print(req_budget.pop())
# # 모든 요청이 배정될 수 없는 경우
# else:
#     # 가장 작은 예산과 가장 큰 예산에 변수 지정 후
#     start = req_budget[0]
#     end = req_budget[-1]
#     print(bs(req_budget, start, end))

####

# 2번째 방법
import sys
input= sys.stdin.readline

n= int(input())
req_budget = list(map(int, input().split()))
total_budget = int(input())
start = 0
end = max(req_budget)


while start <= end:
    mid = (start + end) // 2
    total = 0
    for budget in req_budget:
        # 예산이 상한액보다 크거나 같으면
        if budget >= mid:
            # 상한액을 더하고
            total += mid
        # 예산이 상한액보다 적으면
        else:
            # 요청 예산을 더한다.
            total += budget

    # 총금액이 예산총액보다 적거나 같으면
    if total <= total_budget:
        # start 위치를 올리고
        start = mid + 1
    # 총금액이 예산총액보다 크면
    else:
        # end의 위치를 내린다.
        end = mid - 1
print(end)
# 14501번 퇴사
'''
오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.
최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.
각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.
상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.
'''
# 1. 나만의 방식 + 구글링
# 시간에 맞게 범위를 설정, 범위를 넘어서면 return
# 최댓값 구하기(max 함수 이용)
# dp[i] i번째까지의 최대 수익

n = int(input())
T = []
P = []
dp = [0] * (n + 1)
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)


# n -1부터 0까지 (idx)
# i = idx - 1
for i in range(n - 1, -1, -1):
    # 시간을 넘어서면
    if i + T[i] > n:
        # 상담 x(i가 넘어 섰으니, i + 1도 의미 없는 수)
        dp[i] = dp[i + 1]
    else:
        # max 함수(둘 중 무엇이 낫냐?)
        # 상담을 안하는 것과, 상담을 하는 것 중
        dp[i] = max(dp[i + 1], dp[T[i] + i] + P[i])
print(dp[0])


# # 2. 보고 한 것
# n = int(input())
# dp = [0] * (n + 1)
# lst = []
# for _ in range(n):
#     t, p = map(int, input().split())
#     lst.append([t, p])

# # 인덱스 0이, 시간, 1이 금액
# for i in range(n):
#     # j: i번째 날에 상담했을 경우, 상담이 가능한 모든 날짜
#     for j in range(i + lst[i][0], n + 1):
#         # 해당 날짜의 최고 수익이 i번째까지 일한 최고 수익 + 
#         if dp[j] < dp[i] + lst[i][1]:
#             dp[j] = dp[i] + lst[i][1]
# print(dp[-1])


# 분류: 10주차 정렬
# 문제: 백준 1946 신입사원
# 문제 주소: https://www.acmicpc.net/problem/1946
# 푼 사람: 진홍엽
# 설명: 정렬 그리디 최적화
# 평점: 3/5

# import sys
# from collections import deque


# i_t = int(input())
# for test_case in range(i_t):
#     i_n = int(input())
#     ls_applicants = [tuple(map(int, sys.stdin.readline().split())) for applicant in range(i_n)]
#     ls_applicants.sort()
#     que_applicants = deque(ls_applicants)
#     ls_accepted = []
#     while que_applicants:
#         tup_applicant = que_applicants.popleft()
#         ls_accepted.append(tup_applicant)
#         for i in range(len(que_applicants)):
#             if que_applicants[0][1] > tup_applicant[1]:
#                 que_applicants.popleft()
#             else:
#                 que_applicants.rotate(-1)
#     print(len(ls_accepted))
# 시간초과


# 전체 정렬하고
# 두번째 항목이 이전 기록보다 낮을 경우, 카운트하지 않는 방식으로 연산 간편화
import sys


i_t = int(input())
for test_case in range(i_t):
    i_n = int(input())
    ls_applicants = [tuple(map(int, sys.stdin.readline().split())) for applicant in range(i_n)]
    ls_applicants.sort()
    cnt = 0
    score_2_min = 1e9
    for applicant in ls_applicants:
        if applicant[1] < score_2_min:
            cnt += 1
            score_2_min = applicant[1]
    print(cnt)
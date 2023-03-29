# 분류: 3주차 자유주제
# 문제: 백준 14889 스타트와링크
# 문제 주소: https://www.acmicpc.net/problem/14889
# 푼 사람: 진홍엽
# 설명: itertools.combinations 활용

from itertools import combinations

i_n = int(input())
ls_status = [list(map(int, input().split())) for i_1 in range(i_n)]

# 가능한 combination 수를 튜플로 반환함 
# (0, 1, 2, 3, 4), (0, 1, 2, 3, 5), ...

comb = combinations([i_2 for i_2 in range(i_n)], i_n // 2)

# 각 팀의 점수 계산 함수
def score_sum(array_status, array_comb):
    score_sum = 0
    for i_1 in array_comb:
        for i_2 in array_comb:
            if i_2 != i_1:
                score_sum += array_status[i_1][i_2]
    return score_sum

min_score_gap = 1e9
for tup_1 in comb:
    ls_other = [i_3 for i_3 in range(i_n) if i_3 not in tup_1]
    score_gap = abs(score_sum(ls_status, tup_1) - score_sum(ls_status, ls_other))
    if score_gap < min_score_gap:
        min_score_gap = score_gap

print(min_score_gap)
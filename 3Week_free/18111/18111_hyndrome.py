# 분류: 3주차 자유주제
# 문제: 백준 18111 마인크래프트
# 문제 주소: https://www.acmicpc.net/problem/18111
# 푼 사람: 진홍엽
# 설명: 딕셔너리 순환, 똑똑하게 브루트포스

import sys

# 땅의 높이로 반복문을 돌려야지 순회의 수가 줄어듦
# 최악의 땅의 2차원 배열로 반복문을 돌릴 경우 반복하는 횟수 차이
# 500 * 500 = 25000 vs 257 (땅의 높이 0~256)

# 땅의 분포를 저장하는 딕셔너리
# {땅의 높이: 해당 높이 땅의 개수} 형태로 저장
dct_ground = {}

# 입력 받기 및 딕셔너리에 저장
i_n, i_m, i_b = map(int, sys.stdin.readline().split())
for i_1 in range(i_n):
    ls_input = map(int, sys.stdin.readline().split())
    for i_2 in ls_input:
        dct_ground[i_2] = dct_ground.get(i_2, 0) + 1

# 최적의 땅의 높이는 땅 배열의 최하 또는 최고 높이 사이 -> 해당 높이로 반복문
# 반복문에서 걸리는 시간, 인벤토리의 블럭 수 계산
# 인벤토리의 블럭 수가 0 이상일 경우에만 결과값 리스트에 (해당 높이, 걸린 시간) 형태로 튜플로 저장
ls_result = []
for ground_target in range(min(dct_ground.keys()), max(dct_ground.keys()) + 1):
    result_b = i_b
    result_t = 0
    for ground_height, ground_cnt in dct_ground.items():
        if ground_height > ground_target:
            result_t += 2 * (ground_height - ground_target) * ground_cnt
            result_b += (ground_height - ground_target) * ground_cnt
        else:
            result_t += (ground_target - ground_height) * ground_cnt
            result_b -= (ground_target - ground_height) * ground_cnt            
    if result_b >= 0:
        ls_result.append((ground_target, result_t))

# 리스트에서 걸린 시간 최소, 해당 높이 최대의 값 추출
result = min(ls_result, key = lambda x: (x[1], -x[0]))
print(result[1], result[0])
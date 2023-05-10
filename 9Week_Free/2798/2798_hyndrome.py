# 분류: 9주차 자유주제
# 문제: 백준 2798 블랙잭
# 문제 주소: https://www.acmicpc.net/problem/2798
# 푼 사람: 진홍엽
# 설명: 브루트포스
# 평점: 3/5 [기본]

# 수업 시간에 풀었잖소!
i_n, i_m = map(int, input().split())
ls_input = list(map(int, input().split()))

i_sum = 0

for i_1 in range(len(ls_input) - 2):
    for i_2 in range(i_1 + 1, len(ls_input) - 1):
        for i_3 in range(i_2 + 1, len(ls_input)):
            temp_sum = ls_input[i_1] + ls_input[i_2] + ls_input[i_3]
            if i_sum < temp_sum <= i_m:
                i_sum = temp_sum
print(i_sum)
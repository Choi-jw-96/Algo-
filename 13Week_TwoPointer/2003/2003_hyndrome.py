# 분류: 13주차 두포인터
# 문제: 백준 2003 수들의합2
# 문제 주소: https://www.acmicpc.net/problem/2003
# 푼 사람: 진홍엽
# 설명: 두포인터 슬라이딩윈도우
# 평점: 2/5 [기본]

i_n, i_m = map(int, input().split())
ls_num = list(map(int, input().split()))
start = 0
end = 0
sum_current = ls_num[0]
cnt = 0
while True:
    if sum_current < i_m:
        end += 1
        if end >= i_n:
            break
        sum_current += ls_num[end]
    elif sum_current == i_m:
        cnt += 1
        end += 1
        if end >= i_n:
            break
        sum_current += ls_num[end]
        sum_current -= ls_num[start]
        start += 1
    else:
        sum_current -= ls_num[start]
        start += 1
        if end < start:
            end += 1
            if end >= i_n:
                break
            sum_current += ls_num[end]
print(cnt)
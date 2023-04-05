# 분류: 4주차 그리디
# 문제: 백준 2828 사과담기
# 문제 주소: https://www.acmicpc.net/problem/2828
# 푼 사람: 진홍엽
# 설명: 그리디 구현

# 바구니 왼쪽 끝을 기준으로 계산하였음 
i_n, i_m = map(int, input().split())
i_j = int(input())
p_basket = 1
cnt_move = 0
for i_2 in range(i_j):
    p_apple = int(input())
    if p_apple < p_basket:
        cnt_move += (p_basket - p_apple)
        p_basket = p_apple
    elif p_apple > p_basket + (i_m - 1):
        cnt_move += p_apple - (p_basket + (i_m - 1))
        p_basket = p_apple - (i_m - 1)
print(cnt_move)
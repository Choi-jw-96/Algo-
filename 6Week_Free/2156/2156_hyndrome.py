# 분류: 6주차 자유주제
# 문제: 백준 2156 포도주시식
# 문제 주소: https://www.acmicpc.net/problem/2156
# 푼 사람: 진홍엽
# 설명: DP

# 2579 계단 오르기와 비교했을 때, 조건이 미묘하게 다르다
# 계단오르기 <-> 포도주 시식
# 1. 계단은 반드시 한계단씩 또는 두계단씩 오를 수 있다 <-> 연속해서 세잔을 마실 수 없다. (반드시 마실 필요 x)
# 1-예제 6 1 1 0 0 1 1
# 2. 마지막 계단은 반드시 밟아야 한다 <-> 마지막 잔 안마셔도 됨

import sys
i_n = int(sys.stdin.readline())
ls_wine = [int(sys.stdin.readline()) for i in range(i_n)]

# 포도주가 2잔이하일 경우 무조건 다 마시는게 최대
if i_n == 1:
    print(ls_wine[-1])
elif i_n == 2:
    print(ls_wine[0] + ls_wine[1])
# 3잔 이상일 경우 3잔까지의 초기값을 구한다
# 3가지 경우로 나뉜다
# (마지막 잔 기준) 연속하는 세 잔 중 첫 잔을 안마실 경우
# (마지막 잔 기준) 연속하는 세 잔 중 두 번째 잔을 안마실 경우
# 안마실 경우
else:
    ls_max_wine = [0] * (i_n)
    ls_max_wine[0] = ls_wine[0]
    ls_max_wine[1] = ls_wine[0] + ls_wine[1]
    ls_max_wine[2] = max(ls_wine[0] + ls_wine[1], ls_wine[1] + ls_wine[2], ls_wine[0] + ls_wine[2])
    for i in range(2, i_n-1):
        ls_max_wine[i+1] = max(ls_max_wine[i-2] + ls_wine[i] + ls_wine[i+1], ls_max_wine[i-1] + ls_wine[i+1], ls_max_wine[i])
    print(ls_max_wine[-1])
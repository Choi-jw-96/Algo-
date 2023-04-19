# 분류: 6주차 자유주제
# 문제: 백준 12865 평범한배낭
# 문제 주소: https://www.acmicpc.net/problem/12865
# 푼 사람: 진홍엽
# 설명: 배낭

# 배낭 그 자체
import sys

i_n, i_k = map(int, sys.stdin.readline().split())
ls_items = [(0, 0)] + [tuple(map(int, sys.stdin.readline().split())) for _ in range(i_n)]


ls_bag = [[0] * (i_k + 1) for _ in range(i_n + 1)]

for y in range(1, i_n + 1):
    for x in range(1, i_k + 1):
        if ls_items[y][0] <= x:
            ls_bag[y][x] = max(ls_bag[y-1][x], ls_bag[y-1][x-ls_items[y][0]] + ls_items[y][1])
        else:
            ls_bag[y][x] = ls_bag[y-1][x]

print(ls_bag[i_n][i_k])
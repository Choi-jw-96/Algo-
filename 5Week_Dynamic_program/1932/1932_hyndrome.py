# 분류: 5주차 DP
# 문제: 백준 1932 정수삼각형
# 문제 주소: https://www.acmicpc.net/problem/1932
# 푼 사람: 진홍엽
# 설명: DP

import sys

i_n = int(sys.stdin.readline())
ls_tri = []
for i_1 in range(i_n):
    ls_tri.append(list(map(int, sys.stdin.readline().split())))

ls_topdown = [[-1] * i_1 for i_1 in range(1, i_n + 1)]

def tri(x, y):
    if x == 0 and y == 0:
        return ls_tri[y][x]
    if ls_topdown[y][x] != -1:
        return ls_topdown[y][x]
    if x == 0:
        ls_topdown[y][x] = tri(x, y - 1) + ls_tri[y][x]
    elif x == y:
        ls_topdown[y][x] = tri(x - 1, y - 1) + ls_tri[y][x]
    else:
        ls_topdown[y][x] = max(tri(x - 1, y - 1), tri(x, y - 1)) + ls_tri[y][x]
    return ls_topdown[y][x]

print(max([tri(i_2, i_n - 1) for i_2 in range(i_n)]))
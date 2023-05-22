# 분류: 11주차 플로이드-마셜
# 문제: 백준 1058 친구
# 문제 주소: https://www.acmicpc.net/problem/1058
# 푼 사람: 진홍엽
# 설명: 브루트포스 플로이드-마셜 구현 그래프 
# 평점: 3/5

import sys


i_n = int(sys.stdin.readline())
graph = [sys.stdin.readline().rstrip() for _ in range(i_n)]

i_popular = 0
for y in range(i_n):
    set_y = set()
    for x in range(i_n):
        if graph[y][x] == 'Y':
            set_y.add(x)
            for k in range(i_n):
                if (graph[x][k] == 'Y') and (y != k):
                    set_y.add(k)
    i_cnt = len(set_y)
    if i_cnt > i_popular:
        i_popular = i_cnt
        
print(i_popular)
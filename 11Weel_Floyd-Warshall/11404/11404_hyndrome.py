# 분류: 11주차 플로이드-마셜
# 문제: 백준 11404 플로이드
# 문제 주소: https://www.acmicpc.net/problem/11404
# 푼 사람: 진홍엽
# 설명: 플로이드-마셜 
# 평점: 3/5 [기본]
import sys


i_n = int(input())
i_m = int(input())
INF = int(1e9)
graph = [[INF] * (i_n + 1) for _ in range(i_n + 1)]


for y in range(1, i_n + 1):
    for x in range(1, i_n + 1):
        if x == y:
            graph[y][x] = 0

for i in range(i_m):
    start, end, distance = map(int, sys.stdin.readline().split())
    # 같은 노선 중 최소의 거리만 입력 받는다
    if distance < graph[start][end]:
        graph[start][end] = distance

for k in range(1, i_n + 1):
    for y in range(1, i_n + 1):
        for x in range(1, i_n + 1):
            graph[y][x] = min(graph[y][x], graph[y][k] + graph[k][x])

for y in range(1, i_n + 1):
    for x in range(1, i_n + 1):
        # 연결 경로가 없을 때 문제에서 0 출력 조건
        if graph[y][x] == INF:
            print(0, end=' ')
        else:
            print(graph[y][x], end=' ')
    print()
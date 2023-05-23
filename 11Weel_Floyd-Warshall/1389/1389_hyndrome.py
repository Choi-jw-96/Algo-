# 분류: 11주차 플로이드-마셜
# 문제: 백준 1389 케빈베이컨의6단계법칙
# 문제 주소: https://www.acmicpc.net/problem/1389
# 푼 사람: 진홍엽
# 설명: 플로이드-마셜 다익스트라
# 평점: 3/5
# 플루이드 워셜 
import sys


INF = int(1e9)
i_n, i_m = map(int, sys.stdin.readline().split())
graph = [[INF] * (i_n + 1) for _ in range(i_n + 1)]

# 자기 자신에게 가는 비용 0으로 초기화
for y in range(1, i_n + 1):
    for x in range(1, i_n + 1):
        if x == y:
            graph[y][x] = 0
# 연결 관계 입력 (해당 문제에서는 노드 간의 거리가 1이며 양방향)
for i in range(i_m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start][end] = 1
    graph[end][start] = 1
# 점화식으로 플로이드 워셜 알고리즘
for k in range(1, i_n + 1):
    for y in range(1, i_n + 1):
        for x in range(1, i_n + 1):
            graph[y][x]  = min(graph[y][x], graph[y][k] + graph[k][x])

# 베이컨 수 가장 작은 사람 찾기
i_bacon = INF
i_index = 0
for i in range(1, i_n + 1):
    i_sum = sum(graph[i][1:])
    if i_sum < i_bacon:
        i_bacon = i_sum
        i_index = i

print(i_index)
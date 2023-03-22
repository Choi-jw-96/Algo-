# 분류: 2주차 BFS / DFS
# 문제: 백준 11403 경로찾기 
# 문제 주소: https://www.acmicpc.net/problem/11403
# 푼 사람: 진홍엽
# 설명: bfs 첫 방문 처리 까다로움
import sys
from collections import deque

i_n = int(sys.stdin.readline().rstrip())
graph = []
for i_1 in range(i_n):
    ls_node = []
    ls_input = list(map(int, sys.stdin.readline().split()))
    for i_2 in range(i_n):
        if ls_input[i_2] == 1:
            ls_node.append(i_2)
    graph.append(ls_node)

for i_3 in range(i_n):
    ls_visited = [0] * i_n
    que = deque()
    for i_3 in graph[i_3]:
        que.append(i_3)
    while que:
        v = que.popleft()
        if ls_visited[v] == 0:
            ls_visited[v] = 1
            for i_4 in graph[v]:
                que.append(i_4)
    print(*ls_visited)
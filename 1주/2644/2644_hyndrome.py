# 분류: 1주차 BFS / DFS
# 문제: 백준 2644 촌수계산
# 문제 주소: https://www.acmicpc.net/problem/2644
# 푼 사람: 진홍엽
# 설명: BFS 최단거리
import sys
from collections import deque

i_n = int(sys.stdin.readline())
i_start, i_end = map(int, sys.stdin.readline().split())
i_m = int(sys.stdin.readline())

graph = [[] for i_1 in range(i_n + 1)]
for i_2 in range(i_m):
    i_m_1, i_m_2 = map(int, sys.stdin.readline().split())
    graph[i_m_1].append(i_m_2)
    graph[i_m_2].append(i_m_1)

visited = [-1] * (i_n + 1)
visited[i_start] = 0
que = deque()
que.append(i_start)
while que:
    v = que.popleft()
    for i_3 in graph[v]:
        if visited[i_3] == -1:
            que.append(i_3)
            visited[i_3] = visited[v] + 1
    if visited[i_end] != -1:
        break       

print(visited[i_end])
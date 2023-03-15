# 분류: 1주차 BFS / DFS
# 문제: 백준 11060 점프 점프
# 문제 주소: https://www.acmicpc.net/problem/11060
# 푼 사람: 진홍엽
# 설명: BFS 최단거리
from collections import deque

i_n = int(input())
# 연결 관계가 정의 되어 있는 그래프 형성 (단방향)
graph = []
graph.append([])
ls_input =list(map(int, input().split()))
for i_1 in range(len(ls_input)):
    if ls_input[i_1] == 0:
        graph.append([])
    else:
        graph.append(list(range(i_1 + 2, i_1 + 2 + ls_input[i_1])))

# 방문 확인을 위한 빈 리스트 형성
visited = [-1] * (i_n + 1)

# BFS를 사용하여 최단거리 찾기
# visited[i_2] = visited[v] + 1 이용하여 깊이 확인
def jump(start, end):
    que = deque([start])
    visited[start] = 0
    while que:
        v = que.popleft()
        if v <= end:
            for i_2 in graph[v]:
                if i_2 <= end:
                    if visited[i_2] == -1:
                        que.append(i_2)
                        visited[i_2] = visited[v] + 1
        if visited[end] != -1:
            break
    return visited[end]

print(jump(1, i_n))
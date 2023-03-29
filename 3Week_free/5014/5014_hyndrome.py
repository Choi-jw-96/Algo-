# 분류: 3주차 자유주제
# 문제: 백준 5014 스타트링크
# 문제 주소: https://www.acmicpc.net/problem/5014
# 푼 사람: 진홍엽
# 설명: BFS

from collections import deque

i_f, i_s, i_g, i_u, i_d = map(int, input().split())

ls_visited =  [-1] * (i_f + 1)
ls_visited[i_s] = 0
que = deque()
que.append(i_s)
while que:
    v_floor = que.popleft()
    if (v_floor + i_u <= i_f):
        if ls_visited[v_floor + i_u] == -1:
            ls_visited[v_floor + i_u] = ls_visited[v_floor] + 1
            que.append(v_floor + i_u)
    if v_floor - i_d >= 1:
        if ls_visited[v_floor - i_d] == -1:
            ls_visited[v_floor - i_d] = ls_visited[v_floor] + 1
            que.append(v_floor - i_d)
    if ls_visited[i_g] != -1:
        print(ls_visited[i_g])
        break
if ls_visited[i_g] == -1:
    print('use the stairs')

# 처음에 방문 리스트를 [False]로 두고 방문 확인 조건을 if ls_visited[i_g] == False로 두니까
# 처음에 방문했었던 0도 미방문으로 처리해서 오답이 났음
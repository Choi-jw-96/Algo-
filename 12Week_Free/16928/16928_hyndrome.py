# 분류: 12주차 자유주제
# 문제: 백준 16928 뱀과사디라게임
# 문제 주소: https://www.acmicpc.net/problem 16928
# 푼 사람: 진홍엽
# 설명: bfs 최단경로
# 평점: 3.5/5
# 최단거리 탐색 bfs가 최초로 찾은 도착지점의 깊이
import sys
from collections import deque


i_n, i_m = map(int, sys.stdin.readline().split())
# 뱀과 사다리를 딕셔너리 형태로 받음
dict_snakeNladder = {}
for i in range(i_n + i_m):
    start, end = map(int, sys.stdin.readline().split())
    dict_snakeNladder[start] = end

# 방문 처리 겸 주사위 횟수를 기록할 리스트
ls_visited = [0] * 101
ls_dice = [1, 2, 3, 4, 5, 6]
# bfs 돌리기
que = deque([1])
while que:
    current_location = que.popleft()
    # 도착지점 (100)에 도착할 경우 주사위 굴린 횟수 출력
    if current_location == 100:
        print(ls_visited[current_location])
        break
    # 주사위 나온 수만큼 전진
    for dice in ls_dice:
        next_location = current_location + dice
        # 방문 여부 및 유효성 확인
        if (next_location <= 100) and (ls_visited[next_location] == 0):
            # 뱀과 사다리 처리 (해당 key값이 있을 경우 value로 값 바꿔줌)
            if next_location in dict_snakeNladder:
                next_location = dict_snakeNladder[next_location]
            # 뱀과 사다리로 이동한 곳의 방문 여부확인
            if ls_visited[next_location] == 0:
                # 주사위 수 증가
                ls_visited[next_location] = ls_visited[current_location] + 1
                que.append(next_location)
# 분류: 9주차 자유주제
# 문제: 백준 1931 회의실배정
# 문제 주소: https://www.acmicpc.net/problem/1931
# 푼 사람: 진홍엽
# 설명: 그리디알고리즘 큐 수학
# 평점: 4/5
import sys
from collections import deque


i_n = int(input())
# 갑 입력 받음 [(시작 시간, 종료 시간), ...] 형태로 입력 받음
ls_meeting = [tuple(map(int, sys.stdin.readline().split())) for _ in range(i_n)]
# 종료 시간이 빠른 순으로 정렬
ls_meeting.sort(key=lambda x : (x[1], x[0]))
# popleft 사용하려고 queue 사용
que_meeting = deque(ls_meeting)

# 회의실을 사용 횟수를 저장하는 변수
cnt = 0
# 회의실의 종료 시간을 저장하는 변수
end_time_room = 0
# queue를 순회
while que_meeting:
    # queue의 첫 번째 회의 (지금 남아있는 회의 예정 중 가장 빠르게 종료되는 회의) 
    start_time, end_time = que_meeting.popleft()
    # 추가로 진행할 수 있는 회의라면 (추출한 회의의 시작시간이 현재 회의실 종료시간 보다 같거나 크다면)
    if start_time >= end_time_room:
        # 회의실 사용 횟수 +1
        cnt += 1
        # 회의실의 종료 시간 갱신
        end_time_room = end_time
# 회의실 사용 횟수 출력
print(cnt)
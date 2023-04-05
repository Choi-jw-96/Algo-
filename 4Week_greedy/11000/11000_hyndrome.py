# 분류: 4주차 그리디
# 문제: 백준 11000 강의실배정
# 문제 주소: https://www.acmicpc.net/problem/11000
# 푼 사람: 진홍엽
# 설명: 그리디 heap


import sys
import heapq

i_n = int(sys.stdin.readline())

ls_timetable = []
for i_1 in range(i_n):
    lecture_start, lecture_end = map(int, sys.stdin.readline().split())
    ls_timetable.append((lecture_start, lecture_end))

ls_timetable.sort()
# 강의실 만들기
room = []
# 첫 강의 강의실에서 진행
# 강의실에는 강의 끝난 시간이 남음
heapq.heappush(room, ls_timetable[0][1])
# 두 번째 강의부터 진행
for i_2 in range(1, i_n):
    # 다음부터 진행하는 강의시간과 강의실들 중 가장 빨리 끝나는 강의실과 비교
    # 강의시간 < 강의실 끝나는 최소 시간 (빈 강의실이 없을 때)
    if ls_timetable[i_2][0] < room[0]:
        # 강의실 추가 (강의 끝나는 시간으로)
        heapq.heappush(room, ls_timetable[i_2][1])
    # 강의시간 >= 강의실 끝나는 최소 시간 (강의실에서 강의를 이어할 수 있을 때)
    else:
        # 해당 강의실 시간 강의 끝나는 시간으로 교체
        # heapq로는 제일 첫 번째 값(가장 빨리 끝나는 강의실)을 pop하고 끝나는 시간 값을 push 하는 방식으로 구현
        # heappushpop을 쓸 경우 따로따로 하는 것 보다 미세하게 빠름 
        # heapq.heappop(room)
        # heapq.heappush(room, ls_timetable[i_2][1])
        heapq.heappushpop(room, ls_timetable[i_2][1])
# 강의실 개수 출력 
print(len(room))



# 시간 초과 풀이1
# 시간을 0 으로 이루어진 리스트로 만들어서 수업 시간마다 1씩 더함
# 리스트 중 최대의 숫자 출력
# 컴퓨터가 멈추는 것을 경험할 수 있다
i_n = int(sys.stdin.readline())
ls_timetable = [0] * 1000000000
for i_2 in range(i_n):
    lecture_start, lecture_end = map(int, sys.stdin.readline().split())
    for i_3 in range(lecture_start, lecture_end):
        ls_timetable[i_3] += 1
print(max(ls_timetable))


# 시간 초과 풀이2
# heap 대신에 min으로 같은 알고리즘을 구현할 경우 시간복잡도가 커서 시간 초과 (1%를 넘지 못함)
import sys

def bi_search(array):
    min = 1e9
# heap 대신에 min 사용시 시간초과
i_n = int(sys.stdin.readline())
ls_timetable = []
for i_1 in range(i_n):
    lecture_start, lecture_end = map(int, sys.stdin.readline().split())
    ls_timetable.append((lecture_start, lecture_end))

ls_timetable.sort()
# 강의실 만들기
room = []
# 첫 강의 강의실에서 진행
# 강의실에는 강의 끝난 시간이 남음
room.append(ls_timetable[0][1])
# 두 번째 강의부터 진행
for i_2 in range(1, i_n):
    # 다음부터 진행하는 강의시간과 강의실들 중 가장 빨리 끝나는 강의실과 비교
    # 강의시간 < 강의실 끝나는 최소 시간 (빈 강의실이 없을 때)
    if ls_timetable[i_2][0] < min(room):
        # 강의실 추가 (강의 끝나는 시간으로)
        room.append(ls_timetable[i_2][0])
    # 강의시간 >= 강의실 끝나는 최소 시간 (강의실에서 강의를 이어할 수 있을 때)
    else:
        # 해당 강의실 시간 강의 끝나는 시간으로 교체
        room[room.index(min(room))] = ls_timetable[i_2][1]
# 강의실 개수 출력 
print(len(room))
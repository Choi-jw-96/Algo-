# 11000번 강의실 배정
'''
김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데,
최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다.
(즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
'''

# t와 s가 같으면 강의실 하나로 셈 친다.

import sys
import heapq
input = sys.stdin.readline

n = int(input())
classtime = [] # 튜플로 저장
classroom = [] # 강의실 배열
for _ in range(n):
    s, t = map(int, input().split())
    classtime.append((s, t))

# 시작 시간이 빠른 순으로 정렬한다.
# 만약 시작 시간이 같으면, 종료가 빠른 순으로 정렬
classtime.sort(key=lambda x: (x[0], x[1]))
# print(classtime)
for i in classtime:
    (s, t) = i
    # 강의실이 비어 있지 않고, 현 강의의 시작 시간이 강의실의 최소값보다 작거나 같으면,
    # 강의실의 최소값을 빼고나서, 현 강의의 종료 시간을 푸쉬한다.
    # 힙이 비어있으면 인덱스 에러가 나므로, 강의실이 비어있으면 안됨
    if classroom and classroom[0] <= s:
        heapq.heappop(classroom) # classroom의 최소값 빼기
    heapq.heappush(classroom, t) # 강의실의 현재 강의의 종료 시간 넣기

# print(classroom)
print(len(classroom))
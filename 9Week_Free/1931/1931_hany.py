# 1931번 회의실 배정
'''
N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고,
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 
'''
# 접근방법
'''
- 시작 시간이 빠른 순으로 정렬한다(heapq?)
- 반대로 끝나는 시간이 빠른 순으로 정렬하면?
'''
import sys
input = sys.stdin.readline
n = int(input()) # 회의실 수
class_ = []

for _ in range(n):
    start, end = map(int, input().split())
    class_.append((start, end))
class_.sort(key = lambda x: (x[1], x[0]))
# print(class_)
cnt = 1
e = class_[0][1]
for i in range(1, n):
    # i의 시작시간이 이전 끝나는 시간과 같거나 이후라면,
    if class_[i][0] >= e:
        # 회의 추가해주고, 기존 끝나는 시간을 현 강의의 끝나는 시간으로 바꿔주기
        cnt += 1
        e = class_[i][1]
print(cnt)
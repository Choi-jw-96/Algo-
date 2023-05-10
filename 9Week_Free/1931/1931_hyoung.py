# 1931 회의실 배정

N = int(input())
time = []

for _ in range(N):
  start, end = map(int, input().split())
  time.append([start, end])

time = sorted(time, key=lambda a: a[0]) 
time = sorted(time, key=lambda a: a[1]) 

last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 

for i, j in time:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j

print(conut)
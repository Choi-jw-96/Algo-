import sys
input = sys.stdin.readline

N = int(input())
room = []
# 회의가 금방 끝나면서 가장 빠르게 시작하는 순으로 정렬해준다
time = sorted([tuple(map(int, input().split())) for i in range(N)], key=lambda x:(x[1], x[0]))
cnt = 0
end = -1
# 시작시간이 전에 끝나는 시간보다 크다면 회의를 배정해준다
for i in time:
    if i[0] >= end:
        cnt += 1
        end = i[1]
print(cnt)
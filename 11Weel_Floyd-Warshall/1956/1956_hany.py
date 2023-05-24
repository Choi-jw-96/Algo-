# 1956번 운동
'''
운동을 한 후에는 다시 시작점으로 돌아오는 것이 좋기 때문에, 우리는 사이클을 찾기를 원한다. 
사이클을 이루는 도로의 길이의 합이 최소가 되도록 찾으려고 한다.
도로의 길이의 합이 가장 작은 사이클을 찾는 프로그램을 작성하시오.
두 마을을 왕복하는 경우도 사이클에 포함됨에 주의한다.
'''
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
INF = 1e9
cycle = [[INF] * (v + 1) for _ in range(v + 1)]
for a in range(v):
    for b in range(v):
        if a == b:
            cycle[a][b] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    cycle[a][b] = c
# print(cycle)

for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            cycle[a][b] = min(cycle[a][b], cycle[a][k] + cycle[k][b])
# print(cycle)
lst = []
for a in range(1, v + 1):
    for b in range(1, v  + 1):
        sum_ = cycle[a][b] + cycle[b][a]
        if sum_ < INF and a != b:
            lst.append(sum_)
# print(lst)
if not lst:
    print(-1)
else:
    print(min(lst))

# 14938번 서강그라운드
'''
각 지역은 일정한 길이 l (1 ≤ l ≤ 15)의 길로 다른 지역과 연결되어 있고 이 길은 양방향 통행이 가능하다.
은이는 낙하한 지역을 중심으로 거리가 수색 범위 m (1 ≤ m ≤ 15) 이내의 모든 지역의 아이템을 습득 가능하다고 할 때, 예은이가 얻을 수 있는 아이템의 최대 개수를 알려주자.
'''
## 접근방법
'''
해당 노드로 도달하는 거리가 수색범위 안인지 검사해야함.
각 노드별로 범위내에 있는 노드를 점찍는다.
해당 노드의 아이템 개수를 인덱스로 확인하고 더한다.
합 리스트 중 max값을 구한다.
'''
import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
# 수색범위(m)을 넘어서면 제외한다.
items = list(map(int, input().split()))
INF = 1e9
ground = [[INF] * n for _ in range(n)]

for a in range(n):
    for b in range(n):
        if a == b:
            ground[a][b] = 0

for _ in range(r):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    ground[a][b] = c
    ground[b][a] = c

for k in range(n):
    for a in range(n):
        for b in range(n):
            ground[a][b] = min(ground[a][b], ground[a][k] + ground[k][b])
# print(ground)
lst = []
for a in range(n):
    res = 0
    for b in range(n):
        if ground[a][b] <= m:
            res += items[b]
    lst.append(res)
# print(lst)
print(max(lst))

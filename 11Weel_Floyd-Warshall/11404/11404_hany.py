# 11404번 플로이드
'''
n(2 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 각 버스는 한 번 사용할 때 필요한 비용이 있다.

모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = 1e9
cities = [[INF] * n for _ in range(n)]
for a in range(n):
    for b in range(n):
        if a == b:
            cities[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a, b, c = a - 1, b - 1, c
    cities[a][b] = min(cities[a][b], c)
# print(cities)
for k in range(n):
    for a in range(n):
        for b in range(n):
            cities[a][b] = min(cities[a][b], cities[a][k] + cities[k][b])

for a in range(n):
    for b in range(n):
        if cities[a][b] == INF:
            cities[a][b] = 0

for i in cities:
    print(*i)
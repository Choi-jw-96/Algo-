import sys
input = sys.stdin.readline
INF = int(10e9)

city, area, road = map(int, input().split())
item = [0]+list(map(int, input().split()))
ground = [[INF] * (city + 1) for _ in range(city + 1)]

for i in range(road):
    area_1, area_2, dist = map(int, input().split())
    ground[area_1][area_2] = min(ground[area_1][area_2], dist)
    ground[area_2][area_1] = min(ground[area_2][area_1], dist)

for i in range(1, city+1):
    for j in range(1, city+1):
        for k in range(1, city+1):
            if j == k:
                ground[j][k] = 0
            ground[j][k] = min(ground[j][k], ground[j][i] + ground[i][k])

max_item = 0

for i in range(1, city + 1):
    cnt = 0
    for j in range(1, city + 1):
        if ground[i][j] <= area:
           cnt +=  item[j]
    max_item = max(max_item, cnt)
print(max_item)
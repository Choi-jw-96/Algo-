import sys
input = sys.stdin.readline
INF = int(10e9)

village, road = map(int, input().split())
ground = [[INF] * (village + 1) for _ in range(village + 1)]

for i in range(road):
    village_1, village_2, dist = map(int, input().split())
    ground[village_1][village_2] =  dist

for i in range(1, village + 1):
    for j in range(1, village + 1):
        for k in range(1, village + 1):
          if ground[j][k] > ground[j][i] + ground[i][k]:
            ground[j][k] = ground[j][i] + ground[i][k]

min_dist = INF

for i in range(1, village + 1):
  min_dist = min(ground[i][i], min_dist)

print(-1)if min_dist == INF else print(min_dist)
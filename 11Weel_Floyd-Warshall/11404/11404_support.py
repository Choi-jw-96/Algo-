import sys
input = sys.stdin.readline
INF = int(10e9)

city =  int(input())
bus = int(input())
cheap = [[INF] * (city + 1) for _ in range(city + 1)]

# 직접 가는 경로 입력
for _ in range(bus):
    start, end, cost = map(int, input().split())
    cheap[start][end] = min(cost, cheap[start][end])

# 플로이드-위셜에서 경로는 제일 위
for i in range(1, city+1):
    for j in range(1, city+1):
        for k in range(1, city+1):
            if j == k:
                cheap[j][k] = 0
            else:
                # 직접간(지금 있는데)거나 걸처오거나
                cheap[j][k] = min(cheap[j][k], cheap[j][i]+cheap[i][k])

for i in cheap[1:]:
  for j in i[1:]:
      if j == INF:
          print(0, end=' ')
      else:
          print(j, end=' ')
  print()
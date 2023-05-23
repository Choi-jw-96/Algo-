import sys
input = sys.stdin.readline

n = int(input())
people = [list(input().strip())  for _ in range(n)]

friend = [[0] * n for _ in range(n)]
# 한다리 더 걸쳐야한다
for i in range(n):
    for j in range(n):
        for k in range(n):
          if k == j:
              continue
          # 나랑 친구거나 / 한다리 걸쳐 아는 사이거나
          if people[j][k] == 'Y' or (people[j][i] == 'Y' and people[i][k] == 'Y'):
              friend[j][k] = 1

popular = 0
for i in friend:
    popular = max(sum(i), popular)
print(popular)
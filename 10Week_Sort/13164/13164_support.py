import sys
input = sys.stdin.readline

n, team = map(int, input().split())
kids = list(map(int, input().split()))

teams = []
for i in range(1, n):
    teams.append(kids[i]-kids[i-1])
teams.sort()

cost = 0

for i in range(n-team):
    cost += teams[i]
print(cost)
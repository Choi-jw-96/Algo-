# 1058번 친구
'''
가장 유명한 사람을 구하는 방법은 각 사람의 2-친구를 구하면 된다.
어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, A와 친구이고, B와 친구인 C가 존재해야 된다.
여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다.
가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.

A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.

a -> b 친구 or a-> c-> b여야 하니까
graph[a][b] == 1 or == 2 여야함.
'''
import sys
input = sys.stdin.readline

n = int(input())
friends = []
for _ in range(n):
    friends.append(list(input().rstrip()))
# print(friends)
visited = [[0] * n for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if friends[a][b] == 'Y' or (friends[a][k] == 'Y' and friends[k][b] == 'Y'):
                visited[a][b] = 1

res = 0
for a in range(n):
    cnt = 0
    for b in range(n):
        if visited[a][b] == 1:
            cnt += 1
    res = max(res, cnt)
print(res)
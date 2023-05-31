# 11724번 연결 요소의 개수
'''
방향 없는 그래프가 주어졌을 때, 연결 요소의 개수를 구하는 프로그램 작성하시오.
'''
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n, m = map(int, input().split())

# 연결 리스트를 만들어라.
lst = [[] for _ in range(n + 1) ]
for _ in range(m):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)
# print(lst)

# 방문한적이 있는지 여부를 확인하기 위해
visited = [False] * (n + 1)
cnt = 0

def dfs(i):
    visited[i] = True
    for a in lst[i]:
        if not visited[a]:
            dfs(a)

for a in range(1, n + 1):
    if not visited[a]:
        dfs(a)
        cnt += 1
print(cnt)
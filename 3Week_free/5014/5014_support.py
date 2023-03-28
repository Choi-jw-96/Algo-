import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

def BFS(visited, S, G):
    global U, D
    queue = deque([S])
    visited[S] = 0

    while queue:
        now = queue.popleft()

        if now == G:
            return visited[now]
        
        for i in [U, -D]:
            next = now + i
            if 0 <= next < F and visited[next] == -1:
                visited[next] = visited[now] + 1
                queue.append(next)

F, S, G, U, D = map(int, input().split())

visited = [-1] * F
if S == G:
    print(0)
elif (U==0 and G > S) or (D==0 and S > G):
    print('use the stairs')
else:
    BFS(visited, S-1, G-1)
    if visited[G-1] == -1:
        print('use the stairs')
    else:
        print(visited[G-1])

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit = 10**6

def dist(A, visited):
    q = deque([(0, A[0])])
    while q:
        i, jump = q.popleft()
        for j in range(1, jump + 1):
            if i + j >= N or visited[i + j] != 0:
                continue 
            else:
                visited[i + j] = visited[i] + 1
                q.append(((i + j), A[i + j]))                

N = int(input())
A = list(map(int, input().split()))
visited = [0] * N
          
dist(A, visited)

if N == 1:
    print(0)
else:
    if visited[-1] == 0:
        print(-1)
    else:
        print(visited[-1])

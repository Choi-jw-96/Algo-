import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(start):
    global cnt
    visited[start] = True
    cnt += 1

    for _ in range(2):
        if (0 <= start + stone[start] < n and not visited[start + stone[start]]):
            DFS(start + stone[start])
        elif 0 <= start - stone[start] < n and not visited[start - stone[start]]:
            DFS(start - stone[start])


n = int(input())
stone = list(map(int, input().split()))
start = int(input())

visited = [False] * n
cnt = 0
DFS(start-1)

print(cnt)

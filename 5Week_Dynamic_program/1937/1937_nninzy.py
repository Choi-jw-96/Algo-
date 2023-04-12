# 구글링...했습니다... https://chelseashin.tistory.com/73 참고 (다시 풀 예정)

from sys import stdin
input = stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c):
    if check[r][c]:
        return check[r][c]

    check[r][c] = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        
        if A[r][c] < A[nr][nc]:
            check[r][c] = max(check[r][c], dfs(nr, nc)+1)
    return check[r][c]

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * N for _ in range(N)] 

for r in range(N):
    for c in range(N):
        if not check[r][c]:
            dfs(r, c)
MAX = 0
for i in range(N):
    MAX = max(MAX, max(check[i]))
print(MAX)
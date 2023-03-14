import sys
sys.setrecursionlimit(100000)


m, n = list(map(int, sys.stdin.readline().split()))
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

def dfs(x,y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y-1)
        dfs(x-1,y)
        dfs(x-1,y+1)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1,y-1)
        dfs(x+1,y)
        dfs(x+1,y+1)
        return True
    return False
cnt = 0
for i in range(m):
    for j in range(n):
        if dfs(i,j) == True:
            cnt += 1
print(cnt)
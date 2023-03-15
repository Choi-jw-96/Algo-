import sys
sys.setrecursionlimit(10000)

t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = list(map(int, sys.stdin.readline().split()))
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = list(map(int, sys.stdin.readline().split()))
        graph[y][x] = 1
    
    def dfs(a,b):
        if a < 0 or a > n-1 or b < 0 or b > m-1:
            return False
        if graph[a][b] == 1:
            graph[a][b] = 0
            dfs(a-1,b)
            dfs(a+1,b)
            dfs(a,b-1)
            dfs(a,b+1)
            return True
        return False
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                cnt += 1
    print(cnt)
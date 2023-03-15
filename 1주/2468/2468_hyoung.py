import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m_hight = max(map(max, graph))

cnt_ls = [] # 잠기는 높이에 따른 안전영역의 갯수

for m in range(m_hight):   
    # 높이가 m 이하이면 잠긴다. 잠긴거 0으로 표시.
    visited = [[1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= m:
                visited[i][j] = 0

    def dfs(x,y):
        if x <= -1 or x >= n or y <= -1 or y >= n:
            return False
        if visited[x][y] == 1:
            visited[x][y] = 0
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            return True
        return False
    cnt = 0
    for i in range(n):
        for j in range(n):
            if dfs(i,j) == True:
                cnt += 1
    cnt_ls.append(cnt)
print(max(cnt_ls))
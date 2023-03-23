# 2677 dfs
import sys
sys.setrecursionlimit(10**7)

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

# 이미 1로 표시되어 있어서 단지 2부터 시작.
cnt = 1
ls = []
house = 0

def dfs(x,y):
    if x > -1  and x < n and y > -1 and y < n and graph[x][y] == 1:
        global house
        house += 1
        graph[x][y] = cnt
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
    
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1
            ls.append(house)
            house = 0
            dfs(i,j)
ls.append(house) #마지막에는 house가 추가가 안되기 떄문
ls.sort() 

print(cnt - 1)
for elem in range(1,len(ls)):
    print(ls[elem])
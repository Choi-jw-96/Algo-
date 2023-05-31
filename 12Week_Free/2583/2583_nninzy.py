from collections import deque

m, n, k = map(int, input().split())
graph = list([0]*n for _ in range(m))

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

q = deque()
area = []
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for a in range(m):
    for b in range(n):
        if not graph[a][b]:
            graph[a][b] = 1
            q.append([a,b])
            area.append(1)
            while(q):
                x,y = q.popleft()
                for c,d in move:
                    dx = x+c
                    dy = y+d
                    if m>dx>=0 and n>dy>=0 and not graph[dx][dy]:
                        q.append((dx,dy))
                        graph[dx][dy] = 1
                        area[-1] += 1
print(len(area))
print(*sorted(area))

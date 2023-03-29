n = int(input())

visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
ls = []

def dfs(a, b):
    global min_
    if a == n//2:
        sum1, sum2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    sum1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    sum2 += graph[i][j]
        ls.append(abs(sum1-sum2))
        return

    for i in range(b, n):
        if not visited[i]:
            visited[i] = True
            dfs(a+1, i+1)
            visited[i] = False

dfs(0, 0)
print(min(ls))
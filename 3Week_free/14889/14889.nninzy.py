def dfs(dth, idx):
    global minAns
    # 백트래킹 답 체크 시점
    if dth == N // 2:
        sSum = 0
        lSum = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    sSum += graph[i][j]
                elif not visited[i] and not visited[j]:
                    lSum += graph[i][j]
        minAns = min(minAns, abs(sSum - lSum))
        return
    for k in range(idx, N):
        if not visited[k]:
            visited[k] = True
            dfs(dth+1, k+1)
            visited[k] = False


N = int(input())
visited = [False for _ in range(N)]
graph = []
for _ in range(N):
    graph.append([*map(int, input().split())])
minAns = int(1e9)

dfs(0,0)
print(minAns)
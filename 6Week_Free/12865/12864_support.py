n, k = map(int, input().split())

tool = [[0,0]] + [list(map(int, input().split())) for _ in range(n)]

bag = [[0] * (k + 1) for _ in range(n+1)]

# 전체 물품 수
for i in range(1, n+1):
    # 가방에 담을 수 있는 최대 무게
    for j in range(1, k+1):
        # 물품 당 무게가 최대 무게보다 안나간다면(가방에 들어갈 무게라면) 넣었을때랑 넣지 않을때 비교
        if j - tool[i][0] >= 0:
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-tool[i][0]] + tool[i][1])
        # 아니면 제외한 무게
        else:
            bag[i][j] = bag[i-1][j]
print(bag[n][k])

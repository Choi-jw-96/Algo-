
V, E = map(int, input().split())
matrix = [[int(1e9)] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    matrix[a][b] = c

#경유지 k, 출발지 i, 도착지 j 
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            # i->j 가 빠른지 i->k->j가 빠른지
            if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

answer = 1e9
for i in range(1, V+1):
    answer = min(answer, matrix[i][i])
if answer == 1e9:
    print(-1)
else:
    print(answer)
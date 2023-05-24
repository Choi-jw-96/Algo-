n = int(input())
friends = [list(input()) for _ in range(n)]

ls = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if friends[i][j] == "Y" or (friends[i][k] == "Y" and friends[k][j] == "Y"):
                ls[i][j] = 1

answer = 0
for row in ls:
    answer = max(answer, sum(row))
print(answer)
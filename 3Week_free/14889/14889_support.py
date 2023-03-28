# combination
from itertools import permutations, combinations
import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

# p = permutations(range(0, N), N//2)
p = list(combinations(range(N), N//2))
# print(list(p))
A = []
B = []

for i in range(len(p)//2):
    A.append(p[i])
    B.append(p[-i-1])

min_score = float('inf')
for i in range(len(A)):
    a_score, b_score = 0, 0
    for j in range(len(A[i])-1):
        for k in range(j, len(p[i])):
            a_score += graph[A[i][j]][A[i][k]] + graph[A[i][k]][A[i][j]]
            b_score += graph[B[i][j]][B[i][k]] + graph[B[i][k]][B[i][j]]
    if min_score > abs(a_score - b_score):
        min_score = abs(a_score - b_score)
print(min_score)




# DFS
def DFS(x, y):
    global min_score
    if x == N // 2:
        a_score, b_score = 0, 0
        for i in range(N):
            for j in range(N):
                if visitied[i] and visitied[j]:
                    a_score += graph[i][j]
                elif not visitied[i] and not visitied[j]:
                    b_score += graph[i][j]
        if min_score > abs(a_score - b_score):
            print(a_score, b_score)
            min_score = abs(a_score - b_score)

    for i in range(y, N):
        if not visitied[i]:
            visitied[i] = True
            DFS(x+1, i+1)
            visitied[i] = False

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visitied = [False for _ in range(N)]
min_score = float('inf')
DFS(0, 0)

print(min_score)
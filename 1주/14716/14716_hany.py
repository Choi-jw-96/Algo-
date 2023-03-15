# 14716번 현수막
'''
현수막에서 글자인 부분은 1, 글자가 아닌 부분은 0으로 바꾸는 필터를 적용하여 값을 만드는데 성공

그런데 혁진이는 이 값을 바탕으로 글자인 부분 `1`이 상, 하, 좌, 우, 대각선으로 인접하여 서로 연결되어 있다면 한 개의 글자라고 생각만 하였다.

혁진이가 필터를 적용하여 만든 값이 입력으로 주어졌을 때, 혁진이의 생각대로 프로그램을 구현하면 글자의 개수가 몇 개인지 출력하여라.
'''
import sys
from pprint import pprint
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x + 1, y + 1)
        dfs(x + 1, y - 1)
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x - 1, y + 1)
        dfs(x - 1, y - 1)
        return True
    return False


M, N = map(int, input().split()) # m: x, n: y

graph = []
for _ in range(M):
    nums = list(map(int, input().split()))
    graph.append(nums)
# pprint(graph)

result = 0
for x in range(M):
    for y in range(N):
        if dfs(x, y) == True:
            result += 1
print(result)



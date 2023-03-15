# 2468번 안전 영역
'''
그 다음에 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사하려고 한다.
이때, 문제를 간단하게 하기 위하여, 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.
어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수이다.

어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오. 
'''
import sys
sys.setrecursionlimit(10**6)
from pprint import pprint
import copy

input = sys.stdin.readline

N = int(input())
land = []

for _ in range(N):
    land.append(list(map(int, input().rstrip().split())))
# pprint(land)

## 모든 경우의 수를 구하며, 최대한 파편화 된 곳을 구하라. 즉 dfs의 개수가 많은 곳
# 수위보다 높은 곳을 찾아 연결하라.

def dfs(x, y, graph, dep):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    
    if graph[x][y] > dep and graph[x][y] < 101:
        graph[x][y] = 101
        dfs(x + 1, y, graph, dep)
        dfs(x - 1, y, graph, dep)
        dfs(x, y + 1, graph, dep)
        dfs(x, y - 1, graph, dep)
        return True
    return False

result_lst = []
for dep in range(101):
    graph = copy.deepcopy(land)
    result = 0

    for x in range(N):
        for y in range(N):
            if dfs(x, y, graph, dep) == True:
                result += 1

    result_lst.append(result)
    if result == 0:
        break
    

fin = max(result_lst)
print(fin)
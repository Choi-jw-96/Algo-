# 2644 촌수 계산
import sys
sys.setrecursionlimit = 10000


# 촌수를 알려면 뿌리로 거슬러 올라가 더해야한다.
## 그렇다면 형제간엔?
## 부모를 뿌리로 두고 1+1이다.
## 이를 어떻게 구현 할 것인가?
### 동일하게 만나는 곳! 그곳 까지 수를 센 다음 합하라!
### 동일하게 만나는 곳이 없다면? -1

# dfs 함수 정의
def dfs(graph, visited, start, lst):
    visited[start] = True
    lst.append(start)

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i, lst)

# 입력
n = int(input()) # 전체 사람 수
t_s, t_e = map(int, input().split()) # 타겟
m = int(input()) # 간선 수
graph = [[] for _ in range(n + 1)]
visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)
lst1 = []
lst2 = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# print(graph)


# 출력
dfs(graph, visited1, t_s, lst1)
# print(lst1)
dfs(graph, visited2, t_e, lst2)
# print(lst2)

result = 0
result_lst = []
if len(lst1) == len(lst2): ## 만나면
    for x in range(len(lst1)):
        for y in range(len(lst2)):
            if lst1[x] == lst2[y]:
                result = x + y
                break
        result_lst.append(result)
    result_lst.sort()
    print(result_lst[0])
else: ## 만나지 않으면 -1
    print(-1)
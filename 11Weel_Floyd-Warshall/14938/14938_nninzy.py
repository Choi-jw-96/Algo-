INF = int(1e9)
# 많은 아이템 습득을 위해 어디 떨어져야 하는가

# 지역 n, 수색범위 m, 길의 개수 r
n, m, r = map(int, input().split())
# 각 지역에서 얻을 수 있는 아이템들 t
t_list = list(map(int, input().split()))
# 지역 간의 거리를 나타내는 2차원 리스트, 무한대로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
answer = 0

# 자기 자신으로 가는 거리 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    # 입력 받은 거리 l과 graph 내 저장된 거리 비교 후 작을 경우 대체 (양방향 그래프, 서로다른  방향 거리 업데이트)
    graph[a][b] = min(graph[a][b], l)
    graph[b][a] = min(graph[b][a], l)

# 플로이드 워셜 알고리즘 (모든 경로의 최소거리 구하기)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 중간 지점 거쳐 가는 경우와 비교
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 시작지점에서 도달지점까지 거리가 수색 범위 이내이면 아이템 회수, 아이템 개수 누적 (이전 시작 지점들과 비교)
# 모든 지점을 시작지점으로
for i in range(1, n + 1):
    # 현 시작 시점 기준 회수 가능한 아이템 개수
    temp = 0
    # 수색 범위 이내일 경우
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            temp += t_list[j - 1]
    # 회수 개수 가장 많은 경우 선정
    answer = max(answer, temp)

print(answer)
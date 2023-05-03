# 분류: 8주차 이분탐색
# 문제: 백준 3253 TRAM
# 문제 주소: https://www.acmicpc.net/problem/3253
# 푼 사람: 진홍엽
# 설명: 데이크스트라
# 평점: 4/5
# 문제
# 자그레브의 트램 네트워크는 여러 교차지점과 해당 교차지점을 연결하는 레일로 구성되어 있습니다. 모든 교차지점에는 교차지점에서 나가는 레일 중 하나를 가리키는 스위치가 있습니다. 
# 트램이 교차로에 진입하면 스위치가 가리키는 방향으로만 출발할 수 있습니다. 기관사가 다른 길로 가고 싶다면 수동으로 스위치를 변경해야 합니다.
# 기관사가 교차지점 A에서 교차지점 B로 운전할 때, 기관사가 스위치를 수동으로 변경해야 하는 횟수를 최소화하는 경로를 선택하려고 합니다.
# 교차지점 A에서 교차지점 B로 이동하는 데 필요한 최소한의 스위치 변경 횟수를 계산하는 프로그램을 작성하십시오.

# 입력
# 입력 파일의 첫 번째 줄에는 하나의 공백 문자로 구분된 정수 N, A 및 B가 포함됩니다. 
# (2 ≤ N ≤ 100, 1 ≤ A, B ≤ N)
# N은 교차지점의 수이며 교차지점에는 1에서 N까지 번호가 지정됩니다. 

# 다음 N 행 각각에는 하나의 공백 문자로 구분된 일련의 정수가 포함됩니다. 
# i번째 줄의 첫 번째 숫자는 i번째 교차지점에서 나가는 레일의 수를 나타냅니다. 
# i번째 줄의 두 번째 숫자는 i번째 교차지점에서 스위치가 가르키고 있는 연결된 교차지점을 나타냅니다. 
# i번째 줄의 나머지 숫자들은 해당 교차지점에서 스위치가 가르키고 있지 않은 연결된 다른 교차지점을 나타냅니다. (스위치를 수동으로 변경하여 변경가능)

# 출력
# A지점부터 B지점으로 도착할 수 있는 최소 스위치 변경 횟수를 출력해야합니다. A지점부터 B지점에 도달할 수 없으면 '-1'를 출력합니다.
import sys
import heapq

# 교차지점의 수 N, 출발지점 A, 도착지점 B 입력 받기
i_n, i_a, i_b = map(int, sys.stdin.readline().split())

# 다익스트라 알고리즘을 위한 셋팅
# 교차지점의 번호가 1번부터 시작하기 때문에 그래프의 크기를 N+1 로 설정
INF = int(1e9)
graph = [[] for _ in range(i_n + 1)]
distance = [INF] * (i_n + 1)

# 입력받기
# 교차지점만큼 반복하여 입력
# 교차지점에서 나가는 레일 수가 0일 경우 -> graph 입력 받을 필요 없음
# 교차지점에서 나가는 레일 수가 0보다 클 경우
# 첫 번째 나가는 레일에 가중치 0
# 첫 번째 이후로 나가는 레일에 가중치 1 (첫 번째가 아닌 레일은 경로 변경을 위해서 스위치를 변경해야함)
for i in range(i_n):
    ls_input = list(map(int, sys.stdin.readline().split()))
    if ls_input[0] == 0:
        pass
    else:
        graph[i+1].append((ls_input[1], 0))
        if ls_input[0] >= 2:
            for path in ls_input[2:]:
                graph[i+1].append((path, 1))

# 다이크스트라 알고리즘 적용
def dijkstra(start):
    # heap 사용
    que = []
    # 시작점 설정
    heapq.heappush(que, (0, start))
    distance[start] = 0
    while que:
        # 거리가 최소인 지점 방문
        dist, now = heapq.heappop(que)
        # 현재 heap 안에서의 최소 거리 지점의 방문 여부 확인
        # while문 안의 continue는 반복 작업을 멈추고 while문의 처음으로 돌아가 다시 반복 진행
        if distance[now] < dist:
            continue
        # 방문하지 않았을 경우 다른 인접한 노드 확인
        for path in graph[now]:
            cost = dist + path[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 경우가 더 짧을 경우 거리 갱신
            if cost < distance[path[0]]:
                distance[path[0]] = cost
                # 인접노드 heap에 추가
                heapq.heappush(que, (cost, path[0]))

dijkstra(i_a)

# 도착불가능/가능 여부에 따라서 값 출력
if distance[i_b] == INF:
    print(-1)
else:
    print(distance[i_b])
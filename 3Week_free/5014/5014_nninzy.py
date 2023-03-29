from collections import deque

def bfs(s):
    queue = deque()
    # queue에 초기데이터 삽입 / 1 넣었으니 return시 -1로 return
    queue.append(s)
    visited[s] = 1
    # 움직일 수 있는 방향값
    up_down = [U, -D]
    while queue:
        current = queue.popleft()
        # 현위치가 G에 도달한 경우
        if current == G:
            return visited[current] - 1
        for i in up_down:
            next = current + i
            # 다음 위치가 F 범위 내에 있고, 방문하지 않았을 경우
            if 0 < next <= F and not visited[next]:
                queue.append(next)
                visited[next] = visited[current] + 1
    # 목적지를 찾을 수 없는 경우
    return "use the stairs"

# input 값 받기
F, S, G, U, D = map(int, input().split())
# 층 방문 여부 확인
visited = [0 for i in range(F+1)]

print(bfs(S))
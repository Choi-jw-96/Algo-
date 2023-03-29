from collections import deque

F, S, G, U, D = map(int, input().split())

def bfs():
    queue = deque()
    queue.append(S)
    visited = [0] * (F + 1)
    visited[S] = 1
    while queue:
        q = queue.popleft()
        if q == G:
            print(visited[G] - 1)
            return
        up = q + U
        down = q - D

        if up <= F and not visited[up]:
            queue.append(up)
            visited[up] = visited[q] + 1
        if down > 0 and not visited[down]:
            queue.append(down)
            visited[down] = visited[q] + 1
    else:
        print('use the stairs')
        return
bfs()
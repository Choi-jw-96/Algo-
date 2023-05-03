# 4485 녹색 옷 입은 애가 젤다지?

import sys
import heapq
input = sys.stdin.readline
N = int(input())

dx=[-1,0,1,0]
dy=[0,-1,0,1]
cnt = 0

while N!=0:
    cnt+=1
    board = [list(map(int,input().split())) for _ in range(N)]
    ch_board = [[-1]*N for _ in range(N)]

    hq = []
    heapq.heappush(hq,(board[0][0],0,0))
    ch_board[0][0] = 0
    
    while hq:
        val,x,y = heapq.heappop(hq)
        if x == N-1 and y == N-1:
            print(f'Problem {cnt}: {val}')
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx < N and 0<=ny<N and ch_board[nx][ny] == -1:
                ch_board[nx][ny] = 0
                heapq.heappush(hq,(val+board[nx][ny],nx,ny))

    N = int(input())
# 18111번 마인크래프트
'''
세로 N , 가로 M, 집터 맨 왼쪽 위의 좌표 (0,0)
1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.

1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다

‘땅 고르기’ 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력

작업을 시작할 때 인벤토리에는 B개의 블록이 들어 있다. 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.

답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력하시오.
'''


# 블록제거 - 인벤 넣기 (2초) / 목표 높이보다 높을 때
# house[i][j] -= 1, b += 1, time += 2
# 블록 꺼내기 - 위에 놓기 (1초) / 목표 높이보다 낮을 때
# b -= 1, house[i][j] += 1, time += 1

import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9
fin_height = 0

for height in range(257):
    up_h, down_h = 0, 0 # 초기값 셋팅
    
    # 한 사이클
    for i in range(n):
        for j in range(m):
            # 목표 층수에 따라 다르다.
            # 목표 층수보다 크다면?
            if house[i][j] >= height:
                # 블록을 제거하고 블록을 저장한다. 2초 시간이 든다.
                # 현 높이에서 목표 높이만큼 뺀다
                # up_h는 저장할 블록 개수 이자, 시간을 계산할 단서
                up_h += house[i][j] - height 
            # 목표 층수보다 작으면?
            elif house[i][j] < height:
                # 블록을 더한다. 인벤토리에서 블록을 뺀다. 1초 시간이 든다.
                # 목표높이에서 현 높이를 뺀다.
                # down_h는 인벤토리에서 뺴야할 블록 개수이자, 시간을 계산할 단서
                down_h += height - house[i][j]
    # 새로운 인벤토리는 기존의 인벤토리에 up_h 블록 개수를 더한 것
    new_b = b + up_h
    # 만약 새로운 인벤토리가 빼야할 블록보다 적다면 다시 사이클 돌려!
    if new_b >= down_h:
        time = 2 * up_h + down_h
        if time <= ans:
            ans = time
            fin_height = height
    # 아니라면 시간 계산하고 나머지도 계산
print(ans, fin_height)

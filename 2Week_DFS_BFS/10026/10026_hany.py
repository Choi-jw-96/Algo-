# 10026번 적록색약
'''
기가 N*N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 
구역은 같은 색으로 이루어져 있다. 
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다.
(색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)
- 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. r = g
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 0. 입력 및 초기값 설정
normal = []
jaejoon = []

n = int(input())
for _ in range(n):
    colors = input().rstrip()
    colors1 = list(colors)
    normal.append(colors1)
    colors = colors.replace('R', 'G')
    colors2 = list(colors)
    jaejoon.append(colors2)
# print(jaejoon)   
# print(normal)

def dfs(x, y, who, color):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if who[x][y] == color:
        who[x][y] = 0
        dfs(x, y + 1, who, color)
        dfs(x, y - 1, who, color)
        dfs(x + 1, y, who, color)
        dfs(x - 1, y, who, color)
        return True
    return False

result1 = 0
result2 = 0
result3 = 0
for x in range(n):
    for y in range(n):
        if dfs(x, y, normal, 'R') == True:
            result1 += 1
        elif dfs(x, y, normal, 'B') == True:
            result2 += 1
        elif dfs(x, y, normal, 'G') == True:
            result3 += 1
print(result1 + result2 + result3, end = " ")

result4 = 0
result5 = 0
result6 = 0
for x in range(n):
    for y in range(n):
        if dfs(x, y, jaejoon, 'R') == True:
            result4 += 1
        elif dfs(x, y, jaejoon, 'B') == True:
            result5 += 1
        elif dfs(x, y, jaejoon, 'G') == True:
            result6 += 1
print(result4 + result5 + result6)
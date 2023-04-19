# 9663번 N-Queen
'''
N-Queen 문제는 크기가 N * N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
'''
# 종료 조건
'''
1. 모든 줄에 퀸을 놓을 수 없는 경우(각 줄 당 하나) / 놓을 수 없는 줄이 있을 때 바로 종료
2. 마지막 줄까지 완료하면 종료
'''
# 탐색 방향
'''
8방향 모두 할 필요 없이 아래 대각선 왼쪽, 아래 정방향, 아래 대각선 오른쪽
'''
import sys
input = sys.stdin.readline
n = int(input())
row = [0] * n # 퀸의 위치
cnt = 0

def check(x): # 검증
    for i in range(x):
        # 같은 위치이거나, 대각선 방향이 같다면
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            # false
            return 0
    # ture
    return 1
    
def queen(x):
    global cnt
    
    # 걸리는 거 하나 없이 마지막 줄까지 다 돌았으니, 경우의 수를 +1하고 종료
    if x == n :
        cnt += 1
        return

    # x행에 퀸 놓기    
    for i in range(n): # 0~n-1까지 탐색
        row[x] = i
        if check(x): # 검증을 통과하면 queen(x + 1) 호출
            queen(x + 1)
queen(0)
print(cnt)
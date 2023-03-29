# 14889번 스타트와 링크
'''
축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다.
이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 
팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합
Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다.
'''

# sij 와 sji는 무조건 짝꿍이다
# ij를 택한 순간, 그 이후로 i, j를 조회할 수 없다.
# 전부 탐색하고 모든 경우의 수를 탐색해야 함 (완전 탐색)

# 0. 입력 및 초기값 설정
import sys
input = sys.stdin.readline
N = int(input())
teams = [list(map(int, input().split())) for _ in range(N)]

# 한 팀당 N/2명이어야 한다.
# 조합문제 -> 백트래킹 알고리즘
# 조합을 하고 최소값을 구해야 한다.

# 1. 차이를 구하는 함수

visited = [False] * N
def diff():
    start = 0
    link = 0
    
    for i in range(N - 1): # 0부터 N - 2까지(N-1은 j에 해당)
        for j in range(i + 1, N): # i의 다음 수부터  N - 1까지
            # True인 경우 start 팀
            if visited[i] and visited[j]:
                start = start + teams[i][j] + teams[j][i]
            # False인 경우 link팀
            elif not visited[i] and not visited[j]:
                link = link + teams[i][j] + teams[j][i]
    return abs(start - link)

# 2. 백트래킹
min_ans = 40000 # 최소값을 max로 잡기
def dfs(level, idx, N):
    global min_ans

    # 탈출 조건: 팀내 모집 인원이 꽉 찼을 때
    if level == N // 2:
        diff_ans = diff()
        min_ans = min(diff_ans, min_ans)
        
        # 예외처리(최적화를 위함)
        if min_ans == 0: # min_ans가 0이 되는 그 순간, 아묻따 탈출
            print(min_ans)
            exit()
        return # 탈출
    
    for i in range(idx, N):
        # 한 팀만 구하면 나머지 팀을 저절로 구성됨
        if not visited[i]:
            visited[i] = True
            dfs(level + 1, i + 1, N) # 백트랙킹의 핵심, 재귀하고나서, return하게 되면 그 이후의 것부터 시작
            visited[i] = False
    return
        
dfs(0, 0, N)
print(min_ans)
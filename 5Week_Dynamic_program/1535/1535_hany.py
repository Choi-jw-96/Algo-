# 1535번 안녕
'''
세준이를 생각해준 사람은 총 N명이 있다. 사람의 번호는 1번부터 N번까지 있다. 
세준이가 i번 사람에게 인사를 하면 L[i]만큼의 체력을 잃고, J[i]만큼의 기쁨을 얻는다.
세준이는 각각의 사람에게 최대 1번만 말할 수 있다.


세준이의 목표는 주어진 체력내에서 최대한의 기쁨을 느끼는 것이다.
세준이의 체력은 100이고, 기쁨은 0이다.
만약 세준이의 체력이 0이나 음수가 되면, 죽어서 아무런 기쁨을 못 느낀 것이 된다.

세준이가 얻을 수 있는 최대 기쁨을 출력하는 프로그램을 작성
'''
n = int(input()) # 사람수
# idx 조정을 위하여, 0을 추가
L = [0] + list(map(int, input().split())) # 닳을 체력
J = [0] + list(map(int, input().split())) # 오를 기쁨

# 101개(0~100)의 체력바를 지닌 n + 1명의 사람(dp[0]의 사람은 허수)
dp = [[0 for _ in range(101)] for _ in range(n + 1)]
# print(dp)

# 조건
# 1. health <= 0: game-over (범위)
# 2. 인사하는 게 좋은가? 좋지 않은가? (max 함수)

# 1부터 n까지
for i in range(1, n + 1): # 사람 idx
    # 1부터 100까지
    for j in range(1, 101): # 체력
        if L[i] <= j: # 조건1
            # 조건 2
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - L[i]] + J[i])
        else:
            dp[i][j] = dp[i - 1][j]
            
# dp[n][100]은 세준이가 죽는다.
print(dp[n][99])
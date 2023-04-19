# 퇴사 날 = n + 1일. n일 동안 상담 시작
# 퇴사까지 남은 일수 넘어가면 안되기 때문에 마지막 일수부터 거꾸로 찾으면서 dp 진행.

n = int(input())

t_list = [] # 상담하는데 걸리는 기간
p_list = [] # 상담했을 때 받을 수 있는 금액
dp = [0] * (n+1) # n일까지 벌 수 있는 최대 수익 저장

for i in range(n):
    t, p = map(int, input().split()) # 각가의 상담 완료하는데 걸리는 기간 / 상담 시 받을 수 있는 금액
    t_list.append(t)
    p_list.append(p)

for i in range(n - 1, -1, -1): # 뒤에서부터 거꾸로
    # dp[0]에는 최대로 상담 진행해 얻을 수 있는 이익 저장
    if t_list[i] + i > n: # 상담에 필요한 일수가 퇴사일을 넘어가면
        dp[i] = dp[i + 1] # 해당 날짜에 일 X. 다음 날의 dp값 그대로 가져옴
    else:
        dp[i] = max(p_list[i] + dp[i+t_list[i]], dp[i+1])
        # n을 넘어가면 
        # 오늘 상담을 안할 경우 지난 상담까지의 보수값 dp[i+1]
        # 상담 할 경우 오늘 날짜 + 오늘 시작할 상담에 필요한 일수를 dp에 넣고 상담 보수를 더함
        # 이중 max 값을 선택
print(dp[0])
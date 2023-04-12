# DFS
def dfs(t, money):
    global pay
    # 맨 끝으로 간다면 리턴 & money가 pay보다 크다면 저장
    if t == N:
        if pay < money:
            pay = money
        return
    # t가 N과 동일해 질 때까지 더해준다
    dfs(t + 1, money)
    # 리턴 후 N을 넘지 않는 범위 안에서 더해준다.
    if t + li[t][0] <= N:
        dfs(t + li[t][0], money + li[t][1])

N = int(input())
li = []

for _ in range(N):
    T, P = map(int, input().split())
    li.append((T, P))
pay = 0
dfs(0, 0)
print(pay)


# 일반 for 문
N = int(input())
li = []
for _ in range(N):
    T, P = map(int, input().split())
    li.append((T, P))

# for 문을 도는 도중 범위를 넘기지 않기위해서 N+1를 해준다
money = [0 for _ in range(N+1)]

# 끝에서 부터 시작해서 앞으로 나아간다.
for i in range(N-1, -1, -1):
    # 움직이는 범위가 N안이라면
    if i + li[i][0] <= N:
        # 돌아가서 money 얻는 money와 돌아가지 않고 현재 money 중 어떤게 이득인지 정해서 money[i]에 저장한다
        money[i] = max(money[i+1], li[i][1] + money[i+li[i][0]])
    else:
        money[i] = money[i+1]
print(money[0])
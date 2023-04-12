T = int(input())
li = []

for _ in range(T):
    li.append(list(map(int, input().split())))

# 1행부터(0행의 수는 하나니까) 아래로 내려간다
for i in range(1, T):
    # i행의 갯수만큼 for문을 돈다
    for j in range(len(li[i])):
        # j가 T-1 안에 있다면 a는 한 행 위를 저장한다. 아니라면 0을준다.(어차리 아래 max()로 인해 비교되고 탈락할 수)
        if 0 <= j < len(li[i]) - 1:
            a = li[i-1][j]
        else:
            a = 0
        # j-1이 0보다 같거나 크다면 b에 한 행 위+한 열 앞의 수를 저장하고, 아니면 0을 준다.
        if 0<= j-1 < len(li[i]) - 1:
            b = li[i-1][j-1]
        else:
            b = 0

        # 두 a, b중 큰 수를 해당 부분과 더하여 대체해준다.
        li[i][j] = li[i][j] + max(a, b)
# 마지막 행에서 가장 큰 수를 구해준다.
print(max(li[T-1]))
def pleasuer(l, j, i):
    global L, J, joy
    # 마지막인덱스에 도착했을때 들어간다
    if i == n:
        # joy보다 커졌을때 저장한다
        if joy < j:
            joy = j
        # 마지막 인덱스라면 리턴한다
        return
    # 마지막 인덱스에 갈떄까지 재귀
    pleasuer (l, j, i+1)
    # 리턴 시 돌아온다 & 뒤에서부터 L[i]를 뺴도 0보다 크다면 들어간다/ 아님 풀린다.
    if l - L[i] > 0:
        pleasuer(l - L[i], j + J[i], i+1)
    
n = int(input())

L = list(map(int, input().split()))
J = list(map(int, input().split()))

l, j = 100, 0

joy =0
pleasuer(l, j, 0)

print(joy)




    
n = int(input())

L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))

# 사람만큼의 이중리스트를 만들고 행복만큼 갯수를 넣는다
pleasure = [[0] * 101 for _ in range(n+1)]

# 사람만큼 돈다
for i in range(1, n+1):
    #  행복만큼 돈다
    for j in range(1, 101):
        # 체력이 남아있다면 전 리스트의 최대행복과 전 리스르틔 전 최대행복 + 지금 얻는 행복 중 큰 수를 고른다
        if j - L[i] > 0:
          pleasure[i][j] = max(pleasure[i-1][j], pleasure[i-1][j-L[i]]+J[i])
        # 안남는다면 전 수를 끌고
        else:
           pleasure[i][j] = pleasure[i-1][j]

print(pleasure[n][99])


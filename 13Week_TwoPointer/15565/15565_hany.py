# 15565번 귀여운 라이언
'''
라이언 인형은 1, 어피치 인형은 2로 표현하자. 라이언 인형이 K개 이상 있는 가장 작은 연속된 인형들의 집합의 크기
'''

n, k = map(int, input().split())
doll = list(map(int, input().split()))
start = 0
end = 0
cnt = 0
res = int(1e9)

if doll[end] == 1:
    cnt += 1

'''
1의 개수가 3이 포함되는 순간 개수를 새고 저장한다.
'''
while end < n:
    # 라이언이 k개면 저장
    if cnt == k:
        res = min(res, end - start + 1)
        if doll[start] == 1:
            cnt -= 1
        start += 1
    else:
        end += 1
        if end < n and doll[end] == 1:
            cnt += 1

if res == int(1e9):
    print(-1)
else:
    print(res)

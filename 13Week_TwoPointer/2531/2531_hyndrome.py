# 분류: 13주차 두포인터
# 문제: 백준 2531 회전초밥
# 문제 주소: https://www.acmicpc.net/problem/2531
# 푼 사람: 진홍엽
# 설명: 두포인터 구현
# 평점: 3/5 [기본]
# 전체 순회: 시간 초과 PyPy3으로는 풀 수는 있음 2740ms
import sys
i_n, i_d, i_k, i_c = map(int, sys.stdin.readline().split())
ls_sushi = [int(sys.stdin.readline()) for _ in range(i_n)]
cnt_max = 0
for start in range(len(ls_sushi)):
    set_sushi = set([ls_sushi[i] for i in range(start, start - i_k, -1)])
    cnt_current = len(set_sushi)
    if i_c not in set_sushi:
        cnt_current += 1
    if cnt_current > cnt_max:
        cnt_max = cnt_current
print(cnt_max)

# oat641의 풀이 PyPy3으로는 168ms 초밥의 가짓수가 그리 많지 않다는 점(3000개)을 이용
N, d, k, c = map(int, input().split())

sushi = [int(input()) for _ in range(N)]

count = 1
picked = [0 for _ in range(d+1)]
picked[c] = 1

for i in range(k):
    if picked[sushi[i]] == 0:
        count += 1
    picked[sushi[i]] += 1

answer = count
for i in range(N-1):
    picked[sushi[i]] -= 1
    if picked[sushi[i]] == 0:
        count -= 1
    
    if picked[sushi[(i+k)%N]] == 0:
        count += 1
    picked[sushi[(i+k)%N]] += 1
    
    answer = max(answer, count)

print(answer)
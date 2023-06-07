# 2003번 수들의 합2
'''
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
sum_ = lst[0]
start = 0
end = 1
cnt = 0

while True:
    if sum_ < m:
        if end < n:
            sum_ += lst[end]
            end += 1
        else:
            break
    elif sum_ == m:
        cnt += 1
        sum_ -= lst[start]
        start += 1
    else:
        sum_ -= lst[start]
        start += 1
print(cnt)

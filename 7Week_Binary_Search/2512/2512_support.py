import sys
input = sys.stdin.readline

n = int(input())
tax = list(map(int, input().split()))
limit = int(input())

start, end = 0, max(tax)

while start <= end:
    total_tax = 0
    mid = (start + end) // 2
    # 상한선을 mid로 하고 mid보다 큰수를 제한해준다
    for i in tax:
        total_tax += min(mid, i)
    # total_tax가 예산보다 클거나 같다면 경우는 start를 줄여서 mid 값을 늘여준다
    if limit >= total_tax:
        start = mid + 1
    # 예산보다 작을경우 end를 줄여서 mid값을 줄여준다.
    else:
        end = mid -1
print(end)
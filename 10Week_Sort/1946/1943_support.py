import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    rank = [tuple(map(int, input().split())) for _ in range(n)]
    rank.sort()

    min_rank = rank[0][1]
    cnt = 1
    for i in range(1, n):
      if rank[i][1] < min_rank:
         min_rank= rank[i][1]
         cnt += 1
    print(cnt)
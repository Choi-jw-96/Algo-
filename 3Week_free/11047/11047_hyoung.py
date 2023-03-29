# 11047 동전 0

import sys

ls = []
n, k = map(int, input().split())
for _ in range(n):
    a = int(sys.stdin.readline().strip())
    ls.append(a)
ls.reverse()

result = 0
for i in ls:
    if k // i >= 1:
        result += (k // i)
        k = (k % i)
print(result)
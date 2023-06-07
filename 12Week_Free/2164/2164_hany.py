# 2164번 카드2
'''
우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.
'''

from collections import deque

n = int(input())
d = deque([])
for i in range(1, n + 1):
    d.append(i)

while True:
    if len(d) == 1:
        break
    d.popleft()
    d.append(d.popleft())

print(*d)
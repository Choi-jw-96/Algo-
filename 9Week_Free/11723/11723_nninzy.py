import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    order = input().split()
    if len(order) == 1:
        s = set([i for i in range(1,21)]) if order[0] == 'all' else set()
    else:
        text = order[0]
        num = int(order[1])
        if text == 'add':
            s.add(num)
        elif text == 'remove':
            s.discard(num)
        elif text == 'check':
            print(1 if num in s else 0)
        elif text == 'toggle':
            if num in s:
                s.discard(num)
            else:
                s.add(num)
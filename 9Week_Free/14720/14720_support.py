import sys
input = sys.stdin.readline
S = set()

for t in range(int(input())):
    i = input().split()
    if i[0] == 'all':
        S = set([j for j in range(1, 21)])
    elif i[0] == 'empty':
        S = set()
    elif i[0] == 'add':
        S.add(int(i[1]))
    elif i[0] == 'remove':
        S.discard(int(i[1]))
    elif i[0] == 'check':
        print(1 if int(i[1]) in S else 0)
    elif i[0] == 'toggle':
       S.add(int(i[1])) if int(i[1]) not in S else S.discard(int(i[1]))

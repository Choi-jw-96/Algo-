import sys
N, M, B = map(int,input().split())
block = []
for _ in range(N):
    block.append([int(x) for x in sys.stdin.readline().rstrip().split()])

ans = int(1e9)
glevel = 0

for i in range(257): #땅 높이
    block1 = 0
    block2 = 0
    for x in range(N):
        for y in range(M):
            if block[x][y] > i:
                block2 += block[x][y] - i
            else:
                block1 += i - block[x][y]

   

    count = block2 * 2 + block1

    